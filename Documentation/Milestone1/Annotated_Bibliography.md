# Annotated Bibliography

[METHODOLOGY](https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Documentation/Methodology.md)

<hr/>

### 1. Title: [A Novel Monitoring System for the Data Integrity of Reactor Protection System Using Blockchain Technology](https://ieeexplore.ieee.org/document/9126779)

**Reference:**

_M. K. Choi, C. Y. Yeun and P. H. Seong, "A Novel Monitoring System for the Data Integrity of Reactor Protection System Using Blockchain Technology," in IEEE Access, vol. 8, pp. 118732-118740, 2020, doi: 10.1109/ACCESS.2020.3005134._

**Summary:**

Nuclear Power Plants (NPP) are isolated from external networks but are still vulnerable to internal injection attacks via the NPP safety system. To avoid such attacks, all internal data must be monitored for data integrity (ensuring that unauthorized changes are not made to data). This work proposes the use of a private blockchain system to monitor the data integrity of the PLCs in the NPP system. The developed blockchain is also used to protect the Reactor Protection Systems. The novel blockchain system can detect code injection. The blockchain used is a private, randomized Proof-of-Authority-based blockchain that stores data contained in PLCS in each block and uses the same randomized PoA mechanism for consensus. The verification of traffic is carried out at each PLC, and a majority consensus is used to indicate which PLCs are operating correctly and which are getting errant results. This work calls this process Proof-of-Monitoring. A Merkle Tree is used to store the PLC hash data. Back-tracing algorithms are used to detect data anomalies in the ledger.

**Assessment:**

The work by Choi et al. demonstrates that novel blockchain-based ledger systems have been used with limited success as a means to add layers of security within industrial control systems. While this study does indicate that the system can be used and does provide notable benefits, no data was collected to verify the novel system's effect on safety system performance. Due to the real-time nature of most PLC-based ICS networks, the simple use of blockchain without verifying the effect on the functionality of the ICS only provides limited benefit when applied to real-world applications. 

**Keywords:**

Blockchain, Proof of Authority, Data Integrity

<hr/>

### 2. Title: [Blockchain architecture for process-level traceability of continuous mixing process in battery cell production](https://ieeexplore.ieee.org/document/10586718)

**Reference:**

_S. Otte, L. Reuscher, D. Keller and J. Fleischer, "Blockchain architecture for process-level traceability of continuous mixing process in battery cell production," 2024 1st International Conference on Production Technologies and Systems for E-Mobility (EPTS), Bamberg, Germany, 2024, pp. 1-14, doi: 10.1109/EPTS61482.2024.10586718._

**Summary:**

Lithium-ion batteries rely on the precise mixing of raw materials. This mixing must be tracked to ensure high-quality products and compliance with regulations. Due to the continuous variability of raw materials, tracking chemical mixing data is difficult. This work proposes a novel blockchain solution that integrates all PLC mixing data into a blockchain ledger that can be used for quality control, data validation, and legal compliance. The Hyperledger Fabric platform is used to implement the private blockchain using a SHA-256 hashing algorithm and a Proof-of-Authority consensus mechanism. To monitor the PLCs, external computers were connected to PLC data buses and passively observed the data state of each PLC via MQTT. The PLC data was then hashed via a JavaScript Hyperledger interface and stored in the blockchain. All additions to the blockchain propagate across the network via the PoA consensus mechanism. 

**Assessment:**

The work carried out by Otte et al. provides useful information regarding the actual implementation of a blockchain architecture for the immutable tracking of chemical mixing data originating from PLCs on a distributed ICS. By using the blockchain method, a trusted ledger could be kept that documents, in real-time, the PLC mixing data being produced from the PLCs on the manufacturing floor. With the data collected, the researchers were able to observe the production quality of battery components and prove that the batteries being made met the specifications that regulations required. This study shows that PLC data, regardless of content, can be tracked using an immutable trace ledger for fingerprinting, data validation, intrusion detection, or anomalous behavior. 

**Keywords:**

Blockchain, Proof of Authority, Data Integrity


<hr/>

### 3. Title: [Blockchain application in simulated environment for Cyber-Physical Systems Security](https://ieeexplore.ieee.org/document/9557446)

**Reference:**

_R. Colelli, C. Foglietta, R. Fusacchia, S. Panzieri and F. Pascucci, "Blockchain application in simulated environment for Cyber-Physical Systems Security," 2021 IEEE 19th International Conference on Industrial Informatics (INDIN), Palma de Mallorca, Spain, 2021, pp. 1-7, doi: 10.1109/INDIN45523.2021.9557446._

**Summary:**

Critical Infrastructures often use Industrial Control Systems (ICS). Industrial Control Systems use PLCs. Data and commands from the PLCs that move across the ICS are stored in the Historian, a logging program responsible for tracking logging in the ICS. ICS security comprises not only the operations of the ICS itself but also the logging systems that keep track of the status of the system. By changing logs, attackers can obfuscate attack trails, making digital forensics difficult. This work presents a novel blockchain application that is paired with the ICS historian as a means to immutably store and validate the clear-text logs stored by the Historian. By applying this system, data integrity can be verified for each operation that occurs in the ICS. Beyond data integrity, the proposed blockchain also provides for data recovery given the Historian data is maliciously changed or accidentally corrupted. The system was shown to resist Man-in-the-Middle and data injection attacks. While the blockchain did provide valuable data protection benefits, if an operator chooses to mangle data before it is recorded in the Historian, this system cannot help. 

**Assessment:**

The work carried out by Colelli et al. demonstrates that novel blockchain applications have been used to track, monitor, and validate PLC data, much like Choi et al. This research, while similar to the work carried out by Choi et al., applies blockchain ledger techniques to the logging processes carried out by the Historian resident in the centralized control structure in the ICS. The proposal made in this research demonstrates that an integrity check can be carried out on logging using a distributed ledger, but it also notes some weaknesses. Notably, because the Historian is a central location for logging data, if data is mangled before reaching the Historian logger, the data verification checks will only check against the corrupted data, thus bypassing the data integrity checks provided by the blockchain system. 

**Keywords:**

SCADA, Blockchain, Historian, Data Integrity

<hr/>

### 4. Title: [Protection against Ransomware in Industrial Control Systems through Decentralization using Blockchain](https://ieeexplore.ieee.org/document/10320188)

**Reference:**

_A. Parvizimosaed, H. Azad, D. Amyot and J. Mylopoulos, "Protection against Ransomware in Industrial Control Systems through Decentralization using Blockchain," 2023 20th Annual International Conference on Privacy, Security and Trust (PST), Copenhagen, Denmark, 2023, pp. 1-5, doi: 10.1109/PST58708.2023.10320188._

**Summary:**
ICSs are susceptible to Ransomware attacks due to their highly centralized architecture. Centralization is necessary in ICSs to maximize efficiency and functionality and is, thus, unavoidable. This work introduces a decentralized blockchain that replicates critical data, stores it, and distributes this data across a peer-to-peer network using a consensus algorithm. The distributed nature of the network protects against any single point of failure (SPoF). To protect the network further, a zero-trust architecture is introduced, such that all host-to-host and host-to-network transactions must be authorized. This research introduces a Blockchain-Based Industrial Control System (BBICS) that stores and processes critical data on the blockchain via a set of time-series databases. Non-sensitive data is handled off-chain. 

**Assessment:**

The work carried out by Parvizimosaed et al. takes a more functional perspective by focusing not only on the creation of a robust blockchain ICS system but also on building a blockchain that tries to maximize the efficiency of the system. Previous research generally aims to analyze the usefulness of blockchains in ICSs, whereas this research attempts to understand what impact the use of a blockchain may have on the productivity and functionality of the system. By distributing critical information across the network, this system provided full data recovery after a ransomware attack that affected 40% of all devices on the chain. 

**Keywords:**

Blockchain, Ransomware, Efficiency

<hr/>

### 5. Title: [Toward a Failures Model for Communication of Decentralized Applications with Blockchain Networks Applied in the Industrial Environment](https://ieeexplore.ieee.org/document/9857810)

**Reference:**

_C. T. B. Garrocho, K. N. Oliveira, A. L. d. Santos, C. F. M. da Cunha Cavalcanti and R. A. R. Oliveira, "Toward a Failures Model for Communication of Decentralized Applications with Blockchain Networks Applied in the Industrial Environment," in IEEE Wireless Communications, vol. 29, no. 3, pp. 40-46, June 2022, doi: 10.1109/MWC.001.2100572._

**Summary:**

Communication failures on IIoT networks present a critical problem for operational continuity. This work analyzes failure points in the consensus algorithms of a blockchain-based decentralized industrial application. During the research, each communication failure that occurred in the network was documented, defined, and classified. After analysis, countermeasures for each failure are presented in a novel failure model for decentralized communication networks in industrial applications. The purpose of this work is not to test blockchain functionality in IDCs but rather to analyze subsequent supporting systems that can help alleviate pain points common to decentralized ledger systems in industrial control applications. 

**Assessment:**

The work carried out by Garrocho et al. presents a new angle on blockchain-based ICS research; that is, the research focuses on how to shore up known weaknesses and failure points when applying blockchain and decentralized primitives to industrial control systems. This work provides value in that it demonstrates the need for a holistic approach when applying decentralized architectures to ICS applications. 

**Keywords:**

Blockchain, Failure Models, Blockchain Support


<hr/>

### 6. Title: [BACE: Blockchain-based Access Control at the Edge for Industrial Control Devices of Industry 4.0](https://ieeexplore.ieee.org/document/9628291)


**Reference:**

_C. T. B. Garrocho, K. N. Oliveira, D. J. Sena, C. F. M. da Cunha Cavalcanti and R. A. R. Oliveira, "BACE: Blockchain-based Access Control at the Edge for Industrial Control Devices of Industry 4.0," 2021 XI Brazilian Symposium on Computing Systems Engineering (SBESC), Florianopolis, Brazil, 2021, pp. 1-8, doi: 10.1109/SBESC53686.2021.9628291._

**Summary:**

The Industrial Internet of Things(IIoT) has immediate implications for Industry 4.0. Blockchain is useful to Industry 4.0 due to its ability to provide traceable and auditable access control. Many Industry 4.0 applications using IIoT implement cloud-based architectures. Applying blockchain to cloud infrastructures is difficult due to cost and communication latencies. This work proposes a blockchain architecture called BACE that puts the access control functionality of the system at the edge with the devices that are carrying out access requests. This work takes into account the real-time limitations imposed upon most ICS networks. This real-time sensitivity is likely why blockchain applications have yet to be applied to IIoT systems. BACE uses Smart Contracts and edge-based computing to build a flexible and scalable blockchain communication approach to manage access requests. To mitigate the storage and computational effects of the system via local storage of the PLC, this work focuses on creating a compact JSON-based format that only takes a few bytes of storage.

**Assessment:**

The value of this paper lies in the acknowledgment that time constraints are limiting factors in real-time application environments. Cloud-based IIoT is useful but causes latencies due to digital communication delays. This work creates an "edge" based blockchain that is stored locally on PLCs and propagated across the cloud-based PLC network. To mitigate the storage and computational requirements of the system, this work created a slim, JSON-based storage format that takes only a few bytes of memory to alleviate many of the overhead issues presented by decentralized cryptographic security mechanisms. 

**Keywords:**

Blockchain, Edge, Cloud, Eliminate Communication Latency, Real-Time

<hr/>

### 7. Title: [Securing Manufacturing Using Blockchain](https://ieeexplore.ieee.org/document/9343190)

**Reference:**

_Z. Jadidi, A. Dorri, R. Jurdak and C. Fidge, "Securing Manufacturing Using Blockchain," 2020 IEEE 19th International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom), Guangzhou, China, 2020, pp. 1920-1925, doi: 10.1109/TrustCom50675.2020.00262._

**Summary:**

ICS attacks generally use a phased approach during execution. Current frameworks can generally only scan a single data source and thus cannot detect all possible vectors as an attack is unfolding. This work proposes a two-stage security system wherein a blockchain is used to securely store ICS data in a distributed manner, and a deep learning system is used to analyze the blockchain for anomalous behavior. The proposed design was implemented and tested for functionality, demonstrating a high level of precision, equally comparable to systems that only analyze a single data source. With this model, any manufacturer, upon the discovery of an anomaly, can quickly notify other manufacturers in the supply chain of the failure. The work proposed a public logging blockchain for inter-manufacturer communications concerning manufacturing attacks and anomalies.

**Assessment:**

The work carried out by Jadidi et al. provides value by not only implementing a blockchain structure for data analysis but also a deep learning mechanism wherein data streams are analyzed for patterns and, based on these predictable patterns, anomalies are detected. The outcomes of the work show that multi-stream blockchain analysis is possible using artificial intelligence functionalities and that the use of a public blockchain may pose benefits to industry-specific supply chains.

**Keywords:**

Blockchain, Deep Learning, Logging

<hr/>

### 8. Title: [PLCPrint: Fingerprinting Memory Attacks in Programmable Logic Controllers](https://ieeexplore.ieee.org/document/10130481)

**Reference:**

M. M. Cook, A. K. Marnerides and D. Pezaros, "PLCPrint: Fingerprinting Memory Attacks in Programmable Logic Controllers," in IEEE Transactions on Information Forensics and Security, vol. 18, pp. 3376-3387, 2023, doi: 10.1109/TIFS.2023.3277688.

**Summary:**

A common attack vector in PLC memory is the malicious alteration of internal PLC memory. These memory attacks cause the PLC to function in ways that are not consistent with its operating environments. While memory attacks are a critical security issue in PLC security, different types of memory attacks can manifest similar physical manifestations. This makes attack triage and digital forensics difficult and often quite expensive when dealing with memory attacks. Adding to the damage, misbehaving PLCs can cause interruptions of work, resulting in financial losses as well as physical damage, and in some cases, even result in the loss of life.  This work proposes a novel system that maps PLC register memory state to a set of Mapping Conditions (MC) as a means to indicate if they exist in PLC memory artifacts. These MCs are then modeled and mapped as a means to predict PLC behavior. The study shows how MC deviations can be detected using a supervised learning scheme to determine the occurrence of memory attacks accurately. This work fills the need for attack technique triaging as it allows attacks to be more accurately described, logged, and mitigated.

**Assessment:**

This work is useful in its descriptions of memory fingerprinting as a means to predict and identify deviations from nominal operations. The use of memory fingerprinting to identify well-known operational memory patterns helps identify when deviations occur. This work also provides a robust background and related work section that provides essential information regarding other memory fingerprinting applications.

**Keywords:**

Fingerprinting, Attack Detection, Triaging

<hr/>

### 9. Title: [Fingerprinting for Cyber-Physical System Security: Device Physics Matters Too](https://ieeexplore.ieee.org/document/8490185)

**Reference:**

_Q. Gu, D. Formby, S. Ji, H. Cam and R. Beyah, "Fingerprinting for Cyber-Physical System Security: Device Physics Matters Too," in IEEE Security & Privacy, vol. 16, no. 5, pp. 49-59, September/October 2018, doi: 10.1109/MSP.2018.3761722._

**Summary:**

Physics can be used to define device identifiers. By using the physics of the components in each device, a unique identifier can be created that only that device can produce. These "fingerprints" can be used to increase the integrity of response actuators involved in the ICS. Cyber-physical systems protections are divided into two areas: analysis of network traffic and modeling system behavior based on some predictability matrix. This work proposes a PLC device fingerprinting scheme that uses the network level actuator response time, that is, the time it takes an actuator on the network to respond to a command from a given device. This work demonstrates that the use of physics-based fingerprinting based on residual signals or timing artifacts is a very useful means of providing outside-the-device fingerprinting techniques. Further, upon the creation of device fingerprints, any inconsistent fingerprint from the same device indicates either an attack or anomalous behavior.

**Assessment:**

This work adds value in its exploration of not only memory and software level fingerprinting but also the use of fingerprinting based on physics and/or physical attributes of a given device. Rather than intruding upon the memory of the PLC, external measurements can be taken to verify if the device itself is performing as expected. Given a divergence from this expected measurement, or fingerprint, anomalous behavior can be detected.

**Keywords:**

Hardware Fingerprinting, Physics Fingerprinting

<hr/>

### 10. Title: [Power Measurement Based Code Classification for Programmable Logic Circuits](https://ieeexplore.ieee.org/document/8642680)

**Reference:**

_T. Roy and A. A. L. Beex, "Power Measurement Based Code Classification for Programmable Logic Circuits," 2018 IEEE International Symposium on Signal Processing and Information Technology (ISSPIT), Louisville, KY, USA, 2018, pp. 644-648, doi: 10.1109/ISSPIT.2018.8642680._

**Summary:**

Traditional cyber security controls are not useful when protecting PLCs on ICS networks. Further, current methods of protecting ICS networks do not protect against novel, zero-day attacks. This work proposes the use of power consumption-based fingerprinting schemes to determine nominal operating margins for each device in the ICS. The system developed in this work measures the power output from each device based on each line of code that executes. This data can then map expected power voltages to expected computational commands. Given a specific set of commands, the voltages that can be observed externally will fluctuate predictably. Given that the external monitoring system notes a deviation from power consumption patterns, the system can then detect anomalous behavior. Rather than use data directly from a given PLC, the power data can be used to indicate which command is being executed, and because ladder logic is known, the power outputs should follow a specific path.

**Assessment:**

The work carried out by Roy et al., much like the work done by Formby et al., takes a different approach to securing PLC-based ICS networks. With the understanding that the throughput and efficiency of the ICS network should always be maintained, Roy et al. set out to find another way to validate the operational functionality of each PLC in the ICS process. Because PLCs are simple and the ladder logic they use is predictable and well-known, the power consumption details can be matched to specific PLC operations, and these voltages can then be compared to the ladder logic for validation. This puts the security system outside the ICS and thus ensures the novel fingerprinting security system does not negatively impact the functions of the ICS. The value of this work lies in the purely external nature of the security mechanism.

**Keywords:**

Power, Fingerprinting, External


<hr/>

### 11. Title: [Remote field device fingerprinting using device-specific modbus information](https://ieeexplore.ieee.org/document/7870006)

**Reference:**

_A. Keliris and M. Maniatakos, "Remote field device fingerprinting using device-specific modbus information," 2016 IEEE 59th International Midwest Symposium on Circuits and Systems (MWSCAS), Abu Dhabi, United Arab Emirates, 2016, pp. 1-4, doi: 10.1109/MWSCAS.2016.7870006._

**Summary:**

Device fingerprinting is the practice of determining the unique attributes of different devices and combing these attributes into a unique identifier. Device fingerprinting plays a valuable part in the reconnaissance phase of any malicious attack. These attacks are critically important to understand, especially when dealing with industrial control systems in critical infrastructure processes. This proposes a device fingerprinting scheme wherein the differences between vendor implementation in the Modbus protocol are used to identify and track different devices on a given critical system. Modbus, due to its real-time nature, does not implement any authentication protocols. This work proposes the use of these difference-based Modbus fingerprints as a means to identify and authenticate different devices on a given Modbus system. To test the viability of such a vendor-based fingerprinting scheme, the researchers evaluated modbus-enabled devices that are connected to the internet and indexed by the Shodan search engine. The outcomes of the system indicate that 3% of all Modbus-enabled devices indexed on Shodan were accurately identified based on vendor specifications. This improves Shodan's fingerprinting capabilities by 28%.

**Assessment:**

Much like the work carried out by Roy et al., this work proposes a novel means by which PLCs and ICS-based devices can be accurately fingerprinted for identification and authentication activities. Rather than taking an internal network stance on fingerprinting, this research instead focused on publicly available Modbus-based devices that are registered on the Shodan search engine. While only 308 devices were successfully identified using this novel fingerprinting approach, it demonstrates that there are still many unexplored avenues that can be explored when trying to successfully fingerprint ICS devices.

**Keywords:**

Modbus, Fingerprinting, Identification and Authentication, Recon

<hr/>

### 12. Title: [A Blockchain Architecture to Increase the Resilience of Industrial Control Systems from the Effects of a Ransomware Attack: A Proposal and Initial Results](https://dl.acm.org/doi/10.1145/3637553)

**Reference:**

_Stephen S. Kirkman, Steven Fulton, Jeffrey Hemmes, Christopher Garcia, and Justin C. Wilson. 2024. A Blockchain Architecture to Increase the Resilience of Industrial Control Systems from the Effects of a Ransomware Attack: A Proposal and Initial Results. ACM Trans. Cyber-Phys. Syst. 8, 1, Article 9 (January 2024), 13 pages. https://doi.org/10.1145/3637553_

**Summary:**

ICS and SCADA networks run some of the most critical systems in the United States. The disruption of these systems can cause, at best, chaos and a lack of coordination, and worst, loss of life. Because these systems are so critical, they must be adequately protected. This work proposes a blockchain and the integrity resilience nature of blockchain architectures as a means to protect from ransomware attacks. To implement the blockchain in this model, this research proposes the use of the Historian. This research focuses on the constant running nature of the blockchain process to keep from being encrypted by any ransomware processes. Because the blockchain is always running, ransomware attacks cannot effectively encrypt the data sitting on the blockchain, thus making the blockchain resistant to the ransomware attacks. As the ransomware attack progresses, all the data in the blockchain is kept secure. To encrypt the files being used by the blockchain, the main blockchain function must be killed by the ransomware. Whenever this function is shut down, the system can immediately isolate the device, rendering the ransomware attack useless. 

**Assessment:**

The real value of this work is revealed in the ever-running nature of blockchain operations. By nature, ransomware attacks can only encrypt files that are not locked by any other process. The blockchain architecture proposed in this work ensures that the process that carries out blockchain operations is always running. This ensures that the local blockchain is always locked by some process in the systems as a means to resist encryption by a ransomware package. Many ransomware attacks can target processes for elimination if files cannot be reached. Because the blockchain function must always run, the system itself can run checks to ensure that every device in the system is running the blockchain program. If the program is down, it is likely due to a ransomware attack or some other malformed operation and can thus be immediately isolated. This provides a feasible method for early ransomware detection and isolation.

**Keywords:**

Ransomware, Blockchain, PLC, ICS, SCADA

<hr/>

### 13. Title: [An Innovative Blockchain-Based Traceability Framework for Industry 4.0 Cyber-Physical Factory](https://dl.acm.org/doi/10.1145/3588155.3588174)

**Reference:**

_William Davis, Mahnoor Yaqoob, Luke Bennett, Stefan Mihai, Dang Viet Hung, Ramona Trestian, Mehmet Karamanoglu, Balbir Barn, and Huan Nguyen. 2023. An Innovative Blockchain-Based Traceability Framework for Industry 4.0 Cyber-Physical Factory. In Proceedings of the 2023 5th Asia Pacific Information Technology Conference (APIT '23). Association for Computing Machinery, New York, NY, USA, 118–122. https://doi.org/10.1145/3588155.3588174_

**Summary:**

Traceability allows for all parts and processes in a manufacturing process to be traced, tracked, and assured. This process helps manufacturers ensure quality and efficiency in production. This work proposes a blockchain system that can fulfill all traceability requirements in an industrial system. The system proposed in this work uses an immutable blockchain implementation that facilitates the tracing of all parts and processes in the manufacturing process being tracked. The blockchain architecture is deployed to Rasperri Pis attached to a cyber-physical factory simulator, and the resulting production data is logged, hashed, and attached to the blockchain. The outcomes of this research indicate that a blockchain can be used to verify the authenticity of data within a manufacturing process. 

**Assessment:**

While this work does not focus entirely on the security element, the use of blockchains as a means to track and verify data in an industrial process is useful in all industrial applications. The use in their example, while only applied to tracing manufacturing processes, can also be used to track and predict industrial operations and notify if any anomalies occur. Further, the use of a blockchain in operational tracing can help from a digital forensic perspective as a means to carry out any investigation after an attack occurs. Having trustworthy data to analyze after an event is essential in ensuring that the issue is accurately understood and mitigated.

**Keywords:**

Blockchain, Authenticity, Traceability, Industry 4.0

<hr/>

### 14. Title: [On the Feasibility of Secure Logging for Industrial Control Systems Using Blockchain](https://dl.acm.org/doi/10.1145/3360664.3360668)

**Reference:**

_Stefan Schorradt, Edita Bajramovic, and Felix Freiling. 2019. On the Feasibility of Secure Logging for Industrial Control Systems Using Blockchain. In Proceedings of the Third Central European Cybersecurity Conference (CECC 2019). Association for Computing Machinery, New York, NY, USA, Article 4, 1–6. https://doi.org/10.1145/3360664.3360668_

**Summary:**

Due to the networked nature of all modern ICS systems, the need for sound forensics methodologies in these systems becomes more and more essential. One of the key elements in all forensics investigations is the log files produced in the operation of a given system. By working through log files in a system, investigators can begin to create both a timeline and a picture of just what happened in some cybersecurity event. Due to the importance of such logs in the digital forensics domain, the security of these files must be ensured. If the log files cannot be trusted, there is no real way to be able to understand adequately what happened in a given cyber event. To protect log files from manipulation, some integrity checking mechanism must be introduced to ensure the validity of the files being analyzed. This work proposes the use of a blockchain tracking mechanism that can help ensure the integrity of all the logging data captured during the operation of an ICS system. The system proposed captures logging data from a Siemens SIMATIC S7-1500 and reports the data to the public Ethereum network. The use of the system did ensure the integrity of logging, but the time-intensive nature of the public Ethereum blockchain interactions severely limits the use of this system in real PLC-based systems.

**Assessment:**

This work is directly related to the work done by Davis et al. above and to the work carried out by Jadidi et al. The value in this work, much like the works just mentioned, lies in the benefits blockchains pose when attempting to validate the integrity of captured data. The use of a blockchain can help operations better log and validate the data being captured to ensure that no errors occurred in the storage of the data and no tampering occurred after the data was collected. Interestingly, this work specifically notes the time-intensive nature of using the Ethereum public blockchain architecture and indicates that, due to the slowness of the process, this architecture is likely NOT usable for real-time ICS systems.

**Keywords:**

Logging, Blockchain, Ethereum, Slow

<hr/>

### 15. Title: [Device Fingerprinting for Cyber-Physical Systems: A Survey](https://dl.acm.org/doi/10.1145/3584944)

**Reference:**

_Vijay Kumar and Kolin Paul. 2023. Device Fingerprinting for Cyber-Physical Systems: A Survey. ACM Comput. Surv. 55, 14s, Article 302 (December 2023), 41 pages. https://doi.org/10.1145/3584944_

**Summary:**

Device fingerprinting is used for identification, authentication, conditioning, and security in Cyber-Physical Systems (CPS). Cyber-Physical Systems are systems wherein cyberspace interacts with the physical realm, such as industrial control systems on factory lines, in power grids, water systems, and other critical infrastructure processes. This work aims to canvass the state of the device fingerprinting research available today and try to  distill what has been done into a more understandable set of processes. In their work, the authors investigate different fingerprinting techniques, applications, origins, and characteristics. Fingerprinting is used to identify devices based on unique attributes. It is used to authenticate devices due to the fact that no two devices can generate the same fingerprint. It is used to monitor the conditions of a device due to the predictable patterns in power and operational consumptions that each device exhibits. It is used in tracing and forensics to best understand what device did what and when. The survey created a novel classification scheme that uses physics, operation, and behavioral features to classify fingerprinting techniques. The classification was further refined into passive and active fingerprinting techniques.

**Assessment:**

The key value of this work lies in the breadth of the exploration taken to understanding the state of the art in device fingerprinting for Cyber-Physical Systems. This work will likely be used again and again for all Cyber-Physical device fingerprinting referencing as it contains such a rich set of data relating to the state of device fingerprinting today. The classification scheme and subsequent grouping of techniques are highly useful in this research, especially across the passive/active delineation.

**Keywords:**

Device Fingerprinting, Survey, Classification

<hr/>

### 16. Title: [SymbIoT: Towards An Extensible Blockchain Integration Testbed for IIoT](https://dl.acm.org/doi/10.1145/3609389.3610565)

**Reference:**

_John Hayes, Adel Aneiba, and Mohamed Gaber. 2023. SymbIoT: Towards An Extensible Blockchain Integration Testbed for IIoT. In Proceedings of the 1st Workshop on Enhanced Network Techniques and Technologies for the Industrial IoT to Cloud Continuum (IIoT-NETs '23). Association for Computing Machinery, New York, NY, USA, 8–14. https://doi.org/10.1145/3609389.3610565_

**Summary:**

This work proposes an investigation of distributed ledger technologies in the industrial internet of things. The system proposed by the work is called SymbIoT. SymbIoT uses JSON  and HTTP to connect 31 Raspberry Pi devices for communication. To facilitate communication, the researchers built an API with several endpoints serving data to the devices. ECDSA is used for signatures. This work serves as a proof of concept to simply understand the construction and implementation of a blockchain ledger mechanism distributed between small IoT devices. In application, the researchers were able to verify that multiple consensus algorithms could be used to distribute storage across several devices. While this work did not study the actual effects of such a network on an actual ICS, it produces a novel software/hardware solution that allows flexibility and efficiency when deploying distributed ledgers to disparate devices.

**Assessment:**

The value of this paper lies in the ground-up nature of the work. While the design was theoretical and rather aspirational in nature, the from-scratch application of code to hardware provides useful guidance as to the actual requirements needed to add a separate distributed ledger system to an industrial control network.

**Keywords:**

IIoT, Blockchain, Flexibility

<hr/>

### 17. Title: [A Robust Anomaly Detection Approach for IIoT Time Series](https://dl.acm.org/doi/10.1145/3704558.3707091)

**Reference:**

_Zexin Lu. 2025. A Robust Anomaly Detection Approach for IIoT Time Series. In Proceedings of the 2024 2nd International Conference on Frontiers of Intelligent Manufacturing and Automation (CFIMA '24). Association for Computing Machinery, New York, NY, USA, 168–173. https://doi.org/10.1145/3704558.3707091_


**Summary:**

Time series anomaly detection attempts to glean distinguishable patterns hidden in data to identify anomalies occurring in IIoT networks. The preditability of IIoT operations allows for variations in nominal operational patterns to be harvested from operational data as a means to determine anomalies, unfolding error events, or unfolding attacks. The biggest barriers to successful IIoT time series anomaly detection lie in the noisy nature of IIoT data. This work proposes a time series anomaly detection algorithm called RobAD. The algorithms first divide up the same set of data into sets of different time scale frames. For instance, one set may be a 1-second timescale and be comprised of the data for each second of data. Another set may be a minute timescale and be comprised of the data for each minute of operation. From these different data sets, pattern harvesting occurs as a means to detect existing patterns at each timescale. This work then proposes an encoder call ResMLP that correlates multiple variables across the different time scales. The variable tracking across timescales helps alleviate noise. Next, a time discrepancy block is used to describe nominal patterns for correlation between noise and actual data. 

**Assessment:**

The value in the work carried out by Lu lies in the novel nature of the designed time series anomaly detection mechanism. By acknowledging the part noise plays in the IIoT data and attempting to mitigate such noise in the detection of operational fingerprinting, more robust detection schemes can be designed. This work primarily focuses on the determination of variable patterns across different timescales as a means to resist noise and more accurately track variation in system operations. By carrying out time patching as described above, the system can better determine the actual baseline data from the noise. 

**Keywords:**

Fingerprinting, Anomaly Detection, IIoT

<hr/>

### 18. Title: [Deployment of Cybersecurity Controls in the Norwegian Industry 4.0](https://dl.acm.org/doi/10.1145/3664476.3670896)

**Reference:**

_Kristian Kannelønning and Sokratis Katsikas. 2024. Deployment of Cybersecurity Controls in the Norwegian Industry 4.0. In Proceedings of the 19th International Conference on Availability, Reliability and Security (ARES '24). Association for Computing Machinery, New York, NY, USA, Article 188, 1–8. https://doi.org/10.1145/3664476.3670896_

**Summary:**

An attack on a Cyber-Physical system can be quite severe, leading to not only downtime, lost money, and inconvenience but also to the loss of human life. This work carries out an investigation of multiple industrial organizations in the country of Norway regarding the safeguards they use to protect their Industrial Control Systems. The survey uses the NIST SP 800-82 Rev. 3, "Guide to Operational Technology" as a guide to generate 70 questions for the industries surveyed. The survey contains 38 responses at a 46.9% response rate. The largest industry represented is the Process Industry, while the Healthcare and Discrete and Process Industries were represented the least in the survey. Survey results indicate that the average use of security controls across all respondents is 63%, while 53% of the organizations have security control usage of over 60%. The study indicates that the most widely used control mechanism is the backup of critical software, whereas the least used were training and response planning.

**Assessment:**

The value of this work lies in the robust study of cybersecurity practices in the industries found in Norway. Further, the use of NIST SP 800-82 adds significant validity to the data harvested from the survey. Most of the research described thus far in this study outlines decentralized and fingerprinting technology solutions for ICS networks. This work adds several "Standard" security protocols that can be added to a secure industrial control system design.

**Keywords:**

Survey, Industry Self-Report, NIST

<hr/>

### 19. Title: [SECBlock-IIoT: A Secure Blockchain-enabled Edge Computing Framework for Industrial Internet of Things](https://dl.acm.org/doi/10.1145/3591365.3592945)

**Reference:**

_A. S. M. Sanwar Hosen, Pradip Kumar Sharma, Deepak Puthal, In-Ho Ra, and Gi Hwan Cho. 2023. SECBlock-IIoT: A Secure Blockchain-enabled Edge Computing Framework for Industrial Internet of Things. In Proceedings of the Third International Symposium on Advanced Security on Software and Systems (ASSS '23). Association for Computing Machinery, New York, NY, USA, Article 1, 1–14. https://doi.org/10.1145/3591365.3592945_

**Summary:**

The IIoT is used across many industries and produces a large amount of data in operation. Due to the volume, speed, and criticality of the data produced in the IIoT, the security of IIoT processes is essential. This work describes a peer-to-peer network using a Proof-of-Validation consensus algorithm that facilitates the distributed storage of data, allows the distributed data to be protected, and identifies cyber threats. To build the system, a robust set of registration, verification, and authentication processes were created to add, verify, and authenticate physical devices. Physical Unclonable Functions (PUF) were used to generate device fingerprints and security keys. Operational features were fed to an intelligent thread detection (ITD) module. The ITD used a Recurrent Neural Net to extract notable features from the device data. The system also uses a blockchain to log and protect data.

**Assessment:**

Of all the works canvassed in this study, this work is the closest to what this study is hoping to accomplish. The value in the work carried out by Hosen et al. lies in the robust combination of decentralized technologies to secure an IIoT network. While the network described in this work isn't directly tied to a SCADA or ICS network, it provides valuable insights as to how a more holistic approach can be taken to securing a Cyber-Physical system.

**Keywords:**

Blockchain, Fingerprinting, Physical Unclonable Function

<hr/>

## Survey Keywords: 

- Cyber-Physical Systems
- Industry 4.0
- Industrial Internet of Things
- Blockchain
- Decentralized Ledger Technology
- Fingerprinting
- Time Series Anomaly Detection
- Logging Security
- Secure Logging
- Digital Forensics
- Passive vs Active Monitoring
- Access Control
- Physical Unclonable Function

