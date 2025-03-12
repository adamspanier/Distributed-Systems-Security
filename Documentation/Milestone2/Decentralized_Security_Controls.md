# Decentralized Controls for ICS Network Applications

[HOME](https://github.com/adamspanier/Distributed-Systems-Security)

<hr>

### Traditional versus Decentralized Controls

The impact of existing security controls in ICS systems is well-known. Security controls like encryption, authentication, physical protections, and logging are are already in use in most ICS networks and the impacts these controls have on ICS networks has been thoroughly explored and understood. Due to the limited computational capacity in ICS network devices, many security controls that can be used in standard IT networks to bolster security postures beyond encryption and authentication are not available in ICS networks. 

This work explores the possibility of integrating decentralized security controls (DSCs) in ICS networks as a means to achieve a stronger security posture beyond the use of traditional security controls. These decentralized security controls are security mechanism that can be implemented through combinations of cryptographic primitives to create accurate, reliable, and consistent measurement, assessment, and analysis mechanisms for data and functional security control. 

In this work, a DCS is a security control that is not included in traditional security models. Traditional security controls, as referenced in the work, are security controls outlined in NIST SP 800-82r3 as follows:

**1. Organizational Controls**

   * _Data Flow Maps_ - Attaining a sufficient understanding of how data flows in the network
   * _Governance_ - Policies, Standards, Guidelines, and Baselines for the system
   * _Risk Assessment and Risk Management_ - Risks must be identified and a plan created to manage them
   * _Physical Access Controls_ - Doors, locks, fences, lights, bollards, locking cabinets, electronic surveillance systems, people tracking
   * _Awareness and Training_ - Educating employees to adhere to security policies
   * _Change Management_ - Ensure the system is deployed and maintained in a consistently secure state
   * _Response and Recovery Plans and Testing_ - Create and test response and recovery plans

**2. Network and Host Controls**

   * _Asset Management_ - Unique IDs for assets, Hardware and Software Inventories, Vendor Information, roles and responsibilities
   * _Identity Management and Access Control_ - SSO, authentication, identification, session lock, session termination
   * _Logical Access Controls_ - ACLs, Role-Based Access Control, Attribute-Based Access Control
   * _Network Segmentation_ - Use of VLANs and subnetting to separate assets
   * _Data Security_ - Encryption of data at rest and in transit
   * _Backups_ - Ensuring data is backed up in a sufficient number of mediums and locations
   * _Logging_ - Provide adequate logging for digital forensics
   * _Media Protection_ - Protect removable media
   * _Wireless Communications Security_ - If wireless is used, it must be adequately protected
   * _IDS and IPS_ - Detect and/or prevent intrusions to the network
   * _Security Continuous Monitoring_ - All logs and systems should be continuously monitored for security state and posture
   * _Malicious Code Detection_ - Each ICS must provide mechanisms to detect malicious code

### Decentralized Security Controls in ICS

While the DCS controls below are not included in the list above, NIST SP 800-82r3 does mention, "digital signatures, hashing, and other cryptographic functions are available to prevent unauthorized access or modification of data at rest and in transit." This statement acknowledges the possibility of using _other_ security mechanisms other than the ones explicitly defined in the publication. The previous statement does come with a caveat: NIST SP 800-82r3 mentions that _any_ use of cryptography can have negative effects on the timeliness of ICS networks and can cause key management issues to arise.

When analyzing the security control groups above, DCSs clearly fall into several categories; namely the Data Security, Logging, IDS and IPS, Identity Management, Malicious Code Detection, and Continuous Monitoring groups. DCS controls currently available for each group lists are as follows:

1. _Data Security_ - DCS controls like blockchains, distributed authentication, digital signatures and code signing provide robust integrity and confidentiality functions
2. _Logging_ - DCS controls like blockchains and digital signatures provide logging data integrity security, immutable logging data structures, and faster data analysis processes
3. _IDS and IPS_ - DCS controls like fingerprinting, network hashing, heuristic analysis, and pattern analysis provide useful IDS and IPS functions
4. _Identity Management_ - DCS controls like blockchains, fingerprinting, and digital signatures help validate identity management and authentication functions
5. _Malicious Code Detection_ - DCS controls like digital signatures provide protection against the introduction of malicious code into the system
6. _Continuous Monitoring_ - Any hash-based security ledger can provide fast and accurate network traffic and status monitoring.

### Decentralized Security Controls

1. Blockchain
      * **Definition:**
   
         A blockchain is a collaborative, tamper-resistant ledger that maintains transactional records. The transactional records (data) are grouped into blocks. A block is connected to the previous one by including a unique identifier that is based on the previous block’s data. As a result, if the data is changed in one block, it’s unique identifier changes, which can be seen in every subsequent block (providing tamper evidence). This domino effect allows all users within the blockchain to know if a previous block’s data has been tampered with. Since a blockchain network is difficult to alter or destroy, it provides a resilient method of collaborative record keeping. - [NIST](https://www.nist.gov/blockchain)
        
      * Why use it?
      * What does it apply to?
      * Pros
      * Cons

3. Digital Signature
      * **Definition:**

         As an electronic analogue of a written signature, a digital signature provides assurance that: 1) the claimed signatory signed the information, and 2) the information was not modified after signature generation. - [NIST CSRC](https://csrc.nist.gov/projects/digital-signatures)

      * Why use it?
      * What does it apply to?
      * Pros
      * Cons

5. Code Signing
      * **Definition:**

         Digitally signing code provides both data integrity to prove that the code was not modified, and source authentication to identify who was in control of the code at the time it was signed. When the recipient verifies the signature, he is assured that the code came from the source that signed it, and that it has not been modified in transit. - [NIST CSWP](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.01262018.pdf)

      * Why use it?
      * What does it apply to?
      * Pros
      * Cons

6. Device Fingerprinting
      * **Definition:**

         A fingerprint is a trace of the information left by someone. It is a well-known term in various bio- metric applications such as personal identification, access control, and security. When computers, networks, and security are discussed, it is referred to as a digital fingerprint, browser fingerprint, Device Fingerprint/Fingerprinting (DFP), or machine fingerprint - [Kumar et al.](https://dl.acm.org/doi/10.1145/3584944)

      * Why use it?
      * What does it apply to?
      * Pros
      * Cons

7. Network Traffic Hashing/Fingerprinting
      * **Definition:**

         A fingerprint is a trace of the information left by someone. It is a well-known term in various bio- metric applications such as personal identification, access control, and security. When computers, networks, and security are discussed, it is referred to as a digital fingerprint, browser fingerprint, Device Fingerprint/Fingerprinting (DFP), or machine fingerprint - [Kumar et al.](https://dl.acm.org/doi/10.1145/3584944)

      * Why use it?
      * What does it apply to?
      * Pros
      * Cons

9. Zero Trust Architecture
      * **Definition:**

         A zero trust architecture (ZTA) is an enterprise cybersecurity architecture that is based on zero trust principles and designed to prevent data breaches and limit internal lateral movement. This publication discusses ZTA, its logical components, possible deployment scenarios, and threats. It also presents a general road map for organizations wishing to migrate to a zero trust design approach and discusses relevant federal policies that may impact or influence a zero trust architecture. - [NIST SP 800-207](https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf)
   
   * Why use it? 
      * Eliminate implicit trust in network
      * Prevent lateral movement of threats
      * Reduce potential attack surface
   * What does it apply to? 
      * User access
      * Device communications
      * Network segments
      * Application interactions
   * Pros 
      * Granular access control
      * Minimizes potential breach impact
      * Adapts to dynamic network environments
   * Cons 
      * Complex implementation
      * Higher computational overhead
      * Increased management complexity

       
2. Distributed Authentication
   * **Definition:**

      The distribution of authentication operations accross a peer-to-peer network. This distribution eliminates the need for a single sign on point of entry, and removes a SPoF for most systems.        

   * Why use it? 
      * Decentralize credential management
      * Remove single point of authentication failure
      * Increase system resilience
   * What does it apply to? 
      * User credentials
      * Device identities
      * Inter-system communications
      * Access request validations
   * Pros 
      * No centralized authentication server
      * Improved resistance to credential compromise
      * Real-time authentication updates
   * Cons 
      * Synchronization challenges
      * Performance latency
      * More complex key management
     
4. Network Redundancy
      * **Definition:**

        Multiple paths or systems are provided so that if one fails, another can automatically take over, ensuring continued functionality and improving reliability and resilience. - [NIST SP 800-53](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
        
      * Why use it?
         * Ensure continuous system operation
         * Prevent single link failures
         * Maintain communication during partial network disruption
      * What does it apply to?
         * Communication protocols
         * Network routing
         * Backup communication channels
         * Inter-device connections
      * Pros
         * High availability
         * Improved fault tolerance
         * Automatic failover capabilities
      * Cons
         * Increased infrastructure complexity
         * Higher implementation costs
         * Additional maintenance overhead

6. Decentralized Monitoring
      * **Definition:**

        The distrubtion of montiroing activities accross a peer-to-peer network.
        
      * Why use it?
        * Enable localized threat identification
        * Reduce centralized monitoring bottlenecks
        * Provide real-time threat response
      * What does it apply to?
        * Anomaly detection
        * Event logging
        * Intrusion detection
        * Performance monitoring
      * Pros
        * Faster threat identification
        * Reduced central processing load
        * Improved system resilience
      * Cons
        * Complex correlation of distributed logs
        * Potential information inconsistency
        * Higher computational requirements
