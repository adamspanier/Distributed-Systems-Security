# Executive Summary
[HOME](https://github.com/adamspanier/Distributed-Systems-Security)

What are you doing and why?
Goals and Objectives
Merit of the Project

### Raw Idea

PLCs use a centralized system to coordinate industrial tasks. This system is called an Industrial Control System (ICS). Centralization is used in most manufacturing and industrial applications as it is efficient, simple, and robust. PLCs, due to their limited functionality and computational capabilities, exhibit a very limited ability to carry out internal security tasks. Due to this limitation, the work of securing the ICS must fall to another entity. Further, the real-time nature of PLC-based ICS architectures requires that all additional security systems do not impede the dedicated industrial purpose the ICS is designed to carry out. The limitations as expressed above make securing ICS networks very difficult. Due to the difficulty of securing ICS networks, many ICS architectures simply ignore the need for security controls by accepting the possible risk of PLC or network-based attacks. 

This research will carry out an analysis of threats against PLC-based ICS networks, list possible threat asset pairs, outline various attacks that can be leveraged against ICS networks, and, from this data, attempt to build a list of decentralized cryptographic controls that can be used for each threat/asset pair to mitigate the probability of exploitation. When completed with the decentralized security control list, a novel decentralized cryptographic system will be assembled from the combined set of all decentralized security controls gleaned form the threat/asset list. The system will then be designed and modeled with an emphasis on maximizing efficiency of the industrial process. After assembling the design and the model, testing will be taken to validate the functionality of the system.

### Process
1. List possible attacks on PLCs and ICSs
2. Indicate how each attack can be mitigated with a novel decentralized cryptographic primitive
3. Assemble mitigations into an ICS sub-system
4. Model the system in code
5. Focus on maintaining speed, efficiency, and real-time capability of the PLCs and the ICS
