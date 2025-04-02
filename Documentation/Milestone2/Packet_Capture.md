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
To capture packets within the Docker environment, ensure that Wireshark and tcpdump are installed on the host instance. 

Wireshark install:
```bash
  sudo apt install wireshark
```
tcpdump install:
```bash
  sudo apt install tcpdump
```

### Identify Docker Networks
Before capturing packets on the Docker-simulated network, be sure to examine the available networks to determine which one you want to use when generating a .pcap file. 
```bash
docker network ls
```
The result should look similar to this:

![image](https://github.com/user-attachments/assets/b00aea6d-f702-4786-9875-ecb53c15c090)


### Utilize tcpdump to generate a .pcap
Now that the different networks on the Docker environment are known, the next step is to generate a packet capture (.pcap) file for analysis. This will only be successful if the different network elements (Docker images) are actively talking to each other; otherwise, no traffic will be captured. The general syntax of the tcpdump command to capture network traffic is:
```bash
sudo tcpdump -i <Docker network name> -w </path/to/folder/file_name>.pcap
```
The -i option indicates which interface will be monitored for network traffic. The -w option allows the user to specify the path that they want the .pcap file written to and the name of the .pcap.

In the Docker environment, the executed command will look similar to this:
![image](https://github.com/user-attachments/assets/628d1d1a-b704-4148-ae1f-5cbd4138fdc7)
Note that the system was not running, so no packets were captured in this screenshot. Also, CTRL+C is the command to end the packet capture.

### Export .pcap for analysis
