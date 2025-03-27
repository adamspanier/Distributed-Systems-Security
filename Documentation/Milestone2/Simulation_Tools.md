# Simulation Tools 

[HOME](https://github.com/adamspanier/Distributed-Systems-Security)

<hr>

In this section, potential emulation tools for DCS and SCADA system emulation are explored. 

Definitions

| Acronym | Meaning |
|:-------:|:-------:|
| ICS     |     Industrial Control System |
| SCADA   |     Supervisory Control and Data Aquisition |
| DSC     |     Decentralized Security Control |
| REES    |     Research Environment Emulation System |
| RTU     |     Remote Terminal Units |

### Tool Purpose

This research work uses the following processes:

1. Survey existing ICS and SCADA architectures
2. Identify the most common assets and functions in these systems
3. Determine the most common threats to the assets and functions of these systems
4. Discover potential DSC processes to mitigate these threats
5. Design an ICS system augmented by combinations of DSC systems
6. Model the ICS design in the REES
7. Test the system to determine the efficiency and functionality of the added security controls

Based on this research design, a tool or set of tools (referred to as the Research Environment Emulation System(REES)) will be needed to implement the novel design and test its functionality. From the design stated above, these emulation tools must allow coders/researchers to deploy and connect a variety of different DCS devices, networks, applications, and configurations. Additionally, the REES enables researchers to augment the system with both traditional security controls (encryption, authentication, etc) and novel security approaches (decentralized security controls). 

After adding these systems, the REES must allow coders to run the system both with and without the security controls to determine the effectiveness of security control application. Due to the constraints above, the REES chosen must be flexible, scalable, expandable, and likely open-source such that researchers can not only use the intended functionality of the tool but also augment the functions with custom code structures.

### Tool Requirements

To satisfy the requirements set out by the research design stated above, the REES must:

* provide **virtual representations of common ICS devices**
* facilitate **custom ICS device configurations**
* allow **flexible ICS device connections and custom network designs**
* supply **distributed network traffic emulation** using ModBus
* allow **the ICS system to run**
* provide **network traffic inspection**
* supply **network device inspection and state analysis**
* facilitate the **addition of security controls**
* Allow the **integration of DSC tools**
* provide **analysis functions** to determine _system speed, efficiency, and functionality_

### Possible Simulation Tools

In this section, a set of possible ICS emulation tools is listed. For each tool, the following information will be provided:

* Tool Name
* A brief description of the tool
* A link to the tool
* Install Process

Based on the criteria above, the following tools are identified:

#### Python-Based:

1. [Distributed Control System Library](https://github.com/flyingmeat/aktos-dcs)

      * **DESCRIPTION**: The aktos_dcs package for Python is designed for creating fault tolerant, real-time, massively concurrent, distributed (even behind firewalls), io-bound (eg. heavy-traffic web server), scalable (both vertically and horizontally), cross-platform, and language-agnostic applications. This tool would necessitate the use of a Python-based environment.

      * **INSTALL**:
         * Clone repo
         * <code>cd aktos-dcs && sudo ./install-on-linux.sh</code>

3. [SCADASim](https://github.com/cmu-sei/SCADASim)

      * **DESCRIPTION**: This Python-based package simulates a SCADA system, uses PyModbus to create custom PLC devices, and simulates Modbus TCP/RTU traffic. This tool would necessitate the use of a Python-based environment.

      * **INSTALL**:
         * Clone Repo
         * <code>cd pymodbus</code>
         * <code>python setup.py install</code>
         * <code>pip install twisted cryptography bcrypt pyasn1 service_identity</code>

4. [PyScada](https://github.com/pyscada/PyScada)

      * **DESCRIPTION**: This Python-based package is an open-source SCADA System with HTML5 HMI, built using the Django framework. This tool would necessitate the use of a Python-based environment.

      * **INSTALL**:
         * See [https://pyscada.readthedocs.io/en/main/quick_install.html](https://pyscada.readthedocs.io/en/main/quick_install.html)
         
6. [C104](https://pypi.org/project/c104/) - Only protocol?

      * **DESCRIPTION**: This Python-based package is designed to simulate SCADA systems and RTUs that communicate using the IEC 60870-5-104 protocol. IEC 60870-5-104 is a protocol in the IEC 60870 set of standards that allows control of SCADA systems.
        
      * **INSTALL**:
         * See [https://pyscada.readthedocs.io/en/main/quick_install.html](https://pyscada.readthedocs.io/en/main/quick_install.html)
 
8. [RapidSCADA](https://rapidscada.org/) - Create custom SCADA setups - Maybe help?

      * **DESCRIPTION**: This Python-based package is an open-source SCADA System with HTML5 HMI, built using the Django framework. This tool would necessitate the use of a Python-based environment.

      * **INSTALL**:
         * <code>python3 -m pip install c104</code>
 
#### Docker-Based:

1. [OpenPLC Image](https://hub.docker.com/r/fdamador/openplc)

      * **DESCRIPTION**: This image provides a basic open-source Programmable Logic Controller.
        
      * **INSTALL**:
         * <code> docker pull fbarresi/softplc</code>
         * <code>git clone https://github.com/thiagoralves/OpenPLC_v3.git</code>
         * <code>cd OpenPLC_v3</code>
         * <code>./install.sh [platform]</code>
         
2. [OPC Unified Architecture Image](https://hub.docker.com/r/open62541/open62541)

      * **DESCRIPTION**: This image is an open-source implementation of the OPC Unified Architecture that allows communication in OPC UA-based systems.
        
      * **INSTALL**:
         * <code>docker pull open62541/open62541</code>
         
3. [STunnel Image](https://hub.docker.com/r/dweomer/stunnel)

      * **DESCRIPTION**: This image provides encryption functions for docker network systems.
        
      * **INSTALL**:
         * <code>docker pull dweomer/stunnel</code>

4. [MQTT Broker Image](https://hub.docker.com/_/eclipse-mosquitto)

      * **DESCRIPTION**: This image provides an open source MQTT broker for SCADA system simulation.
        
      * **INSTALL**:
         *<code> docker pull eclipse-mosquitto</code>

5. [InfluxDB Database Image](https://hub.docker.com/_/influxdb)

      * **DESCRIPTION**: This image provides an open-source time series database built for real-time analytic workloads.
        
      * **INSTALL**:
         *<code>docker pull influxdb</code>

6. [Grafana Image](https://hub.docker.com/r/grafana/grafana)

      * **DESCRIPTION**: This image provides monitoring, analytics, and data visualization functions for web applications.
        
      * **INSTALL**:
         *<code>docker pull grafana/grafana</code>

7. [WireGuard Image](https://hub.docker.com/r/linuxserver/wireguard)

      * **DESCRIPTION**: This image provides VPN functionality.
        
      * **INSTALL**:
         *<code>docker pull linuxserver/wireguard</code>

7. [Ignition Image](https://hub.docker.com/r/inductiveautomation/ignition)

      * **DESCRIPTION**: This image is a powerful integrated development environment with everything you need to create virtually any kind of industrial application – SCADA, IIoT, MES, and beyond – all on one platform. 
        
      * **INSTALL**:
         *<code>docker pull inductiveautomation/ignition</code>

8. [Wireshark](https://hub.docker.com/r/linuxserver/wireshark)
   
      * **DESCRIPTION**: Wireshark is a network protocol analyzer that allows researchers to analyze packet data flowing across networks.
        
      * **INSTALL**:
         *<code>docker pull linuxserver/wireshark  

### Docker-Based REES Tool Chart

| Tool Name | Tool Function |
|:---------:|:-------------:|
| Ignition  | Provides SCADA System emulation and functionality |
| OpenPLC   | Provides open-source PLC emulations |
| MQTT      | Facilitaes the machine-to-machine message queueing service |
| InfuxDB   | A Database built specifically for time-series data in high-volume, high-velocity systems |
| Grafana   | Provides visualization tools for data presentation in web applications |
| STunnel   | Provides TLS/SSL tunneling services |
| WireGuard | Provides open-source VPN servicing |

### REES Test Outcomes

To test the tools, a Linode instance is deployed using a standard Ubuntu distribution. From this node, each tool is installed and deployed. During deployment and testing, the pros and cons of each tool are outlined below.

### REES Selection

What was selected?

### REES Setup

How to set it up on a computer

### REES USE

How to Use.

### Deployment Analysis

Are we all on the same page?
