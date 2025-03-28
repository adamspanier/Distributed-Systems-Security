# Capturing Packets Transmitted Between Docker Images in the DCS Environment

## Prerequisites
* Wireshark and tcpdump installed on the environment host
* Wireshark installed on a local machine for file analysis

### Packet Capture Overview
Since all of the network traffic between PLCs, the MQTT broker, and the SCADA image are transmitted locally, a packet capture must be conducted on the 
images themselves to determine the messages being sent. Do not conduct a packet capture on the host, as the only data obtained will be communications between the user and the host.

Once the packet capture is complete, the results can be exported to a local computer for analysis. This is why it is important to have access to a computer with Wireshark installed.

**Packet Capture Steps**
* Ensure all necessary programs are installed (Wireshark and tcpdump).
* Identify Docker Networks
* Utilize tcpdump to create a .pcap of live network traffic
* Export the .pcap for analysis

### Install Necessary Programs

### Identify Docker Networks

### Utilize tcpdump to generate a .pcap

### Export .pcap for analysis
