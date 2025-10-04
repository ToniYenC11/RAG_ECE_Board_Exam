## BASIC GSM AND MOBILE NETWORKS

PECEC 3 - Communications 3: Data Communications (Lecture) Prepared by: Jepp Quijano, ECE, ECT

<!-- image -->

## Talking Points

- What is GSM?
- Evolution of Mobile Communication
- GSM Architecture
- Elements of GSM

<!-- image -->

## Global System for Mobile Communication

- formerly: Groupe Spéciale Mobile (founded 1982)
- now: Global System for Mobile Communication
- Pan-European standard (ETSI, European Telecommunications Standardisation Institute)
- simultaneous introduction of essential digital cellular services in three phases (1991, 1994, 1996) by the European telecommunication administrations, seamless roaming within Europe possible
- today many providers all over the world use GSM (more than 130 countries in Asia, Africa, Europe, Australia, America)
- more than 100 million subscribers

<!-- image -->

## Global System for Mobile Communication

- The most popular wireless communication systems which gives us the freedom to not only roam within a network, but also between different networks.
- Users can, in fact, communicate with other different users (almost) everywhere, and at (almost) any time. Failure dependencies can vary from signal strength in all areas up to the subscription payment of a user.
- GSM technology contains the essential intelligent functions for the support of personal mobility, especially with regards to user identification and authentication, and for the localization and administration of mobile users.
- The evolution took place from a simple messaging service to internet data usage and over-the-top (OTT) services.

<!-- image -->

## Performance Characteristics of GSM

- Communication
- Total mobility
- Worldwide connectivity
- High Transmission quality
- Security functions

<!-- image -->

## Disadvantages

- Offers less data rate compared to wired networks
- Macro cells are affected by multipath signal loss.
- The capacity is lower and depends on channels/multiple access techniques employed to serve subscribers.
- As the communication is over the air, it has security vulnerabilities.
- Requires higher cost in order to setup cellular network infrastructure.
- The wireless communication is influenced by physical obstructions, climatic conditions and interference from other wireless devices.

<!-- image -->

## Evolution of the Mobile Communication

## Generations of Mobile Communication

<!-- image -->

<!-- image -->

## GSM: Mobile Services

## GSM offers

- several types of connections
- voice connections, data connections, short message service
- multi-service options (combination of basic services)

## Three service domains

- Bearer Services - interface to the physical medium (transparent for example in the case of voice or non-transparent for data services)
- Telematic Services - services provided by the system to the end user (e.g., voice, SMS, fax, etc.)
- Supplementary Services - associated with the tele services: call forwarding, redirection, etc.

<!-- image -->

## GSM: Mobile Services

<!-- image -->

tele services

<!-- image -->

## GSM Architecture

## GSM is a PLMN (Public Land Mobile Network)

- several providers setup mobile networks following the GSM standard within each country
- components
- MS (mobile station)
- BS (base station)
- MSC (mobile switching center)
- LR (location register)
- subsystems
- RSS (radio subsystem): covers all radio aspects
- -NSS (network and switching subsystem): call forwarding, handover, switching
- OSS (operation subsystem): management of the network

<!-- image -->

## GSM Architecture Overview

<!-- image -->

<!-- image -->

## GSM Elements and Interfaces

<!-- image -->

<!-- image -->

## GSM System Architecture

<!-- image -->

<!-- image -->

## Radio Subsystem

## Components

- MS (Mobile Station)
- BSS (Base Station Subsystem): consisting of
- BTS (Base Transceiver Station): sender and receiver
- BSC (Base Station Controller): controlling several
- transceivers

## Interfaces

- 𝑈𝑚 : radio interface
- 𝐴𝑏𝑖𝑠 : standardized, open interface with 16 kbit/s user channels
- 𝐴 : standardized, open interface with 64 kbit/s user channels

<!-- image -->

## Radio Subsystem

- The Radio Subsystem (RSS) comprises the cellular mobile network up to the switching centers
- Components
- -Base Station Subsystem (BSS):
1. Base Transceiver Station (BTS): radio components including sender, receiver, antenna - if directed antennas are used one BTS can cover several cells
2. Base Station Controller (BSC): switching between BTSs, controlling BTSs, managing of network resources, mapping of radio channels (Um) onto terrestrial channels (A interface)

<!-- formula-not-decoded -->

- -Mobile Stations (MS)

<!-- image -->

## Cellular Network

- use of several carrier frequencies
- not the same frequency in adjoining cells
- cell sizes vary from some 100 m up to 35 km depending on user density, geography, transceiver power etc.
- hexagonal shape of cells is idealized (cells overlap, shapes depend on geography)
- if a mobile user changes cells - handover of the connection to the neighbor cell.

## segmentation of the area into cells

<!-- image -->

<!-- image -->

## BTS and BSC

- Tasks of a BSS are distributed over BSC and BTS
- BTS comprises radio specific functions
- BSC is the switching center for radio channels

| Functions                                  | BTS   | BSC   |
|--------------------------------------------|-------|-------|
| Management of radio channels               |       | X     |
| Frequency hopping (FH)                     | X     | X     |
| Management of terrestrial channels         |       | X     |
| Mapping of terrestrial onto radio channels |       | X     |
| Channel coding and decoding                | X     |       |
| Rate adaptation                            | X     |       |
| Encryption and decryption                  | X     | X     |
| Paging                                     | X     | X     |
| Uplink signal measurements                 | X     |       |
| Traffic measurement                        |       | X     |
| Authentication                             |       | X     |
| Location registry, location update         |       | X     |
| Handover management                        |       | X     |

<!-- image -->

## Network and Switching Subsystem

## Components

- MSC (Mobile Services Switching Center):
- IWF (Interworking Functions)
- ISDN (Integrated Services Digital Network)
- PSTN (Public Switched Telephone Network)
- PSPDN (Packet Switched Public Data Network)
- CSPDN (Circuit Switched Public Data Network)

## Databases

- HLR (Home Location Register)
- VLR (Visitor Location Register)
- EIR (Equipment Identity Register)

<!-- image -->

## Network and Switching Subsystem

- NSS is the main component of the public mobile network GSM switching, mobility management, interconnection to other networks, system control
- Components
1. Mobile Services Switching Center (MSC) controls all connections via a separated network to/from a mobile terminal within the domain of the MSC - several BSC can belong to a MSC
2. Databases (important: scalability, high capacity, low delay)
- -Home Location Register (HLR) central master database containing user data, permanent and semi-permanent data of all subscribers assigned to the HLR (one provider can have several HLRs)
- Visitor Location Register (VLR) local database for a subset of user data - data about all users currently visiting in the domain of the VLR

<!-- image -->

## Mobile Service Switching Center

- The MSC (mobile switching center) plays a central role in GSM
- switching functions
- additional functions for mobility support
- management of network resources
- interworking functions via Gateway MSC (GMSC)
- integration of several databases
- Functions of a MSC
- specific functions for paging and call forwarding
- termination of SS7 (signaling system no. 7)
- mobility specific signaling
- location registration and forwarding of location information
- provision of new services (fax, data calls)
- support of short message service (SMS)
- -generation and forwarding of accounting and billing information

<!-- image -->

## Operation Subsystem

- The OSS (Operation Subsystem) enables centralized operation, management, and maintenance of all GSM subsystems
- Components
1. Authentication Center (AUC)
- generates user specific authentication parameters on request of a VLR
- authentication parameters used for authentication of mobile terminals and encryption of user data on the air interface within the GSM system
2. Equipment Identity Register (EIR)
- registers GSM mobile stations and user rights
- stolen or malfunctioning mobile stations can be locked and sometimes even localized

<!-- image -->

## Operation Subsystem

- Components
3. Operation and Maintenance Center (OMC)
- different control capabilities for the radio subsystem and the network subsystem

<!-- image -->

## GSM Spectrum Allocation (900MHz)

<!-- image -->

<!-- image -->

## GSM Spectrum Allocation (1800MHz)

<!-- image -->

<!-- image -->

## TDMA/FDMA

<!-- image -->

<!-- image -->

## Call Simulation on 2G

## Sub A calls Sub B

<!-- image -->

<!-- image -->

## SMS Simulation on 2G

## Sub A sends SMS to Sub B

<!-- image -->

<!-- image -->

## GPRS

<!-- image -->

<!-- image -->

## Internet Surfing Simulation using GPRS

## Sub A connects to the Internet

<!-- image -->

<!-- image -->

## GSM Trends Worldwide

## Countries who partially or completely shutdown their 2G networks

<!-- image -->

<!-- image -->

## Other Current Use of GSM (2G)

- POS Machines
- Self-service eLoad
- GPS Tracker
- Network in a Box (NIB)

<!-- image -->

<!-- image -->

Size: ~500 x 400 x 200 mm

Weight: 20-25kg

Coverage: 5OOm-1km radius (2Om ant. height)

Radio Power: 5-10W

Battery: built-in with spare (3hrs each)

assessment ongoing on utilization of fuel cells

Interface: RJ45 Ethernet port; N-female ant.

Port

Bandwidth Rqmt: 1Mbps

## Features

- Internal Subscriber DB management

- Can be configured as master-slave with other NIBs

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
- https://courses.mnet-it.com/learn
- Eberspacher, J et. al (2009) GSM - Architecture, Protocols and Services (3 rd edition) John Wiley &amp; Sons, Ltd.

<!-- image -->

## Research Work

- Research and differentiate 3G, 4G and 5G architectures.

<!-- image -->

Thank you for listening!

Stay safe and God bless,

Future Engineers!

☺

<!-- image -->

- Sir Jepp

<!-- image -->