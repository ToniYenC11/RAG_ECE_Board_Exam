## NETWORK DEVICES AND BASIC NETWORK SIMULATION

PECEC 3 - Communications 3: Data Communications (Lecture) Prepared by: Jepp Quijano, ECE, ECT

<!-- image -->

## Talking Points

- Different Basic Network Devices
- Basic Network Simulations

<!-- image -->

## Basic Network Devices

- Modem/Media Converter -A device used convert signals (ADC/DAC).
- to

<!-- image -->

<!-- image -->

## Basic Network Devices

- Ethernet Hub
- -Layer 1 and passive device.
- No security
- 1 big collision domain

Sample Photo/Network Symbol

Hub

<!-- image -->

<!-- image -->

## Collision Domain vs Broadcast Domain

- A collision domain is the part of a network where collisions of packets can occur while a broadcast domain is the part of a network where broadcast communication occurs.

<!-- image -->

<!-- image -->

## Basic Network Devices

- Bridge
- -Layer 2 and active device.
- Uses MAC addressing scheme to filter traffic
- -Traffic filtering is software-based.
- 1 broadcast domain
- -Every port is a collision domain.

<!-- image -->

<!-- image -->

## Basic Network Devices

- Switch
- -Layer 2 and active device.
- Uses MAC addressing scheme to filter traffic
- -Traffic filtering is based on hardware functions called ASICS.
- 1 broadcast domain
- -Every port is a collision domain.

## Sample Photo/Network Symbol

<!-- image -->

<!-- image -->

<!-- image -->

## Basic Network Devices

- Router
- -Layer 3 and active device.
- -Uses IP addressing scheme to filter traffic
- -Main function is to route packets from one network to another.
- -Isolates the internal network from the outside (Internet).
- -Every port is a broadcast domain.

<!-- image -->

<!-- image -->

## Basic Network Devices

- Firewall
- A network security tool used to filter and block unauthorize traffic based on the policies implemented by the organization.

Sample Photo/Network Symbol

<!-- image -->

<!-- image -->

<!-- image -->

## Basic Network Devices

## · IDS/IPS

- -Intrusion Detection System or IDS, is a network security tool used to monitor traffic for malicious activity or policy violations and sends

notification to the administrator

- -Intrusion Prevention System or IPS, is a network security tool used to inspect, detect and classify network traffic and proactively stops malicious activities from occurring into the network.

<!-- image -->

<!-- image -->

## Basic Network Devices

- Load Balancer
- -Load balancers manage the flow of information between the server and an endpoint device (PC, laptop, tablet or smartphone).

<!-- image -->

<!-- image -->

## Basic Network Devices

- Proxy Server
- A proxy server acts as another gateway between you and the internet.
- Proxy servers provide varying levels of functionality, security, and privacy depending on your use case, needs, or company policy.

<!-- image -->

<!-- image -->

## Basic Network Devices

- Wireless Access Point
- -Devices that act as point of communication wirelessly.
- -Best example for this is the Wi-Fi technology (IEEE 802.11 standards).

<!-- image -->

<!-- image -->

## Basic Network Simulation

<!-- image -->

<!-- image -->

## Basic Network Simulation

<!-- image -->

<!-- image -->

## Basic Network Simulation

<!-- image -->

<!-- image -->

## Simulation Exercise

- Recreate the given point-topoint connection of routers below and apply all the basic router configuration for both. Ensure that both routers are reachable to each other using the 'ping' command.

<!-- image -->

<!-- image -->

## Router to Router Connection

## For line console 0:

Router(config-line)#password cisco

Router(config-line)#exec-timeout 1 30

Router(config-line)#logging synchronous

Router(config-line)#login

Router(config-line)#exit

## For line vty 0 4:

Router(config)#line vty 0 4

Router(config-line)#password cisco

Router(config-line)#exec-timeout 1 30

Router(config-line)#logging synchronous

Router(config-line)#login

Router(config-line)#exit

<!-- image -->

## Router to Router Connection

## For router configuration

Router(config)#hostname TUPManila

TUPManila(config)#enable secret class

TUPManila(config)#service password encryption

TUPManila(config)#no ip domain-lookup

TUPManila(config)#banner motd ' AUTHORIZED ACCESS ONLY! '

## Interface Configuration:

TUPManila(config)#interface FastEthernet x/y or GigabitEthernet x/y TUPManila(config-if)#ip address assigned IP subnet mask TUPManila(config-if)#no shutdown

## Saving Router Configuration:

TUPManila#write or copy run start

<!-- image -->

## Open Forum

<!-- image -->

<!-- image -->

## Course References

- Forouzan, Behrouz (2007) Data Communications and Networking (4th ed.) McGraw-Hill Education
- Tomasi, W. (2004) Electronic Communication Systems (5th ed.)
- Sapak, M. (2017) Digital Communications (1st ed.)
- Ciora, J (2008) CCNA Exam Prep (2 nd ed.) Pearson Education Inc.
- Odom, W. (2019) CCNA 200-301 Official Cert Guide Library vol. 1 &amp; 2 (1 st ed.) Cisco Press
- https://jimayson.wordpress.com/2011/08/13/the-night-benjiehooked-up-the-philippines-to-the-internet/

<!-- image -->

Thank you for listening!

Stay safe and God bless,

Future Engineers!

☺

<!-- image -->

- Sir Jepp

<!-- image -->