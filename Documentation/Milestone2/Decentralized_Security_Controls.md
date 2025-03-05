# Decentralized Controls for Novel DCS Designs

[HOME](https://github.com/adamspanier/Distributed-Systems-Security)

<hr>

### Controls

1. Zero Trust Architecture - Continuous verification and strict access controls
   1.	Why use it? 
         * Eliminate implicit trust in network
         * Prevent lateral movement of threats
         * Reduce potential attack surface
   2.	What does it apply to? 
         * User access
         * Device communications
         * Network segments
         * Application interactions
   3.	Pros 
         * Granular access control
         * Minimizes potential breach impact
         * Adapts to dynamic network environments
   4.	Cons 
         * Complex implementation
         * Higher computational overhead
         * Increased management complexity

       
2. Distributed Authentication - Peer-to-peer identity verification mechanisms
   1.	Why use it? 
         * Decentralize credential management
         * Remove single point of authentication failure
         * Increase system resilience
   2.	What does it apply to? 
         * User credentials
         * Device identities
         * Inter-system communications
         * Access request validations
   3.	Pros 
         * No centralized authentication server
         * Improved resistance to credential compromise
         * Real-time authentication updates
   4.	Cons 
         * Synchronization challenges
         * Performance latency
         * More complex key management
     
3. Network Redundancy - Multiple independent communication pathways
   1. Why use it?
         * Ensure continuous system operation
         * Prevent single link failures
         * Maintain communication during partial network disruption
   2. What does it apply to?
         * Communication protocols
         * Network routing
         * Backup communication channels
         * Inter-device connections
   3. Pros
         * High availability
         * Improved fault tolerance
         * Automatic failover capabilities
   4. Cons
         * Increased infrastructure complexity
         * Higher implementation costs
         * Additional maintenance overhead

4. Decentralized Monitoring - Distributed threat detection and logging
   1. Why use it?
        * Enable localized threat identification
        * Reduce centralized monitoring bottlenecks
        * Provide real-time threat response
   2. What does it apply to?
        * Anomaly detection
        * Event logging
        * Intrusion detection
        * Performance monitoring
   3. Pros
        * Faster threat identification
        * Reduced central processing load
        * Improved system resilience
   4. Cons
        * Complex correlation of distributed logs
        * Potential information inconsistency
        * Higher computational requirements
