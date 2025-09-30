# Topic1

Disclaimer:

- Slides not mine…

# The Microprocessor Age 

World’s first microprocessor the Intel 4004.

A 4-bit microprocessor-programmable controller on a chip. 

Addressed 4096, 4-bit-wide memory locations.

- a bit is a binary digit with a value of one or zero
- 4-bit-wide memory location often called a nibble

The 4004 instruction set contained 45 instructions.

Fabricated with then-current state-of-the-art P-channel MOSFET technology. 

Executed instructions at 50 KIPs (kilo-instructions per second). 

- slow compared to 100,000 instructions per second by 30-ton ENIAC computer in 1946 
- early shuffleboard game produced by Bailey

Difference was that 4004 weighed less than an ounce.

4-bit microprocessor debuted in early game systems and small control systems. 

Main problems with early microprocessor were speed, word width, and memory size. 

Evolution of 4-bit microprocessor ended when Intel released the 4040, an updated 4004. 

- operated at a higher speed; lacked improvements in word width and memory size 
- still survives in low-end applications such as microwave ovens and small control systems
- Calculators still based on 4-bit BCD (binary-coded decimal) codes

Texas Instruments and others also produced 4-bit microprocessors. 

With the microprocessor a commercially viable product, Intel released 8008 in 1971.

- extended 8-bit version of 4004 microprocessor
- A byte is generally an 8-bit-wide binary number and a K is 1024. 
- memory size often specified in K bytes
- engineers developed demanding uses for 8008

Addressed expanded memory of 16K bytes.

Contained additional instructions, 48 total.

Provided opportunity for application in more advanced systems.

Somewhat small memory size, slow speed, and instruction set limited 8008 usefulness. 

Intel introduced 8080 microprocessor in 1973.

- first of the modem 8-bit microprocessors 
- other companies soon introduced their own versions of the 8-bit microprocessor

Motorola Corporation introduced MC6800 microprocessor about six months later. 

8080—and, to a lesser degree, the MC6800—ushered in the age of the microprocessor.

# Table 1–1  Early 8-bit microprocessors 

<!-- image -->

Only Intel and Motorola continue to create new, improved microprocessors.

- IBM also produces Motorola-style microprocessors
- now called Freescale Semiconductors, Inc. 
- microcontrollers and embedded controllers instead of general-purpose microprocessors

Motorola sold its microprocessor division.

Zilog still manufactures microprocessors. 

# What Was Special about the 8080?   

8080 addressed four times more memory.

- 64K bytes vs l6K bytes for 8008 
- addition taking 20 µs on an 8008-based system required only 2.0 µs on an 8080-based system 
- the 8008 was not directly compatible 

Executed additional instructions; 10x faster. 

TTL (transistor-transistor logic) compatible.

Interfacing made easier and less expensive.

The MITS Altair 8800, was released in 1974.

- number 8800 probably chosen to avoid copyright violations with Intel
- Bill Gates and Paul Allen, founders of Microsoft Corporation 
- once produced DR-DOS for the personal computer

BASIC language interpreter for the Altair 8800 computer developed in 1975. 

The assembler program for the Altair 8800 was written by Digital Research Corporation.

# The 8085 Microprocessor 

In 1977 Intel Corporation introduced an updated version of the 8080—the 8085. 

Last 8-bit, general-purpose microprocessor developed by Intel.

Slightly more advanced than 8080; executed software at an even higher speed. 

- 769,230 instructions per second vs 500,000 per second on the 8080).

Main advantages of 8085 were its internal clock generator and system controller, and higher clock frequency.

- higher level of component integration reduced the 8085’s cost and increased its usefulness
- its most successful 8-bit, general-purpose microprocessor. 
- also manufactured by many other companies, meaning over 200 million in existence 

Intel has sold over 100 million of the 8085.

Applications that contain the 8085 will likely continue to be popular.

Zilog Corporation sold 500 million of their 8-bit Z80microprocessors. 

The Z-80 is machine language–compatible with the 8085. 

Over 700 million microprocessors execute 8085/Z-80 compatible code.

# The Modern Microprocessor 

In 1978 Intel released the 8086; a year or so later, it released the 8088.  

Both devices are 16-bit microprocessors.

- executed instructions in as little as 400 ns (2.5 millions of instructions per second) 
- major improvement over execution speed of 8085
- 16 times more memory than the 8085
- 1M-byte memory contains 1024K byte-sized memory locations or 1,048,576 bytes

8086 &amp; 8088 addressed 1M byte of memory.

Higher speed and larger memory size allowed 8086 &amp; 8088 to replace smaller minicomputers in many applications.

Another feature was a 4- or 6-byte instruction cache or queue that prefetched instructions before they were executed. 

- queue sped operation of many sequences of instruction
- basis for the much larger instruction caches found in modem microprocessors. 

Increased memory size and additional instructions in 8086/8088 led to many sophisticated applications.

Improvements to the instruction set included multiply and divide instructions.

- missing on earlier microprocessors 
- from 45 on the 4004, to 246 on the 8085
- over 20,000 variations on the 8086 &amp; 8088

Number of instructions increased.

These microprocessors are called CISC (complex instruction set computers).

- additional instructions eased task of developing efficient and sophisticated applications
- additional registers allowed software to be written more efficiently
- evolved to meet need for larger memory systems 

16-bit microprocessor also provided more internal register storage space. 

Popularity of Intel ensured in 1981 when IBM chose the 8088 in its personal computer.

Spreadsheets, word processors, spelling checkers, and computer-based thesauruses were memory-intensive .

- required more than 64K bytes of memory found	 in 8-bit microprocessors to execute efficiently
- The 16-bit 8086 and 8088 provided 1M byte of memory for these applications 

# The 80286 Microprocessor 

Even the 1M-byte memory system proved limiting for databases and other applications.

- Intel introduced the 80286 in 1983 
- an updated 8086 
- addressed 16M-byte memory system instead of a 1M-byte system 
- managed the extra 15M bytes of memory

Almost identical to the 8086/8088.

Instruction set almost identical except for a few additional instructions.

80286 clock speed increased in 8.0 Mhz version. 

- executed some instructions in as little as 250 ns (4.0 MIPs) 

Some changes to internal execution of instructions led to eightfold increase in speed for many instructions.

# The 32-Bit Microprocessor 

Applications demanded faster microprocessor speeds, more memory, and wider data paths.

Led to the 80386 in 1986 by Intel. 

- major overhaul of 16-bit 8086–80286 architecture
- Intel produced an earlier, unsuccessful 32-bit microprocessor called iapx-432

Intel’s first practical microprocessor to contain a 32-bit data bus and 32-bit memory address.

Through 32-bit buses, 80386 addressed up to 4G bytes of memory. 

- 1G memory = 1024M, or 1,073,741,824 locations
- 1,000,000 typewritten, double-spaced pages of ASCII text data 

80386SX addressed 16M bytes of memory through a 16-bit data and 24-bit address bus.

80386SL/80386SLC addressed 32M bytes memory via 16-bit data, 25-bit address bus.

80386SLC contained an internal cache to process data at even higher rates. 

Intel released 80386EX in 1995.

Called an embedded PC. 

- contains all components of the AT class computer on a single integrated circuit

24 lines for input/output data.

26-bit address bus; 16-bit data bus.

DRAM refresh controller.

Programmable chip selection logic

Applications needing higher speeds and large memory systems include software systems that use a GUI, or graphical user interface

Modern graphical displays contain 256,000 or more picture elements (pixels, or pels). 

VGA (variable graphics array) resolution is 640 pixels per scanning line by 480 lines. 

- resolution used to display computer boot screen
- requires a high-speed microprocessor

To display one screen of information, each picture element must be changed.

GUI packages require high microprocessor speeds and accelerated video adapters for quick and efficient manipulation of video text and graphical data. 

- the most striking system is Microsoft Windows 

GUI often called a WYSIWYG (what you see is what you get) display.

32-bit microprocessor needed due to size of its data bus. 

- transfers real (single-precision floating-point) numbers that require 32-bit-wide memory 
- with 8-bit data bus, takes four read or write cycles
- only one read or write cycle is required for 32 bit 

To process 32-bit real numbers, the microprocessor must efficiently pass them between itself and memory. 

Significantly increases speed of any program that manipulates real numbers.

High-level languages, spreadsheets, and database management systems use real numbers for data storage. 

- also used in graphical design packages that use vectors to plot images on the video screen 
- CAD (computer-aided drafting/design)  systems as AUTOCAD, ORCAD
- allowed memory resources to be allocated and managed by the operating system 

80386 had higher clocking speeds and included a memory management unit. 

80386 included hardware circuitry for memory management and assignment.

- improved efficiency, reduced software overhead
- earlier microprocessors left memory  management completely to the software
- additional instructions referenced 32-bit registers and managed the memory system 

Instruction set, memory management upward-compatible with 8086, 8088, and 80286.

Features allowed older, 16-bit software to operate on the 80386 microprocessor.

# The 80486 Microprocessor 

In 1989 Intel released the 80486.

Highly integrated package.

80386-like microprocessor.

80387-like numeric coprocessor.

8K-byte cache memory system. 

Internal structure of 80486 modified so about half of its instructions executed in one clock instead of two clocks.

- in a 50 MHz version, about half  of instructions executed in 25 ns (50 MIPs) 
- 50% over 80386 operated at same clock speed 
- called a double-clocked microprocessor

Double-clocked 80486DX2 executed instructions at 66 MHz, with memory transfers at 33 MHz. 	

A triple-clocked version improved speed to 100 MHz with memory transfers at 33 MHz.

- about the same speed as 60 MHz Pentium. 
- in place of standard 8K-byte cache 

Expanded 16K-byte cache. 

Advanced Micro Devices (AMD) produced a triple-clocked version with a bus speed of 40 MHz and a clock speed of 120 MHz. 

The future promises rates 10 GHz or higher.

Other versions called OverDrive processors.

- a double-clocked 80486DX that replaced an 80486SX or slower-speed 80486DX 
- functioned as a doubled-clocked version of the microprocessor

# The Pentium Microprocessor 

Introduced 1993, Pentium was similar to 80386 and 80486 microprocessors. 

Originally labeled the P5 or 80586.

- Intel decided not to use a number because it appeared to be impossible to copyright a number 

Introductory versions operated with a clocking frequency of 60 MHz &amp; 66 MHz, and a speed of 110 MIPs.

Double-clocked Pentium at 120 MHz and 133 MHz, also available.

- fastest version produced 233 MHz Pentium a three and one-half clocked version 
- depending on the version of the Pentium

Cache size was increased to 16K bytes from the 8K cache found in 80486.

8K-byte instruction cache and data cache.

Memory system up to 4G bytes.

Data bus width increased to a full 64 bits.

Data bus transfer speed 60 MHz or 66 MHz.

Wider data bus width accommodated double-precision floating-point numbers used in high-speed, vector-generated graphical displays. 

- should allow virtual reality software and video to operate at more realistic rates
- comparable to commercial television 

Widened data bus and higher speed allow full-frame video displays at scan rates of 30 Hz or higher.

Recent Pentium versions also included additional instructions.

- multimedia extensions, or MMX instructions
- few software companies have used 
- no high-level language support for instructions
- system performs somewhere between a 66 MHz Pentium and a 75 MHz Pentium

Intel hoped MMX would be widely used

OverDrive (P24T) for older 80486 systems. 

63 MHz version upgrades 80486DX2 50 MHz systems; 83 MHz upgrades 66 MHz systems.

Pentium OverDrive represents ideal upgrade path from the 80486 to the Pentium.

- executes two instructions not dependent on each other, simultaneously per clocking period
- dual integer processors most ingenious feature 
- contains two independent internal integer processors called superscalar technology 

Jump prediction speeds execution of program loops; internal floating-point coprocessor handles floating-point data.

These portend continued success for Intel. 

Intel may allow Pentium to replace some  RISC (reduced instruction set computer) machines.

Some newer RISC processors execute more than one instruction per clock. 

- through superscaler technology 
- boosts Macintosh performance, but slow to efficiently emulate Intel microprocessors

Motorola, Apple, and IBM produce PowerPC, a RISC with two integer units and a floating-point unit. 

Currently 6 million Apple Macintosh systems

260 million personal computers based on Intel microprocessors.

1998 reports showed 96% of all PCs shipped with the Windows operating system.

Apple computer replaced PowerPC with the Intel Pentium in most of its computer systems. 

- appears that PowerPC could not keep pace with the Pentium line from Intel

To compare speeds of microprocessors, Intel devised the iCOMP- rating index. 

- composite of SPEC92, ZD Bench, Power Meter 

The iCOMP1 rating index is used to rate the speed of all Intel microprocessors through the Pentium.

Figure 1–2 shows relative speeds of the 80386DX 25 MHz version through the Pentium 233 MHz version.

# Figure 1–2  The Intel iCOMP-rating index. 

<!-- image -->

Since release of Pentium Pro and Pentium II, Intel has switched to the iCOMP2- rating.

- scaled by a factor of 10 from the iCOMP1 index 
- newer available do not compare versions

Figure 1–3 shows iCOMP2 index listing the Pentium III at speeds up to 1000 MHz.

Figure 1–4 shows SYSmark 2002 for the Pentium III and Pentium 4.

Intel has not released benchmarks that compare versions of the microprocessor since the SYSmark 2002. 

# Figure 1–3  The Intel iCOMP2-rating index. 

<!-- image -->

# Figure 1–4  Intel microprocessor performance using SYSmark 2002. 

<!-- image -->

# Pentium Pro Processor 

A recent entry, formerly named the P6. 

21 million transistors, integer units, floating-point unit, clock frequency 150 and 166 MHz 

Internal 16K level-one (L1) cache.

- 8K data, 8K for instructions
- Pentium Pro contains 256K level-two (L2) cache 
- can conflict and still execute in parallel 

Pentium Pro uses three execution engines, to execute up to three instructions at a time. 

Pentium Pro optimized to efficiently execute 32-bit code.

- often bundled with Windows NT rather than normal versions of Windows 95 
- Intel launched Pentium Pro for server market
- 36-bit address bus if configured for a 64G memory system

Pentium Pro can address 4G-byte or a 64G-byte memory system.

# Pentium II and Pentium Xeon Microprocessors 

Pentium II, released 1997, represents new direction for Intel.

Intel has placed Pentium II on a small circuit board, instead of being an integrated circuit.

- L2 cache on main circuit board of not fast enough to function properly with Pentium II

Microprocessor on the Pentium II module actually Pentium Pro with MMX extensions.

In 1998 Intel changed Pentium II bus speed.

- newer Pentium II uses a 100 MHz bus speed 
- replaces 10 ns SDRAM with 66 MHz bus speed
- 

Higher speed memory bus requires 8 ns SDRAM.

Intel announced Xeon in mid-1998. 

- specifically designed for high-end workstation and server applications 
- Intel produces a professional and home/business version of the Pentium II

Xeon available with 32K L1 cache and L2 cache size of 512K, 1M, or 2M bytes.

Xeon functions with the 440GX chip set. 

Also designed to function with four Xeons in the same system, similar to Pentium Pro. 

Newer product represents strategy change.

A likely change is a shift from aluminum to copper interconnections inside the microprocessor.

Copper is a better conductor.

- should allow increased clock frequencies 
- especially true now that a method for using copper has surfaced at IBM  
- increase beyond current maximum 1033 MHz 

Another event to look for is a change in the speed of the front side bus. 

# Pentium III Microprocessor 

Faster core than Pentium II; still a P6 or Pentium Pro processor.

Available in slot 1 version mounted on a plastic cartridge.

Also socket 370 version called a flip-chip which looks like older Pentium package.

Pentium III available with clock frequencies up to 1 GHz.

Slot 1 version contains a 512K cache; flip-chip version contains 256K cache.

Flip-chip version runs at clock speed; Slot 1 cache version runs at one-half clock speed.

Both versions use 100 MHz memory bus.

- Celeron memory bus clock speed 66 MHz
- this change has improved performance
- memory still runs at 100 MHz

Front side bus connection, microprocessor to memory controller, PCI controller, and AGP controller, now either 100 or 133 MHz.

# Pentium 4 and Core2 Microprocessors 

Pentium 4 first made available in late 2000.

- most recent version of Pentium called Core2 
- uses Intel P6 architecture
- supporting chip sets use RAMBUS or DDR memory in place of SDRAM technology 
- improvement in internal integration, at present the 0.045 micron or 45 nm technology 

Pentium 4 available to 3.2 GHz and faster.

Core2 is available at speeds of up to 3 GHz.

# Pentium 4 and Core2, 64-bit and Multiple Core Microprocessors 

Recent modifications to Pentium 4 and Core2 include a 64-bit core and multiple cores.

64-bit modification allows address of over 4G (109) bytes of memory through a 64-bit address. 

- 40 address pins in these newer versions allow up to 1T (terabytes: 1000G) of memory to be accessed
- less important than ability to address more memory

Also allows 64-bit integer arithmetic.

Biggest advancement is inclusion of multiple cores.

- each core executes a separate task in a program
- called multithreaded applications

Increases speed of execution if program is written to take advantage of multiple cores.

Intel manufactures dual and quad core versions; number of cores will likely increase to eight or even sixteen.

Multiple cores are current solution to providing faster microprocessors.

Intel recently demonstrated Core2 containing 80 cores, using 45 nm fabrication technology.

Intel expects to release an 80-core version some time in the next 5 years. 

Fabrication technology will become slightly smaller with 35 nm and possibly 25 nm technology.

# The Future of Microprocessors 

No one can make accurate predictions.

Success of Intel should continue. 

Change to RISC technology may occur; more likely improvements to new hyper-threading technology.

- joint effort by Intel and Hewlett-Packard
- software for the system will survive

New technology embodies CISC instruction set of 80X86 family.

Basic premise is many microprocessors communicate directly with each other.

- allows parallel processing without any change to the instruction set or program
- new technology contains many microprocessors
- each contains its own register set linked with the other microprocessors’ registers 

Current superscaler technology uses many microprocessors; all share same register set. 

Offers true parallel processing without writing any special program.

In 2002, Intel released a new architecture 64 bits in width with a 128-bit data bus.

Named Itanium; joint venture called EPIC (Explicitly Parallel Instruction Computing) of Intel and Hewlett-Packard.

The Itanium architecture allows greater parallelism than traditional architectures.

128 general-purpose integer and 128 floating-point registers; 64 predicate registers.

Many execution units to ensure enough hardware resources for software.

# Figure 1–5a  Conceptual views of the 80486, Pentium Pro, Pentium II, Pentium III, Pentium 4, and Core2 microprocessors. 

<!-- image -->

# Figure 1–5b  Conceptual views of the 80486, Pentium Pro, Pentium II, Pentium III, Pentium 4, and Core2 microprocessors. 

<!-- image -->

Clock frequencies seemed to have peaked.

Surge to multiple cores has begun.

Memory speed a consideration. 

- speed of dynamic RAM memory has not changed for many years.
- main problem with large static RAM is heat 
- static RAM operates 50 times faster than dynamic RAM

Push to static RAM memory will eventually. increase the performance of the PC. 

Speed of mass storage another problem.

- transfer speed of hard disk drives has changed little in past few years 
- new technology needed for mass storage
- write speed comparable to hard disk memory 
- would allow operating system to load in a second or two instead of many seconds now required

Flash memory could be solution.

Flash memory could store the operating system for common applications.

# 1–2  THE MICROPROCESSOR-BASED PERSONAL COMPUTER SYSTEM 

Computers have undergone many changes recently. 

Machines that once filled large areas reduced to small desktop computer systems because of the microprocessor. 

- although compact, they possess computing power only dreamed of a few years ago

Figure 1–6 shows block diagram of the personal computer.

Applies to any computer system, from early mainframe computers to the latest systems.

Diagram composed of three blocks interconnected by buses. 

- a bus is the set of common connections that carry the same type of information

# Figure 1–6  The block diagram of a microprocessor-based computer system. 

<!-- image -->

# The Memory and I/O System 

Memory structure of all Intel-based personal computers similar.

Figure 1–7 illustrates memory map of a personal computer system. 

This map applies to any IBM personal computer. 

- also any IBM-compatible clones in existence

# Figure 1–7  The memory map of a personal computer. 

<!-- image -->

Main memory system divided into three parts:

- TPA (transient program area) 
- system area
- XMS (extended memory system) 
- Intel microprocessors designed to function in this area using real mode operation

Type of microprocessor present determines whether an extended memory system exists. 

First 1M byte of memory often called the real or conventional memory system.

80286 through the Core2 contain the TPA (640K bytes) and system area (384K bytes).

- also contain extended memory
- often called AT class machines 
- depending on the model number

The PS/1 and PS/2 by IBM are other versions of the same basic memory design. 

Also referred to as ISA (industry standard architecture) or EISA (extended ISA). 

The PS/2 referred to as a micro-channel architecture or ISA system.

Pentium and ATX class machines feature addition of the PCI (peripheral component interconnect) bus.

- now used in all Pentium through Core2 systems 

Extended memory up to 15M bytes in the 80286 and 80386SX; 4095M bytes in 80486 80386DX, Pentium microprocessors. 

The Pentium Pro through Core2 computer systems have up to 1M less than 4G or 1 M less than 64G of extended memory.

Servers tend to use the larger memory map.

Many 80486 systems use VESA local, VL bus to interface disk and video to the microprocessor at the local bus level.

- allows 32-bit interfaces to function at same clocking speed as the microprocessor
- recent modification supporting 64-bit data bus  has generated little interest 
- specifically designed to function with the Pentium through Core2 at a bus speed of 33 MHz.

ISA/EISA standards function at 8 MHz.

PCI bus is a 32- or 64-bit bus. 

Three newer buses have appeared.

USB (universal serial bus). 

- intended to connect peripheral devices to the microprocessor through a serial data path and a twisted pair of wires	 

Data transfer rates are 10 Mbps for USB1.

Increase to 480 Mbps in USB2.

Increase to 480X10 Mbps in USB3.

AGP (advanced graphics port) for video cards.

The port transfers data between video card and microprocessor at higher speeds. 

- 66 MHz, with 64-bit data path
- video subsystem change made to accommodate new DVD players for the PC.

Latest AGP speed 8X or 2G bytes/second. 

Latest new buses are serial ATA interface (SATA) for hard disk drives; PCI Express bus for the video card. 

The SATA bus transfers data from PC to hard disk at rates of 150M bytes per second; 300M bytes for SATA-2.

- serial ATA standard will eventually reach speeds of 450M bytes per second 

PCI Express bus video cards operate at 16X speeds today.

# The TPA

The transient program area (TPA) holds the DOS (disk operating system) operating system; other programs that control the computer system.

- the TPA is a DOS concept and not really applicable in Windows 
- also stores any currently active or inactive DOS application programs
- length of the TPA is 640K bytes 

# Figure 1–8  The memory map of the TPA in a personal computer. (Note that this map will vary between systems.) 

<!-- image -->

- DOS memory map shows how areas of TPA are used for system programs, data and drivers.
- also shows a large area of memory available for application programs
- hexadecimal number to left of each area represents the memory addresses that begin and end each data area 

Hexadecimal memory addresses number each byte of the memory system. 

- a hexadecimal number is a number represented in radix 16 or base 16
- each digit represents a value from 0 to 9 and  from A to F 
- 1234H is 1234 hexadecimal
- also represent hexadecimal data as 0x1234 for a 1234 hexadecimal

Often a hexadecimal number ends with an H to indicate it is a hexadecimal value. 

Interrupt vectors access DOS, BIOS (basic I/O system), and applications. 

Areas contain transient data to access I/O devices and internal features of the system. 

- these are stored in the TPA so they can be changed as DOS operates

The IO.SYS loads into the TPA from the disk whenever an MSDOS system is started.

IO.SYS contains programs that allow DOS to use keyboard, video display, printer, and other I/O devices often found in computers. 

The IO.SYS program links DOS to the programs stored on the system BIOS ROM.

Drivers are programs that control installable I/O devices. 

- mouse, disk cache, hand scanner, CD-ROM memory (Compact Disk Read-Only Memory), DVD (Digital Versatile Disk; Digital Video Disk), or installable devices, as well as programs

Installable drivers control or drive devices or programs added to the computer system.

DOS drivers normally have an extension of .SYS; MOUSE.SYS.

DOS version 3.2 and later files have an extension of .EXE; EMM386.EXE.

Though not used by Windows, still used to execute DOS applications, even with Win XP. 

Windows uses a file called SYSTEM.INI to load drivers used by Windows. 

Newer versions of Windows have a registry added to contain information about the system and the drivers used. 

You can view the registry with the REGEDIT program.

COMMAND.COM (command processor) controls operation of the computer from the keyboard when operated in the DOS mode. 

COMMAND.COM processes DOS commands as they are typed from the keyboard.

If COMMAND.COM is erased, the computer cannot be used from the keyboard in DOS mode.

- never erase COMMAND.COM, IO.SYS, or MSDOS.SYS to make room for other software
- your computer will not function

# The System Area 

Smaller than the TPA; just as important.

The system area contains programs on read-only (ROM) or flash memory, and areas of read/write (RAM) memory for data storage. 

Figure 1–9 shows the system area of a typical personal computer system. 

As with the map of the TPA, this map also includes the hexadecimal memory addresses of the various areas.

# Figure 1–9  The system area of a typical personal computer. 

<!-- image -->

- First area of system space contains video display RAM and video control programs on ROM or flash memory. 
- area starts at location A0000H and extends to C7FFFH 
- size/amount of memory depends on type of video display adapter attached

Display adapters generally have video RAM at A0000H–AFFFFH.

- stores graphical or bit-mapped data
- contains programs to control DOS video display
- used for expanded memory system (EMS) in PC or XT system; upper memory system in an AT

Memory at B0000H–BFFFFH stores text data. 

The video BIOS on a ROM or flash memory, is at locations C0000H–C7FFFH. 

C8000H–DFFFFH is often open or free.

Expanded memory system allows a 64K-byte page frame of memory for use by applications.

- page frame (D0000H - DFFFFH) used to expand memory system by switching in pages of memory from EMS into this range of memory addresses
- often open or free in newer computer systems

Locations E0000H–EFFFFH contain cassette BASIC on ROM found in early IBM systems.

Video system has its own BIOS ROM at location C0000H.

System BIOS ROM is located in the top 64K bytes of the system area (F0000H–FFFFFH). 

- controls operation of basic I/O devices connected to the computer system 
- does not control operation of video 

The first part of the system BIOS (F0000H–F7FFFH) often contains programs that set up the computer.

Second part contains procedures that control the basic I/O system.

# Windows Systems 

Modern computers use a different memory map with Windows than DOS memory maps.

The Windows memory map in Figure 1–10 has two main areas; a TPA and system area. 

The difference between it and the DOS memory map are sizes and locations of these areas.

# Figure 1–10  The memory map used by Windows XP. 

<!-- image -->

- TPA is first 2G bytes from locations 00000000H to 7FFFFFFFH.
- Every Windows program can use up to 2G bytes of memory located at linear addresses 00000000H through 7FFFFFFFH. 
- System area is last 2G bytes from 80000000H to FFFFFFFFH.

Memory system physical map is much different. 

Every process in a Windows Vista, XP, or 2000 system has its own set of page tables.

The process can be located anywhere in the memory, even in noncontiguous pages. 

The operating system assigns physical memory to application.

- if not enough exists, it uses the hard disk for any that is not available

# I/O Space 

I/O devices allow the microprocessor to communicate with the outside world.

I/O (input/output) space in a computer system extends from I/O port 0000H to port FFFFH.

- I/O port address is similar to a memory address
- instead of memory, it addresses an I/O device

Figure 1–11 shows the I/O map found in many personal computer systems.

# Figure 1–11  Some I/O locations in a typical personal computer. 

<!-- image -->

- Access to most I/O devices should always be made through Windows, DOS, or BIOS function calls.
- The map shown is provided as a guide to illustrate the I/O space in the system.

The area below I/O location 0400H is considered reserved for system devices

Area available for expansion extends from I/O port 0400H through FFFFH. 

Generally, 0000H - 00FFH addresses main board components; 0100H - 03FFH handles devices located on plug-in cards or also on the main board.

The limitation of I/O addresses between 0000 and 03FFH comes from original standards specified by IBM for the PC standard.

# The Microprocessor 

Called the CPU (central processing unit).

The controlling element in a computer system. 

Controls memory and I/O through connections called buses.

- buses select an I/O or memory device, transfer data between I/O devices or memory and the microprocessor, control I/O and memory systems 

Memory and I/O controlled via instructions stored in memory, executed by the microprocessor.

Microprocessor performs three main tasks:

- data transfer between itself and the memory or I/O systems
- simple arithmetic and logic operations
- program flow via simple decisions
- stored programs make the microprocessor and computer system very powerful devices

Power of the microprocessor is capability to execute billions of millions of instructions per second from a program or software (group of instructions) stored in the memory system.

Another powerful feature is the ability to make simple decisions based upon numerical facts.

- a microprocessor can decide if a number is zero, positive, and so forth 

These decisions allow the microprocessor to modify the program flow, so programs appear to think through these simple decisions.

# Buses 

A common group of wires that interconnect components in a computer system.

Transfer address, data, &amp; control information between microprocessor, memory and I/O. 

Three buses exist for this transfer of information: address, data, and control.

Figure 1–12 shows how these buses interconnect various system components.

# Figure 1–12  The block diagram of a computer system showing the address, data, and control bus structure. 

<!-- image -->

The address bus requests a memory location from the memory or an I/O location from the I/O devices.

- if I/O is addressed, the address bus contains a 16-bit I/O address from 0000H through FFFFH. 
- if memory is addressed, the bus contains a memory address, varying in width by type of microprocessor. 

64-bit extensions to Pentium provide 40 address pins, allowing up to 1T (240 .=.1012) byte of memory to be accessed.

The data bus transfers information between the microprocessor and its memory and I/O address space. 

Data transfers vary in size, from 8 bits wide to 64 bits wide in various Intel microprocessors. 

- 8088 has an 8-bit data bus that transfers 8 bits of data at a time
- 8086, 80286, 80386SL, 80386SX, and 80386EX transfer 16 bits of data
- 80386DX, 80486SX, and 80486DX, 32 bits 
- Pentium through Core2 microprocessors transfer 64 bits of data

Advantage of a wider data bus is speed in applications using wide data.

Figure 1–13 shows memory widths and sizes of  8086 through Core2 microprocessors.

In all Intel microprocessors family members, memory is numbered by byte.

Pentium through Core2 microprocessors contain a 64-bit-wide data bus.

# Figure 1–13a  The physical memory systems of the 8086 through the Core2 microprocessors. 

<!-- image -->

# Figure 1–13b  The physical memory systems of the 8086 through the Core2 microprocessors. 

<!-- image -->

Control bus lines select and cause memory or I/O to perform a read or write operation.

In most computer systems, there are four control bus connections:

MRDC	(memory read control)

MWTC	(memory write control)

IORC	(I/O read control)

IOWC	(I/O write control). 

overbar indicates the control signal is active-low; (active when logic zero appears on control line)

The microprocessor reads a memory location by sending the memory an address through the address bus.

Next, it sends a memory read control signal to cause the memory to read data.

Data read from memory are passed to the microprocessor through the data bus.

Whenever a memory write, I/O write, or I/O read occurs, the same sequence ensues.