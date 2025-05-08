# Distributed Security Controls in Industrial Control Systems - Final Report

[HOME](https://github.com/adamspanier/Distributed-Systems-Security)

## Executive Summary

### ***** NEWS ALERT START *****

**29 JUL 2027: 0300** 

A wave of darkness covers the United States as power substation after power substation fails. The cascading blackout ripples slowly cross the country, shutting down water, coolant, and industrial production systems in its wake. City after city, home after home, fall eerily quiet as air conditioners, refrigerators, freezers, fans, and electrical devices fall into silence. The people are scared, but with fully charged phone batteries and backup generators, the population remains calm.

**27 AUG 2027: 1200** 

Panic grips the population. The phones have been dead for weeks now. Natural gas production is dead. All but a handful of generators have stopped producing electricity. The black start has begun, and portions of the grid are back up, but only for short durations due to heavy electrical loads. Water is running short, and the flow of gasoline is drying up. The lingering possibility that this may last for months more threatens the tenuous peace that keeps the population from taking matters into their own hands.

### ***** NEWS ALERT END *****

### The Problem

While the scenario above reads like a chapter from a science-fiction film, the critical systems holding modern society together are only one cyber attack away from complete collapse. These critical systems, often controlled by distributed Industrial Control Systems (ICS), generally use small, computationally limited devices to carry out day-to-day operations. The distributed nature of these ICS networks can make securing these networks very difficult. The limited computing power and real-time nature of these systems renders commonly used cybersecurity tools useless. The functions of these distributed industrial systems simultaneously make them the _most important_ and the _least secure_ systems in the world. Given one effective cyber attack, the power grid could be down for weeks, if not months, leaving society to crumble in its wake.

When designing an ICS system, security and functionality are _always_ competing requirements. When the computing power of a device is limited, any applied security measure threatens to reduce system functionality. While traditional methods of securing networks aren't useful in ICS networks, there are many new decentralized security control (DSC) measures that could be used to secure critical systems. Concepts like blockchains, hashes, digital signatures, and device fingerprinting present new and fresh possibilities for securing distributed critical systems. While these types of security measures are not entirely new to industrial control systems, there are a limited number of words considering the application of such security mechanisms from a system-design perspective.

### The Questions

**RQ1: How can Distributed Industrial Control Systems be designed for security using distributed cryptographic security controls?**

**RQ2: What effect, if any, do these combined mechanisms have on the security stance of ICS systems?**

### The Goals

This DSC design investigation aims to:

1. Provide holistic, system-level DSC design guidance for ICS network engineers
2. Observe how different applications and combinations of DSC measures affect ICS networks
3. Understand the benefits and drawbacks of applying system-level DSC design to ICS networks

### The Project Methodology

To carry out this research, an initial survey of decentralized security measures in industrial control systems was carried out. Using the information discovered, a set of asset/threat pairs is derived based on common distributed industrial control system designs. Next, a decentralized security solution is matched to each asset/threat pair as a means to mitigate the risk posed to each asset. With each threat assigned to a security measure, a system is designed using two possible decentralized security controls. This system is then emulated in Docker, compared to both control and comparison networks, and analyzed for effectiveness.

### The Benefits

By allowing industrial control system designers to focus on the holistic, system-level security requirements of distributed industrial control systems, the networks they design can take a more robust, consistent, and predictable security profile. By using the method described above, the blind spots, computational bottlenecks, network complexities, and hidden threats common to distributed control systems can be systematically analyzed such that appropriate distributed security controls can be applied without affecting the functions of the system as a whole. By providing a more comprehensive security approach for industrial control system  designers, the critical systems that society relies upon for peace and order can be protected to the level that the people who need them expect.

### Results / Findings

The use of decentralized security controls (DSC) like blockchains or fingerprinting mechanisms is not new in ICS security operations. The majority of research aimed at better understanding DSC implementations in ICS networks focuses primarily on the effectiveness of a single DSC. Existing research generally focuses on two DSC mechanisms: 1) blockchain-based data validation and 2) fingerprint-based anomaly detection. Both the blockchain validation and fingerprint anomaly detection controls are shown to be effective in ensuring data integrity and in intrusion and anomalous behavior detection functions. 

This research notes the existence of a void in the assessment and understanding of how combinations of these DSC mechanisms affect ICS networks. To fill this void, this research aims to test combinations of DSC mechanisms in conjunction with standard ICS functions as a means to test the holistic effects these combinations have on ICS functions. To do this, an ICS model system is created to emulate the operations of a power substation. The power substation is selected for this research due to its commonality in real-world applications and its simplicity. The substation model designed in this work includes PLCs, RTUs, a database, and a SCADA controller.

From this design, three Docker networks, a Python scenario script, and a Python security evaluation script are created to emulate, operate, and test the model system. The first network is a simple control network comprised of PLCs, an MQTT broker, a database, and a SCADA controller. The second network is a comparison network comprised of the same components as the control but secured by encrypted traffic and a VPN. The third network is the experimental network, again comprised of the same components as the control and comparison networks, but instead of encryption and VPN protection, this network implements both a blockchain logging validator and a fingerprint-based anomalous behavior detection server. These two controls are selected due to their prevalence in existing literature. 

System testing reveals that the control system, as predicted, fails all security testing. The comparison network indicated the existence of multiple security flaws, including data integrity and anomaly detection failures, but passed data-in-transit testing. The experimental network passed all data integrity checks and successfully detects anomalous behavior and intrusions, but fails data-in-transfer testing. These results indicate that the combination of traditional security models with combined DSC mechanisms provides a more robust security stance for ICS networks.

#### Reflection

The initial proposal presented for this project changed significantly during the course of research efforts. Initially, the concept lay in a more hardware-oriented approach. As the initial literature review progressed, the focus of the project moved more toward a holistic design approach for the implementation of decentralized security controls into ICS networks. Upon settling on the newer approach, we needed to be able to model the system. In early conversations, Python was presented as a viable option, but as the research team investigated the implementation specifics of available Python packages, it became clear that a different solution was needed. The use of Python packages alone with custom Python code augmentations would've made consistency across test beds and the effort in coding overwhelming. With the limited amount of time available in the semester, a smaller scope was needed. 

At this point, a search was made for alternative methods and Docker emerged the clear favorite for modeling the ICS networks for testing. Docker provided consistency, automatability, flexibility, and accessibility for the networks that needed to be investigated. While Docker provided a meaningful solution to the implementation specifics of the project, many of the team were not very familiar with Docker functionality. This unfamiliarity led to a steep learning curve for the team. After figuring out the system, the test networks were created and the experiments successfully run.

While the Docker networks created in this work provided meaningful data for the study, a more robust deployment with more decentralized security control mechanisms should also be undertaken. Along with these bolstered DSC networks, networks with both traditional security mechanisms and DSC mechanisms should also be run and tested. Further, the testing on the networks can also be augmented through more intense timing checks when relating security control deployment to system functionality.

The most significant effort in this research lay in the compilation and subsequent understanding of just _what_ ICS networks are. The research team allotted a significant amount of effort to simply _understanding_ ICS networks, the assets the compose them, the functions they fulfill, the threats that threaten them, the security mechanisms that can secure them, and the regulations that govern them. From this effort, the team gained a much more robust comprehension of just what ICS networks are and how they connect to concepts like Operational Technology and Cyber-Physical systems. It is only through this learning curve that the team was able to create the model network designs and emulation strategies that were used to test the developed security functions.

Additional effort was expended in the research, comprehension, design, and implementation of two completely original DSC implementations. To create these implementations, a significant amount of research was required such that the controls met the requirements as stated by previous literature. While these new controls do work, they are also only in a prototype phase. Further work must be done to better refine their flexibility and functionality.

## Packaging and Release

### Requirements
* Linux - Ubunto
* Git
* Pip
* Docker

### Installation Instructions
* Make a new working directory and move into the new directory
* Download the install script found [here](https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Code/install.sh) to the new directory
* Open a Terminal in the new directory
* Run ```sudo chmod 777 install.sh && ./install.sh```
  * The ```install.sh``` bash file will _automatically configure your system_
  * Initial installation will automatically run the ```deply.sh``` script that runs the test networks

### Getting Started
* To run the system again, execute the deploy.sh script at _Distributed-Systems-Security/Code/DockerTestNets_
  * ```./deploy.sh```
