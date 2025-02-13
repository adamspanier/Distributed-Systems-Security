# Executive Summary
[HOME](https://github.com/adamspanier/Distributed-Systems-Security)

## Decentralized Security Design in Industrial Control Systems

### ***** NEWS ALERT START *****

**29 JUL 2027 : 0300** 

A wave of darkness covers the United States as power sub-station after power sub-station fails. The cascading blackout ripples slowly across the country shutting down water, coolant, and industrial production systems in its wake. City after city, home after home, fall eerily quiet as air conditioners, refrigerators, freezers, fans, and electrical devices fall into silence. The people are scared, but with full phone batteries and backup generators, the population remains calm.

**1 SEP 2027 : 1200** 

Panic grips the streets. The phones have been dead for a month now. Natural gas production is dead. All but a handful of generators still produce electricity. The black start has begun and portions of the grid are back up, but only for short durations due to heavy electrical loads. Water is running short and the flow of gasoline is drying up.

### ***** NEWS ALERT END *****

### Problem Statement

While the scenario above reads like a chapter from a sci-fi film, the critical systems holding modern society within the tenuous grasp of peace and order are only one cyber attack away from complete collapse. These critical systems, often controlled by distributed Industrial Control Systems, generally use small, computationally limited devices to carry out day-to-day operations. These systems generally implement a central control structure used to coordinate and control small digital devices on distant networks. While the centralized nature of these systems ensures efficient and functional control of complex systems, the distributed nature of the remote portions of the system can make securing the network very difficult. Further exacerbating the issue, the limited computing power and real-time nature of the remote devices eliminates the use of many commonly used cyber security tools. The demands and the functions of these distributed industrial systems simultaneously makes them the _most important_ and the _least secure_ systems in the world. Given one effective cyber attack, the power grid could be down for weeks if not months, leaving society to crumble in it's wake.

The limited computing abilities of the remote devices in distributed industrial control systems makes securing these networks very difficult. In designing a system, security and functionality are _always_ competing requirements. When the computing power of a device is limited, any security measure that uses even a modicum of system resources threatens to render the system unusable. While traditional methods of securing networks don't serve distributed industrial systems, there are many new decentralized cryptographic security measures and design that can be used to secure critical systems. Concepts like blockchains, hashes, digital signatures, and device fingerprinting present new and fresh possibilities for securing distributed critical systems. While these types of security measures are not new to industrial control, there is a limited number of studies that take a system-design stance, aiming to design a robust distributed system by mitigating threat/asset pairs with novel distributed security designs.

### Goals and Objectives

This Holistic Decentralized System Design development aims to create more secure distributed industrial systems using the following four-phase approach:

1. Data Collection
2. System Design
3. System Emulation
4. Analysis and Reporting

To carry out this research, a initial survey of decentralized security measures in industrial control systems will be carried out. Using the information discovered, a set of asset/threat pairs will be derived based on common distributed industrial control system designs. Next, a decentralized security solution will be applied to each asset/threat pair as a means to mitigate the risk posed to each asset. With each threat assigned to a security measure, a novel system will be designed with each security control included. This novel system will be emulated in code and validated for functionality. Finally, the novel system will be tested using the limited computing and real-time constraints present in all industrial control systems.

### How it Helps Society

By allowing industrial control system designers to focus on the holistic, system-level security requirements of distributed industrial control systems, the networks they design can take a more robust and predictable security profile. By using the method described above, the blind spots, computational bottlenecks, network complexities, and hidden threats common to distributed control systems can be systematically analyzed such that appropriate distributed security controls can be applied without effecting the functions of the system as a whole. With this systematic approach, the security profile of the network will take on a more predictable and quantifiable nature, providing better oversight, design, and maintenance for distributed control systems worldwide. By providing a more comprehensive security approach for industrial control system  designers, the critical systems that society relies upon for peace and order can be protected to the level that the people who need them expect.

<!---
### Raw Idea

PLCs use a centralized system to coordinate industrial tasks. This system is called an Industrial Control System (ICS). Centralization is used in most manufacturing and industrial applications as it is efficient, simple, and robust. PLCs, due to their limited functionality and computational capabilities, exhibit a very limited ability to carry out internal security tasks. Due to this limitation, the work of securing the ICS must fall to another entity. Further, the real-time nature of PLC-based ICS architectures requires that all additional security systems do not impede the dedicated industrial purpose the ICS is designed to carry out. The limitations as expressed above make securing ICS networks very difficult. Due to the difficulty of securing ICS networks, many ICS architectures simply ignore the need for security controls by accepting the possible risk of PLC or network-based attacks. 

This research will carry out an analysis of threats against PLC-based ICS networks, list possible threat asset pairs, outline various attacks that can be leveraged against ICS networks, and, from this data, attempt to build a list of decentralized cryptographic controls that can be used for each threat/asset pair to mitigate the probability of exploitation. When completed with the decentralized security control list, a novel decentralized cryptographic system will be assembled from the combined set of all decentralized security controls gleaned form the threat/asset list. The system will then be designed and modeled with an emphasis on maximizing efficiency of the industrial process. After assembling the design and the model, testing will be taken to validate the functionality of the system.

### Process
1. List possible attacks on PLCs and ICSs
2. Indicate how each attack can be mitigated with a novel decentralized cryptographic primitive
3. Assemble mitigations into an ICS sub-system
4. Model the system in code
5. Focus on maintaining speed, efficiency, and real-time capability of the PLCs and the ICS
-->
