# Research Paper Outline

[HOME](https://github.com/adamspanier/Distributed-Systems-Security)

<hr>

## Paper Outline - M2 Feedback
- Complete - **Merge Related work with Background** - Comment: I would either incorporate the related work into the background section OR move it to the end of the paper ahead of the conclusion so that you can use it as an evaluation comparison point to your tool.
- **Justify Model-based system before system design** - Prior to your system design section I think you need to explicitly justify model-based system engineering as an approach. Why use a model?
- **Justify decentralized controls in system design** - In your system design section, you need to clearly state how and why you selected the specific controls or techniques (e.g. digital signatures, blockchain, etc) - why these and not others?
- **Justify Power Stations** - Consider adding some bullets to justify power stations as a good use case. The justification in your talk is great - so I'd suggest just making sure it appears either in your intro and/or your system design sections.
- **Justify Choice of Docker** - you should also justify your choice of docker and other technology choices as a platform
- **Connect testing with contraints of ICS systems** - in your testing section make sure to connect the test criteria (responsiveness, security under attack) back to your constraints and challenges of ICS systems. Taking a few sentences to tie these back to your research questions should help make your narrative flow jive better.


## Abstract

* Summation of the work

## I. Introduction

* Problem
   * Distributed industrial control systems play a significant role in the critical systems that maintain the world today.
   * Protecting these systems is _essential_ in maintaining stability, health, and prosperity in human society.
   * Current critical systems, while more secure than they once were, can still be made safer.
   * Traditional security measures have been thoroughly explored, but alternate approaches could exist
     
* Value
   * Due to the importance ICS networks have in critical systems, the security of an ICS directly serves the safety and security of the people that use the critical system.
   * Any improvement in these systems will help make a more peaceful, stable and prosperous society.
     
* While securing ICS networks in needed and beneficial, it is also difficult for the following reasons:
   * ICS networks use devices with limited computational power
   * ICS networks run in real-time environments
   * Malfunctioning ICS networks can cause physical and financial damages, and in some cases can lead to human casualties
   * Maintaining the functionality of an ICS network is _essential_
   * Any security mechanism deployed _must not_ negatively impact the real-time constraints on the system
     
* How others have attempted to improve ICS network security
   * Traditional approaches include the use of encryption, tunneling, limited authentication mechanisms, and physical security controls
   * Research has also been done on the use of blockchains, fingerprinting, and other decentralized security controls in ICS networks
      * These attempts are less researched
      * Most attempts are focused only on the security control, not a cohesive system design

*  In this research, we explore the following questions to address the challenges above
   * **RQ1:** How can Distributed Industrial Control Systems be designed for security from a system design standpoint using distributed cryptographic security controls?
   * **RQ2:** How can these distributed security controls be applied and combined in ICS networks as a means to increase security?

## II. Background
* ICS System Fundamentals
   * Industrial Control Systems are cyber-physical systems that use programs to control physical actuators.
   * These systems are combined in such a way as to serve a concrete, real-world function
   * Examples or ICS systems are: power substations, nuclear power plants, hydroelectric dams, manufacturing plants, oil refineries, etc.
   * Programmable Logic Controllers carry out many of the cyber-physical operations in ICS networks

* Distributed ICS   
   * Many ICS networks operate in distributed networks
   * These networks operate in geographically separate environments
   * To control disparate geographic locations, Supervisory Control and Data Acquisition (SCADA) system controllers are used
   * SCADA systems use Remote Terminal Units (RTUs) to communicate with the devices in the distributed network

* Hard Real-Time
   * Most SCADA systems operate in hard real-time environments
   * Hard-real-time indicates that tasks that are assigned must be carried out in some acceptable time-frame
   * If the task does not occur in the correct timing, the system can cease to be functional or even cause physical damage
   * Hard-real-time constraints are enforced by the environments, not the engineers; thus they cannot be changed or ignored

* Operational Technologies
   * Operational Technologies (OT) comprise any system in which operational constraints (aka real-time constraints) outweigh the information constraints
   * Most ICS networks are OT networks  

* Decentralized Security Controls
   * Blockchains, digital signatures, Code Signing, and Fingerprinting are common decentralized security primitives

   * Blockchains
      * A blockchain is a linked list that used a hash address to point to the next node in the list
      * A hash is a one way function that creates a fixed bit output for a variable bit input.
      * A cryptographically secure hash is a hash that implements collision resistance
      * Collision resistance indicates that the bit length of the resulting digest is so vast collisions cannot be intentionally discovered

   * Digital Signatures
      * Digital Signatures are unique values that are associated with a single document and a single key

      * Signing
         * A signature is achieved by first hashing a document using a cryptographically secure hashing algorithm
         * The resulting hash is encrypted with private key of a user
         * The resulting value is affixed to the document

      * Validating a signature
         * A signature is validated by decrypting the signature using the public key of the user
         * The resulting hash is then compared to the hash of the received document
         * If the two values match, the signature is validated

   * Code Signing
      * Uses the same concept as digital signatures, but with code
      * Code that is signed can be verified via the public key of some organization

   * Digital Fingerprinting
      * A process by which the digital data or physical constraints of a device are patterned to generate a unique id

## III. Related Work
* Related Works
   * The related works fall into three categories
      * Data Integrity Protection
      * Device Fingerprinting
      * Decentralized System Design
        
   * Data Integrity breaks into two categories
      * Centralized Protection
      * Decentralized Protection
        
   * Device Fingerprinting breaks into two categories
      * Anomalous Behavior Detection
      * General Fingerprinting
        
   * Decentralized System Desing breaks into two categories
      * Decentralized System Weaknesses
      * Decentralized System Design
        
   * Discussion
      * The use of decentralized security controls is not new to ICS networks
      * Most exploration has been done via the application of blockchains to ICS networks
      * These blockchains are often applied as a means to create immutable logging processes
      * Fingerprinting is also used, generally to detect anomalous behavior
      * The least explored area in this review lies in the Decentralized System Design category  

## IV. System Design

* To begin testing ICS security mechanisms, we need to create a model system

### Model System Overview
  
* Model System Function
  * Our model system function is that of a power substation
  * A power substation takes high voltage power and steps it down for commercial and residential applications
  * IN a power substation a step down transformer changes the voltage and distribution busses transmit the lower volatge power
  * The power lines in the substation are protected by breakers
  * These breakers, while coming in multiple types, are controlled via PLCs
  * The PLCs use sensor inputs to connect the breaker mechanisms via ladder logic
  * The PLCs connect to the SCADA system using an MQTT broker
  * Message Queuing Telemetry Transport is the messaging protocol commonly used in ICS networks
  * The SCADA system tracks data with a database
    
* There are many other types of ICS network functions
  * Power plants, factories, hydroelectric dams
  * We chose a substation due to its simplicity
  * This simplicity allows us to better undersatnd the system for better testing results
  * The simplicity of the system also allows a more robust model to be created

* System Operation
  * The model system will analyze voltages
  * If volatges fall outside acceptable parameters, the breakers will be thrown
  * Security violations occur if the breakers cannot sufficiently react
    
* System Diagram

![Function](https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Images/SDF2.png)

### ICS System Requirements
* ICS Systems have the following assets
  * Hardware: PLCs, RTUs, Human Machine Interfaces (HMI), workstations, servers, sensors, actuators, relays, routers, and switches
  * Software: SCADA, DCS controllers, PLC ladder logic, firmware, HMI, historian, drivers, and databases
  * Data: Variable data, set points, thresholds, configurations, historical data, backups, parameters, topology information, and control recipes and sequences
  * Communication: Protocols, OPC comms, fieldbus networks, serial comms, and remote access
  * Human: Engineers and operators, maintenance personnel, security personnel, policies, procedures, compliance, regulations, disaster recovery plans

* ICS Systems have the following Threats
  * Architectural Threats: lack of defense in depth, single points of failure, improper security boundaries, etc.
  * Operational Threats: improper change management procedures, delayed patching, human error, inconsistent backups, etc.
  * Cyber Attack Threats: APTs, ransomware, supply chain attacks, C&C exploitation, Cyber-Physical attacks, etc.
  * Physical Threats: unauthorized physical access, HVAC failure, fire, tampering, power, etc.
  * Data Threats: integrity violations, MiTM attacks, time sync attacks, data historian compromises, etc.
  * Insider Threats: malicious insider threats, social engineering, shared credential abuse, remote access exploitation, etc.
  * Governance Threats: inadequate security policies, insufficient risk assessment processes, inadequate security testing, etc.
  * Supply Chain Threats: compromised third party software, single-source vendor dependency, use of out-dated components, etc.

* Threat/Asset Groupings
  * Asset to threat groupings diagrams based on the data [here](https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Documentation/Milestone2/Assets_Threats_Controls.md)
    
* Decentralized Security Controls
  * Fingerprinting, blockchain logging, digital signatures and code signing is used to protect the assets above via applicable threat vectors
  * Blockchain: data integrity validations, MiTM mitigations, time sync attack mitigations, intrusion detection, etc.
  * Fingerprinting: anomalous behavior, malfunction, failure detection, fire detection, tampering detection, ransomware detection, etc.
  * Digital Signatures: APT defense, malware defense, ransomware defense
     
* System Functional Requirements
  * Synchronize hardware and software assets according to the specific time-critical functions of the system
  * Limit latency, delay, and jitter in communication circuits to accepted tolerances
  * Detect unsafe states and transfer from unsafe to safe with as little human intervention as possible
  * Facilitate bi-directional communication between connected devices
  * Carry out the physical movements needed to both maintain a safe state and carry out system objectives
  * Operate within the constraints of the PLCs and other network devices in the system
  * Exhibit the simplest control complexity possible to meet system operation objectives
  * Coordinate widely distributed hardware devices

* System Non-Functional Requirements
  * Log all access requests
  * Log all successful access
  * Log all data transfers
  * Log all program updates

### Model System Architecture
* To model this system, Docker will be used to create an emulation of the environemnt and system described above

* The basic network components will be:
  * Four PLCs
  * An MQTT Broker
  * A SCADA control system
  * A Database
  * Emulation and Model
    * The PLCs in the emulation will control the breakers
    * The SCADA system will be responsible for tracking the function of the system

* Three emulated networks will be created for this experiment
  * Network 1 (Control): A network with four PLCs, an MQTT broker, a SCADA controller, and a Database.

![net1](https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Images/423647388-912c2833-6906-4abd-9a3a-4e402d5a5da4.png)

  * Network 2 (Comparison): Network 1 but with encryption and tunneling enabled

![net2](https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Images/enc.png)

  * Network 3 (experiment): Network 1 but with decentralized security controls
    * The decentralized security controls will be a Fingerprinting server and a logging blockchain
   
![net3](https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Images/net3.jpg)

* Model System Requirements
  *  The model system will meet the requirements stated in the section above

## V. System Emulation
* Docker
  * The system model stated above will be implemented across the three networks outlined above using Docker
  * Docker is an imaging tool that allows compartmentalized containers to be deployed in virtual networks
  * Operations can be automated in these networks and the functionality of the network can be observed

*Linode
  * The Docker test networks will be implemented via a Linode server
    
* Other Approaches
  * Initially a Python approach was considered, but shelved due to limited functional code
  * Other code-bases like Java can also be used
  * Emulation software is available, but generally costs money

* Docker Rationale
  * Docker is free
  * Docker provides Docker Hub
  * The Docker Hub allows access to emulations of the hardware we are testing
  * Docker is flexible and easy to use
  * Docker allows the network model above to be reasonably implemented for testing
  * The creation of custom Docker containers is free and relatively easy to accomplish

* Docker Implementation Specifics
  * To build the network docker compose files were used to outline the services and functions in the system
  * A master control shell script is used to tear down and reboot the test networks
  * The third network implements custom sockets-based servers that emulate the blockchain and fingerprinting test functions

## VI. Testing
* To test the system, an over-voltage scenario will be implemented wherein the automated breakers must flip
* The scenario will be run on each network without a cyber attack and the responsiveness of the network measured
* The scenario will be run on each network with a cyber attack testing security controls and responsiveness will be measured
* Network functionality will also be noted
* Criteria:
  * If the network fails to protect against the attack, the network fails
  * If the network fails to meet real-time specification, the network fails
* Discussion of raw results
  * When we have the results, the raw material will be discussed here  
  
## VII. Discussion
* Restate the research questions:
   * RQ1: How can Distributed Industrial Control Systems be designed for security from a system design standpoint using distributed cryptographic security controls?
   * RQ2: How can these distributed security controls be applied and combined in ICS networks as a means to increase security?
* Explain how we answered each
* Explain the meaning of these discoveries
  
## VIII. Conclusion
* Present a final overview of the findings of the paper
