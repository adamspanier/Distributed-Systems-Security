# Assets and Threats

### Distributed Control System Assets

  #### Hardware Assets
    1. Programmable Logic Controllers (PLCs)
    2. Remote Terminal Units (RTUs)
    3. Intelligent Electronic Devices (IEDs)
    4. Human-Machine Interface (HMI) stations
    5. Engineering workstations
    6. Historian servers
    7. Control servers
    8. Field sensors and actuators
    9. Industrial switches and routers
    10. Redundant controllers
  
  #### Software Assets
    1. SCADA software
    2. Distributed Control System (DCS) software
    3. PLC programming environments
    4. Firmware for control devices
    5. HMI applications
    6. Historian software
    7. Alarm management systems
    8. Device drivers
  
  #### Data Assets
    1. Process variable data
    2. Control logic programs
    3. Set points and thresholds
    4. Alarm configurations
    5. Historical process data
    6. Control system backups
    7. Equipment parameters
    8. Device configuration files
    9. System topology information
    10. Control recipes and sequences
  
  #### Communication Assets
    1. Industrial protocols (Modbus, Profinet, EtherNet/IP)
    2. OPC UA/DA communications
    3. Fieldbus networks
    4. Serial communications (RS-232/485)
    5. Control network segments
    6. Time synchronization services
    7. Device discovery services
    8. Protocol gateways
    9. Industrial wireless networks
    10. Remote access connections

  #### Human and Organizational Assets
    1. Operators and engineers
    2. Maintenance personnel
    3. Security personnel
    4. Safety policies and procedures
    5. Compliance and regulatory frameworks
    6. Operational Logs and Auditing
    7. Vendor and Supply Chain Management Policies
    8. Disaster Recovery & Business Continuity Plans

### Distributed Control Threats

#### Architecture and Design Threats

    1. Insufficient network segmentation
    2. Lack of defense-in-depth strategies
    3. Single points of failure in critical components
    4. Inadequate redundancy planning
    5. Improper security boundaries
    6. Legacy system integration vulnerabilities
    7. Insecure system architecture
    8. Unprotected communication paths
    9. Inappropriate trust relationships
    10. Inadequate disaster recovery design

#### Operational Threats

    1. Improper change management procedures
    2. Inadequate security monitoring
    3. Insufficient threat detection capabilities
    4. Delayed or absent security patching
    5. Configuration drift over time
    6. Ineffective incident response planning
    7. Human error during operations
    8. Inadequate staff training
    9. Improper system documentation
    10. Inconsistent backup procedures
    11. Lack of system integrity verification

#### Cyber Attack Threats

    1. Advanced Persistent Threats (APTs) targeting industrial systems
    2. Ransomware specifically designed for industrial environments
    3. Supply chain compromises
    4. Command and control exploitation
    5. Process manipulation attacks
    6. Cross-zone pivoting
    7. System reconnaissance and intelligence gathering
    8. Malware specifically targeting industrial protocols
    9. Cyber-physical attacks affecting physical processes
    10. Zero-day vulnerability exploitation
    11. Denial of service affecting critical processes

#### Physical and Environmental Threats

    1. Unauthorized physical access to control hardware
    2. Environmental control failures (cooling, power)
    3. Natural disasters affecting control centers
    4. Electromagnetic interference
    5. Power quality issues affecting control equipment
    6. Physical damage to communication infrastructure
    7. Tampering with field equipment
    8. Inadequate physical security for critical nodes
    9. TEMPEST/side-channel attacks
    10. Combined physical/cyber attacks

#### Data and Communication Threats

    1. Data integrity violations
    2. Protocol-specific vulnerabilities
    3. Man-in-the-middle attacks on industrial protocols
    4. Unencrypted communications exposure
    5. Data exfiltration of sensitive process information
    6. Time synchronization attacks
    7. Traffic analysis revealing operational patterns
    8. Communication channel saturation
    9. Data historian compromises
    10. Process value manipulation

#### Insider Threats

    1. Malicious insider actions
    2. Privileged user account abuse
    3. Social engineering targeting control system operators
    4. Compromised third-party vendors with system access
    5. Inadequate access control enforcement
    6. Shared credential abuse
    7. Remote access exploitation
    8. Credential theft
    9. Unauthorized system modifications by staff
    10. Sabotage by disgruntled employees

#### Governance and Compliance Threats

    1. Inadequate security policies for industrial systems
    2. Insufficient risk assessment processes
    3. Regulatory compliance failures
    4. Unclear security responsibilities
    5. Poor vendor management
    6. Inadequate security testing procedures
    7. Insufficient vulnerability management
    8. Weak security architecture reviews
    9. Inadequate third-party security assessment
    10. Poor documentation of security controls

#### Supply Chain Threats

    1. Compromised third-party software or hardware
    2. Dependency on single-source vendors
    3. Insider threats from contractors or suppliers
    4. Use of outdated or End-of-Life components
    5. Untrusted third-party logistics providers
    6. Lack of supply chain visibility
    7. Weak contract enforcement
    8. Failure to perform risk assessments
    

### Asset/Threat Pairs

#### Hardware Asset Threats


  1. Programmable Logic Controllers (PLCs) 
       * Firmware compromise/backdoors
       * Physical tampering
       * Malware infection
       * Unauthorized configuration changes
       * Power supply failures
       * Environmental damage (heat, moisture)
       * Hardware obsolescence/lack of vendor support

  2. Remote Terminal Units (RTUs) 
       * Signal interception/manipulation
       * Device spoofing
       * Physical security breaches
       * Battery/power failures
       * Communication interruptions
       * Environmental exposure damage
       * Unauthorized access

  3. Intelligent Electronic Devices (IEDs) 
       * Firmware exploitation
       * Relay configuration attacks
       * Man-in-the-middle attacks
       * Clock/timing manipulation
       * Hardware failure
       * Abnormal electrical conditions

  4. Human-Machine Interface (HMI) stations 
      * Malware infection
      * Credential theft
      * Unauthorized physical access
      * Screen manipulation/false readings
      * Operating system vulnerabilities
      * Social engineering attacks
      * Hardware failures
     
  5. Engineering workstations 
      * Privilege escalation
      * Malicious software installation
      * Unauthorized remote access
      * Data exfiltration
      * Supply chain compromise
      * Credential theft
      * Inadequate patch management
     
  6. Historian servers 
      * Database corruption
      * Data tampering/manipulation
      * Denial of service attacks
      * Storage failure
      * Backup compromise
      * Unauthorized access
      * Data exfiltration
     
  7. Control servers 
      * Operating system vulnerabilities
      * Malware infection
      * Unauthorized access
      * Resource exhaustion
      * Component failure
      * Improper configuration
      * Supply chain attacks
      
  8. Field sensors and actuators 
      * Calibration manipulation
      * Physical damage
      * Signal spoofing
      * Environmental interference
      * Power fluctuations
      * Communication interruptions
      * Counterfeiting/supply chain issues
      
  9. Industrial switches and routers 
      * Network traffic manipulation
      * Denial of service
      * ARP poisoning
      * MAC flooding
      * Firmware compromise
      * Hardware failure
      * Misconfiguration
      
  10. Redundant controllers 
      * Failed failover mechanisms
      * Synchronization attacks
      * Common mode failures
      * Inconsistent configurations
      * Undetected primary controller compromise
      * Simultaneous hardware failures


#### Software Asset Threats

  1. SCADA software 
      * Logic injection attacks
      * Zero-day vulnerabilities
      * API exploitation
      * Credential compromise
      * Session hijacking
      * Command injection
      * Unpatched vulnerabilities
    
  2. Distributed Control System (DCS) software 
      * Exploitable software bugs
      * Memory corruption
      * Configuration manipulation
      * Improper authentication
      * Resource exhaustion
      * Interface vulnerabilities
      * Logic flaws
    
  3. PLC programming environments 
      * Logic manipulation
      * Trojanized software updates
      * Improper access controls
      * Malicious logic insertion
      * Software vulnerabilities
      * Unauthorized program downloads
      * Version control issues
    
  4. Firmware for control devices 
      * Malicious firmware updates
      * Firmware downgrade attacks
      * Hidden backdoors
      * Update mechanism exploitation
      * Verification bypass
      * Signing key compromise
      * Undocumented functions
    
  5. HMI applications 
      * Interface manipulation
      * Client-side attacks
      * Input validation exploitation
      * Screen falsification
      * Unauthorized command execution
      * Cross-site scripting (if web-based)
      * Command injection
    
  6. Historian software 
      * SQL injection
      * Unauthorized data access
      * Improper query handling
      * Denial of service
      * Authentication bypass
      * Integrity verification issues
      * Data corruption
    
  7. Alarm management systems 
      * Alarm flooding attacks
      * False alarm injection
      * Alarm suppression
      * Priority manipulation
      * Notification bypass
      * Configuration tampering
      * Filter manipulation
    
  8. Device drivers 
      * Buffer overflows
      * Device communication hijacking
      * Driver tampering
      * Privilege escalation
      * Memory corruption
      * Unsigned driver installation
      * Legacy/unpatched drivers

#### Data Asset Threats

  1. Process variable data 
      * Data falsification
      * Integrity violation
      * Process value manipulation
      * Replay attacks
      * Man-in-the-middle interception
      * Malicious range modification
      * Timing attacks
     
  2. Control logic programs 
      * Logic alteration
      * Unauthorized changes
      * Malicious logic insertion
      * Logic bombing
      * Backup corruption
      * Version control compromise
      * Logic extraction/theft
     
  3. Set points and thresholds 
      * Threshold manipulation
      * Safety limit alteration
      * Parameter drift
      * Unauthorized changes
      * Calibration attacks
      * Control range tampering
      * Integrity violation
     
  4. Alarm configurations 
      * Alarm disabling
      * Threshold manipulation
      * Priority changes
      * False alarm configuration
      * Critical alarm suppression
      * Configuration corruption
      * Bypass settings
     
  5. Historical process data 
      * Data poisoning
      * Deletion/corruption
      * Unauthorized access
      * Data exfiltration
      * Falsified trending
      * Archive tampering
      * Storage manipulation
     
  6. Control system backups 
      * Backup corruption
      * Unauthorized modification
      * Backup theft
      * Inadequate storage security
      * Incomplete backups
      * Restoration failures
      * Malicious restoration
     
  7. Equipment parameters 
      * Parameter manipulation
      * Safety limit changes
      * Performance degradation
      * Misconfiguration
      * Unauthorized access
      * Parameter drift
      * Documentation inconsistencies
     
  8. Device configuration files 
      * Unauthorized configuration changes
      * Parameter manipulation
      * Configuration exfiltration
      * Default credential exposure
      * Insecure storage
      * Version control issues
      * Template manipulation
     
  9. System topology information 
      * Network mapping exfiltration
      * Architecture exposure
      * Unauthorized documentation access
      * Critical asset identification
      * Vulnerability mapping
      * Attack surface analysis
      * Security control identification
     
  10. Control recipes and sequences 
      * Sequence manipulation
      * Process sabotage
      * Recipe theft
      * Intellectual property exfiltration
      * Quality manipulation
      * Safety override insertion
      * Unauthorized modifications

#### Communication Asset Threats

  1. Industrial protocols (Modbus, Profinet, EtherNet/IP) 
       * Protocol fuzzing
       * Function code abuse
       * Lack of authentication exploitation
       * Command injection
       * Protocol-specific vulnerabilities
       * Man-in-the-middle attacks
       * Replay attacks
     
  2. OPC UA/DA communications
       * Certificate vulnerabilities
       * Authentication bypass
       * Session hijacking
       * Encryption weaknesses
       * Trust relationship exploitation
       * Denial of service
       * Implementation flaws
     
  3. Fieldbus networks
       * Traffic analysis
       * Signal tampering
       * Physical tapping
       * Electromagnetic interference
       * Protocol exploitation
       * Node impersonation
       * Termination issues
     
  4. Serial communications (RS-232/485)
       * Physical wiretapping
       * Signal interception
       * Communication flooding
       * Line noise injection
       * Timing attacks
       * Protocol vulnerabilities
       * Lack of encryption exploitation
     
  5. Control network segments
       * Network segmentation bypass
       * VLAN hopping
       * Traffic sniffing
       * ARP poisoning
       * Routing attacks
       * Trust relationship exploitation
       * Unauthorized device connection
     
  6. Time synchronization services 
       * Time manipulation
       * NTP attacks
       * Clock skew
       * Synchronization disruption
       * GPS signal spoofing
       * Time-based authentication bypass
       * Timing attack vectors
     
  7. Device discovery services 
       * Reconnaissance exploitation
       * Service enumeration
       * Device fingerprinting
       * Spoofing
       * Unauthorized device registration
       * Information leakage
       * Service disruption
     
  8. Protocol gateways 
       * Translation manipulation
       * Cross-protocol attacks
       * Gateway compromise
       * Configuration tampering
       * Protocol boundary violations
       * Buffer handling issues
       * Denial of service
     
  9. Industrial wireless networks 
       * Signal jamming
       * Rogue access points
       * Authentication bypass
       * Encryption cracking
       * Session hijacking
       * Interference
       * Man-in-the-middle attacks
     
  10. Remote access connections
       * VPN vulnerabilities
       * Credential theft
       * Unauthorized access
       * Connection hijacking
       * Session persistence
       * Improper access controls
       * Insecure channel exploitation






### Distrubuted Controls in DCSs

1. Ledger
2. Fingerprinting
3. etc

### Asset/Threat to Distributed Control Pairs

1. Logs:Ledger
