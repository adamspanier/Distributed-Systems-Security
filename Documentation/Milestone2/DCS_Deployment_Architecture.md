# DCS Environment Architecture Summary

## Non-Secure Environment (No-Crypto)

**Communication Overview**
* PLCs periodically publish data to MQTT broker.
* SCADA polls PLCs over Modbus TCP.
* SCADA and MQTT forward data to InfluxDB.
* Grafana queries InfluxDB to visualize historical trends.

**Network:** `no_crypto_env_industrial_no_crypto`  
**Subnet:** `172.18.0.0/16`

| Component            | Container Name        | IP Address     | Port Mappings                   |
|---------------------|------------------------|----------------|----------------------------------|
| PLC1                | plc1_no_crypto         | 172.18.0.2     | 1502:502, 8081:8080              |
| PLC2                | plc2_no_crypto         | 172.18.0.6     | 1503:502, 8082:8080              |
| PLC3                | plc3_no_crypto         | 172.18.0.7     | 1504:502, 8083:8080              |
| MQTT Broker         | mqtt-broker-no-crypto  | 172.18.0.4     | 1883:1883                        |
| InfluxDB            | influxdb-no-crypto     | 172.18.0.3     | 8087:8086                        |
| Grafana             | grafana-no-crypto      | 172.18.0.8     | 3002:3000                        |
| SCADA               | scada-no-crypto        | 172.18.0.5     | 8090:8088                        |

**Non-Secure Environment Diagram**

![image](https://github.com/user-attachments/assets/ba349bd0-9962-4bc6-bd23-e0b2129a7bab)

---

## Secure Environment

**Secure Communication Overview**
* PLCs are accessed using TLS over port 550X.
* All MQTT communications are encrypted via port 8883.
* InfluxDB runs behind HTTPS (TLS), port 8097.
* SCADA polls PLCs over secure TLS Modbus.
* Data storage and visualization handled via InfluxDB + Grafana (secured).

**Network:** `encrypted_env_industrial_net`  
**Subnet:** `172.19.0.0/16`

| Component            | Container Name    | IP Address     | Port Mappings                     |
|---------------------|-------------------|----------------|------------------------------------|
| PLC1                | plc1              | 172.19.0.10    | 5502:5502, 8084:8080               |
| PLC2                | plc2              | 172.19.0.8     | 5503:5502, 8085:8080               |
| PLC3                | plc3              | 172.19.0.11    | 5504:5502, 8086:8080               |
| MQTT Broker         | mqtt-broker       | 172.19.0.6     | 8883:8883 (TLS)                    |
| InfluxDB (Secure)   | influxdb-secure   | 172.19.0.4     | 8097:8097 (HTTPS)                  |
| Grafana (Secure)    | grafana-secure    | 172.19.0.9     | 3001:3000                          |
| SCADA               | scada             | 172.19.0.7     | 8088:8088                          |
| Modbus-TLS Gateway  | modbus-tls        | 172.19.0.2     | 9502:8502                          |
| VPN Gateway         | vpn               | 172.19.0.5     | 51820:51820/udp                    |
| OPC-UA Server       | opc-ua            | 172.19.0.3     | 4840:4840                          |

**Secure Environment Diagram**

![image](https://github.com/user-attachments/assets/535a0ab6-4f2d-415f-84e3-465a34afd2e9)
