# Chapter 2:  The Microprocessor and its Architecture

# Introduction 

This chapter presents the microprocessor as a programmable device by first looking at its internal programming model and then how its memory space is addressed. 

The architecture of Intel microprocessors is presented, as are the ways that the family members address the memory system.

Addressing modes for this powerful family of microprocessors are described for the real, protected, and flat modes of operation. 

# Chapter Objectives 

Describe function and purpose of each program-visible register in the 8086-Core2 microprocessors, including 64-bit extensions.

Detail the flag register and the purpose of each flag bit.

Describe how memory is accessed using real mode memory-addressing techniques.

Upon completion of this chapter, you will be able to: 

# Chapter Objectives 

Describe how memory is accessed using protected mode memory-addressing techniques.

Describe how memory is accessed using the 64-bit flat memory model.

Describe program-invisible registers found in the 80286 through Core2 microprocessors.

Detail the operation of the memory-paging mechanism.

Upon completion of this chapter, you will be able to: 

(cont.)

# 2–1  INTERNAL MICROPROCESSOR ARCHITECTURE 

Before a program is written or instruction investigated, internal configuration of the microprocessor must be known. 

In a multiple core microprocessor each core contains the same programming model. 

Each core runs a separate task or thread simultaneously. 

# A thread consists of a program counter, a register set, and a stack space. A task shares with peer threads its code section, data section, and operating system resources

# The Programming Model 

8086 through Core2 considered program visible.

- registers are used during programming and are specified by the instructions 
- not addressable directly during applications programming

Other registers considered to be program invisible.

80286 and above contain program-invisible registers to control and operate protected memory. 

- and other features of the microprocessor 
- including the 64-bit extensions  

80386 through Core2 microprocessors contain full 32-bit internal architectures.

8086 through the 80286 are fully upward-compatible to the 80386 through Core2.

Figure 2–1 illustrates the programming model 8086 through Core2 microprocessor.

# Figure 2–1  The programming model of the 8086 through the Core2 microprocessor including the 64-bit extensions. 

<!-- image -->

# Multipurpose Registers 

RAX - a 64-bit register (RAX), a 32-bit register (accumulator) (EAX), a 16-bit register (AX), or as either of two 8-bit registers (AH and AL). 

The accumulator is used for instructions such as multiplication, division, and some of the adjustment instructions. 

Intel plans to expand the address bus to 52 bits to address 4P (252~1015 =peta) bytes of memory.

RBX, addressable as RBX, EBX, BX, BH, BL.

- BX register (base index) sometimes holds offset address of a location in the memory system in all versions of the microprocessor 
- a (count) general-purpose register that also holds the count for various instructions 
- a (data) general-purpose register
- holds a part of the result from a multiplication or part of dividend before a division

RCX, as RCX, ECX, CX, CH, or CL.

RDX, as RDX, EDX, DX, DH, or DL.

RBP, as RBP, EBP, or BP.

- points to a memory (base pointer) location for memory data transfers
- often addresses (destination index) string destination data for the string instructions
- the (source index) register addresses source string data for the string instructions
- like RDI, RSI also functions as a general- purpose register

RDI addressable as RDI, EDI, or DI.

RSI used as RSI, ESI, or SI. 

R8 - R15 found in the Pentium 4 and Core2 if 64-bit extensions are enabled. 

- data are addressed as 64-, 32-, 16-, or 8-bit sizes and are of general purpose
- the 8-bit portion is the rightmost 8-bit only
- bits 8 to 15 are not directly addressable as a byte

Most applications will not use these registers until 64-bit processors are common. 

# Special-Purpose Registers 

Include RIP, RSP, and RFLAGS

- segment registers include CS, DS, ES, SS, FS, and GS
- defined as (instruction pointer) a code segment 
- the (stack pointer) stores data through this pointer

RIP addresses the next instruction in a section of memory.

RSP addresses an area of memory called  the stack. 

RFLAGS indicate the condition of the microprocessor and control its operation.

Figure 2–2 shows the flag registers of all versions of the microprocessor. 

Flags are upward-compatible from the 8086/8088 through Core2 .

The rightmost five and the overflow flag are changed by most arithmetic and logic operations.

- although data transfers do not affect them

# Figure 2–2  The EFLAG and FLAG register counts for the entire 8086 and Pentium microprocessor family. 

<!-- image -->

Flags never change for any data transfer or program control operation.

Some of the flags are also used to control features found in the microprocessor. 

Flag bits, with a brief description of function.

C (carry) holds the carry after addition or  borrow after subtraction. 

- also indicates error conditions
- if a number contains three binary one bits, it has odd parity
- if a number contains no one bits, it has even parity

P (parity) is the count of ones in a number expressed as even or odd. Logic 0 for odd parity; logic 1 for even parity. 

# List of Each Flag bit, with a brief description of function.

C (carry) holds the carry after addition or  borrow after subtraction. 

- also indicates error conditions
- if a number contains three binary one bits, it has odd parity; If a number contains no one bits, it has even parity

P (parity) is the count of ones in a number expressed as even or odd. Logic 0 for odd parity; logic 1 for even parity. 

A (auxiliary carry) holds the carry (half-carry) after addition or the borrow after subtraction between bit positions 3 and 4 of the result. 

Z (zero)	 shows that the result of an arithmetic or logic operation is zero. 

S (sign) flag holds the arithmetic sign of the result after an arithmetic or logic instruction executes.

T (trap)	The trap flag enables trapping through an on-chip debugging feature. 

I (interrupt) controls operation of the INTR (interrupt request) input pin. 

D (direction)	 selects increment or decrement mode for the DI and/or SI registers.

O (overflow)	 occurs when signed numbers are added or subtracted. 

- an overflow indicates the result has exceeded the capacity of the machine

IOPL used in protected mode operation to select the privilege level for I/O devices. 

NT (nested task)	flag indicates the current task is nested within another task in protected mode operation.

RF (resume)	 used with debugging to control resumption of execution after the next instruction.

VM (virtual mode) flag bit selects virtual mode operation in a protected mode system. 

AC, (alignment check) flag bit activates if a word or doubleword is addressed on a non-word or non-doubleword boundary.

VIF is a copy of the interrupt flag bit available to the Pentium 4–(virtual interrupt)

VIP (virtual) provides information about a virtual mode interrupt for (interrupt pending) Pentium. 

- used in multitasking environments to provide virtual interrupt flags

ID (identification)	 flag indicates that the Pentium microprocessors support the CPUID instruction. 

- CPUID instruction provides the system with information about the Pentium microprocessor

# Segment Registers 

Generate memory addresses when combined with other registers in the microprocessor.

Four or six segment registers in various versions of the microprocessor.

A segment register functions differently in real mode than in protected mode.

Following is a list of each segment register, along with its function in the system.

CS (code) segment holds code (programs and procedures) used by the microprocessor.

DS (data) contains most data used by a program. 

- Data are accessed by an offset address or contents of other registers that hold the offset address

ES (extra) an additional data segment used by some instructions to hold destination data. 

SS (stack) defines the area of memory used for the stack. 

- stack entry point is determined by the stack segment and stack pointer registers 
- the BP register also addresses data within the stack segment 

FS and GS segments are supplemental segment registers available in 80386–Core2 microprocessors.

- allow two additional memory segments for access by programs 

Windows uses these segments for internal operations, but no definition of their usage is available. 

# 2–2  REAL MODE MEMORY ADDRESSING 

80286 and above operate in either the real or protected mode. 

Real mode operation allows addressing of only the first 1M byte of memory space—even in Pentium 4 or Core2 microprocessor. 

- the first 1M byte of memory is called the real memory, conventional memory, or DOS memory system

# Segments and Offsets 

All real mode memory addresses must consist of a segment address plus an offset address. 

- segment address defines the beginning address of any 64K-byte memory segment
- offset address selects any location within the 64K byte memory segment

Figure 2–3 shows how the segment plus offset addressing scheme selects a memory location. 

# Figure 2–3  The real mode memory-addressing scheme, using a segment address plus an offset. 

<!-- image -->

- this shows a memory segment beginning at 10000H, ending at location IFFFFH
- 64K bytes in length 
- also shows how an offset address, called a displacement, of F000H selects location 1F000H in the memory

Once the beginning address is known, the ending address is found by adding FFFFH.

- because a real mode segment of memory is64K in length
- a segment address of 1000H; an offset of 2000H

The offset address is always added to the segment starting address to locate the data.

Segment and offset address is sometimes written as 1000:2000.

# Default Segment and Offset Registers 

The microprocessor has rules that apply to segments whenever memory is addressed. 

- these define the segment and offset register combination 

The code segment register defines the start of the code segment.

The instruction pointer locates the next instruction within the code segment. 

Another of the default combinations is the stack. 

- stack data are referenced through the stack segment at the memory location addressed by either the stack pointer (SP/ESP) or the pointer (BP/EBP)
- a memory segment can touch or overlap if 64K bytes of memory are not required for a segment 

Figure 2–4 shows a system that contains four memory segments.

# Figure 2–4  A memory system showing the placement of four memory segments. 

<!-- image -->

- think of segments as Windows that can be moved over any area of memory to access data or code 
- a program can have more than four or six segments, 
- but only access four or six segments at a time

# Figure 2–5  An application program containing a code, data, and stack segment loaded into a DOS system memory. 

<!-- image -->

- a program placed in memory by DOS is loaded in the TPA at the first available area of memory above drivers and other TPA programs 
- area is indicated by a free-pointer maintained by DOS
- program loading is handled automatically by the program loader within DOS

# TPA

The transient program area (TPA) holds the DOS (disk operating system) operating system; other programs that control the computer system.

# Segment and Offset Addressing Scheme Allows Relocation 

Segment plus offset addressing allows DOS programs to be relocated in memory.

A relocatable program is one that can be placed into any area of memory and executed without change.

Relocatable data are data that can be placed in any area of memory and used without any change to the program. 

Because memory is addressed within a segment by an offset address, the memory segment can be moved to any place in the memory system without changing any of the offset addresses. 

Only the contents of the segment register must be changed to address the program in the new area of memory.

Windows programs are written assuming that the first 2G of memory are available for code and data. 

# 2–3  INTRO TO PROTECTED MODE MEMORY ADDRESSING 

Allows access to data and programs located within &amp; above the first 1M byte of memory.

Protected mode is where Windows operates.

In place of a segment address, the segment register contains a selector that selects a descriptor from a descriptor table. 

The descriptor describes the memory segment’s location, length, and access rights. 

# Selectors and Descriptors 

The descriptor is located in the segment register &amp; describes the location, length, and access rights of the segment of memory. 

- it selects one of 8192 descriptors from one of two tables of descriptors

In protected mode, this segment number can address any memory location in the system for the code segment.

Indirectly, the register still selects a memory segment, but not directly as in real mode.

Global descriptors contain segment definitions that apply to all programs.

Local descriptors are usually unique to an application. 

- a global descriptor might be called a system descriptor, and local descriptor an application descriptor 
- each descriptor is 8 bytes in length
- global and local descriptor tables are a maximum of 64K bytes in length 

Figure 2–6 shows the format of a descriptor for the 80286 through the Core2. 

# Figure 2–6  The 80286 through Core2 64-bit descriptors. 

<!-- image -->

The base address of the descriptor indicates the starting location of the memory segment.

- the paragraph boundary limitation is removed in protected mode
- segments may begin at any address
- 32-bit offset address allows segment lengths of 4G bytes
- 16-bit offset address allows segment lengths of 64K bytes. 

The G, or granularity bit allows a segment length of 4K to 4G bytes in steps of 4K bytes. 

Operating systems operate in a 16- or 32-bit environment. 

DOS uses a 16-bit environment.

Most Windows applications use a 32-bit environment called WIN32.

MSDOS/PCDOS &amp; Windows 3.1 operating systems require 16-bit instruction mode. 

Instruction mode is accessible only in a protected mode system such as Windows Vista. 

The access rights byte controls access to the protected mode segment. 

- describes segment function in the system and allows complete control over the segment
- if the segment is a data segment, the direction of growth is specified 

If the segment grows beyond its limit, the operating system is interrupted, indicating a general protection fault. 

You can specify whether a data segment can be written or is write-protected. 

# Figure 2–7  The access rights byte for the 80286 through Core2 descriptor. 

<!-- image -->

Descriptors are chosen from the descriptor table by the segment register. 

- register contains a 13-bit selector field, a table selector bit, and requested privilege level field 
- If privilege levels are violated, system normally indicates an application or privilege level violation

The TI bit selects either the global or the local descriptor table.

Requested Privilege Level (RPL) requests the access privilege level of a memory segment. 

# Figure 2–8  The contents of a segment register during protected mode operation of the 80286 through Core2 microprocessors. 

<!-- image -->

Figure 2–9 shows how the segment register, containing a selector, chooses a descriptor from the global descriptor table. 

The entry in the global descriptor table selects a segment in the memory system. 

Descriptor zero is called the null descriptor, must contain all zeros, and may not be used for accessing memory.

# Figure 2–9  Using the DS register to select a description from the global descriptor table. In this example, the DS register accesses memory locations 00100000H–001000FFH as a data segment. 

<!-- image -->

# Program-Invisible Registers 

Global and local descriptor tables are found in the memory system.

To access &amp; specify the table addresses, 80286–Core2 contain program-invisible registers. 

- not directly addressed by software
- often called cache memory because cache is any memory that stores information

Each segment register contains a program-invisible portion used in the protected mode. 

# Figure 2–10  The program-invisible register within the 80286–Core2 microprocessors. 

<!-- image -->

When a new segment number is placed in a segment register, the microprocessor accesses a descriptor table and loads the descriptor into the program-invisible portion of the segment register. 

- held there and used to access the memory segment until the segment number is changed 
- hence the term cache

This allows the microprocessor to repeatedly access a memory segment without referring to the descriptor table.

The GDTR (global descriptor table register) and IDTR (interrupt descriptor table register) contain the base address of the descriptor table and its limit. 

- when protected mode operation desired, address of the global descriptor table and its limit are loaded into the GDTR
- one of the global descriptors is set up to  address the local descriptor table

The location of the local descriptor table is selected from the global descriptor table. 

To access the local descriptor table, the LDTR (local descriptor table register) is loaded with a selector. 

- selector accesses global descriptor table, &amp; loads local descriptor table address, limit, &amp; access rights into the cache portion of the LDTR
- a task is most often a procedure or application 

The TR (task register) holds a selector, which accesses a descriptor that defines a task. 

Allows multitasking systems to switch tasks to another in a simple and orderly fashion.