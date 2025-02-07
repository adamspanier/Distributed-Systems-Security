# Annotated Bibliography

[METHODOLOGY](https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Documentation/Methodology.md)

<hr/>

### 1. Title: [A Novel Monitoring System for the Data Integrity of Reactor Protection System Using Blockchain Technology](https://ieeexplore.ieee.org/document/9126779)

**Reference:**

_M. K. Choi, C. Y. Yeun and P. H. Seong, "A Novel Monitoring System for the Data Integrity of Reactor Protection System Using Blockchain Technology," in IEEE Access, vol. 8, pp. 118732-118740, 2020, doi: 10.1109/ACCESS.2020.3005134._

**Summary:**

Nuclear Power Plants (NPP) are isolated from external networks, but are still vulnerable to internal injection attacks via the NPP safety system. To avoid such attacks all internal data must be monitored for data integrity. This work proposes the use of a private blockchain system to monitor the data integrity of the PLCs in the NPP system. The developed blockchain was also used to protect the Reactor Protection Systems. The novel blockchain system can detect code injection. The blockchain used is a private, randomized Proof-of-Authority-based blockchain that stores data contained in PLCS in each block and uses the same randomized PoA mechanism for consensus. The verification of traffic is carried out at each PLC and a majority consensus is used to indicate which PLCs are operating correctly and which are getting errant results. This work calls this process Proof-of-Monitoring. A Merkle Tree is used to store the PLC hash data. Back-tracing algorithms are used to detect data anomalies in the ledger.

**Assessment:**

The work by Choi et al. demonstrates that novel blockchain-based ledger systems have been used with limited success to add layers of security within industrial control systems. While this study does indicate that the system can be used, no data was collected to verify the novel system's effect on safety system performance. 

**Keywords:**

Blockchain, Proof of Authority, Data Integrity

<hr/>

### 2. Title: [Blockchain architecture for process-level traceability of continuous mixing process in battery cell production](https://ieeexplore.ieee.org/document/10586718)

**Reference:**

_S. Otte, L. Reuscher, D. Keller and J. Fleischer, "Blockchain architecture for process-level traceability of continuous mixing process in battery cell production," 2024 1st International Conference on Production Technologies and Systems for E-Mobility (EPTS), Bamberg, Germany, 2024, pp. 1-14, doi: 10.1109/EPTS61482.2024.10586718._

**Summary:**

Lithium-Ion batteries rely on precise mixing of raw materials. This mixing must be tracked to ensure high quality products and compliance with regulations. Due to the continuous variability of raw materials, tracking chemical mixing data is difficult. This work proposes a novel blockchain solution that integrated all PLC mixing data into a blockchain ledger that can be used for quality control, data validation, and legal compliance. The Hyperledger Fabric platform was used to implement the private blockchain using a SHA-256 hashing algorithm and a Proof-of-Authority consensus mechanism. To monitor the PLCs external computers were connected to PLC data busses and passively observed the data state of each PLC via MQTT. The PLC data was then hashed via a JavaScript Hyperledger interface and stored into the blockchain. All additions to the block chain propagate across the network via the PoA consensus mechanism. 

**Assessment:**

The work carried out by Otte et a. provides useful information regarding the actual implementation of a blockchain architecture for the immutable tracking of chemical mix data originating from implemented PLCs. By using the blockchain method, a trusted ledger could be kept that documents, in real time, the PLC mixing data being produced on the battery manufacturing floor. This study shows that PLC data, regardless of content, can be tracked using an immutable trace ledger for either fingerprinting, data validation, intrusion detection, or anomalous behavior. 

**Keywords:**

Blockchain, Proof of Authority, Data Integrity


<hr/>

### 3. Title: [Blockchain application in simulated environment for Cyber-Physical Systems Security](https://ieeexplore.ieee.org/document/9557446)

**Reference:**

_R. Colelli, C. Foglietta, R. Fusacchia, S. Panzieri and F. Pascucci, "Blockchain application in simulated environment for Cyber-Physical Systems Security," 2021 IEEE 19th International Conference on Industrial Informatics (INDIN), Palma de Mallorca, Spain, 2021, pp. 1-7, doi: 10.1109/INDIN45523.2021.9557446._

**Summary:**

Critical Infrastructures often use Industrial Control Systems (ICS). Industrial Control Systems use PLCs. Data and commands from the PLCs that move across the ICS are stored in the Historian, a logging program responsible for tracking logging in the ICS. ICS security comprises not only the operations of the ICS itself, but also the logging systems that keep track of the status of the system. By changing logs, attackers can obfuscate attack trails making digital forensics difficult. This work presents a novel blockchain application that is paired with the ICS historian as a means to immutably store and validate the clear-text logs stored by the Historian. By applying this system, data integrity can be verified for each operation that occurs in the ICS. Beyond data integrity, the proposed blockchain also provides for data recovery given Historian data is maliciously changed or accidentally corrupted. The system was shown to resists Man-in-the-middle and data injection attacks. While the blockchain did provide valuable data protection benefits, if an operator chooses to mangle data before it is recorded in the Historian, this system cannot help. 

**Assessment:**

The work carried out by Colelli et al. demonstrates that novel blockchain applications have been used to track, monitor, and validate PLC data. This research also shows the limitations of the system as applied to the centralized Historian. Though the Historian is a central location for logging data, if data is mangled before reaching the Historian logger, the data verification checks will only check against the corrupted data, thus bypassing the data integrity checks provided by the blockchain system. 

**Keywords:**

SCADA, Blockchain, Historian, Data Integrity

<hr/>

### 4. Title: [Protection against Ransomware in Industrial Control Systems through Decentralization using Blockchain](https://ieeexplore.ieee.org/document/10320188)

**Reference:**

_A. Parvizimosaed, H. Azad, D. Amyot and J. Mylopoulos, "Protection against Ransomware in Industrial Control Systems through Decentralization using Blockchain," 2023 20th Annual International Conference on Privacy, Security and Trust (PST), Copenhagen, Denmark, 2023, pp. 1-5, doi: 10.1109/PST58708.2023.10320188._

**Summary:**
ICSs are susceptible to Ransomware attacks due to their highly centralized architecture. Centralization is necessary in ICSs to maximize efficiency and functionality and is, thus, unavoidable. This work introduces a decentralized blockchain that replicates critical data and distributes this data across a peer-to-peer network using a consensus algorithm. The distributed nature of the network protects against any single point of failure. To protect the network further,a  zero trust architecture is introduced such that all host-to-host and host-to-network transactions must be authorized. This research introduces a Blockchain-Based Industrial Control System (BBICS) that stores and processes critical data on the blockchain via a set of time-series databases. Non-sensitive data is handled off chain. 

**Assessment:**

The work carried out by Parvizimosaed et al. takes a more functional perspective by focusing not only on a the creation of  a robust blockchain ICS system, but also on building a blockchain that tries to maximize the efficiency of the system. By distributing critical information across the network, this system provided full data recovery after a ransomware attack that affected 40% of all devices on the chain. 

**Keywords:**

Blockchain, Ransomware, Efficiency

<hr/>

### 5. Title: [Toward a Failures Model for Communication of Decentralized Applications with Blockchain Networks Applied in the Industrial Environment](https://ieeexplore.ieee.org/document/9857810)

**Reference:**

_C. T. B. Garrocho, K. N. Oliveira, A. L. d. Santos, C. F. M. da Cunha Cavalcanti and R. A. R. Oliveira, "Toward a Failures Model for Communication of Decentralized Applications with Blockchain Networks Applied in the Industrial Environment," in IEEE Wireless Communications, vol. 29, no. 3, pp. 40-46, June 2022, doi: 10.1109/MWC.001.2100572._

**Summary:**

Communication failures on IIoT networks present a critical problem for operational continuity. This work analyzes failure points in the consensus algorithms of a blockchain-based decentralized industrial application. During the research, each communication failure that occurred int he network is documented, defined, and classified. After analysis, countermeasures for each failure are presented in a novel failure model for decentralized communication networks in industrial applications. The purpose of this work is not to test blockchain functionality in IDCs, but rather to analyze subsequent supporting systems that can help alleviate pain points common to decentralized ledger systems in industrial control applications. 

**Assessment:**

The work carried out by Garrocho et al. presents a new angle on blockchain-based ICS research; that is, the research focuses on how to shore up known weaknesses and failure points when applying blockchain and decentralized primitives to industrial control systems. This work provides value in that it demonstrates the need for a holistic approach when applying decentralized architectures to ICS applications. 

**Keywords:**

Blockchain, Failure Models, Blockchain Support


<hr/>

### 6. Title: [BACE: Blockchain-based Access Control at the Edge for Industrial Control Devices of Industry 4.0](https://ieeexplore.ieee.org/document/9628291)


**Reference:**

_C. T. B. Garrocho, K. N. Oliveira, D. J. Sena, C. F. M. da Cunha Cavalcanti and R. A. R. Oliveira, "BACE: Blockchain-based Access Control at the Edge for Industrial Control Devices of Industry 4.0," 2021 XI Brazilian Symposium on Computing Systems Engineering (SBESC), Florianopolis, Brazil, 2021, pp. 1-8, doi: 10.1109/SBESC53686.2021.9628291._

**Summary:**

The Industrial Internet of Things(IIoT) has immediate implication for Industry 4.0. Blockchain has immediate potential for these systems due to it's ability to provide traceable and auditable access control. Applying blockchain to cloud infrastructures is difficult due to cost and communication latencies. This work proposes a blockchain architecture called BACE that puts the access control at the edge with the devices that are carrying out access requests. This work takes into account the real-time limitations imposed upon most ICS networks. This real-time sensitivity is likely why blockchain applications have yet to be applied to IIoT systems. BACE uses Smart Contracts and edge-based computing to build a flexible and scalable blockchain communication approach to manage access requests. To mitigate the storage and computational eff4ects of the system via local storage of the PLC, this work focuses on creating a compact JSON-based formate that only takes a few bytes of storage.

**Assessment:**

The value of this paper lies in the acknowledgment that time constraints are limiting factors in real-time application environments. Cloud-based IIoT is useful, but causes latencies due to digital communications delays. This work creates an "edge" based blockchain that is stored locally on PLCs and propagated across the PLC network. To mitigate the storage and computational requirements of the system, this work created a slim JSON-based storage format that takes only a few bytes of memory to alleviate many of the overhead issues presented by decentralized cryptographic security mechanisms. 

**Keywords:**

Blockchain, Edge, Cloud, Eliminate Communication Latency, Real-Time

<hr/>

### 7. Title: [Securing Manufacturing Using Blockchain](https://ieeexplore.ieee.org/document/9343190)

**Reference:**

_Z. Jadidi, A. Dorri, R. Jurdak and C. Fidge, "Securing Manufacturing Using Blockchain," 2020 IEEE 19th International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom), Guangzhou, China, 2020, pp. 1920-1925, doi: 10.1109/TrustCom50675.2020.00262._

**Summary:**

ICS attacks generally use a phased approach during execution. Current frameworks can generally only scan a single data source and thus cannot detect all possible vectors as an attack is unfolding. The work proposes a two stage security systems wherein a blockchain is used to securely store ICS data in a distributed manner and a deep learning system is used to analyze the blockchain for anomalous behavior. The proposed design was implemented and tested for functionality demonstrating a a high level of precision; comparable to systems that only analyze a single data source. Upon the discovery of an anomaly, other manufacturers can be notified. The work proposed a public logging blockchain for inter-manufacturer communications concerning manufacturing attacks and anomalies.

**Assessment:**

The work carried out by Jadidi et al. provides value by not only implementing a blockchain structure for data analysis, but also a deep learning mechanism wherein data streams are analyzed for patterns and anomalies detected. The outcomes of the work show that multi-stream blockchain analysis is possible using artificial intelligence functionalities.

**Keywords:**

Blockchain, Deep Learning, Logging

<hr/>

### 8. Title: [PLCPrint: Fingerprinting Memory Attacks in Programmable Logic Controllers](https://ieeexplore.ieee.org/document/10130481)

**Reference:**

M. M. Cook, A. K. Marnerides and D. Pezaros, "PLCPrint: Fingerprinting Memory Attacks in Programmable Logic Controllers," in IEEE Transactions on Information Forensics and Security, vol. 18, pp. 3376-3387, 2023, doi: 10.1109/TIFS.2023.3277688.

**Summary:**

A common attack vector in PLC memory is the malicious alteration of internal PLC memory. These memory attacks cause the PLC to function in ways that are not consistent with their operating environments. While memory attacks are a critical security issue in PLC protection, different types of memory attacks themselves can manifest similar physical manifestations. This makes attack triage and digital forensics difficult and often quite expensive. Adding to the damage, misbehaving PLCs can cause interruptions of work resulting in financial losses as well as physical damage, and in some cases, even result in the loss of life.  This work proposes a novel system that maps PLC register state to a set of Mapping Conditions (MC) as a means to indicate if they exist in PLC memory artifacts. These MCs are then modeled and mapped as a means to predict PLC behavior. The study shows how MC deviations can be detected using a supervised learning scheme to accurately determine the occurrence of memory attacks. This work fills the need for attack technique triaging as it allows attacks to be more accurately described, logged, and mitigated.

**Assessment:**

This work is useful in it's descriptions of memory fingerprinting as a means to predict and identify deviations from nominal operations. The use of memory fingerprinting to identify well-know operation patterns helps identify when deviations occur. This work also provides a robust background and related work section that provides essential information regarding other memory fingerprinting applications.

**Keywords:**

Fingerprinting, Attack Detection, Triaging

<hr/>

### 9. Title: [Fingerprinting for Cyber-Physical System Security: Device Physics Matters Too](https://ieeexplore.ieee.org/document/8490185)

**Reference:**

Q. Gu, D. Formby, S. Ji, H. Cam and R. Beyah, "Fingerprinting for Cyber-Physical System Security: Device Physics Matters Too," in IEEE Security & Privacy, vol. 16, no. 5, pp. 49-59, September/October 2018, doi: 10.1109/MSP.2018.3761722.


**Summary:**

**Assessment:**

**Keywords:**


<hr/>

### 10. Title: [Optimized fingerprint generation using unintentional emission radio-frequency distinct native attributes (RF-DNA)](https://ieeexplore.ieee.org/document/7045829)

**Reference:**

R. D. Deppensmith and S. J. Stone, "Optimized fingerprint generation using unintentional emission radio-frequency distinct native attributes (RF-DNA)," NAECON 2014 - IEEE National Aerospace and Electronics Conference, Dayton, OH, USA, 2014, pp. 327-330, doi: 10.1109/NAECON.2014.7045829.

**Summary:**

**Assessment:**

**Keywords:**


<hr/>

### 11. Title: [Power Measurement Based Code Classification for Programmable Logic Circuits](https://ieeexplore.ieee.org/document/8642680)

**Reference:**

T. Roy and A. A. L. Beex, "Power Measurement Based Code Classification for Programmable Logic Circuits," 2018 IEEE International Symposium on Signal Processing and Information Technology (ISSPIT), Louisville, KY, USA, 2018, pp. 644-648, doi: 10.1109/ISSPIT.2018.8642680.

**Summary:**

**Assessment:**

**Keywords:**


<hr/>

### 12. Title: [Remote field device fingerprinting using device-specific modbus information](https://ieeexplore.ieee.org/document/7870006)

**Reference:**

A. Keliris and M. Maniatakos, "Remote field device fingerprinting using device-specific modbus information," 2016 IEEE 59th International Midwest Symposium on Circuits and Systems (MWSCAS), Abu Dhabi, United Arab Emirates, 2016, pp. 1-4, doi: 10.1109/MWSCAS.2016.7870006.

**Summary:**

**Assessment:**

**Keywords:**


<hr/>

### 13. Title: [A Blockchain Architecture to Increase the Resilience of Industrial Control Systems from the Effects of a Ransomware Attack: A Proposal and Initial Results](https://dl.acm.org/doi/10.1145/3637553)

**Reference:**

Stephen S. Kirkman, Steven Fulton, Jeffrey Hemmes, Christopher Garcia, and Justin C. Wilson. 2024. A Blockchain Architecture to Increase the Resilience of Industrial Control Systems from the Effects of a Ransomware Attack: A Proposal and Initial Results. ACM Trans. Cyber-Phys. Syst. 8, 1, Article 9 (January 2024), 13 pages. https://doi.org/10.1145/3637553

**Summary:**

**Assessment:**

**Keywords:**



<hr/>

### 14. Title: [An Innovative Blockchain-Based Traceability Framework for Industry 4.0 Cyber-Physical Factory](https://dl.acm.org/doi/10.1145/3588155.3588174)

**Reference:**

William Davis, Mahnoor Yaqoob, Luke Bennett, Stefan Mihai, Dang Viet Hung, Ramona Trestian, Mehmet Karamanoglu, Balbir Barn, and Huan Nguyen. 2023. An Innovative Blockchain-Based Traceability Framework for Industry 4.0 Cyber-Physical Factory. In Proceedings of the 2023 5th Asia Pacific Information Technology Conference (APIT '23). Association for Computing Machinery, New York, NY, USA, 118–122. https://doi.org/10.1145/3588155.3588174

**Summary:**

**Assessment:**

**Keywords:**



<hr/>

### 15. Title: [On the Feasibility of Secure Logging for Industrial Control Systems Using Blockchain](https://dl.acm.org/doi/10.1145/3360664.3360668)

**Reference:**

Stefan Schorradt, Edita Bajramovic, and Felix Freiling. 2019. On the Feasibility of Secure Logging for Industrial Control Systems Using Blockchain. In Proceedings of the Third Central European Cybersecurity Conference (CECC 2019). Association for Computing Machinery, New York, NY, USA, Article 4, 1–6. https://doi.org/10.1145/3360664.3360668

**Summary:**

**Assessment:**

**Keywords:**



<hr/>

### 16. Title: [Device Fingerprinting for Cyber-Physical Systems: A Survey](https://dl.acm.org/doi/10.1145/3584944)

**Reference:**

Vijay Kumar and Kolin Paul. 2023. Device Fingerprinting for Cyber-Physical Systems: A Survey. ACM Comput. Surv. 55, 14s, Article 302 (December 2023), 41 pages. https://doi.org/10.1145/3584944

**Summary:**

**Assessment:**

**Keywords:**


<hr/>

### 17. Title: [SymbIoT: Towards An Extensible Blockchain Integration Testbed for IIoT](https://dl.acm.org/doi/10.1145/3609389.3610565)

**Reference:**

John Hayes, Adel Aneiba, and Mohamed Gaber. 2023. SymbIoT: Towards An Extensible Blockchain Integration Testbed for IIoT. In Proceedings of the 1st Workshop on Enhanced Network Techniques and Technologies for the Industrial IoT to Cloud Continuum (IIoT-NETs '23). Association for Computing Machinery, New York, NY, USA, 8–14. https://doi.org/10.1145/3609389.3610565

**Summary:**

**Assessment:**

**Keywords:**


<hr/>

### 18. Title: [A Robust Anomaly Detection Approach for IIoT Time Series](https://dl.acm.org/doi/10.1145/3704558.3707091)

**Reference:**

Zexin Lu. 2025. A Robust Anomaly Detection Approach for IIoT Time Series. In Proceedings of the 2024 2nd International Conference on Frontiers of Intelligent Manufacturing and Automation (CFIMA '24). Association for Computing Machinery, New York, NY, USA, 168–173. https://doi.org/10.1145/3704558.3707091


**Summary:**

**Assessment:**

**Keywords:**



<hr/>

### 19. Title: [Deployment of Cybersecurity Controls in the Norwegian Industry 4.0](https://dl.acm.org/doi/10.1145/3664476.3670896)

**Reference:**

Kristian Kannelønning and Sokratis Katsikas. 2024. Deployment of Cybersecurity Controls in the Norwegian Industry 4.0. In Proceedings of the 19th International Conference on Availability, Reliability and Security (ARES '24). Association for Computing Machinery, New York, NY, USA, Article 188, 1–8. https://doi.org/10.1145/3664476.3670896

**Summary:**

**Assessment:**

**Keywords:**



<hr/>

### 20. Title: [SECBlock-IIoT: A Secure Blockchain-enabled Edge Computing Framework for Industrial Internet of Things](https://dl.acm.org/doi/10.1145/3591365.3592945)

**Reference:**

A. S. M. Sanwar Hosen, Pradip Kumar Sharma, Deepak Puthal, In-Ho Ra, and Gi Hwan Cho. 2023. SECBlock-IIoT: A Secure Blockchain-enabled Edge Computing Framework for Industrial Internet of Things. In Proceedings of the Third International Symposium on Advanced Security on Software and Systems (ASSS '23). Association for Computing Machinery, New York, NY, USA, Article 1, 1–14. https://doi.org/10.1145/3591365.3592945

**Summary:**

**Assessment:**

**Keywords:**



<hr/>

