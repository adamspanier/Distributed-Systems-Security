# Requirements

[HOME](https://github.com/adamspanier/Distributed-Systems-Security)

<hr>

Industrial Control Systems (ICS), due to their critical nature in critical infrastructure, exhibit very strict requirements. ICS networks, comprised of Operational Technology (OT), have several design considerations based on functionality that must be met. Based on [NIST SP 800-82r3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf), the following seven (7) considerations must be taken into account when designing OT-based ICS:

1. **Safety:** ICS networks must be able to detect unsafe conditions and reduce unsafe conditions to safe ones.
2. **Control Timing Requirements:** ICS networks have time-related requirements such that the system can synchronize to meet its function.
3. **Geographic Distribution:** ICS networks can be very localized or widely distributed.
4. **Hierarchy:** ICS networks generally use a centralized supervisory control system to manage the system.
5. **Control Complexity:** The complexity of the system must be managed such that the control actions meet the objectives of the system.
6. **Availability:** Redundancy may be needed to ensure the up-time requirements of the system.
7. **Impact of Failures:** ICS systems must be able to continue operation, even in a degraded state.

Based on the considerations above and the requirements stated in [NIST SP 800-82r3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf), ICS networks exhibit the following eleven (11) functional requirements:

1. **Timeliness and Performance Requirements:** ICS networks are time-critical and must meet real-time requirements of the system for synchronization and system performance
2. **Availability Requirements:** ICS networks are continuous and must meet strict up time requirements, often with a level of 99.999% up-time.
3. **Risk management Requirements:** ICS networks must use fault tolerance as a means to prevent loss of life and endangerment to the public.
4. **Physical Process Requirements:** The physical events required by the system must be understood.
5. **System Operation Requirements:** The operational requirements between IT and OT-based ICS are not the same.
6. **Resource Constraints:** ICS systems use resource-constrained real-time operating systems that cannot include typical IT capabilities.
7. **Communications Requirements:** Communications in ICS networks are very different from IT systems and are sometimes proprietary.
8. **Change Management Requirements:**  How the system changes must be carefully planned and monitored.
9. **Managed Support Requirements:** The entities that are supporting the hardware and software environment used in the ICS must be tracked and documented.
10. **Component Lifetime Requirements:** Hardware lifetimes must be strictly tracked, and hardware should be replaced when EoL is reached.
11. **Component Location Requirements:** The possible remote locations of components must be considered when designing the system.

Beyond the functional and non-functional requirements of an OT-based ICS network, several special considerations must be taken regarding the security of the system. Based on [NIST SP 800-82r3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf), the following eleven (11) considerations must be taken into account to secure an ICS.

Security controls must not:
1. Impair the real-time nature of an ICS network
2. Effect the up-time and availability of the system
3. Cause unsafe states or risk to loss of life and public property
4. Cause the physical processes in the system to fail
5. Restrict the operational functionality of the system
6. Overburdened resource-constrained hardware devices
7. Limit or impair communications between devices in ICS networks
8. Impair change management tracking and functions in the system
9. Prohibit managed support functions in the system
10. Prolong or shorten the lifetime of components in the system
11. Impair hardware device operations in remote locations

### Functional

Based on the functional requirements stated above, the system proposed here must:

1. Synchronize hardware and software assets according to the specific time-critical functions of the system
2. Limit latency, delay, and jitter in communication circuits to accepted tolerances
3. Detect unsafe states and transfer from unsafe to safe with as little human intervention as possible
4. Facilitate bi-directional communication between connected devices
5. Carry out the physical movements needed to both maintain a safe state and carry out system objectives
6. Operate within the constraints of the PLCs and other network devices in the system
7. Exhibit the simplest control complexity possible to meet system operation objectives
8. Coordinate widely distributed hardware devices

### Non-Functional

In service of the functions above, the system must also meet the following non-functional requirements:

1. Log all access requests
2. Log all successful access
3. Log all data transfers
4. Log all program updates
