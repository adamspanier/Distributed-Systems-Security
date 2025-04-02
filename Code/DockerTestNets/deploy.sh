#!/bin/bash

echo "🚀 Stopping all running containers..."
docker stop $(docker ps -aq) 2>/dev/null
docker rm $(docker ps -aq) 2>/dev/null

echo "📌 Taking down existing Docker Compose environments..."
docker-compose -f docker-compose-no-crypto.yml down
docker-compose -f docker-compose-crypto.yml down

echo "🛑 Removing all networks..."
docker network prune -f
existing_networks=$(docker network ls | grep -E "no_crypto|encrypted_env" | awk '{print $1}')
if [[ -n "$existing_networks" ]]; then
    echo "Removing networks: $existing_networks"
    echo "$existing_networks" | xargs docker network rm
else
    echo "No networks found to remove."
fi

echo "🗑  Removing stale Docker volumes..."
docker volume prune -f

echo "🧹 Ensuring ports are freed..."
sudo fuser -k 8081/tcp 2>/dev/null
sudo fuser -k 8082/tcp 2>/dev/null
sudo fuser -k 8083/tcp 2>/dev/null
sudo fuser -k 502/tcp 2>/dev/null
sudo fuser -k 5502/tcp 2>/dev/null
sudo fuser -k 5503/tcp 2>/dev/null
sudo fuser -k 5504/tcp 2>/dev/null

echo "⬇️ Pulling latest images..."
docker-compose build --no-cache

echo "🚀 Starting Docker Compose environments..."
docker-compose -p no_crypto_env -f docker-compose-no-crypto.yml up -d
docker-compose -p encrypted_env -f docker-compose-crypto.yml up -d

# Function to retrieve a valid InfluxDB token
get_influx_token() {
    TOKEN=$(docker exec influxdb-no-crypto influx auth list --json 2>/dev/null | jq -r '.[] | select(.description=="Super Admin Token") | .token')
    if [[ -n "$TOKEN" && "$TOKEN" != "null" ]]; then
        echo "$TOKEN"
    else
        echo ""
    fi
}

echo "🛠  Setting up InfluxDB..."
sleep 5  # Allow time for InfluxDB to initialize

# Ensure InfluxDB is running
MAX_RETRIES=10
RETRY_COUNT=0
while ! docker exec influxdb-no-crypto influx ping &>/dev/null; do
    echo "⏳ Waiting for InfluxDB to start..."
    sleep 3
    ((RETRY_COUNT++))
    if [[ $RETRY_COUNT -eq $MAX_RETRIES ]]; then
        echo "❌ ERROR: InfluxDB failed to start!"
        exit 1
    fi
done

# Retrieve or validate the existing token
if [[ -f influx_token.txt && -s influx_token.txt ]]; then
    EXISTING_TOKEN=$(cat influx_token.txt)

    # Validate token
    if docker exec influxdb-no-crypto influx org list --token "$EXISTING_TOKEN" &>/dev/null; then
        echo "✅ Using existing valid InfluxDB token."
        export INFLUX_TOKEN="$EXISTING_TOKEN"
    else
        echo "⚠️ Invalid token found. Removing and setting up InfluxDB again..."
        rm -f influx_token.txt
    fi
fi

# If no valid token, set up InfluxDB
if [[ ! -f influx_token.txt || ! -s influx_token.txt ]]; then
    echo "⚠️ InfluxDB requires setup. Running setup now..."

    # Setup InfluxDB if not already initialized
    docker exec influxdb-no-crypto influx setup --username admin --password admin123 --org my-org --bucket plc_data --retention 0 --force || echo "⚠️ InfluxDB setup may already exist."

    # Attempt to retrieve the token again
    INFLUX_TOKEN=$(get_influx_token)

    # If token retrieval fails, manually create a new token with all-access
    if [[ -z "$INFLUX_TOKEN" ]]; then
        echo "🔄 Creating a new authentication token..."
        INFLUX_TOKEN=$(docker exec influxdb-no-crypto influx auth create \
          --user admin \
          --all-access \
          --description "Super Admin Token" | awk 'NR==2 {print $3}')
    fi

    # Validate and save the token
    if [[ -n "$INFLUX_TOKEN" && "$INFLUX_TOKEN" != "null" ]]; then
        echo "$INFLUX_TOKEN" > influx_token.txt
        echo "✅ InfluxDB setup complete. Token saved."

        # Also update .bashrc to persist the secure token
        sed -i '/export INFLUX_TOKEN/d' ~/.bashrc
        echo "export INFLUX_TOKEN=$(cat influx_token.txt)" >> ~/.bashrc
        source ~/.bashrc
    else
        echo "❌ ERROR: Failed to retrieve the Secure InfluxDB token! Check Secure InfluxDB logs."
        exit 1
    fi
fi

# Ensure InfluxDB CLI uses the correct token
export INFLUX_TOKEN=$(cat influx_token.txt)
docker exec influxdb-no-crypto influx config create \
  --config-name default \
  --host-url http://localhost:8086 \
  --org my-org \
  --token "$INFLUX_TOKEN" \
  --active || echo "⚠️ Warning: Config may already exist."

echo "🛠   Setting up Secure InfluxDB..."
sleep 5  # Allow time for Secure InfluxDB to initialize

# Ensure Secure InfluxDB is running before setup
MAX_RETRIES=10
RETRY_COUNT=0
while ! curl -ks https://localhost:8097/health &>/dev/null; do
    echo "⏳ Waiting for Secure InfluxDB to start..."
    sleep 3
    ((RETRY_COUNT++))
    if [[ $RETRY_COUNT -eq $MAX_RETRIES ]]; then
        echo "❌ ERROR: Secure InfluxDB failed to start!"
        exit 1
    fi
done

# 🔹 Retrieve the stored token instead of recreating it
if [[ -f influx_secure_token.txt && -s influx_secure_token.txt ]]; then
    INFLUX_SECURE_TOKEN=$(cat influx_secure_token.txt)
else
    INFLUX_SECURE_TOKEN=""
fi

# 🔹 Validate the stored token
if [[ -n "$INFLUX_SECURE_TOKEN" ]]; then
    echo "🔍 Checking if Secure InfluxDB token is valid..."
    if docker exec influxdb-secure influx org list \
      --host https://localhost:8097 \
      --token "$INFLUX_SECURE_TOKEN" \
      --skip-verify &>/dev/null; then
        echo "✅ Using existing valid Secure InfluxDB token."
    else
        echo "⚠️ WARNING: Secure token validation failed. Removing and reconfiguring Secure InfluxDB..."
        rm -f influx_secure_token.txt
        INFLUX_SECURE_TOKEN=""
    fi
fi

# 🔹 If token is still empty, reinitialize InfluxDB
if [[ -z "$INFLUX_SECURE_TOKEN" ]]; then
    echo "⚠️ Secure InfluxDB requires setup. Running setup now..."

    # Run Secure InfluxDB setup
    docker exec -i influxdb-secure influx setup \
      --host https://localhost:8097 \
      --skip-verify \
      --username admin \
      --password admin123 \
      --org my-org-secure \
      --bucket plc_data \
      --force \
      --name secure-config

    # 🔹 Retrieve the newly generated Secure InfluxDB token
    INFLUX_SECURE_TOKEN=$(docker exec influxdb-secure influx auth list \
      --host https://localhost:8097 \
      --skip-verify --json | jq -r '.[] | select(.description == "admin'\''s Token") | .token')

    # 🔹 Save the token for later use
    if [[ -n "$INFLUX_SECURE_TOKEN" && "$INFLUX_SECURE_TOKEN" != "null" ]]; then
        echo "$INFLUX_SECURE_TOKEN" > influx_secure_token.txt
        echo "✅ Secure InfluxDB setup complete. Token saved."
    else
        echo "❌ ERROR: Failed to retrieve Secure InfluxDB token!"
        exit 1
    fi
fi

# 🔹 Configure CLI with the secure token
docker exec influxdb-secure influx config create \
  --config-name secure-default \
  --host-url https://localhost:8097 \
  --org my-org-secure \
  --token "$INFLUX_SECURE_TOKEN" \
  --active --configs-path /etc/influxdb2/influx-configs || echo "⚠️ Warning: Secure config may already exist."

echo "✅ Secure InfluxDB deployment complete."
echo "✅ All containers should now be running!"

