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

Due to the uniqueness of every ICS network in it's function, the only way to experiment with novel system security designs is to explicitly define what Cyber-Physical function the test system will be responsible for. Without an adequately designed and defined industrial function, the benchmarks and system limits are completely unknown. Without any understanding of how the system must perform, the integration of novel security controls cannot be adequately tested for impact. While system requirements serve as a general litmus test for function, only with a explicitly designed industrial system for an industrial function can actual functionality of novel DSCs be measured. 

#### Test System Industrial Function

Knowing any test system must have an explicitly defined system purpose, this work seeks to outline the industrial system function below.

### II. Test System Design Methodology

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

