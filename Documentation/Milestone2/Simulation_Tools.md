# Python Simulation Tools 

In this section, an exploration of potential Python tools for DCS and SCADA system emulation are explored. 

### Tool Purpose

This research work uses the following proces:

1. Survey existing DCS and SCADA architectural devices and networking designs
2. Identify the most commons assets and functions in these systems
3. Determine the most common threats to the assets and functions of these systems
4. Discover potential decentralized security control processes to mitigate these threats
5. Design a novel DCS design using a standard DCS architecture augmented by novel decentralized controls
6. Model the novel design in emulation software
7. Test the system digitally to determine functionality, efficiency, and functionality of the added security controls

Based on this research design, a tool will be needed to implement the novel design and test its functionality. From the design stated above, the Python-based emulation tool must allow coders to deploy and connect a variety of different DCS devices and configurations. To this deployed network, the tool must enable coders to augment the system with novel security systems. After adding these systems, the tool must allow coders to run the system both with and without the security controls to determine the effectiveness of the security controls as well as the burden the novel controls place on the system. Due to the constraints above, the tool chosen must be flexible, and likely open-source, such that researchers can not only use the intended functionality fo the tool, but also augment the functions with custom code structures.

### Tool Requirements

To satisfy the requirements set out by the research design stated above, the Python-based tool must:

* provide **virtual representations of common DCS devices**
* facilitate **custom DCS device configurations**
* allow **flexible DCS device connections and custom network designs**
* supply **distributed network traffic emulation** using ModBus
* allow **the DCS system to run**
* provide **network traffic inspection**
* supply **network device inspection and state analysis**
* facilitate the **addition of security controls**
* Allow the **integration of decentralized security tools**
* provide **analysis functions** to determine _system speed, efficiency, and functionality_

### Possible Python Simulation Tools

In this section, a set of possible Python-based DCS emulation tools will be listed. For each tool, the following information will be provided:

* Tool Name
* A brief description of the tool
* A link to the tool
* Install Process

Based on the criteria above, the following tools are identified:

1. [Distributed Control System Library](https://github.com/flyingmeat/aktos-dcs)

      * **DESCRIPTION**: The aktos_dcs package is designed for creating fault tolerant, realtime, massively concurrent, distributed (even behind firewalls), io-bound (eg. heavy-traffic web server), scalable (both vertically and horizontally), cross-platform and language agnostic applications.

      * **INSTALL**:
         * Clone repo
         * <code>cd aktos-dcs && sudo ./install-on-linux.sh</code>

3. [SCADASim](https://github.com/cmu-sei/SCADASim)

      * **DESCRIPTION**: Simulates a SCADA system. Uses PyModbus to create custom PLC devices. Simulates Modbus TCP/RTU traffic

      * **INSTALL**:
         * Clone Repo
         * <code>cd pymodbus</code>
         * <code>python setup.py install</code>
         * <code>pip install twisted cryptography bcrypt pyasn1 service_identity</code>

4. [PyScada](https://github.com/pyscada/PyScada)

      * **DESCRIPTION**: A Open Source SCADA System with HTML5 HMI, build using the Django framework. If you like to setup your own SCADA system head over to http://pyscada.rtfd.io.

      * **INSTALL**:
         * See [https://pyscada.readthedocs.io/en/main/quick_install.html](https://pyscada.readthedocs.io/en/main/quick_install.html)
         
6. [C104](https://pypi.org/project/c104/) - Only protocol?
7. [RapidSCADA](https://rapidscada.org/) - Create custom SCADA setups - Maybe help?
8. [ASTORIA](https://github.com/ComputerNetworks-UFRGS/ASTORIA) - Attack simualtor - maybe help? - Paper: https://ieeexplore.ieee.org/document/7502822/
9. Our own solution?

NOTE: Good Source for possible packages and justifications - [ICS Simulation](https://wpcdn.web.wsu.edu/wp-vcea/uploads/sites/3267/2022/11/GISiteVisit2022_poster_SpencerScamman.pdf)
### Python Tool Test Outcomes

To test the tools, a Linode instance is deployed using a standard Ubuntu distribution. From this node, each tool is installed and deployed. During deployment and testing, the pros and cons of each tool are outlined below.

1. Tool - Overview of the test.
    * Pros
    * Cons

### Python Tool Ranking

1. Best Tool
2. ...
3. Worst Tool

### Chosen Tool

Tool - About

### Python Simulation Tool Setup

How to set it up on a computer

### Python Simulation Tool use

How to Use.

### Deployment Analysis

Are we all on the same page?
