# Data Gathered During Testing

## Unencrypted Environment - Security and Vulnerability Test
The unencrypted environment (172.18.0.0/16) showed several security issues:

- **PLC1**:
  - Network Availability: PASS (IP: 172.18.0.8)
  - Port Accessibility: PASS (Expected: [502, 8080], Open: [502, 8080])
  - Modbus Security: SKIP (pymodbus library not installed)
  - Password Security: FAIL (Possible successful login with admin:admin)

- **PLC2**:
  - Network Availability: PASS (IP: 172.18.0.2)
  - Port Accessibility: FAIL (Expected: [502, 8080], Open: [])
  - Modbus Security: SKIP (Port not available)
  - Password Security: PASS (Basic password brute force attempt failed)

- **PLC3**:
  - Network Availability: PASS (IP: 172.18.0.7)
  - Port Accessibility: FAIL (Expected: [502, 8080], Open: [])
  - Modbus Security: SKIP (Port not available)
  - Password Security: PASS (Basic password brute force attempt failed)

- **MQTT_Broker**:
  - Network Availability: PASS (IP: 172.18.0.4)
  - Port Accessibility: FAIL (Expected: [1883], Open: [])
  - MQTT Security: SKIP (Port not available)

- **InfluxDB**:
  - Network Availability: PASS (IP: 172.18.0.5)
  - Port Accessibility: FAIL (Expected: [8086], Open: [])
  - Authentication: PASS (Query databases without auth failed: 000)
  - Password Security: PASS (Basic password brute force attempt failed)

- **Grafana**:
  - Network Availability: PASS (IP: 172.18.0.9)
  - Port Accessibility: PASS (Expected: [3000], Open: [3000])
  - Default Credentials: PASS (Default admin/admin credentials rejected)
  - API Exposure: INFO (Health API endpoint accessible)
  - Password Security: PASS (Basic password brute force attempt failed)

- **SCADA**:
  - Network Availability: PASS (IP: 172.18.0.3)
  - Port Accessibility: FAIL (Expected: [8088], Open: [])
  - Password Security: PASS (Basic password brute force attempt failed)

- **Network**:
  - Network Segmentation: PASS (All expected devices found: 7/7)
  - Vulnerability Scan: INFO (Scan completed on 7 IPs. Results in /tmp/nmap_vuln_results.xml)

## Encrypted Environment - Security and Vulnerability Test
The encrypted environment (172.19.0.0/16) revealed these findings:

### Summary
- Pass: 13
- Warn: 3
- Fail: 14
- Info: 4
- Skip: 4
- Total: 38

### Components

- **PLC1**:
  - Network Availability: PASS (IP: 172.19.0.10)
  - TCP Port Accessibility: FAIL (Expected: [5502, 8080], Open: [8080])
  - Modbus Security: SKIP (Port not available)

- **PLC2**:
  - Network Availability: PASS (IP: 172.19.0.11)
  - TCP Port Accessibility: PASS (Expected: [5502, 8080], Open: [5502, 8080])
  - TLS Support: FAIL (TLS not supported or connection failed)
  - Modbus Security: SKIP (pymodbus library not installed)

- **PLC3**:
  - Network Availability: PASS (IP: 172.19.0.8)
  - TCP Port Accessibility: FAIL (Expected: [5502, 8080], Open: [])
  - Modbus Security: SKIP (Port not available)

- **MQTT_Broker**:
  - Network Availability: PASS (IP: 172.19.0.6)
  - TCP Port Accessibility: FAIL (Expected: [8883], Open: [])
  - Connectivity: FAIL (TLS port not accessible)

- **InfluxDB**:
  - Network Availability: PASS (IP: 172.19.0.5)
  - TCP Port Accessibility: FAIL (Expected: [8097], Open: [])
  - TLS Support: FAIL (TLS not supported or connection failed)
  - Authentication: INFO (Query response: 000)
  - Authentication Headers: WARN (No WWW-Authenticate header found)

- **Grafana**:
  - Network Availability: PASS (IP: 172.19.0.9)
  - TCP Port Accessibility: FAIL (Expected: [3000], Open: [])
  - Default Credentials: PASS (Default admin/admin credentials rejected)
  - Security Headers: WARN (Missing security headers: X-Content-Type-Options, X-XSS-Protection, Content-Security-Policy, Strict-Transport-Security)

- **SCADA**:
  - Network Availability: PASS (IP: 172.19.0.7)
  - TCP Port Accessibility: FAIL (Expected: [8088], Open: [])

- **Modbus_TLS_Gateway**:
  - Network Availability: PASS (IP: 172.19.0.4)
  - TCP Port Accessibility: FAIL (Expected: [8502], Open: [])
  - Connectivity: FAIL (Port not accessible)

- **VPN_Gateway**:
  - Network Availability: PASS (IP: 172.19.0.3)
  - UDP Port Accessibility: FAIL (Expected: [51820], Open: [])
  - UDP Port: WARN (VPN port 51820 not reachable in scan)
  - Configuration Check: SKIP (Skipping configuration checks in containerized environment)

- **OPC_UA_Server**:
  - Network Availability: PASS (IP: 172.19.0.2)
  - TCP Port Accessibility: FAIL (Expected: [4840], Open: [])
  - Connectivity: FAIL (Port not accessible)

- **Network**:
  - Network Segmentation: PASS (All expected devices found: 10/10)
  - Network Segmentation: INFO (Skipping full subnet scan for unexpected devices)
  - Vulnerability Scan: INFO (Performing limited version detection instead of full vulnerability scan)
  - Version Detection: INFO (Scan completed on 10 IPs. Results in /tmp/nmap_version_results.xml)

### Critical Findings
1. PLC1: TCP Port Accessibility - Expected: [5502, 8080], Open: [8080]
2. PLC2: TLS Support - TLS not supported or connection failed
3. PLC3: TCP Port Accessibility - Expected: [5502, 8080], Open: []
4. MQTT_Broker: TCP Port Accessibility - Expected: [8883], Open: []
5. MQTT_Broker: Connectivity - TLS port not accessible
6. InfluxDB: TCP Port Accessibility - Expected: [8097], Open: []
7. InfluxDB: TLS Support - TLS not supported or connection failed
8. Grafana: TCP Port Accessibility - Expected: [3000], Open: []
9. SCADA: TCP Port Accessibility - Expected: [8088], Open: []
10. Modbus_TLS_Gateway: TCP Port Accessibility - Expected: [8502], Open: []
11. Modbus_TLS_Gateway: Connectivity - Port not accessible
12. VPN_Gateway: UDP Port Accessibility - Expected: [51820], Open: []
13. OPC_UA_Server: TCP Port Accessibility - Expected: [4840], Open: []
14. OPC_UA_Server: Connectivity - Port not accessible

## Blockchain/Fingerprinting Environment - Security and Vulnerability Test
The blockchain/fingerprinting environment (172.20.0.0/16) testing revealed:

### Dependencies Check
- Found nmap: /usr/bin/nmap
- Found openssl: /usr/bin/openssl
- Found curl: /usr/bin/curl
- pymodbus, paho-mqtt, and pycomm3 are installed

### Component Test Results

- **PLC1**:
  - Network Availability: PASS (IP: 172.20.0.9)
  - TCP Port Accessibility: FAIL (Expected: [502, 44818], Open: [502])
  - Modbus Security: INFO (pymodbus library not installed)
  - EtherNet/IP Security: INFO (Port not available)

- **PLC2**:
  - Network Availability: PASS (IP: 172.20.0.5)
  - TCP Port Accessibility: FAIL (Expected: [502, 44818], Open: [502])
  - Modbus Security: INFO (pymodbus library not installed)
  - EtherNet/IP Security: INFO (Port not available)

- **PLC3**:
  - Network Availability: PASS (IP: 172.20.0.6)
  - TCP Port Accessibility: FAIL (Expected: [502, 44818], Open: [502])
  - Modbus Security: INFO (pymodbus library not installed)
  - EtherNet/IP Security: INFO (Port not available)

- **MQTT_Broker**:
  - Network Availability: PASS (IP: 172.20.0.8)
  - TCP Port Accessibility: FAIL (Expected: [1883, 8883], Open: [])
  - Connectivity: FAIL (MQTT ports not accessible)

- **InfluxDB**:
  - Network Availability: PASS (IP: 172.20.0.7)
  - TCP Port Accessibility: PASS (Expected: [8086], Open: [8086])
  - API Accessibility: INFO (InfluxDB ping endpoint accessible)
  - Authentication: PASS (Authentication required for queries)
  - Authentication Headers: WARN (No WWW-Authenticate header found)

- **Grafana**:
  - Network Availability: PASS (IP: 172.20.0.11)
  - TCP Port Accessibility: PASS (Expected: [3000], Open: [3000])
  - HTTPS: FAIL (Grafana does not use HTTPS)
  - Default Credentials: PASS (Default admin/admin credentials rejected)
  - API Exposure: INFO (Health API endpoint accessible)
  - Security Headers: WARN (Missing security headers: X-XSS-Protection, Content-Security-Policy, Strict-Transport-Security)

- **SCADA**:
  - Network Availability: PASS (IP: 172.20.0.2)
  - TCP Port Accessibility: FAIL (Expected: [80, 8080], Open: [])
  - Connectivity: FAIL (Ports not accessible)

- **Blockchain**:
  - Network Availability: PASS (IP: 172.20.0.10)
  - TCP Port Accessibility: PASS (Expected: [1065], Open: [1065])
  - Data Access: INFO (Blockchain data access response received)
  - Data Write Access: INFO (Response: timed out)

- **Fingerprinting**:
  - Network Availability: PASS (IP: 172.20.0.3)
  - TCP Port Accessibility: PASS (Expected: [1066], Open: [1066])
  - Data Access: INFO (Fingerprinting data access response received)
  - Data Write Access: INFO (Response: timed out)

- **Data_Populator**:
  - Network Availability: PASS (IP: 172.20.0.4)
  - TCP Port Accessibility: INFO (No ports defined for component)

- **Network**:
  - Network Segmentation: PASS (All expected devices found: 10/10)
  - Network Segmentation: INFO (Skipping full subnet scan for unexpected devices)
  - Vulnerability Scan: INFO (Performing limited version detection instead of full vulnerability scan)
  - Version Detection: INFO (Scan completed on 10 IPs. Results in /tmp/nmap_version_results.xml)

### Security Assessment Summary
- Total Tests: 43
- PASS: 17
- WARN: 2
- FAIL: 8
- INFO: 9
- SKIP: 7

### Critical Findings
1. PLC1: TCP Port Accessibility - Expected: [502, 44818], Open: [502]
2. SCADA: TCP Port Accessibility - Expected: [80, 8080], Open: []
3. SCADA: Connectivity - Ports not accessible
4. PLC2: TCP Port Accessibility - Expected: [502, 44818], Open: [502]
5. PLC3: TCP Port Accessibility - Expected: [502, 44818], Open: [502]
6. MQTT_Broker: TCP Port Accessibility - Expected: [1883, 8883], Open: []
7. MQTT_Broker: Connectivity - MQTT ports not accessible
8. Grafana: HTTPS - Grafana does not use HTTPS

