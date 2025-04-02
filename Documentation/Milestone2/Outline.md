# Research Paper Outline

[HOME](https://github.com/adamspanier/Distributed-Systems-Security)

<hr>

## Abstract
* Summation of the work

## I. Introduction

* Problem
   * Distributed industrial control systems play a significant role in the critical systems that maintain the world today.
   * Protecting these systems is _essential_ in maintaining stability, health, and prosperity in human society.
   * Current critical systems, while more secure than they once were, can still be made safer.
   * Traditional security measures have been thoroughly explored, but alternate approaches could exist
     
* Value
   * Due to the importance ICS networks have in critical systems, the security of an ICS directly serves the safety and security of the people that use the critical system.
   * Any improvement in these systems will help make a more peaceful, stable and prosperous society.
     
* While securing ICS networks in needed and beneficial, it is also difficult for the following reasons:
   * ICS networks use devices with limited computational power
   * ICS networks run in real-time environments
   * Malfunctioning ICS networks can cause physical and financial damages, and in some cases can lead to human casualties
   * Maintaining the functionality of an ICS network is _essential_
   * Any security mechanism deployed _must not_ negatively impact the real-time constraints on the system
     
* How others have attempted to improve ICS network security
   * Traditional approaches include the use of encryption, tunneling, limited authentication mechanisms, and physical security controls
   * Research has also been done on the use of blockchains, fingerprinting, and other decentralized security controls in ICS networks
      * These attempts are less researched
      * Most attempts are focused only on the security control, not a cohesive system design

*  In this research, we explore the following questions to address the challenges above
   * RQ1: How can Distributed Industrial Control Systems be designed for security from a system design standpoint using distributed cryptographic security controls?
   * RQ2: How can these distributed security controls be applied and combined in ICS networks as a means to increase security?

## II. Background
* ICS System Fundamentals
   * Industrial Control Systems are cyber-physical systems that use programs to control physical actuators.
   * These systems are combined in such a way as to serve a concrete, real-world function
   * Examples or ICS systems are: power substations, nuclear power plants, hydroelectric dams, manufacturing plants, oil refineries, etc.
   * Programmable Logic Controllers carry out many of the cyber-physical operations in ICS networks

* Distributed ICS   
   * Many ICS networks operate in distributed networks
   * These networks operate in geographically separate environments
   * To control disparate geographic locations, Supervisory Control and Data Acquisition (SCADA) system controllers are used
   * SCADA systems use Remote Terminal Units (RTUs) to communicate with the devices in the distributed network

* Hard Real-Time
   * Most SCADA systems operate in hard real-time environments
   * Hard-real-time indicates that tasks that are assigned must be carried out in some acceptable time-frame
   * If the task does not occur in the correct timing, the system can cease to be functional or even cause physical damage
   * Hard-real-time constraints are enforced by the environments, not the engineers; thus they cannot be changed or ignored

* Operational Technologies
   * Operational Technologies (OT) comprise any system in which operational constraints (aka real-time constraints) outweigh the information constraints
   * Most ICS networks are OT networks  

* Decentralized Security Controls
   * Blockchains, digital signatures, Code Signing, and Fingerprinting are common decentralized security primitives

   * Blockchains
      * A blockchain is a linked list that used a hash address to point to the next node in the list
      * A hash is a one way function that creates a fixed bit output for a variable bit input.
      * A cryptographically secure hash is a hash that implements collision resistance
      * Collision resistance indicates that the bit length of the resulting digest is so vast collisions cannot be intentionally discovered

   * Digital Signatures
      * Digital Signatures are unique values that are associated with a single document and a single key

      * Signing
         * A signature is achieved by first hashing a document using a cryptographically secure hashing algorithm
         * The resulting hash is encrypted with private key of a user
         * The resulting value is affixed to the document

      * Validating a signature
         * A signature is validated by decrypting the signature using the public key of the user
         * The resulting hash is then compared to the hash of the received document
         * If the two values match, the signature is validated

   * Code Signing
      * Uses the same concept as digital signatures, but with code
      * Code that is signed can be verified via the public key of some organization

   * Digital Fingerprinting
      * A process by which the digital data or physical constraints of a device are patterned to generate a unique id

## III. Related Work
* Related Works
   * The related works fall into three categories
      * Data Integrity Protection
      * Device Fingerprinting
      * Decentralized System Design
        
   * Data Integrity breaks into two categories
      * Centralized Protection
      * Decentralized Protection
        
   * Device Fingerprinting breaks into two categories
      * Anomalous Behavior Detection
      * General Fingerprinting
        
   * Decentralized System Desing breaks into two categories
      * Decentralized System Weaknesses
      * Decentralized System Design
        
   * Discussion
      * The use of decentralized security controls is not new to ICS networks
      * Most exploration has been done via the application of blockchains to ICS networks
      * These blockchains are often applied as a means to create immutable logging processes
      * Fingerprinting is also used, generally to detect anomalous behavior
      * The least explored area in this review lies in the Decentralized System Design category  

## IV. System Design

### System Design Methodology
* How did we choose to design the system?
* Why did we choose to design the system in this way?
* Are there alternatives?
* What is our design plan?
    * Control ICS System for Baselines
    * Standard Protection ICS System
    * Decentralized Security Control Combinations

### System Purpose
* System Purpose? - What does this system do?
* System Components
* System Security Controls
* Functional Explanation of the system
    
### System Architecture
* System Diagrams
* How does this design fit the methodology, and does it solve the problem?

### System Requirements
* Assets in ICS Systems
* Threat/Asset Groupings
* Decentralized Security Controls and Threat Groups
* System Functional Requirements
* System Non-Functional Requirements
  
## V. System Emulation
* System Emulation Software Explanation
    * Why did we choose this approach?
* System Emulation Implementation Methodology
* How does the emulation system work?
* System Architecture
* System demonstration

## VI. Testing
* What tests will be used?
* How did we come up with these tests?
* How were the tests deployed?
* What are the raw results?
  
## VII. Discussion
* How did we attempt to answer the research questions?
* Did we answer them?
* If so, what is the answer?
  
## VIII. Conclusion
* Overview of the findings of the paper
