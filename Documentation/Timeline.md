# 1.0 Project Timeline
[HOME](https://github.com/adamspanier/Distributed-Systems-Security)

To follow scientific guidelines and conduct a research experiment with actionable results, the following steps must be completed in the order listed. The estimated time spent on each step is included in the step heading.

## 1.1 Determine Python Environment/Emulation Setup (1 Week)

The group will determine if an existing Python repository will satisfy the requirements for our emulation environment, or if the group needs to code an environment themselves. Existing environments include:
- [SCADASim](https://github.com/cmu-sei/SCADASim)
- [Cpppo](https://github.com/pjkundert/cpppo) and [Cpppo-ENIP-API](https://hardconsulting.com/products/6-cpppo-enip-api)

Regardless of the direction for the emulation environment, the team must ensure that environment variables are the same across all machines. Any versions of Python/repository dependencies must be the same on everyone's computer to produce uniform, repeatable results.

## 1.2 Deploy Simulation Environment (2 Weeks)

Every team member should have the simulation environment deployed on a computer they have access to. During this phase, tests to determine a standard environment should be implemented and compared across the teams' distributions to verify uniformity in individual deployments. 

## 1.3 Design Novel DCS (3 Weeks)

With everyone's environments running and baselines established, the team will create a novel system design using cryptographic functions to secure a DCS. This design will utilize baselines established in 1.2 and literary reviews detailing successes and failures of past cryptographic implementations to DCS instances.

## 1.4 Implement Novel DCS Design and Test Emulated DCS (4 Weeks)

The novel DCS using cryptographic functions will be modeled using Python. The successes and failures of these implementations will be noted. For failure scenarios, adjustments will be made in an attempt to rectify any failure scenarios.

## 1.5 Report Findings (3 Weeks)

The entire process of this project, from implementing the Python environment to deploying novel cryptographic functions, will be documented. At the conclusion of the testing phase, the observations and results will be compiled into a report. Successful implementations, failure scenarios, and areas for further expansion of testing efforts will be discussed in the report.
