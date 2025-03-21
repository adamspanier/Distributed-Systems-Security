# **Distributed Industrial Control System (DCS) Deployment Report**

## **1. Overview of Work**
This project involved setting up a Distributed Industrial Control System (DCS) using Docker to simulate an industrial environment with encrypted and non-encrypted networks. The system includes Programmable Logic Controllers (PLCs), SCADA, MQTT communication, InfluxDB for data storage, and Grafana for visualization.

The objectives were:
- Deploy two separate environments (encrypted & non-encrypted) to compare performance and security.
- Establish PLC communication using Modbus TCP & OPC-UA.
- Set up MQTT for IoT sensor data exchange.
- Use InfluxDB for real-time process data logging.
- Implement Grafana dashboards to monitor industrial data.

---

## **2. Steps Performed**

### **2.1 Setting Up the Linux Server and Docker Host**
- Provisioned a virtual Linux server for hosting Docker-based industrial control systems.
- Installed required dependencies:
  ```bash
  sudo apt update && sudo apt install -y docker.io docker-compose net-tools
  ```
- Verified Docker installation:
  ```bash
  docker --version
  docker-compose --version
  ```

---

### **2.2 Creating Docker-Compose Files for Encrypted & Non-Encrypted Environments**
#### **Docker Images Used**
The system was built using the following Docker images:
| Component      | Image Used                          | Description |
|----------------|-------------------------------------|-------------|
| **PLC**        | `openplc`                           | Simulated PLCs using OpenPLC |
| **SCADA**      | `inductiveautomation/ignition`      | Ignition SCADA for process control |
| **MQTT Broker**| `eclipse-mosquitto`                 | MQTT for real-time IoT messaging |
| **Database**   | `influxdb`                          | Time-series database for industrial data |
| **Grafana**    | `grafana/grafana`                   | Dashboarding tool for visualization |
| **WireGuard**  | `linuxserver/wireguard`             | PLC-to-PLC encrypted communication (VPN) |
| **Stunnel**    | `dweomer/stunnel`                   | Encrypts traffic between two hosts |
| **Open62541**  | `open62541/open62541`               | OPC UA Communication Between PLCs and SCADA |

#### **YAML Configuration**
Two separate **`docker-compose.yml`** files were created:

**`docker-compose-crypto.yml` (Encrypted Environment)**
```yaml
version: '3.8'

services:
  plc1:
    image: openplc:v3
    container_name: plc1
    privileged: true
    ports:
      - "5502:5502"   # Encrypted Modbus TCP over TLS
      - "8084:8080"   # Webserver
    networks:
      - industrial_net
    depends_on:
      - modbus-tls
    environment:
      - MODBUS_SECURE=true
      - MODBUS_PORT=5502  # Ensure Modbus listens on the correct port

  plc2:
    image: openplc:v3
    container_name: plc2
    privileged: true
    ports:
      - "5503:5502"
      - "8085:8080"
    networks:
      - industrial_net
    depends_on:
      - modbus-tls
    environment:
      - MODBUS_SECURE=true
      - MODBUS_PORT=5503

  plc3:
    image: openplc:v3
    container_name: plc3
    privileged: true
    ports:
      - "5504:5502"
      - "8086:8080"
    networks:
      - industrial_net
    depends_on:
      - modbus-tls
    environment:
      - MODBUS_SECURE=true
      - MODBUS_PORT=5504

  modbus-tls:
    image: dweomer/stunnel
    container_name: modbus-tls
    privileged: true  # <-- Add this to allow volume access
    environment:
      - STUNNEL_SERVICE=modbus-tls
      - STUNNEL_ACCEPT=8502   # Port where encrypted Modbus traffic is received
      - STUNNEL_CONNECT=plc1:502  # Forward traffic to unencrypted PLC port
    ports:
      - "9502:8502"
    volumes:
      - /root/Capstone/stunnel.conf:/etc/stunnel/stunnel.conf
      - /root/Capstone/certs/stunnel.pem:/etc/stunnel/stunnel.pem
      - /root/Capstone/certs/stunnel.key:/etc/stunnel/stunnel.key
      - /root/Capstone/certs/ca-cert-stunnel-ca.pem:/etc/stunnel/ca-cert-stunnel-ca.pem
    networks:
      - industrial_net
    restart: always

  scada:
    image: inductiveautomation/ignition
    container_name: scada
    ports:
      - "8088:8088"
    networks:
      - industrial_net
    depends_on:
      - opc-ua
    environment:
      - OPCUA_SECURE=true

  mqtt-broker:
    image: eclipse-mosquitto
    container_name: mqtt-broker
    ports:
      - "8883:8883"  # Encrypted MQTT over TLS
    volumes:
      - ./mosquitto/mosquitto.conf:/mosquitto/config/mosquitto.conf
      - ./mosquitto/config/certs:/mosquitto/config/certs
    networks:
      - industrial_net
    command: ["sh", "-c", "apk add --no-cache iputils net-tools && mosquitto -c /mosquitto/config/mosquitto.conf"]

  database:
    image: influxdb
    container_name: influxdb-secure
    networks:
      - industrial_net
    environment:
      - INFLUXD_HTTP_HTTPS_ENABLED=true
      - INFLUXD_HTTP_CERTIFICATE=/etc/ssl/influxdb.pem
      - INFLUXD_HTTP_PRIVATE_KEY=/etc/ssl/influxdb.key
      - INFLUXD_HTTP_BIND_ADDRESS=:8097
      - DOCKER_INFLUXDB_INIT_MODE=setup
      - DOCKER_INFLUXDB_INIT_USERNAME=admin
      - DOCKER_INFLUXDB_INIT_PASSWORD=admin123
      - DOCKER_INFLUXDB_INIT_ORG=my-org-secure
      - DOCKER_INFLUXDB_INIT_BUCKET=plc_data
      - DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=${INFLUX_SECURE_TOKEN}
    ports:
      - "8097:8097"
    volumes:
      - /root/Capstone/influxdb/influxdb.conf:/etc/influxdb/influxdb.conf:ro
      - /root/Capstone/certs:/etc/ssl:ro
      - influxdb-data:/var/lib/influxdb2  # Persist database data and auth tokens
    command: ["influxd", "--tls-cert", "/etc/ssl/influxdb.pem", "--tls-key", "/etc/ssl/influxdb.key", "--http-bind-address=:8097"]

  opc-ua:
    image: open62541/open62541
    container_name: opc-ua
    networks:
      - industrial_net
    environment:
      - OPCUA_SERVER_SECURITY_MODE=SignAndEncrypt
      - OPCUA_SERVER_CERTIFICATE=/etc/opc-ua/cert.pem
      - OPCUA_SERVER_PRIVATE_KEY=/etc/opc-ua/private_key.pem
    volumes:
      - ./certs:/etc/opc-ua

  vpn:
    image: linuxserver/wireguard
    container_name: vpn
    cap_add:
      - NET_ADMIN
      - SYS_MODULE
    networks:
      - industrial_net
    environment:
      - PUID=1000
      - PGID=1000
      - SERVERPORT=51820
      - PEERS=3
    volumes:
      - ./vpn:/config

  grafana-secure:
    image: grafana/grafana
    container_name: grafana-secure
    restart: always
    ports:
      - "3001:3000"
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=admin
    depends_on:
      - database
    networks:
      - industrial_net
    user: "472:472"  # Run as Grafana user
    volumes:
      - ./grafana-secure:/var/lib/grafana
    command: ["bash", "-c", "apt update && apt install -y iputils-ping net-tools && /run.sh"]

networks:
  industrial_net:
    driver: bridge

volumes:
  influxdb-data:  # Persistent storage for InfluxDB
```

**`docker-compose-no-crypto.yml` (Non-Encrypted Environment)**
```yaml
version: '3.8'

services:
  plc1:
    image: openplc:v3
    container_name: plc1_no_crypto
    privileged: true
    ports:
      - "8081:8080"  # Webserver
      - "1502:502"   # Modbus TCP
    networks:
      - industrial_no_crypto
    restart: "no"

  plc2:
    image: openplc:v3
    container_name: plc2_no_crypto
    privileged: true
    ports:
      - "8082:8080"  # Webserver
      - "1503:502"   # Modbus TCP
    networks:
      - industrial_no_crypto
    restart: "no"

  plc3:
    image: openplc:v3
    container_name: plc3_no_crypto
    privileged: true
    ports:
      - "8083:8080"  # Webserver
      - "1504:502"   # Modbus TCP
    networks:
      - industrial_no_crypto
    restart: "no"

  scada:
    image: inductiveautomation/ignition
    container_name: scada-no-crypto
    ports:
      - "8090:8088"
    networks:
      - industrial_no_crypto

  mqtt-broker:
    image: eclipse-mosquitto
    container_name: mqtt-broker-no-crypto
    ports:
      - "1883:1883"  # MQTT (Unsecured)
    networks:
      - industrial_no_crypto
    command: ["sh", "-c", "apk add --no-cache iputils net-tools && mosquitto -c /mosquitto/config/mosquitto.conf"]

  database:
    image: influxdb
    container_name: influxdb-no-crypto
    networks:
      - industrial_no_crypto
    environment:
      - INFLUXDB_DB=plc_data
    ports:
      - "8087:8086"  # Non-encrypted InfluxDB listens on host port 8087
    volumes:
      - /root/Capstone/influxdb-no-crypto:/var/lib/influxdb2  # Fix path for InfluxDB v2
    command: ["bash", "-c", "apt update && apt install -y iputils-ping net-tools && influxd"]

  grafana-no-crypto:
    image: grafana/grafana
    container_name: grafana-no-crypto
    restart: always
    ports:
      - "3002:3000"
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=admin
    depends_on:
      - database
    networks:
      - industrial_no_crypto
    user: "472:472"  # Run as Grafana user
    volumes:
      - ./grafana-no-crypto:/var/lib/grafana
    command: ["bash", "-c", "apt update && apt install -y iputils-ping net-tools && /run.sh"]

networks:
  industrial_no_crypto:
    driver: bridge
```

- The **encrypted environment** runs on `industrial_net`, while the **non-encrypted environment** runs on `industrial_no_crypto`.

---

### **2.3 Configuring PLC Communication**
- **Verified PLC communication using Modbus TCP**:
  ```bash
  docker exec -it scada modbus_client --debug -m tcp -u 1 -a 1 -t 3 -r 0 plc1:502
  ```
- **Configured Ignition SCADA** to read from **PLC registers** via **Modbus TCP**.

---

### **2.4 Setting Up MQTT Communication**
- Verified **MQTT broker connectivity** by subscribing to PLC data:
  ```bash
  docker exec -it scada mosquitto_sub -h mqtt-broker -t "plc1/data" -v
  ```
- Configured SCADA and PLCs to **publish sensor data** to MQTT topics.

---

### **2.5 Configuring InfluxDB for Data Storage**
- **Checked if InfluxDB is running:**
  ```bash
  docker ps | grep influxdb
  ```
- **Verified database connection:**
  ```bash
  curl -I http://localhost:8086/health
  ```
- **Queried Modbus register data stored in InfluxDB:**
  ```sql
  SELECT * FROM modbus_registers LIMIT 10;
  ```

---

### **2.6 Setting Up Grafana Dashboards**
- **Two Grafana instances** were deployed:
  - **Secure:** `http://<server-ip>:3001`
  - **Non-Secure:** `http://<server-ip>:3002`
- **Added InfluxDB Data Sources** with **Token Authentication**.
- **Created dashboards** to visualize:
  - **Live PLC sensor values**
  - **Historical trends**
  - **IoT data from MQTT**

---

## **3. Summary**
✔ **Deployed a Docker-based DCS with encrypted & non-encrypted environments.**  
✔ **Configured PLCs to communicate via Modbus TCP & OPC-UA.**  
✔ **Implemented MQTT messaging for real-time sensor data exchange.**  
✔ **Set up InfluxDB for industrial process data logging.**  
✔ **Created Grafana dashboards for live monitoring & historical analysis.**
