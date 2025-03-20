# Distributed Control Architecture Testbed

[HOME](https://github.com/adamspanier/Distributed-Systems-Security)

<hr>

### I. Test System Purpose

#### Cyber-Physical Systems

All ICS networks serve and support real-world operations. These systems are called _Cyber-Physical systems_. The operations of these systems embed ICS devices in functional environments where they are tasked with interacting with real-world sensor input and real-world actuators. Due to the mechanical and Cyber-Physical nature of ICS networks, each ICS serves a very specific, very well defined _function_. This function, served by the system, is the _most important_ service the system must fulfill. These functions cover a _wide range_ of operations:
* Assembly line robotics control
* Oil field pumping, storage, and distribution management
* Power substation monitoring, protection, and operation
* Nuclear centrifuge automation and protection
* Hydroelectric dam operations

As noted above, each of these example functions is highly integrated into the physical environment it serves. The computers in the system must control pumps, arms, robots, relays, motors, locks, and more; each serving an innately physical function. In each instance, where a human once operated such a physical device or interacted with such a physical system, now a computer is tasked with doing so. The benefits of automation in this way are seven-fold: no longer are humans put in the same dangers as they once were, operations can be streamlined with faster reaction times, and systems can be scaled up and down with ease. Alongside such notable benefits, the integration of computer controls in Cyber-Physical systems also brings a number of drawbacks; namely, if a computer fails or operates too slowly, the system can experience catastrophic failures, sometimes even leading to the loss of life.

The innate connection between the physical function, the industrial design serving the function, and the ICS system make each ICS network completely unique. Even across the same application domain, no two OT or ICS networks are going to be the same. Though one system may serve an oilfield in Wyoming and another in Texas, the topography, landscape, accessibility, weather, and spacial limitations make both systems completely different. This difference from ICS system to ICS system necessitates that general designs must be flexible and loosely defined; not the optimal atmosphere to carry out testing for real-world implications.

Due to the uniqueness of every ICS network in it's function, the only way to experiment with novel system security designs is to explicitly define what Cyber-Physical function the test system will be responsible for. Without an adequately designed and defined industrial function, the benchmarks and system limits are completely unknown. Without any understanding of how the system must perform, the integration of novel security controls cannot be adequately tested for impact. While system requirements serve as a general litmus test for function, only with a explicitly designed industrial system for an industrial function can actual functionality of novel DSCs be measured. Knowing any test system must have an explicitly defined system purpose, this work seeks to outline the industrial system function below.

#### Test System Industrial Function

The testbed system used in this work will emulate a Power Distribution Substation (PSS). A Power Distribution Substation is nothing more than a physical location that distributes high frequency alternating current to different users in the system. Generally, power substations will step-down high frequency power feeds, divert them to low voltage power lines, regulate the voltages both coming and going out, and ensure that all customers have power. If any issue arises, the safety functions of the substations will automatically operate relays and breakers to protect the system from physical damage. Many times, in an effort to avoid physical damages, substations going offline can cause cascading failures in power grid systems by diverting electrical current through other PSSs. The more current moving through a PSS, the higher the probability that PSS will need to go offline to protect itself. Given enough PSSs drop, large rolling blackouts can occur.

There are three primary sections of a power substation:
1. Incoming Transmission
2. Power Routing and Conversion
3. Outgoing Distribution
Source: [https://www.osha.gov/etools/electric-power/illustrated-glossary/sub-station](https://www.osha.gov/etools/electric-power/illustrated-glossary/sub-station)

The incoming transmission section is comprised of incoming high voltage transmission lines. The distribution section is comprised of outgoing low voltage transmission lines. The power routing and coversion section holds the majority of the PSS devices:

* **Lightning arresters (Surge Arrestors)** - Serve to divert abnormally high voltages to ground, generally in the case of a lightning strike

<img src="https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Images/Considerations-in-Arrester-Lead-Design-Application.jpeg" alt="drawing" width="500"/>

Source: [inmr.com](https://www.inmr.com/arrester-lead-design-application/)

* **Air-break Switches** - Switches with contacts in the open air. As they open, the resistance of the air quenches the circuit, though an arc generally forms for a few moments

<img src="https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Images/air-break_switch.jpg" alt="drawing" width="500"/>

Source: [southernstatesllc.com](https://www.southernstatesllc.com/applications/group-operated-disconnect-switches)
  
* **Step-down Transformers** - A device that transforms high voltage signals to low voltage signals through the use of electrical induction in copper coils

<img src="https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Images/step_down.jpg" alt="drawing" width="500"/>

Source: [eaton.com](https://www.eaton.com/us/en-us/catalog/medium-voltage-power-distribution-control-systems/substation-transformer.html)
  
* **Oil Circuit Breakers** - Much like an air-break switch, but uses oil to quench arcs instead of air

<img src="https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Images/oil_breaker.jpeg" alt="drawing" width="500"/>

Source: [electricalengineering.xyz](https://www.electricalengineering.xyz/high-voltage-circuit-breakers/)

* Voltage Regulators - Maintain power distribution system voltages within a predefined range

<img src="https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Images/voltage_reg.jpg" alt="drawing" width="500"/>

Source: [eaton.com](https://www.eaton.com/us/en-us/products/medium-voltage-power-distribution-control-systems/voltage-regulators/voltage-regulators--fundamentals-of-voltage-regulators.html)

* Distribution Busses - A metal bar that connectes substation components and carries current

<img src="https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Images/busbar.jpg" alt="drawing" width="500"/>

Source: [semanticscholar.org](https://www.semanticscholar.org/paper/Automatic-busbar-detection-in-substation%3A-Using-and-Hongkai-Shiying/86f914ce00674ff27e2dc4325179e8deb7812a25)

* Control Housings - The location of the electrical control components in the substation

<img src="https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Images/control_house.jpg" alt="drawing" width="500"/>

source: [kva-emc.com](https://kva-emc.com/substation-control-enclosures/)

The devices listed above can be seen below in Figure 1:

<img src="https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Images/substation_energy_flow.jpg" alt="drawing" width="900"/>

source: [osha.gov](https://www.osha.gov/etools/electric-power/illustrated-glossary/sub-station)

#### Test System Industrial Design

### II. Test System Design Methodology

The specifics of the system

### III. Test System Description

#### Assets

1. Operational Technology Components
* PLCs
* RTUs
* HMI Systems
* Field Devices
* Safety Instrumented Systems

2. Communication Infrastructure
* Industrial Protocols
* Network Segments
* Remote Access Points
* Protocol Gateways
* Wireless Communications

3. System Data
* Control Logic
* Configuration Files
* Historical Process Data
* Setpoints and Parameters
* Authentication Credentials

#### Security Controls

1. Zero Trust Architecture
* Continuous authentication
* Micro-segmentation
* Least privilege access

2. Distributed Authentication
* Peer-to-peer identity verification
* Blockchain-based credential management
* Distributed PKI

3. Network Redundancy
* Multiple independent communication paths
* Distributed routing protocols
* Failover mechanisms

4. Decentralized Monitoring
* Distributed intrusion detection
* Peer-validated anomaly detection
* Distributed logging


### Design Process

1.	Threat Modeling
2.	Asset Identification
3.	Security Control Selection
4.	Architecture Development
5.	Prototype Validation
6.	Iterative Refinement

### Functional Description

* Authenticate every device interaction
* Isolate network segments
* Implement multi-layer encryption
* Provide redundant communication paths
* Enable localized threat detection
* Support rapid incident response


### System Design Diagram

#### Unencrypted Environment

![image](https://github.com/user-attachments/assets/912c2833-6906-4abd-9a3a-4e402d5a5da4)



#### Encrypted Environment

![image](https://github.com/user-attachments/assets/2a0c3eb3-23a2-4cb4-96fa-ad3aa9c32313)


### System Application Benefits

1.	Enhanced network resilience
2.	Reduced single point of failure
3.	Improved threat detection
4.	Granular access control
5.	Scalable security architecture


### System Application Drawbacks

1.	Increased complexity
2.	Higher computational overhead
3.	More complex management
4.	Potential performance latency
5.	Higher initial implementation cost


### System Refinement Process

1.	Continuous threat assessment
2.	Performance metric analysis
3.	Regular security control evaluation
4.	Technology stack updates
5.	Stakeholder feedback integration

