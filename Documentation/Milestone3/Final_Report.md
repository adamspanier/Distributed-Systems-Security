# Distributed Security Controls in Industrial Control Systems

[HOME](https://github.com/adamspanier/Distributed-Systems-Security)

## Executive Summary - Distributed Security Controls in Industrial Control Systems

### ***** NEWS ALERT START *****

**29 JUL 2027: 0300** 

A wave of darkness covers the United States as power sub-station after power sub-station fails. The cascading blackout ripples slowly cross the country, shutting down water, coolant, and industrial production systems in its wake. City after city, home after home, fall eerily quiet as air conditioners, refrigerators, freezers, fans, and electrical devices fall into silence. The people are scared, but with fully charged phone batteries and backup generators, the population remains calm.

**27 AUG 2027: 1200** 

Panic grips the population. The phones have been dead for weeks now. Natural gas production is dead. All but a handful of generators have stopped producing electricity. The black start has begun, and portions of the grid are back up, but only for short durations due to heavy electrical loads. Water is running short, and the flow of gasoline is drying up. The lingering possibility that this may last for months more threatens the tenuous peace that keeps the population from taking matters into their own hands.

### ***** NEWS ALERT END *****


### The Problem

While the scenario above reads like a chapter from a science-fiction film, the critical systems holding modern society together are only one cyber attack away from complete collapse. These critical systems, often controlled by distributed Industrial Control Systems (ICS), generally use small, computationally limited devices to carry out day-to-day operations. The distributed nature of these ICS networks can make securing these networks very difficult. The limited computing power and real-time nature of these systems renders commonly used cyber security tools useless. The functions of these distributed industrial systems simultaneously make them the _most important_ and the _least secure_ systems in the world. Given one effective cyber attack, the power grid could be down for weeks, if not months, leaving society to crumble in its wake.

When designing an ICS system, security and functionality are _always_ competing requirements. When the computing power of a device is limited, any applied security measure threatens to reduce system functionality. While traditional methods of securing networks aren't useful in ICS networks, there are many new decentralized cryptographic security (DCS) measures that could be used to secure critical systems. Concepts like blockchains, hashes, digital signatures, and device fingerprinting present new and fresh possibilities for securing distributed critical systems. While these types of security measures are not entirely new to industrial control systems, there are a limited number of words considering the application of such security mechanisms from a system-design perspective.

### The Questions

**RQ1: How can Distributed Industrial Control Systems be designed for security using distributed cryptographic security controls?**

**RQ2: What effect, if any, do these combined mechanisms have on the security stance of ICS systems?**

### The Solution: Goals and Objectives

This Decentralized Cryptographic Security Design investigation aims to:

1. Provide holistic, system-level DCS design guidance for ICS network engineers
2. Observe how different applications and combinations of DCS measures affect ICS networks
3. Understand the benefits and drawbacks of applying system-level DCS design to ICS networks

### Project Methodology

To carry out this research, an initial survey of decentralized security measures in industrial control systems is carried out. Using the information discovered, a set of asset/threat pairs is derived based on common distributed industrial control system designs. Next, a decentralized security solution is matched to each asset/threat pair as a means to mitigate the risk posed to each asset. With each threat assigned to a security measure, a system is designed using two possible decentralized security controls. This system is then emulated in code, compared to both control and comparison networks, and analyzed for effectiveness.

### The Benefits

By allowing industrial control system designers to focus on the holistic, system-level security requirements of distributed industrial control systems, the networks they design can take a more robust, consistent, and predictable security profile. By using the method described above, the blind spots, computational bottlenecks, network complexities, and hidden threats common to distributed control systems can be systematically analyzed such that appropriate distributed security controls can be applied without affecting the functions of the system as a whole. By providing a more comprehensive security approach for industrial control system  designers, the critical systems that society relies upon for peace and order can be protected to the level that the people who need them expect.

## Results / Findings
(brief overview of outcomes - what did you achieve?, list milestone 1/2/3 outcomes, make an effort to logically collect and organize the findings)

(bulleted lists can also be helpful to structure your results discussion)
* outcome 1
* outcome 2

## Install Instructions (if applicable)
### Requirements
(list of any software / hardware requirements necessary to run the code/app/etc)

### Installation Instructions
(list of steps to install the product/app/code/etc)

### Getting started
(list of any steps to run the code after installation and/or manage the apps over their lifecycle)
