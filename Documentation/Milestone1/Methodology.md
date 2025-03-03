# Project Methodology
[HOME](https://github.com/adamspanier/Distributed-Systems-Security)

## 1.0 Literature Review Methodology

This research uses a three step literature review methodology to generate a literature corpus for further analysis. The three steps used are: _1) the literature search, 2) literature selection_, and _3) literature synthesis_. The literature search sees a keyword-based search string applied to two research databases. The literature selection process applies specific criteria to each pertinent paper for inclusion into the research corpus. Finally, the literature synthesis section discusses the findings of the literature search.

The literature review sees a set of keywords combined into logical search strings. These strings are applied to two specific databases. The query results are analyzed and literature in the results that meets selection criteria are added to the research corpus. Upon the completion of the corpus, all added literature is analyzed, grouped, categorized, and discussed regarding relevance to the topic of this research.

### 1.1 Literature Search Keywords

The literature search uses the following keywords: 
1. _PLC_
2. _Programmable Logic Controller_
3. _Blockchain_
4. _Fingerprinting_

These keywords are used due to their relevance to the topic at hand. Terms _one (1)_ and _two (2)_ relate to PLCs and terms _three (3)_ and _four (4)_ relate to decentralized or novel cryptographic applications.

The following terms are also used due to the discovery of emergent terminology in applying the search method:
1. _IIoT_
2. _Industry 4.0_

Based on the keywords above, the following search strings are used:
1. _PLC Blockchain_
2. _PLC Fingerprinting_
3. _Programmable Logic Controller Blockchain_
4. _Programmable Logic Controller Fingerprinting_
5. _IIoT_
6. _Industry 4.0_

### 1.2 Literature Search Databases

The following Databases will be used in this literature search:
1. _IEEE Xplore_
2. _The ACM Digital Library_

During the search, snowballing will be used to add pertinent literature to the selection candidates.

### 1.3 Literature selection

To be added to the research corpus, each relevant literature candidate must be:
1. _relevant to the research topic_
2. _published in either an IEEE or ACM sanctioned publication_
3. _a full research paper_
4. _written in English_
5. _published within the last five (5) years_

Upon addition to the research corpus, snowballing can be used to add related works to the literature corpus for review.

### 1.4 Literature Synthesis

Upon completion of the research corpus, the included literature will be analyzed for common themes. Literature with similar themes will be grouped together. Each grouping will be categorized and given a name. Each category will be described briefly based on the literature included, and an overview of the findings will be discussed.

## 2.0 Literature Review

### 2.1 Review Results

After conducting the systematic literature review described above, nineteen (19) relevant pieces of literature were added to the research corpus. From these works, the following three (3) categories emerged: 1) Data Integrity Protection (DIP), 2) Device Fingerprinting (DF), and 3) Decentralized System Design (DSD). In the DIP category , two (2) sub-categories were identified: 1) Centralized Protection and 2) Decentralized Protection. In the DF category, two sub-categories were identified: 1) Anomalous Behavior Detection and 2) General Fingerprinting. In the DSD category, the following two (2) categories emerged: 1) Supporting Decentralized System Weaknesses and 2) Combining Decentralized Protections.

Of the nineteen (19) works analyzed in this literature review, ten (10) fell into the DIP classification. Of the 10 in the DIP classification, three (3) were added to the Centralized Protection classification and seven (7) to the Decentralized Protection classification. Six (6) of the works in this review were added to the DF classification. Of the six (6) works in the DF category, three (3) were added to the Anomalous Behavior Detection sub category and three (3) were added to the General Fingerprinting sub-category. The remaining three (3) works were added to the DSD category. Of the three (3) in the DSD category, one (1) was added to the Supporting Decentralized System Weaknesses sub-category and two (2) were added to the Combining Decentralized Protections sub-category.

**2.1.0 - Data Integrity Protection**

Relating to Centralized Data Protection, Colelli et al. [3] propose a blockchain ledger associated with an ICS Historian as a means to provide immutable data tracking for all PLC-related data via a data integrity scanner on the blockchain. Davis et al. [13] propose a blockchain-based traceability solution wherein all parts and processes of a given manufacturing system are logged, hashed, and appended to the blockchain for quality assurance validation. Schorradt et al. [14] chose to carry out a design much like Davis et al. but rather than a novel-private blockchain, the researchers chose to add the data to the public Ethereum blockchain. While the application created by Schorradt et al. worked, the use of the public Ethereum blockchain indicated prohibitively slow speeds for real-time operating systems.

Relating to Decentralized Data Protection, Choi et al. [1] propose a decentralized blockchain-based data storage system for both data protection and for secure, immutable logging in a Nuclear Power Plant. Otte et al. [2] propose a blockchain for process level traceability in mixing battery chemicals as a means to verify compliance with quality requirements and chemical regulations. Parvizimosaed et al. [4] present a decentralized ledger storage scheme that allows PLC data to be stored at the edge with the PLCs as a means to resist ransomware attacks. Garrocho et al. [6] present a novel blockchain based access control mechanism for cloud-based Industrial Internet of Things (IIoT) devices housed at the edge for faster and more secure PLC authentications. Jadidi et al. [7] carry out a blockchain much like other works in this category, but add a deep learning layer to help identify anomalous ICS behaviors. Kirkman et al. [12] provide a ransomware-resistant design that relies on OS-file locks and the ever-running nature of blockchain software to both resist and detect ransomware intrusions. Hayes et al. [16] created a ground-up Raspberri Pi-based communication ledger for IIoT-based decentralized data storage.

**2.1.1 - Fingerprinting**

Relating to Anomalous Behavior Detection, Cook et al. [8] present a PLC fingerprinting mechanism using the memory contents of each PLC as a means to map memory patterns against known Memory Mapping conditions. Formby et al. [9] present a physics and timing-based fingerprinting mechanism wherein residual signals and timing artifacts are measured for each PLC as a means to accurately detect anomalous behavior. Lu et al [17] present a novel noise reduction scheme for the identification of time-based anomalies in IIoT traffic.

Relating to General Fingerprinting, Roy et al. [10] present an external, power consumption-based fingerprinting algorithm wherein the power signatures of PLCs are measured and documented in nominal operations and subsequently measured for anomalous behaviors. Keliris et al. [11] present a system wherein the application of modbus functionality allows the system to predict different PLC models. Kumar et al. [15] make a deep dive on the state of the art regarding all fingerprinting techniques and methodologies.

**2.1.2 - Decentralized System Design**

Relating to the support of known decentralized system weaknesses, Garracho et al. [5] propose a failure model to help security professionals shore up known weaknesses in IIoT systems enabled with decentralized security. 

Relating to the combination of decentralized protections in industrial control systems, Kannelonning et al. [18] categorizes security protections in Norwegian industry and Hosen et al. [19] design a prototype decentralized security system for an industrial control system.

**2.1.3 - Annotated Bibliography**

The annotated bibliography produced in this literature survey can be found [HERE](https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Documentation/AnnotatedBibliography.md).

### 2.2 Keywords

From the literature review the following notable keywords emerged:

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

### 2.3 Literature Review Discussion

Based on the literature review carried out in this research, the study of blockchain and decentralized functionality in industrial control systems is not new. Of the nineteen works covered in this review, ten of them fall in the blockchain or decentralized ledger classification. While the approach fell in two categories; that of centralized and decentralized, the consistent thread among all works lay in the novel application of some blockchain-type application in some industrial system, generally for the purpose of either distributed storage or for secure logging. 

Further, the idea of using fingerprinting as a means to both identify devices and anomalies is also not a novel idea. While only six of the works cited in this study analyze fingerprinting, the state of the art well-known and well-explored. The most common use of fingerprinting in industrial control systems lies in the use of either power consumption, physics-based, timing-based, or memory-based analysis as a means to observe anomalous PLC or ICS behaviors. Other uses of fingerprinting lay in it's ability to uniquely identify any device.

Where this review found lacking information lay more in the observations of existing decentralized ICS research. Only three works fell in the Decentralized System Design classification. Of these three, each pushed at the problem from a different angle. Garracho et al. [5] simply tried to understand existing weaknesses and Kannelonning et al. [18] canvassed the Norwegian industry landscape for security controls. Hosen et al. [19] presented a novel combination of a number of decentralized ICS protocols to create a holistic design for a possible ICS network.

### 2.4 Literature Review Diagram

![Lit Review](https://github.com/adamspanier/Distributed-Systems-Security/blob/main/Images/LitReview-Diagram.png)

### Citations

1. [M. K. Choi, C. Y. Yeun and P. H. Seong, "A Novel Monitoring System for the Data Integrity of Reactor Protection System Using Blockchain Technology," in IEEE Access, vol. 8, pp. 118732-118740, 2020, doi: 10.1109/ACCESS.2020.3005134.](https://ieeexplore.ieee.org/document/9126779)
2. [S. Otte, L. Reuscher, D. Keller and J. Fleischer, "Blockchain architecture for process-level traceability of continuous mixing process in battery cell production," 2024 1st International Conference on Production Technologies and Systems for E-Mobility (EPTS), Bamberg, Germany, 2024, pp. 1-14, doi: 10.1109/EPTS61482.2024.10586718.](https://ieeexplore.ieee.org/document/10586718)
3. [R. Colelli, C. Foglietta, R. Fusacchia, S. Panzieri and F. Pascucci, "Blockchain application in simulated environment for Cyber-Physical Systems Security," 2021 IEEE 19th International Conference on Industrial Informatics (INDIN), Palma de Mallorca, Spain, 2021, pp. 1-7, doi: 10.1109/INDIN45523.2021.9557446.](https://ieeexplore.ieee.org/document/9557446)
4. [A. Parvizimosaed, H. Azad, D. Amyot and J. Mylopoulos, "Protection against Ransomware in Industrial Control Systems through Decentralization using Blockchain," 2023 20th Annual International Conference on Privacy, Security and Trust (PST), Copenhagen, Denmark, 2023, pp. 1-5, doi: 10.1109/PST58708.2023.10320188.](https://ieeexplore.ieee.org/document/10320188)
5. [C. T. B. Garrocho, K. N. Oliveira, A. L. d. Santos, C. F. M. da Cunha Cavalcanti and R. A. R. Oliveira, "Toward a Failures Model for Communication of Decentralized Applications with Blockchain Networks Applied in the Industrial Environment," in IEEE Wireless Communications, vol. 29, no. 3, pp. 40-46, June 2022, doi: 10.1109/MWC.001.2100572.](https://ieeexplore.ieee.org/document/9857810)
6. [C. T. B. Garrocho, K. N. Oliveira, D. J. Sena, C. F. M. da Cunha Cavalcanti and R. A. R. Oliveira, "BACE: Blockchain-based Access Control at the Edge for Industrial Control Devices of Industry 4.0," 2021 XI Brazilian Symposium on Computing Systems Engineering (SBESC), Florianopolis, Brazil, 2021, pp. 1-8, doi: 10.1109/SBESC53686.2021.9628291.](https://ieeexplore.ieee.org/document/9628291)
7. [Z. Jadidi, A. Dorri, R. Jurdak and C. Fidge, "Securing Manufacturing Using Blockchain," 2020 IEEE 19th International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom), Guangzhou, China, 2020, pp. 1920-1925, doi: 10.1109/TrustCom50675.2020.00262.](https://ieeexplore.ieee.org/document/9343190)
8. [M. M. Cook, A. K. Marnerides and D. Pezaros, "PLCPrint: Fingerprinting Memory Attacks in Programmable Logic Controllers," in IEEE Transactions on Information Forensics and Security, vol. 18, pp. 3376-3387, 2023, doi: 10.1109/TIFS.2023.3277688.](https://ieeexplore.ieee.org/document/10130481)
9. [Q. Gu, D. Formby, S. Ji, H. Cam and R. Beyah, "Fingerprinting for Cyber-Physical System Security: Device Physics Matters Too," in IEEE Security & Privacy, vol. 16, no. 5, pp. 49-59, September/October 2018, doi: 10.1109/MSP.2018.3761722.](https://ieeexplore.ieee.org/document/8490185)
11. [T. Roy and A. A. L. Beex, "Power Measurement Based Code Classification for Programmable Logic Circuits," 2018 IEEE International Symposium on Signal Processing and Information Technology (ISSPIT), Louisville, KY, USA, 2018, pp. 644-648, doi: 10.1109/ISSPIT.2018.8642680.](https://ieeexplore.ieee.org/document/8642680)
12. [A. Keliris and M. Maniatakos, "Remote field device fingerprinting using device-specific modbus information," 2016 IEEE 59th International Midwest Symposium on Circuits and Systems (MWSCAS), Abu Dhabi, United Arab Emirates, 2016, pp. 1-4, doi: 10.1109/MWSCAS.2016.7870006.](https://ieeexplore.ieee.org/document/7870006)
13. [Stephen S. Kirkman, Steven Fulton, Jeffrey Hemmes, Christopher Garcia, and Justin C. Wilson. 2024. A Blockchain Architecture to Increase the Resilience of Industrial Control Systems from the Effects of a Ransomware Attack: A Proposal and Initial Results. ACM Trans. Cyber-Phys. Syst. 8, 1, Article 9 (January 2024), 13 pages. https://doi.org/10.1145/3637553](https://dl.acm.org/doi/10.1145/3637553)
14. [William Davis, Mahnoor Yaqoob, Luke Bennett, Stefan Mihai, Dang Viet Hung, Ramona Trestian, Mehmet Karamanoglu, Balbir Barn, and Huan Nguyen. 2023. An Innovative Blockchain-Based Traceability Framework for Industry 4.0 Cyber-Physical Factory. In Proceedings of the 2023 5th Asia Pacific Information Technology Conference (APIT '23). Association for Computing Machinery, New York, NY, USA, 118–122. https://doi.org/10.1145/3588155.3588174](https://dl.acm.org/doi/10.1145/3588155.3588174)
15. [Stefan Schorradt, Edita Bajramovic, and Felix Freiling. 2019. On the Feasibility of Secure Logging for Industrial Control Systems Using Blockchain. In Proceedings of the Third Central European Cybersecurity Conference (CECC 2019). Association for Computing Machinery, New York, NY, USA, Article 4, 1–6. https://doi.org/10.1145/3360664.3360668](https://dl.acm.org/doi/10.1145/3360664.3360668)
16. [Vijay Kumar and Kolin Paul. 2023. Device Fingerprinting for Cyber-Physical Systems: A Survey. ACM Comput. Surv. 55, 14s, Article 302 (December 2023), 41 pages. https://doi.org/10.1145/3584944](https://dl.acm.org/doi/10.1145/3584944)
17. [John Hayes, Adel Aneiba, and Mohamed Gaber. 2023. SymbIoT: Towards An Extensible Blockchain Integration Testbed for IIoT. In Proceedings of the 1st Workshop on Enhanced Network Techniques and Technologies for the Industrial IoT to Cloud Continuum (IIoT-NETs '23). Association for Computing Machinery, New York, NY, USA, 8–14. https://doi.org/10.1145/3609389.3610565](https://dl.acm.org/doi/10.1145/3609389.3610565)
18. [Zexin Lu. 2025. A Robust Anomaly Detection Approach for IIoT Time Series. In Proceedings of the 2024 2nd International Conference on Frontiers of Intelligent Manufacturing and Automation (CFIMA '24). Association for Computing Machinery, New York, NY, USA, 168–173. https://doi.org/10.1145/3704558.3707091](https://dl.acm.org/doi/10.1145/3704558.3707091)
19. [Kristian Kannelønning and Sokratis Katsikas. 2024. Deployment of Cybersecurity Controls in the Norwegian Industry 4.0. In Proceedings of the 19th International Conference on Availability, Reliability and Security (ARES '24). Association for Computing Machinery, New York, NY, USA, Article 188, 1–8. https://doi.org/10.1145/3664476.3670896](https://dl.acm.org/doi/10.1145/3664476.3670896)
20. [A. S. M. Sanwar Hosen, Pradip Kumar Sharma, Deepak Puthal, In-Ho Ra, and Gi Hwan Cho. 2023. SECBlock-IIoT: A Secure Blockchain-enabled Edge Computing Framework for Industrial Internet of Things. In Proceedings of the Third International Symposium on Advanced Security on Software and Systems (ASSS '23). Association for Computing Machinery, New York, NY, USA, Article 1, 1–14. https://doi.org/10.1145/3591365.3592945](https://dl.acm.org/doi/10.1145/3591365.3592945)

## 3.0 Project Technical Plan

The Project Technical Plan will provide the step-by-step process this investigation will take. The purpose of this research is to investigate existing ICS networks, understand traditional ICS network design and implementation, discover Decentralized Cryptographic Security (DCS) methods that can protect ICS asset, deploy an ICS wherein combinations of DCS methods can be observed for effect on network operations, and discuss the findings of the DCS-oriented system design.

### 3.1 Technical Plan Approach

To produce structured, repeatable, and actionable results, the project will be conducted in the manner as outlined below.

 - **Phase 1:** Data Collection
 - **Phase 2:** ICS System Synthesis
 - **Phase 3:** DCS Method Exploration
 - **Phase 4:** DCS-Enabled ICS System Design
 - **Phase 5:** DCS-Enabled ICS System Emulation
 - **Phase 6:** Analysis/Reporting

**3.1.1 Phase 1: Data Collection**

The initial phase of this research involves the collection of pertinent data relating to industry-standard ICS network design and implementation. In this phase, data concerning industry-standard ICS network design and deployment is collected and analyzed. From this data, the following information will be collected:

* **Hardware Assets** - The devices, wires, support structures, and physical infrastructure used in ICS
* **Hardware Constraints** - Limitations on hardware assets in the system such as size, temperature, humidity, and elevation
* **Software Assets** - The applications, services, and packages used in the ICS
* **Software Constraints** - The limitations on the software assets like communications requirements, licensing, and capabilities
* **Data Assets** - The data used to inform the ICS including databases, logging, and file system support
* **Data Constraints** - The limitations imposed on the data in the system
* **Communication Assets** - The protocols, services, and connections in the ICS
* **Human and Organizational Assets** - The personnel, regulations, and planning structures serving the ICS

The data collected in this phase of research is gathered from research papers, textbooks, training manuals, white papers, NIST documentation, and regulations.

**3.1.2 Phase 2: ICS System Synthesis**

From the documents collected in Phase 1, industry-standard asset and constraint lists, operational directions, ICS design diagrams, and ICS security discussions are produced. These findings are then analyzed and presented as a discussion on not only current ICS network design, but also on current ICS security controls. 

The purpose of this portion of the project is to adequately understand the current state of the discipline as relates to ICS networks. Without adequate comprehension of how ICS systems are currently designed, deployed, and secured, the test systems developed in this work will not be valid for industry professionals.

**3.1.3 DCS Method Exploration**

After collection and synthesis of industry standard ICS designs, an exploration of existing DCS methods provides a list of possible DCS security controls that can be integrated into ICS designs. DCS methods will be correlated to threat/asset pairs as a means to mitigate the realization of threats to assets. When at least one DCS security control is associated with every asset/threat pair, the ICS design can progress.

**3.1.4 DCS-Enabled ICS System Design**

From the data gathered in phases 1 through 3, DCS security controls is applied to a standard ICS network. The ICS network is based upon a well-known ICS network types, such as the power grid or a nuclear power plant. For this system, there will be three ICS network diagrams. The first will be an ICS network with no security controls. This network will be used as a control and as a means to base line network operations. The second network will be an ICS with standard ICS security protocols enforced. This includes controls like encryption. The third diagram will be the same ICS as both diagram 1 and 2, but with DCS methods applied in various combinations. From this DCS security control diagram, DCS-Enabled ICS Networks can be derived based on a series of DCS security control combinations.

**3.1.5 DCS-enabled ICS System Emulation**

From these designs, system emulations will be deployed and tested. A control deployment consisting of the ICS network with no added security will be deployed and, under heavy traffic and light traffic, the response times of the system will be evaluated. Further, the accuracy of the packets arriving at the distributed devices will be checked using integrity validations as a means to verify that the traffic in the system is not deteriorated. These initial evaluations will be used as a base line for testing the security controls in the security enabled ICS networks.

Next, an ICS with standard encryption and security protocols will be emulated. The same heavy/light traffic test will be carried out and the response times evaluated. Packet integrity will be checked at the distributed devices to verify that data in the system is not deteriorated. The data from this test will be collected and used for analysis and reporting.

Finally, a series of ICS designs will be emulated using a combination of different DCS security controls. Each of theses systems will be subjected to the same heavy/light traffic test and data integrity verifications.

<!--
What data will we collect? How will we test the system? How will be baseline the system? What kind of system will be use? How can be measure the impact of a DCS control? We should consider not only fast, but also quality of the system. Is it okay to take a hit on performance in exchange for enhanced secuirty? How much of a hit can we take? How can we decide what kind of a hit is possible?
-->
**3.1.6 Analysis and Reporting**

After testing the emulated system(s), an analysis on the raw findings will be reported and a discussion on the findings will be carried out. In the analysis, the baseline of the control system will be explained. From this explanation, the ICS with standard security will be compared. The DCS-Enabled systems will then be comaproed for performance. Finally, a summary of the findings will be discussed.

<!--
#### 3.1.1 Data Collection

The data collection phase consists of research and resource selections. Research will be conducted against PLCs operating in a DCS, industry-standard system design involving PLCs and other aspects of a DCS, and initial efforts of integrating crpytographic structures into DCS (both successful and unsuccessful implementations). In lieu of a physical lab, a DCS written in Python will be chosen as the testbed for the DCS. The network topology for the DCS, including PLCs within the DCS, will also be determined in this phase. To make the simulated Python environment identical to a live DCS, typical DCS anomalies such as message delays and their operational impacts on the greater system will be identified and modeled in Python.

#### 3.1.2 System Emulation

An industry-standard DCS will be modeled and written in Python. Proper operation of the Python project, including imitating PLC operation and data reporting will be evaluated to ensure proper system functionality. When the system passes verification checks, this system will be used as the baseline/recovery point for the project.

#### 3.1.3 Novel System Emulation

Using the system designed in step 3.1.2, novel cryptographic structures will be strategically inserted into the DCS. The tests conducted in step 3.1.2 will be conducted again against the system, and its responses will be recorded. It should be noted that the novel system emulation, complete with cryptographic functions, will only be tested at a proof-of-concept level. While attempts will be made to accurately model a DCS environment in Python and incorporate the novel cryptographic structures, full operational potential will not be realized until the novel system is fully vetted on a development DCS network with industry-standard PLCs, controllers, HMIs, etc. As such, this final step is out of scope for the current project.


#### 3.1.4 Data Collection/Analysis and Reporting

The results from the above test will be analyzed and compiled into a detailed report. This report will include specifics such as system design, normal operation, operation anomalies observed once cryptographic structures were implemented, any adjustments made to respond to the anomalies, and final results and summaries from the evaluation.

-->
