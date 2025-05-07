# Simulation and Data Gathering

## Unencrypted Environment
```python
import paho.mqtt.client as mqtt
import random
import time
import json
import requests
import socket
from influxdb_client import InfluxDBClient, Point, WritePrecision

# MQTT Broker Details
MQTT_BROKER = "mqtt-broker-no-crypto"  # Use hostname instead of IP
MQTT_PORT = 1883
MQTT_TOPIC = "dcs/plc/data"

# InfluxDB
INFLUXDB_URL = "http://influxdb-no-crypto:8086"
INFLUXDB_TOKEN = "TOEKN_OMITTED"  # InfluxDB token
INFLUXDB_ORG = "my-org"  # The InfluxDB organization name
INFLUXDB_BUCKET = "plc_data"  # The target bucket

# Create InfluxDB client using the token-based authentication
influx_client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)

write_api = influx_client.write_api()

# Retry logic for MQTT connection
def connect_mqtt(client):
    while True:
        try:
            client.connect(MQTT_BROKER, MQTT_PORT, 60)
            print("Connected to MQTT Broker")
            return
        except socket.error as e:
            print(f"[MQTT] Connection failed: {e}. Retrying in 5 seconds...")
            time.sleep(5)

def generate_plc_data(plc_id):
    return {
        "plc_id": plc_id,
        "temperature": round(random.uniform(20, 100), 2),
        "pressure": round(random.uniform(1, 10), 2),
        "flow_rate": round(random.uniform(5, 50), 2),
        "timestamp": int(time.time())
    }
# This is a partial copy of the script. The full script can be found at <script location>.
```
## Encrypted Environment
```python
import paho.mqtt.client as mqtt
import random
import time
import json
import requests
import socket
from influxdb_client import InfluxDBClient, Point, WritePrecision

# MQTT Broker Details
MQTT_BROKER = "mqtt-broker"  # Updated for encrypted environment
MQTT_PORT = 8883
MQTT_TOPIC = "dcs/plc/data"

# InfluxDB
INFLUXDB_URL = "https://influxdb-secure:8097"
INFLUXDB_TOKEN = "TOKEN_OMITTED"  # InfluxDB token
INFLUXDB_ORG = "my-org"  # The InfluxDB organization name
INFLUXDB_BUCKET = "plc_data"  # The target bucket

# Create InfluxDB client using the token-based authentication
influx_client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)

write_api = influx_client.write_api()

# Retry logic for MQTT connection
def connect_mqtt(client):
    while True:
        try:
            client.connect(MQTT_BROKER, MQTT_PORT, 60)
            print("Connected to MQTT Broker")
            return
        except socket.error as e:
            print(f"[MQTT] Connection failed: {e}. Retrying in 5 seconds...")
            time.sleep(5)

def generate_plc_data(plc_id):
    return {
        "plc_id": plc_id,
        "temperature": round(random.uniform(20, 100), 2),
        "pressure": round(random.uniform(1, 10), 2),
        "flow_rate": round(random.uniform(5, 50), 2),
        "timestamp": int(time.time())
    }
# This is a partial copy of the script. The full script can be found at <script location>.
```

## Blockchain/Fingerprinting Environment
