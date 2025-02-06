# Annotated Bibliography

[METHODOLOGY](https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Documentation/Methodology.md)

<hr/>

### Title: [A Novel Monitoring System for the Data Integrity of Reactor Protection System Using Blockchain Technology](https://ieeexplore.ieee.org/document/9126779)

**Reference:**

M. K. Choi, C. Y. Yeun and P. H. Seong, "A Novel Monitoring System for the Data Integrity of Reactor Protection System Using Blockchain Technology," in IEEE Access, vol. 8, pp. 118732-118740, 2020, doi: 10.1109/ACCESS.2020.3005134. 

**Summary:**

Nuclear Power Plants (NPP) are isolated from external networks, but are still vulnerable to internal injection attacks via the NPP safety system. To avoid such attacks all internal data must be monitored for data integrity. This work proposes the use of a private blockchain system to monitor the data integrity of the PLCs in the NPP system. The developed blockchain was also used to protect the Reactor Protection Systems. The novel blockchain system can detect code injection. The blockchain used is a private, randomized Proof-of-Authority-based blockchain that stores data contained in PLCS in each block and uses the same randomized PoA mechanism for consensus. The verification of traffic is carried out at each PLC and a majority consensus is used to indicate which PLCs are operating correctly and which are getting errant results. This work calls this process Proof-of-Monitoring. A Merkle Tree is used to store the PLC hash data. Back-tracing algorithms are used to detect data anomalies in the ledger.

**Assessment:**

The work by Choi et al. demonstrates that novel blockchain-based ledger systems have been used with limited success to add layers of security within industrial control systems. While this study does indicate that the system can be used, no data was collected to verify the novel system's effect on safety system performance. 

<hr/>

### Title: [Blockchain architecture for process-level traceability of continuous mixing process in battery cell production](https://ieeexplore.ieee.org/document/10586718)

**Reference:**

S. Otte, L. Reuscher, D. Keller and J. Fleischer, "Blockchain architecture for process-level traceability of continuous mixing process in battery cell production," 2024 1st International Conference on Production Technologies and Systems for E-Mobility (EPTS), Bamberg, Germany, 2024, pp. 1-14, doi: 10.1109/EPTS61482.2024.10586718.

**Summary:**

Lithium-Ion batteries rely on precise mixing of raw materials. This mixing must be tracked to ensure high quality products and compliance with regulations. Due to the continuous variability of raw materials, tracking chemical mixing data is difficult. This work proposes a novel blockchain solution that integrated all PLC mixing data into a blockchain ledger that can be used for quality control, data validation, and legal compliance. The Hyperledger Fabric platform was used to implement the private blockchain using a SHA-256 hashing algorithm and a Proof-of-Authority consensus mechanism. To monitor the PLCs external computers were connected to PLC data busses and passively observed the data state of each PLC via MQTT. The PLC data was then hashed via a JavaScript Hyperledger interface and stored into the blockchain. All additions to the block chain propagate across the network via the PoA consensus mechanism. 


**Assessment:**

The work carried out by Otte et a. provides useful information regarding the actual implementation of a blockchain architecture for the immutable tracking of chemical mix data originating from implemented PLCs. By using the blockchain method, a trusted ledger could be kept that documents, in real time, the PLC mixing data being produced on the battery manufacturing floor. This study shows that PLC data, regardless of content, can be tracked using an immutable trace ledger for either fingerprinting, data validation, intrusion detection, or anomalous behavior. 


<hr/>

### Title: [Blockchain application in simulated environment for Cyber-Physical Systems Security](https://ieeexplore.ieee.org/document/9557446)

**Reference:**

R. Colelli, C. Foglietta, R. Fusacchia, S. Panzieri and F. Pascucci, "Blockchain application in simulated environment for Cyber-Physical Systems Security," 2021 IEEE 19th International Conference on Industrial Informatics (INDIN), Palma de Mallorca, Spain, 2021, pp. 1-7, doi: 10.1109/INDIN45523.2021.9557446.

**Summary:**

Critical Infrastructures often use Industrial Control Systems (ICS). Industrial Control Systems use PLCs. Data and commands from the PLCs that move across the ICS are stored in the Historian, a logging program responsible for tracking logging in the ICS. ICS security comprises not only the operations of the ICS itself, but also the logging systems that keep track of the status of the system. By changing logs, attackers can obfuscate attack trails making digital forensics difficult. This work presents a novel blockchain application that is paired with the ICS historian as a means to immutably store and validate the clear-text logs stored by the Historian. By applying this system, data integrity can be verified for each operation that occurs in the ICS. Beyond data integrity, the proposed blockchain also provides for data recovery given Historian data is maliciously changed or accidentally corrupted. The system was shown to resists Man-in-the-middle and data injection attacks. While the blockchain did provide valuable data protection benefits, if an operator chooses to mangle data before it is recorded in the Historian, this system cannot help. 

**Assessment:**

The work carried out by Colelli et al. demonstrates that novel blockchain applications have been used to track, monitor, and validate PLC data. This research also shows the limitations of the system as applied to the centralized Historian. Though the Historian is a central location for logging data, if data is mangled before reaching the Historian logger, the data verification checks will only check against the corrupted data, thus bypassing the data integrity checks provided by the blockchain system. 

<hr/>

### Title: [Protection against Ransomware in Industrial Control Systems through Decentralization using Blockchain](https://ieeexplore.ieee.org/document/10320188)

**Reference:**

A. Parvizimosaed, H. Azad, D. Amyot and J. Mylopoulos, "Protection against Ransomware in Industrial Control Systems through Decentralization using Blockchain," 2023 20th Annual International Conference on Privacy, Security and Trust (PST), Copenhagen, Denmark, 2023, pp. 1-5, doi: 10.1109/PST58708.2023.10320188.

**Summary:**

**Assessment:**


<hr/>

### Title: [Toward a Failures Model for Communication of Decentralized Applications with Blockchain Networks Applied in the Industrial Environment](https://ieeexplore.ieee.org/document/9857810)

**Reference:**

C. T. B. Garrocho, K. N. Oliveira, A. L. d. Santos, C. F. M. da Cunha Cavalcanti and R. A. R. Oliveira, "Toward a Failures Model for Communication of Decentralized Applications with Blockchain Networks Applied in the Industrial Environment," in IEEE Wireless Communications, vol. 29, no. 3, pp. 40-46, June 2022, doi: 10.1109/MWC.001.2100572.

**Summary:**

**Assessment:**


<hr/>

### Title: [BACE: Blockchain-based Access Control at the Edge for Industrial Control Devices of Industry 4.0](https://ieeexplore.ieee.org/document/9628291)


**Reference:**

C. T. B. Garrocho, K. N. Oliveira, D. J. Sena, C. F. M. da Cunha Cavalcanti and R. A. R. Oliveira, "BACE: Blockchain-based Access Control at the Edge for Industrial Control Devices of Industry 4.0," 2021 XI Brazilian Symposium on Computing Systems Engineering (SBESC), Florianopolis, Brazil, 2021, pp. 1-8, doi: 10.1109/SBESC53686.2021.9628291.

**Summary:**

**Assessment:**


<hr/>

### Title: [Securing Manufacturing Using Blockchain](https://ieeexplore.ieee.org/document/9343190)

**Reference:**

Z. Jadidi, A. Dorri, R. Jurdak and C. Fidge, "Securing Manufacturing Using Blockchain," 2020 IEEE 19th International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom), Guangzhou, China, 2020, pp. 1920-1925, doi: 10.1109/TrustCom50675.2020.00262.

**Summary:**

**Assessment:**


<hr/>

### Title: [PLCPrint: Fingerprinting Memory Attacks in Programmable Logic Controllers](https://ieeexplore.ieee.org/document/10130481)

**Reference:**

M. M. Cook, A. K. Marnerides and D. Pezaros, "PLCPrint: Fingerprinting Memory Attacks in Programmable Logic Controllers," in IEEE Transactions on Information Forensics and Security, vol. 18, pp. 3376-3387, 2023, doi: 10.1109/TIFS.2023.3277688.

**Summary:**

**Assessment:**


<hr/>

### Title: [Fingerprinting for Cyber-Physical System Security: Device Physics Matters Too](https://ieeexplore.ieee.org/document/8490185)

**Reference:**

Q. Gu, D. Formby, S. Ji, H. Cam and R. Beyah, "Fingerprinting for Cyber-Physical System Security: Device Physics Matters Too," in IEEE Security & Privacy, vol. 16, no. 5, pp. 49-59, September/October 2018, doi: 10.1109/MSP.2018.3761722.


**Summary:**

**Assessment:**


<hr/>

### Title: [Optimized fingerprint generation using unintentional emission radio-frequency distinct native attributes (RF-DNA)](https://ieeexplore.ieee.org/document/7045829)

**Reference:**

R. D. Deppensmith and S. J. Stone, "Optimized fingerprint generation using unintentional emission radio-frequency distinct native attributes (RF-DNA)," NAECON 2014 - IEEE National Aerospace and Electronics Conference, Dayton, OH, USA, 2014, pp. 327-330, doi: 10.1109/NAECON.2014.7045829.

**Summary:**

**Assessment:**


<hr/>

### Title: [Power Measurement Based Code Classification for Programmable Logic Circuits](https://ieeexplore.ieee.org/document/8642680)

**Reference:**

T. Roy and A. A. L. Beex, "Power Measurement Based Code Classification for Programmable Logic Circuits," 2018 IEEE International Symposium on Signal Processing and Information Technology (ISSPIT), Louisville, KY, USA, 2018, pp. 644-648, doi: 10.1109/ISSPIT.2018.8642680.

**Summary:**

**Assessment:**


<hr/>

### Title: [Remote field device fingerprinting using device-specific modbus information](https://ieeexplore.ieee.org/document/7870006)

**Reference:**

A. Keliris and M. Maniatakos, "Remote field device fingerprinting using device-specific modbus information," 2016 IEEE 59th International Midwest Symposium on Circuits and Systems (MWSCAS), Abu Dhabi, United Arab Emirates, 2016, pp. 1-4, doi: 10.1109/MWSCAS.2016.7870006.

**Summary:**

**Assessment:**


<hr/>

### Title: [A Blockchain Architecture to Increase the Resilience of Industrial Control Systems from the Effects of a Ransomware Attack: A Proposal and Initial Results](https://dl.acm.org/doi/10.1145/3637553)

**Reference:**

Stephen S. Kirkman, Steven Fulton, Jeffrey Hemmes, Christopher Garcia, and Justin C. Wilson. 2024. A Blockchain Architecture to Increase the Resilience of Industrial Control Systems from the Effects of a Ransomware Attack: A Proposal and Initial Results. ACM Trans. Cyber-Phys. Syst. 8, 1, Article 9 (January 2024), 13 pages. https://doi.org/10.1145/3637553

**Summary:**

**Assessment:**


<hr/>

### Title: [An Innovative Blockchain-Based Traceability Framework for Industry 4.0 Cyber-Physical Factory](https://dl.acm.org/doi/10.1145/3588155.3588174)

**Reference:**

William Davis, Mahnoor Yaqoob, Luke Bennett, Stefan Mihai, Dang Viet Hung, Ramona Trestian, Mehmet Karamanoglu, Balbir Barn, and Huan Nguyen. 2023. An Innovative Blockchain-Based Traceability Framework for Industry 4.0 Cyber-Physical Factory. In Proceedings of the 2023 5th Asia Pacific Information Technology Conference (APIT '23). Association for Computing Machinery, New York, NY, USA, 118–122. https://doi.org/10.1145/3588155.3588174

**Summary:**

**Assessment:**


<hr/>

### Title: [On the Feasibility of Secure Logging for Industrial Control Systems Using Blockchain](https://dl.acm.org/doi/10.1145/3360664.3360668)

**Reference:**

Stefan Schorradt, Edita Bajramovic, and Felix Freiling. 2019. On the Feasibility of Secure Logging for Industrial Control Systems Using Blockchain. In Proceedings of the Third Central European Cybersecurity Conference (CECC 2019). Association for Computing Machinery, New York, NY, USA, Article 4, 1–6. https://doi.org/10.1145/3360664.3360668

**Summary:**

**Assessment:**


<hr/>

### Title: [Device Fingerprinting for Cyber-Physical Systems: A Survey](https://dl.acm.org/doi/10.1145/3584944)

**Reference:**

Vijay Kumar and Kolin Paul. 2023. Device Fingerprinting for Cyber-Physical Systems: A Survey. ACM Comput. Surv. 55, 14s, Article 302 (December 2023), 41 pages. https://doi.org/10.1145/3584944

**Summary:**

**Assessment:**


<hr/>

### Title: [SymbIoT: Towards An Extensible Blockchain Integration Testbed for IIoT](https://dl.acm.org/doi/10.1145/3609389.3610565)

**Reference:**

John Hayes, Adel Aneiba, and Mohamed Gaber. 2023. SymbIoT: Towards An Extensible Blockchain Integration Testbed for IIoT. In Proceedings of the 1st Workshop on Enhanced Network Techniques and Technologies for the Industrial IoT to Cloud Continuum (IIoT-NETs '23). Association for Computing Machinery, New York, NY, USA, 8–14. https://doi.org/10.1145/3609389.3610565

**Summary:**

**Assessment:**


<hr/>

### Title: [A Robust Anomaly Detection Approach for IIoT Time Series](https://dl.acm.org/doi/10.1145/3704558.3707091)

**Reference:**

Zexin Lu. 2025. A Robust Anomaly Detection Approach for IIoT Time Series. In Proceedings of the 2024 2nd International Conference on Frontiers of Intelligent Manufacturing and Automation (CFIMA '24). Association for Computing Machinery, New York, NY, USA, 168–173. https://doi.org/10.1145/3704558.3707091


**Summary:**

**Assessment:**


<hr/>

### Title: [Deployment of Cybersecurity Controls in the Norwegian Industry 4.0](https://dl.acm.org/doi/10.1145/3664476.3670896)

**Reference:**

Kristian Kannelønning and Sokratis Katsikas. 2024. Deployment of Cybersecurity Controls in the Norwegian Industry 4.0. In Proceedings of the 19th International Conference on Availability, Reliability and Security (ARES '24). Association for Computing Machinery, New York, NY, USA, Article 188, 1–8. https://doi.org/10.1145/3664476.3670896

**Summary:**

**Assessment:**


<hr/>

### Title: [SECBlock-IIoT: A Secure Blockchain-enabled Edge Computing Framework for Industrial Internet of Things](https://dl.acm.org/doi/10.1145/3591365.3592945)

**Reference:**

A. S. M. Sanwar Hosen, Pradip Kumar Sharma, Deepak Puthal, In-Ho Ra, and Gi Hwan Cho. 2023. SECBlock-IIoT: A Secure Blockchain-enabled Edge Computing Framework for Industrial Internet of Things. In Proceedings of the Third International Symposium on Advanced Security on Software and Systems (ASSS '23). Association for Computing Machinery, New York, NY, USA, Article 1, 1–14. https://doi.org/10.1145/3591365.3592945

**Summary:**

**Assessment:**


<hr/>

