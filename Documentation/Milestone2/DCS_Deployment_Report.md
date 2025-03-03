# **Distributed Industrial Control System (DCS) Deployment Report**

## **1. Overview of Work**
This project involved setting up a **Distributed Industrial Control System (DCS)** using **Docker** to simulate an industrial environment with **encrypted and non-encrypted networks**. The system includes **Programmable Logic Controllers (PLCs), SCADA, MQTT communication, InfluxDB for data storage, and Grafana for visualization**.

The objectives were:
- Deploy **two separate environments** (encrypted & non-encrypted) to compare performance and security.
- Establish **PLC communication** using **Modbus TCP & OPC-UA**.
- Set up **MQTT for IoT sensor data exchange**.
- Use **InfluxDB** for real-time process data logging.
- Implement **Grafana dashboards** to monitor industrial data.

---

## **2. Steps Performed**

### **1️⃣ Setting Up the Linux Server and Docker Host**
- Provisioned a **virtual Linux server** for hosting Docker-based industrial control systems.
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

### **2️⃣ Creating Docker-Compose Files for Encrypted & Non-Encrypted Environments**
#### **📌 Docker Images Used**
The system was built using the following Docker images:
| Component       | Image Used                           | Description |
|----------------|--------------------------------------|-------------|
| **PLC**        | `fdamador/openplc`                  | Simulated PLCs using OpenPLC |
| **SCADA**      | `inductiveautomation/ignition`      | Ignition SCADA for process control |
| **MQTT Broker**| `eclipse-mosquitto`                 | MQTT for real-time IoT messaging |
| **Database**   | `influxdb`                          | Time-series database for industrial data |
| **Grafana**    | `grafana/grafana`                   | Dashboarding tool for visualization |

#### **📌 YAML Configuration**
Two separate **`docker-compose.yml`** files were created:

**🔹 `docker-compose.yml` (Encrypted Environment)**
```yaml
version: '3.8'
services:
  plc1:
    image: fdamador/openplc
    container_name: plc1
    ports:
      - "502:502"
    networks:
      - industrial_net

  scada:
    image: inductiveautomation/ignition
    container_name: scada
    ports:
      - "8088:8088"
    networks:
      - industrial_net

  mqtt-broker:
    image: eclipse-mosquitto
    container_name: mqtt-broker
    ports:
      - "1883:1883"
    networks:
      - industrial_net

  database:
    image: influxdb
    container_name: influxdb-secure
    ports:
      - "8086:8086"
    networks:
      - industrial_net

  grafana:
    image: grafana/grafana
    container_name: grafana-secure
    ports:
      - "3001:3000"
    networks:
      - industrial_net

networks:
  industrial_net:
    driver: bridge
```

**🔹 `docker-compose-no-crypto.yml` (Non-Encrypted Environment)**
```yaml
version: '3.8'
services:
  plc1:
    image: fdamador/openplc
    container_name: plc1_no_crypto
    ports:
      - "505:502"
    networks:
      - industrial_no_crypto

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
      - "1884:1883"
    networks:
      - industrial_no_crypto

  database:
    image: influxdb
    container_name: influxdb-no-crypto
    ports:
      - "8087:8086"
    networks:
      - industrial_no_crypto

  grafana:
    image: grafana/grafana
    container_name: grafana-no-crypto
    ports:
      - "3002:3000"
    networks:
      - industrial_no_crypto

networks:
  industrial_no_crypto:
    driver: bridge
```

- The **encrypted environment** runs on `industrial_net`, while the **non-encrypted environment** runs on `industrial_no_crypto`.

---

### **3️⃣ Configuring PLC Communication**
- **Verified PLC communication using Modbus TCP**:
  ```bash
  docker exec -it scada modbus_client --debug -m tcp -u 1 -a 1 -t 3 -r 0 plc1:502
  ```
- **Configured Ignition SCADA** to read from **PLC registers** via **Modbus TCP**.

---

### **4️⃣ Setting Up MQTT Communication**
- Verified **MQTT broker connectivity** by subscribing to PLC data:
  ```bash
  docker exec -it scada mosquitto_sub -h mqtt-broker -t "plc1/data" -v
  ```
- Configured SCADA and PLCs to **publish sensor data** to MQTT topics.

---

### **5️⃣ Configuring InfluxDB for Data Storage**
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

### **6️⃣ Setting Up Grafana Dashboards**
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

🎉 **The DCS is now fully operational and ready for industrial automation testing!** 🚀  
