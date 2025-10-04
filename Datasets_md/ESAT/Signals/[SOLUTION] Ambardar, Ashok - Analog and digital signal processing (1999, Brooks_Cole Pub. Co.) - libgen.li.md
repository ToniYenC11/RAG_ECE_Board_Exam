## COMPLETE SOLUTIONS MANUAL FOR

## ANALOG AND DIGITAL SIGNAL PROCESSING

SECOND EDITION

AsHOKAMBARDAR

## Complete Solutions Manual for

## Analog and Digital Signal Processing

Second Edition

Ashok Ambardar

Michigan Technological University

<!-- image -->

Brooks/Cole Publishing Company

An Intemational Thomson Publishing Company

COPYRIGHT @ 1999 by Brooks/Cole Publishing Company A division of International Thomson Publishing Inc. I@P The ITP logo is a registered trademark used herein under license.

For more information, contact:

BROOKSICOLE PUBLISHNG COMPANY 511 Forest Lodge Road Pacifc Grove; CA 93950 USA

International Thomson Editores Seneca 53 Col. Polanco 11560 México, D. E,México

International Thomson Publishing Europe Beckshire House 168-173 High Holbom London WCIV 7AA England

International Thomson Publishing GmbH Königswinterer Strasse 418 53227 Bonn Germany

Thomas Nelson Australia 102 Dodds Street South Melbourne, 3205 Victoria, Australia

International Thomson Publishing Asia 60 Albert Street #15-01 Albert Complex Singapore 189969

Nelson Canada 1120 Birchmount Road Scarborough; Ontario CanadaMIK 5G4 Japan

International Thomson Publishing Palaceside Building, SF 1-1-1 Hitotsubashi Chiyoda-ku; 100-0003 Japan Tokyo

All rights reserved.  Instructors of classes Analog and Digital Signal Processing, 2nd Ed, by Ashok Ambardar; as a textbook reproduce material from this publication for classroom use. Otherwise, the text of this written permission of the publisher; Brooks/Cole Publishing Company, Pacific Grove, Califomia 93950. You can request permission to use material from this text through the following and fax numbers: using may prior phone

Phone: 1-800-730-2214

Fax: 1-800-730-2215

Printed in the United States of America

## CONTENTS

| A NOTE TO THE INSTRUCTOR      | A NOTE TO THE INSTRUCTOR      | A NOTE TO THE INSTRUCTOR              |     |
|-------------------------------|-------------------------------|---------------------------------------|-----|
| USEFUL MATHEMATICAL RELATIONS | USEFUL MATHEMATICAL RELATIONS | USEFUL MATHEMATICAL RELATIONS         | 2   |
| Chapter                       | 2                             | ANALOG SIGNALS                        |     |
| Chapter                       | 3                             | DISCRETE SIGNALS                      |     |
| Chapter                       | 4                             | ANALOG SYSTEMS                        | 45  |
| Chapter                       | 5                             | DISCRETE-TIME SYSTEMS                 | 65  |
| Chapter                       | 6                             | CONTINUOUS CONVOLUTION                | 92  |
| Chapter                       | 7                             | DISCRETE CONVOLUTION                  | 113 |
| Chapter                       | 8                             | FOURIER SERIES                        | 131 |
| Chapter                       | 9                             | THE FOURIER TRANSFORM                 | 157 |
| Chapter 10                    |                               | MODULATION                            | 190 |
| Chapter 11                    | Chapter 11                    | THE LAPLACE TRANSFORM                 | 200 |
| Chapter 12                    | Chapter 12                    | APPLICATIONS OF THE LAPLACE TRANSFORM | 219 |
| Chapter 13                    | Chapter 13                    | ANALOG FILTERS                        | 235 |
| Chapter 14                    | Chapter 14                    | SAMPLING AND QUANTIZATION             | 269 |
| Chapter 15                    | Chapter 15                    | THE DISCRETE-TIME FOURIER TRANSFORM   | 287 |
| Chapter 16                    | Chapter 16                    |                                       | 319 |
| Chapter 17                    | Chapter 17                    | THE z-TRANSFORM                       | 342 |
| Chapter 18                    | Chapter 18                    | APPLICATIONS OF THE z-TRANSFORM       | 380 |
| Chapter 19                    | Chapter 19                    | IIR DIGITAL FILIERS                   | 400 |
| Chapter 20                    | Chapter 20                    | FIR DIGITAL FILTERS                   | 416 |

## A Note to the Instructor

This manual contains solutions to all the end-of-chapter problems in the second edition of the text Analog and Digital Signal Processing: Itivial algebraic details have, for the most part, been omitted (in order to four places after tbe decimal) .

The m-files corresponding to the MATLAB code for the design /computation problems are also supplied on the accompanying disk in the subdirectory SOLUTION (as chXpY .n where X is the one/two digit chapter number and Y is the one/two digit problem number) . These files may be run without modification (for MATLAB v4:x or higher) or edited /expanded to suit your own needs.

The MATLAB code is by no means unique; no attempt was made to optimize it, and it is included only to give an indication of tbe expected results (even tbough few plots bave been reproduced). Routines from the ADSP toolbox (from the text) that were used for solving the problens are listed in the solutions; where appropriate;

This disk also contains updated versions of the following m-files (with extension .m) in the ADSP toolbox (that comes with the text). Tbese files reside in the subdirectory UPDAIES.

| FILE                  | UPDAIED FEAIURES                                |
|-----------------------|-------------------------------------------------|
| ustep afd,Ipp         | ADSP files Fixed bug for elliptic filter design |
| dfftgui dfftedt       | GUI files Fixed to catch callback errors bug    |
| dfirdes,dfirauop      | GUI files Fixed to catch callback errors bug    |
| fsgui,fsplt ,fssynplt | GUI files _ Fixed to catch callback errors bug  |
| ctconplt,dtsiggen     | GUI files. Fixed to catcb callback errors bug   |

## Installation

- 1 the solution files to a subdirectory on the hard drive (say solution) where MATLAB resides. Copy
2. the updated ADSP toolbox files over the already existing files in the subdirectories for tbe ADSP toolbox (Chapter 21 of the text describes tbe installation of the ADSP toolbox). Copy
- 3 Add the names of these subdirectories to the MATLAB path.
4. Start MATLAB. To run a file say ch3p44 .E, just enter its filename without the extension (ch3p44).

If you catch any errors in the text or in tbe solutions manual, Or discover any in the software; we would like to hear from you. errata for the text and the solutions manual that comes to our attention; and any upgrades to the software (including the files listed above) will appear on our Internet site. bugs Any

Ashok Ambardar

Michigan Technological University

Internet site:

ee mtu.edu/faculty/akambard.btnl

e-mail:

akanbard@mtu . edu

## USEFUL MATHEMATICAL RELATIONS

| TRIGONOMETRIC IDENTITIES   | TRIGONOMETRIC IDENTITIES           |
|----------------------------|------------------------------------|
|                            | cosQ                               |
|                            | cos(a + ß) = cosœcos ß F sinœsin ß |
| = 2 sin œ cosœ             | cos Za =                           |
| 2 sin? œ                   | cos 2a cos? Q sin? œ               |

<!-- image -->

## USEFUL MATHEMATICAL RELATIONS

## SEQUENCES AND SERIES

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

| SEQUENCES AND SERIES   | SEQUENCES AND SERIES         | SEQUENCES AND SERIES   | SEQUENCES AND SERIES      | SEQUENCES AND SERIES   |
|------------------------|------------------------------|------------------------|---------------------------|------------------------|
|                        | Jal <1                       | E* sin(kz)             | 1 2œ cos(z) +02 ,         |                        |
|                        | Q qk = lal < 1               |                        | Q cos(z) 1 2œ cos() + 02= |                        |
|                        | kœk = Q lal                  | 2                      | 1 +02,                    | 1                      |
|                        | 02 + Q Jol < 1               | sin(kz) k              |                           |                        |
|                        | ~alkl 1+e-0 e = œ > 0 1 ~e-Q | sin? (kr) k2 k=]       |                           |                        |

| Function   | Expansion                  | Remarks   |
|------------|----------------------------|-----------|
|            | 1 1 + 2! 2? 2}             | Il < 1    |
|            | 2 I=1 +2 2= 1 +2 4 3 5 I+1 | I > 0     |
| In(1 + 2)  | 1 1 1 (~I)n =-2 n          |           |
| I          | 1 1 - 12 + 4 3!            |           |
|            | 1                          | Inzl < 1  |

## ANALOG SIGNALS

- 2.1 (Solution) Tbe three signals are sketched below
- (a) y(t) = 2(-t): Fold z(t) about the vertical axis through the origin.

<!-- image -->

1

Signal y(t)=x(-t)

<!-- image -->

<!-- image -->

- Shift z(t) left (advance) by 3.

<!-- image -->

<!-- image -->

Confirm location of end-points tn tn +3=tòr tn =t - 3. For example: using

<!-- formula-not-decoded -->

- (c) g(t) = 2(2t 2) Shift z(t) right (delay) by 2 and then compress by 2

<!-- image -->

<!-- image -->

<!-- image -->

Confirm location of end-points tn using For example: For Signal 1: 2tn

- 2t): Shift z(t) left (advance) by 2, then compress by 2, then fold.

<!-- image -->

Confirm location of end-points tn 2 \_ 2tn = t. For example: using

For Signal 1:

t =3 \_ tn =-0.5 and t = 0 \_+ tn =1

<!-- image -->

Confirm location of end-points tn 0.5(tn 2) =t. For example: using

$$For Signal 1: t=3 =+ tn = 8 and t = 0 ~ tn = 2$$

- (f) s(t) = z(-0.5t 1) Shift z(t) right (delay) by 1, then stretch by 2 and fold. Signal Signal 2 s(t)=(-0.5t+1) Signal 3 s(t)=(-0.54+1)

<!-- image -->

For example:

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

- (g) Ie(t) (its even part): Add 0.52(t) and 0.52(-t)

<!-- image -->

<!-- image -->

Confirm by making sure %e(t) has even symmetry!

- Obtain the difference 0.52(t)

<!-- image -->

<!-- image -->

- 2.2 (Solution)
- (a) z(t) = e-tu(t) Thus, (t) = 0.5le-tu(t) + e'u(-t)] e'u(-t)]
- (b) I(t) = (1+t)2 Expand: z(t) = 1+ 2t +t2.

<!-- formula-not-decoded -->

## 2.3 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 2.4 (Solution) The periodic signals are shown below .

<!-- image -->

Compute tbe average value as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

VP

The signal energy for various signals from Review Panel 2.2 (reproduced below) will prove useful

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- E 56 (Signal 2) E = (4)2(3) + (~2)2(2) = 56 = =8 = Irms
- (Signal 3) Tbe pulse width is 3 units. Over one period, z(t) may be expressed as tbe sum of I1(t) and z2(t) as shown below.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Tbe energy in one period is tbus

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 2.5 (Solution)

- (a) te-tu(t) Energy signal with E = t2e = 0.25 (from tables)
- (b) e'[u(t) \_ u(t 1)] Energy signal with = 0.5(e? \_ 1) = 3.1945
- (c) signal (two-sided decaying exponential) with E = 2 +2e-2dt = 0.5 Energy
- (d) Neither an energy signal nor a signal. e~ power
- (e) 10e-'sin(t)u(t) Energy signal with E = 100 e-2t sin? ?(t)dt = 12.5 (from tables)
- (f) sinc(t)u(t) Energy signal with € = sinc? (t)dt = 0.5 (from tables)

## 2.6 (Solution)

Periodic. Tbe individual frequencies are 6 Hz and 15 Hz

Thus, fo = GCD(6, 15) = 3 Hz

Signal power P =

(4)2 +0.5(-3)2+0.5(1)2 = 21.

- = Periodic Individual frequencies are 15 Hz and 5 Hz. Thus; fo GCD(15, 5) = 5 Hz T =1/fo = 0.2 s

Signal power P = 0.5(0.5)2 +0.5(0.5)2 = 0.25.

- (c) z(t) = cos(20t) Almost periodic. Signal power P = 0.5(1)2 + 0.5(-1)2 = 1.
- 10)+)]  So, almost periodic. Signal power P = 0.5(0.5)2 + 0.5(0.5)2 = 0.25.
- Periodic. Individual frequencies are 6 Hz and 4 Hz. Thus, fo = GCD(6, 4) = 2 Hz +0.5(2)2 = 2.375.
- (f) z(t) = cos(2t) Vcos(2t = cos(2t) ~ [cos(2t) + sin(2t)] = sin(2t) . 1 So, periodic with frequency fo = Signal power P = 0.5(-1)2 = 0.5. T

## 2.7 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- Almost periodic with P = 0.5(1)2 + (0.5)2 + 0.5(0.5)2 = 0.875
- 2.8 (Solution) Refer to the following sketches.

<!-- image -->

## (a) For z(t) by intervals:

<!-- formula-not-decoded -->

- (b) For z(t) by steps and/or ramps:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) For z(t) by rect and/or tri functions:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 4x'(t) Signal 1 (t) Signal 2 4x'(t) Signal 3

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

- (e) For the signal energy; we use the results of Review Panel 2.2:
- (Signal 1:) Section r(t) into three pon-overlapping rectangular strips. E = (2)2(2) + (4)(2) + (2)2(2) = 48

<!-- formula-not-decoded -->

- (Signal 2:) Express z(t) as the sum of two signals z1(t) and 22(t) as shown

The signal energy is thus

<!-- formula-not-decoded -->

- (Signal 3:) Section z(t) into three non-overlapping triangular and rectangular strips.
- (Signal 4:) Section I(t) into two non-overlapping triangular strips.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (Signal 5:) Section z(t) into four non-overlapping triangular and rectangular strips.

<!-- image -->

- (Signal 6:) E = (4)2(22 4 (4)2(22 = 64 3 3 3
- 2.9 (Solution) The following signals are sketched below. The signals (d), (e), (h), (i), (k) and (1) are best sketched as the product of the individual terms.
- 2.10 (Solution) Tbe signals are sketched below. Here are some details.
- (a) z(t) = 38(t - 2) is an impulse at t = 2 with strength 3
- (b) z(t) = 38(2t 2) = gf(t ~ 1) (by the scaling property)
- ~ 1) (scaling and product properties)
- (scaling property)
- (f) 2(t) = because the rect function extends over 2.,5 &lt;t &lt; 7.5).

<!-- image -->

<!-- image -->

## 2.11 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 2.12 (Solution)

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- image -->

## (c) z(t) = 2rect(0.5t) + tri(t)

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

- 2.13 (Solution) Refer to the figures below. Note that in the ideally sampled signal, the impulse strengths equal the signal values but in the impulse approximation; the impulse strengths equal the product of the signal value and ts

<!-- image -->

<!-- image -->

## 2.14 (Solution)

- (a) The product of two periodic pulse trains will have zero area if the pulses do not overlap. If do overlap; however; the area will equal the the area of the product summed for period; which can equal only zero or %they each
- symmetry about 0.5T. If balf-wave symmetry is also present; So,
- (c) The reasoning is similar to part(b) .
- period) the same. stays

## 2.15 (Solution) Assume a pulse width of to and period T, and use Review Panel 2.2.

<!-- formula-not-decoded -->

- Irms = 2T
- A?to (c) Sawtooth: P = = = 3T Irms
- (d) Itiangular: P = = 4A?D = 3T A?to Irms

This means even we also see odd symmetry about

- 2.16 (Solution) Tbe signals are sketched for 0 &lt;t &lt;4. The signals of parts (a) and (d) are identical.
- 2.17 (Solution) Tbe signals are sketched below. We see that
- 0.5) 0.5u(t ~ 0.5)
- 2.5) - 2.5u(t \_ 2.5)
- (a) z(t) = u(t+1) - u(t - 1)
- (f) z(t) = u(t+1) - r(t + 1) +r(t)
- 2.18 (Solution) We provide the following examples. Integration is over all time.
- =1 but since
- (b) f |sinc? (t)ldt =1 but f Jsinc(t)|dt is not finite (the sinc function is not absolutely integrable).
- (c) f |sinc?(t)| =1 and sinc(t)dt =1 (both areas are finite)
- 2.19 (Solution) Tbe signal(t) covers the range -3 &lt;t &lt; 3. Its energy is 12 J. In the following; remember that only amplitude scaling or time scaling changes the energy.
- (b) 22(t) is only amplitude scaled and covers ~3 &lt;t &lt; 3. Its energy is E = (2)?(12) = 48 J.
- (c) z(t \_ 4) is delayed by 4 and covers 1 &lt;t &lt; 7. Its energy is E =12 J.
- (d) z(-t) is folded and still covers -3 &lt;t &lt; 3. Its energy is E =12 J
- find that t =-3 translates to tn = 3 and t = 3 translates to tn =-15. The signal thus covers

<!-- image -->

<!-- image -->

- 2.20 (Solution) only amplitude scaling changes the power and only time scaling changes the period.
- (d) z(-t) is folded; so T = 6 (no change) and P = 4 W (n0 change).
- Its period is T = 18 but its power is still P = 4 W (no change) .

## 2.21 (Solution)

<!-- formula-not-decoded -->

its integral (the last term) is zero and thus Ez = Ez

- 2.22 (Solution) following-
- (a) Tbe area of z(t) = e-2u(t) equals 1/2.
- (b)
- c) Ibe area of y(t) = 2e =-5
- (d) The energy of y(t) = 24e-3t + 36e-2t\_ 2+
- 2.23 (Solution)

<!-- image -->

Review Panel 2.2, the signal energy in one period is thus Using

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 2.24 (Solution)

- (a) Tbe sum of energy signals is an energy signal. Irue.
- (c) The algebraic sum of two power signals can be an energy signal or a power signal or identically zero! Irue. u(t 1) is an energy signal (a pulse) , u(t) + u(t \_ 1) is a power signal and u(t) u(t) is zero
- (d) Tbe product of two energy signals is zero or an energy signal. Ttue. Example: The energy of the product z(t) = [eu(~t)lle-tu(t)] is zero.
- (e) The product of a power and energy signal is an energy signal or identically zero. Ttue. Example: r(t) 2
- (f) Tbe product of two power signals is a power signal or identically zero. False:   Example: The product z(t) = u(t + 1)u(1 - t) equals the energy signal rect(t/2)
- 2.25 (Solution) Let z(t) be a periodic signal with power Pr and y(t) be its switched periodic version given by y(t) = 2(t)u(t to) as shown below

<!-- image -->

<!-- image -->

If we use the limiting relation for finding the power

and average both signals over two periods (2T) about to (i.e. over to -T &lt;t &lt; to + T) the area of 0.5Pz.

- (a) y(t) = u(t) Ibe signal power in z(t) = 1 is 1. So, the power in y(t) is 0.5.
- (b) y(t) = |sin(t)lu(-t) The signal power in z(t) = |sin(t)| is 0.5. Tbe signal power in y(t) is thus 0.25.
- obtain P = 0.5(0.5)(2)2 + 0.5(2)2 = 3.
- 0.5(22 + 12) = 2.5
- power in u(t) and equals P = 0.5.
- (f) y(t) = 2sin(rt)u(t) + 2sin(at) . Since the frequencies are identical, we must Split this into two find tbe power as P = 0.5[(0.5)(2)? + (0.5)(4)2) = 5

## 2.26 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (e) r(t) = e-(1-2t)u(1 2t): Fom part c (and compression), E = 0.25
- e-(~t-2)u(-t ~ 2) is the same as tbe energy in e-tu(t) (because folding and shifting do not change the energy).

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 2.27 (Solution)

- = u(t): Switched; power signal, P = 0.5 (because power in dc signal y(t) = 1 is 1)
- P = So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- t2 1. Not an energy signal (r2(t) decays as 1/t and not any faster) vi

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (h) 2(t) = cos(at)u(t): Switched power signal. P = 0.5(0.5) = 0.25.
- (i) z(t) = cos(nt)u(t) 4)Ju(t 4) Energy signal. Tbis corresponds to 2 periods (4 half-cycles) of a sine with T = 2 Each half-cycle has unit width and height= 41. S0 (Review Panel 2.2), E = 4(0.5)(1)2(1) = 2
- are commensurate\_ To see this consider

<!-- formula-not-decoded -->

~ T2)/TiTz are commensurate. Ti and T2 must be rational fractions in order for tbeir sum, difference or product to be rational fractions. So,

- 2.29 (Solution) In the following; 2(t) = is periodic with period T = 1/fo. ej2rfot
- (a) y(t) = 2(2t) +3æ(0.5t): The frequencies are f1 = 2f and f2 = 0.5f0y(t) is periodic with fundamental fequency = GCD(f1, f2) = 0.5f0 and period 2T
- (b) f(t) = + 3e-j7mt; So, f1 = 8 Hz f2 = 3.5 Hz and So,
- (c) Is the signal g(t) = 5e-7mt: Not periodic (the second term is a decaying exponential) . 4ej16nt
- 2e Tbe second term is a constant
- (d) Is the signal h(t) = 3ej16rt So, fundamental frequency = 8 Hz and period 0.125 s
- (e) Is the signal s(t) k=-0

periodic with fundamental frequency = fo and period T = 1/fo. So,

- 2.30 (Solution) See sketches below.
- (a) u[sin(rt)] To sketch; note tbat u[f(t)] is 0 if f(t) &lt; 0 and +1 if f(t) &gt; 0. The period is T = 2 Tbe signal power is P = 0.5.

<!-- image -->

- (b) sgn[sin(at)] The period is T =2 The signal power is P = 1.
- To find the impulse strengths; see Problem 2.47(6) This signal is periodic but not a power signal

## 2.31 (Solution)

- (a) 2(t) = sin(2nt) is a sinusoid with period T = 1. Its power is P = 0.5.
- (b) y(t) = is periodic with the same period as z(t). ex() S0,
- 1
- 2.32 (Solution) See the sketches below- The area of one period of each periodic extension equals the total area of z(t) = tri(t/2)

<!-- image -->

<!-- image -->

## 2.34 (Solution)

- (a) z(t) = cos(2nt) + cos(6nt) + cos(lOnt) Its components are at 1, 3 and 5 Hz. S0 fo =1 and Each component is half-wave symmnetric over one composite period, and s0 is z(t).
- This cannot be half-wave symmetric since its dc value is not zero.
- Its components are at 1, 2 and 3 Hz. S0 fo = 1 and T = 1. Since cos(4nt) is not half-wave symmetric over one composite period; neither is z(t).

## 2.35 (Solution) See the sketches below. At jumps, the derivative will include impulses-

<!-- image -->

- (a) z(t) = cos(0.Snt)
- (c) z(t) = tri(t). See tbe sketches.

## 2.36 (Solution)

- (a) I(t) = e-t/u(t). S0, E = e-2t/7
- 0 = 0.25+3 (from tables)
- (c) f(t) = sin(2t)u(t). So, E = [e-t sin(2t)}? dt = 0.2 (from tables)
- 2.37 (Solution) = found from 0.01A = Tbis gives t ~ 4.6T \_

This compares reasonably with the practical estimate of t = 5T .

## 2.38 (Solution)

- are found from 0.1 = 1 and 0.9 = 1 In(0.9) and t2 = In(0.1) tR = t2 = t1 ln(0.9) In(0.1) = 2.1972 So,
- Tbe time t1 to reach 109 and t2 to reach 90% = e-t2
- (b) y(t) = sin(0.5nt) 0 &lt;t &lt;1 Tbe fnal value of z(t) is 1 1 t21
- The time t1 to reach 109 and t2 to reach 909 are found from 0.1 = sin(0.S"t1) and 0.9 = sin(0.5nt2) . = 0.0638 = 0.6491
- x" (t) = cos(at)
- " (t) =-2 (plus impulses)

## 2.39 (Solution)

- (a) z(t) = (1 are found from 0.1=1 \_ and 0.9 = 1 ~ Tbus, t1 = In(0.9) and t2 = ~Tln(0.1) In(0.1)] = 2.1972T. This compares well with tR ~ 2.27 e-t1/+
- (b) For the compressed signal f(t) = z(3t), the time taken to reach 109 and 909 of the fnal value will be three times less and the time constant will be tR/3.

Similarly; the rise-time of tbe stretched signal g(t) = 2(t/3) will be 3tR'

In general, the rise-time of the signal h(t) = c(at) will be

## 2.40 (Solution)

- (a) z(t) = (1 e-')u(t). Tbe time to reach within 5% of the final value (of unity) is found from 0.95 = 1 ~ Thus, e-t = 0.05 and t = In(0.05) = 2.9957 e-t
- sin(0.5ut) 0 &lt;t &lt;1 (b) y(t) = Tbe time to reach within 5% of the final value (of unity) is t 2 1 0.7978

<!-- formula-not-decoded -->

- (b)

<!-- formula-not-decoded -->

- z(t) = e-otu(t) The area of z(t) is I/œ and the area of 22(t) is 0.5/œ. So, tables, using

<!-- formula-not-decoded -->

3. z(t) = te-atu(t). The area of r(t) is and tbe area of æ?(t) is 0.25/03. S0, tables , 1/02 using

<!-- formula-not-decoded -->

## 2.42 (Solution) Refer to the sketch.

<!-- image -->

- (a) z(t) = = 1 Also; z(1) = 1 So, So,

<!-- formula-not-decoded -->

- =0 or œ =In2 = 0.6931 ~2at S0,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 2.44 (Solution)

- (b) If the instantaneous frequency varies linearly from 0 to 100 Hz in two seconds, f (t) = 50t. =
- (d) If the frequency varies linearly from fo Hz to f1 Hz in to seconds; f;(t) = fo + f1\_fet.

<!-- formula-not-decoded -->

- to and z(t) = cos[ø(t)]
- 2.45 (Solution) =

10 Q =

## 2.46 (Solution)

- (a) z(t) = As œ 0, I(t) becomes more compressed and tall. Since z(t) is even c symmetric,
- (b) z(t) = 6 (from tables) . The Jimi ~c
- (c) 2(t) = Zsinc (4) As œ = 0, z(t) becomes more compressed and tall. Since z(t) is even sym0 metric, r(t) = 2

- As œ ~ 0, r(t) becomes more compressed and tall. We find I(t) = 1 (from 0 tables) . The limiting form of z(t) is thus 6(t)

## 2.47 (Solution) See the sketches below

<!-- image -->

- Tbe roots of f(t) = t2 \_ 3t+ 2 = 0 are tk = 1, 2
- (b) z(t) = The roots of f(t) = n = 0,4l, 42, With we find |f'(tk)| = = T, This describes an impulse train.

## COMPUTATION AND DESIGN

## 2.48 (Solution) Uses the ADSP routine enerpwr

'Problem 2.48 t=0:0.01:3; 'Tine array x=sin(2*pi*t); 'Signal x(t) y=exp(x) ; z=exp(j*x); 'z is complex valued f=cos(pitx); g=cos(pitx.*x) plot (t,x) ,grid,pause Plot (t,y) ,grid,pause plot (t,real(z)) ,grid,pause plot (t,f),grid,pause plot (t,g) ,grid,pause

'Finding the period

xM-max(x) ;i=find(abs(x-xm)&lt;lOO*eps)

'Period of

x is

1

ym=max(y) ;i-find(abs(y-yu)&lt;lOO*eps) ;ti=t(i);di=diff(ti);Ty-di(1)

'Period

of y is

1

fm-max(f) ;isfind(abs(f-fn)&lt;1OO*eps) ti=t(i);di-diff(ti) Tf-di(1) 'Period of f is 0 .5

gm-max(g) ;isfind(abs(g-gu)&lt;1OO*eps)

ti-t(i);di=diff(ti);Tg-di(1)

'Period of

is

0.5

'Finding Pover 'Power in 2 is 1 W 'For the rest use the ADSP routine enerpwr

```
'Define as a string variable Px-enerpwr(x, [0 , Ix] Tx) 'Pover in 0.5 'exp(sin(2*pi*t))';Py-enerpur(y , [O,Iy] ,Iy) 'Pover in y 2.2796 'Pover in f 0.6101 'Pover in g 0.6521
```

## 2.49 (Solution) Uses the ADSP routines ustep, uramp, enerpwr

```
'Problen 2.49 plot(t,x),grid 'Period is 2 plot(t,y) ,grid,pause 'Period is 2 plot(t,f) ,grid,pause 'Period is 2 (t,g) ,grid,pause 'Period is 2 plot(t,b) ,grid,pause 'Period is 2 'Use enerpwr to compute pover vith T-2 ustep(sin(pitt)) ;Px-enerpwr(x, [0 2] ,2) 'Pover is 0.5 'Pover is 1 'Pover is 2 8 uramp(sin(pi*t)) 'Pover is 0.25 b='exp(sin(pi*t)) Pb=enerpur (b, [0 2] ,2) 'Pover is 2.2796 ,pause plot X='
```

## 2.50 (Solution) Uses the ADSP routines tri, enerpur ustep,

```
'Problem 2.50 'PART (a) x2=x.#x;y=sin(pitt);y2=y.*y; ax=sum 'Repeat for axzsum (x) /N ax2=sun(x2) /N ,ay=sun(y) /N ,ay2=sum (y2) /N 'PART (c) 'Repeat for N=10
```

## 2.51 (Solution)

```
To tables, I = cos(2T6) . As To ~ 0, I + 4 'Problem 2.51 'PARI (a) x=lO*exp(-t).*sin(2+t); sxe=4-2*exp(-t) _ (sin(2*t)+2#cos(2#t)); (t,SX ,t,sxe) pause 'Repeat for ts=0.01 (x) ; sxe=4-2*exp(-t) . *(sin(2*t)+2*cos(2*t)) ; 'PARI (b) 'Repeat for ts=0.1 and pause ts=0.01 IO; (sin(2+t)+2*cos(2*t)); Using
```

```
plot(t,SX,t,sxe) 'Repeat for sxea4-2*exp(-t) _ plot (t,SX,t ,sxe) sin(2t)} 'Problen 2.52 xd-diff(x)/ts;Lslength(xd) 'umerical derivative xde=lO*exp(-t).*(2*cos(2*t)-sin(2*t)); 'exact derivative plot(t,xde,t(1:L) ,xd) Pause errzxde(1:L)-xd;plot (t(1:L) err) ,pause 'error 'Repeat for ts=0.05 ts=0.05;t=O;ts:3;x-1O*exp(-t).*sin(2*t); xd=diff (x)/ts;L-length(xd) ; Plot
```

```
xde-lOtexp(-t) (2+cos(2*t)-sin(2*t)); err-xde(1:L)-xd;plot(t(1:L) err)
```

## 2.53 (Solution)   Uses the ADSP routines ustep, uramp, operate

```
'Problem 2.53 t=-2:0.01:2; [tf ,f]-operate(t,*,-2,1) (tf ,f) ;plot
```

You could also use ctsiggui. The results are shown for (-2t+ 1)

<!-- image -->

## 2.54 (Solution) gcd1

to find tbeir rational epproximation.

```
'Problem 2.54 [nl ,dl]=rat(fl) ;[n2,d2]=rat (f2) [n3,d3]=rat(f3) 'Find rational approxinations [na, da] =gcdl ( [nl ,n2 ,n3] [d1,d2,d3]) ; fO-na/da 'f0=3/10=0.3 [nb ,db]=lcnl ( [d1 ,d2,d3] T-nb/db '1-10/3 =3.3333 2.55 (Solution) Uses the ADSP routines sinc, enerpwr 'Problen 2.55 b*sinc(2*t)' Exzenerpvr (x, [-0.5,0.5]) 'Ex=16.2508 11 .6077 2.56 (Solution) r(t) = 'Problem 2.56 'PART (a) sound (x) pause sound (x) ,pause 'PARI 'Ihe beat signal is periodic _ You can read the beat frequency from the plots = S0, f1(t) = = S0, the instantaneous frequency increases (linearly) with time. Tbe signal is not periodic. 'Problem 2.57 T;x-cos(pi*t.*t/6) ;plot(t,x) ,pause 1=6;t=O:ts:I;x=cos(pitt.*t/6);plot(t,x) pause (t,x) 2.58 (Solution) 'Problen 2.58 'PARTS (a-c) 2;x=exp(-Pi*t.*t/tO/tO)/tO;plot(t,x) ,Ax-sun(x)*ts pause pause Ax-sun(x)= pause X=' t/6 . ;plot *ts
```

Ax=sum(x) #ts,pause

'PART (d) The derivative approaches the doublet d' (t)

xd-diff (x)/ts;L-length(xd) ;plot(t(1:L),xd) ,Axd-sum(xd)#ts,pause xd=diff (x)/ts;L-length(xd) ;Plot(t(1:L) ,xd) ,Axd-sum(xd)#ts,pause

xd-diff (x)/ts;L-length(xd) ;plot(t(1:L) ,xd) Axd-sun(xd)#ts ,pause xd-diff(x)/ts;L-length(xd) ;plot(t(1:L),xd) ,Axd-sum(xd)*ts pause

xd-diff(x)/ts;L-length(xd) ;plot(t(1:L) ,xd) ,Axd-sum(xd)#ts

## DISCRETE SIGNALS

- 3.1 (Solution) See the following figure for sketches .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 3.2 (Solution)

<!-- formula-not-decoded -->

With z[n] 4, 2, 2}, we find

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 0,8} (fold y[n])

Tbe energy in each signal is E =36 + 16 +4+4= 60

- 3.3 (Solution) Note that z[n] = 4, 2, 1} Tben
- (c) g[n] 1, 2, 4, 8, 16} (shift left by 4, then fold)
- 3.4 (Solution) Find and sketch each of the following signals and compare their signal energy with tbe energy in z[n]
- (c) step-interpolated g[n] =
- assuming next sample is zero)
- 3.5 (Solution) See the following figures (not to scale). and the odd part as z [n] = 0.5([n]

<!-- image -->

<!-- formula-not-decoded -->

<!-- image -->

<!-- image -->

- 3.6 (Solution) See the following figure for sketches. We note that
- 6] is easily sketched as a sum of steps and ramps.
- = ~3 to n = 3
- (c) z[n] = rect(252) is a 5-sample rectangular pulse centered at n = 2
- (d) z[n] = 6tri( "54) is a 7-sample triangular pulse centered at n = 4 (with values of zero). end
- (a) Signals as a numeric sequence:
- (Signal 1:) [n] = {2,2,2,2,1,1,1,1,1,1,1,1}
- (Signal 2:)
- (Signal 3:) {9,1,2,3,4,5}

Figure P3.7. Signals for Problem 3.7.

<!-- image -->

- (Signal 4:) z[n] = {8,5,4,3,2,2, 2,2,2}
- (b) Signal representation by impulses
- (Signal 1:)
- (Signal 3:)
- (Signal 2:)
- (Signal 4:)
- c) Signal representation by steps and ramps:
- (Signal 1:)
- (Signal 3:)

<!-- formula-not-decoded -->

- (Signal 4:)
- (d) and (e) Signal energy and signal power (if periodic)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 3.8 (Solution)

- (a) r[n] = cos(0.5nr). So, F = 0.25=4, 80 periodic witb N = 4.
- S0, N1 = 8, Nz = 12. So, periodic with N = LCM(8,12) = 24

=

- So, periodic with N = LCM(24,9) ='72 S0,
- Not periodic because F2 = &amp; is not rational.
- (h) z[n] = +0.5 cos(6 S0, Fi = periodic with N = 12.
- (i) zn] = periodic with N = 20. So,
- (j) z(n] = = 2ejo.3nr
- (k) z[n] = F = Not periodic because F is not rational. ej0.3n So,
- F = So, periodic with N = 8. So,

## 3.9 (Solution)

- (a) z[n] = F =4/6 = 2/3. z[n] = cos(-2nn/3) = cos(2n7/3)So, So, So,
- z[n] = [Note: Tbis can be simplified to z[n] = So,

## 3.10 (Solution)

- (a) z(t) = cos(320nt + 0.257) fo = 160 5 = 100 Hz, and F = fo/S = 1.6. There is aliasing because F &gt; 0.5 (or S &lt; 2fo) . So, Hz,

Now, F = 1.6 = -0.4,s0 z[n] =

- (b) z(t) = 0.257) . fo = 70 and F = fo/S = 0.7 So, Hz, Hz,

Now, F = 0.7 = ~0.3, s0 z[n] =

= 0.3 There is no aliasing because F &lt;0.5 (or S &gt; 2fo) =

- 3.11 (Solution) The product of a right-sided and a left-sided discrete-time signal is always time-limited OI identically zero\_

Example 2: u[n + 2] and u[\_n]: Their product is {

## 3.12 (Solution) Refer to the sketch.

<!-- image -->

Figure P3.12. Signals for Problem 3.12

- Also z[0] = 4 = A Also; z[2] = 1 = 402 = 0.5.

<!-- formula-not-decoded -->

## 3.13 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) z[n] = cos(nr). Periodic, F = 0.5 and N = 2. s[n] = {1, -1} for one period.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (f) z[n] = 1]  Neitber a power signal por an energy signal (because r?[n] does not decay faster than 1/n and does not converge)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- Neitber power nor energy (growing complex exponential) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 3.14 (Solution) Refer to the sketch.

<!-- image -->

- (a) z[n] = 2 y[n k=-0 one period.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 3.15 (Solution) All represent the same signal because

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 3.16 (Solution)

- (a) Q = 0.5 (0.5)"u[n] = {1,0.5,0.25,0.125, ~

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) (~0.5)"u[n} = {1,~0.5,0.25,-0.125, This is a decaying exponential. Q = 1 (~1)"u[n] = 0 =2 (~2)"u[n] = {1, -2,4, -8,..} This is a growing exponential step.
- (0.5e8)" = (0.5)"ein0 . Tbis is an exponentially damped sinusoid. Q = = This is a sinusoid. = (2)"ejne . This is an exponentially growing sinusoid. ejno 2eje
- (d) 0 = Damped sinusoid with samples alternating in sign. Q = (eje)n = (~1)"eine . Sinusoid with samples alternating in sign. Q = = (~2)"ein8 . Growing sinusoid with samples alternating in sign. ~0.5ej0 ~Zeje

<!-- formula-not-decoded -->

- (a) z[n/3] = {0,0,0,1,0,0,2,0,0,3,0,0,4,0,0,3,0,0,2,0,0,1,0,0,0,0,0} (zero interpolation) 2,0,0,*,0,0,2,0,0,0,0} (decimation)
- (b) z[n/3] = {0,0,0,1, 1,1,2,2,2,3,3,3,4,4,4,3,3,3,2,2,2,1,1,1,0,0,0} (step interpolation)
- (c) z[2n] = {0,2,4,2,0} (decimation) = {0,0,0,2,0,0,4,0,0,2,0,0,0,0,0} (zero interpolation)
- (d) z[2n} = {0,2,4,2,0} (decimation)

## 3.18 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) z[n] Restriction: M and N must be integers.

## 3.19 (Solution) Refer to the sketcbes.

- z = IN

<!-- image -->

N =5: Angular spacing =

N = 6:

- =-1 = ejr ei(2k+1)æ 2 = N = 5: Angular spacing = =3 = N = 6: Angular spacing = 2 = 2
- (b)

## 3.20 (Solution)

- 3 3 &lt; F &lt; 4. So,
- = [n] = cos(n) or z[n] = cos[2nr(3 + So,
- 3.21 (Solution) =
- (a) Aliasing has occurred.  fo = 160 Hz. So, Fo =
- (b) 8 full periods of z(t) generate one period (5 samples) of z[n].
- (c) The digital frequency in tbe principal range is Fo = 1.6= Fo = -0.4. The analog frequency of tbe recovered signal Ir(t) is fa = SF = 200(-0.4) = -80 Hz
- =
- 4) Ir(t)

<!-- formula-not-decoded -->

## 3.22 (Solution)

- (a) z(t) = sin(15800nt+0.257) and 5 = 8000 Hz. fo = 7900 Hz and Fo = = S0, z[n] = sin(-2 4 0.257) = sin( 2 0.257) So,
- (b) If SR = 4 kHz, the reconstructed frequency is FoSR = = 50 Hz (i.e., 50 Hz)
- (c) If SR = 8 kHz, the reconstructed frequency is FoSR = =
- (d) If SR = 20 kHz, the reconstructed frequency is FoSR = 29990 =
- This varies linearly with t.
- (a) If the frequency varies from 0 to 2 Hz in 10 seconds, " = = cos(\_
- (b) s[n + N) = + N2)]

=m and = 2k (where N m and k are integers that make tbe last two terms integer multiples of 2r) Tbe smallest N that satisfies these results is N = 80. So, z[n] is periodic with period N = 80.

- periodic with period N = 32.
- 3 &lt; F &lt; 4

## 3.24 (Solution)

- (a) z{n] = (0.5)"u[n] z[0] =1 The 60-dB time constant is found from (0.5)" = 0.001 and gives n Jog(0.5) = log(0.001) or n = 9.9658 ~ 10. The 40-dB time constant is found from (0.5)" = 0.01 and gives n log(0.5) = log(0.01) or n = 6.6439 ~ 7.
- (b)

## 3.25 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- Refer to the sketches for the periodic extensions.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (e) For N = 3, we have
- its periodic extension with period N is So,

<!-- formula-not-decoded -->

sn] Tbus, y[n] = 1

<!-- formula-not-decoded -->

(0.5)" For a = 0.5 and N = 3, y[n] = Its signal power is 1 ~ (0.5)5

<!-- formula-not-decoded -->

- 3.28 (Solution)

<!-- formula-not-decoded -->

- (b) The norm Ilzll1 signifes the absolute area.

Tbe norm Ilzll2 is similar to the rms value (and related to the signal power)

The norm

## COMPUTATION AND DESIGN

- 3.29 (Solution) Uses the ADSP routines ustep, uramp, urect, udelta, tri, operate, dtplot

'PROBLEM 3.29

'PART (a)

n=-10:10

y]=operate(n,X,~1 ,-4)

';x=ustep(n+4)-ustep(n-4)+2*udelta(nt6)-udelta(n-3) ;ax=[-15 15

subplot (2,1,2) ,dtplot (ny,Y ,'0') ,axis(ax) ,pause

0' ) , axis(ax)

0 3] ;

## 'PART (b)

x=uramp(nt6)~uramp(n+3)~uranp (n-3)+uramp(n-6) ;ax-[-15 15 0 4] ;

## 'PART (c)

0 2] ; [ny ,y]=operate(n,*,1,4) ;subplot (2,1,1) ,dtplot '0') ,axis(ax) \_ subplot (2,1,2) ,dtplot '0') ,axis(ax) ,pause

## 'PARI (d)

X=B*tri(n/6)-3*tri(n/3) ;ax-[-15 15 0 4]; [ny,y] =operate(n,I,-1,4) ;subplot(2,1,1) ,dtplot(n,I,'0') ,axis(ar) = subplot (2,1,2) ,dtplot ,Y,'0') ,axis(ax) (ny

You could also use the routine dtsiggui. Tbe plot shown is for part (d)

<!-- image -->

## 3.30 (Solution) Uses the ADSP routines dtplot interpol

```
'PROBLEM 3.30 hz-interpol (h, 'Step interp hz=interpol(h,'1' ,3) ;dtplot(O:L,hz,'0') 'Linear interp
```

## 3.31 (Solution) Uses the ADSP routíne dtplot

```
'IPROBLEM 3.31 n=0:40;a=1.2;x=a_ n;subplot (3,1,1) ,dtplot (n,X,'0') 'PART (b) a=-1.2;x=a 'subplot(3,1,1) ,dtplot(n,x,'05 a=-0.8;x=a. subplot (3,1,3) ,dtplot (n,X,'0') ,pause 'PART (c) a=1.2*exp(j*pi/4) ;x=asubplot (3,2,1) ,dtplot (n,real (x) ,' . ') ,subplot (3,2,2) ,dtplot (n,imag(x) , 2=1 O*exp(j*pi/4) ;x-a_ subplot (3,2,3) ,dtplot (n,real (x) ) ,subplot (3,2,4) ,dtplot (n,imag(x) ') ~n; subplot (3,2,5) ,dtplot (n ,real (x) ') ,subplot (3,2,6) ,dtplot (n imag(x) ') ,pause 'PARI (d) n; subplot (3,2,3) ,dtplot (n,abs(x) ) , subplot (3,2,4) ,dtplot (n,angle(x) , a-0.B*exp(j*pi/4) x=a subplot (3,2,5) ,dtplot(n,abs (x) ) ,subplot (3,2,6) ,dtplot (n,angle(x) ~; ~n; ~n; ~1;
```

## 3.32 (Solution) Uses the ADSP routine dtplot

```
'PROBLEM 3.32 2=-10:30; xls2+cos(n*pi/2)+S*sin(n*pi/5) subplot (2,2,1) ,dtplot (n,xl , 'Period N=20 x2-2+cos (ntpi/2) .#sin(ntpi/3) ;subplot(2,2,2) ,dtplot (n,x2, 'Not periodic subplot (2,2,4) ,dtplot (n,x4 , 'Zero (Note tbe y-scale)
```

```
3.33 (Solution) 909, 2vL 45" , 'PROBLEM 3.33 Uses the ADSP routine dtplot 2=-30:30;x=exp(-j*0.3+n*pi);axis([-30 30 ~1 1]) subplot (2,2,1) ,dtplot (n,real (x) ) ,axis( [-30 30 ~1 1]) , subplot (2,2,2) ,dtplot (n,inag(x)) ,axis( [-30 30 ~1 1]) subplot (2,2,3) ,dtplot (n,abs(x)) ,axis([~30 30 0 1]) 'Al1 (except magnitude) determined N-20 Imaginary part: z; = 5vsin( % Magnitude: Im = 5v2, Ir = Ii = 'PROBLEM 3.34 Uses the ADSP routine dtplot 1=-20: 'PART (a) subplot(2,2,1) ,dtplot(n,real (x) ,'0' ) subplot (2,2,2) ,dtplot(n,inag(r) ,0') (b) subplot (2,2,3) ,dtplot (n,abs(x) ,'0') subplot (2,2,4) ,dtplot (n,angle(x) ,'0' ) ,pause 'PART (c) subplot (2,1,2) ,dtplot(n,real (x)-inag(x) ,0' 'All plots (except magnitude) allov the period to be determined. N=18 = 2cos(nn/4). 'PROBLEX 3.34 Uses tbe ADSP routine dtplot 'PART (a) subplot(2,2,1) ,dtplot (n,real (x) '0') subplot (2,2,2) ,dtplot (0, (x) ,'0') subplot (2,2,3) ,dtplot (n,abs(x) ,'0') subplot(2,2,4) ,dtplot (n,angle(x) ,'0') 'Ibe real part and angle allov tbe period to be deternined. N=5 Pi]) ~Pi e-jna/4 imag
```

```
timefreq(x) ; 'Frequency increases decreases (aliasing) 3.37 (Solution) Uses tbe ADSP routine dtplot For periodicity; z n] = T(2nN + N2) So =2kr or 2nN + 12k. This is satisfed for N = 6. 6 'PROBLEM 3.37 n=0:20;x=cos(pitn.*n/6) ;dtplot(n,x,'0') 'Period J=6 3.38 (Solution) Uses the ADSP routine randist 'PROBLEM 3.38 % Time array ax= [0 0.01 1.5] ; % Plot for 0.01 for all signals Pure sinusoid 'PART (b) xn-randist(x, ,0) ; uniform noise (mean-0) snr=10; % Desired SNR A=std(x)/std (xn)/(10- (snr/20)) ; % Compute 4 % Generate noisy signal subplot (3 ,1 ,1) ,plot (t,x) ,axis(ax) subplot (3,1,2) plot(t,y) ,axis(ax) subplot (3,1,3) plot (t,z) axis(ax) ,pause SNR=10*log1o (sum(x.*x) /sum(y.*y)) % Compute actual SWR 'PARI (c) z=O;for n=1:64; % Initialize and start loop z=ztxty; % Sum a16-2/16; end Save average of 16 runs end % End of summing 64-runs a64=z/64; % Average of 64 runs subplot (3,1,1) ,plot (t,zn) axis(ax) ' Plot noisy signal subplot (3,1,2) ,plot (t,al6) ,axis (ax) % and 16-run average subplot (3,1,3) (t,a64) axis(ax) ,pause % and 64-run (not any better) N? 'Plot
```

```
Fon + 2N 'PROBLEM 3.36 Uses the ADSP routine tinefreq timefreq(x) ;pause 'Frequency increases linearly from F=0 to F=0.5 FO-0;F1=1; up to F=0.5, then
```

```
'PART (d) % Initialize 2 and Start loop ,0) % Keep summing eacb run if 1==16, a16-2/16; end % Save average of 16 runs end End of sunming 64-runs a64=z/64; % Average of 64 runs subplot (3,1,1) ,plot(t,zn) ,axis(ax) % Plot noisy signal subplot (3,1,2) ,plot(t,al6) ,axis(ax) % and 16-run average subplot (3,1,3) (t,a64) ,axis(ax) ,pause % and 64-run (much better) 'PARI (e) m=randist(x,'nor ,0) ; % Gaussian noise (meanro) SDI=10; A=std(x) /std(mn) / (10-(snr/20)) ; " Compute A y=Atxn; % Compute actual SNR z=O;for n=1:64; % Initialize 2 and start loop nor ,0) % Keep summing each run if n==16 a16-2/16; end % Save average of 16 end % End of summing 64-runs a64=2/64; % Average of 64 runs subplot(3,1,1) ,Plot(t,z2) axis(ax) % Plot noisy signal subplot (3,1,2) ,plot (t,a16) axis(ax) and 16-run average subplot (3,1,3) ,plot (t,a64) axis(ax) % and 64-run (much better)
```

## Uses the ADSP routine randist

```
'PROBLEM 3.39 uni O) ;for k=1:2,S-S+randist (500, ,0) end 'For N-2 , should idealy be triangular (convolution of uniforn distributions) subplot (2,2,1) ,hist(x,20) subplot (2,2,2) ,hist (S,20) ,pause S-O;for k=1:6,S-Strandist (500, uni' ,0) ;end subplot (2,2,1) hist (x,20) subplot (2,2,2) ,hist (S,20) uni 0) ; end Pause 'PART (b) S-O;for k=l:6,S-S+randist(500,'exp' ) ;end % Exponential distribution subplot (2,2,1) ,hist (x,20) S-O;for k=l:12,S-S+randist (500 exp' ) ;end uni
```

## 3.40 (Solution)

```
'PROBLEM 3 .40 f0-340; d=fO;
```

```
(2-(5/12)) ; bf=fO*(2-(8/12)) ; ts=1/8192; 'Sampling interval t=O:ts:0.4; 'time for each note s1=0*(O:ts:0.1); 'silent period 'shorter silent period tl-O:ts:l; 'time for last note of asc and desc scale asc=-[d1 51 f1 s1 g1 51 bf1 s1 52 dll]; 'Create asc scale dsc-[cl 51 bf1 51 f1 51 d12] ; %Create desc scale y=[asc s1 dsc s1] ; 'Malkauns scale sound(y) gfO*
```

```
'FRDM Prob 3.40 (2-(5/12)) ;bf=f0*(2-(8/12)) ; asc=[d1 51 f1 s1 g1 51 bf1 51 52 dl1] ; dsc-[cl 51 bf1 51 g1 s1 f1 nov let each note decay by adding an exponential decay asc=[dl.*ex s1 fl.*ex s1 bf1.*ex s1 c1.*ex s2 dsc=[c1 *ex s1 bf1. s1 *ex s1 f1.*ex 51 d12.*exl] ; ybd=[asc s1 dsc s1]; ;g=fO* g1 .*ex g1 .= *ex
```

```
bb= [f1 s1 d1 51 el s1 a2 s1 s1 a1 s1 el 51 f1 s1 d2] ; 'Big Ben Notes
```

```
f-f0*(2(3/12)) ; 3.41 (Solution) 'PROBLEM 3 .41 sound (yhd) 3.42 (Solution) 'PROBLEK 3 .42 al=sin(2*pi*a*tl);a2-sin(2*pitatt2); sound (bb)
```

```
'Tben add decaj for string-like sound bb2=[f1.*exl 51, d1 .#exl , 51, el.*exl, 51, a2.*ex2] ; bb2= [bb2 , s1, s1, 51 , 51 , 51 , al.*exl , s1, el.*exl s1, f1.*exl] ; bb2=[bb2 , s1, d2.*ex2] ;sound(bb2) 3.43 (Solution) 'PROBLEM 3 .43 f0=440; a-fO; g2-sin(2*pi*gg*t2) ; P=[al s1 g1 s1 cl s1 d2 s1 g2 s1 el s1 d2 s1 82 s1 el s1]; p=[p c1 51 d1 s1 al s1 g1 s1]; 'First bar of Pictures sound (p) 'Add decay for string-like sound exl=exp(-4*tl) ;ex2-exp(-3*t2) ; Pd=[al.*exl 81.*ex1 51 51 d2.*ex2 s1 82.*ex2 51 e1.*exl 51 d2.*ex2] Pd=[pd 51 *ex2 51 el.*exl 51 cl.*exl s1 dl.*exl s1 al.*exl s1 s1] ; sound (pd) 3.44 (Solution) (a) 'PROBLEM 3 _ 44 'PARI {a) '1=[697 ,1209] 2=[697 ,1336] 3=[697 ,1477] 4=[770,1209] 5=[770,1336] '6-[770,1477] 7=[852,1209] 8=[852,1336] 9=[852,1477] 0=[941,1336] 'Generate 1000 samples each z=zeros(1,1000) ; %50 zeros is too short! ! eigbt-[sin(n*ul3)+sin(n*vh2) ,2] ; pb=[four_ eight,seven ,five,five,oh] ;sound(pb) gg fO* 82 . 81 . tuo
```

- (b) Here is one of the many possible solutions .

```
function [sigtt,snd]zdialtt(n,S) Sound of tones in a at sanpling freq $ 'S-sampl (Defaults to 8192 Hz) 'n=vector artay of digits in the pbone number Use 10 for and 12 # on the dial % Use sound(sigtt) to listen to the tones 'See getnum _ (in Chapter 18) to decode the signal low-[697 770 852 941] ; hi-[1209 1336 1477] ; D=(:); 'make column 0 to 11 'silent passage N=O:M-1; 1=length(n) ; sigtt=[] snd=[] ;for k=1:1 n(k) tone-[lov(il) bi(ib)]; snd=[snd ;tone] sigtt-[sigtt cos if kkl,sigtt-[sigtt, 2] ;end %add zeros to all except last digit end ing freq end
```

## 4.1 (Solution)

- (a) O[] = 4[] = = 4b[z2]
- (b) O[] = 4]+3

<!-- formula-not-decoded -->

- aOfz1] =0 sin(z), bO[z2] = bsin(z2)
- (e) y(t) = z(4t)
- = 4dzldt + = 312 311,

## 4.2 (Solution)

## ANALOG SYSTEMS

- LTI, dynamic, causal
- (b) y"(t) + 3y(t)y(t) = 2z(t) + z(t) Nonlinear, time-invariant, dynamic, causal.

- (c) %'(t) + 3tz(t)y(t) = 2z(t)
- Nonlinear , time-invariant,dynamic, noncausal.

Nonlinear , timeinvariant,instantaneous(static) , causal.

- (f) y(t) = 22(t +1) + 5 Nonlinear, time-invariant,dynamic; noncausal.
- Nonlinear; time-varying,dynamic, causal
- (b) y(t) =22(t) + 22(t + 1) Nonlinear , time-invariant,dynamic, noncausal.
- (i) y"(t) + cos(2t)y(t) = 2(t + 1) Linear, time-varying;dynamic, noncausal.
- = 2z(t) Linear, time-varying dynamic, causal.
- Nonlinear, time-invariant,dynamic, causal
- (1) y"(t) +tJ+ y(t)d = 2(t) +2
- Nonlinear, time-varying dynamic; causal.
- 4.3 (Solution) All are causal, instantaneous (static) and time-varying-
- (a) y(t) =
- (b) y(t) = [A+ z(t)] cos(2n fot) is nonlinear-
- (c) y(t) = cos[2nfotz(t)] is nonlinear .
- (d) y(t) = cos[2afot + z(t)] is nonlinear.
- (e) y(t) =comb(t ts)z(t) is linear.

## 4.4 (Solution)

- (a) %(t) + 2y(t) = u(t). So,
- yF(t) + 2yF(t) = (B + 2A) cos(t) + (2B A) sin(t) cos(t). Compare coefficients of sine and cosine to give B + 2A = 1
- (c) y(t) + 2y(t) = e-tu(t). yF = Ce-t. With yF(t) = ~Ce-t we yF(t) + 2yF(t) = ~Ce-t + 2Ce-t = So, get e~t

<!-- formula-not-decoded -->

- (d) y(t) + 2y(t) = e-2tu(t) = Cte-2t (tbe natural response already has the form e With yF(t) = Ce-2 2Cte-2 ~2t)~ get we
- yF(t) + 2yF(t) = B+2A +2Bt = t. Compare coefficients of powers of t (and constant terms): B+2A= 0
- yF(t) + 2yF(t) = ~2Ct2e~2t + 2Cte-2t + 2Ct?e-2t =te-2t 2C = 1 or C = 0.5 So,

## 4.5 (Solution)

- = So,

- (c) y"(t) + 5y'(t) + 6y(t) = 5 cos(t)u(t) With yF = ~Asin(t) + Bcos(t) and y} = ~Acos(t) Bsin(t) , we find Comparing coefficients of the cosine and sine terms, we 5A+ 5B = 5 5A+5B = 0. Solve to give A = B = 0.5. get
- Upon substitution; y(t) + 5y(t) + 6y(t) = Ce-2 = 2e-2
- = 0. Thus Solve to A = get
- (f) y"(t) + 5y(t) + 6y(t) = (6e-: + 2e-2)u(t). Use superposition of parts (b) and (d) to give

## 4.6 (Solution)

- (a) y(t) + 5y(t) = 2u(t). So, yF = C. Tbus 0 + 5C = 2 and C = 0.4.
- (b) %(t) + y(t) = cos(t)u(t) YF = Y(t) + y(t) = (A+ B)cos(t) + (B \_ A) sin(t) = cos(t) B - A = 0 and A = B = 0.5. So,
- (c) y(t) + 3y(t) = sin(t)u(t). So, yF = Acos(t) + Bsin(t) and yF = ~Asin(t) cos(t) Y(t) + 3y(t) = (3A+ B) cos(t) + (3B \_ A) sin(t) A = B = 0.3 4B ~0.1,
- (d) y(t) + 4y(t) = cos(t) + sin(2t) Use superposition: Y(t) + 4y(t) = (4A+ B) cos(t) + (4B A) sin(t) = For sin(2t): yF = Acos(2t) + B sin(2t) and yF = ~2Asin(2t) + 2B cos(2t) y(t) + 4y(t) = (4A+ 2B) cos(2t) + (4B 2A) sin(2t) = sin(2t) . This gives A =-0.1, B =0.2. Tbus, YF = 0.1cos(2t) + 0.2sin(2t)
- (e) y(t) + 5y(t) + 6y(t) = cos(3t)u(t) So, YF = Acos(3t) + Bsin(3t) and yF 2 ~3Asin(3t) + 3B cos(3t) and yF = ~9Asin(3t) ~ 9B cos(3t) = (~3A + 15B) cos(3t) + (3B + 15A) sin(3t) = cos(3t) . This gives A = 5 7

- y'(t) + 4y(t) + 4y(t) = cos(2t)u(t) S0, YF = Acos(2t) + Bsin(2t) and yF = ~2Asin(2t) + 2B cos(2t) and y} ~4Asin(2t) 4B cos(2t) y" (t) + 4y (t) + 4y(t) = 8B cos(2t) ~ 8Asin(2t) = cos(2t).

## 4.7 (Solution)

- 0 + 2C = 1 and C = 0.5. Ke-2t. So, y(t) = UN + yF +0.5. So, =Ke-2
- (b) %(t) + y(t) = cos(t)u(t) YF = With y(0) = 0 (zero state) K + 0.5 =0 and K = -0.5.
- (c) y(t) + y(t) = r(t) So, yF =
- YN = With y(0) = 0 (zero state) , K +0.5 =0 and K = ~0.5 e-t
- (from 4.4d). YN = With y(0) = 0 (zero state) K + 0 = 0 and K = 0. te~2t te-2t ,
- (f) y(t) + 2y(t) = cos(t)u(t). YF = e-2[Acos(t) + Bsín(t)]: Then, YF = y(t) + 2y(t) = Be-2t cos(t) YN = So, y(t) = yN + yF = Ke-2 sin(t) With y(0) = 0 (zero state) K + 0 = 0 and K = 0\_ e-2t Sò, Ke-2t . +e-2t

## 4.8 (Solution)

- (a) y"(t) + 5y(t) + 6y(t) = 6u(t). So, yF = C and 0 + 0 + 6C = 6 or C = 1. YN =

<!-- formula-not-decoded -->

- (b) %(t) + 4y(t) + 3y(t) = 2e-2u(t). So, yF = Substituting, yf(t) + 4yr(t) + 3yF(t) = ~Ce-2 = 2e-2 C =.-2. YN = Kie-t + Kpe-3. 2e -2t With y(0) = 0 = y (0): we find Solve to give K1 = 1, Kz = 1 Ce-2t . So, So,

<!-- formula-not-decoded -->

- (d) y' (t) + 4y(t) + 5y(t) = cos(t)u(t) So; yF = Acos(t) + Bsin(t). Substituting, y"(t)+4y(t)+5y(t) = (4A+4B)cos(t) + (4B-4A) sin(t) = cos(t). So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- = With y(0) = 0 =y(0), we find So,

- (f) y"(t) + 5y'(t) + 4y(t) = (2e-t +

Input 2e -t: =Cite-2t . Substitute to find C1 =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 4.9 (Solution)

- (a) y(t) + 5y(t) = u(t) y(0) =2. First find yF = C =0.2 and yN = Ke-5t .

For total response: y(t) = 0.2 + Ke-5t, y(0) = 2. Tbis gives K = 1.8.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- = = Ke-4t
- (c) y(t) + 4y(t) = 8tu(t) y(0) 2. First find yF = A+ Bt = -0.5+ 2t and yN
- For total response: y(t) =~0.5 + 2t + Ke-4, y(0) This gives K = 2.5. For ZIR: yzi(t) = YN = Ke-4t , y(0) =2. For ZSR: yzs(t) = ~0.5 +2t + Ke-4t , y(0) = 0.

- (d) y(t) + 2y(t) = 2 cos(2t)u(t) y(0) =4 First find yF 2 Acos(2t) + Bsin(2t) = 0.5 cos(2t) + 0.5sin(2t) and yN = Ke-2t .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (e) y(t) + 2y(t) = 2e y(0) = 6. First find yF = Cte-2t 2te-2t and yN = Ke-2t . ~2tu(t)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (f) y(t) + 2y(t) = cos(t)u(t) y(o) = 8. First find yF = '[Acos(2t) + Bsin(2t)] 2e 2t cos(2t) and yN = Ke-2 .

For total response: y(t) = cos(2t) + Ke-2, y(0) = 8. This gives K = 6. 2e~2t

<!-- formula-not-decoded -->

## 4.10 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

12e-2t

- 2(t) = 4e-2u(t), y(0) = 0

ZIR is 0 because initial conditions are zero.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Total response: y(t) = Yzs(t)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Find total response: y(t) = yzi(t) + %zs(t) = -1 +3e-4t

<!-- formula-not-decoded -->

Find total response: y(t) = Yzs(t)

ZIR is yzi(t) = 0 (because initial conditions are zero)

2e-2t .

4e-2)u(t)~ e-2(t-1)Ju(t 1)

Find ZSR as y1(t) = 2e-' + Ke-2t, y1(0) = 0 or y1(t) = 2e-t \_

Find total response: y(t) = Yzs(t)

- = y(0) = 4 Find ZIR as yzi(t) Ke-2t
- 2e-tu(t) y(0) = 4 or yzi(t) = Find ZSR as y1(t) = 2e-t + y1(0) = 0 or y1(t) = 2e-t \_ Ke-2t 2e~2t

Use linearity and time-invariance: yzs(t) =y{(t)-2yí(t-1)+y1(t- 2) and y(t) = yzs(t) + yzi(t) Tbis may be simplifed if desired.

## 4.11 (Solution) In all cases, a5 a check, y(t) = YN 4 yF

<!-- formula-not-decoded -->

- (b) y" (t) + 5y(t) + 6y(t) = 2e-tu(t) y(0) = 0 y(0) = 1 Ch. Eq: s2 + 5s + 6 = 0 YN = K1e-3t + Kze-2 Forced Response: yF = Ce-t YF = ~Ce-t

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

=e-t

Zero-State: y2s = y(t)

+ K1e-3 + Kze-2t with zero IC.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

=

K1 = 0.5,K2

~0.5

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- y(0) = 0 y'(0) = 1

<!-- formula-not-decoded -->

Forced Response: yF = Ct?e-2t (because of root repeated twice)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

So, y(0)

y(t)

=

0 = K

=

So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

K2 = 1

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (e) y'(t) + 4y(t) + 4y(t) = 8cos(2t)u(t) y(0) = 0 y(0) = 1

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

YF = sin(2t) Now ,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Forced Response: yF = Cte-2 (because of repeated root)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 4.12 (System Response)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 4e-2u(t), y(0) = 0, y' (0) = 0 Start with y"(t) + 4y(t) + 3y(t) = 2(t) = 54e-3 . Find total response: y(t) = yzs(t) 48e~2t

- z(t) = 4u(t) , y(0) = 6, Now, start with y"(t) + 4y'(t) + 4y(t) = z(t) =4. Find yF(t) = 1 Find ZSR as y1(t) = 1 + (K1 4 Find total response: y(t) = %zi(t) + yzs(t) = -1 + + e~2t 6te~2t 7e-2t
- = 4u(t) , y(0) = 0, ZIR is yzi(t) = 0 (because initial conditions are zero)
- (e) y'(t) + 5y(t) + 6y(t) = 2(t) 2z(t = 1) z(t) = y(0) = 0 ZIR is yzi(t) = 0 (because initial conditions are zero) Start with y"(t) + 5y(t) + 6y(t) = z(t) = 2e-t. Find yF(t) = Ce-t = e-t. +e-3t =e-t
- r(t) = 3e-tu(t) y(0) = 4, y' (0) = -4 Find ZIR a yzi(t) = K1e-t Find ZSR as y1(t) =

## 4.13 (Solution)

(a) y(t) + 3y(t) = z(t)

For impulse response, solve h' (t) + 3h(t) = 0, h(0) = 1.

<!-- formula-not-decoded -->

- Solve ho(t) + 4ho(t) = 0, ho(0) = 1 to ho(t) = e-4u(t). by linearity; h(t) = 2ho(t) = 2e-4tu(t) get Then,

- 2z(t) Start with single-input system y(t) + 2y(t) = (t). Solve hó(t) + 2ho(t) = 0, ho(0) = 1 to get ho(t) = e-2u(t).

- Solve hó(t) + ho(t) = 0, ho(0) = 1 to get ho(t) = e-tu(t) Then,

## 4.14 (Solution)

<!-- formula-not-decoded -->

- OI ho(t) = te-2tu(t). Then; by linearity; h(t) = 2ho(t) = 2te-2u(t).

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- ho(t) = te-tu(t)
- 4.15 (Solution) Remember, for stability every root must have a negative real part and the degree of tbe highest derivative of y(t) must exceed the degree of the highest derivative of z(t)
- Stable (root is s = ~4)
- Unstable (root is s = 4)
- (c) y(t) + 4y(t) = 2(t) + 32(t) Unstable (degree of y' (t) equals (does not exceed) that of z (t))
- (d) y"(t) + 5y(t) + 4y(t) = 6z(t)
- Stable (two equal roots $ = ~2)
- Stable (roots at s = -3, $ = -2)

- Unstable (roots at $ = 1, $ = -3)

## 4.16 (Solution)

- (a) Refer to the circuit below.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Assuming a relaxed circuit, y(0) = 0 = 4+K K = =

<!-- formula-not-decoded -->

- (b)

<!-- image -->

<!-- formula-not-decoded -->

- 4.17 (Solution) Refer to the following sketches.

<!-- image -->

- h(t) = /(t) = e-tu(t).
- (b) Since z(t) = rect(t \_ 0.5) = u(t) - u(t - 1), by linearity and time invariance

<!-- formula-not-decoded -->

~

<!-- image -->

<!-- image -->

## 4.19 (Solution)

- (a) y(t) = y(0)+ Nonlinear (unless y(0) = 0); time invariant; causal, dynamic; unstable (for example; the bounded input u(t) integrates to the unbounded ramp r(t))
- (b) y(t) t&gt; 0
- t+1 (c) y(t) = LTI; causal, dynamic; stable (integration is over finite range) t~1
- (d) y(t) = 1+2
- t=0 (e) y(t) = Jt-2 ft-2-0
- rt+a (f) y(t) = t-1

## 4.20 (Solution)

- (a) y(t) = z(2t) Linear , time varying, dynamic; noncausal; stable
- (b) y(t) = z(-t) Linear, time varying; dynamic; noncausal, stable
- (c) y(t) = 2(0.5t) Linear, time varying, dynamic, causal; stable
- (d) y(t) = sgn[z(t)] Nonlinear; time invariant, instantaneous, causal, stable
- (e) y(t) = |z(t)l Nonlinear, time invariant, instantaneous, causal, stable

## 4.21 (Solution) Refer to the following table:

| a)   | Linear for:         | any œ   | any Q   |
|------|---------------------|---------|---------|
|      | Causal for:         |         | Q < 0   |
|      | Time-Invariant for: | Q =1    | any Q   |
|      | Instantaneous for:~ |         |         |

## 4.22 (System Response)   Refer to the following sketches:

Figure P4.22. Input signals for Problem 4.22.

<!-- image -->

Consider the relaxed system

- (a) y(t) + y(t) = z(t) z(t) = u(t) The response is yo(t) = (1 \_ e-')u(t)

- This gives y1(t) = (t \_ 1 + e-')u(t)
- Alternate method: Since tu(t) is the running integral of u(t) , by linearity, +e-t.
- y2(t) So,
- (e) Tbe results of (a) and (b) are the derivative of the results of (c) and (d), respectively

## 4.23 (Solution)

- SF = C =T and s(t) = T + With s(0) = 0, we get s(t) = T(1
- y(t) = (5 +3e-2)u(t).
- (a) yv(t) = and yF(t) = 5 3e-2t
- (b)
- (c) yzi(t) = Ke-2 , y(0) = 8 OI ~5e-2t
- (d) z(t) = lOu(t) (because the forced response is a constant) .
- 4.25 (Solution) %(t) +y(t) = 2(t) y(t) = (5e-t
- y(0) =5+3 = 8. The forced response is yF(t) = 3e-2t 3e-2)u(t) Also, S0, So,
- y2(t) = yzs(t) + 2yzs(t) = 3e- \_ 6e-2t = ~3e-tu(t)
- y(t) = (5 + 2t)e-3)u(t).

= Ke-t y(0) =0 or Yzs(t) = (~3e-t + 43e-2t

- ~ 2)

- (a) Tbe natural response will be of the form yv(t) = Ke-t . S0, the term 2te-3 describes the forced response.  Also; œ = 3 and y(0) = 5.

<!-- formula-not-decoded -->

- (b) If y(0) = 10, we have yzi(t) = y(0) = = 1Oe-3t Ke-3

- y2(t) = 2yzs(t) + %zs(t) = ~(3 + 2t)e-3u(t)
- yzi(t) = 4e-3 and the complete response is y3(t) = 4e-3t + y2(t) = (1 2t)e-3tu(t)
- (a) h(t) = e-t/-u(t)
- (b) The response is s(t) = h(t)dt = T(1 \_ If z1(t) = 4[u(t) u(t \_ œ)] then step

We find,

<!-- formula-not-decoded -->

Using e ~ 1 + 2, this simplifies to y1(t) = =e-t/-

- y2(t) = Ke-t/- + This gives y2(t) = Thus, ~e-t/-
- 4.28 (Solution)
- (a) y(t) + 2y(t) = 2e-(t-I)u(t \_ 1). If I(t) = 2e-t, the forced response id yF = Ce-t = 2e-t and the ZSR is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- For e-2u(t): yF = Cte-2 = + Ke-2, y(0) = 0 or yzs Tbe required response is y(t) = Result of 4.28(a) 4 te-2t te-2t te-2t te-2t

0, and we get y2(t)

- (c) y(t) + 2y(t) = + 2e-(-Iu(t ~ 1). Use superposition. For y(0) = 0 +t)e-: The required response is y(t) = Result of 4.28(a) + (-1+t)e -t te-t Ke-2t 4e-2t +e-2t
- (d) y(t) + 2y(t) = cos(2t) + 2e-(t~1)u(t - 1). Use superposition

For cos(2t)u(t): YF = Acos(2t) + Bsin(2t) 0.25 cos(2t) + 0.25 sin(2t) ZSR is yzs 0.25 cos(2t) + 0.25sip(2t) + y(0) = 0 OI Yzs = 0.25 cos(2t) + 0.25 sin(2t) 0.25e-2t The required response is y(t) = Result of 4.28(a) +0.25 cos(2t) + 0.25 sin(2t) 0 . So, Ke-2t 25e-2i

## 4.29 (Solution) Note: s(t) is the response and h(t) is the impulse response: step

<!-- image -->

- (Circuit 1:)
- (Circuit 2:) +Cs(t) = 0 s' (t)+!s(t) = !u(t) So, sv(t) = Ke-t/-

Choose sF = C = 1 s(0) = 0 = 1+K K = -1 s(t) = (1 Tbus h(t) = /(t) =

- (Circuit 3) s(t) = u(t) = (1 e-t/-)u(t) =
- (Circuit 4:) (Mesh Equation): Li' (t) + Ri(t) = u(t) (7 = 4) Since s(t) = Ri(t), we have $(t) + !s(t) =
- (Circuit 5:) (KCL at output node): s(t) ~ u(t) + /(t) + s(t) = 0 s' (t) + 2s(*) = u(t) S0, SN = Ke-2 SF = 0.5 s(t) =0.5 \_ Ke-2 . With s(0) = 0 we find s(t) (0.5 h(t) = /(t) = e-2u(t).
- (Circuit 6:) (KCL at output node): s(t) = u(t) + f s(t)dt + s(t) = 0 s(t) = With s(0) = 0, K = 0.5. Thus, s(t) = h(t) = /(t) = 0.58(t) 0.25e-+/2u(t) So; =SN

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## 4.30 (Solution) Refer to the following sketcbes.

<!-- image -->

- 1 The system is LTI, s0 we advance (shift left) the input and output 1 unit
3. The step response s(t) is 2u(t)~ 4u(t = 2)
- 2 Tbe input is 2u(t) - 2u(t \_ 1) (superposition of two steps) and tbe response is the superposition of two pulses.  The response to 2u(t) is the first 4u(t) 4u(t 2) pulse
- 4

## 4.31 (Solution) Refer to the following sketch.

<!-- image -->

<!-- image -->

- (a) The unit step response is s(t) = (1 \_ Witb z(t) = 5[u(t) y1(t) = 5(1 \_ e-2)u(t) 5(1 ~e-2(-1))u(t) y2(t) = 5(1 \_ e-0.2)u(t) - 5(1 - e-0.2(-1))u(t)

<!-- formula-not-decoded -->

- 4.32 (Solution) Argue for against the following statements assuming relaxed systems and constant element values. You may validate your arguments simple circuits. using
- (a) A system with only resistors is always instantaneous and stable Ttue See circuit 1 of Prob.4.29, for example
- (b) A system with only inductors and/or capacitors is always stable. False. It is linear, causal, but not necessarily stable. = Li' (t) (an inductor), the operational transfer function H(s) = sL is pot strictly proper, and tbe system is unstable.
- (c) An RLC system with at least one resistor is always linear, causal and stable. True. Examples: Tbe circuits of Prob.4.29 are linear, causal and stable.

## 4.33 (Solution)

- (b) h(t) = e~tu(t) e-2tu(t) This suggests roots s =-1 and = ~2 and a differential equation

<!-- formula-not-decoded -->

## 4.34 (Solution)

- The inverse system is y(t) + 2y(t) =2"(t) + 22(t) + 2(t) (unstable)

## 4.35 (Solution)

- Not invertible (sign ambiguity)
- (b) y(t) = Inverse system is z(t) = Iny(t) er(t)
- (c) y(t) = cos[z(t)] Not invertible (ambiguity due to periodicity)
- (d) y(t) = ejz(t) Not invertible (ambiguity due to periodicity)
- (e) y(t) = z(t \_ 2)
- (f) %(t) + y(t) = z(t) Inverse system is y(t) = %(t) + z(t)

## COMPUTATION AND DESIGN

- 4.36 (Solution) Uses the ADSP routine sysrespl

```
'PROBLEM 4 .36 N=2;D=[1,2] ; ystep=sysrespl(s' ,N,D, [1 0 0 0 0])
```

```
4.37 (Solution) Uses tbe ADSP routine sysrespl 'PROBLEM 4.37 'PARI (a) N=1;D=[1,1] ; t=0:0.01:4;subplot(2,1,1) ,plot (t,eval (ys) ) subplot(2,1,2) ,plot(t,eval(yi)) ,pause 'PART (b) N=1;D=[1 ,sqrt (2) ,1] ; ys=sysrespl ('s' ,N,D, [1 0 0 t-0:0.01:4;subplot(2,1,1) ,Plot (t,eval (ys)) subplot(2,1,2) ,plot(t,eval(yi)) ,pause 'PART (c) N=[1,0] ;D=[1,1,1] ; t=0:0.01:4;subplot(2,1,1) ,plot (t,eval(ys)) subplot (2,1,2) ,plot (t ,eval (yi)) ,pause 'PART (d) N=1;D=[1,2,2,1] ; 0 0 0]) ;yi=sysrespl('s' ,N,D) ; t-0:0.01:4;subplot(2,1,1) ,plot (t ,eval (ys)) subplot (2,1,2) (t,eval(yi)) 4.38 (Solution) For step response and impulse response; see previous problem. 'PROBLEM 4 .38 Uses the ADSP routine trbw N-1;D=[1,sqrt (2) ,1] trbv(N,D,5) pause 'Ibis vill produce an error subplot (t,y) N-[1] ;D=[1,2,2,1] ;trbv (N ,D,5) 4.39 (Solution) Uses the ADSP routines sysrespl _ 'PART (a) C-3;N=1 ;D=[1 4,C] ;ys=sysrespl ('8' ,#,D,[1,0,0,0,0]) ;yi=sysrespl ('s' ,N,D) ; t=0:0 . 01:5;subplot(2,1,1) ,plot (t ,eval (ys)) subplot (2,1,2) ,plot (t,eval (yi)) ,pause t=0:0.01:5;subplot(2,1,1) ,plot(t ,eval (ys) ) subplot (2,1,2) ,plot (t ,eval (yi) ) ,Pause 'plot
```

```
t-0:0.01:5;subplot(2,1,1) (t,eval(ys)) 'KPARI (b) smallest tr and ts 'PART (c) C-3;N=l;D=[1,4,C] trbw(N,D) ,pause C-4;N=l;D=[1,4,C] trbw (N,D) pause C-5;=1;D=[1,4,C] ;trbw(N ,D) 4.40 (Solution) Uses the ADSP routine ssresp X= [2,3,-pi/3] ;t=0:0.01:3; 'PARI (a) pause 'PART () C=4;N=1;D=[1,4,C] ;yss4-ssresp('s' ,W,D,x) ,plot(t,eval (yss4) ) ,pause 4.41 (Solution) ctsin 'PROBLEX 4 41 ye=(1-exp(-t)) _ (t<=1)+(exp(-t+1)-exp(-t)).*(t>1); 'PART (b) a=1;N-a;D=[1,a] ;x='sin(t).*(t<-pi) ;t=0:0.02:6; yn=ctsim(N,D,X,t) ;plot(t,yn,t,eval(x)) ,pause sin(t).*(t<=pi) ;t=0:0.02:6; t=0:0.02:6; 'PART (c) a=100;N=a;D=[1,a] sin(t),*(t<-pi) ;t=0:0.02:6; pause a=1OO;N=a;D=[1,a] ;x='sin(t).*(t<-pi)';t-0:0.03:6; ya=ctsin(#,D,x,t);plot(t,yn,t,eval(x)) ,pause t=0:0.0201:6; yn-ctsim(,D,x,t);plot(t,yn,t,eval(x)) pause a=10O;-a;D=[1,a] ;x=' sin(t).*(t<-pi)' t=0:0.0202:6; yo=ctsim(N,D,x,t);plot(t,yn,t,eval(x)) ,pause a=100; 'sin(t).*(t<-pi) t=0:0.0203;6; yn=ctsin(N,D,X,t);plot(t,yn,t,eval(x)) ;x='
```

## 5.3 (Solution)

<!-- formula-not-decoded -->

## DISCRETE-TIME SYSTEMS

## 5.1 (Solution)

- (b) O2[] = 4[]+3
- (c) O[] aO[r] = nonlinear . =q[] So,

## 5.2 (Solution)

- = linear.
- LII, dynamic; causal
- (b) y[n] +y[n + 1] = nz[n]
- LTI, dynamic, Doncausal.
- Nonlinear, time-varying, dynamic; noncausal.
- Nonlinear, time-invariant, dynamic, noncausal.
- Linear, time-varjing; instantaneous (static), causal.
- 2] LII, dynamic, causal.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

No general form discernible.

## 5.4 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(0.5A B) sin(0.5næ) = cos(O.5nn). Comparing coefficients of the cosine and sine terms; we get

<!-- formula-not-decoded -->

## 5.5 (Solution)

<!-- formula-not-decoded -->

- yF[n] = Cn(0.5)" (because one root is z = 0.5). 2)(0.5)"-2 . y[n] 0.9y[n = 1] +0.2y[n = 2] = [Cn ~ 1.8C(n ~ S0, So,
- c(0.5)n-2

- (d) y[n] 0.25y[n 2] = cos(nr/2) Thus, yF[n 2] Acos[0.5(n = ~Acos(0.5nn) y[n] = A = 0.8, B = 0 So;

## 5.6 (Solution)

- (a) y[n] 0.5y[n = 1] = 2u[n]. S0, Characteristic eq is: 1 0.5z-1 = 0 or yN[n] = K(0.5)". S0,
- Characteristic eq is; 1 \_ Also, yF[n] = y[n] 0.4y[n ~ 1] 0.8C)(0.5)" (0.5)" or C = 5. So, ZSR is yzs[n] = K(O.4)" + 5(0.5)", v[-1] = 0. Thus, K(0.5)-1 +5(0.5)-1 =0or K = -4. So, =(C \_ S0,

- yF[n] = Cn(0.4)" and yF[n C(n 1)](0.4)" = So, So,

- (d) y[n] - 0.5y[n 1] = cos(0.5n7) So, Characteristic eq is: 1 ~

## 5.7 (Solution)

Also, YF = C = 10 (from Problem 5.5a) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) y[n]-0.9y[n-1]+0.2y[n-2] = (0.5)". Ch eq is 1-0.9z-1+0.22-2 = 0 or (z-0.5)(z-0.4) = 0. So,

<!-- formula-not-decoded -->

Also; yF = C(0.5)" =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) yln] ~ 0.25y[n = So, Ch eq is 1 0.25z -2 = 0 or (z - 0.5)(z + 0.5) =0 So;

<!-- formula-not-decoded -->

This gives K1 = 0.1, Kz = 0.1

- 5.8 (Solution) y[n] Ch. 1-0.52-1 = 0 root: z = 0.5 YN = K(0.5)" Eq:
- (a) z[n] = 2 y[n] = yN + yF = K(o.5)" + 4 y[-1] =-1 =2K + 4 K = -2.5 y[n] = 4 \_ 2.5(0.5)"
- (b) z[n] = (0.25)" yF[n] = C(0.25)" yF[n] 0.5yF [n = 1] = C(0.25)" 0.5C(0.25)2-1 = (0.25)"

<!-- formula-not-decoded -->

- (c) z[n] = n(0.25)"

Comparing coefficients of powers of n, we find

<!-- formula-not-decoded -->

=0

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (e) zn] = n(0.5)" yFln] = (C + Dn)n(0.5)" (because natural response has same form) 0.5[C + D(n 1)](n ~ 1)(0.5)"-1 = (c ~ D) + 2nD = n C =D =0.5 yF{n] = 0.5(n + 1)n(0.5)" y[~1] =-1 = 2K K = -0.5 y[n} = ~(0.5)(0.5)"+0.5(n+1)n(0.5)" = +n-1)(0.5)"+1 So, So, So, (n?

So, yF[n]

O.5yF[n

1] = (0.5)" cos(0.5n1).

The left-hand side is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Comparing coefficients of the sine and cosine terms, we find

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.9 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Also; YF = C(0.5)" =

<!-- formula-not-decoded -->

1(0.5)" (from Problem 5.5c).

<!-- formula-not-decoded -->

- y[~1] = 0, Ch eq is 1 \_ y[n] = K1(0.5)" + K2(-0.5)" \_ 4(0.4)". With y[~1] = 0 and y[-2] = 3, we K1(o.5)-1 + K2(-0.5)-1 4 (0.4)-1 0 K1(0.5)-2 + K2(-0.5)~2 4(0.4)-2 = 0 This gives K1 = 2.875, Kz = 0.6528 So, get
- 2] = (0.5)", y[-1] =0, y{-2] = 0 Ch eq is 1 \_ 0.252-2 =0 or (z - 0.5)(z + 0.5) = 0. Also, yF = Cn(0.5)". So, [Cn 0.25C(n ~ 2)(0.5)-2](0.5)" = (0.5)" or € = 0.5 With y[~1] = 0 and y[~2] = 0, we get K1(0.5)-1 + K2(-0.5)-1 \_0.5(0.5)-1 K1(0.5)-2 + K2(-0.5)-2 \_ (0.5)-2 = 0. Tbis gives K1 = 0.75, Kz = 0.25

## 5.10 (System Response) Refer to the sketch for realizations.

Realization for part (a)

<!-- image -->

Generic realization for parts (b e)

- y(-1] =0 Ch eq is: 1 Also, yF[n] = C(0.5)". So, [C 0.4C(0.5)-1] = (0.5)" or € = 5.

So, y[n]

=

- y[~1] =0 From part (a), for z[n] = (0.5)" the ZSR is yzs[n] = [~4(0.4)" + 5(0.5)"Ju[n] By linearity and time invariance, y[n] = 2yzs[n] + yzs[n \_ 1]

K(0.4)" + 5(0.5)"

- z[n] = (0.5)"u[n], y[~1] =5 Also; the ZIR is yzi[n] = K(0.4)". Witb yzil-1] = 5 = K(0.4)-1, we find K = 2 Thus, yzi[n] = 2(0.4)"u[n]

By linearity and time invariance; y[n] = 2y2s[n] + yzs[n \_ 1] + yri[n]

- y[~1] = 2 S0, [C + 0.5C(0.5)-1] = (0.5)" or € = 0.5. the ZSR is yzs[n] = K(-0.5)" + 0.5(0.5)" With y[~1] = 0, we fnd K = 0.5 and s[n} = 0.5(-0.5)" + 0.5(0.5)" Also, the ZIR is yzi[n] = K(-0.5)" witb y[-1] = 2 = K(-0.5)-1 we get K = So, thus; So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.11 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

4-0.5B-0.25A = 1

S0, yF[n]

=

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (8) {z2 + 42 + 4}y[n] = 2"u[n]

Ch.

Eq: z2 + 4z + 4 = 0

roots:

2 =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Note: We need the IC y[0], y[1}- By recursion, we find

<!-- formula-not-decoded -->

B+0.54-0.25B = 0

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

roots: -0.5,

~0.25

=

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

=

K(-0.5)n + K2(-0.25)"

A =12/13 =

0.923, B

=

~8/13 = -0.615

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.12 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The zero state response is the response of part(a) shifted two units.

<!-- formula-not-decoded -->

Ch. Eq: 22\_gz+356

roots:

2 =

0.5, 0.25

- z[n] = u[n]

YN =

A(0.5)" + B(0.25)"

<!-- formula-not-decoded -->

Zero-State: yzs

=

YF 4 YN

=

<!-- formula-not-decoded -->

Zero-Input: yzi

=

YN

=

<!-- formula-not-decoded -->

0.75(0.5)" \_ 0.125(0.25)"

=

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (e) [1 y[-1] =y[-2] = 1

Ch. Eq: z2

~

0.25 = 0

roots: 0.5, ~0.5

YN

=

A(0.5)" + B(-0.5)"

<!-- formula-not-decoded -->

Zero-State: yzs = YF

So,

=

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (f) [z2 = By time invariance; this is equivalent to [1-4z-2Jy = [2 + 2-2]z Yzs = ~ g(0.5)" By superposition; y[n] = 2y2s[n] + yzs[n = 2] + yzi So, y[n] =

=

! +A(O.5)" + B(-0.5)n with ZERO IC

<!-- formula-not-decoded -->

## 5.13 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.14 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) yn] +2y[n - 1] = [n = 1} IIR, Causal Start with ho[n] + 2ho[n ~ 1] = z[n]
- (e) y[n] + 2y[n ~ Ftom part(c), ho[n] = (~2)"u[n]- By linearity and time-invariance

- IIR; Noncausal Start with ho[n] + 2ho[n - 1] = [n] From part(c), ho[n] = (~2)"u[n}  By linearity and time-invariance

- (g) [1 Start with [1 + 42-1 + 32-2]y = z. Its impulse response is ho[n] = A(-3)" + B(-1)" with ho[~1] = 0, ho[o] = 1A+ B =1 B = -0.5 ho[n] = [1.5(-3)" \_ 0.5(-1)rJu[n] By time-invariance; h[n] = ho[n - 2] = [1.5(-3)"-2 0.5(-1)n-2Ju[n ~ 2]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.15 (Solution)

## 5.16 (Solution) All systems are static.

- (a) y[n} = 3"[n] Linear , time varying, causal, stable
- Linear, time varying, causal, stable
- Linear, time varying, causal, stable
- Linear, time varying, causal, stable
- (e) y[n} = Nonlinear , time invariant, causal, stable ez[n]
- Nonlinear , time invariant, causal, stable

## 5.17 (Solution)

- (a) y[n] = zn/3] Linear, time varying, causal, stable
- (b) yn] = cos(nr)z[n] Linear, time varying, causal, stable; static
- (c) y[n] = [1 + cos(nz)Jz[n} Linear, time varying, causal, stable, static
- (d) y[n] = cos(nzz[n]) Nonlinear , time varying, causal, stable, static
- (e) y[n] = Nonlinear, time varying, causal; stable, static
- LTI, causal, stable
- LTI, causal, stable

<!-- formula-not-decoded -->

- 0 &lt; Q &lt; 1 LTI, causal, stable
- (j)   y[n] = Nonlinear , time invariant, causal, stable
- Noncausal and stable (FIR filter)
- Causal and stable (FIR filter)
- causal. So,
- Noncausal (due to z[n + 2]) and stable (root is z = 0.2).
- Causal. Roots: z = -0.54j0.5. S0 |zl = 0.707, s0 stable.
- Noncausal. Roots: z = 0.5+j1.5. stable.
- Causal. Roots: z = 1 S0 unstable .
- Noncausal, Roots:

5.18 (Solution) Classify each system in terms of its linearity; time invariance; memory, causality; and stability.

- Linear, time varying, noncausal; stable
- (b) The decimating system y[n] = z[2n] Linear, time varying, noncausal, stable
- (c) The zero-interpolating system y[n] = z[n/2] Linear, time varying, noncausal , stable
- Nonlinear, time invariant, causal, stable; static
- (e) Nonlinear , time invariant; causal, stable, static

## 5.19 (Solution)

- (a) v[n] round{z[n]} stable
- (b) y[n] = median{z[n + 1], z[n] z[n 1]} Nonlinear , time invariant, noncausal, stable
- (c) y[n] = r[n]sgn(n) Linear, time varying; causal, unstable
- (d) y[n] = z[n]sgn{z[n]} Nonlinear , time invariant, causal, stable

## 5.20 (Solution)

- 0 &lt; Q &lt; 1
- (e) y[n) = cos(nr)z[n] Invertible. Inverse system: cos(nr)y[n] = z[n]
- (f) y[n] = cos(z[n]) Not invertible (ambiguity due to periodicity)
- (g) y[n] = Invertible. Inverse system: = ez[n]

## 5.21 (Solution) See sketches for the realizations.

<!-- image -->

- ts =0.5 ms and 1 ms corresponds to N = 2 So,

- (b) y[n] = z[n] + O.5[n 2] The response is sn] = u[n] + 0.5u[n = 2] So, step
- (c)

The roots of the characteristic equation are z = h[o] = 1, h[-1] = 0. We find h[0] = 1 = A and u[n], the forced response is yF = C, which gives C+0.5C = 1 ? y[n] = y[~1] =0 =y[-2] Or A = sin(0.5n7)] So, So, So, So,

## 5.22 (Solution) Refer to the sketch for the realizations.

<!-- image -->

- (a) yIn} = z[n] + 0.25y[n A delay of 1 ms means N = 2.
- = A+ B, h[-1] = 0 = 24 - 2B. S0, A = B = 0.5 and h[n] = 0.5[(0.5)" + (~0.5)"] For the response, y[-1] = 0, y[-2} = 0 Thus y[-2] = 0 =4A+4B+ ! step So,
- (c) is 2]- Its response is s{n] = u[n] - 0.25u[n 2] step

## 5.23 (Solution) y[n] - 0.5y[n - 1] = zn]. So; yv{n] = K(0.5)"

- (a) z[n] = u[n] YF =C. ZSR is yzs[n] = K(0.5)" +2, y[-1] = 0. Ihis gives 0 = 2+ 2K or K = -1 So, So,
- 0.5(n = 1)c(o.5)-1](0.5)" = (0.5)" and € = 1.

- (c) z[n] = cos(nn/2)u[n] yF[n] = (form Problem 5.4d). S0,

So,

- This gives 0 = -?+2K or K = ;
- Note that the response is complex valued because tbe input is complex valued
- = 2 cos(0.25nT) . Substitute into yF[n] 0.5yF[n So, So,

B = 1.3025.

## 5.24 (Solution) For the realization; y[n] = z[n] - 0.5y[n 1] = z[n] S0, yN[n] K(-0.5)"

<!-- image -->

Figure P5.24. System realization for Problem 5.24.

- y[-1] So, So,
- y[-1] = 4 Follow part (a) and set y[n] = K(-0.5)"+3, y[-1] = 4 This gives 4 = ~2K + ? o K = 3f
- (c) z[n] = (0.5) "u[n], y[-1] So, yF[n] = C(0.5)". So, [C + 0.5C(0.5)-1](0.5)" = {(0.5)" or =0.5 This gives 0 = ~2K + 1 or K = 0.5
- (d) z[n] = (0.5) u{n] y[-1] = 6. Follow part (c) and set
- (e) z[n] = (~0.5)"u[n}, y[-1] = 0. yF[n] = Cn(-0.5)". (~0.5)" or C = 1 So, So, So,
- y[-1] =-2. Follow (e) and set y[n] = K(-0.5)" + n(-0.5)" y[-1] = -2 Tbis gives ~2 = -2K + 2 or K = 2 part

- 5.25 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

So,

K = 1 and y2in] = (0.4)"u[n]

For the input (0.4)"u[n], the forced response is yF[n] = Cn(0.4)". So,

<!-- formula-not-decoded -->

By linearity and time invariance; y[n] = yo[n = 1] + y1[n] + yzi[n]

- (c) yn] - 0.4y[ny[-1] = 2.5 Ftom part (b), its ZIR is yzi[n] = (0.4)"u[n] B = 5 Its ZSR is y2[n] = K(0.4)" (5n 20)(0.5)", y2[-1] = 0. 0 = 2.5K - 50 or K = 20. So, y2[n] = [20(0.4)" \_ (5n \_ 20)(0.5) "Ju[n] = So,

## 5.26 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 5.27 (Solution) Response: y{n] = 5 + 3(0.5)".
- (a) yF[n] = 5 yv[n] 3(0.5)"
- (b) Q = -0.5 and y[-1] =5+6 = 11.
- Tbus 11 = 2K and yzi[n] = 5.5(0.5)". Thus 0 = 2K + 5 and yzs[n] =
- 5.28 (Solution) System: yn) + 0.5y[n - 1] = z[n]
- (a) yF[n] = 5(0.5)" yzs[n] = K(-0.5)" + 5(0.5)", y[-1] =0 Tbus 0 = -2K + 10 and So,
- (c) 2]
- (d)
- 5.29 (Solution) System: y[n] + 1] = z[n] Response: y{n 1] = (5 + 2n)(0.5)"u[n] œy[n
- (a)

- (c) For tbe input z[n 1], the response is yzs[n \_ 1]
- (d) For the input 2z[n
- So, for the input 2r[n 1] + z[n], the response is 2yzs [n 1] + yzs [n] + yzi[n]

## 5.30 (Solution) In all cases, the input is u[n]

- So,
- (b) System 1: y[n] System 2: y[n] = z[n] - z[n = 1] The output of system 1 is y[n] = yF{n] + yv[n] = 2+ K(0.5)". With y[-1] = 0 = 2+2K, we K = = s[n] + (0.5)"u[n 1] = (0.5)"u[n]. Tbus, the order of cascading does not matter here (because both systems are LTI). get
- (c) System 1: y[n] = 2?[n] The output of system 2 is thus y2[n] = [2 \_ (0.5)"Ju[n] (step response from part (b))

The response is not the same so order of

- (d) System 1: y[n] = 0.5y[n = 1] + z[n] Tbe output of system 2 is y2[n] = [2 cascading is important (because the squaring system is not LTI) .

## 5.31 (Solution) Refer to tbe sketch

Figure P5.31. System realization for Problem 5.31.

<!-- image -->

- (a) For the two feedback subsystems; y[n] ~ œy[n ~
- (b) For Q = 1] and the difference equation is y[n] - œy[n 1] =

## 5.32 (Solution)

<!-- formula-not-decoded -->

- (c) h[n] = (0.3)"u[n] difference eq has the RHS y{n] ~ 0.3y[n = 1] y[n] ~ 0.3y[n 1] = 2[n] So, So,
- = 40.5, s0 the RHS of tbe difference equation bas the form y[n] ~ 0.25y[n = 2] h[n] So,

<!-- formula-not-decoded -->

The difference equation of tbe inverse system is y[n] = ~ This is an FIR filter that performs an averaging operation.

## 5.34 (Solution)

- (a) y(t) + 3y(t) + 2y(t) = 2u(t) Ch. Eq: roots: Negative real parts, s0 stable system8?
- (b)
- 1]) +2y[n] = 2u[n] S0,

<!-- formula-not-decoded -->

- y" (t) ~ y[n + 2] - 2y[n + 1] + yn] y' (t)+3y(t)+2y(t) = This simplifies to: y[n + 2] + y[n + 1] = 2u[n] Ch. roots: 2 = So,

<!-- formula-not-decoded -->

- (d) The results suggest that the backward Euler algorithm is better for preserving stability.

Figure P5.35. Filter realization for Problem 5.35.

<!-- image -->

- ~ 1] The difference eq is y1[n] = z[n] ~ z1[n \_ 1]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.36 (Solution) Refer to the sketch for the realization.

<!-- image -->

z[n] = the difference equation is y[n] = y[n \_ 7] = 2[n] So,

## 5.37 (Solution)

<!-- formula-not-decoded -->

## 5.38 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- So,
- S0, y[n} = {1

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 5.39 (Solution) y[n] - 0.8y[n 1] = z[n]  Its impulse response is h[n] = (0.8)"u[n}.

The three-term truncated impulse response is hB[n] =

<!-- formula-not-decoded -->

Tbe step response of the truncated filter is y3[n] = u[n} + 0.8u[n - 1] + 0.64un ~ 2]

We tabulate y[n] and y3[n] for 0 &lt; n &lt; 6.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Clearly; tbere is more mismatch as n increases. As n -+ 0,

## 5.40 (Solution)

- (a) y[nJy[n

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

it appears tbat the choice of the initial condition y[~1} has little effect. So,

## 5.41 (Solution)

n =0 :

get

n =1 :

n =3 :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

S0 the response magnitude keeps increasing and the system is BIBO unstable.

- (b) y[n] ~ 0.5y[n -

Check response by recursion. Let z[n]

n =0 :

n =1:

$$y[1] = 0.5y[0] + (1 + 1) = 3$$

n =2 :

y[2] = 0.5y[1] + (2 + 1) =4.5

n =3 ;

$$y[3] =0.5y[2] + (3 + 1) = 6.25$$

Again, the response magnitude is increasing and indicates BIBO instability.

## 5.42 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## COMPUTATION AND DESIGN

## 5.43 (Solution) Uses the ADSP routine sinc

```
'PROBLEX 5.43 format ye=0.53309323761827 ; ts=0.1;t=O:ts:3;x=sinc(t); N-0.5*ts* [1,1] ;D=[1 _ err5-ye-yn err= [errl,err2,err3,err4,err5] ,min(abs(err)) ts=0.3;t=O:ts:3;x-sinc(t); N=0.S*ts*[1,1] ;D=[1,-1] ;y filter(N,D,x) ;L-length(y) ;yn-y(L)= err2-ye-yn err5-ye-y err=[errl ,err2,err3 ,err4 ,err5] min(abs (err)) format long
```

'Simpsons rule gives least Smaller tine produces smaller error step

## 5.44 (Solution) Uses the ADSP routine dtplot

```
'PROBLEM 5 .44 x-ones (size(n));y=filter(N ,D,x) ; subplot (2,1,1) ,dtplot (n,x,'0') ,subplot (2,1,2) ,dtplot '0') , pause subplot (2,1,1) ,dtplot (n,x,'0') ,subplot (2,1,2) ,dtplot '0') ,pause x=sin(.l*n*pi);y-filter(N,D,x); subplot (2,1,1) ,dtplot '0') ,subplot(2,1,2) ,dtplot (n,J,'0') ,pause x=(rem(,5)=z0);y-filter(N,D,x); subplot (2,1,1) ,dtplot '0') ,subplot(2,1,2) ,dtplot '0') ,pause (n,y, (n,J, (n,x, (n,y,
```

## 5.45 (Solution)

```
'PROBLEM 5 .45 xsones subplot (2,1,1) ,dtplot (n,x,'0' ) ,subplot (2,1,2) ,dtplot 0' ) ,pause subplot (2,1,1) ,dtplot'0') ,subplot(2,1,2) ,dtplot_ '0? ) ,pause x=sin(0.l#n*pi);y-filter(N,D,x) ; subplot (2,1,1) ,dtplot '0') ,subplot (2,1,2) ,dtplot (n,Y,'0' ) ,pause subplot (2,1,1) ,dtplot (n,x , '0') ,subplot (2,1,2) ,dtplot '0') ,pause subplot (2,1 ,1) ,dtplot '0') ,= subplot (2,1,2) ,dtplot'0') (n,y, (n,y,
```

## 5.46 (Solution) Uses the ADSP routine dtplot

```
'PROBLEM 5 .46 n=0:199; x=(0.9 n) ; yl=[x;O*x;O*x] ;y-yl(:) ' :200) ; subplot(2,1,1) ,dtplot (n,x , ') ,subplot(2,1,2) ,dtplot(,y,' .') x=cos(0.O4*n*pi);y-cos(0.2*n*pi).*X; subplot(2,1,1) ,dtplot (n,X , pause x-cos(0.O4*n*pi);y-(l+cos(0.2*n*pi)).*I; subplot (2,1,1) ,dtplot (2,x, ') ,subplot (2,1,2) ,dtplot (n,Y,' .') ;yFy(1 Pause
```

```
5.47 (Solution) Uses the ADSP routine dtplot 'PROBLEM 5.47 x2=0.1*(n-2)+sin(0.1*(n-2)#pi);x3=0.1*(n-3)+sin(0.1*(n-3)#pi); subplot (2,2,1) ,dtplot ''),title('input') subplot (2,2,2) ,dtplot subplot (2,2,3) ,dtplot (n,yd , '),title('Direct computation of output') subplot (2,2,4) ,dtplot (n,y-yd , ('error FILTER direct' ) ,pause subplot (2,2,1) ,dtplot (n,* , ') ,title input') subplot (2,2,2) ,dtplot ') ,title('output of FILTER.M') subplot (2,2,3) ,dtplot (n,yd , ') ,title('Direct computation of output') subplot (2,2,4) ,dtplot (n,y-yd , '),title ('error FILIER direct') ,pause vay possible subplot (2,1,1) ,dtplot '),title('input-) subplot(2,1,2) ,dtplot= ') ,title('output of FILIER.M ) 5.48 (Solution) Uses the ADSP routines dtplot _ randist 'PROBLEM 5.48 uni x1=0.1*(n-1)+sin(0.1*(n-1)#pi); 12=0.1*(n-2)+sin(0.1*(n-2)*pi);x3-0.1*(n-3)+sin(0.1*(n-3)#pi); N=0.25* [1,1,1,1] ;D=l;y=filter(N,D,x) ;yd=0.25*(x+xl+x2+x3) ; subplot (2,2,1) ,dtplot (,<, ') ,title('input') subplot (2,2,2) ,dtplot (,Y , '),title('output of FILTER.M' ) subplot (2,2,3) ,dtplot yd , ') ,title('Direct computation of output') subplot (2,2,4) ,dtplot (n,y-yd , '),title ('error FILTER direct') ,pause subplot (2,2,1) ,dtplot (n,x, P) ,title('input') subplot (2,2,2) ,dtplot '),title('output of FILTER.M') subplot (2,2,3) ,dtplot ') ,title('Direct computation of output') subplot (2,2,4) ,dtplot (n,J-yd , ') ,title ('error FILIER direct' ) ,pause ) ,title(input ) subplot (2,1,2) ,dtplot ) ,title('output of 5.49 (Solutiop) Uses the ADSP routine dtplot 'PROBLEX 5 .49 N=[1,-1] ;D=l;y=filter (N,D,x) ; subplot (2,1,1) ,dtplot (,I, N=[1,-2,1];D=l;y-filter(#,D,x) ; ') ,subplot (2,1,2) ,dtplot ') ,pause N=[1,1,1]/3;D=l;yfilter(N,D,x) ; subplot (2,1,1) ,dtplot ') ,subplot(2,1,2) ,dtplot (n,J,' .') ,pause (n,y, (n,y, (n,<, (n,y, yd , (n,y, (0,y, (n,I,
```

```
subplot(2,1,1) ,dtplot '),subplot(2,1,2) ,dtplot(n,y,' .')
```

## 5.50 (Solution) Uses the ADSP routine dtplot , sysrespl

```
'PROBLEH 5.50 spause ~4) ,dtplot eval pause (ytl) ,0') ,Pause (n, (n,
```

You could also use dtsimgui.  The shows the results of part (d) gui

<!-- image -->

## 5.51 (Solution) Uses the ADSP data file echosig.mat

'EXAMPLE 5.51

load echosig

% Load echo signal

sound(echosig)

% Listen to ecbo signal

Nl-fix(0.09375*8192) ;/2-2*11 ;

Filter delays

2=[1

zeros(1,N2)J ;

% Numerator

of

inverse

d=[1

zeros (1,N1-1)

0.9

zeros(1,N2-N1-1) 0.8] ;

% Denominator

of

inverse

{ Filtered signal

sound (noecho)

% Listen to filtered signal

## CONTINUOUS CONVOLUTION

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

With œ = 1, this simplifies to y(t) = (t - 1 +e-t)u(t)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Split this into 4 integrals and simplify tbe limits on each

<!-- formula-not-decoded -->

we cannot just add the results.  Using appropriate step functions with each result, we So, get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Upon integration and appropriate step functions; using

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 6.4 (Solution) Refer to the sketches shown. Convolution with an impulse replicates a signal. If the Convolution 1 'Convolution 2

<!-- image -->

## 6.5 (Solution)

<!-- image -->

Since the signals are piecewise constant; the convolution is and peaks at t = 1. Fom the figure; y(1) = 32. At the end-points; the convolution is zero. Thus; y(-3) = 0 = y(5). linear

More formally; we compute the convolution by ranges.

<!-- formula-not-decoded -->

At the range end-points, we find y(-3) = 0, y(1) = 32, y(5) = 0.

- Pairwise sum: [~2, -1,2,3]

<!-- image -->

## 6.6 (Solution) Tbe sketches are shown below

<!-- image -->

(b)

- (a) y(t) 2)]We use superposition;
- With rect(t)*rect(t) = tri(t) and by superposition and shifting; we find y(t) = tri(t) \_ tri(t \_ 1).

<!-- formula-not-decoded -->

- y(t) = s(t)*[u(t)-2u(t-2)+u(t-4)] = (1-e-t)u(t)-2(1-e-(-2))u(t-2)+(1-e-(t-4))u(t-4)
- 1)] So,

## 6.8 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) z(t) = cos(t) y(t) = cos(t) * [2e-tu(t) - 6(t)] = [cos(t) + sin(t)] cos(t) = sin(t) (from Prob 6.3 d) . So,

<!-- formula-not-decoded -->

## 6.10 (Cascaded Systems)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 6.11 (Solution)

- (a) h(t) = e'+Ju(t - 1) causal and unstable (J |h(t)ldt = %)
- (b) h(t) = e-tu(t+1) noncausal and stable (f |h(t)|dt is finite)
- (c) h(t) = 8(t) causal and stable (J |h(t)ldt = 1)
- causal and unstable =
- (e) h(t) = 6(t) - e-'u(t) causal and stable (J |h(t)ldt = 1+1 = 2)
- (f) h(t) = sinc(t \_ 1)

<!-- formula-not-decoded -->

This means that y(t) starts only when z(t) is epplied.

If z(t) starts at t = t0, such that z(t) = z(t)u(t

<!-- formula-not-decoded -->

Since y(t) = 0 for t &lt; to, the response y(t) starts at t = to also.

## 6.13 (Solution)

<!-- formula-not-decoded -->

- (b) Using h(t X) and a periodic signal z(X), we y(t) = t-T get

Tbis is the average value of the periodic signal z(t). If z(t) is a sawtooth beight A, width to, period T and duty ratio D = y(t) = 0.54 = 0.5AD pulse get we

<!-- image -->

## 6.15 (Solution)

- (a) To find the output at t = 1 we need to convolve only the first For a series RC circuit with T = 1, h(t) = e-'u(t) pulse.

<!-- image -->

<!-- image -->

<!-- image -->

Since the second pulse starts only at + = 2, we find the response at t = 1 and t = 2 as

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) The steady-state response is the periodic convolution of one period of z(t) and the periodic extension of h(t) with T = 2. Now, h(t) = e-tu(t)

We first find the convolution of one period of the input [u(t) u(t = 1)] and hp(t) convolution by ranges; and the final steady-state response for one period using wraparound. regular using

<!-- image -->

<!-- formula-not-decoded -->

We now use and added to the result for 0 &lt;t&lt;1 as shown. Tbe steady-state response is thus past

<!-- image -->

6.16 (Solution) Refer to the sketches (regular convolution followed by wraparound) . Regular convolution Pcriodic convolution I=l

<!-- image -->

## 6.17 (Solution)

<!-- formula-not-decoded -->

- 0 because &amp; '(t) is not absolutely integrable) .

<!-- formula-not-decoded -->

- 6.18 (Solution) (t) = rect(t + 0.5) h(t) = trect(t \_ 0.5)

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

Signal endpoints: [~1,0], {0, 1], pairwise sum: [~1,0,1]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) y(t) = Thz = h(t) * z(-t) We use convolution by ranges

<!-- formula-not-decoded -->

<!-- image -->

'wise sum: [0,1,2] pairt

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

- (e) Tzh = Thz(-t)

## 6.19 (Solution)

- (a) Refer to the figure
- (b) The convolution y(t) lasts for 9s. The maximum value of y(t) is 10.
- (c) If we approximate z(t) by 10 impulses, the convolution y(t) will last for 9.5s. The maximum value of y(t) will still be 10.
- (d) Tbe exact form will approach a triangular pulse from 0 to with a peak of 10 units at t = 5. 105,

<!-- image -->

## 6.20 (Solution)

<!-- formula-not-decoded -->

- ~ 1) is a function (convolution)

<!-- image -->

<!-- image -->

## 6.22 (Solution) The response s(t) is the running integral of the impulse response h(t). step

- (a) h(t) = rect(t 0.5) = u(t)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) h(t) So, s(t) dX. Evaluate separately for t &lt; 0 and t 2 0:

<!-- formula-not-decoded -->

## 6.23 (Solution)

- (a) y(t) + 2y(t) = 2(t) h(t) = e-2u(t) So,
- (b) If z(t) = e-2u(t), y(t) = e-2u(t) *e-2u(t) = te-2u(t)
- (c) If z(t) = e-2u(t) and y(0) = 0, yF = Cte-2 and yF = C(1 \_ 2t)e-2t . 4 2CtJe -2 OI C = 1. S0, y(t) = yv(t) + yF(t) = Ke-2 + With y(0) = 0 = K +0, we y(t) =te ~2tu(t) =e-2t ~2t) get
- (d) If y(0) = 1, then 1 = K +0 and y(t) = 4te ~2)u(t) (e-2t
- (e) Outputs of parts (b) and (c) are identical (both describe the zero-state response) .

## 6.24 (System Response) Refer to the figure.

Figure P6.24. The circuits for Problemn 6.24.

<!-- image -->

- (a) = RC

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 6.25 (Solution) Refer to the sketch. is
- extension gives the desired periodic convolution (remember to include tbe normalizing factor of 2). Iect(t 0.5) is simply y(t) = tri(t \_ 1)

<!-- image -->

<!-- image -->

## 6.27 (Solution)

Regular convolution

<!-- formula-not-decoded -->

Periodic convolution T-2

<!-- formula-not-decoded -->

- Evaluate separately for t &lt;0 and t 2 0. ~2*u(t)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) z(t) = e-2u(t) + e2tu(-t) superpose the results of parts (a) and (b) S0,

## 6.28 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- The impulse response of the RC circuit, with T = 1, is h(t) = e-'u(t) We use convolution by ranges:\_Refer to the sketches below

t-

Range: O&lt;t&lt;l y(t)

<!-- image -->

0.37

- 0.5) Signal endpoints:  [0, % ], [0, 1], pairwise sum: [0, 1, %].

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) z(t) = trect(t \_ 0.5)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Tbe maximum value of y(t) occurs at t = 1, with y(1) = 1/e = 0.3679.

- (c) z(t) = (1 - t)rect(t \_ 0.5) Signal endpoints: [0, % ]: [0, 1], pairwise sum: [0, 1, %]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

when y (t) = 0 or -1 + 2e-t = 0. This gives

<!-- formula-not-decoded -->

[-1

Range: O&lt;t&lt;l

(a)

1[

Range: Dl

()

- 6.30 (Solution) Tbe step response of the cascaded system may be described as

<!-- formula-not-decoded -->

S0, the response is the convolution of the response of one system and the impulse of the other . response step step

- 6.31 (Solution)

<!-- formula-not-decoded -->

Outputs are not identical because systems are not LTI (the compression system is time varying).

- 6.32 (Solution)

<!-- formula-not-decoded -->

Outputs are not identical because systems are not LTI (the squaring system is nonlinear) .

## 6.33 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Outputs are identical because both systems are LTI

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) We find h12(t) = h21(t) because both systems are LTI
- (e) The parallel connection of h (t) and h12(t) must equal 8(t). ~e-tu(t) +te-'u(t)
- 6.35 (Solution)

- (b) y(t) =
- (c) One system is the inverse of the other because h1(t) * h2(t) = 8(t)

<!-- formula-not-decoded -->

## 6.36 (Solution) Refer to the circuits shown.

<!-- image -->

- (a)

<!-- formula-not-decoded -->

Tbis does not equal h (t) for the physical cascade because an ideal cascade assumes an infinite input impedance for tbe second system. If not, we have an impedance mismatch which causes buffer amplifiers between the two systems.

- (c) At t = 0,h12(0) = 2 and h3(0) = (0.99)} The larger the value of R; the less the difference between h12(0) and h3(0)

## 6.37 (Solution)

- (a) h(t) = e-(t+1)u(t) Causal and stable
- (b) h(t) = e-t-Ju(t+1) Noncausal and stable
- (c) h(t) = 8(t) - e-tu(t) Causal and stable
- Noncausal and stable
- 6.38 (Solution) Let hP(t) be the impulse response of the parallel combination and hc(t) be the cascaded impulse response.
- hP is causal, stable; hc is causal; stable
- hP is noncausal; stable; hc is causal , stable
- (c) h1(t) = e-'u(t) h2(t) = e-t+2u(t \_ 1)
- (d) h1(t) = e-tu(t) h2(t) = e'u(-t) hP is noncausal, stable; hc is noncausal, stable
- (e) h1(t) h2(t) hP is noncausal; stable; hc is noncausal , stable =e-ltl
- (f) h1(t) = eltl , h2(t) = hpP is noncausal, unstable; hc does not exist e-Jt-1}
- (g) h1(t) = elt-lI, h2(t) = hp is noncausal, unstable; hc does not exist

## 6.39 (Solution)

- (a) y(t) = z(t)
- stable for œ &gt; 0 because h(t) =
- (c) y(n)(t) = 2(t) unstable for n &gt; 1, since h(t) will be a step (J 8(t)) for n = 1 OI &amp; polynomial
- (d) y(t) = unstable for any n 2 1, since h(t) will be &amp;(t) for n = 1 OI 6(n)(t) for n 2 1. These derivatives of the impulse are not absolutely integrable.  Alternatively; a step input (bounded) will yield impulses (n = 1) Or tbeir derivatives (n &gt; t =

## 6.40 (Solution)

- (1) h1(t) = 28(t) y1(t) = z(t) * 28(t) = 22(t) = 2[u(t) - u(t \_ 1)]

- (b) The statement applies only to instantaneous systems.
- (c) System 1 is instantaneous. Its system equation y(t) = 2z(t) System 2 is dynamic because y(t) = 3) tbe arguments of the input and output do not match t 3. System 3 is
- (d) For an instantaneous system; h(t) must have the form Kf(t) (and not K'(t œ) for example).

## 6.41 (Solution)

- (a) rect(t) * tri(t) Convolution is smoother and longer in duration
- Convolution has same duration and form as rect(t).
- (c) rect(t) * &amp;  (t) Convolution is derivative of rect(t) and less smooth!
- (d) sinc(t) * sinc(t) Convolution equals sinc(t) and shows no smoothing: y(t) = 4 Convolution has the same (Gaussian) form but is more stretched out.
- (e) sin(2rt) * rect(t) Convolution is zero. As we slide the folded rect pulse; the product over one unit (the period of the sine) integrates to zero.

## 6.42 (Solution)

- (a) z(t) = cos(t), y(t) = Tbis describes a linear system; tbe response is at the input frequency:
- (b) z(t) = cos(t), y(t) = cos(2t) Tbis is a nonlinear system; the response is not at the input frequency.

## 6.43 (Solution)

- (b) Itue. Example: ete-tu(t) = ejxe-(t-=l) d = e(1+j) dX = = Keit is an 0 =c 1+j eigensignal of any LTI system such as that described by the impulse response h(t) =e-Btu(t). e-t
- (c) Only in special cases will A (or 0) equal zero.
- (d) Itue. Examples sinc(t) * sinc(t) = sinc(t) sinc(t) * sinc(2t) = 0.5sinc(t)

## (b) Yes (c) No (d) No

- 6.45 (Solution) For stability Jh(t)ldt must be finite. For causality; h(t) = 0, t &lt; 0 (a) h(t) = u(t) Unstable, causal
- (b) h(t) = e-2u(t) Stable, causal
- (c) h(t) = 8(t \_ 1) Stable; causal
- (d) h(t) = rect(t) Stable, noncausal
- (e) h(t) = sinc(t) Unstable (sinc is not absolutely integrable), noncausal
- (f) h(t) = sinc? (t) Stable( J sinc? (t)dt = 1), noncausal

## 6.46 (Solution)

- (a) h(t) = e-2u(t)

- (c) h(t) = sinc(t) Not invertible. Different inputs can produce identical outputs. For example; sinc(t) * sinc(t) = sinc(t) and sinc(t) * 2sinc(2t) = sinc(t)

6.47 (Solution) (a) 2(t) = 0 &lt;t &lt;T 0 1 (b) I(t) = te-t/7u(t) 0 &lt;t &lt;T ~ Equating the two results and comparing the coefficients of  and +2 have S0, we

<!-- formula-not-decoded -->

- 6.48 (Solution) Refer to tbe following sketches.
- u(t = 2)] As we fold and slide the sine pulse; the convolution after 2 units is the area under the sine and equals 0 S0 the convolution duration is 2 units. (2) rect(t)* cos(2ut)u(t) . As we fold and slide the rectangular pulse; the convolution after 1 unit pulse
- is the area under cos(2ut) over one unit and equals 0. S0 the convolution duration is 1 unit.
- (b) After Ta units, the convolution the area under z(t) = 0 equals
- (c) After 1 unit; tbe convolution the area under Ip(t) = 0 equals

<!-- image -->

## 6,49 (Solution) Use the area property of convolution.

- =

<!-- formula-not-decoded -->

- So,

<!-- formula-not-decoded -->

- (c) = is 1. The area of *e-rt? e~Tt? e~Tt?
- 1 A (d) The area of is T and tbe area of 1+t2 1 + (2)2 1+(27 1 + t?

## 6.50 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Now y(t) = z(t) * h(t) = tri(t). Since y(t) is even; we compute

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 6.51 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- Ke-a(-n)? = (t =n) n!

<!-- formula-not-decoded -->

- 0 (d) From the area property; Jo hn(t)dt = 1 Ihe area of gn(t) must also unity  Since shifting does not change areas; we use equal

<!-- formula-not-decoded -->

- 6.52 (Solution) Refer to the following sketches
- (a)
- (b) The response y(t) is y(t) = z(t) * h(t) = tri(t \_ 2)
- (c) The response y(t) is maximum at t = tm = 2 5. This also corresponds to the time d by which the signal s(t) is delayed to obtain z(t)

<!-- image -->

- 6.53 (Solution) An autocorrelation function must be a non-negative; even symmetric function with a maximum at the origin.
- Tzz (t) = Can be an autocorrelation function
- ~atu(t) Canpot be an autocorrelation function (not even symmetric).
- Tzz(t) = te-œtu(t)
- Tzz(t) = '(at) Can be an autocorrelation function
- Trr(t) = Cannot be an autocorrelation function (not maximum at origin)
- 1 (f) Tzz(t)
- = Can be an autocorrelation function 1+t2
- = Cannot be an autocorrelation function (not even symmetric).
- 1 (b) Tzz(t) = Can be an autocorrelation function 4+t2 4t2
- 1+t2
- t2 \_ 1 (i) rzz(t) = Cannot be an autocorrelation function (not non-negative) t2 + 4

## 6.54 (Solution)

- Tzh(t) = e-'u(t)*e-tu(t) =te-tu(t) and Thz(t) = ~te'u(-t) 8 Txh = Thz(t) ~tu(t) = te'u(-t) (Prob 6.28a) Tzh(t) = Tzh(-t)

## COMPUTATION AND DESIGN

- 6.55 (Solution) Use ctcongui to animate the convolution. Tbe result shown is tbe partial convolution for part (d).

<!-- image -->

6.56 (Solution) Use ctcongui to animate the convolution.

<!-- image -->

- 7.1 (Solution)
- 7.2 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## DISCRETE CONVOLUTION

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 7.3 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- h[n] = {8,4,2,0} Both z[n] and h[n] start at n = 0, so y[n] starts at n = 0

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- {4,0,2,0,3,0,2} Both z[n] and h[n] are zero interpolated versions of part(d), 50

<!-- formula-not-decoded -->

- (f) zn] =

(ignore leading zeros),h[n] starts at n = ~1, s0 y[n] starts at n = 2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 7.4 (Solution) r[n] = h[n] = {8,4,2,1}

- š} (folding property) 24,

- 22, 12, 4, 1} 28,

- 7.5 (Solution) z[n] = h[n] = {ž,6,0,4}.
- (a) y[n] = z[2n] * h[2n] =
- (b) g[n] = 2[n/2] * h[n/2}. Now, z[n/2] = h[n] =

- z[n] * h[n/2] = {4, 20, 36,50, 34,28, 28,20, 16,8} So,

## 7.6 (Solution)

- (c) The response of this system to {1,2,3,4,5} is
- (d) The system perform the required averaging operation. The first and last samples of z[n] are averaged with zero. does

| Index n   |     |     | 2   | 3   |     | 5   |
|-----------|-----|-----|-----|-----|-----|-----|
| I         |     | 2   | 3   |     | 5   |     |
| h         | 0.5 | 0.5 |     |     |     |     |
| 0.5       | 1.0 |     | 1.5 | 2.0 | 2.5 |     |
|           |     | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 |
|           | 0.5 | 1.5 | 2.5 | 3.5 | 4.5 | 2.5 |

## 7.7 (Solution)

- (a) h[n] = (2)"u[n ~ 1]- Causal but unstable

- (e) h[n] = (0.5)-nu[-n]. Noncausal and stable (folded version of (0.5)"u[n]).

- 7.8 (Solution) We use wrap-around to fnd the periodic convolution in each case.

- Periodic convolution = (N =4)
- 'b) z[n] =
- h[n] = Regular convolution y[n] = z[n] * h[n] = {0,12,32,56,32,12,0} Periodic convolution yp[n] = {0,12,32, 56} + {32,12,0,0} = {32,24,32,56} (N = 4) Now, Nr = Nh = 4 and Ny = 7. So,

(N = 5)

- h[n] = {4,3,2,0,0} Regular convolution y[n] = {~12,-17,~ Now, Nz = Nn = 5 and Ny = 9. So, the minimum number of padded zeros is 9 \_ 5 = 4.

(d) z[n] = {3,2,é,1,2} #{n] = {4,2,3,2,0} Regular convolution y[n} = {12,14,17,18,17,9,8,4,0} Periodic convolution = yp[n] = {12,14,17,18,17} + {9,8,4,0,0} = {21,22,21,18,17} (N = 5) Now, Nz = Nh = 5 and Ny = 9. S0, the minimum number of padded zeros ís 9 \_ 5 = 4.

- 7.9 (Solution)

circulant matrix for z[n], we find Using

- h[n] = {2,2,3,0}

<!-- formula-not-decoded -->

As &amp; sequence; yp[n] = {4,9,7,8}

- (b) z[n] = {8,2,4,6} h[n] = {8,4,2,0} Using

<!-- formula-not-decoded -->

As a sequence; yp[n] = {32,24,32, 56}

- 7.10 (Solution) c[n] = {8,3,9,12,15,18}

<!-- formula-not-decoded -->

Except for end effects; the output describes a interpolation between the samples of z[n]step

- {8,0,0,3,0,0,9,0,0,12,0,0,15,0,0,18,0,0} y[n] = z[n/3] * h[n] = {*,0,0,3,3,3,9,9,9,12,12,12,15,15,15,18,18,18,0,0} So,
- Except for end efects, the output describes a interpolation between the samples of z[n]step
- (c) For step interpolation by 4, we require N = 4 and h[n] =

## 7.11 (Solution) z[n] =

<!-- formula-not-decoded -->

- (a) hn] = tri(n/2) = {0,0.5,1,0.5,0} With N = 2, 2[n/2] = y[n] z[n/2] * h[n] = {0,0,9,1.5,3,6,9,10.5,12,13.5,15,16.5,18,9,0,0} Except for end efects, tbe output describes a interpolation between the samples of z[n] So, step
- {8,0,0,3,0,0,9,0,0,12,0,0,15,0,0,18,0,0} y[n] = z[n/3] * h[n] = {0,0,0,8,1,2,3,5,7,9,10,11,12,13,14,15,16,17,18,12,6,0,0,0}
- Except for end effects, the output describes a interpolation between the samples of z[n] step
- (c) For linear interpolation by 4, we require N = 4 and h[n] = tri(n/4)

## 7.12 (Solutiop)

- (a) z[n] = {í,2,0,1}, h[n] = {2,2,3}

<!-- formula-not-decoded -->

- (e)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- Since z[~n] starts at n = ~5 and z[n] at n = 0, their convolution starts 8t n = -5, 50

<!-- formula-not-decoded -->

- Since h[n} and h[~n] are even symmetric; we get Thh[n] =
- Now, z[n] starts at n = 0, and h[-n] at n = ~2, their convolution starts at n = -2, 50 {0,0,8,1,2,3,3,3,2,1}
- {1,1,1,0,0,8} * Thz[n] = {1,2,3,3,3,2, 1,8,0,0}

7.14 (Solution) Use convolution and wraparound. See Problem 7.12 for intermediate results. regular

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 7.15 (Solution)

- cos[0.25 (n

## 7.16 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 7.18 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

0 = 2K - 2 or K = 1 or y[n] = (n + 1)(0.5)"u[n] get

- (e) The outputs of parts (b) and (c) are identical Botb describe tbe zero-state response

## 7.17 (Solution)

- 7.19 (Solution) Assume that both convolved sequences start at n = 0
- (c) {2, 2} * {1, 1} = {2,4,2} (even symmetric about n = 1)

- (f) {2, ~2} * {1, ~1} = {2,~4,2} (even symmetric about n = 1)
- ~1} = {2,1,0, -1,2} (odd symmetric about n = 2)

- (i) {2, 2} * {1, ~1} = {2,0,~2} (odd symmetric about n = 1)
- 7.20 (Solution) z[n] = {ž,4,6,8}

- (c) z[n/2] = {ž,0,4,0,6,0,8,0} (zero interpolation).

y2 {n] = lated version of y[n]) . So,

- (d) z[n/2] = {2,2,4,4,6,6,8,8} (step interpolation)

<!-- formula-not-decoded -->

y3 [n] z[n/2] * z[n/2] = {4,12,25,44, 70, 104, 147,180, 196,185, 160, 120, 64, 16} (ya[n} So; 194,

- {ž,3,4,5,6, 7,8,4} (linear interpolation) not related to

- 7.21 (Solution) z[n] UP-SAMPLE (zero-interpolate) by N Filter y[n} (a) For interpolation by a factor of N, we require h[n] = tri(n/N) linear

<!-- formula-not-decoded -->

- (c) For N = 2, we have h[n] = tri(n/2) = {0,0.5,

Ibe zero interpolated input is æ[n/2] = {0,0,1,0,2,0,3,0,4,0,3,0,2,0,1,0,0,0}. The output is y[n] =

- 7.22 (Solution) If h[n] has tbe form h[nJu[n], we may write

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

If z[n] starts at n =

<!-- formula-not-decoded -->

Thus, the response also starts at n = no.

## 7.23 (Solution)

- (a) Let z(t) = h(t) = rect(t/2). y(t) = 2tri(t/2) and y(kts) = {0,0.5,1,1.5,2,1.5,1,0.5,0} So,

(b) z[n] = h[n] = {1,1,,1,1,1} So, y[n] = z[n] * h[n] = {1,2,3,4,5,4,3,2,1} yR(nts) = tsy[n] = {0.5,1,1.5,2,2.5,2,1.5,1,0.5} This does not match the exact result y(kts) because t, is not small enough and the sample value at the jumps is ambiguous (chosen as 1) So,

- (c) Using the sum by column method, we have

<!-- formula-not-decoded -->

0.5 1 2 3 4 3 2 0.5 trapezoidal rule) (by

- (b)
- (c) Generalizing; we have rect(n /2N) * rect(n /2N) = (2N + 1)tri

## 7.25 (Solution)

- (c) For the parallel connection; hp = hF + hB = (stable and noncausal) .
- (stable and noncausal) .

= {0.25,0.5,1,1.5,2,1.5,1,0.5,0.25} . This matches y(kts) exactly (except at tbe end points) The likely source of error is the ambiguity in the sample values at the jumps.

- The sum by column metbod gives:

<!-- formula-not-decoded -->

yr(nts) = {0,0.25,1,1.75, 2,1.75, 1,0.25,0} The trapezoidal rule will yield a better approximation.

- 7.24 (Solution) z[n] = rect(n/2) = h[n] = rect(n/4) =
- g[n] = h[n] * h[n] = {1,2,3,4, 5,4, 3,2,1}

## 7.26 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 7.27 (Solution)

- Does not qualify as an eigensignal
- Qualifies as an eigensignal =e-jnt/2
- Does not qualify as an eigensignal
- (d) z[n] = cos(nr/2) Does not qualify as an eigensignal
- (e) z[n] = j" = Qualifies as an eigensignal ejnz/2
- ~n Does not qualify as an eigensignal

- 1] h2[n] = (a) For the two systems in parallel with œ = 0.5, hP[n] =
- (b) For the two systems in parallel with œ = -0.5, hP[n] =
- (c) ~
- (d) 1]
- 7.29 (Solution) Refer to tbe figure: The difference equation of the two subsystems is y1[n] = œy1[n - 1] + ~
- (a) The impulse response of the overall system is h[n] 1] This is an IIR filter.
- (b) If œ = ß, we find h[n] = œ"u[n] 1] This is an IIR filter.
- represents an identity system (whose input and output are equal) .
- 7.30 (Solution) hz[n] Tbis does not equal the convolution of the individual = u[n] * h1[n] and s2[n] = step S0,
- 7.31 (Solution) Given that System 1 is a squaring circuit and System 2 is an exponential averager with h[n] = Find the output of each cascaded combination. Will their output be identical? Should it be? Explain.

Figure P7.29. System realization for Problem 7.29

<!-- image -->

<!-- formula-not-decoded -->

- y[n] = (n + 1)2(0.25)"u[n} So,

The two outputs are not and the order of cascading matters because the systems are not LTI (the squaring circuit is nonlinear) . equal

- (a) 2(0.5)"u[n] 4(0.5)2n = 4(0.25)" .

<!-- formula-not-decoded -->

The two outputs are equal.  The order of cascading does not matters because both systems are LII

- = =
- 7.33 (Solution) y[n} = 0.5y[n 1] + z[n] So, h[n] = (a) The impulse response in parallel: h P[n]
- (0.5)"u[n] - (n + 1)(0.5)"u[n]
- (0.5)"u[n] = (n + 1)(0.5)"u[n]
- (d) Yes, h12[n] and h21[n] are identical (because both systems are LII).

<!-- formula-not-decoded -->

- (b) y[n] = S[n] * (0.5)"u[n] * h[n] = (0.5)"u[n] * (6[n] ~ 0.58[n 1]) y[n] = (0.5)"u[n] ~ So,
- (c) One system is the inverse of the other (tbe output of the cascaded system equals the input).

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- So, y[n] = z[n] * hpe[n] = 26 {128,128,96,64,24,8,2} and yp[n] = 26 {152,136,98,64}

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 7.37 (Solution)

- (a) zn] = (c)"u[n] (lal &lt; 1)

<!-- formula-not-decoded -->

For n 2 0, u[kJu[k \_ n] is zero for k &lt; n, so

<!-- formula-not-decoded -->

(all n)

<!-- formula-not-decoded -->

For n 2 0, v[kJu[k ~

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For n &lt; 0; u[kJu[k n] is zero for k &lt; 0 and

<!-- formula-not-decoded -->

- = rect(n/2N) = rect(n/2N)

The correlation of z[n] and h[n] is also their convolution; because both are even symmetric. Thus (2N + 1)tri

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## COMPUTATION AND DESIGN

```
7.39 (Solution) yn] 0.By[n h[n] = (0.8)"u{n] 'PROBLEN 7.39 Uses the ADSP routine dtplot h='0.8 ht=' (0.8 '20 term truncation n=0:15;x=ones(size(n)) ; pause n=0: 30;x=ones(size(n)); ) , pause n=0 ) ,pause 'PARI (b) y-filter(eval(h),1,x);ylsfilter(eval(ht),1,x) ;dtplot(,y-yl, ') pause n=0
```

## 7.40 (Solution) Uses the ADSP routine dtplot

```
'PROBLEM 7 .40 n=-10:10;ny=-20:20; 'Part (a) subplot (2,2,1) ,dtplot subplot (2,2,2) ,dtplot (n,b, subplot(2,1,2) ,dtplot(ny,, ,pause 'Part (b) subplot (2,2,1) ,dtplot (n,x, subplot (2,1,2) ,dtplot= ) ,pause 'Part (c) subplot (2,2,1) ,dtplot (n,x, subplot (2,2,2) ,dtplot (n,b, subplot (2,1,2) ,dtplot (ny,Y ,Pause 'Part (d) subplot (2,2,1) ,dtplot(n,X, subplot (2,2,2) ,dtplot (2,b, (ny,y,
```

```
7.41 (Solution) Uses the ADSP routines dtplot _ randist, corrp 'PRDBLEM 7 .41 'PARI (a) uni' ,0) ; rsscorrp(s,s); dtplot ') ,axis( [0 60 ~inf inf]) 'PARI (b) rx-corrp(x,x) ; dtplot (n,rx, ') ,axis( [0 60 -inf inf]), pause 'PART (c-d) rem(n,N) ; y=corrp(s,imp)#N/M; % Normalizing factor is N/M (n,rs pause
```

## FOURIER SERIES

- 8.1 (Solution) Onesided

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Ftequencies present: 2 Hz and 8 Fundamental frequency fo = GCD(2,8) = 2 Hz Hz, harmonics present: k = 1 (fundamental), and k = 4 (4th harmonic) So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Frequencies present: 3 Hz and 9 Hz. fundamental frequency fo GCD(3,9) = 3 Hz So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

Exponential form: r(t) = 2+ ZejBrt

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Frequencies present: 4 Hz and 6 Hz. So, fundamental frequency fo = GCD(4,6) = 2 Hz

So; harmonics present: k = 2 (2nd harmonic) and k = 3 (3rd harmonic)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Ftequencies present: [1,2,3,4] rad/s. So, fundamental frequency wo GCD(1, 2,3,4) = 1 rad /s So, harmonics present; k = [1,2,3,4} (fundamental thru 4th harmonic)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (a) fo = 800 Hz and T = = 1.25 ms.
- (b) = = 0, Ck = = 0 and X[k] = :sin?(4).
- (c) Zero dc offset and X[k] =0 fOr even k, 50 z(t) has half-wave symmetry. The X[k] are purely (t) also has even symmetry.
- 6 8.3 (Solution) Consider tbe periodic signal z(t) =
- (a) fo = 50 Hz and T = % = 20 ms\_

<!-- formula-not-decoded -->

- Also, So,
- (c) Zero dc ofset and ck 0 for even k. z(t) is half-wave symmetric. So;

<!-- formula-not-decoded -->

- 8.4 (Solution) Refer to the following figures:

<!-- image -->

<!-- formula-not-decoded -->

- = 2u fo = T Since z(t) = u(t) ~ get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 8.5 (Solution) Refer to the spectra.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## For Signal 1:

- (a) Ftequencies present: 90, 150, 210 Hz. fo = GCD(90,150,210) = 30 Hz. Harmonics present: k = 3, 5, 7 So,
- (b) Nonzero dc value: Only odd harmonics. Harmonic phase = 490" (so only sine terms) . S0 hidden odd symmetry and hidden half-wave symmetry.
- (c) 909)
- Irms = = = 3.39

<!-- formula-not-decoded -->

## For Signal 2:

- (a) Frequencies present: 10, 20, 40 Hz. fo = GCD(10,20,40) = 10 Hz. So;

- (b) Zero dc value (a = 0). Harmonic = S0 only cosines. S0 even symmetry. phase
- 8 cos(4Ont)
- (d) Signal power P = 0.5[42 + 82 + 42] = 48 Irms = = 6.93
- 8.6 (Solution) Refer to the following sketches
- (a) Even symmetric about T/2.
- (b) Odd symmetric about T/4.
- (c) Even symmetric about T/2 and odd symmetric about Tl4.
- (d) Odd symmetric about T/2 and even symmetric about Tl4.

<!-- image -->

## 8.7 (Solution) Refer to the sketches.

Figure P8.7. The periodic signals for Problem 8.7.

<!-- image -->

- (a) z(t) has even symmetry. So bk = 0. Now, T = 4, Wo =

## (Signal 1)

<!-- formula-not-decoded -->

The second term is zero (integral of odd function between symmetric limits)

<!-- formula-not-decoded -->

4sinc(0. The dc value is 0 and al odd harmonics are absent\_

- (b) Power in the fundamental (k = 1) is P1 = = 3.2423 W
- (d) Total power (from z(t)): P = energy in 1 period/T = 32/4 = 8 W
- (e) Tbe convergence rate is 1/k (and the Gibbs effect will be present) .

- (Signal 2) (a) z(t) has odd symmetry. So a0
- =@k =

<!-- formula-not-decoded -->

- (b) Power in the fundamental (k = 1) is Pi = 0.562 = 1.441 W
- (d) Total power (from r(t)): P = energy in 1 period/T = 16/4 = 4 W
- (e) Tbe convergence rate is 1/k2 (and the Gibbs effect will be absent) .

## (Signal 3)

<!-- formula-not-decoded -->

- = 0. Now, T = 4, = 0.57 Wo

<!-- formula-not-decoded -->

- (b) Power in the fundamental (k = 1) is P1 = 0.50{ = 1.314 W
- (c)
- (d) 32 = 10.6667 W
- (e) The convergence rate is 1/k2 (and the Gibbs effect will be absent) .
- (Signal 4)

<!-- formula-not-decoded -->

- =0.5t

- (c)
- (d) Total power (from 2(t)): P = energy in 1 period/T = ! W
- (e) The convergence rate is 1/k (and the Gibbs effect will be present) .

## (Signal 6)

- (a) I(t) bas even symmetry bk = = So, Wo

<!-- formula-not-decoded -->

- = = 3.9958 W (ak = 0, k = 3,5, 7, . .
- (d) Total power (from z(t)): P = energy in 1 period/T = 16/4 = 4 W
- (e) The convergence rate is (and the Gibbs effect will be absent) . 1/k2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- =
- (d) Total power (from z(t)): P = energy in 1 period/T = ; W
- (e) The convergence rate is 1/k (and the Gibbs efect will be present)

(Signal 5) (a) z(t) bas odd symmetry. =ak =0. Now, T = 4, Wo = So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 8.8 (Solution) Refer to the sketches for magnitude and spectra. phase

~180

- (a)
- (b) For 2(2t): Signal compression doubles the fundamental frequency to 2Hz. Spectral coefficients do not change. Their frequency spacing doubles.
- U): No change in fundamental frequency or magnitude spectrum

Original phase is augmented by ~kuoto = 4 = ~60k"\_

<!-- formula-not-decoded -->

- (d) Since % (t) jkwo X[k], there is no change in fundamental frequency (so fo = 1 Hz) Tbe original phase is augmented by 90" for all k.

Tbe magnitude spectrum is scaled by = = kwo

## 8.9 (Solution)

- (a) f(t) = 2(2t): The coeffcients F{k] equal X[k} but the fundamental frequency and the frequency spacing of the spectra is doubled.
- = 0.5ak j0.5bk. G[k] = the ak Iemain unchanged, but the bk change sign. Also,
- (c) and the frequency spacing of the spectra is doubled.
- equal X[k} k # 0 but the fundamental frequency and the frequency spacing of tbe spectra is doubled.

<!-- image -->

## 8.10 (Solution)

- (a) Refer to the sketch.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) Refer to the sketch.

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) Refer to the sketch.

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) Refer to the sketch.

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 8.11 (Solution) Refer to the following figure for Problems 8.1l-8.14
- (a) Convergence rate is No Gibbs effect. Time period T = 2 1/k2.
- 8.12 (Solution) Refer to the figure for Problem 8.11
- (b) T=2 Fourier series converges to 3 at t = 0, 6 at t = 0.25T and 3 at t = 0.5T .
- Refer to the figure for Problem 8.11
- (a) Convergence rate is 1/k. Gibbs effect is present. Peak overshoot = 99 of jump. (at t = 0: (0.09)(12), at t = 0.5 and t = 1.5: (0.09) (6)
- (b) T =2 Fourier series converges to 0 at t =0, 3 at t = 0.25T and 0 at t = O.5T.

<!-- image -->

## 8.14 (Solution) Refer to the figure for Problem 8.11

- (a) Convergence rate is 1/k. Gibbs efect is present. Peak overshoot = 99 of jump. (at t = 0: (0.09)(4), (0.09)(4/e).
- (b) T=2 Fourier series converges to 2 at t = 0, 4/ve at t = 0.25T and 2/e at t = 0.5T.
- 8.15 (Solution) Tbe spectra for parts (a) and (b) are shown in the following figure:
- (b) Upon modulation by cos(16OOnt), the spectrum of æ(t) is shifted by +800 summed and amplitude scaled by 0.5. Hz,
- (from spectrum) = 3? + 2[(0.5)2 + 22 + 12] = 19.5

<!-- image -->

<!-- formula-not-decoded -->

- (a) Refer to the following sketch. The output is just the dc component and thus y(t) = 2

<!-- image -->

- (b) Refer to the following sketch. Tbe flter passes components at 4250 Hz,
- (c) Refer to the following sketch. The filter passes dc and 4250 Hz.
- 8.17 (Solution)

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

We have fo 800 Hz and a0 = 2. Only odd barmonics are present with 01 =6 (at 800 Hz); 03 = 2 (at 2400 Hz) and @5 =1.2 (at 4000 Hz) . The transfer function of the RC filter is H(f) = where T = 0.001 s

- (a) Refer to the figure. The ideal filter blocks all frequencies past 200 Hz. Only the dc component is passed . S0, y(t) = 2
- (b) Refer to the fgure. The ideal filter passes only frequencies between 200 and 2 kHz. Only the fundamental shows up. = The output of the RC filter is So,

<!-- image -->

<!-- formula-not-decoded -->

0. 00027)]

<!-- image -->

- (c) Refer to the figure. The ideal filter blocks all frequencies 2 kHz. So, the dc component and the fundamental are passed. From the results of parts (a) and (b), y(t) = 2+1.17 cos[16007(t 0.00027)] past

027

<!-- image -->

- 8.18 (Solution) Refer to the circuits sbown. z(t) = |10sin(t) | volts.
- (Circuit 1) Vo = 0.5Vin
- (a) co and Ck for z(t) have been already listed.
- (b) The dc component of tbe output is 0.5co 9 = 3.183.
- (c) Tbe fundamental component of the output is y1(t) = 0.5c1 cos(wot) = 29 cos(2t).
- (d) The power in y(t) thru k = 2 is P2 = (0.5c0)2 + 0.5[(0.5c1)2 + (0.5c2)2] = 9.4955 W.
- (Circuit 2) H(w) =
- (a) c and ck for z(t) have been already listed .
- (b) Tbe dc component of the output is co = 2 6.366.
- (c) The phasor output for k = 1 is Yi = = 1.898/116.60

<!-- image -->

<!-- formula-not-decoded -->

- C2 (d) Tbe phasor magnitude for k = 2 is 0.2059

<!-- formula-not-decoded -->

- (a) co and ck for 2(t) have been already listed.
- (b) The dc component of the output is zero
- j2c1 (c) The pbasor output for k = 1 is Yi = 3.7961 2 1+j2 y1(t) = 3.7961 cos(2t S0,
- j4c2 (d) Tbe phasor magnitude for k = 2 is |Y2l = = 0.8235 1+j4 S0, Pz = 0.5[(3.7961)2 + (0.8235)2] = 7.5441 W.
- (Circuit 4) H(w) = S0 the results are identical to those for circuit 1. 1+j2k
- (Circuit 5) H() = 2 + jut 2 + j2k
- (a) co and ck for z(t) have been already listed.
- (b) The dc component of the output is 0.5co 3.183 .
- C1 (c) = 2+ j2 So,
- (d)
- The phasor magnitude for k = 2 is lYzl = = 0.1898 2 + j4 S0, P2 (0.5co)2 + 0.5[(1.5)2 + (0.1898)2] = 11.276 W.

<!-- formula-not-decoded -->

- (a) co and ck for z(t) have been already listed.
- (b) The dc component of the output is zero.
- j2c1 (c) Tbe phasor output for k = 1 is Yi = = 2.0587 2 165.960 1+j4 S0, y1(t) = 2.0587 cos(2t
- j4c2 (d) The phasor magnitude for k = 2 is [Yzl = = 0.4211 1+j8 S0, Pz = 0.5[(2.0587)2 + (0.4211)2] = 2.2078 W.

- (a) Third harmonic distortion c3/c1 in output = 2/10 = 209.

<!-- formula-not-decoded -->

- (a) dc output = 0
- (b) Harmonics present: fundamental and third
- (c) Third harmonic distortion c3/c1 = = 33.339
- (d) Total harmonic distortion third harmonic distortion because only third harmonic is present.

## 8.21 (Solution) Refer to the sketches shown.

<!-- image -->

Vín Vin For an RC circuit, Vc = = 1 + jwt 1 + jkuot

<!-- formula-not-decoded -->

Tbe output is thus an integrated version of the input and appears as a triangular wave (with zero dc ofset) and amplitude scaled by 1/1OOT.

<!-- formula-not-decoded -->

The output thus resembles the input and appears as a near square wave.

## 8.22 (Solution) Refer to the sketches .

<!-- image -->

Assume a symmetric triangular wave with peak value of unity.

2 0.02s, s0 fundamental frequency of input =

Fundamental frequency of rectifed output = IOOHz

- 0.25 sin(6nfot)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

With w = So,

## 8.23 (Design) Refer to the sketches

<!-- image -->

1 = = 0.5, @k = 7 T(1 ~

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

With wo

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

So, ak = Qk cos(kwoto) and bk = sin(kwoto)

## 8.25 (Solution) Refer to the sketches.

<!-- image -->

- = 0 and with T = 4 and wo =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

the FS coefficients of z(t) are

<!-- formula-not-decoded -->

- = 0.5 and T =4 and Wo = 0.51. So,

<!-- formula-not-decoded -->

Since r(t) = y(t + 1) the results of Problem 8.24 with t0 = 1 give the FS coeffcients of z(t):

<!-- formula-not-decoded -->

- 8.26 (Solution) Refer to the sketch below. bk = T Integration is over = At and =At = 12t or A = 12. So,
- 8.27 (Solution) 12t cos(0.5kut)dt (k odd)

<!-- image -->

<!-- image -->

We have T = 4..Integration is over (0, 0.25T). S0, z(t)

- 8.28 (Solution) P5.13: Solution

See the sketches.

<!-- image -->

s(t) = = With T =1 0.lsinc(0.1k) Now, S[k] = 0 for k = 410,+20, (every 10 harmonics) Tbe nulls are thus 1Of (0.01 MHz) apart.

The modulated signal is the sinc function displaced by 4l MHz.There are 100 nulls (99 sidelobes) before the peak on either side of the origin.

<!-- image -->

- (a) y(t) = S0, a0 = @k = 4k2)]. Harmonics present are kfa where fo = 10 Hz.
- (b) Third harmonic distortion = PIP = = 209 4/37 Total harmonic distortion = Total harmonic distortion V(Pr P)TP = 22.739 Now,

## 8.30 (Solution) = =

<!-- image -->

- (a) The output y(t) is a square wave with bk = (k odd) So only odd harmonics (of fo = 5 Hz) are present in y(t) \_
- = 33.339 The total barmonic distortion is V(Pr = P)TP = 0.8106, and 0.1894. THD = = 48.34%

<!-- formula-not-decoded -->

- y(t) =8 sin(8OOnt) + 2sin(1600t) Spectrum of x(t) Magnitude specuum of y(t) Phase spectrum of y(t) [deg]

(Hz)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

800

Magnitude spectrum of w(t) Phase spectrum of w(t) [deg]

<!-- image -->

<!-- image -->

X[k] = {2,2,2} with spacing 800 Hz and Y[k] = {j,j4,8,-j4,-j} with spacing 400 Hz

- 9,0,-j2} with spacing 400 Hz. So, z(t) = Magnitude spectrum of z(t) Phase spcctrum [deg] of z(t) Time domain output z(t)
- 8.32 (Solution) Since 2(t) = I(-t) we bave even symmetry Witb k &lt; 3 and T = 2, we have z(t)

<!-- image -->

<!-- image -->

<!-- image -->

= @1 cos(at)

Since P = 0.5a2 = 4, we find a1

- 8.33 (Solution) Since fo = = 10 Hz and the ideal lowpass filter blocks all frequencies 15 Hz, y(t) =a0 + @1 past

Since yav

= = =

Since P = =

- 8.34 (Solution) Tbe system describes an RC circuit (with T = 1) and its transfer function is 1/(1+j2ukfo)
- (a) Tbe input z(t) = rect(t) witb duty ratio 0.5 suggests even and hidden half-wave symmetry.
- (b) Tbe output y(t) will show only hidden half-wave symmetry.
- (c) Tbe dc output will equal the dc component of the input. The 2nd harmonic component of y(t) will be zero.
- (d) The FS coefficients of z(t) decay as 1/k. The transfer function has a 1/k dependence. the FS coefficients of y(t) will decay as the Gibbs effect wll be absent . S0, 1/k2 . So;

<!-- image -->

w/Qwo With wo = and = =

The FS coefficients of &amp; half-wave symmetric square wave pulse train have the form Alk, (k odd).

Tbe harmonics closest to k = 25 (ie. k = 23 or k = 27) will also produce largest outputs.

<!-- formula-not-decoded -->

Since we want to reject all but the resonant frequency we require Q 1 and 1 get

The specifications call for |Vl/IVol 0.05 and this gives ~ 130.

- 8.36 (Solution) For an RC circuit; Vc Vin Vin
- For a square wave with zero dc offset, Ck = 4/km, (k odd). So,

Vc = (k odd)

- ~j2 1+j So, Thus,
- (b) The half-power frequency at which the response 1/v@ times tbe maximum response re-= equals

<!-- formula-not-decoded -->

- (a) The convergence as 1/k, s0 the Gibbs effect is present.
- (b) z(t) converges to 2 at t = 0 (the terms in the summation equal
- (d) At t =0.25T = 0.5,

- 8.38 (Solution)
- Vc % Vin/k (for large k) If Vin % 1/k, then Vc % 1/k2, and the Gibbs effect is absent. So,
- VR % Vn

<!-- formula-not-decoded -->

- € =

<!-- formula-not-decoded -->

- 8.40 (Solution)   Refer to tbe sketches.
- (a) Sawtooth (unit beigbt) P = @k =

<!-- image -->

<!-- formula-not-decoded -->

- (b) Iriangular wave (unit beight) P =

<!-- formula-not-decoded -->

- (c) Full-rectifed sine (unit height) P =

<!-- formula-not-decoded -->

- =l, we get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 8.42 (Solution) rect(k/2N)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

tri(k /M)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- = 0.0521 erroI. So,

<!-- formula-not-decoded -->

- (e) Each different set of choices for t1 and t2 gives a different set of values for Ao and B1- There is no unique way to choose between them. For more harmonics; we include more constants. This means more equations (at more time instants) and more computation to evaluate the constants.
- (f) The constants are not independent of each other . Iheir values change if we change the time instants.  And the power error is never less than that obtained by choosing the constants as the Fourier series coefficients!

## 8.44 (Solution)

- (a) re(t)z (t)dt is an odd function integrated between symmetric limits and equals zero
- (b) Let z(t) = cos(2mt) and y(t) = cos(4mt). Are orthogonal over 0 &lt;t &lt;1. they

<!-- formula-not-decoded -->

- 1/4 (d) From (b), 0.5 cos(6nt) dt + 0.5
- = 0.5 and bk =

<!-- formula-not-decoded -->

## 8.45 (Solution)

<!-- formula-not-decoded -->

S0, set is not orthogonal

<!-- formula-not-decoded -->

0

te-t?

~0

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 8.46 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

dt =

O(odd function; between symmetric limits) , s0 the set is orthogonal.

- 8.47 (Solution) z(t) = te-t/2u(t)

<!-- formula-not-decoded -->

This is an orthonormal set with Eo = E1 = E2 = 1

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- t2e-'dt = 2 S0, zero error (i.e. tbe representation is exact)
- 8.48 (Solution) 2(t) = 12e ~ ~3tu(t)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

So, zero energy error (and an exact representation) . Energy

## COMPUTATION AND DESIGN

## 8.49 (Solution)

<!-- formula-not-decoded -->

```
'PARI () x=O;for end plot(t,x) You may also use fsgui (see following plot) or fssyngui.
```

<!-- image -->

## 8.50 (Solution)

```
'PROBLEM 8.50 'PART (a) for savtooth % Generate RHS matrix that multiplies X[k]
```

```
1bsst(:); % Generate LFS function array X=inv(rhs)*lhs;Xe=j./k/2/pi; 'exact FS coeffs are X[k]=j/(k*pi) 'with X [0]=0.5 disp(' Computed k=-M:M; ' Generate RHS matrix that multiplies X[k] % Generate LHS function array 'exact FS coeffs are disp(' Computed 'PARI (b) for tri(t) lbs-tri(t) 'exact FS coeffs are X[k]-0.Ssinc-2(k/2) disp(' Computed Exact ') ,disp( [X Xe(:)J) ,pause for 'exact FS coeffs are X[k]-0.Ssinc-2(k/2) disp(' Computed Exact') ,disp( [X Xe(:)]) ,pause (1,:
```

## 8.51 (Solution) the ADSP routine sinc\_ tri Uses

```
'PROBLEM 8 .51 'PART (a) for sawtooth T=1;N=6;ts=I/n;M=(N-1)/2; % Replace first value by average at jump X=[];for X= end disp(' Computed Exact' ) disp( [X Xe(:)]) ,pause % Replace first value by average at jump n=0:N-1 X=[I;sum (exp( end
```

```
disp(' Computed Exact' ) disp([X Xe(:)J) ,pause 'PART (b) for tri(t) T-2;=6;ts=I/n;M=(N-1)/2; X=[];for m=0:N-1 end 5*Xe disp(' Computed Exact' ) disp( [x Xe(:)J) ,pause X=[] ;for m=0:N-1 end disp(' Computed Exact' ) ([X Xe(:)J) #Xe; #Xe; disp
```

## THE FOURIER TRANSFORM

- 9.1 (Solution) Refer to the sketches .
- 9.2 (Solution) Refer to the sketches.

<!-- image -->

Figure P9.2. Figure for Problern 9.2.

<!-- image -->

- X(f) = 18sinc? (3f) - 2sinc?(f)
- 4tri[4 (t 2)] X(f) = [16sinc(4f) Ssinc?\_
- 3)] 4tri(t
- 3)] + 2tri(t \_ 3) X(f) = [24sinc(6f) 18sinc?(3f) + '(f)Je-j6zf 2sinc?(

## 9.3 (Solution) Refer to the sketches .

<!-- image -->

<!-- image -->

<!-- image -->

## from sketch)X(f) = 2sinc(2f)

<!-- image -->

- (e) z(t) = u(1 - |t {)sgn(t). Its sketch suggests superposition

<!-- image -->

X(f) = sinc(f)e-jrf sinc( f)eirf ~j2sin(&amp; f)sinc(f)

- (f) 2(t) = 0.Srect(0.5f)
- (g) z(t) = cos?(2rt) sin(27t)

(g)

(1/8)

(1/8)

(1/8)

(1/8)

1/2

12

<!-- formula-not-decoded -->

Note: We could also use modulation or trig identities and superposition.

<!-- image -->

- 9.4 (Solution)

<!-- image -->

X(f (radians)

<!-- image -->

- ~
- =

## 9.5 (Solution) z(t) = te-2u(t) 4 X(f)

- =

- ~2tu(t)
- (c) X'(f) =+ (~j2mt)te-2u(t)

- (f) X(f/2) 2(2t)e~2(20)u(2t) = Ate-4u(t) = T1(t)

- (h) (1 \_

## 9.6 (Solution)

- (a) Real signals have a real Fourier transform. Not true.
- (b) Two-sided signals have a two-sided Fourier transform. True.
- (c) Tbe Fourier transform of a real; even symmetric signal is a function of f2 . True

- 9.7 (Solution) Refer to tbe sketches for the amplitude spectra.
- =2 cos(2n f) (phase = 0)

<!-- image -->

<!-- formula-not-decoded -->

- ~ = = 90" ~ ej2rf e-j2 f

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9.8 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (e) X(f) = sinc(f/4) cos(2nf). Refer to the sketches.

<!-- image -->

<!-- image -->

Since 4rect(4t) 4 = 2rect[4(t 1)] + 2rect[4(t + 1)}

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 9.9 (Solution) Refer to the sketcbes for parts (a) and (b).

(a)

- (a) y(t) = rect(t/4) * rect(t/4) Y(f) = [Asinc(4f)]?

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9.10 (Solution) Refer to the sketches.

<!-- image -->

- So,

## 9.11 (Solution) Refer to the sketches.

<!-- image -->

9.12 (Solution) For a series RC circuit with T = 1,H(f)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Note: The input energy (for tbe impulse input) is infinite.

<!-- formula-not-decoded -->

## 9.13 (Solution) Refer to the sketches.

<!-- image -->

- 2 (d) z(t) = |sin(at)| fo = 1, X[0} = ? X[k] = #(1 S0,

## 9.14 (Solution) Refer to the sketches. The filter blocks frequencies past 5 Hz.

<!-- formula-not-decoded -->

<!-- image -->

<!-- image -->

Spectrum of input

A(2.5)

f(Hz)

Phasc (rad)

~0.64

f(Hz)

<!-- image -->

<!-- formula-not-decoded -->

<!-- image -->

## 9.15 (Solution)

<!-- image -->

- (a) h(t) = 8sinc[8(t 1)] Now, H(fo) =lL \_ T. So, y(t) = cos(at T) = =e-jt

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9.17 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9.18 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 9.20 (Solution) HLP(f) = rect(f /2fc) and hLP(t) = 2fcsinc(2fct)
- Hnf) = HLP(4f) and h1(t) = 0.25hLP(0.25t)
- (b) HPF (with cutoff 2fc)
- (c) BPF (fo = 8fc, passband = 2fc): HBP(f) = HLP(f + fo) + HLP(f \_ fo) and hBP(t) = 2hLP(t) cos(2ufot)
- (d) BSF (fo = 8fc, stopband = 2fc):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 9.22 (Solution) Refer to the sketches. X(f) =
- A (a) X[k] = X(f) = Ae-j2rfto

<!-- image -->

<!-- formula-not-decoded -->

- (c) X[k} = '(0.5kfoto) 0.5Atosinc? (0.5fto) 2T Ato 'sinc?

<!-- formula-not-decoded -->

## 9.23 (Solution) Refer to the sketches.

<!-- image -->

- (a) z(t) = rect(t), X(f) = sinc(f), T=2, f =kfo = 0.5k, X[k] = 0.5sinc(0.5k)
- = 0.5k, X[k] = 0.5sinc(0.5k)e-jkz/2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (f) z(t) = tri(t) X(f) = sinc? (f) T =1.5, f =kfo = 2k/3,

<!-- formula-not-decoded -->

- X(f) = 0.5sinc(0.5f)le-jrf /2 = ~jsinc(0.5f)sin(0.5nf) T =2, f =kfo = 0.5, X[k] ~jO.5sinc(0.25k) sin(0.25k7)

## 9.24 (Solution)

<!-- formula-not-decoded -->

- (b) (t) No conjugate symmetry. =e-jtt

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9.25 (Solution) Use the modulation or convolution property

- (a) z(t) sgn(t)rect(t) , X(f) =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) I(t) = sinc(2t)sinc(4t), X(f) = [0.5rect(0.5f)] * [0.25rect(0.25f)} a trapezoid)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 9.26 (Properties) Refer to the sketches\_

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

9.27 (Solution) For œ &lt; 0, we see exponential growth and tbe Fourier transform does not exist.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- X(f) = 0.25rect(0.25f).
- (a) y(t) = z(-t) Y(f) =X(-f) = 0.25rect(0.25f) (even symmetry)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9.29 (Convolution) Refer to the sketches for parts (d-f)-

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

= sinc(f) with f 4 kfo = 0.5k, the FS coefficients are Y[k] = 0.5sinc(0.5k) So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9.30 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (f) X(f) = [u(f +2) - 2u(f) + u(f + 2)e-j2rf = Y(f)e-j2rf ~ y(t) = 2sinc(2t)e~j2rt = So,

## 9.31 (Refer to the sketches

<!-- image -->

- (a) 2(t) = sinc(t ~ 2) X(f) = rect(f)e-j4nf
- X(f) =05[tri(f + 4) + tri(f = 4)] (by modulation)
- 0.257), X(f) = 0.58(f +
- X(f) = 0.5[sinc(f + 0.5) + sinc(f 0.5)}

50, X(f) approximates a pair

- X(f) = ~ 0.5)] The sinc functions are lOOO-times compressed versions of sinc(f) of impulses of strength 0.5 (the area of each sinc)
- (f) z(t) = cos(at)rect(1OO0t) , X(f) = 4 sinc(
- The sinc functions are 1000-times stretched versions of sinc(f) So, X(f) is nearly constant.

## 9.32 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (f) X(f) = tri(f) z(t) = sinc? (t)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9.33 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9.34 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 9.35 (Solution) With T = 2, and fo = 0.5, the FS coefficients of the periodic extension y(t) are found as So, Y(f) = f=kfo

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9.36 (Solution)

- (b) X(f) real and even; s0 2(t) is also real and even.

## 9.37 (Solution) Refer to the sketches

<!-- image -->

- (a) z(t) = rect(t): Decay rate % 1/f, X(f) = sinc(f)
- (b) z(t) = tri(t): Decay rate % 1/f2, X(f) = sinc2(f)
- X(f) = 2sinc(2f) +sinc(2f -1) +sinc(2f +1) 1/f3 ,

<!-- formula-not-decoded -->

- (e) z(t) = cos(0.5nt)rect(0.5t): Decay rate x 1/f2, X(f) = sinc(2f 0.5) + sinc(2f + 0.5)
- (f) z(t) = (1 \_ t?)rect(0.5t): Decay rate % 1/f2

9.38 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

- (b) Magnitude is constant. Filter type is allpass.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) Filter type is lowpass.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (Circuit 3)
- (b) Filter type is highpass.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (Circuit 4) This gives the same results as circuit 2

<!-- formula-not-decoded -->

- (Circuit 5)
- (b) Filter type is lowpass.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (Circuit 6)

<!-- formula-not-decoded -->

- (b) Filter type is highpass.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- So, = 0.2[4 + cos(47t)} y(t)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (f) h(t) = sinc(t) cos(8nt) , H(f) = Fom its sketch, observe that only the 4 Hz component is passed (with a gain
- (g) h(t) = H(f) = 0.5[tri(f 2.5) + tri(f + 2.5)]. Ftom its sketch; observe that only the 2 Hz component is passed (with a of 0.25) and thus y(t) gain
- (h) h(t) = sinc?(t) cos(l6mt),
- component is passed and thus y(t) = 0

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

X(f) = ~ 1.5k) The filter output blocks frequencies past 2 Hz and thus k=-0 So,

<!-- formula-not-decoded -->

- 9.43 (Solution) The outputs of the two systems are not the same because the cascade contains a nonlinear system

<!-- formula-not-decoded -->

Refer to the sketch. cos(rt) sin2 = 0.5(1 Outpur of phase shifter

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Refer to the sketch. cos(rt) 4 0.5(1 + sin(2"t Output of phase shifter [Y(f]

<!-- formula-not-decoded -->

<!-- image -->

The outputs of the two systems are not identical.

<!-- image -->

<!-- image -->

Tbe outputs of parts(b) and (c) are identical.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## e-jnf

- (b) z(t) = cos(8nt) . So, fo = 4 Hz and H(fo) = =1 e-j45
- cos(4Ont) For fo = 0, H(O) = 1. For f1 =
- (c) z(t) = 4+ cos(Tt For f2 = 20, H(20) = 0 = 0.757)
- (d) z(t) = sinc[5 (t \_ 1)], X(f) = 0. = 0.2e-j2" f Ifl&lt;2.5. So, Y(f) = X(f)H(f) = 0.2e-j3f= Ifl&lt;2.5 and y(t) = sinc[5(t 1.5)]
- y(t) = 1

- = 2rect(2f) + 4rect(4f) = 6rect(2f) + Arect[4(f 1.5)] + Arect[4(f + 1.5)] and H(f)

<!-- formula-not-decoded -->

- = = 2rect(2f). S0, Q = 0.5 and H(f) = 2Arect(2f) I2A = 2 and 1 S0,
- (a) If y(t) sinc(0.5t) , then Y(f) H(f)X(f) = (6)2Arect(2f).
- (b) If y(t) = sinc(0.25t), then Y(f) = 4rect(4f) there are no values of A and a for which this happens. So,
- (c) If z(t) = y(t) then Y(f) = X(f). This requires Q 2 4 and A = %.
- 9.49 (Solution) h(t) = Asinc(5t \_ 8). So, H(f) = =
- (a) z(t) = 1, Y(f) = X(f)H(f) = 0.88(f), y(t) = 0.8
- =
- (d) z(t) = sinc(t), X(f) = rect(f) , Y(f) =X(f)H(f) = Ifl &lt; 0.5. So, y(t) = 0.Bsinc(t 1.6)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

X(f) = 0.5sinc?(0.5f). With f = kfo = k, the FS coefficients are X[k] = 0.5sinc2 (0.5k). S0, the output (for |fl &lt; 2.5) contains dc and k = 4l (at 1 Hz) (note that X[2] = 0) So,

4 The time domain output is thus y(t) = 0.5(0.8) + (0.8) cos(2nt

- 9.50 (Solution) h(t) = 4sinc? (2t
- (a) z(t) =1, y(t) = 2
- (b) z(t) = cos(2nt) . fo =1, H(1) = and y(t) = cos(2nt T) = So,
- (d) z(t) = sinc(t), X(f) = rect(f), A sketch shows that Y(f) = [0.5tri(2f) + = 0.25sinc?[0.5(t = 0.5)] + 1.Ssinc(t \_ 0.5)
- (e) z(t) = sinc(12t), y(t) = 1) So,

<!-- formula-not-decoded -->

## 9.51 (Solution)

<!-- formula-not-decoded -->

## 9.52 (Solution)

<!-- formula-not-decoded -->

- (b) h(t) = [1 \_ e-2Ju(t) Causal and unstable, since J |h(t)ldt is infinite)
- (c) h(t) sinc(t), H(f) = rect(f) Noncausal and unstable; since f |h(t)ldt is infinite)

<!-- formula-not-decoded -->

- (e) h(t) = 0.58(t), H(f) = 0.5, y(t) = 0.52(t). Causal and stable

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) h(t) = sinc?(t + 1), H(f) = Noncausal and stable (f |h(t)ldt = 1)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) For cfo &lt; 1, the response will resemble (be a approximation to) the input. good

## 9.54 (Solution)

<!-- formula-not-decoded -->

- (c)
- (d) False. If z(t) = cos(ot) then y(t) = Acos(at) + Bsin(at) = Ccos(at + 0). This does not, in general; equal K cos(at)
- (e) if ß &gt; œ, Y(f) = So,
- So, if ß &gt;

- If X(f) = 0, |fl &gt; B and ß &gt; 2B, then Y(f) = #X(f) and y(t) =
- 8 9.55 (Solution) The frequency response of a filter is H() =
- (a) dc Ao = |H(o)| = 1 gain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

So, 0.0001 (64 16w2 + + 1602) = 64 or W4 = 640000 or W = 28.2843 rad/s 64

<!-- formula-not-decoded -->

- 1 02 + VZjw
- (a) dc Ao = |H(o)1 = 1 gain
- 1 (b) Gain is (1 ~ 02)2 + 22

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

1 = 10000 or w = 9.9997 or W ~ 10 rad /s S0,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9.57 (Solution) Refer to the sketches.

<!-- image -->

<!-- image -->

- [32, 8, 18] W. The two-sided PSD shows impulses of strength 16, 4 and 9 at 45,410,415 Hz
- = [32; 8] W. The two-sided PSD shows an impulse of strength 16 at f = 0, and impulses of strength Hz,
- 9.58 (Solution) Tbe autocorrelation R(f) must be even symmetric function of f2 . an
- 1 (a) R(f) = Does not qualify.

<!-- formula-not-decoded -->

- 1 (c) R(f) = Does not qualify.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9,59 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9.60 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9.61 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9.62 (Solution)

Babs = 0.5 and Tr = 2 (width of central lobe of h(t). S0, TrBabs = 1 Sp,

- 9.63 (Solution) For a second-order Butterworth filter with a cutoff frequency of 1 rad /s, the magnitude 1 squared function is |H(f)I? = and H(0) = 1 1 +

<!-- formula-not-decoded -->

- 9.64 (Solution) Compute the indicated time-bandwidth product for each system

<!-- formula-not-decoded -->

## 9.65 (Solution)

<!-- formula-not-decoded -->

- 9.66 (Solution) Tbe overall impulse response of a complex system with many subsystems is the convolution of the individual impulse responses and tends to a Gaussian signal (by the central limit theorem). Tbus; the frequency response is also a Gaussian signal.

## 9.67 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) Probe time constant ís TP = 0.1 nsEstimate tbe rise-time as TP = Tm = (T2+T}+T2)1/2 = Thus (in ns), 1 + (0.22)2 +T2 = 1.21 and To So,

## COMPUTATION AND DESIGN

## 9.68 (Solution)

```
'PROBLEM 9 .68 'PART (b) w=0:0.01:5;
```

```
,grid
```

```
9.69 (Solution) Uses the ADSP routine sysrespl , trbw 'PROBLEM 9.69 'PART (a) N=l;D=[1 1] ;b-(1) ./polyval (D,s) ; subplot (2,2,1) ,plot(t ,eval (y)) ,grid yzsysrespl(s' ,N,D, [1]) subplot (2,2,1) ,plot (t,eval (y)) ,grid subplot (2,2,2) ,plot (v,abs (h) ) N=1;D=[1 sqrt(2) 1];h=(1) ./polyval (D,s) ; yzsysrespl('5' ,N,D, [1]) subplot (2,2,1) ,plot(t,eval(y)) ,grid subplot (2,2,2) ,plot (v ,abs (h) ) subplot (2,2,4) (w,angle(h)*lBO/pi) ,grid,pause N=1;D=[1 2 2 1] ;b=(1) ./polyval (D,s) ; subplot (2,2,1) ,plot(t ,eval (y) ) subplot (2,2,2) ,plot (w,abs (b) ) subplot (2,2,4) ,Plot (w angle(h)*18O/pi) ,grid,pause 'PART (b) N=1;D= [1 1] ;trbw (N , D) pause "Part (a) N=1;D=[1 2 1] ;trbw(N ,D) pause 'Part (b) N=1;D=[1 sqrt (2) 1] ;trbv (N , D) ,Pause %Part (c) N=1;D=[1 2 2 1] ; trbv (N ,D) 'Part (d) 9.70 (Solution) Uses the ADSP routine sspesp 'PROBLEM 9 . 70 X= [2,3,-pi/3] ;t=0:0.01:6; 'PARI (a) a=1;N-2;D=[1,a] pause 'grid 'grid 'plot 'grid 'grid
```

```
'PARI (b)
```

```
C-3;N=1 ;D=[1,4,C] ;yss3=ssresp(' s' ,N ,D,x) ,plot (t,eval (yss3) ) pause pause (t,eval (yss5)) ,plot
```

## 10.1 (Solution) Refer to the sketches.

<!-- image -->

<!-- formula-not-decoded -->

10.2 (Solution) Refer to the sketch. fc = 1.5 MHz, f = 50 Hz to 15 kHz Spectrum of modulated signal

<!-- image -->

The frequencies in the modulated signal will cover 1500+0.05 kHz and 15004 15 kHz the LSB extends from 1500 - 15 = 1485 kHz to 1500 0.050 = 1499.95 kHz (positive frequencies) So,

- Ic(t)lmax = 3, So,
- So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## MODULATION

<!-- image -->

- = f1)t]

<!-- image -->

- 10.4 (Solution) ß =0.8, Pr = 50 kW
- Pr 50 (a) Pr = Pc(1+0.582). Pc = = 37.88 kW 1+0.5ß2 1.32 So,
- Pr = Pc (b) Message power equals Pr ~ Pc. So, = 0.2424 Pr

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 10.6 (Solution)

Refer to the sketches (we assumed f1 = 10, f2 = 20, fc = 200 Hz Spectrum of modulated signal

<!-- image -->

- So, ID(t) =
- (b) Ideal LPF for recovery requires a of 2 and a cutof frequency fB &gt; max(f1,f2) gain

## 10.7 (Solution)

- No recovery possible (z(t) is not 2 0 for all Imin(t) = &lt; 0) time; 21,
- &lt; 0)
- &lt;0)

## 10.8 (Solution)

<!-- formula-not-decoded -->

## 10.9 (Solution)

- (b) z(t) =

## 10.10 (Solution) x(t) = A

- 0(t)
- =
- (a) Carrier frequency fc = Hz = 10 MHz. 107
- (b) Ftequency of the modulating signal fB = 104 Hz = 10 kHz

Af Peak frequency deviation Af = (50)(104) Modulation index ß = = (50)(104)/(104) = 50 fB

Af 10.11 (Solution) Af = 75 kHz; ß = Since f varies from 50 Hz to 15 kHz, the allowable range of f 5 &lt; ß &lt; 1500 i.e,

- Af 10.12 (Solution) fB = 15 Af = 30 kHz. So, ß = =2 fB kHz,

Using

## 10.13 (Solution) Refer to the sketch.

<!-- image -->

## Spectrum of modulated signal

- (b) Pr = 2[(2)2 + (1)2] = 2.5, Pu(t)] = 4(2)[(1)2 + (3)?] = 1.25 = 509 of Pr.
- (c) Since there is no transmitted carrier, n = 1009
- 47,

- 10.14 (Solution) I(t) = cos(6OOnt) and fc 10 kHz Tbe signal power is Pr = 0.5(1+1+1)=1.5 W.
- Specuum of modulated signal

<!-- image -->

Tbe in f1(t) is P = 2[(0.5)?+6(0.1)?] =0.62 W. The sideband power is Ps = 2[6(0.1)2] = 0.12. This is 8% of the signal power Pr power

<!-- image -->

The power in 22(t) is Pz = 2{6(0.25)2] = 0.75 W. Tbe sideband power is also 0.75 W. This is 50% of the signal power Pz.

- 10.15 (Solution) z(t) =4+4cos(2nt) + 2cos(4nt)

spectrum with [0.5, 1, 12, 1, 0.5] at f = +[18, 19, 20, 21, 22] Hz

<!-- formula-not-decoded -->

Tbe power in the sidebands is Ps = 2[2(1)2 + 2(0.5)2] = 5 W.

<!-- formula-not-decoded -->

- (a) Frequencies present: 10 1041 10 4 2 kHz, 10+ 5 kHz kHz, kHz,

<!-- formula-not-decoded -->

## 10.18 (Solution)

<!-- formula-not-decoded -->

- = 0 and we cannot recover the message.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

fo and can lead to the phenomenon of beats (if Af is not too large) get ~Af

- ID(t) Af)t] So, IR(t) If Af = 0, we

With the demodulating carrier cos[2;(1000+ Af)t + 0}, the demodulated signal is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- offset and is bandlimited to B the modulated signal reduces the spectrum by half and centers it about +fc. Hz,

2 = 0.542(1 + Pr)

<!-- formula-not-decoded -->

- (b) Af =0; 0 =0.25m. Upon filtering, we recover 2/I(t) because

<!-- formula-not-decoded -->

- (c) Af = 0, 8 = 0.57. There is no signal t0 recover because ID(t) = 0.25 0.57))
- (d) We cannot recover the message because ID(t) = 0.25

<!-- formula-not-decoded -->

The last two terms add up to 0.5[cos(2rfot) cos(2uAft)]

<!-- formula-not-decoded -->

The last two terms

- 10.20 (Solution) Tbe message z(t) is bandlimited to 10 kHz and fc = 100 kHz.

1 The detector discharging time constant 7 is bounded by:

- 10.21 (Solution) = sinc?(t),

Refer to the sketches for the various spectra.

<!-- image -->

=

0.57)] = 0

## 10.22 (Solution) ß = 5. Harmonics at fc+kfo, k = 0,1,2,3

- With ß = 5, we find

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 10.23 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 10.24 (Solution)

<!-- formula-not-decoded -->

This follows because î(t) =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (e) Tbe Hilbert transform of a real signal is also real. This follows because the convolution of two
- (c)

<!-- formula-not-decoded -->

## 10.26 (Solution) Refer to the sketches.

<!-- image -->

1 îM(t) = Tt = Now, sgn(f) = -1, f &lt; 0 and sgp(f) = 1, f &gt; 0. XB(f - fc) (positive frequencies) and sgn(f)XB(f + fc) = -XB(f + fc) (negative frequencies) &amp;M(f) = This spectrum describes modulation of rM(t) by a sine wave at f = fc. (t) = B(t)sin(2rfct) So, So,

## COMPUTATION AND DESIGN

## 10.27 (Solution)

```
'PROBLEM 10.27 ydsb=x.*c;plot (t,ydsb,t,x) pause pause 'Can use envelope detectio (1+0.8*x) .#c;plot(t,yan2,t,1+0.8*x) ,pause 'Can use envelope detection (1+1.2*x) .#c;plot(t,yan3,t,1+1.2+x) ,Pause 'Cannot use envelope detection use envelope detection yan2= yam3=
```

## 10.28 (Solution)

```
'PROBLEM 10.28 ydsb=x.*C.*c;plot(t,ydsb) ,pause #c;plot(t,yanl) pause yam2=(1+0.8+x)_ #C.#C;plot yam2) pause (t,
```

```
jan3=(1+1.2*x) *C;plot(t,yan3) ,pause
```

```
'Note To see the demodulated signal try the folloving smoothing filter: 'Use filtfilt for linear phase filtering for easy comparison b-[-3 ~6 ~5 3 21 46 67 74 67 46 21 3 ~5 ') ,pause yf2-filtfilt(h,1,yan2) ;plot(t,2*yf2-1,t,0.8*x,
```

%we recover scaled version of message except for startup transients

## 10.29 (Solution)

```
'PROBLEM 10.29 'Note To see the demodulated signal the following snoothing filter 'Use filtfilt for linear phase filtering for easy comparison ~6 ~5 3 21 46 67 74 67 46 21 3 ~5 ~6 -3]/320; 'Spencer filter t=0:0 . cd-cos(2OO*pi*t);ydsb=x.*C.*cd;plot(t,ydsb) ,pause yfl=filtfilt(h,1,ydsb) ;plot(t,yfl,t,0.5*x, ') ,pause pause yfl=filtfilt(h,1,ydsb) ;plot(t,yfl,t,0.5*x, ') pause yfl=filtfilt(b,1,ydsb) ') pause pause ) ,pause cd-cos(2OO*pitt) ;ydsb=(1+0.5*x) #C_ #cd;plot(t,ydsb) pause pause pause yfl-filtfilt(h,1,ydsb) ;plot(t,2*yfl-1,t,0.5+x,'-.') pause (1+0.5*x) #C . #cd;plot(t,ydsb) ,pause yfl=filtfilt(h,1,ydsb) ;plot(t,2#yfl-1,t,0.5*x, ') ,pause #cd;plot(t,ydsb) ,pause ') ,pause cd=cos (22O*pi*t) (1+0.5*x) *C.#cd;plot(t,ydsb) ,pause yfl=filtfilt(h,1 ,ydsb) (t,2*yfl-1,t,0.5*x, ) ,pause *C.*cd;plot(t,ydsb) pause yfl=filtfilt(h,1,ydsb) ;plot(t,2*yfl-1,t,0.8*x ') pause ydsb) ,pause yfl=filtfilt(h,1,ydsb) ;plot(t,2*yfl-1,t,0.8*x, ') ,pause (1+0.8*x) #C.*cd;plot(t,ydsb) ,pause yflsfiltfilt(h,1,ydsb) ;plot(t,2*yfl-1,t,0.8*x, ') ,pause #C.*cd;plot (t ydsb) pause try ydsb= ;ydsb= ;plot ydsb=
```

```
#C.#cd;plot(t,ydsb) ,pause yfl-filtfilt(h,1,ydsb) (t,2+yfl-1,t,0.8#x, ') ,pause cd-cos(2OO*pitt);ydsb=(1+1.2*x) .*C.#cd;plot(t ,ydsb) ,pause Jfl=filtfilt(h,1,ydsb) ;plot(t,2*yfl-1,t,1.2*x, ') pause #cd;plot(t,ydsb) ,pause yfl-filtfilt(h,1,ydsb) ;plot(t,2*yfl-1,t,1.2*x,' - .') ,pause yfl=filtfilt(h,1 ,Jdsb) ;plot(t,2*yfl-1,t,1.2+x, ') ,pause #C.#cd;plot(t, ,pause yfl-filtfilt(h,1,ydsb) ;plot(t,2*yf1-1,t,1.2*x, ') ,pause cd-cos(22O+pi*t);ydsb=(1+1.2*x) *C #cd;plot(t,ydsb) pause yflsfiltfilt(h,1,ydsb) ) ;plot ydsb) ;plot
```

## THE LAPLACE TRANSFORM

## 11.1 (Solution)

<!-- formula-not-decoded -->

11.2 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 4s (d) %(t) 4 [derivative property] (s + 2)2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 11.4 (Solution) I(t) = e-2tu(t) # X(s) (a) X(2s) = 0.5e ~2(0.50)u(0.5t)
- (b) X's) = ~te-2u(t)

<!-- formula-not-decoded -->

- (d) sX'(s) = 4(-te-2u(t)] =
- 11.5 (Solution) Refer to the sketches.
- (a) H(s) = 4+ s = -l; =1 Unstable marginally stable due to simple poles on the ju-axis at +j)
- (b) H(s) = Poles: 1, zeros: $ = 0, 0, 0 Unstable due to tbe in the RHP) pole
- Poles: = O; ~1, zeros: s = 2 Unstable (marginally stable due to simple on jw-axis at the origin) pole
- Poles: +j, 0, ~2, zeros: s = Unstable marginally stable due to simple on poles
- (e) H(s) Poles: s = -4, 0, 0 Unstable due to repeated pole

<!-- image -->

on jw-axis at the origin)

- 2(s+1) (f) H(s) = Unstable pole

due to repeated on jw-axis at +j and -j)

- 11.6 (Solution) IVI: I(0) = Ji2 sX(s)

<!-- formula-not-decoded -->

Since X(s) is not strictly proper, 50 we write Y(s) = to find z(0) = lim sY(s) = -1 part s+1,

(s + 2)2 (b) X(s) = 1 is Y(s) = 1/(s+ 1) and z(0) = lim sY(s) = =1

<!-- formula-not-decoded -->

- FVT does not apply (poles on the ju-axis) 52 + 1 Since X(s) is not strictly proper, by The strictly proper part is =2 long

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (g) X(s) = 16/(s2 + 4)2, FVI does not apply (unstable, poles on the ju-axis) lim sX(s) = 0
- (h) X(s) = sX (s) = FVT does not apply unstable; poles on the ju-axis) lim sX(s) = 0
- 11.7 (Solution) We have omitted the algebra that yields the constants of the PFE

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

4e-2t

So, h(t) = (-e-t +

~3e-3)u(t)

- 4s A Ko K1 2 3 (c) H(s) = + = 4 (s +3)( +1)5 s +3 7s +1)2 5 + 1 s +3 (s+1)2 4s Note that Ko = Is=-1 and K1 = h(t) = (3e-3t 2te-t + s+ 1 5+3 So;

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 4(s + 1) A K 1+j 1\_j (f) H(s) = 4 + + + (s +2)(s2 + 2s + 2) s +1+j s +2 5 +1 +j h(t) = ~2e-2u(t) + 2e~'[cos(t) + sin(t)Ju(t) since 0.257)u(t) So, Or,
- 2(s2 + 2) A K K' 12 ~5 \_ j4 ~5+j4 (g) H(s) = = + = 4 (s+2)(s2 +4s +5) s + 2 8+2+j 5 + 2 s +2+j So, h(t) = Or ,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.8 (Solution)

- (a) H(s) = Not strictly proper, S0 use long

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) H(s) = (s+222 division s + 1 long

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 4(s2 e-s) (d) H(s) = Separate terms and use as a (s+1)(s +2) ~ not proper and requires division. long

<!-- formula-not-decoded -->

## 11.9 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- H(s) = = 52+25 Unstable (or marginally stable, due to simple on jw-axis at origin) pole

<!-- formula-not-decoded -->

- (c) h(t) = te-tu(t) H(s) = Stable (proper H(s) and all in LHP) (s + 1)2 Y(s) H(s) = poles

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.10 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) y(t) = 0.22(t) , Y(s) = 0.2X (s) H(s) = 0.2,

## 1l.11 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

11.14 (Solution) Refer to the circuits.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 2 + 2s 11.15 (Solution) H(s) =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.17 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.18 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) z(t) = cos(t)u(t \_ 0.252) = cos[(t = = Jlcos(t sin(t 0.257)Ju(t

<!-- formula-not-decoded -->

For parts (d-f), refer to the sketches below.

<!-- image -->

- (d) z(t) = This is a switched periodic signal with period T = 1 and first period

<!-- formula-not-decoded -->

- &lt; 0 This is a switched periodic square wave with 21(t) =

<!-- formula-not-decoded -->

- f(t) = So, the impulse strengths are 1/*.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 11.20 (Solution) (t) = e-2u(t) 4 X(s)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

11.21 (Solution) We have omitted the algebra that yields the constants of the PFE

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.22 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) H(s) = Not strictly proper, s0 use division Jong

<!-- formula-not-decoded -->

For parts (c,d), see the following sketch.

<!-- formula-not-decoded -->

- (c) H(s) =

<!-- image -->

<!-- formula-not-decoded -->

- 1 Convert to form for switched periodic signal ~e-s

<!-- formula-not-decoded -->

- 11.23 (Solution) H(s) = Ml is a ratio of polynomials wth N(s) of degree N, D(s) of degree D. D(s)
- (a) If D&lt; N, IVT does not apply (not strictly proper) unless strictly proper of H(s) is used. part
- = 0!

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

the algebra. Of course; we cannot choose values of s that correspond to the of H(s). poles

## 11.26 (Solution)

<!-- formula-not-decoded -->

## 2 11.27 (Solution) h(t) = 2e-2u(t) # H(s) = s + 2 '

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.28 (Solution)

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By partial fraction expansion, h(t) = 1.155e-t/2 cos(0.866t + 309)

<!-- formula-not-decoded -->

By partial fraction expansion, y(t) = [~e-t + 1.155e-t/2 cos(0.866t 309)Ju(t)

<!-- formula-not-decoded -->

By fraction expansion; v(t) = cos(0.866t + 609)u(t) 2e-t/2 . partial

<!-- image -->

<!-- formula-not-decoded -->

By partial fraction expansion; h(t) = 6(t) +1.155e-t/2 cos(0.866t + 1509)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By partial fraction expansion; v(t) = ~2.309e-t/2 sin(0.866t)u(t)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- =0.8. So, for a dc output of 2, we must have a dc input of
- (b) y(t) = 2+ cos(2t) At W = 0, H(o) 2 0.8 = Then; by superposition (and the results of part (a) I(t) = 7sin(2t)

- (c) y(t) = cos? (2t) = 0.5+0.5cos(2t). From the results of parts (a) and (b), = 1 sin(2t)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.31 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.32 (Solution)

- (a) y(t) = 2(t), Y(s) =sX(s) H(s) =5. unstable (not a proper rational function) So,

## 11.33 (Solution)

<!-- formula-not-decoded -->

This is unstable (or marginally stable due to the simple on ju-axis at origin) pole

## 11.34 (Solution)

<!-- formula-not-decoded -->

The term e ~20tu(t) decays much faster than e-tu(t) and if ignored, we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

```
11.35 (Solution) Uses the ADSP routine sysresp2 'PROBLEM 11.35 N=2;D= [1,2] ; 11.36 (Solution) Uses the ADSP routines sysresp2 , trbw 'PROBLEM 11.36 t=0:0.01:6; 'PARI (a) C-3;N=1;D=[1,4,C] ; subplot (2,1,1) ,plot (t,eval(ystepl)) subplot (2,1,2) ,Plot (t,eval(yimpl)) ,pause ystep2=sysresp2('s' ,N,D,1 , [1 0]) ,yimp2-sysresp2('5' ,N,D) subplot (2,1,1) ,plot (t,eval(ystep2)) subplot (2,1,2) ,plot(t,eval (yimp2) ) Pause C-5;W=1;D=[1,4,C] ; subplot (2,1,1) ,plot(t,eval(ystep3)) pause 'PART (b) subplot (1,1,1) ,plot(t, [eval (ystepl) ;eval (ystep2) ;eval (ystep3) ]) ,Pause 'PART (c) trbv(N,D,3) pause pause 11.37 (Solution) Uses the ADSP routine ssresp x=-[2,3,-pi/3];t=0:0.01:6;
```

```
'PROBLEM 11.37 'PART (a) (t,eval(yss2)) ,pause 'PARI (b) ,Plot
```

## THE LAPLACE TRANSFORM

## 11.1 (Solution)

<!-- formula-not-decoded -->

11.2 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 4s (d) %(t) 4 [derivative property] (s + 2)2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 11.4 (Solution) I(t) = e-2tu(t) # X(s) (a) X(2s) = 0.5e ~2(0.50)u(0.5t)
- (b) X's) = ~te-2u(t)

<!-- formula-not-decoded -->

- (d) sX'(s) = 4(-te-2u(t)] =
- 11.5 (Solution) Refer to the sketches.
- (a) H(s) = 4+ s = -l; =1 Unstable marginally stable due to simple poles on the ju-axis at +j)
- (b) H(s) = Poles: 1, zeros: $ = 0, 0, 0 Unstable due to tbe in the RHP) pole
- Poles: = O; ~1, zeros: s = 2 Unstable (marginally stable due to simple on jw-axis at the origin) pole
- Poles: +j, 0, ~2, zeros: s = Unstable marginally stable due to simple on poles
- (e) H(s) Poles: s = -4, 0, 0 Unstable due to repeated pole

<!-- image -->

on jw-axis at the origin)

- 2(s+1) (f) H(s) = Unstable pole

due to repeated on jw-axis at +j and -j)

- 11.6 (Solution) IVI: I(0) = Ji2 sX(s)

<!-- formula-not-decoded -->

Since X(s) is not strictly proper, 50 we write Y(s) = to find z(0) = lim sY(s) = -1 part s+1,

(s + 2)2 (b) X(s) = 1 is Y(s) = 1/(s+ 1) and z(0) = lim sY(s) = =1

<!-- formula-not-decoded -->

- FVT does not apply (poles on the ju-axis) 52 + 1 Since X(s) is not strictly proper, by The strictly proper part is =2 long

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (g) X(s) = 16/(s2 + 4)2, FVI does not apply (unstable, poles on the ju-axis) lim sX(s) = 0
- (h) X(s) = sX (s) = FVT does not apply unstable; poles on the ju-axis) lim sX(s) = 0
- 11.7 (Solution) We have omitted the algebra that yields the constants of the PFE

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

4e-2t

So, h(t) = (-e-t +

~3e-3)u(t)

- 4s A Ko K1 2 3 (c) H(s) = + = 4 (s +3)( +1)5 s +3 7s +1)2 5 + 1 s +3 (s+1)2 4s Note that Ko = Is=-1 and K1 = h(t) = (3e-3t 2te-t + s+ 1 5+3 So;

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 4(s + 1) A K 1+j 1\_j (f) H(s) = 4 + + + (s +2)(s2 + 2s + 2) s +1+j s +2 5 +1 +j h(t) = ~2e-2u(t) + 2e~'[cos(t) + sin(t)Ju(t) since 0.257)u(t) So, Or,
- 2(s2 + 2) A K K' 12 ~5 \_ j4 ~5+j4 (g) H(s) = = + = 4 (s+2)(s2 +4s +5) s + 2 8+2+j 5 + 2 s +2+j So, h(t) = Or ,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.8 (Solution)

- (a) H(s) = Not strictly proper, S0 use long

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) H(s) = (s+222 division s + 1 long

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 4(s2 e-s) (d) H(s) = Separate terms and use as a (s+1)(s +2) ~ not proper and requires division. long

<!-- formula-not-decoded -->

## 11.9 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- H(s) = = 52+25 Unstable (or marginally stable, due to simple on jw-axis at origin) pole

<!-- formula-not-decoded -->

- (c) h(t) = te-tu(t) H(s) = Stable (proper H(s) and all in LHP) (s + 1)2 Y(s) H(s) = poles

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.10 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) y(t) = 0.22(t) , Y(s) = 0.2X (s) H(s) = 0.2,

## 1l.11 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

11.14 (Solution) Refer to the circuits.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 2 + 2s 11.15 (Solution) H(s) =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.17 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.18 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) z(t) = cos(t)u(t \_ 0.252) = cos[(t = = Jlcos(t sin(t 0.257)Ju(t

<!-- formula-not-decoded -->

For parts (d-f), refer to the sketches below.

<!-- image -->

- (d) z(t) = This is a switched periodic signal with period T = 1 and first period

<!-- formula-not-decoded -->

- &lt; 0 This is a switched periodic square wave with 21(t) =

<!-- formula-not-decoded -->

- f(t) = So, the impulse strengths are 1/*.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 11.20 (Solution) (t) = e-2u(t) 4 X(s)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

11.21 (Solution) We have omitted the algebra that yields the constants of the PFE

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.22 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) H(s) = Not strictly proper, s0 use division Jong

<!-- formula-not-decoded -->

For parts (c,d), see the following sketch.

<!-- formula-not-decoded -->

- (c) H(s) =

<!-- image -->

<!-- formula-not-decoded -->

- 1 Convert to form for switched periodic signal ~e-s

<!-- formula-not-decoded -->

- 11.23 (Solution) H(s) = Ml is a ratio of polynomials wth N(s) of degree N, D(s) of degree D. D(s)
- (a) If D&lt; N, IVT does not apply (not strictly proper) unless strictly proper of H(s) is used. part
- = 0!

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

the algebra. Of course; we cannot choose values of s that correspond to the of H(s). poles

## 11.26 (Solution)

<!-- formula-not-decoded -->

## 2 11.27 (Solution) h(t) = 2e-2u(t) # H(s) = s + 2 '

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.28 (Solution)

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By partial fraction expansion, h(t) = 1.155e-t/2 cos(0.866t + 309)

<!-- formula-not-decoded -->

By partial fraction expansion, y(t) = [~e-t + 1.155e-t/2 cos(0.866t 309)Ju(t)

<!-- formula-not-decoded -->

By fraction expansion; v(t) = cos(0.866t + 609)u(t) 2e-t/2 . partial

<!-- image -->

<!-- formula-not-decoded -->

By partial fraction expansion; h(t) = 6(t) +1.155e-t/2 cos(0.866t + 1509)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By partial fraction expansion; v(t) = ~2.309e-t/2 sin(0.866t)u(t)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- =0.8. So, for a dc output of 2, we must have a dc input of
- (b) y(t) = 2+ cos(2t) At W = 0, H(o) 2 0.8 = Then; by superposition (and the results of part (a) I(t) = 7sin(2t)

- (c) y(t) = cos? (2t) = 0.5+0.5cos(2t). From the results of parts (a) and (b), = 1 sin(2t)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.31 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.32 (Solution)

- (a) y(t) = 2(t), Y(s) =sX(s) H(s) =5. unstable (not a proper rational function) So,

## 11.33 (Solution)

<!-- formula-not-decoded -->

This is unstable (or marginally stable due to the simple on ju-axis at origin) pole

## 11.34 (Solution)

<!-- formula-not-decoded -->

The term e ~20tu(t) decays much faster than e-tu(t) and if ignored, we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

```
11.35 (Solution) Uses the ADSP routine sysresp2 'PROBLEM 11.35 N=2;D= [1,2] ; 11.36 (Solution) Uses the ADSP routines sysresp2 , trbw 'PROBLEM 11.36 t=0:0.01:6; 'PARI (a) C-3;N=1;D=[1,4,C] ; subplot (2,1,1) ,plot (t,eval(ystepl)) subplot (2,1,2) ,Plot (t,eval(yimpl)) ,pause ystep2=sysresp2('s' ,N,D,1 , [1 0]) ,yimp2-sysresp2('5' ,N,D) subplot (2,1,1) ,plot (t,eval(ystep2)) subplot (2,1,2) ,plot(t,eval (yimp2) ) Pause C-5;W=1;D=[1,4,C] ; subplot (2,1,1) ,plot(t,eval(ystep3)) pause 'PART (b) subplot (1,1,1) ,plot(t, [eval (ystepl) ;eval (ystep2) ;eval (ystep3) ]) ,Pause 'PART (c) trbv(N,D,3) pause pause 11.37 (Solution) Uses the ADSP routine ssresp x=-[2,3,-pi/3];t=0:0.01:6;
```

```
'PROBLEM 11.37 'PART (a) (t,eval(yss2)) ,pause 'PARI (b) ,Plot
```

## APPLICATIONS OF THE LAPLACE TRANSFORM

<!-- formula-not-decoded -->

- (a) H(0) =0 = H(c). Also, H(s) peaks around w = 4 rad/s. bandpass filter. So,
- (b) z(t) = cos(0. &lt; 4 rad/s and w &gt; 4 rad /s. At W = 4 rad/s, H(s = j4) = 1. So, y(t) ~ sin(4t) 2t)

## 12.2 (Solution) Refer to the circuits

<!-- image -->

(a) (Circuit 1) H(s)

So, h(t)

=

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(1/s)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

3

3

=

## 12.3 (Solution)

<!-- formula-not-decoded -->

## 12.4 (Solution)

<!-- formula-not-decoded -->

## 12.5 (Solution)

<!-- formula-not-decoded -->

0 dB /dec, dB shift 20 log(0.1) = -20 dB slope:

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

Starting 20 dB /dec. (from tbe jw term) dB shift = 20 log(1) = 0 dB slope:

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

Break frequencies (rad/s): 10 (Den, repeated) , 100(Num) Starting ~20 dB/dec, dB shift = 20log(1) 0 dB Starting phase: -909 , final phase: -1800 slope:

<!-- image -->

-120

<!-- formula-not-decoded -->

Break frequencies (rad/s: 1(Num) 5(Den); I0(Den) Starting 0, dB sbift = 20l0g(0.02) = -34 dB slope:

<!-- image -->

<!-- formula-not-decoded -->

Starting 20 dB /dec, dB shift = 20l0g(4) = 12 dB slope:

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

Break frequencies (rad/s): 1(Num) 1O(Den, repeated)

Starting ~20 dB /dec, dB shift = 20l0g(0.1) = -20 dB slope:

<!-- image -->

## 12.6 (Solution) Refer to the sketch.

<!-- formula-not-decoded -->

Break frequencies (rad/s): 1(Num), 2(Den), 1O(Den)

Starting slope: 0, dB shift = 20 log(0.5) = -6 dB. We compute the following:

Frequency (rad/s)

1

10

Asyuptotic magnitude (dB)

~6

0

0

Corrected nagnitude (dB)

-2

3

Exact magnitude (dB)

~4.02

~2.21

~3.13

<!-- image -->

<!-- formula-not-decoded -->

Break frequencies (rad/s): 0.1(Den) 1(Num)

Starting phase: 0, final phase: -909 . We compute the following:

Frequency (rad/s)

0.01

0 .1

1.0

10

Asymptotic phase (degrees)

0

~90

~135

~90

Exact phase (degrees)

-10.8

~84.3

-123.6

~94.6

<!-- image -->

<!-- image -->

- 12.8 (Solution) Refer to the sketches
- (a) (System 1) Starting slope: ~20 dB/dec implies the term }

<!-- image -->

Break frequencies (rad/s): 1(Num), 2(Den, repeated)

<!-- formula-not-decoded -->

=

- (b) (System 2) Starting slope; 0. Break frequencies (rad/s): 1(Num) 10(Den, repeated)

<!-- formula-not-decoded -->

Note: Starting dB shift is ~40 dB, so 20log(K) = ~40 and K = 0.01

- 12.9 (Solution) Refer to the sketches.

<!-- formula-not-decoded -->

The Bode plot shows a of ~20 dB/dec past w = 1 rad /s. slope

<!-- formula-not-decoded -->

The Bode plot shows a slope of ~40 dB/dec past w = 1 rad/s.

<!-- formula-not-decoded -->

The Bode plot shows a of ~60 dB/dec past w =1 rad /s. slope

In each case, at w = magnitude is 0 dB)

<!-- image -->

<!-- image -->

## 12.10 (Solution) Refer to the sketches .

<!-- image -->

For (c), tbe phase plot does not include the phase due to the delay term Tbis linear phase, must be added (on a log frequency scale) to the phase shown. e-jw ~W,

Only (a) describes a minimum-phase filter.

Working backwards from the magnitude spectrum alone, we obtain

<!-- formula-not-decoded -->

1+ s71 12.11 (Solution) H(s) = Refer to the sketches. 1+ ST2

<!-- image -->

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

Ihe break frequencies in rad /s are 0.1 (Den) and 10 (Num)

<!-- formula-not-decoded -->

Tbe break frequencies in rad/s are 0.1 (Num) and 10 (Den).

<!-- formula-not-decoded -->

- = is an even function of w2 so minimum phase. 1 + (@)2n
- (b) At w = œ, we see that

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 12.13 (Subsonic Filters) Refer to the sketch

<!-- image -->

fB = 15 so WB = 30T. Also 12 dB /octave 40 dB /dec. Hz,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 12.14 (Solution) Refer to the sketches. Let ~ = RC

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

- (c)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For k = 0.5, the gain is constant for all frequencies. For k = 0, the break frequencies are ! (Num) and '(Den) For k =1, the break frequencies are The is nearly constant for frequencies past 4\_ For k = 0, the dc gain is 120 (nearly zero) For k = 1, the dc is # (nearly unity)  For both k = 0 and k = 1, the high frequency is 0.5. So, settings closer to k = 0 provide a cut and settings closer to k = 1 provide a frequency boost gain gain gain Jow

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For k = 0.5, the is constant for all frequencies. For k 0, the break frequencies are For k = 1, the break frequencies are is nearly constant for frequencies below For k = 0, the high frequency zero)  For k = 1, the high frequency is # (nearly unity). For both k = 0 and k = 1, the dc (Jow frequency) is 0.5. settings closer to k = 0 provide a cut and settings closer to k =1 provide a high frequency boost. gain gain gain gain gain So;

For the base control; "B = = 6 7 = 4.77 mS For the treble control, WB = 6 T = 0.2865 ms If R =1 kn, then C = 4.77 pF. So, So,

## 12.15 (Solution) Refer to the sketches

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 12.17 (Solution) Refer to the figure. RIAA equalization curve

f Hz(log)

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 12.18 (Solution) Refer to the sketches. Let T2 27(1500)

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

- 12.19 (Solution) An allpass filter must be a mixed phase system since the LHP poles must be matched by RHP zeros. A stable allpass filter (with only LHP poles) is a maximum phase system since all its zeros are in the RHP.
- K(s =2

<!-- formula-not-decoded -->

- 12.21 (Solution) Since the delay of an allpass filter is greater than zero, the delay of a cascade of a minimum filter cascaded with an allpass filter (which does not change the magnitude)   will always be larger than the delay of the minimum phase filter itself. phase
- 12.22 (Solution)
- (a) We place zeros at = =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 12.23 (Solution)

- (a) Place pairs at $1 pole

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) The flter order is 4

(c) Assuming high Q (arithmetic symmetry of the cutoff frequencies) , w0 ~0.5(1 +w2) = 45 H(ø) = [H(wo)l ~ 0.0055 Tbe half-power frequencies where H()l = 0.707(0.0055) are w1 =38 rad/s and w2 = 52 rad/s. S0, So,

Wo The approximate value of Q is Q ~ ~ 3 (not really a high Q circuit) . B

- (d) Decreasing œ moves the closer to the jw-axis and makes the frequency response much sharper (and the Q much higher) . poles
- 12.24 (Solution) H(s) =
- (a) H) = The Bode plot shows 0 dB up to w = 1 rad /s and of -40 dB /dec past w =1 rad/s slope
- (b) The dc gain is Ao = 1
- (c) Tbe is Ao/vz at w = 1 rad/s gain
- (d) Tbe equals 0.01Ao at w ~ 10 rad /s (a 20 dB/dec decrease) gain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

At the = So, W = 10 rad/s. 1 +(0.010)

- 1 (6) Tbe is 0.01 if |H(v)l? = 0.0001 = W = gain So,
- Tbe response is underdamped and will show oversboot.

<!-- formula-not-decoded -->

- (a) The center frequency is W = 10 rad/s with H(w) 1. The half-power frequencies at which = 0.5 are found from

<!-- formula-not-decoded -->

W1 = 6.18 rad/s, 02 = 16.18 rad/s and the half-power bandwidth Aw = 10 rad /s.

- (b)
- =1 + cos(0.lwit) + cos(wot) + cos(lOw2t), the response is y(t) cos(wot) because the filter gain at the other frequencies is negligible.
- (d) z(t) = cos(0.2w1t) + cos(wot). The input SNR 0 dB (input terms have equal magnitude). We find |H (0.21)| = 1.2455. S0 the ratio of the output powers is = 64.4661 and the SNR is 10 64.4661 = 18.0933 dB log
- (e) 2(t) = The input SNR = 0 dB (input terms have equal magnitude) We find |H(5w2)| = 1.2455. So, output SNR is 18.0933 dB (as ín previous part) .
- (f) 18.0933 dB (identical to the SNR figures computed in the earlier part) .

## 12.27 (Solution) Refer to the figure.

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The response is = 0.1(1 O.O1RC and and the rise time are much smaller and the response reaches final value about about 90 times faster . step its

- (c) s(t) t2 = compensation works. Yes;

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

To correct the phase distortion; the allpass filter must provide a phase of 45" at w = 1 rad/s and

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The allpass filter is 0.5. If z(t) = Bcos(t) + C cos(t/3) , then B = 0.3535 and C = 0.4743.gain

## COMPUTATION AND DESIGN

## 12.29 (Solution)

<!-- formula-not-decoded -->

'You can identify tbe minimum phase filter from magnitude spectrun

```
12.30 (Solution) Uses the ADSP routine tfnin 'PROBLEM 12.30 (c) s) . /polyval(D1,s); zeros (1,0-1) 1] ,'5') h2-1O+polyval (N2_ s) . /polyval (D2,s) ; 1] ,'5') zeros 'PARI (à) subplot (2,2,1) ,plot 'PARI (e) 1 ~4 0J) ,grid 'PART (f) hd3=-diff (hp3)./diff(w) ;hd4--diff (hp4)./diff (u) subplot (2,2,4) ,plot (wd , [hdl ;hd2;hd3;hd4] ) ,axis( [0 1 0 6]) ,grid 12.31 (Solution) Uses the ADSP routine bodelin 'PROBLEM 12.31 bodelin(1, [1 sqrt (2) 1]) ; pause bodelin( [1 0] [1 1 1]) ;pause bodelin(1, [1 2 2 1]) ; 12.32 (Solution) Uses the ADSP routine sysresp2 'PROBLEM 12.32 (a) t=0:0.01:1O;subplot(2,1,1) ,plot (t,eval(ys)) subplot (2,1,2) ,plot (t,eval (yi)) pause 'PART (b) N=1 ;D=[1,sqrt (2) ,1] ; ys=sysresp2(s' ,N,D,1, [1 O]) ;yi-sysresp2('s' ,,D) ; t=0:0.01 1O;subplot(2,1,1) ,plot (t,eval (ys) ) (", 'grid
```

```
subplot (2,1,2) ,plot (t,eval(yi)) ,Pause 'PART (c) N=[1,0] ;D=[1,1,1] ; t=0:0.01:10;subplot(2,1,1) ,plot (t,eval (ys) ) subplot (2,1,2) ,plot (t,eval(yi)) 'PART (d) N=1 ;D=[1,2,2,1] ; t=0:0.01:10;subplot(2,1,1) , plot(t,eval(ys)) subplot (2,1,2) ,plot (t,eval(yi)) ,pause
```

## 12.33 (Solution) Uses the ADSP routine bodelin

```
'PROBLEM 12.31 N=1;D=[1 1] ;bodelin (N,D) pause h=(1) ./polyval (D,s) ;plot (v,abs(b)) ,grid ,pause N=1;D=[1 sqrt(2) 1] ; bodelin (N D) ;pause b=(1) ./polyval (D,s) ;plot (v,abs(h)) ,grid,pause N=1;D=[1 1 1] ;bodelin (N D) ;pause b=(1) ./polyval (D,s) (w abs (h)) ,grid ,pause N=1;D= [1 2 2 1] ;bodelin (N ,D) ; pause ;plot 'grid
```

## 12.34 (Solution) Uses the ADSP routine sysrespl , trbw

```
'PROBLEM 12.34 'PARI (a) t=0:0.01: subplot (2,2,1) ,plot (t,eval(y)) subplot (2,2,4) ,plot (v,angle(h)*18O/pi) ,grid,pause N=1 ;D=[1 2 1] ;b=(1) ./polyval (D,s) ; y-sysrespl('6' ,,D, [1]) subplot (2,2,1) ,Plot (t ,eval (y) ) subplot (2,2,2) ,plot (w ,abs (h)) subplot (2,2,4) ,plot (w,angle(h)*180/pi) ,grid ,pause N-1;D-[1 sqrt(2) 1] ;b=(1) ./ polyval (D ,s) subplot (2,2,1) ,plot (t ,eval (y)) subplot (2,2,2) ,plot (w ,abs (b) ) 'grid grid 'grid 'grid 'grid ,grid
```

```
N=1;D=[1 2 2 1] ;b=-(1) ./polyval (D,s) ; subplot (2,2,1) ,plot (t,eval(y) ) 'PART (b) 'Part (a) 2 1] ;trbv (N = D) ,pause 'Part (b) N=1;D=[1 sqrt(2) 1] ;trbw (N ,D) pause 'Part (c) 2 1] ; trbw (N ,D) 'Part (d) 'grid ,grid
```

## 12.35 (Solution) Uses the ADSP routine ssresp

```
'PROBLEM 12.35 x=[2,3,-pi/3];t=0:0.01:6; (a) a=1;N=2;D=[1 ,a];yssl-ssresp('s' N,D,x) ,plot(t,eval(yssl)) ,Pause 'PARI () C-3;N-1;D=[1,4,C] ;yss3-ssresp('s' ,W,D,x) ,Plot (t,eval (yss3)) C-4;N=1;D= [1,4,C] ;yss4=ssresp('s' ,N,D,x) (t,eval (yss4)) ,Pause (t ,eval (yss5)) Pause ,plot 'plot
```

## 13.1 (Solution)

## ANALOG FILTERS

- = 2 kHz
- =1.5 with normalizing frequency =3 kHz
- So, f = [7.5,10,15,20] kHz, Afp = 5 kHz, Afs = 12.5 kHz and
- = 800 we change f2 t0 fg = 23.5294 kHz f3 f = [20,23.5294, 34,40] kHz, 20 Af, = 10.4706 kHz and Vp = 1, Vs = 162806 = 1.9101, B = 20 kHz, fo Afp S0, kHz,

## 13.2 (Solution)

- = 144 Since f2f3 = 140 &lt; we = 12.8/4.4 = 2.9091 with B = 4.4 Hz and fo = 12 Hz Hz, \_ So, =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- So,f = [5,10,62.5,125] Hz, Afp = 52.5 Hz, Afs = 120 Hz and Vp = 1, vs = }29 = 2.2857 with B = 52.5 Hz and fo = 25 Hz

<!-- formula-not-decoded -->

## 13.3 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (e)

<!-- image -->

Butterworth Poles

- (a) R =[
- IIn () R = (l/e)
- (c) Vn
- (a) V3 = 1. Poles lie on a circle of R = (unit circle)

LHP orientations (w.I. to jw-axis) 0k = (2k pole

<!-- formula-not-decoded -->

- (b) € =0.707 and a passband of 1 rad /s.

Poles lie on a circle of radius R = v3 =

For n = 2,v3 = 1.1893, for n = 3,v3 = 1.1225.

LHP orientations as in part(a) pole

- (c) passband edge of IOOHz.

Pole radius R = WpV3 = 2m(100)(1/e)1/" , orientations as in (a)

For n = 2,v3 = 747.2573, for n = 3,v3 = 705.2992

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (f) B = 1,W = 1, s0 LPZBS transformation is s = +1) and =s/(s?

<!-- formula-not-decoded -->

- (g) B = 2,W = 10, s0 LPZBS transformation is s = 2s/(s2 + 100), and

<!-- formula-not-decoded -->

13.5 (Solution) Refer to the sketches.

<!-- image -->

## 13.6 (Solution)

<!-- formula-not-decoded -->

- (6) V3 = = 1.1262

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (e) High frequency decay rate = 20n dB /dec = 60 dB /dec.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 13.9 (Solution)

- (a) Wp = 4,Ap = 3 dB(actually 3.0103 dB), 50 €2 =1 and v3 = 1 High frequency decay 60 dB /dec 20n dB /dec, s0 n = 3

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Together H(s) = Hp(up/sv3)  So, "p/s.

<!-- formula-not-decoded -->

We normalize W.r to f3, s0 =1 1, €2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We denormalize with respect to the half-power frequency; so

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) fp = [20,30] Hz, fs = [10,50] We first make the frequency specifications geometrically symmetric. Hz,

Since f1f4 = 500 &lt;

<!-- formula-not-decoded -->

= 153.91 rad/s

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We frst denormalize Hv(s) to Hv(s/v3), then use the LP2BP transformation $ = OI together = [s2 + (wovs)?]/sBv3; to (tedious algebral) (s2 get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

153.91 rad/s Wo

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

= OI together $ (tedious algebra') get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For n = 3, the poles of the normalized Butterworth filter are

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) 1 = 0.5849, € = 0.7648 For n = 4, the of the normalized Butterworth filter are poles

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 13.12 (Solution) Refer to the sketches\_

<!-- image -->

Locate the normalized Butterworth poles on the unit circle. Draw and extend radial lines. Draw horizontal and vertical lines at the intersections with the other two circles. These lines will intersect at the Chebyshev poles.

- (a) (1/n) sinh-1(1/e) 0.549,sinb(a) = 0.577,cosb(a) = 1.155

- 13.13 (Solution) |H(v)l? =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (a) Attenuation at v = 0.5 is l0log[l + 0.4913(4)] =1.732 dB Attenuation at v = 2 is 10log[1 + 0.4912(2)] = 25.215 dB
- (b) Half power frequency v3 cosh[(1 /n) cosh -1 (1/e)] = 1.0449
- (c) Tbe normalized Butterworth poles for n = 3 are

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (e) High frequency rate is 20n dB /dec. = 60 dB /dec. decay

13.14 (Solution) n = 5,fp = 1 kHz, Ap = 1 dB, = 6?

<!-- formula-not-decoded -->

## 13.15 (Solution) Refer to the sketch-

<!-- image -->

The filter order is n = 3. Max band gain = 10, Min passband =9.55\_ gain

<!-- formula-not-decoded -->

Ibe normalized passband attenuation (with respect to unit peak gain) is Ap = 20log(0.955) = 0.4 dB

<!-- formula-not-decoded -->

## 13.17 (Solution)

- (a) øp = 4, Ap = 3 dB(actually 3.0103 dB) , 50 €2 = 1 and v3 High frequency decay = 60 dB /dec =

<!-- formula-not-decoded -->

Real part of Chebyshev = Relpk] sinh(a) = ~0.149,-0.149,-0.298 part of Chebyshev poles = = 0.9037, ~0.9037,0 Chebyshev poles are Pck = [~0.149 + j0.9037,~0.298] poles Imag

<!-- formula-not-decoded -->

Since n is odd, for peak of unity, K = Q(0) = 0.125 gain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Real part of Chebyshev poles = ~0.549,~0.549

part of Chebyshev poles = Im[pk] cosh(a) 0.895,~0.895 Imag

Chebyshev poles are pck = [~0.549 + j0.895]

<!-- formula-not-decoded -->

Since n ís even, for peak of K = Q(0)/(1 + 02)0.5 0.876 gain unity;

<!-- formula-not-decoded -->

- (c) n = 2, minimum gain = 1.8 over 0 \_ 5 Hz filter order n 2 s0 €2 = 0.23457 and So,

<!-- formula-not-decoded -->

Real part of Chebyshev poles = Relpk] sinb(a) = -0.569,-0.569

part of Chebyshev poles = Im[pk] cosh(a) = 0.9075, ~0.9075 Imag

Chebyshev poles are pck = [~0.569 + j0.9075]

<!-- formula-not-decoded -->

H(s) = 1.0324/(s? + 1.138s + 1.147)

13.18 (Solution) For each part, Ap = 2 dB,As = 40 dB

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Since n is even; for peak of unity; K = Q(0)/(1 + 82)0.5 = 0.1634 gain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Since n is odd, for peak of unity; K = Q(0) = 0.327 gain

<!-- formula-not-decoded -->

- ~1 =0.5849

<!-- formula-not-decoded -->

= we pick WN We successively increase n = = A(vs) Às 2 As. We find until

<!-- formula-not-decoded -->

Thus; the required filter order is n = 3, and wN =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

S0 Chebyshev poles = [~0.184+ j0.923,-0.369]

<!-- formula-not-decoded -->

Since n is odd, for of K = Q(0) = 0.327 peak gain unity

<!-- formula-not-decoded -->

- We first make the frequency specifications geometrically symmetric.

<!-- formula-not-decoded -->

Vp = 1,Vs = = 27v600 = 153.91 rad/ s

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Since n is odd, for peak of unity; K = Q(0) = 0.327 gain

We use the LP2BP transformation (tedious algebra!) get

<!-- formula-not-decoded -->

change f3 to f}|f2 = 30 Hz

<!-- formula-not-decoded -->

= 2rv600 = 153.91 rad/ s

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

S0 Chebyshev = {~0.1844j0.923, ~0.369] poles

Since n is odd, for peak of unity; K = Q(0) = 0.327 gain

We use the LPZBS transformation s = (tedious algebral) get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 13.20 (Solution)

So,

- (b) V3 = 1/ {cosh[(1 /n) cosh -1(1/e)]} = 0.6492
- (c) Q = (1/n) sinh-1(1/e) = 0.99941,sinb(a) = 1.1743,cosh(a) = 1.5424

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) Zeros zk = =1to int(n/2) = 1) s0 zk = 4j1.155 Hv(s) = KPv(s)/Qv(s) = K(s - z1)(s ~ z2) / [(s = p1)(s p2) (s = ps)}

<!-- formula-not-decoded -->

For peak of 1,K = Qv(o)/ Pv(o) = 0.4/1.3333 = 0.3 gain

- (e) From Hv(s) see that for bigh frequencies H(s) x 1/s. high frequency decay is 20 dB /dec. we So,
- (a) n = 3,€ = 0.1, Attenuation A = 10log{1 + [1/e272(1/v)]} dB

<!-- formula-not-decoded -->

18.21 (Solution) n = 1/(100.14, \_ 1) = 0.0001

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

13.22 (Solution) For each part; Ap = 2 dB, As = 40 dB

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For peak gain

For denormalization w.I.to passband edge,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- =1/(100.14. 1) = 0.0001

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

=1to

#jsec(0) (k

<!-- formula-not-decoded -->

For peak of = Qv(o) / Pv(o) = 0.04/1.333 = 0.03 1,K gain

First; we denormalize w.I.to unit passband edge;

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Finally we use the LP2HP transformation ~p/s get

<!-- formula-not-decoded -->

- (c) fp = 10 fs = 50 1) = 0.0001 Hz; Hz,

<!-- formula-not-decoded -->

V3 = 1/ {cosb [(1 /n) cosh '(1/e)]} = 0.3323 Since w3 = We successively increase = and As = As. We find WN

<!-- formula-not-decoded -->

Thus the required filter order is n = 3 and WN

<!-- formula-not-decoded -->

For peak gain of 1,K = Qv(o)/Pv(0) = 0.04/1.333 = 0.03

We denormalize Hv(s) using "D =WN = 283.6 to get

<!-- formula-not-decoded -->

- (d) fp = [20,30] Hz, fs = [10,50] Hz; 50 We frst make the frequency specifications geometrically symmetric.

<!-- formula-not-decoded -->

Vp = 1,Vs = 2nv600 = 153.91 rad/ s Wo

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For peak of 1,K = Qv(o)/Pv(o) = 0.04/1.333 = 0.03 gain

First, we denormalize w.r.to unit passband edge using s = s/uD, where

<!-- formula-not-decoded -->

Tben, we use the LPZBP transformatíon = Together, we can directly use (tedious algebral) get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Then, we use the LPZBS transformation = we can directly use s = (tedious algebra') get

<!-- formula-not-decoded -->

## 13.23 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

zeros of Rn are Zk = 0.8723 and poles of Rn are pk = vs/zk = 3.4392 So,

<!-- formula-not-decoded -->

The zeros of H(s) are the poles of Rn, s0 zN = 4j3.4392

The poles of H(s) are the LHP roots of

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Its LHP oots are PN = ~0.17626 + j0.92968,-0.38139

<!-- formula-not-decoded -->

Since n is odd, for peak unit gain; K = Q(0)/P(0) = 0.0289

We denormalize using wD = Wp =4OOOT and obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

NOTE: Since n = 2.549, the design does not EXACTLY meet the passband specs. With n = 3, the actual stopband edge corresponding to Ap is 2.139 (not 3) . With 1/(2.139)2. this value; subsequent yield Using this, steps

<!-- formula-not-decoded -->

Tbis design now exactly meets passband specs.

- (b) Ap = 2 dB, As = 40 =4 dBfp

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

zeros of Rn are Zk = 0.7096 and poles of Rn are pk = vslzk = 8.4556 So,

<!-- formula-not-decoded -->

The zeros of H(s) are the of Rn, s0 zN = 4j8.4556 poles

The poles of H(s) are the LHP roots of

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Its LHP roots are pN ~0.4+j0.82

<!-- formula-not-decoded -->

Since n is even, get

<!-- formula-not-decoded -->

13.24 (Solution) fp = 100 Ap = 3 dB(actually 3.01 dB), delay to = 1 ms For unit 2n fpto = 0.628 Hz, delay,

We now compute the actual attenuation and normalized delay, increasing n as we go, until the computed normalized is within 1% of unity and the computed attenuation is &lt; Ap delay

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We denormalize s sto = s/1000 to get using

<!-- formula-not-decoded -->

Ap = 0.3 dB, delay to

= 0.628

<!-- formula-not-decoded -->

We now compute the actual attenuation and normalized increasing n 25 we go, until-the computed normalized delay is within 19 of unity and the computed attenuation is &lt; delay: Ap

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

=

lms

(b) fp = 100

For unit gain, K = Qv(0) = 105

We denormalize s = sto = s/1000 to using get

<!-- formula-not-decoded -->

## 13.25 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(tedious algebral) get

<!-- formula-not-decoded -->

## 13.26 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

= OI (tedious algebra!) get

<!-- formula-not-decoded -->

- (c) = 0. 5849.fp = [15, ? fs = [5,5o],f = [5,15, ?, 50], fo = 20 100.1Ap

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We first denormalize Hv(s) to Hv(s/v3) , then use the LP2BP transformation $ = OI together = [s2 + (wov3)?J/sBv3, to (tedious algebra') get

<!-- formula-not-decoded -->

## 13.27 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We first denormalize Hv(s) to Hv(s/vs), then use the LP2BS transformation 5 = OI together s =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) Ap = 2 dB,As = 40 dB, = 1 = 0.5849 1oo.1Ap

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We first denormalize Hv(s) to Hv(s/v3) then use the LP2BS transformation s = sB/(s2+w8), OI together =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

101.25/21.25 = 5.2706 with B = 2"(112) rad/s and wo = 2r(90) rad /s

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

k =1,2,3 : 91 = 1/ =2 By symmetry, 92 91 =2 and 93

<!-- formula-not-decoded -->

OI together $ = get

<!-- formula-not-decoded -->

## 13.28 (Solution)

Vp

- 1 = 0.5849

Since f2f3

=

1500 &lt; f? , we

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

=

315/23.333

=

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Now,œ = (1 /n) sinb

S0 Chebyshev = ~0.402+ j0.813 poles

<!-- formula-not-decoded -->

Since n is even, for peak We use the LPZBP transformation $ = +w3)/sB) to get (tedious algebral) gain (s2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Now; Q =

poles

S0 Chebyshev poles = {~0.1844j0.923,-0.369]

<!-- formula-not-decoded -->

=

=

Since n is odd, for peak gain

We use the LP2BP transformation s = (s2 +w)/sB to (tedious algebral) get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

f = [5,15,26.667,50] Hz; = 11.667 So, Afp Hz,

Vp = =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

So Chebyshev poles = [~0.184+ j0.923,-0.369]

<!-- formula-not-decoded -->

Since n is odd, for gain of unity; K = Q(0) = 0.327 peak

We use the LP2BP transformation $ = (s2 +u3)/sB to (tedious algebra') get

<!-- formula-not-decoded -->

## 13.29 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

27(30) rad/s

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This gives

Pk

<!-- formula-not-decoded -->

poles

Cheby

S0 Chebyshev poles = [~0.253 + j0.397, ~0.1054 j0.958]

<!-- formula-not-decoded -->

Since n is even; for peak gain of unity; K = Q(O)/(1 + 02)0.5 = 0.1634 We use tbe LP2BS transformation s = (tedious algebra') get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) Ap = 2 dB, As = 40 dB,€2 =

<!-- formula-not-decoded -->

=

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

S0 Chebyshev = [~0.1844 j0.923,~0.369] poles

<!-- formula-not-decoded -->

Since n is odd, for peak gain of K = Q(0) = 0.327 unity;

We use the LP2BS transformation $ =

<!-- formula-not-decoded -->

- (c) 1 =0.5849

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Vp = 101.25/21.25 = 5.2706 with B = 2r(112) rad/ s and wo = 27(90) rad/ s

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

= (1/n) sinh -1(1/e), Cheby = S0 Chebysbev = {~0.184+j0.923, -0.369] poles poles

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Since n is odd, for peak gain

We use the LP2BS transformation s = sB/(s? +48) to get (tedious algebral)

<!-- formula-not-decoded -->

## 13.30 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

vp = 1,v = 315/23.333 = 13.5 with B = 2r(23.333) tad/s and wo =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For peak gain of 1,K = Qv(o) / Pv(0) = 0.02/2 = 0.01

<!-- formula-not-decoded -->

Then, we use the LPZBP transformation = 4 we can directly use 4 (s2 [s2

<!-- formula-not-decoded -->

- (b) Ap = 2 dB,As = 40 dB, €2 = 1/(100.1A. ~ 1) =0.0001

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

=

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For peak gain

<!-- formula-not-decoded -->

use the LPZBP transformation = Together; we can directly use s = (tedious algebra') get

<!-- formula-not-decoded -->

## 13.31 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Vp = = = 27(30) rad/s

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Zeros zk = = 4j2.613,4j1.082

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For peak gain of 1,K = Qv(o)/Pv(o) = 0.08/8 = 0.01

First, we denormalize w.r.to unit passband edge s = s /wD, where using

<!-- formula-not-decoded -->

Then, we use the LP2BS transformation = Together, we can directly  use s = (tedious algebral) get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

= 70/10 = 7 with B = 27(70) rad/s and wo =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For peak = 0.03 gain

<!-- formula-not-decoded -->

Then, we use the LP2BS transformation = Together, we can directly use s =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (a) For a normalized second order Butterworth filter, Hv(s) = KIQv(s)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- ~ 1) =0.2589, € = 0.5088

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Comparing with H(s) = Kl(s?+As+B), we find A = 1.098,B = 1.1025, and

<!-- formula-not-decoded -->

- (c) For a normalized second order Bessel filter: H(s) = KI(s? +3s + 3) . Comparing with H(s) = Kl(s?+As+B), we find A = 3,B = 3, and

<!-- formula-not-decoded -->

- 13.33 (Solution) We look for the following clues:

Butterworth and Chebyshev I lowpass filters have a constant numerator.

For a 3-dB Butterworth lowpass filt the coefficients of the denominator polynomial are symmetric about the midpoint.  (If the passband edge is not unity; normalize the filter to unit passband.) ter,

For a Chebyshev II lowpass filter transfer function with unit stopband edge; the numerator poles are

(2k located at pk = +jsec k =1,2, int(n/2), where 8k = (If the stopband edge is not 2n 0k , and Q = 1 3v2

## COMPUTATION AND DESIGN

## Uses the ADSP routines lpP, lp2af , tfplot

```
'PROBLEM 13.34 %18dB/oct means 60 dB/dec_ So require 3rd order filter [n,d] =lpp ( 'bv' ,3,3) 'Lowpass prototype 3dB passband edge [nh,dh] -lp2af ('bp' ,n,d ,2*pi*15) 'Highpass filter [m,P,f]=tfplot('s' nh,dh , [0.1 100] ,1) ; 'Freq response, scale senilogx(f ,n) Uses tbe ADSP routines afd, minphase_ bodelin 'PROBLEM 13.35 'PART (a) 'FROM IHE DATA GIVEN: 'LPF specs Ap [1 45] dB fp 20 Hz fs=40 Hz Iy-Butter 'BPF specs Ap [1 50] dB fP [150 200] Hz fs [100 300] Hz 1 'Tvo calls to afd: lp' [1 45] ,20,40) ; [n2,d2]=afd( 'cl' bp [1 50] [150 200] [100 300]) ; n2=G+n2; 'Multiply n2 by gain equivalent of 12 dB (3.9811) 'Combine Need parallel conbination So H NP /DP (N1) (D2) + (N2 (D1) / (D1) (D2) 'Use conv for polyzomial multiplication 'Numerator of parallel combination dp=conv(d1,d2) ; 'Denominator of parallel coubination 'PARI (b) subplot (1,2,1) , f]=tfplot('s' ,nP,dP, [0 400 401] ,0,1) ; subplot (1,2,2) tfplot('s= dp, [1 1000] ,1,1) ;pause 'Design verification: i-[20_ 40 100_ 150 , 200 300]'index for band edges fspec=f(i); 'frequency of band edges alp= [1 45] ; 'Attenuation of LP stage abp=[50 1 1 50]-12; 'Attenuation of BP stage (v r to peak att of aspec=-[alp abp] 'Total specs _ Ihe converts to a column vector a= 'Actual attenuation at band edges [fspec aspec a] 'Display design specs and actual values (3 colunns) 'REMARK : 'Tbe Attenuation specs are EXACILY MET at the PASSBAND edges 'And attenuation specs are EXCEEDED at the other frequencies 'Computation of maximum attenuation index of minimum [-20*10g10(m) ;f(i)] 'Display ATTEJUAIION and frequency 'PART (c) roots(np) 'NOT MINIMUM PHASE (Sone roots bave real parts >=0) 1og 'grid [h,P , ,PP, +1 ; gain
```

- 13.35 (Solution)

```
'Convert IF [hnt ,hma] =bodelin ndm ,0) ; pause 'Bode info (true and asymptotic) 'PART (d) 'To compare the Bode plot of the minimun phase TF vith original we use tfplot('s' ,PP,dp, [1 1000] ,1,1) ; hold semilogx(hnt(:,1)/2/pi,bmt(:,2),'r') 'Plot true Bode f (Hz) semilogx(hma(:,1)/2/pi ,hma(:,2) ,'8' ) 'Asymptotic Bode Vs f (Hz) axis( [1 1000 -120 20]) Plot ,grid
```

## SAMPLING AND QUANTIZATION

<!-- image -->

- (d) Natural sampling. td = 0.1 ms; ts = 0.2 ms.
- (e) Zero-order-hold samplingts = 0.2 ms. S = 5 kHz. The spectrum of part (d) multiplied by sinc(f/5).
- 14.2 (Solution) z(t) = B = 2 kHz
- (a) Ideal sampling function ts = 0.2 ms, $ = 5 kHz. X{k] = S = 5000 Values of the sampled signal I(t) are

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) Ideal sampling: ts = are
- t x(t)

0.75

0

- 0

<!-- formula-not-decoded -->

- (c) Ideal sampling. ts = 0.4 ms; $ = 2.5 kHz. X[k] = S = 2500 Values of the sampled signal are I(t)
- t (ns) x(t)
- 0.8 ~0.06

0 .4

1

-0.19

<!-- formula-not-decoded -->

- (d) Natural sampling: td = 0.1 ms, ts = 0.2 ms. S = 5 X[k] = 0.5sinc(0.5k). Refer to the following sketch. So, kHz,

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

- (e) Zero-order-hold sampling. ts 0.2 ms. 5 =5 kHz. The spectrum of part (d) multiplied by sinc(f/S).
- 1.2 0.04

<!-- image -->

<!-- image -->

1.6

0.047

2

0

0 .25

- 0 5
- 1.25 1.5 0
- 1.75 0

2

0

## 14.3 (Solution)

<!-- formula-not-decoded -->

## 14.4 (Solution)

- B = 150 Hz. So, $ = 300 Hz
- (b) z(t) = cos(30Ont) B = 150 Hz,
- B = 250 Hz,
- 4150 Hz and 4250 Hz. S0 X(f) extends over +4OOHz. So, B = 400 Hz and S = 2B = 8OOHz.
- B = 100 s &gt; 2B = 2OOHz Hz,
- X(f) = (6/1OO)rect(f /100), B = 50 Hz,
- X(f) = O.ltri(f/100), B = 100 Hz, S &gt; 2B = 200 Hz.
- (b) z(t) = X(f) is the convolution of two signals whose spectra cover 450 Hz and +lOOHz. S0 the convolution extends over 15OHz. B = 150 Hz and S = 300 Hz. So, So,
- 14.5 (Solution) If z(t) = sampling Iate is $ = 3SN 6 samples /period. So, we acquire 36 samples over 6 periods.
- 14.6 (Solution) If z(t) = 3SN 4 samples /period. to acquire 100 samples, we must sample for 25 periods. If we sample analog ftequency is fo = 25 the sampling rate is S = 100 Hz and the digital frequency is F =0.25 So, Hz,
- 14.7 (Sampling Theorem) If z(t) = and the Nyquist rate is SN = 2 samples/period (or 6 samples per 3 periods), the sampling rate is 5 =

<!-- formula-not-decoded -->

- 14.8 (Solution) Refer to the sketches. In all cases; the spectrum ís the periodic extension of Xp(f) with period equal to the sampling frequency S. If S &lt; 2B, we observe overlap of the spectral images and aliasing.
- (a) X(f) = rect(f /40), B = 20 S = 50 Hz(no aliasing), 40 Hz, 30 Hz Hz,
- (b) X(f) = tri(f /20) B = 20 30 Hz Hz, Hz,
- (a) z(t) = cos(2OOnt) , B = 100 Hz, S = 450 Hz, F = 48 =
- (b) 2(t) = sin(4OOnt B = 200 S = 300 Hz, F = 40.257) = 0.25æ) = Hz,
- S = 300 Hz, F2 = gnr) sin(5n7/6)
- 0.257) S = 120 Hz F2 = {2 = ~ =

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

- IX(o)} = 1 Refer to the sketch.

<!-- formula-not-decoded -->

<!-- image -->

## 75 14.11 (Solution) 2(t) = sin(15Ont) 1 80

{Magnitude

<!-- image -->

- (a)
- (c)
- (d) An ideal BPF with passband from 60 Hz to 100 Hz recovers the 75 Hz and 85 Hz signal

14.12 (Solution) {z[n]} = {~1,2,3,2}, ts = 1. Refer to the sketch for parts (a) and (b)

<!-- image -->

- (a) From the step interpolated signal;, 2(2.5) = 3.
- cos(15O7t

- (b) From the linearly interpolated signal, 2(2.5) = 2.5.

<!-- formula-not-decoded -->

- =Ez[kJsinc(t ~ k)

- (d) For raised cosine interpolation (with R = 0.5): z(t) S0 z(t) = sinc(t) cos 2(2.5) =-0.0171 0.2401 So,
- 14.13 (Solution) z(t)=t2, 0 &lt;t&lt;2), ts =0.1 s, four quantization levels
- (a) zn] = {0,0.01,0.04,0.09,0.16,0.25,0.36,0.49,0.64,0.81,1,1.21,1.44,1.69, 1.96,,2.25, 2.56,2.89,3.24,3.61,4}
- (b) Since z [n] varies between 0 and 4, the 4 quantization levels are one unit apart. So the quantized signal zq[n) using rounding is

<!-- formula-not-decoded -->

- = 1.447. The actual quantization SNRQ is SNRQ 16.986 dB ,e? [n]

<!-- formula-not-decoded -->

- (d) The statistical estimate of the quantization SNRs is SNRs = lOlogPs +10.8 + 20log(L) - 20log(D), with L = 4 and D = 4 and N = 21, Ps = = 10log Ps + 10.8 = 16.17 dB
- (e) An estimate of the SNR; assuming z(t) to be periodic is based on

<!-- formula-not-decoded -->

14.14 (Solution) Refer to the sketch\_

<!-- image -->

For a filter cutoff frequency of 4 only components to 4 kHz are passed and so S &gt; 8 kHz. kHz,

But the signal is half-wave symmetric; 80 even harmonics are absent; s0 the highest frequency at the filter output is 3 kHz (not 4 kHz), so S &gt; 6 kHz

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (a) If fc = 20 the output of the band-limiting filter contains harmonics up to kfo = 20or k = 2 After sampling, this spectrum is replicated at intervals of 80 Hz. The ideal filter recovers the original harmonics (in the +40 Hz range) . Since X[2] = 0, one period of the periodic spectrum corresponds to the signal z(t) = Hz,
- (b) If fc = 40 the output of the band-limiting filter contains harmonics up to kfo = 40 or k = 4. After sampling, this spectrum is replicated at intervals of 80 Hz. The ideal filter recovers the original harmonics (in the 440 Hz range) Since X[2] = 0 = X[4], one period of the periodic spectrum corresponds to the signal z(t) = Hz,
- (c) If fc = 60 filter contains harmonics up to kfo = 60 or k = 6. After sampling at 80 the harmonics kfo above 40 Hz (for k &gt; 4) are aliased to to frequencies fka = kfo (k = 5) is aliased to 30 Hz (and added to the component already present. The ideal filter recovers the (original and aliased) harmonics in the +40 Hz range. One period of the periodic Hz, iting Hz,

14.16 (Solution) X(f) = 0.2rect(0.2f), S = 10 fc = 5 Hz. Hz,

<!-- formula-not-decoded -->

The sampling is ideal; s0 y(t) = 1Oz(t)

<!-- image -->

<!-- formula-not-decoded -->

Due to ZOH sampling; Y(f) # X(f) but is a sinc distorted version

<!-- image -->

## 14.17 (Solution)

- (b) If S = 140, components at fk &gt; 70 Hz aliased to fka = fk - MS where |fka| 70 Hz. The only components that are not aliased are at 10 Hz and 40 Hz. get

The digital frequencies are 1, 249

With |Fl &lt; 0.5, these become &amp;= 1

= sin(2nnF), the components at equal positive and negative frequencies cancel out and we are left with

<!-- formula-not-decoded -->

shows impulse pairs at f = 10 Hz and f = 20 Hz with strength 0.5. at f = 10 Hz and +909 at f = 20 Hz (with reversed phase at negative frequencies) .

- (c) The spectra of z(t) and y(t) are different due to aliasing. Only S &gt; 2B = 2(400) = 800 Hz, will allow perfect reconstruction æ(t) from its samples.

## 14.18 (Solution) The signal z(t) =

- (B) y(t) = 23(t) is bandlimited to 150 Hz. So, S &gt; 300 Hz
- (c) y(t) = |z(t)| is not bandlimited (a periodic; full rectified cosine)
- (d) h(t) = the filter output is cos(lOOnt). So, $ &gt; 100 Hz Hz,
- (e) h(t) = sinc(500t). Since fc = S &gt; 100 Hz So,

- (g) y(t) = S0,
- (h) y(t) = u[z(t)] is not bandlimited (it is a square wave).

we recover a 150 Hz sinusoid Hz,

- (a) If S exceeds the Nyquist rate, ie., S &gt; 300 then fo = 150 Hz? Hz,
- (b) If z(t) is sampled at a third sampling rate (say; 600 kHz) and leads to recovery of a 150 Hz signal, tben no aliasing has occurred.

4OOm where k and m are integers. This means that

- (c) For no phase reversal, the aliased frequency is positive fa = 150 = fo = 5 Tbus; or k = 8, m = 10, etc. allowed 2.5 kHz range. So,
- (d) If phase reversal occurs, the aliased frequency is negative.

fa 4OOm where k and m are integers.  Tbis means that &amp; m = 10, etc. So,

With k = 4,

## 14.20 (Solution) Refer to the sketches.

<!-- image -->

<!-- image -->

- (a) Ifi(t) = k=-c with fo = 0.25 Hz. So, X[k] = 0.5, k odd and X[k] = 0 otberwise.
- cutoff frequency of 0.6 the only frequency that appears is 0.25 Hz (for k = = cos(0.5nt) Hz,
- 8 (c) If i(t) = k=-0

## 14.21 (Solution Refer to the sketcbes.

<!-- image -->

- = 9 Hz. fo-5-
- = ~5. With $ = 48 the 40 Hz component is aliased to ~8 Hz and the 80 Hz component to ~16 Hz. Hz,
- f2 = 50 Hz and fo = GCD(40,50)=10 Hz fmax = 5fo = NFo. Hz, So,

We require œ = fo = 4 =9.5 Hz. the 40 Hz component is aliased to 2 Hz and the 50 Hz component to 2.5 Hz. Hz,

## 14.22 (Solution) Refer to the sketches.

<!-- image -->

- (a) f# = 500 We need a LPF for recovery. Hz,
- (b) N = int(f# / fo) = int( 508) = 2 Hz;

<!-- formula-not-decoded -->

For minimum S, k = 2 and fH &lt; S &lt; 2fL or 500 Hz &lt; S &lt; 600 Hz

So, choose $ = 500 Hz.  We require a BPF with band edges at 300 Hz and 500 Hz for recovery.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

edges at 400 Hz and 500 Hz for recovery

<!-- formula-not-decoded -->

- X(f) is bandlimited to 40 Hz. So the spectrum Y(f) is over 320 +40 (280 to 360 Hz) . The spectrum G(f) =Y(f) * Y(f) is between 560 and 720 Hz-
- (b) Since y(t) is a bandpass signal, fL = 280 Hz; f# = 360 B = 80 Hz and N = int ( 389) = 4 2fL We require, &lt;S &lt; k =1,2,3,4 Hz,

or 180 &lt; S &lt; 186.67 Hz.

- (c) Since g(t) is 2 B = 160 Hz and N = int( 2f# 2fL We require; &lt; S &lt; k =1,2,3,4 k k = 1 Hz,

## 14.24 (Solution) Refer to the sketch.

<!-- image -->

- (a) The zero-order-hold leads to sinc distortion of the form sinc(f / S) We require sinc(B 2 0.9 So,
- (b) Attenuation at 4 kHz 0.25) is 1 dB \_ 20 Isinc(0.25)/ = 1.92 dB. Attenuation at 12 kHz (5 = 0.75) is 1 dB 20 |sinc(0.75)| = 40.45 dB. log log
- (c) 1) = 0.2589 Filter order n = = 3.76 = n = 4
- 14.25 (Solution) Peak value = 4 V, B = 12 bits. With a full-scale range of 45 V; D = 10. Now, L and the signal power is Ps = 0.5(4)2 =8

S0, SNR = 10log Ps + 10.8 + 20log L 20log D = 72.078 dB

<!-- formula-not-decoded -->

- =4

## 14.26 (Solution) Refer to the sketch.

f (e)

Truncation

<!-- image -->

For truncation; the error is equally distributed between \_A and 0 The mean is m = ~0.54.

<!-- formula-not-decoded -->

For sign-magnitude truncation, the error is equally distributed between -A and 4.

<!-- formula-not-decoded -->

## 14.27 (Solution) Butterworth filter: n = 3, half-power frequency =4 kHz. B = 8 bits.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 14.28 (Solution) Amplitude level 41 V. Butterworth filter n = 2, fp = 4 kHz.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equating tbe we find tbe minimum value of 5 two,

- 14.29 (Solution) Butterworth filter: n = 3, fp = 3 kHz. 5 = 10 kHz.

<!-- formula-not-decoded -->

Signal level at 3 kHz is 0.707. The ratio of the aliasing level and signal level is 0.0555 (or 5.559)

- 14.30 (Solution) Amplitude level = +l V. Vrs = 2 B = 12 bits So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Signal power Ps = 0.5(22 + 42) = 10.

D We expect the peak vale of z(t) to be less than 6. choose D = 12. Then, A = 0.0029 and 2B So,

<!-- formula-not-decoded -->

With L = 2B , SNR = 10l0g Ps + 10.8+ 20log L \_ 20log D = 71.4636 dB

NOTE: The value of æ(t) is actually 5.4702 (and not 6). Then, D = 10.9404 and we compute = 7.7105(10)-4 and SNR 72.2666 dB peak

- 14.32 (Solution) Bandwidth = 4 kHz, B = 8 bits. TA = 20 ns, Th = 2 ps

<!-- formula-not-decoded -->

- 14.33 (Solution) fo = 10 kHz. Amplitude level = +l V. SNR=45 dB

42 Now; signal power Ps = 0.5(1)2 = 0.5, noise power PN = 02 = and 4 = = 25 12 2B

<!-- formula-not-decoded -->

This gives B ~ 7.77. B = 8 bits. With S = 20 kHz; the bit rate is SB = 160 kBits/s. So,

- 14.34 (Solution) B = 4. The signal level in the passband is attenuated by less than 1.2 dB due to the sinc distortion If S is the sampling rate in kHz, then 20log[sinc(4/S)] = 4 Tbus, 0.2858 and $ = 13.9964 kHz.

<!-- formula-not-decoded -->

= 9.1557 dB So,

- 14.35 (Solution) B = 4 kHz Tbe signal level in the passband is to be attenuated less than 1.5 dB and an image rejection of better than 45 dB in the stopband is required.

With $ = 16 kHz, the sinc distortion provides an attenuation of \_20log(f = 0.9121 dB at the the filter specifications are Ap = = 45 \_ 10.4545 = So,

<!-- formula-not-decoded -->

- B = 12 bits.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This gives n 2 3.57. pick a 4th order Butterworth filter .

The image rejection due to sinc distortion at the stopband edge fs = S-4kHz will be ~20log( 12.62 dB for an overall image rejection of better than 50 dB, the anti-imaging filter must provide an attenuation of at least 50 12.62 = 37.38 dB So,

## COMPUTATION AND DESIGN

## 14.37 (Solution)

```
Uses the ADSP routine dtplot 'PROBLEM 14.37 'PARI (a) 'Actual value at t=0.5 is 1/sqrt (2)=0.707 'Value predicted by interpolation is 1 , by linear interp is 0 .5 'Yes more samples vill improve results. 'PART (b) s2=sum(xn.*sinc(0.5-n)); 2=-50:50 m=cos(0.S+n*pi) 'Results approach true value but require nore signal samples step
```

- 14.38 (Solution) Uses the ADSP routine dtplot , tri, sinc

```
'PROBLEM 14.38 N=8;xu=[xn;zeros(N-1,4)];xu=xu(:)' ; 'PARI (a) nu=(0:4+N-1) ; dtplotys , ''),hold off ,pause 'PARI (b) nu=( (0:4*J-1)) ; 'M') ,hold off ,pause 'PARI (c) yi=filter(hi,1,xu) ; 'n') ,hold off= pause (nu ,
```

```
dtplot(nu-M,yi,'*') ,bold dtplot(ntN,xn,'0' ,'n') ,hold off ,pause 'More signal samples means periods N-8;xu=[xn;zeros(N-1,8)];xu=xu(:) (0:8+W-1) ; dtplot (ou-M,yi,'*') ,hold '') ,hold off
```

## 14.39 (Solution) Uses the ADSP routine dtplot \_ quantiz

```
'PROBLEM 14.39 'PART (a) subplot (1,1,1) ,plot (t,x) bold dtplot(ntts,xn,'') , axis( [0 4 ~2 2]) ,hold off ,Pause plot (t,x) ,bold 2]) ,bold off ,pause subplot (2,1,1) ,dtplot (n*ts,err) subplot (2,1,2) hist(err 10) ,pause subplot (1,1,1) ,plot (t,x) ,bold on,dtplot(n*ts,xn,'0') , axis( [0 4 ~2 2]) ,bold off ,pause B=4;L=2-B; [y,ty,snr2]=quantiz(xn, [0 10] ,L,'r' ,0) ; axis( [0 1 -2 2]) ,hold off pause err=xn-y; subplot (2,1,1) ,dtplot (ntts,err) subplot (2,1,2) hist(err,10) ,pause 'PART (b) t=0:0.01:1O;x=cos(2*pitt)+cos(G*pitt); subplot(1,1,1) ,plot (t,x) ,hold on,dtplot(ntts,xn,'0') , axis( [0 4 pause subplot (1,1,1) ,plot(t,x) ,hold on,dtplot(n*ts,Y,'') , axis( [0 1 -2 2]) ,bold off ,pause subplot (2,1,1) ,dtplot (ntts,err) subplot (2,1,2) ,bist (err . 10) ,pause on ,
```

```
n=0;799;ts=0.05;x=cos subplot (1,1,1) ,plot(t,x) ,hold on,dtplot(n*ts,m,'0') , axis( [0 4 ~2 2]) ,hold off ,pause [0 10] ,L,'r' ,0) ; subplot(1,1,1) plot(t,x) ,hold on,dtplot(n*ts,J,'') , axis( [0 1 ~2 2]) ,hold off ,pause subplot (2,1,1) ,dtplot (ntts,err) subplot(2,1,2) ,hist(err ,10) ,pause 'PART (c) Ihe signal pover is P=1 Ibe dynamic range is D=4 P=1;D=4; 'Iheoretical SNR 'PART (d) subplot(1,1,1) ,plot(t,x) ,hold on,dtplot(n*ts,xn,'0') , axis( [0 4 pause subplot (1,1,1) ,plot (t,x) ,hold dtplot (n*ts,Y,'0') , axis( [0 1 ~2 2]) ,hold off ,pause subplot (2,1,1) ,dtplot(n*ts,err) subplot (2,1,2) ,hist (err_ 10) ,pause n=0:799;ts=0.05 xn=Cos (2*n*ts#pi)+cos(6*n*tstpi); subplot (1,1,1) ,plot (t,x) ,hold on,dtplot (ntts,xn,'0') , axis( [0 4 ~2 2]) , hold off ,pause axis( [0 1 subplot (2,1,1) ,dtplot(n*ts,err) subplot(2,1,2) ,hist (err ,10) ,pause n=0:199;ts=0.05 subplot (1,1,1) ,plot(t,x) ,hold axis( [0 4 ~2 2]) ,bold off pause axis( [0 1 ~2 2]) ,hold off ,Pause subplot (2,1,1) ,dtplot (ntts,err) subplot(2,1,2) ,hist (err,10) ,pause (xn, on,
```

```
(2*n*ts*pi)tcos(G+n*ts*pi); subplot (1,1,1) ,Plot (t,x) ,bold on,dtplot(n*ts,xn,'0') , axis( [0 4 -2 2]) ,hold off ,pause B-8;L-2-B; [y,ty,snr2] =quantiz(xn, [0 10] ,L,'t' ,0) ; subplot 1,1) ,plot (t,x) hold on,dtplot(n*ts,y,'0') , axis ( [0 1 ~2 2]) ,bold off ,pause subplot (2,1,1) ,dtplot (n*ts,err) subplot (2,1,2) ,hist (err,10)
```

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## THE DTFT

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 15.2 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 4 15.3 (Solution) z[n] # = X(F)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- = ~j2sin(0.5nr) (0.5)"u[n]

- 15.5 (Solution) Refer to the sketches . pair pair.

<!-- image -->

<!-- formula-not-decoded -->

## 15.6 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The product property of impulses makes the first term in the numerator=0, s0

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 15.7 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 15.8 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b)

<!-- image -->

- 7/12)

- So,
- 15.11 (Solution) Refer to the sketches for magnitude spectra.
- 50 this is a HPF S0,
- ~ ~ 0.5. So, this is an LPF
- the results of part(a) apply. This is a HPF.

<!-- image -->

<!-- formula-not-decoded -->

- H(F)=1 ~ The response shows two humps. This describes a comb filter.

## 15.12 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 1, 1} Create periodic extension of hn] and find response (periodic convolution) using regular convolution plus wraparound.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 15.14 (Solution) I(t) = cos(2ufot), z[n] = Fo = fo/S, 5 = 1 kHz.

1. If fo = 0.2 kHz, Fo = 0.2. With F = 0.25 corresponding to f = 200 we recover y(t) = Hz,
2. 2
3. If fo = 0.75 kHz, Fo = 0.75 = =

With F = 0.25 corresponding to f = 250 we recover y(t) Hz,

- 0.5sin(0.5r) sin(0.5nr) =

## 15.15 (Solution)

- (a) z[n] = sin(0.2n) Since 0.2sinc(0.2n) rect(F/0.2), X(F) = 5rect(5F)
- =
- (c) g[n] = sinc?(0.2n). So, G(F) = X(F)@X(F) = 5tri(5F)

## 15.16 (Solution) See the figure for spectra

<!-- image -->

- =2 cos(2TF)
- X(F) = =

<!-- formula-not-decoded -->

## 15.17 (Solution) See the figures for the spectra.

- (b) z[n] = cos(0.2nm + 7) ~
- (c) z[n] = cos(n),

<!-- image -->

- (d) z[n] = 4) (because F = 0.6 = -0.4) So,
- = cos(O.4nr) (because F = 1.2 + 0.2) 0.2)] S0,
- (f) z[n} =

<!-- image -->

<!-- image -->

## 15.18 (Solution) Refer to the figure for spectra.

- (a) [n] = sinc(0.2n), X(f) = 5rect(5F) (see Prob. 15.15a)
- = X(F) 2 2.5rect[5(F + 0.2)] + 2.5rect[(5(F 0.2)] (modulation)
- (c) z[n] = sinc?(O.In) X(F) = Stri(5F) (see Prob. 15.15c)
- (d) z[n] = X(F) = 2.5rect[5(F+0.05)]+ 2.5rect((5(F-0.05)] (modulation)
- (e) z[n] = 0.2)} (modulation) sinc?

<!-- image -->

(f)

=

<!-- image -->

## 15.19 (Solution)

sinc?(0.2n) cos(0.2nz) ,

X(F) =

<!-- image -->

2.5tri[5(F + 0.1)] + 2.5tri[(5(F

<!-- formula-not-decoded -->

- 1 (b) z[n] X(F) = (folding property) 1 0.5ej27F
- 1 0.75 So, X(F) = 4 (after simplification) 1 1.25

0.1)] (modulation)

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 15.20 (Solution)
- Y(F) =X(-F)

- G(F) = X(F)X(-F) = |X(F)I?
- R(F) = X(4F) (compression)

- H(F) =X(F -0.25)

<!-- formula-not-decoded -->

- B(F) = X(F - 0.25)
- 1] P(F) = = ~X(F ~
- (a) Tbe DTFT of the odd part of z[n] is zero (even symmetric z[n])

<!-- formula-not-decoded -->

- (c) The phase of X(F) is zero (even symmetric z[n])
- (d)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- dF

## 15.22 (Solution)

<!-- formula-not-decoded -->

## 15.23 (Solution) Refer to the sketches.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 15.24 (Solution) r[n] = na"u[n]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 15.25 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## ~2, 0, 1}

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) h[n] = sinc(0.8n) H(F) = 1.25rect(1.25F). The cutoff frequency is Fc = 0.4. S0 only the components at F = 0.25 and F = 0.75 (ie. F =-0.25) appear at the filter output. So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

S0, y[n] =

## 15.27 (Solution) H(F) = A(F)ejs(F) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- Fo = 0.5,

- +e-j2F
- X(F) =1, Y(F) = H(F)
- Fo = 0.25, Ve-jz/4 So,
- Fo = 0.5, H(0.5) =2 =0, y[n] = 0
- (d) z[n] = 1, Fo = 0, H(o) = 2, y[n] = 2
- (e) z[n] = Fo = 0.2, H(0.2) = 4nT
- Fo = 0.25, H(0.25) = 2 y[n} =

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

15.30 (Frequency Response)   y[n] = 1]. Refer the sketch for spectra. to

- (a) H(F) = 0.5(1+e-j2F) = cos(TF).
- Fo = 0.25. So, H(Fo) = 0.257)

<!-- formula-not-decoded -->

- (f) = cosN (TFc) '(0.5)1/2N So, cos(;Fc) = (0.5)1/2N Or Fc 2 T

- (ej2rF
- (b) Phase = 0 Phase delay =0 = group (even symmetric sequence) It is a linear phase filter . delay
- y[n] = 0 S0,
- =-1 S0, y[n] = cos(nr)
- Ifz[n] = = = g cos(2nr/3)

Refer to tbe sketch for spectra.

<!-- image -->

- (b) Phase = 0. Phase =0 group (even symmetric sequence). It is a linear phase filter\_ delay delay
- S0, y[n] = } cos(nr/3)
- So,
- So,

Refer to the sketch for spectra.

<!-- image -->

- (a) H(F) =1 = e-j2rF
- (b) = 0.5. Even symmetric sequence; s0 linear phase filter . delay
- = cos(nr), Fo = 0.5, H(Fo) = 2 y[n] = 2 So;
- (a) H(F) = (0.5+ + 0.5e-j4rF) = e-j2F
- (b) Phase = Phase delay = 1 = group deley. Even symmetric sequence; 50 linear phase filter .
- y[n] = 0.51) = sin(0.5nr) So,
- y[n] = 0 S0, if z[n] = 1+ (-1)" y[n] = 2 (by superposition). So,

<!-- image -->

1} Refer to the sketch for spectra. AX(F)

<!-- image -->

- 15.35 (Solution) h[n) =
- H(F) = S0,
- (b) Phase = group delay. Symmetric sequence, so phase filter. linear
- (c) z[n] = cos(nr/4), Fo = H(Fo) = [3 + 2v2 + = yIn} 4(5.8284) sin( 4) OJe~jr/2 S0,
- =
- S0,
- 0.5 H(F) =
- 1+0.5e-327F Not a linear phase filter . Now,
- 0.75 tg (See Eq: 18.45 and 18.47 in text).
- 0.5 =j (c) zn] = cos(0.5nr), Fo = 0.25, H(Fo) = = y[n] = cos(0.5n7 36.9*) So,
- y[n] cos(nz) S0,
- 36.90)

<!-- image -->

<!-- image -->

3(0.5)" Its periodic extension with period N is hp[n] = 1

<!-- formula-not-decoded -->

So, z[n] * hp[n] = {1ž8,6.4,96,8,3.2,1.6,0.4} and yp[n] = {16,8,10,8} (by wraparound)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 14{1,0.5,0.25} and hp[n] = 4{{, 0.5, 0.25} r[n] * hp[n] = {48, 48, 36, 12, 3} and yp[n] = {60, 51, 36} (by wraparound) So,
- 15.38 (Solution) z[n] = {4, 3, 2, 3} N = 4,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Xp(F) = 3 (F) + 0.58(F - 0.25) + 0.58(F + 0.25) So, get

- (a) h[n] = sinc(0.4n), H(F) = 2.5rect(2.5F). Its cutoff frequency is Fc = 0.2. Only tbe dc component is passed. Y(F) =X(F)H(F) = 7.58(F) and y[n] = 7.5. a sequence (with N = 4), y[n} {7.5, 7.5, 7.5, 7.5} So; As
- (b) H(F) = tri(2F) . Its cutoff frequency is 0.5. It lets through dc (with a of 1) and the components at F = 40.25 (with a gain of 0.5). gain

So,

Y(F) = 36(F) + 0.258(F

As a sequence (with N = 4), y[n] = {3.5, 3, 2.5, 3}

- 1, 1; 1} = hp[n] So,

15.39 (Solution) Refer to the figure

<!-- image -->

<!-- formula-not-decoded -->

- 1 \_ e-j2mF

Tbe overall system is unstable (one root of 1 + 2-1 \_ z-2 = 0 is outside the unit circle)

<!-- formula-not-decoded -->

- H(F) =0.5(1+e-j2rF) 0.5 + 0.5e-j2zF H(F) = The overall system is stable (both roots of 1 + 0.52-1 + 0.52-2 = 0 are inside the unit circle)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) Cascade, œ = 0.5, 1} Hc(F) = 1 So,
- (d) Cascade; œ ~0.5,
- = 0.5, 1] + (0.5)nu[n]
- h2[n] = (0.5)"u[n],

- (b) Parallel, Q = -0.5, y[n] = (0.5)"u[n] So,
- (c) Cascade; œ = 0.5, 1] So,
- (d) Cascade; œ = 0.5,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) Since fts = S, Xi(f) and Xp(F) are identical.
- (c) Xp(F) is the periodic extension of X(f) with period 5 = 1 /ts because the Fourier transform of the ideally sampled (analog) signal is ESX(f - kS). In general; X(f) equals the central period of Xp(F) only if z(t) is bandlimited to 0.5s
- 15.44 (Solution) H(F): ideal LPF (Fi = 0.2), H2(F): ideal LPF (Fi = 0.4). Refer to the figure. (a)
- (a) Ideal HPF with Fc 0.2 : H(F) =1 \_ H(F)
- (b) Ideal HPF with Fc = 0.4 : H(F) =1 \_ H2(F)
- (c) Ideal BPF with passband 0.2 &lt; F &lt;0.4 :
- (d) Ideal BSF with stopband 0.2 &lt; F &lt;0.4 :
- h2[n] = (0.5)"u[n}, c[n] = =

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) Cascade, œ = -0.5, Hc(F) = 1 (see Prob 15.40d). So, y[n] = cos(0.5nr)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (a) H(F) = œ+ =
- (b) To block the frequency F = ;

<!-- formula-not-decoded -->

- = = =
- (a) The echo signal is y(t) = z(t) +0.52(t N = 0.00125S is the integer corresponding to 1.25 ms. delay

## 15.46 (Solution)

- (c) For N = 1.25S to be an integer (where $ &gt; 10 is an = 12 kHz for which N = (1.25)(12) = 15 S0, y[n] 15} and H(F) =1+0.5e-j30TF
- (d) The frequency response describes a comb filter. Tbe transfer function of the inverse system 1 = This describes an inverse comb filter . Tbe difference equation of 1 the inverse filter is y[n] + 0.5y[n 15] = z[n] The frequency response of the overall system is Hc(F) = H(F)H(F) =1
- 15.47 (Solution) Bandwidtb of r(t) is 4 kHz and 5 = 10 kHz to obtain z[n} The passband of the digital filter is 0.03 &lt; F &lt; 0.3
- (a) For f = 60 Hz, F = =0.0006. Tbis frequency is blocked by the BPF .
- (b) For f = 360 Hz, F = 0.036. Tbis frequency will appear in tbe output of the BPF .
- (c) For f = 8.8 kHz; F = 0.88 = 0.12. This frequency will appear in the output of the BPF
- (d) For f = 9.8 kHz, F = 0.98 = 0.02. This frequency will be blocked by the BPF .

## 15.48 (Solution) H(F) = rect(2F)e = rect(2F)e-j2r(0.25)F \_

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) fo = 75 Hz. Fo = 1.25 = 0.25, H(Fo) =} So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

With T = 0.1 (the width of z(t)) and fo = 10 Hz, X[k] = #X(kfo) = 2.5sinc?(0.5k).

- (a) B = 20 Hz: Only dc and fundamental (k = 1 at 10 Hz or F = }) component are passed. = Now,
- (b) are passed. = 0.1126, H(g) =0.25. With (0.25)(0.1126) ~ 0.028, y(t) = So,
- B = 80 Hz. The dc, and harmonics at k = 1,3,5,7 are passed. However the 50 Hz (F = g) and 70 Hz = and \_10 Hz (F =
- (c) (Fg) will be aliased to ~30 Hz (F With X[5] = 2.5sinc? (2.5) = 0.0405, X[7] = 2.5sinc2(3.5) = 0.0207, we find y(t)

## 15.51 (Solution) For s(t) B = 5 kHz. For LPF , fc = 4 kHz

- (b) If z(t) is first sampled to obtain z[n], identical to y[n], the digital filter cutoff frequency must be Fc = 0.4 (to correspond to 4 kHz) Thus, H(F) = rect(F/0.8) and h[n] = 0 .Bsinc(0.8n) we

## 15.52 (Solution)

<!-- formula-not-decoded -->

- (b) Transfer function of tbe compensating filter is Hc(f) = H(f) sinc(fts)

## 15.53 (Solution)

- (b) Transfer function of the compensating filter is Hc(f) = H(f) sinc?( fts)

## 15.54 (Solution) Refer to the figure for spectra.

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) The sketches compare |Hs(F)l and |Hr(F)l with the ideal integrator
- (c) Tick's rule does yield a approximation for 0 &lt; F &lt; 0.25. Yes, good

## 15.55 (Solution) Refer to the sketches.

<!-- image -->

- (a) The reconstructed output will match the filter output:.
- (B) Because of the zero-order-hold, there will be sinc distortion.

## 15.56 (Solution) X(F) = tri(4F), H(F) =

<!-- formula-not-decoded -->

Refer to the sketches for tbe spectra.

<!-- image -->

<!-- image -->

modulate y2[n]

H(F)

=

rect(2F)

Refer to the sketches for the spectra.

<!-- image -->

<!-- image -->

- (c) y[n] is an amplitude scaled (by 4) version of z[n].

<!-- formula-not-decoded -->

The spectrum of y[n] = 22[n] extends to F2 Io ensure y(t) = r2(t), we need F2 &lt; 0.5 or S &gt; 16 kHz.

- 15.58 (Solution) (a) Sampling rate: S1
- =
- = 400 Hz. after sampling; Fi = No aliasing. reconstructed signal is y(t) = 0.5sin(150mt) + 0.5sin(4Ont) So, So,
- (b) Sampling rate: S1 = 200 Hz. So, after sampling; Fi = Fz = 2 (aliasing)
- (c) Sampling rate: S1 = 120 Hz. So, after sampling; Fi = Reconstruction rate S2 = 120 Hz: Upon reconstruction, fa = I20Fi 30, f6 = 120F2 =

## 15.59 (Solution) X(f) = trilf/4000). Refer to the sketches for spectra.

<!-- image -->

y[n)

<!-- image -->

<!-- image -->

40 Hz.

<!-- image -->

<!-- formula-not-decoded -->

- (a) For linear interpolation by N = 2, we require h[n] = tri(n/2) = {0.5, é, 0.5}
- Refer to tbe sketch for part(c) to see H(F)

<!-- image -->

## 15.62 (Solution) Up-sample 1 N ideal LPF y[n]

<!-- image -->

- (a) z@n] = sinc(0.4n),
- (b) X(F) = tri(4F), N = 2, Fc = 0.375.

<!-- formula-not-decoded -->

Fo = = =2 Refer to the sketch for spectra for N = 2 and N = 3 Decimation by N scales the by So, gain

<!-- image -->

<!-- image -->

Note that Y(F) is the periodic extension of the stretched principal range\_

<!-- image -->

The outputs are not identical. In part (b), Y(F) is the periodic extension of the stretched principal range of the filtered signal.

<!-- image -->

<!-- image -->

Tbe outputs are identical for part (a) and (c)

## 15.67 (Solution) = 2 . gain

<!-- image -->

None of the systems produce identical outputs.

## 15.68 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- = 0.25, =2 gain

<!-- image -->

Method 1 and method 2 produce identical results.

Method 1 and method 2 produce different results.

<!-- image -->

- '(c) For identical results; decimation by N must produce a spectrum restricted to {Fl &lt; 0.5. the So,

<!-- formula-not-decoded -->

- (a) Refer to the fgure for spectra.
- (b) Tbe reconstructed spectrum is Y(f) = y(t) = (t 0.5ts) . S0,
- 15.70 (Solution) X(F) = tri(4F). Refer to the figure for spectra.

<!-- image -->

<!-- image -->

<!-- image -->

slope = ~TF

Assume that the LPF has a of 2 The of the phase after the 1-sample delay is ~2TF and after decimation the slope is ~TF. 0.5] gain slope

## 15.71 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## COMPUTATION AND DESIGN

## 15.72 (Solution) Uses the ADSP routine dtplot

```
'PROBLEM 15.72 'PART (a) (2*pi*n*F) subplot,dtplot ') ,axis( [0 30 ~1 1]) ,pause 'PART (b) subplot (2,1,1) ,dtplot (n,yl , ) ,axis( [0 30 -1 1]) subplot (2,1,2) ,dtplot (n,y2, ') ,axis( [0 30 ~1 1] ) ,pause (n,xn,
```

```
'PARI (c) Ja=filter(h2,1,x);yb=filter(hl,1,ya) subplot(2,1,1) ,dtplot (n,ya, ~1 1]) subplot (2,1,2) ,dtplot (n,yb , .'),axis( [0 30 ~1 1]) ,pause 'Reversing the order gives sane overall output 'PART (d) Jlsxn.*xn;y2-filter(h2,1,y1) ; subplot (2,1,1) ,dtplot (n,yl , ) ,axis( [0 30 1] ) subplot(2,1,2) ,dtplot (n,y2, '') axis( [0 30 1]) ,pause 'Reverse ya-filter(h2,1,xn) ;yb-ya.*ya; subplot (2,1,1) ,dtplot (n,ya, ) ,axis( [0 30 1] ) subplot (2,1,2) ,dtplot (n yb, ') ,axis( [0 30 1]) 'Reversing the order does not give sane intermediate or overall output 15.73 (Solution) 'PRDBLEM 15.73 'PARI (a) j=sqrt(-1) ;hl=[1 2 1] ;b2= [2 0 -2] ; F=0:0.005:0.5;Hl=freqz(bl 1 ,2*pi*F) ;H2=freqz(h2 subplot (2,2,1) plot (F,abs(HI)) ,subplot(2,2,2) plot (F abs (H2) ) subplot (2,2,3) ,plot (F ,angle(Hl) ) ,subplot (2,2,4) ,plot (F ,angle(H2) )_ pause is lowpass and H2 is bandpass 'PART (b) 'Claim is false 'PART (c) hpl-hl+h2; hp2=[1 2 1 0]+ [0 2 0 -2] ; subplot (1,2,1) ,plot (F ,abs ( [HP1 ;HP2J )) subplot (1,2,2) ,plot (F , angle ( [HP1 ; HP2] ) ) pause 'PARI (d) HC1-H1 subplot (1,2,2) ,plot (F ,angle ( [HC1 ;HC2] ) ) ,pause 'Claim is true 'PART (e) subplot (1,2,1) (F,abs ( [HCI ;HC2J)) subplot (1,2,2) ,plot (F ,angle ( [HC1 ;HC2] ) ) 'plot
```

```
15.74 (Solution) 'PART (a) b='0.8 'PART (b) F=0:0.005:0.5;H=freqz( [1 0] n=0:2;ht=0.8 D;HT-freqz(ht,1,2#pi*F) ; '3 term truncation subplot (1,2,1) ,plot (F ,abs ( [H;HTJ )) subplot (1,2,2) ,plot (F ,angle ( [H;HI] ) ) ,pause 'PART (c) n=0:9;bt-0.8 '10 tern truncation subplot (1,2,2) ,plot (F angle( [H;HI]) ) 15.75 (Solution) Uses tbe ADSP routine sinc 'PROBLEM 15.75 '(a) Filter 1 is FIR and Filter 2 ius IIR 'PARI (b) F=0:0.005:0.5;Hl=freqz( [1 subplot (1,1,1) ,Plot (F ,abs ( [H1 ;H2;HS] ) ) 'PART (c) Sinc boost is provided up to about F=0.3 by each filter 15.76 (Solution) 'PROBLEM 15.76 'PART (a) (F ,abs(X)) 'PART (b) [m;zeros(size(x))] subplot (2,2,2) ,plot (F abs (Y)) 'PART (c) subplot (2,2,3) ,Plot (F ,abs (Z)) 'PARI (d) subplot (2,2,4) ,Plot (F ,abs (G)) 'ote hov the frequency F-0.2 F=0.6 and is aliased to F=0.4 ,plot
```

```
15.77 (Solution) Uses the ADSP routines urect, tri 'PROBLEN 15.77 (a) F=0:0.005:0.5;HC-freqzíhc,1,2*pi*F) ;HL=freqz(hl,1,2*pi*F) ; H=N*urect (N#F); 'Ideal interpolation subplot (2,1,1) ,plot (F ,abs ( [HC ;HL] ) ,F ,H) F=0:0.005:0.5 ;HC-freqz 1 ,2#pi*F) ; HL=freqz(hl,1,2*Pi#F) ; H=Nturect(N#F); 'Ideal interpolation 15.78 (Solution) Uses the ADSP routine dtplot , tri, sinc, dtplot 'PROBLEM 15.78 N=8;xu=[xn;zeros (N-1,4)];xu=xu(:)' ; 'PARI (a) (0:4+N-1) ; '*') ,hold on,dtplot (n*",xn,'0' 'n'),hold off ,pause 'PARI (b) nu=(0:4+N-1) ; 'Use filtfilt for linear phase filtering xn,'0' ,'n') ,hold off ,pause 'PART (c) dtplot (nu-N,Yl ,'*') ,hold on,dtplot (n*"_ 'PARI (d) 'dtplot(u-M,Ji,'*') ,hold on,dtplot (n*N,xn,'0' pause 'More signal samples means more periods D=0:7 xn=cos(0.S*pi*n) ; (hc,
```

```
M=8;m=-M:M;hi-sinc(u/M);yi-filter(hi,1,xu) ; dtplot (nu-M,yi, 4'
```

## 15.79 (Solution) Uses the ADSP routine dtplot

```
'PROBLEM 15.79 F0-22.5/180;F1=60/180; 'Filter gain should be zero at FI For uit gain at FO, a=1/(l+sqrt(2)) a=1/ (1+sqrt (2)) ;h=[a a a] ; subplot (2,2,1) ,dtplot(n,x) ,subplot (2,2,2) ,dtplot (n,s) subplot(2,2,3) ,dtplot (n,g) subplot (2,2,4) ,dtplot (n,y) 'So ,
```

## 15.80 (Solution)

```
'PROBLEM 15.80 'See problen 18.28 for analytical details 'Filter H(2)=z/(2-0.5) ; H=z/ (2-0.5) ;A=abs (H) ,t=angle(H) tpO=-t/2/pi/FO;tp=-tpO; 'need delay of allpass filter to balance out tpO_ 'For a first order allpass filter H(z)=(l+az) / (z+a) and 'Exact result (See Prob 18.28) 'Exact result at FO 'Test the filter J=[1 0] ;D=[1 ~0.5] ;NA=[a 1]/A;DA=[1 a] ; pause 'NOTE tbat and is unstable So vorkaround is to 'add pi to the phase of H(F) and also add pi (~ sign) to HA (z) tpO=-(t+pi)/2/pi/FO;tp=-tpO; a=sin((1-tp)*pitFO)/sin((l+tp)*pi*FO) 'Exact result [t ta] 'Actual/allpass phase at FO 'Test the filter N=[1 0] ;D=[1 ~0.5] NA=-[a 1J/A;DA= [1 a] ; n=0:50;x=cos (2*pi*FO+n) Jlsfilter(N,D,x);y2-filter(NA DA ,yl) ; plot (n,x,n,y2) 'Identical results except for startup transients
```

```
15.81 (Solution) the ADSP routine randist 'PROBLEM 15.81 1=0:300;x=1-(0.6."2) xn=xtrandist(x uni' ,0) ;F=0:0.005:0.5;"=2*pi*F; N3=[1-a 0] Hl=freqz (hl,1,") ;H2=freqz(h2,1,w) ;H3=freqz(N3,D3,") ; plot (F= abs ( [H1 ;H2 ;H3] ) ) Pause xfl=filter(hl,1,xn) ;xf2-filter(h2,1_ xn) ;xf3-filter (13,D3,xn) ; plot [x;xfl;xf2;xf3]) ,pause N=9;k=0:N-1;hl=ones (1 a= (N-1)/ (N+1) [1 -a] N3=[1-a 0] ; plot (F_ abs ( [H1 H2;H3] ) ) ,pause xfl-filter(hl,1,xn) plot (n, [x;xfl;xf2;xf3]) , Uses (n, ;D3=
```

## 16.1 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## THE DFT AND FFT

<!-- formula-not-decoded -->

NOTE: In simplifications; use = +j e-jt/2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

IN = 0 for n = 0 e-jnk2m

<!-- formula-not-decoded -->

## 16.2 (Solution)

<!-- formula-not-decoded -->

Since XDFT[k] is conjugate symmetric; we expect z[n] to be real (but not conjugate symmetric) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

16.3 (Solution)

- S0,

<!-- formula-not-decoded -->

- 16.4 (Solution) N =4
- = {1, -2, 3, -4}

- 16.5 (Solution) N-fold replication of z[n] yields an amplitude-scaled by N, zero interpolated DFT. N-fold zero interpolation of z[n] yields N-fold DFT replication.
- (c) {z[n/2]} + {1,2,3,4,5,1,2,3,4,5}
- (d) {z[n/3]} + {1,2,3,4,5,1,2,3,4,5,1,2,3,4,5}
- 5 or Its nonzero DFS samples are The Nyquist sampling rate for a pure sinusoid is $ = 2f or 2 samples per period. e-jn/6
- (a) 4 samples /period over 1 period. Spectral spacing = = fo. So-index of

<!-- formula-not-decoded -->

- (b) 4 of nonzero samples is k = 2 (at fo) and k = N \_ 2 = 6

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- = fo. S0 index of nonzero samples is k = 1 (at fo) and k = N \_ 1 = 7

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) 6 samples /period over 3 periods. of nonzero samples is k = 3 (at fo) and k = N \_ 3 = 15 So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (e) 1.6 =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 1.6 samples /period over 10 periods\_ N = 16, 5 = 1.6fo. There is aliasing. Spectral spacing = S0 index of nonzero samples is k = 10 (for the component at fo) and k =N \_ 10 = 6 S0,

<!-- formula-not-decoded -->

So, XDFT = {0,0,0,0,0,0, 8ejr/6

## 16.7 (Solution)

- (a) z(t) cOS F = g Io prevent leakage; we must sample for 2 ful] periods. So N = 25 and spectral spacing = The nonzero DFS samples are 0.5 So,

<!-- formula-not-decoded -->

- (b) z(t) = cos(20mt) + 2sin(4Ont) N = 15, 5 = 25 Hz. Spectral spacing = 9 = Hz. Now, f1 = 10. S0 the index of nonzero DFS samples is k = 6 (DFS value 0.5) and k = N - 6 = 19. Also, f2 = 20 Hz, so k = 12 (DFS value = = ~j) and k = N \_ 12 = 13. e-jn/2

<!-- formula-not-decoded -->

- (c) z(t) = = 25, = 25 Hz. Spectral spacing = = 1 Hz. Now; f1 = 5. So the index of nonzero DFS samples is k = 5 (DFS value ~j0.5) and s0 k = 20 (DFS value = = (DFS value = = j) So, the combined DFS value at k =5 is j0.5. {because the 20 Hz component aliased to 20 - S =-5 Hz) Hz, gets

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This result is identical to the DFT of y(t) = sin(lOnt) sampled at $ = 25 Hz with N = 25.

<!-- formula-not-decoded -->

if we sample over 4 periods; N = =100 and spectral spacing = So,

For f1 = 20 we find k = 8 (DFS value = = ~j0.5) and k = N \_ 8 = 92. For f2 = 30 Hz, we k =12 (DFS value = = ~j) and k = N \_ 12 = 88. Hz, get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 16.8 (Solution) Io avoid aliasing; sample at higher rate. To avoid leakage; sample for integer periods

- (b) fo = 100, = 70 Hz. S0, Fo = 10 There is aliasing. There is leakage because we are not sampling for multiples of 10 full periods.
- (a) S0 sampling {or 2 periods causes no Jeakage
- (c) fo = 100, = 4 We obtain 10 samples by sampling 2.5 periods; s0 there is leakage. Because of leakage; there is also aliasing (even though $ = 400 Hz)
- (e) f1 = 100, f2 = 150 Hz. S0, fo = 50 Hz or T = 20 ms. S0, for 100 ms, we are sampling for 5 full periods. So, n0 leakage   Since $ = 450 there is no aliasing. Hz,
- 10 (d) fo = 100, S = 70 Hz. Fo = There is aliasing. There is leakage because we sampled for 2.5 periods. So,
- (f) f1 = 100, f2 = 150 Hz. Since we are sampling for a half-period; there is leakage.   Because of tbere is also aliasing (even tbough $ = 400 Hz) leakage,
- (h) Square wave with period T = lOms for 1.5 periods at 4OOHz. Both leakage and aliasing present.
- = 1Oms for 2 periods at 4OOHz. Leakage absent but aliasing present.

## 16.9 (Solution) N = 500, S = 1 kHz. So, spectral spacing =

## 16.10 (Solution) Signal duration = 1 s B = 50 Hz. 5 = 100 Hz So,

- N 200 But the 1 s record yields only 100 samples. S0, padding zeros 200-100=100 So,
- (a) N = (S) (duration) = 100. Spectral spacing Af = ; = 1 Hz
- (c) Spectral spacing Af = 9 =0.5 Hz. So, N = 200 = N = 256 (for FFT) number of padding zeros is 256 100 = 156. So,

## 16.11 (Solution) Lz = 12, Ly =20

- (b) If z[n] is padded with 8 zeros, both sequences have 20 samples.  'Their periodic convolution also has 20 samples. This regular convolution has 39 samples. Io find the periodic convolution; 19 samples are wrapped around S0, tbe 2Otb sample is left uncontaminated. Since the last 8 samples of the regular convolution are zero (due to padding) the 12th and 19th samples will thus also be uncontaminated after wraparound.
- (a) Tbeir regular convolution has length Lz = =31. z[n] requires 31-12=19 padding zeros, y[n] requires 11 padding zeros. So,

The (nine) uncontaminated samples thus correspond to the index k = ll to k = 19.

```
16.12 (Solution) (b) {0,~1,2,-3,4,-5,6,~7} = {000,001,010,011,100,101,110,1l1}
```

```
So, the bit-reversed sequence is {1,3,2,4} So,
```

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (a) Refer to the fowchart for the 8-point DIF algorithm.

~2(1+j)

<!-- image -->

- (b) Refer to the fowchart for the 8-point DIT algorithm.
- 16.14 (Solution) Signal duration =1 5 B = 100 Hz. S = 200 Hz Spectral spacing Af &lt; 0.5 Hz So,
- = 400 So,

<!-- image -->

With N = 400 the actual spacing is Af = | = 0.5 Hz, as required.

- = 0.5. N = 2S = 400 = 512 (for the FFT) With N = 512 the actual spacing is Af = 9 ~0.39 Hz, less than required. So,
- h[n] = {1,2,3}
- (a) the sum by column method, Using

<!-- formula-not-decoded -->

- (b) Tbe DFT requires both sequences to be zero-padded to the convolution length N = 5 h1[n] = {1,2,3,0,0} We compute the DFT and their product

<!-- formula-not-decoded -->

The IDFT of Y gives y[n] = {1, 4,8,8,3}, as before.

- (c) The FFT requires both sequences to be zero-padded to N = 8

We compute the DFT and their product. We list results only up to the index k = 4

<!-- formula-not-decoded -->

Tbe IDFT of the &amp;-sample Y gives y[n] = {1,4,8,8,3,0,0,0} . Note the 3 trailing zeros.

- h[n} = {1,2,3}
- S0,
- (b) the DFT; We compute: XDFT[k] = {4, ~0.50 j0.87, ~0.50 + j0.87} , HpF[k] = {6,~1.50+j0.87, ~1.50 j0.87 Using

Their element-wise product gives YoFT[k] = {24; 1.50+j0.87, 1.50 j0.87} Its IDFT gives yp[n} = {9, 7, 8}

- (c)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This result does not match the previous two. Reason: the sequences are now assumed to be periodic with period 4 (not 3)

- 16.17 (Solution) z|n} = {1,2,1} h[n] = {1,2,3}
- (a) Tzh = [n) * h[-n] = [n] * {1,3,2} (by circular folding) Tprh[n] = {8,7,9} (by wraparound)
- (b) Using the DFT, we compute ~0.50 + j0.87, HpFT[k] = {6, ~1.50 - j0.87, ~1.50+ j0.87} . = {24, j1.732, -j1.732 and rpzh[n] = {8,7,9}
- h[n] = {1,2,1,3,2,2,3,0,1,0, 2,2}
- (a) (Overlap Add)   Split h[n] into

<!-- formula-not-decoded -->

Find their regular convolution with z[n] and shift successively by 3 samples to get

<!-- formula-not-decoded -->

- (b) (Overlap Save) Let L = 12, N = 3. Create the zero-padded sequence h1[n] = {0,0,h[n]} of length 14 (L+N -1) Choose M = 5 and create overlapping by 2(N \_ 1) 5-sample sections of h1 [n] (zero-pad the last section to length 5, if necessary) to generate

<!-- formula-not-decoded -->

Zero-pad z[n] to length 5, find its PERIODIC convolution with each of the above segments, discard the first 2(N \_ 1) samples from each convolution and concatenate. Here are the results

| Periodic convolution    | Result       | Save     |
|-------------------------|--------------|----------|
| {1,2,1,0,0}@{0,0,1,2,1} | {4,1, 1,4,6} | {1,4,6}  |
| {1,2,1,0,0}0{2,1,3,2,2} | {8,7, 7,9,9} | {7,9,9}  |
| {1,2,1,0,0 2,2,3,0,1}   | {4,7, 9,8,4} | {9,8,4}  |
| {1,2,1,0,07 {0,1,0,2,2} | {6,3, 2,3,6} | {2,3, 6} |
| {1,2,1,0,0} {2,2,0,0,0} | {2,6, 6,2,0} | {6,2,0}  |

Glue the saved samples together to give y[n] = {1,4,6,7,9,9,9,8,4, 2,3,6,6,2,0}

Tbe extra zero at the end is due to zero-padding of last section of h[n]

- (c) Using the sum by column method, we get

<!-- image -->

Tbis agrees with tbe previous results.

## 16.19 (Solution)

<!-- formula-not-decoded -->

For odd N, tbere is no integer index corresponding to k = 0.5N.

Thus, 2 DFT samples are real if N is even; and 1 sample is real if N is odd.

## 16.20 (Solution) XpFT[k] is the DFT of a (possibly complex) signal z[n]

- (a) If XDFr[k] is conjugate symmetric; then z[n} is real.
- (d)
- (e) XDFT[k] is imaginary and odd symmetric; then z[n] is real and odd symmetric.

## 16.21 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Note: We could also use Parsevals theorem Ez?[n] = k=0

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 16.23 (Solution)

- () cos(nn) = X[k] = 0.5N]
- 8 [n] = J[n - 0.5(N ~ 1)] (N odd); X[k] = =
- r[n] = X[k] = NS[k \_ 2] (Use tbis in i,j)
- (j) z[n] = X[k] =
- = X[k] = (k = 2)]

A typical DFT term XDFT[n] has the form Let 2nkuN = % Aeje .

The IDFT gives z[n] with terms of tbe form =

If we conjugate XDFr[n], a typical term becomes Its DFT gives terms of the form Ae-j0 = Ae~j0 e-jø

- N = 8
- So, G[k] = {1, ~2,

## 16.26 (Solution) I(t) =

- (a) 25 Hz corresponds to the index k = 25 = 3.125. Also, 100 Hz 8 corresponds to the index k = = 12.5. The spectral peaks will not occur at the frequencies of the original signal So,
- (b) Let N = 128, Af = š = 6.25 Hz. 25 Hz corresponds to the index k = 25 =4 Also, 6.25 100 Hz corresponds to the index k = 16. the spectral peaks correspond to tbe exact frequencies of the original signal. So, So,
- k])
- ~j2, 1+j, ~2, 1, ~2, 1 - j; j2} (shift)
- H[k] = 3X[k/3] (signal replication DFT zero interpolation) S0,

- (a) N = 100, = =1 Hz. 25 Hz corresponds to the index k = 25 Also, 40 Hz corresponds to the index k = 4 2 40. the spectral peaks correspond to the exact frequencies of the original signal. So, So,
- (b) N = 128, Af = =32. 40 Hz corresponds to tbe index k = 49 =51.2 So, only the spectral peak at k =32 corresponds to the exact frequency (25 Hz) of the original signal.

## 16.28 (Solution) S = 100 Hz and 128 signal samples.

- (a) N = 128. Af = = 21 Hz corresponds to k = = 26.88. there will be no DFT component at exactly 21 Hz. Since k = 26.88 ~ 27, the frequency closest t0 21 Hz that can be identifed is f = kAf = 21.0938 Hz So, So, So,
- (b) Assuming zero-padding; the 21 Hz component will correspond to an integer index k if k9 = 21 Or k = 214 is an integer. So, k = O.21N, or N 200, etc. With N &gt; 128, the smallest value is N = 200. Thus; we require 200 128 72 padding zeros and the index of the 21 Hz component is k = 42

## 16.29 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

S &gt; 2(3.18) = 6.36 Hz Choose $ = 6.5 Hz. S0,

Now, |z(t)lmax =1 and maximum when = 0.01 or t = In(100) = 4.61 s et its

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

S0, $ &gt; 2(0.694) = 1.388 Hz. Choose $ = 1.4 Hz

Now, z(t) = = 0.01/e. Numerically; t = 7.64 s. te-t So;

= 1/e Imax

- (c) z(t) = tri(t) X(f) = sinc? (f), = 1 S0, |X(f)l = 0.05Xmax N =2S ~ 4 Xmax So,

<!-- formula-not-decoded -->

The duration D that contains 959 of tbe signal energy is found from

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- S = 31.8294 Hz Then, N = DS ~ 48.
- (b) the in-band signal energy must exceed 999 of the total signal energy.

<!-- formula-not-decoded -->

Tben, N = DS ~ 31.

- 16.31 (Solution) The original signal æ(t) is a periodic square wave with duty ratio 0.5 and T = 2 and sampled for 1 full period. It is half-wave symmetric and components at 0.5 Hz and its odd multiples. Refer to the figure. has

<!-- image -->

The signal y(t) = A + Bsin(zt) includes a dc component and components at +0.5 Hz (with purely imaginary DFT)

- (a) The smallest possible value is N = 3. The sampled signal will be {0.5, 1, 0} However, X[1] (at 0.5 Hz) will not be purely imaginary. Tbis is not a valid choice

For N = 4, zn] = {0.5, 1, 0.5, 0} Its DFS is {0.5, -j0.25, 0, j0.25} Tbis corresponds to

For N = 5, c[n] = {0.5, 1, Its DFT contains a nonzero component at 1 Hz (k = 2). This is not a valid choice.

For N 2 6, tbe DFT shows components at 1.5 Hz (k = 3) and beyond. not a valid choice So,

- (b) For Iadix-2 FFT the only choice we have to consider is N = 4.
- (c) It is not possible for y(t) to be identical to I(t) for any choice of sampling rate because r(t) (a periodic signal) is not bandlimited.

- 16.32 (Solution) T =2 is sampled for one full period to obtain N samples. The signal reconstructed from the N-point DFS of the samples is y(t)
- (a) There will be no leakage leakage because z(t) is sampled for 1 full period.
- (b) For N = 8, we can identify k &lt; 3 harmonics (k = 4 will be at the Nyquist frequency and give meaningless results) For y(t) = r(t) the periodic signal must have been bandlimited to 0.5Nfo =2 Hz
- (c) For N = 12, we can identify k &lt; 5 harmonics (k = 6 will be at the Nyquist frequency and give meaningless results) . For y(t) = z(t) the periodic signal must have been bandlimited to 0.5Nfo = 3 Hz

## 16.33 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 16.34 (Solution) = f1 = 75, f2 = 90 Hz
- (a) Tbe minimum sampling rate to prevent aliasing is Smin = 180 Hz
- (b) S = 2Smin = 360 Hz. Fi = 3 and F2 = % = = 4The minimum number of samples required to prevent leakage is Nmin = 24 So,
- (c) S = 2Smin = 360, N = 3Nmin = 72. = So the index of the nonzero DFT samples is k = 15, k = 18 and k = 54, k = 57. The DFT values will be 0.5N = 36

<!-- formula-not-decoded -->

- (d) $ = 160 N = 256. So, Af = the 75 Hz appears at k = = 120 and the 90 Hz appears at k = = 144. There is no leakage because the frequencies appear at the exact indices (or F1 = 1 = Nmin 32 and N = 256 is an integer multiple there is also aliasing: Hz, So, So,

- 16.35 (Solution) z(t) = cos(5Omt) cos(80nt), f1 = 25, f2 = 40, $ = 200 Hz.
- (a) Fi = 2 = and F2 = 2 = 5 = The minimum number of samples required to prevent leakage is =40 Nmin
- (b) If z(t) is sampled for 1 s, N = 200. Fi = 2 and F2 = 2 The indices of the nonzero components are k = 25, 175 and k = 40, 160. The DFT values at these indices are 0.5N = 100. So,
- (c) With N = 128, Af = 229 So, the 25 Hz appears at k = = 16 and 40 Hz appears at 40 k = 25.6 ~ 26. Af

## 16.36 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) Aliasing will occur if Fo &gt; 0.5. Leakage will occur if the duration KT, an integer number of periods. For no leakage; KT = } o K = fs For K to be an integer , equal
- (c) N =8,F 0.25, 50 no = 50 no =2

<!-- formula-not-decoded -->

- 4, leakage (duration 25+0.125k)

Now, XDFT[k] =0 for all k except k = 2 or k = 6 when the first (or second) term becomes indeterminate.

- There is alíasing- Now Fo = So, no leakage. Since Fo = 1.25 = 0.25, we obtain the same DFT as in part(c)

<!-- formula-not-decoded -->

## 16.37 (Solution) S = 5

- (a) If N = 1000, the frequency resolution is Af = ; = 5 Hz
- (c) If Af = 2 Hz with no window; we require N = =2500
- (b) For tbe von Hann windowed DFT, Af = =
- S0, leakage is present. 1 =
- (d)
- =5000

## COMPUTATION AND DESIGN

## 16.38 (Solution) the ADSP routine convp Uses

```
'PROBLEM 16.38 y=[x(1) fliplr(x(2:N))J;Y=fft(y);Y1=[X(1) fliplr(X(2:M))J; [Y;Y1] Pause Pause [G;G1] pause Pause 'F=0.25 50 shift P1=0.5* [X(7:8) X(1:6)]+0.5*[X(3:8) X(1:2)]; [P;P1] ,pause r=x pause s=convp(x,x) ;S-fft(s);S1-X.*X; [S;81]
```

## 16.39 (Solution)

```
'PRDBLEM 16 .39 [x;xx] ,pause 'Part (a) no relation Jy=fft(0.l*conj(X));[x;yy] 'Part (b) result is conjugate of x[n] 'Part (c): Find FFT(conj(X))/N and corjugate the result to x [n] get
```

## 16.40 (Solution) Uses the ADSP routine vindow

```
'PROBLEN 16 .40 'PART (a) plot (f,X) axis( [90 110 0 inf]),grid,pause 'Need larger N ,N) ; XB=abs (fft(xb,N1))/N1;plot(f,XB) axis( [90 110 0 inf]) ,grid,pause N xb=x #windov( 'black' ,N) ; XB=abs(fft(xb,N1)) /Nl;plot(f,XB) axis([90 110 0 inf]) ,grid,pause 'PART (b) SWITCH TD normalized dB scale for magnitude ~60 0] ) pause plot (f,20*l0g10(X/nax(X))) ,axís( [90 110 -60 0]) ,grid,Pause 'grid_
```

```
axis( [90 110 ~60 0]) ,grid ,pause xb=x.*window ( 'vonh' N) ;XB-abs (fft(xb,N1))/Nl;plot (f,20+10810 (XB/max(XB))) = axis( [90 110 -60 0]) ,grid,pause axis( [90 110 -60 0]) ,grid,pause axis( [90 110 ~60 0]) grid,pause 'The blackran window seens to clear results Bive
```

## 16.41 (Solution)

```
16.41 'PARI (a) x=[1 2 1 2 3 3 5] ;yr=conv(x,b) L=lepgth(yr) ; xI=[x 0 0 X2=fft(x,16) ;H2-fft(h,16) ;y2-real(ifft(X2.+H2)) [yr;yl(l:L);y2(1:L)J LAll give sane results. Extra samples are all zeros 'PART (b) yp-perext (yr,5) X2=fft(x,16) ;H2-fft(h,16) ;yp2-real(ifft(X2.*H2)) ypl; 'Only tbe first two give the sane results [yP; -
```

## 16.42 (Solution)

```
'PROBLEM 16.42 nl-0:4;x=4*(0.5 'Part (a) (b) X2=fft(x,N+2) 'Part (c) X3=fft(x,"-2) 'Part (d) 'Only results of parts a,b and vill match
```

## 16.43 (Solution) Uses tbe ADSP routine dtplot

```
'PART (a) Sigal x is periodic_ Can identify only magnitude fromn FFI uni ,0) ; subplot(2,1,1) ,dtplot(n(1.32) ,x(1.32) ' .') X=fft(x);f=n*S/N; subplot(2,2,3) ,plot (f,abs(X)) ,subplot (2,2,4) ,plot (f,angle(X)) ,pause 'PART (b) Signal y is not periodic Can identify only magnitude fron FFT Y=fft(y);f=n*S/N; subplot (2,2,3) ,plot (f ,abs (Y)) subplot (2,2,4) ,plot (f ,angle(Y)) ,pause 'PART (c) Signal is not periodic Cannot identify anything from FFT z=x.*5;subplot (2,1,1) ,dtplot(n(1:32) ,2(1.32) subplot (2,2,3) ,plot abs (Z)) ,subplot (2,2,4) ,Plot (f ,angle(Z) )
```

## 16.44 (Solution)

```
'PROBLEN 16 .44 load ecg;load ecgo 'Matlab indexing starts at 1 t=(O:N-1)/S;plot(t,ecgo,t,x,'-') 'Results matcb
```

## 16.45 (Solution) Uses the ADSP data fles ecg.mat, ecgo.mat

```
'PROBLEM 16.45 load ecg;load ecgo ecg=ecg(1:512) X=fft(ecg) Xl-X;i-[kl 'Matlab indexing starts at 1 'KResults do not quite match plot (n,abs (X) ) pause 'Use FFT to pick broader range to zero out % Zero out 40 sample range centered at kl 'Results are much improved
```

## 16.46 (Solution) Uses the ADSP data file nysteryl.mat

```
'PROBLEM 16 . 46 load mysteryl; subplot(2,2,1) plot(n,mysteryl) pause X=fft(uystery1);subplot(2,2,2) ,plot(n,abs(X)) ,pause 'Use FFT to remove low freq signal (with large FFT nag)
```

```
subplot(2,2,4) ,plot (n,abs (X)) pause 'Identify range of bi noise and zero it out nessage-real(ifft(X));subplot(2,2,3) ,Plot(n,uessage) 'Message says HI freq
```

## 16.47 (Solution) Uses the ADSP routines randist, blt2ord

```
'PROBLEM 16 .47 uni' ,0) ; XN=fft(xn) ;subplot (2,1,1) 'PART (c) Design notch filter [nl 1,0.005,1/12) ; ylsfilter(nl,d1 x);Ylsfft(yl) ;subplot (2,1,2) ,Plot (n,abs (Y1)) subplot(2,1,1) ,plot (n,x) ,subplot (2,1,2) ,plot (n,yl) ,pause 'PART (d) b=ones(1,10)/10; '10 point moving average filter, you can others subplot(3,1,1) ,plot (n,x) ,subplot (3,1,2) ,plot (n,Jl) subplot (3,1,3) ,plot (n,J2) 'To quantify, we need to fit a straight line to filtered data. polyfit P-polyfit(n,y2,1) 'ist order ,Plot try Try
```

## 16.48 (Solution)

```
'PROBLEM 16 .48 ones (1 ,M) zeros(1,N-2#M-1) ones (1 ,M)]; X=fft(x);Y-X.*H;y-real(ifft(Y));subplot(3,1,1),plot(n,x,n,y) ,axzaxis; 'PART (b) 'Double lepgtb M-fix(W#fc/s) K=[1 ones (1 ,M) zeros(1,N-2#M-1) , 'No improvenent 'Double length ones (1 ,M) zeros(1,N-2*M-1)= ones (1,M)J; 'PARI (c) ones (1 ,M) zeros (1 ,N-2*M-1) , ones(1,M)J; b=real(ifft (H)) ; ) 'Sane number of points F=0.25*(0: 4*N-1) /N; subplot(2,1,2) ,Plot(F*S ,abs(HA) ,Fl*S ,abs(H) ) pumber of points
```

```
16.49 (Solution) 'PROBLEM 16 .49 'KPARI (b) subplot(2,2,1) ,plot (nl,y-y1) _ 'PART (c) G-8*X;Y=[G(1:0.5#N+1) zeros(1,28) G(0.5#N+2:N)];y_real(ifft(Y)); subplot(2,2,3) ,Plot (nl,y-yl) 'PART (d) The periodic extension of Part (a) is sinusoid, 50 bandlinited 'and leads to perfect interpolationIhe periodic extension of Part (c) '(half cycle sinusoid) is bandlinited. any is not high enough 16.50 (Solution) Uses the ADSP routine dtplot 'PROBLEM 16.50 subplot (2,2,1) , dtplot (F ,abs (X)_ .') ,axis( [0 0.5 0 inf]) 'PART (b) subplot (2,2,2) ,dtplot (F2,abs (X2) ) ,axis( [0 0.5 0 inf]) 'Can recover X by bandlimited interpolation 'PART (c) ) ,axis( [0 0.5 0 {nf]) 'Iot sufficiently bandlimited. DFT shows only F=0.4 corresponding to F=0.1 'Upon decimation F-0.2 = F=0.6 which is aliased to F=0.4 'Cannot recover by bandlinited interpolation 16.51 (Solution) 'PROBLEM 16.51 'PARI (a) (1:12) N=length(x) R=3;C=4;y-reshape(x,R,C) ;'Reshape x into RxC matrix (fill along coluns) 'Replace each by its DFT times W=exp(-j*2*pi*r*c/n) uhere 'r=0 for row1, for row2 r=R-1 for rowR and c=0:C-1 (for each rov) for k=l:R,y(k,:)=fft(y(k,:)).*exp(-j*2*Pi*(k-1)*(O:C-1)/N) ;end 'Now, replace each colunn by its for "Read out the result by rowS ot So , X=
```

```
;yl=reshape(y,size(x)) ; 'PARI (b) Repeat R=4;C-3;y=reshape(x,R,C) ; for k=l:C,y(:,k)=fft(y(:,k)) ;end,y=y. y=reshape(y,size(x)) ; 'PART (c) and (d) X=fft(x);[X yl y] 'All give the same result 16.52 (Solution) Uses the ADSP routines tinefreq 'PROBLEM 16.52 'PART (a) n=0:599 subplot (2,2,1) ,plot (n/600,abs (fft(x))),axis( [0 0.5 0 inf]) subplot(2,2,3) ,timefreq(x) ; 'PART (b) cos #pi)]; subplot(2,2,2) ,plot (n/600 ,abs (fft(y))) axis( [0 0.5 0 inf]) subplot(2,2,4) ,tinefreq(y) ; 'Part (c) Iinefreq shows the spectrum as it evolves in tine_ FFI does not 16.53 (Solution) 'PROBLEM 16.53 'PART (a) x=[1 2 3 4] ;b= [1 h (+ trailing zeros) 'PART (b) X=fft(x,L);Y=fft(y) ;H2=Y./X;b2-ifft(H2) 'h2 natches h (+ trailing zeros) 'PART (c) x=[1 2 ~3] ;b=[1 2 H3=Y./X;hB=ifft(H3) 'Meaningless (division by 0) 'Replacing 0 by nunber totally different results. 16.54 (Solution) 'PROBLEM 16.54 j=sqrt(-1) ;N=4;x=[1 2 3 4];y=[5 6 7 8] X=fft(x);Y=fft(y); g-x+j*y;G-fft(g) gives
```

## 16.55 (Solution) Uses the ADSP routine quantiz, window

```
subplot (1,2,1) ,plot(f,X) ,subplot (1,2,2) ,plot (f ,20*10g10(X)) ,Pause (b) Rounding 0) ;Y=abs (fft(y)) ; subplot (1,2,2) ,plot (f,20*10g10(X) ,f ,20*10810 (Y) 1 = ) ,pause B=1;L=2-B;y-quantiz(x, [0 255] ,L, subplot (1,2,1) ,plot (f ,X,f,Y,'--') , 'Spurious frequencies show up ) ,pause 'PART (c) Iruncation subplot(1,2,1) ,plot(f,X,f,Y,'--') = ') ,pause B=1;-2-B;y=quantiz(x, [0 255] ,L, t' ,0) ;Y=abs (fft(y)); subplot(1,2,1) (f ,X,f,Y,'--') , subplot (1,2,2) ,plot(f,20*log1O(X) ,f,20*10g10 (Y) ' ~') ,pause 'IPART (d) Windoving vonh 256) '~') , pause subplot (1,2,1) ,plot (f ,X,f,Y,'--') = subplot (1,2,1) plot (f,X,f,Y,'') subplot (1,2,2) ,plot(f,20*l0g10(X) ,f,20*l0g10 (Y) 'Repeat for truncation Windowing leads to more noise ,plot
```

## 16.56 (Solution) Uses the ADSP routines randist, vindov

```
'PROBLEN 16.56 f=n#S/N;x=cos X=abs(fft(x));plot(f,X) 'PART (b) 4=0.01;ton=tntrandist(tn,'uni
```

```
A=0.1;tnn=tntrandist(tn, uni 0)#A/S;xn=cos(2*pi*fO*tnn) ; A=l;tnnstntrandist(to,'uni XN-abs(fft(xn)) ;subplot(2,2,3) ,Plot(f ,X,f,XN,' --') (2+pi*fOttnn) ; 'Cannot identify spectrum noise floor) 256) ;A=0.01 ;tnn=tntrandist(tn,'uni O)*A/S ; XN-abs(fft(xn)) ;subplot(2,2,1) A=0.1;tnn-tntrandist(tn, uni 0)#A/S;x-cos(2*pitfO*tnn) #w ; XN=abs (fft(xn));subplot(2,2,2) ,plot (f ,X,f,XN uni xn=cos '~) 'Cannot identify spectrum (tn, *w;
```

## 17.1 (Solution)

## 17.3 (Solution)

## THE z-TRANSFORM

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.2 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.4 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.7 (Solution) X(z) = (2)"u[n] = z[n]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.8 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.9 (Solution)

- (a) By division Jong

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) By long division

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.10 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.11 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 2 (b) X(z) =

<!-- formula-not-decoded -->

- (i) X(z) =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.12 (Solution)

- (a) By long division

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 22 + 52 17.13 (Solution) X(z) = 2?

<!-- formula-not-decoded -->

- [2(3)" \_ (-1)"Ju[n]
- (c) ROC 1 &lt; |zl &lt; 3. S0, z[n] is two-sided; with anti-causal part 7zl &lt; 3) and causal part

<!-- formula-not-decoded -->

## 17.14 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.15 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

final value = 0 So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Poles inside unit circle (lzl &lt; 1). So, final value = 0

<!-- formula-not-decoded -->

Final value theorem does not hold (one root is outside unit circle).

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Final value = 0 (all inside the unit circle) . poles

<!-- formula-not-decoded -->

## 17.16 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Unstable (pole is outside the unit circle) .

<!-- formula-not-decoded -->

Unstable (or marginally stable) (because one root z = 1 is on the unit circle)

<!-- formula-not-decoded -->

inside unit circle) poles

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

~ 1]. Stable system (all poles inside the unit circle)

<!-- formula-not-decoded -->

outside the unit circle) poles

17.17 (Solution) Systems of parts (a) and (b) are unstable.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.18 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.19 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

z

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

y[n] = So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

S0, H(z)| = 28.6750 z=ej*/4 0.5

The zero state response is %zs[n] = K(0.5)" + 2.7144cos(0.25n7 28.675")

cos(0.257) Note: The tedious way is to find X(z) = 2 and then compute Y(z) and its partial fractions etc. 22 22

## 17.21 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 17.22 (Solution) y[n]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

S0, y[n} = [~0.5(0.5)"

2(0.5)" + 4Ju[n] = [4 \_ 2.5(0.5)"Ju[n]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.23 (Solution)

<!-- formula-not-decoded -->

## 17.24 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.25 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.27 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.28 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

So,

Yzs

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and (z e-jn/2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 2z(z \_ 1) 17.29 (Solution) H(z) = 0.25 + z2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- F =0.25, 2 = j,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) z[n] = {2,4,6,8}  y[n] = z[n] * h[n] = {1,4,8,10,11,4}

<!-- formula-not-decoded -->

- 17.31 (Solution) Refer to the sketches for spectra. At F = 0 At F =0.5,
- 2 - 1 0.25

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) The filter is stable but noncausal.
- (b) H(z) describes an IIR filter.
- H(z) 0.4 0.4 17.33 (Solution) H(z) = = = (z 505)(z +2)' (z = 0.5)(z + 2) 2 = 0.5 2 + 2 ` (a) Causal: ROC is |zl &gt; 2, h[n] = [0.4(0.5)" 0.4(-2)7Ju[n]
- (b) Anti-causal: ROC is |z/ &lt; 0.5,
- (c)

1]. Refer to the sketch for spectra.

<!-- image -->

- (a) H(z) = 0.5+0.52-1 H(F) =0.5(1 + ) =
- H(Fo) = So,
- 1]
- So, y[n] = 1

Refer to the sketch for spectra.

<!-- image -->

- So,
- 1] - 4cos(nr/3) (by linearity and superposition)

17.36 (Solution) h[n] = {0.5, 1, 0.5}. Refer to tbe sketch for spectra.

<!-- image -->

- (a) H(z) = 0.5 + +0.5z-2, H(F) = (0.5 + 4 0.5e-j zF) e-j2F

- = 2. y[n] = 2 = 0.5, H(Fo) = 0. So,
- 2] - 4sin(0.5nr) (by linearity and time invariance)
- (a) H(z) = 1 -2-1, H(F) =1 -e-j2mF = HPF S0,

<!-- image -->

- (c) z[n] = u[n} So,
- y[n] = 26[n] -
- y[n] = 2 So,

17.38 (Solution) y[n] + 0.5y[n ~ 1]. See figure for spectra. 1/6 1/2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

17.39 (Solution) For all parts, ROC is 0 &lt; |zl &lt; œ (excludes z = 0, 2 = 0)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.40 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.41 (Solution)

- (b) If the system is stable; the ROC includes the unit circle
- (c) If the system is stable and h[n] is causal; the ROC is |z/ &gt; 1-

## 17.42 (Solution)

- (a) If the system is stable, the zeros may be anywhere; the poles must lie outside the ROC.
- An FIR filter with real coefficients is stable. All must be at the origin. poles
- (b) circle and their number must equal or exceed the number of zeros.
- must display conjugate reciprocal symmetry.
- (e) For a causal, linear phase FIR filter with real coefficients; all poles must lie at the origin, the zeros must display conjugate reciprocal symmetry and the number of poles (at the origin) must OF exceed the number of zeros. equal

<!-- formula-not-decoded -->

- (a) For 0 &gt; ß, X(z) will not represent a valid transform
- (c) For œ = ß, X(z) represents a valid transform

## 17.44 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This is not a valid transform (ROC is: |zl &gt; 2 and |z/ &lt; 0.5)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- X(z) represents a valid transform

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 8
- 8
- (e)
- Q2
- Ff h[n] = (~1)"c[n], the ROC of H(z) is |z| &lt; œ
- =

<!-- formula-not-decoded -->

This represents a valid transform only if |al &lt; 1.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 17.49 (Solution) z[n} = (2)"u[n] + X(z)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) H(z) = zX'(-z). Now X(-z) = (~2)"u[n]
- 17.50 (Solution) X(z) = Assume a causal z[n]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- with ROC: |z| &gt; 4, the ROC of X(1/2) will be |z| &lt; 0.25 and 0.5[X(z)+X(-z)] 2 = 4 will not represent a valid transform.

However, if X(z) with ROC: |z/ &gt; 0.25 and 4 0.5[X(z) + X(-z)] will represent a valid transform.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 17.52 (Solution) Refer to the sketches.

<!-- image -->

<!-- formula-not-decoded -->

The zeros are at -1.618, +0.618. There is a at 0 There is no symmetry in z[n} pole

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Double zeros at -0.5+j0.866 show conjugate reciprocal symmetry.

<!-- formula-not-decoded -->

- ~ (c) X(z) = 22 are their own

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The 2 zeros at +l are their own

Now, s[n] is odd symmetric. In fact, X(1/z) =2-2

## 17.53 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.54 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.55 (Solution) Refer to the figures

<!-- image -->

- X(z) =1+2-1 + z-2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.56 (Solution) Refer to the figure

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.57 (Solution)

- (a) Ftom h[n] For causality; h[n] = O,n &lt; 0
- (c) 4 is causal if there are no terms of the form z[n + K], K &gt; 0

The difference equation y[n + N] + .4 Avy[n} = Bor[n} is causal if M &lt; N

- (d) From pole-zero plot: For causality; the number of poles must Or exceed the number of zeros. For stability; all must lie inside the unit circle (if causal) . equal poles

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

X1(z) 17.59 (Solution) For all parts, set up in the form X(z) =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- h[n] = {2,3,~2,3,2 32 -1 2z -2
- (c) h[n] describes a linear phase sequence. Yes,

<!-- formula-not-decoded -->

- (b) If causal, h[n] = [0.4(0.5)"
- (a) If stable; h[n] =
- 1]

- 2 H(z) 0.4 0.4 17.62 (Inverse Transforms) Let H(z) = (z = 0.5)(z + 2) (z = 0.5)(z + 2) 2 = 0.5 z + 2

<!-- image -->

<!-- formula-not-decoded -->

- 17.64 (Solution) h[n] = cos(2n"Fo) H(z) = 22

If Fo = 0.25, H(z) See figure for its realizations 22 + 1 '

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 2 =Q 17.65 (Solution) H(z) = A-

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.67 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (a) f1 = 5, f2 = 10 Hz; So, $ &gt; 20 Hz to prevent aliasing.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 17.69 (Solution) See figure for pole-zero plots.

- (a)
- (c) For allpass filter, So,

## 17.70 (Solution) See figure for pole-zero plots.

<!-- image -->

(a)

Im(z}

<!-- image -->

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

- Q &gt; 0 (and Q &lt; 1 for stability) . So,
- (c) An allpass filter is not possible for any nonzero &amp;-
- (b) Q &lt; 0 (and œ &gt; -1 for stability) . So,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) y[n] = From the results of part (a) and (b), z[n] = 0.25

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 17.74 (Solution) Two poles at z = 0, two zeros at z = ~1, dc gain = 8.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) This is an FIR filter
- (c) Tbis is a causal filter
- (d) This is a linear phase filter and h[n] has even symmetry about its midpoint.
- K(z+1)3 (e) With another zero at z = -1, H(z) = = H(z =1) = 8K = 8, 22 Hdc

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

So, this is a noncausal; linear phase; FIR filter and h[n] is even symmetric about its midpoint;

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This is FIR but not linear phase.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This is FIR and linear phase (with h[n] even symmetric about its midpoint) .

- z = 0.5 (c) y[n] = (~0.5)"u[n] Y(z) = H(z) = So, IIR, not linear phase. 2 + 0.5 2 + 0.5

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- z2 + 0.25 17.78 (Solution) H(z)H (z)H2(z) = 22 0.25

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

17.79 (Solution) Refer to the figure

<!-- image -->

<!-- formula-not-decoded -->

- 22 + 0.5z H(z) = 22 + z + 0.5 Its poles are z = 0.54j0.5. So, stable (both unit circle)

<!-- formula-not-decoded -->

- 17.81 (Solution) Filter 1: h[n] = {5,1,1}

<!-- formula-not-decoded -->

- (b) z[n] = cos(nm), F = 0.5, z = -1. both filters give the same output y[n} = r[n] = cos(nn) So, So;
- 1 (c) The two are identical. By division, H2(z) = =1+2-1 1 +2-2 Jong ~2-1

## COMPUTATION AND DESIGN

## 17.82 (Solution) Uses the ADSP routines dtplot\_ sysresp2

```
'PROBLEM 17.82 2=0:30;N=[1,0] ;D=[1,-0.5] ; ystep=sysresp2('2' ,N,D, [1 0] [1 -1]) ,dtplot (,eval (ystep) '0') ,pause ~0.5] ,-4) ,dtplot(,eval(ytl) ,'0') ,pause yt2=sysresp2( '2' ,,D, [1 0] , [1 ~0.5] [-4,3]) ,dtplot (n,eval (yt2) ,'0')
```

## 17.83 (Solution) Uses the ADSP routines dtplot , ssresp

```
'PROBLEM 17.83 [2,0.2*pi, -pi/3] ;n=0:50; N=[1 0] ;D=[1 ) ,pause N=[3,0,0] ;D=[1,1,0.5] ;yss2=-ssresp('2' ,N,D,x) ,dtplot (n,eval (yss2) ,
```

## APPLICATIONS OF THE z ~TRANSFORM

## 18.1 (Solution) Set up the generic 2nd order realization and delete the missing paths

<!-- image -->

<!-- image -->

## 18.2 (Solution)

- (a) Comparing with the generic first order direct form II realization for
- (b) Comparing with the generic second order direct form II realization for

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

## 18.3 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 18.4 (Solution)

<!-- formula-not-decoded -->

- ~ 4 (b) H(z) = Maximum phase (all zeros outside unit circle)  Unstable (poles at z = 4j3) 22+9 22

<!-- formula-not-decoded -->

Minimum (zero inside unit circle) Unstable (two poles at z = 2). phase

- z2 \_ 2z (d) y[n] + y[n ~ 1] + 0.25y[n H(z) = z2 + z + 0.25 Mixed phase (one zero inside unit circle). Stable (Two poles at z = ~0.5).
- 18.5 (Solution) In all parts, we choose the constant K for equal dc gain.

<!-- formula-not-decoded -->

At dc:, JH(1)/2 = 0.25, we

K = ;

get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (a) It is stable for any ß and a) &lt; 1
- (c)
- (b) It is minimum phase

## 18.7 (Solution)

- ={{,-1}

(a) fo = 0.540 = 0,92 S0 locations are = = 4j0.92 Retjno pole

We locate zeros at F = 0 (z = 1) and F = 0.5 (z = -1)

<!-- formula-not-decoded -->

- (b) Notch frequency fo = 1 kHz; Af = 20 Hz, 5 = 8 kHz.

So locations are pole

= 2TFo = R~1 - 0.54n = 0.99 = 0.

Io obtain the notch at Qo = 0.251, we locate zeros at e*jr/4.

<!-- formula-not-decoded -->

- 18.8 (Solution) H(z) = 2 = 2
- (a) H(z) is unstable (the at.z = 2 is outside unit circle) pole
- (b) To make H(z) stable; cascade with allpass flter A1(z) = 150.52 2 = 0.5

<!-- formula-not-decoded -->

- (c) Hs(z) is not minimum phase (the zero at z = -3 is outside unit circle)

2 + To make it minimum phase, cascade with allpass filter Az(z) = +

0.5(z + 3)(z + ! 1.5(2+') (z = 0.5)(1 + 0.52) 2

- (d) At dc (F = 0 or z = 1); we fnd |H(z) = |Hs(z) = |HM(z)l = 4
- H(z) =

<!-- image -->

- (Filter 1) Compare with a generic 3rd order direct form II realization to get A1 = 0, Az = -4, A3 = 4 and Bo = B1 = B3 = 0, B2 = 2

<!-- formula-not-decoded -->

- (Filter 2) Compare with a generic 2nd order transposed realization to A1 = Az = 4 and Bo = B2 = 0, B1 = 3. get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (a) For poles

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

So, overall impulse response is t[n] = 55[n] + 40(0.6) "un] 45(0.4)"u[n]

- at z 6z S0, ß +1.2 =1.2, poles

<!-- formula-not-decoded -->

## 18.11 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 18.12 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

18.13 (Solution) Refer to the figure.

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This is an FR system and represents an identity system.

## 18.14 (Solution)

- (a) All the finite poles of an FIR flter must lie at z = 0. TRUE.
- (c) An FIR filter is always stable. TRUE,
- (b) An FIR filter is always linear phase. FALSE.
- (d) A causal IIR filter can never display linear phase. TRUE
- (f) A minimum phase filter (poles, zeros inside unit circle) is not linear phase. TRUE
- (e) A linear sequence is always symmetric about is midpoint. TRUE phase
- (g) An allpass Gilter can never display linear phase. TRUE
- (i) Tbe inverse of a minimum phase filter is also minimum phase. TRUE.
- (h) An allpass filter can never be minimum phase. TRUE
- (j) The inverse of a causal filter (e.g. H(z) is also causal.  FALSE 0.25
- (k) poles as finite zeros. TRUE.

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) H4(z) =1 \_ Hs(z) = H(z) + H(-z) will be a BSF with band edges at 0.15 and 0.35.
- (a) Refer to the fgure. H(z) is an LPF .

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) H2(F) and H1(F) are not related (H2 is IIR and H1 is FIR)

## 18.17 (Solution)

- symmetric)
- (c) If there are no zeros at z = 1 and z[n] is linear phase, it is also even symmetric. TRUE (only an odd number of zeros at z = 1 can yield odd symmetry)
- (b) If z[n] is linear phase its zeros must always lie on the unit circle. FALSE (zeros can be conjugate reciprocals e.g. 2, 0.5).
- number of zeroS at z =1 produces odd symmetry)
- = 1. FALSE (there can be an even number of zeros at z = 1)

## 18.18 (Solution)

- 0.4096 (a) H(z) = Its zeros areat z = 40.8, z =.+j0.8. Its are at 2 = 40.9, z = 410.9. 24 0.6561 This is a peaking filter. poles
- 24 \_ 1 (b) H(z) = Its zeros are at 2 = 2 = are at 2 = 40.9, 2 = 24 0.6561 This is a notch filter. poles

## 18.19 (Solution)

- (a) The cascade connection of two linear phase filters is also a linear phase filter. TRUE (because the impulse response is tbe convolution of symmetriç sequences, which is also symmetric)
- (b) The parallel connection of two linear phase filters is also a linëar phase filter. FALSE (because the impulse response is the sum of symmetric sequences, wbich may ot be symmetric (sum an odd and even symmetric sequence, for example)
- TRUE

## 18.20 (Solution)

- (a) The cascade connection of two minimum phase filters is also a minimum phase filter. TRUE (because tbe and zero locations correspond to the two filters) pole
- The parallel connection of two minimum phase filters is also a minimum phase filter. FALSE N(z) N2(z) Write HP = 4 D1(z) D2(z) Di(z)D2(z)

zeros) may not lie inside the unit circle.

## 18.21 (Solution)

- (a) Ihe cascade connection of two allpass filters is also an allpass filter. TRUE (because the magnitude |H (F)H2(F)| will be constant)
- (b) The parallel connection of two allpass filters is also an allpass filter, FALSE (For unit filters, the parallel combination is (F) + = constant) gain ejø2(F)

<!-- formula-not-decoded -->

- (a) H(z) is minimum pbase (all poles and zeros inside unit circle)
- (b) To find a flter witb the same denominator as H(z), we pick A(z) with denominator H(z) and numerator with coefcients in reversed order. So, A(z) = 0.652-1+012 2 + 2-2

<!-- formula-not-decoded -->

This is not minimum phase but is stable (with poles inside unit circle)

## 18.23 (Solution) We use C for causal, S for stable; M for minimun phase.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (a) H(z) an allpass filter. Its dc (at z = 1) is |H(z = 1)l = 2 gain

<!-- formula-not-decoded -->

- (d) If Fo = 0.5, tp =

<!-- formula-not-decoded -->

We use C for causal, $ for stable; U for unstable, A for allpass.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 1.5z (d) N(z) = F(z) + G(z) = 22 0.25

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (a)   Verify that the delay of the linear sequence z[n] = {4,3,2, 1,8,1,2,3,4} is zero. phase
- (b) Compute the delay of the signals g[n] = r[n ~ 1] and h[n] = z[n
- (c) What is the delay of tbe signal y[n] = 1.5(0.5)"u[n} ~ 28[n]
- (d) Consider the first-order alpass filter H(z) = (1 +az) /(z +a) Compute the signal delay for its impulse response h[n}.
- =0 and D = 0 k=-4

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 18.27 (Solution) Refer to the figure for pole-zero plots.

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

we find

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

we find

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

I ~ I; we find tan =1

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) of the allpass filter must be G = 0.8944 1.118 gain

<!-- formula-not-decoded -->

- (a) To stabilize H(z), cascade with an allpass filter wbose zeros cancel the offending poles.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) Hs(z) is causal and minimum-phase; but not allpass.

## COMPUTATION AND DESIGN

## 18.30 (Solution) Uses the ADSP routine dtplot

'PROBLEM 18.30

'PARI (a)

FO-22.5/180;F1-60/180; 'Filter should be Zero at F1 gain

'Place zeros and conjugate at FO \_ gain

b=/G 'Divide h by G uit at FO gain

'PART (b)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

subplot (2,2,1) ,dtplot (n,x) ,subplot (2,2,2) ,dtplot (n,g)

<!-- formula-not-decoded -->

## 18.31 (Solution)

```
'PROBLEM 18.31 F=-0.5:0.001:0.5;w-2#pi#F; h=[1 N=[1
```

```
0 0 0 0.5] ;H=freqz(h,1 ,#) ;subplot(2,2,1)= plot (F,abs (H)) b=[1 0 0 0 0.5 0 0 0 0 0 0.5 0 0 0 0.25 0 0 0 0.125] 0 0 0 0] ;D=[1 0 0 0 ~0.5]
```

## 18.32 (Solution) Uses the ADSP routine ecgsin

```
'PROBLEM 18.32 (a) 'Filter sbould be Zero at Fl 'Place zeros at and conjugate_ 'Find dc gain G and divide h by G for uit dc 'IPART (b) 'Pick bandwidth =10 Hz 'Zeros at 'Poles at radius R 'ormalize dc gain to unity 300 ,10,60) 'Can also use this (see 19) 'PART (c) yl=filter(b,1,yn) ; 'Zero phase filtering y2-filter(N,D,yn) subplot (2,2,1) ,plot (n,yecg) ,subplot (2,2,2) ,plot (n,yn) subplot (2,2,4) ,plot (n,yecg,n,y2,' --') ,pause 'Nov compare filter frequency response F=0:0.001:0.5; H2=freqz (N,D,w) ;subplot (1,2,2) ,plot (F abs (H2) ) gain gain Chap
```

## 18.33 (Solution) Uses the ADSP routine plotpz

```
'PROBLEM 18 33 'IPARI (a) h='0.8 1' 'PART (b) F=0:0.005:0.5;H=freqz( [1 0] n=0:2;ht=0.8 '3 term truncation subplot (2,2,1) ,plot (F ,abs ( [H;HT] ) )
```

```
subplot (2,2,2) ,plot (F N=[1 0] ;D=[1 subplot (2,2,4) ,plotpz(ht,1,'2' ) ;pause (c) n-0:9;bt-0.8 '10 term truncation subplot (2,2,1) ,plot (F ,2bs ( [H;HT] ) ) subplot (2,2,2) ,Plot (F ,angle( [H;HT] ) ) subplot (2,2,3) ,plotpz(N ,D,'2') ; subplot (2,2,4) ,plotpz(ht,1,'2' ) ;pause n;subplot(2,2,1) ,plotpz(ht ,1,'2') ; n;subplot(2,2,2) ,plotpz(ht,1,'2'); => infty, the zeros will collapse to the origin 18.34 (Solution) 'PROBLEM 18.34 'Design peaking filter vitb a half-power bandvidth of 1000 Hz 0 subplot = plot (F*S ,abs (H) ) 18.35 (Solution) Uses the ADSP routine bltZord and data file nysteryl mat 'PROBLEM 18.35 load ysteryl; clf , Lslengtb(mysteryl) (nysteryl) ,pause F=(O:L-1)/L;H=fft(mysteryl) ;plot (F,abs(H)) ,pause FO=0.1;B=0.05;S=1; 'Pick B=0.05 (you can try otbers) 'Design peaking filter vith a half-pover bandvidth of 1000 Hz [S ,20] ,B,FO) ; N=[1 0 OJ/A;D=[1 F1=0:0.005:0.5;HF=freqz (N,D,2*pi*F1) (F1,abs (HF)) pause sig-filter(),D,mysteryl); (sig) ,pause out Lov freq signal much too strong %So _ first renove lov frequency component brute force subplot (2,1,1) ,Plot (F ,abs (H) ) pause 'Mystery signal cinus lov freq signal sig2-filter(N,D,mys) ; subplot ,plot (sig2) 'Can make cut Message says HI angle( 'grid ;plot ;plot plot
```

## 18.36 (Solution) Refer to tbe figure. GLP(z) = 0.5(1+2-1)

<!-- image -->

- (a) The transfer functions of the three circuits are

<!-- formula-not-decoded -->

- Refer to the following MATLAB code.
- (c) Tbe frequency response is similar for all tbree circuits. All three have the same locations. pole

```
'PROBLEM 18.36 clf ,subplot D=12;4=0.9;n1=[1 zeros (1,D)J;d=[1 zeros (1,D-1) f=(0:400)/800; 'subplot (3,1,2) plot(f_ abs (h2) ) h3=freqz(1,d,2tpi*f); 'subplot(3,1,3) ,Plot(f,abs(h3)) subplot,plot(f,abs(hl) ,f,abs(h2) ,f ,abs (h3)_
```

## 18.37 (Solution)

```
'PROBLEM 18.37 5-10000;f0=880,F=880/10000;f=(0:400)/800; a= (1-tp)/(1+tp);A=0.9; l=[0.5 0.5] ;d1=[1 zeros(1,D-1) ~0,5*4 subplot (3,1,1) ,plot(f,abs(hl)) set (gca, 'manual' xtick FO* [0:5]) ,grid 'without allpass filter [0.5 0.5*(a+1) 0 . 5*a] d=[1 (1,D-2) f=(0:400)/800; hl-freqz(n,d,2*pi*f); subplot(3,1,2) ,plot (f ,abs (hl) ) set (gca= xtickmode' 'manual xtick 'With allpass filter a-sin((1-tp)*pitF)/sin((1+tp)#pi*F) 1= [0.5 0.5*(a+1) ,grid
```

```
d=[1 zeros(1,D-2) -0.5*A*a ~0.5+A*(a+1) ~0.5*4] ; hl-freqz(n,d,2*pitf) ; subplot (3,1,3) ,plot (f ,abs(hl)) set (gca, xtickuode' manual xtick' ,F* [0:5]) 'Using exact values of does not make difference_ grid
```

To find the exact relation for Q in terms of tp  rewrite Eq 18.45:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Using tan(z) = sin(z)/ cos(z) and simplifying; we obtain

<!-- formula-not-decoded -->

## 18.38 (Solution) Uses the data file tonebank

```
10 12] the nunbers 'nake colunn 'IChange 0 to 11 M-fix(0.1*S) % M samples for 0.1 2 3;4 5 6;7 8 9;10 11 12] ; ('load tonebank' ) ; nl=[1 ~clov(il) 0] ;dl-[1 -2*clow(il) 1] ;sl-filter(2l ,d1, [1 zeros(1,M-1)]); [1 zeros (1,M-1)J) ; tone-sltsh;tonefft-abs(fft(tone)); dig-tonemat(il,ih) ;sound(tonebank(:,dig)); plot(f ,tonefft) axis( [0 2000 0 500}) set (gca, 'xtickode' 'manual xtick [0 low(il) hi(ib) 2000]) ,pause end eval dh ,
```

## 18.39 (Solution)

- (a) Iry the routines dialttl and dialtt2 to generate DIMF tones. The second routine uses a digital oscillator to generate the signals.

```
function [sigtt,snd]=dialttl(n,S) '[sigtt,snd]-dialttl(n,S) generates tones for a phone nunber 'S-sampling freq (Defaults to 8192 Hz) 'n=vector or array of digits in the pbone nunber 'speak is spoken rendition of number Uncomnent to use 'NOTE: Use 10 for 12 fOr # on the dial 'See getnuml.n and getnum2.n to decode if nargin<2,S-8192;end low= [697 770 852 941] ; hi-[1209 1336 1477] ; 'make column i-find(n==0);n(i)=ll+O*i; 'Change 0 to 11 M=10oo 'silent passage 1-lengtb(n) ; sigtt=[] n(k) ib-ren(n(k)-1,3)+1;il-fix( (n(k)-1)/3)+1; tone=[lov(il) hi (ib)]; snd=[snd;tone] ; sigtt=[sigtt, Cos if k<l,sigtt-[sigtt, 2] ;end 'add zeros to all except end 'speak (snd) function [sigtt,snd]=dialtt2(n,S) '[sigtt,snd]=dialtt2(,S) Sound of tones in a at 'S=sampling freq (Defaults to 8192 Hz) 'Uses digital oscillator to generate signals %n=vector or array of digits in the phone pumber 'Speak is spoken redition of nunber Uncomment to use 'NOTE: Use 10 for and 12 for # on the dial 'ISee getnunt OI getnun2.m to decode if nargin<2,S-8192;end hi=[1209 1336 1477] ;whi-2*pithi/S;chi-cos(vhi) ; n=n(:); colun isfind(n--0);n(i)-ll+O*i; 'IChange 0 to 11 %silent passage N=0:M-1; 2(k) ib=rem((k)-1,3)+1;il-fix( (n(k)-1)/3)+1; [snd;tone] 1] ;sl-filter(nl,dl , [1 zeros (1,M-1)J); [1 ~chi(ib) O];dh=[1 -2*chi(ib) 1] ;sh=filter(nh,dh, [1 zeros(1,M-1)J); and snd= nb=
```

```
sigtt-[sigtt, sl+sh] ; if k<l,sigtt-[sigtt, 2] ;end 'add zeros to all except last digit end 'speak (snd) (b) To decode using the FFT; try the following routine function n=getnunl(sigtt,th,S) 'getnun(sigtt) decodes tones in phone number fron freq info 'sistt is output generated by dialtt (defaults to 8192) 'th-detection threshold (defaults to 0.7) 'NOTE: Use 10 for and 12 for # on the dial 'm=vector of digits found by decoding fft of tone signal 'speak is the spoken rendition of the phone number _ Uncomment to use it 'see dialttl.m code if nargin<2,th=0.7;end if th>l,error('threshold cannot exceed 1') ,return,end low=[697 770 852 941] ;hi-[1209 1336 1477] ; tonemat=[1 2 3;4 5.6;7 8 9;10 11 12] [] ;while ~isempty(sigtt) tone-sigtt(1:1000); 'Each tone assumed 1000 samples+1ooo zeros if length(sigtt)>2000,sigtt(1:2000)=[J;else,sigtt(1:1000)=[] tonefft=abs(fft(tone)) tonefft-tonefft(1 500) notefreq-[i(1)-1 i (L)-1]+S/1000; x=abs(lov-notefreq(1)) il=find(x=-min(x)); [m;digtt]; end 'speak (n) (c) To decode using bandpass (peaking) filters; the following routine 'S-sampling freq (defaults to 8192) 'sigtt is output generated by dialtt 'Uses peaking filters for detection Use 10 for and 12 for # on the dial 'm=vector of digits found by decoding tone signal 'speak is the spoken rendition of the Uncomnent to use it 'see dialtt.@ to code if nargin<2,8-8192;end ;end try
```

## 18.40 (Solution)

```
low-[697 770 852 941] ;hi-[1209 1336 1477] ; chi=cos(whi); R=0.99;4lo=1/ (1-R*R)./sin(ulo);Ahi-1/(1-R#R)./sin(whi); N=[1 0 0] ; end for k=1:3;DH(k,:)=[1 -2*R*chi(k) R#R]#Ahi (k) end tonenat=[1 2 3;4 5 6;7 8 9;10 11 12] ; [] ;wbile ~isempty(sigtt) tone=sigtt(1:1000); 'Each tone assuned 1000 sanples+10oo zeros if length(sigtt)>2000,sigtt(1:2000)=[];else,sigtt(1:1000)=[] ;end for k=1:4,lf=filter(N,DL(k,:) tone) ;El (k)=su(lf.*lf) ;end 'Output energy il=find(El=-nax(El)); 'Find vhich filter has naximum output energy Eh(k)=sum(lh.*lb) end digttztonemat(il,i2); if digtt==ll,digtt-O;end [n;digtt]; end 'speak (n) 'PROBLEM 18.40 F=0:0.005:0.5;"=2*pi*F; 'Repeat for tp-0.5 M2=abs(H) P2=angle(H) ;U2-unwrap(P2) ; 'Repeat for tp=0.9 tp=0.9;a=(1-tp)/(lttp);N-[a 1] ;D=a* [1 a] ; M3=abs (H) ; P3-angle(H) ;U3=unwrap (P3) ; subplot [M1;M2;M3]) ,pause 'PART (b) (F [P1 P2;P3] ) , Pause plot (F , [U1 U2;U3] ) pause subplot (2,1,1) 0 1.2]) subplot (2,1,2) ,plot (F , [G1;G2;63] ) axis( [0 0.5 0 1.2]) ,grid 'PART (c) The higher tbe phase delay , the more constant the group delay. 'PARI (d) Smaller alpha gives constant the group 'PART (e) plot delay .
```

```
F=0.5 at F=0 Dmin-nin( [G1(:) G2(:) G3(:)J) 'Max delay at F=0.5
```

## IIR DIGITAL FILTERS

<!-- formula-not-decoded -->

- 1 (a) For impulse invariance; H(s) = 4 H(z) = = 5 + Q 2 2 e-1 0.3679 =e-at,
- (c) The response of H(s) and H(z) will NOT match at the sampling instants. step
- (b) The impulse response of H(s) and H(z) will match at the sampling instants.
- 1 19.2 (Solution) H(s) = 5 + 2'

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) The impulse response of H(s) and H(z) will NOT match at the sampling instants.

<!-- formula-not-decoded -->

- (c) The step response of H(s) and H(z) will match at the sampling instants.
- 1 19.3 (Solution) H(s) = 0.5 s.

<!-- formula-not-decoded -->

- (b) Tbe impulse response h[n] will not match h(t) of tbe analog filter at the sampling instants.

<!-- formula-not-decoded -->

- (c) Tbe response s[n] will not match tbe response s(t) at the sampling instants. analog step step
- (d) The ramp response vn] will match the analog ramp response v(t) at the sampling instants

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 1 19.5 (Solution) For impulse invariance, H(s) = H(z) = 2 = e-œt,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 1 19.6 (Solution) H(s) = with cutof frequency = 1 rad/s.
- So, the analog filter with frequency 1.5708z So, by impulse Invariance (with ts = 1), H(z) = z z = 0.2079 cutoff Sc

gain.

- (b) Tbe dc gains are H(s)| =1, H(z) z = 1 =1.983 s=0 multiply H(z) by G = 1885 = 0.5043 to obtain unit dc So,
- (c) The of H(s) at 1 rad/s is |H(s j)| = 0.7071. Tbe of H(z) at 9 = 2 = j1.5708 = 1.5379. multiply H(z) by G1 0.7071 0.4598 0.2079 18379 to match its to H(s) With tbis change, the dc gains will no longer match. gain gain So, gain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 19.8 (Solution)

<!-- formula-not-decoded -->

- 19.9 (Solution) H(s) = s + Q
- (a) H(s) is stable for œ &gt; 0?
- (b) The forward difference mapping is is s = 2=1 ts

<!-- formula-not-decoded -->

This is stable if |1 ats| &lt; 1. For a &gt; 0, we require 0 &lt; ts &lt; 2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 2 = 1 (c) The backward difference is s = zts

<!-- formula-not-decoded -->

For stability; |1 + ats| &gt; 1. This is always satisfied (for ts &gt; 0 and a &gt; 0)

- 3 19.10 (Solution) H(s) =
- (a)

<!-- formula-not-decoded -->

- (b) If S = 80 kHz, and the of H(z) at fm = 20 kHz matches the of H(s) at w = 3 rad/s. = WA = (z +1)2 7z2 \_ 4z + 1 gain gain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (a) H(s) is a bandpass filter.
- (b) S = 1 kHz, fm = = =

We require wA =1=

<!-- formula-not-decoded -->

H(z) is also a bandpass filter .

<!-- formula-not-decoded -->

We require WA =21 =C = So,

<!-- formula-not-decoded -->

Tbis filter is also a bandpass filter.

2 + 1 19.12 (Solution) H(z) = S = 10 kHz, =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- = 0.902 27 ,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 2 19.13 (Solution) H(s) = with a cutoff frequency of 1 rad/s. s2 + 2s + 2
- (a) LPF C(z = 1) 0.1135(2+ 1)2 s = HLP(z) = fc = 22

<!-- formula-not-decoded -->

- (b) HPF: fc = 500 1 =C S0, C = 1 C(z + 1) ~ 1)2 s = HuP(z) 2 = 1 Hz,

<!-- formula-not-decoded -->

- (d)

<!-- formula-not-decoded -->

## 19.14 (Solution)

- Following Chapter 13, we find n = 4. The LPP with unit cutoff frequency is kHz,

<!-- formula-not-decoded -->

The backward Euler transformation $ = (z I)/zts with ts = 1 gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- Following Chapter 13, we find n = 3. Tbe LPP with unit cutoff frequency is

<!-- formula-not-decoded -->

After partial fraction expansion of HLP(s) the impulse invariant transformation (with ts = 1) gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) Chebyshev BPF: Ap = 2dB; 'As = 3OdB, fp [800,1600] Hz, fs = [400,2000] First, prewarp frequencies = = [1.0995,3.1515], Ws [0.5135,6.1554} Hz, using Wpre
- S = 5 kHz

Following Chapter 13, we find n = 3. The Chebyshev LPP with unit cutof frequency is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

C(z? ~ 2œz + 1) We use tbe A2D transformation: s = to give z2 \_ 1

<!-- formula-not-decoded -->

- (d) Inverse Chebyshev BSF: Ap = 2dB , As = 3OdB, fp = [200, 1200] Hz, fs = [500, 700] Hz, 4 kHz

Prewarp frequencies using Wpre = 2tan(0.50) where $ = 2rf/S

<!-- formula-not-decoded -->

Following Chapter 13, we find n = 2 The Chebyshev II LPP with unit cutoff frequency is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 19.15 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 19.16 (Solution)

<!-- formula-not-decoded -->

## 19.17 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- K(z + I)(z = e-1/4) (b) (b) Replace only one occurrence of z by (z + 1) H1(z) =
- (c) Replace all but one occurrences of z by (z + 1) (none; in our case)

<!-- formula-not-decoded -->

## 19.19 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Compare with the ideal integrator, H(s) = 1 to give

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) Tbe poles of H(z) are at z = -2ts + (3t2 + Clearly; (3t? + 9)1/2 &gt; 1 for any ts &gt; 0. S0 magnitude of one 9)1/2. pole

## 19.20 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) dcH(s = 0) = 1 and dcH(z = 1) = 1. So, the dc are identical. gains
- Gain of H(s) at W rad /s (or s = j) is 0.707. The 0.6421. Ibey do not match. (d) gain

## 19.21 (Solution)

<!-- formula-not-decoded -->

## 19.22 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 19.24 (Solution) Refer to the sketch.

<!-- image -->

Even though any sampling rate above 220 kHz will avoid aliasing; we can use a lower sampling rate as a5 the aliased noise spectrum does not overlap the signal spectrum. example, sampling rate of between 130 kHz and 140 kHz can avoid signal contamination by the alíased spectrumn (see = 140 kHz, say; a typical set of filter specifications might be: long For

Passband edge = 20 passband attenuation; say 0.1 dB (minimum loss) Stopband edge = 30 kHz; minimum stopband attenuation of 40 dB (100-fold reduction). kHz,

## 19.25 (Solution) A monotonic response in the passband and stopband requires a Butterworth filter.

<!-- formula-not-decoded -->

Following chapter 13, we find the Butterworth filter order n = 1l. This problem is best  solved pumerically  For example; use the ADSP routine dfdiir as follows.

<!-- formula-not-decoded -->

This gives the analog lowpass prototype as

<!-- formula-not-decoded -->

The routine performs partial fraction expansion; impulse invariant transformation (with ts = 1) and subsequent re-assembly   We find the numerator and denominator coefficients of the digital flter H(z) (in descending powers of z as

| 0.0011         | 0.0150   | 0 .0897   |   0.2990 | 0.6149     | 0.8174   | 0.7180   |
|----------------|----------|-----------|----------|------------|----------|----------|
| 0.4186         | 0.1597   | 0.0383    |  0.0052  | 0.0003     |          |          |
| Denoninator: 1 | 0 .1888  | 1.3117    |  0.0885  | 0.5212     | ~0.0084  | 0.0761   |
| ~0.0046        | 0.0039   | ~0.0002   |  4.7e-05 | ~0.0000013 |          |          |

## 19.26 (Solution) Notch frequency = 50 Hz. Notch bandwidth =4 Hz. S = 300 Hz.

C = tan(0.540) = 0.0419

<!-- formula-not-decoded -->

To compute the of tbis filter at 40 at 50 Hz and at 60 evaluate H(z) at z = where 3 8 The results are 0.9835, 0, 0.9789 . gain Hz, Hz;

- 19.27 (Peaking Filters) A peaking flter is required to isolate a 100 Hz signal with unit Design such a filter the bilinear transformation assuming a bandwidth of 5 Hz and a sampling rate of 500 Hz. Compute the of this filter at 90 Hz, at 100 Hz and at 110 Hz. gain. using gain

Peaking frequency 100 Hz. Bandwidth =5 Hz. S = 500 Hz.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

To compute the of this filter at 90 where F = 38, 38 Tbe results are 0.2366, 1, 0.2460. Hz, gain

- 19.28 (Solution) Order = 4, passband =[8, 12] kHz. Maximum passband ripple = 59. S = 40 kHz.

The design calls for a Chebyshev filter. A 5% ripple means a passband attenuation of 0.4455 dB. The lowpass prototype corresponding to a 4th order Chebyshev filter is of order 2

<!-- formula-not-decoded -->

The (unwarped) digital band edges are [021, ß2] = 4

C(z2 \_ 2az + 1) 0.0973(z4 2z2 + 1) We use the A2D transformation: s = to give HBP(z) = 22 \_ 1 24 + 1.006422 + 0.4159

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 19.30 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

2 + sts 2 + 0.5s 5 + 4 First order Pade approximation z = H(s) = 2 sts 2 = 0.5s 3s + 4 So,

With get

<!-- formula-not-decoded -->

- (c) The first order mapping is identical to the bilinear transformation.

## COMPUTATION AND DESIGN

- 19.31 (Solution) Uses the ADSP routines s2zinvar s2zni\_ tfplot

```
'PRDBLEM 19.31 [nz,dz, G]=s2zinvar(na,da,S,'i' [ha,Pa,fa]=tfplot('s' ,na,da, [0,0.5]) ; {hd ,Pd,fd]=tfplot('z' ,nz,dz , [0 0.5]) ; plot (fa,ha,fd,hd) set (gca, xticknode' manual' 'xtick' [0 1/8 1/2/pi 0.5]) ytickode' manual 'ytick' [0 1/sqrt(2) 1]) ,grid,Pause 'After natching (fa,ha,fd,hd) set (eca, xtickmode manual 'xtick' [0 1/8 1/2/pi 0.5]) set (gca,'yticxmode manual 'ytick [0 1/sqrt(2) 1]) ,grid,pause 'PART (b) 'PART (c) snra-20+l0g10 (H(1) /H(2)) HD=abs (polyval (nz,2) ./polyval (dz,2)) ; snrd=20*10g10 (HD(1) /HD(2) ) 'PART(d) [fO FO]) [hd ,Pd,fd]=tfplot('2' ,nz,dz, [0 0.5]); plot(fa,ba,fd,bd) set (gca, 'xtickmode manual' xtick' [0 1/8 1/2/pi 0 .5]) set(gca, 'yticknode= manual' 'ytick' [0 1/sqrt(2) 1]) ,grid HD=abs (polyval (nz,2) . /polyval(dz,2) ) ; 'Tbe bilinear design provides better SNR especially at higher frequencies set(gca, gain plot
```

```
19.32 (Solution) Uses the ADSP routine dfdiir 'PROBLEM 19.32 'bili [ne _ de]-dfdiir( 'el 'lp' bili' ,A,S,fp,fs) ; ordbut-lengtb(db)-1,ordellip-length(de)-1 W) ; plot (F ,DB,F ,DE, ' --') ,pause 'PARI (b) NE-DE(1) grid,pause plot (n,X,n-MB ,yb ,n-NE ,ye) 'PART (c) Assune filter with zero-phase and use the sane gain 'as the passband to find output _ Compare with the real output the two line uP , the distortion is due to attenuation. WP=pi* [0.03,0.09 ,0.15] H=abs(freqz(nb,db,WP)) ; 'For Butterworth plot (n-NB,yb,n,ybl) ,grid,pause 'No match, phase distortion present H=abs (freqz(ne,de,WP) ) ; 'For elliptic even more phase distortion 19.33 (Solution) Uses the ADSP routine blt2ord 'PROBLEM 19.33 half-pover bandvidth of 100o Hz subplot plot (F*S,abs (H) ) ,grid,pause 'Compare vith filter designed in Prob 18.34 'From Prob 18.34 ~2+R#C R*R] 19.34 (Solution) Uses the ADSP routines lpP, lp2iir, 'PROBLEM 19.34 clf ,L=length(nysteryl) (uysteryl) pause 'PART (b) de , delay 'grid gain 'grid ;plot 'grid ;plot
```

```
'Pick band edges of [0.08 0.12] and LPP =1/(s+1) [N ,D]=lp2iir('bp' 'a',1, [1 1] ,1 , [0.08 0.12]) ; sigl-filter(N ,D,nysteryl);sig2-filtfilt (N_ D,mysteryl); subplot(2,1,1) ,plot(sigl) 'Cannot make out subplot(2,1,2) ,plot (sig2) ,pause 'Can make out but still not clear 'PART (c) i=find(abs (HM) >3000) ;H2-HM;H2(i)-O*i; subplot (2,1,1) ,plot (F , abs (HM) ) subplot (2,1,2) ,plot (F ,abs (H2) ) pause uys-real(ifft (H2)); 'Mystery signal minus low freq signal 'Pick [Ap As]=[1 40] dB , FP=0.12, Fs=0.3 to design filter D2]=dfdiir('bw 'lp impu [1 40],1,0.12,0.3) ; subplot (2,1,1) ,plot (sig3) subplot(2,1,2) (sig4) Much better. Can make out message as HI 'PART (d) Better detection vith part (c) and using filtfilt 19.35 (Solution) Uses the ADSP routines interpol, dtplot, lp2iir 'KPROBLEM 19.35 M=20;n=0:M-1;F0=0.4;x=Cos (2*pi*FO*n) ;subplot(2,1,1) ,dtplot (n,%,= ) N=5; nl=O:M#N-1 ;xu=interpol subplot(2,1,2) ,dtplot (2l ,xu_ ) ,Pause 'PARI (6) Fc=Fo/N 'PART (c) filter from Sth order analog LPP vitb unit half-pover Fc-FO/N;A=N; [na da]-lpp('bw' ,5,3) ; [nz,dz]=lp2iir( 'lp' ,'a' ,na,da,1 ,Fc) ;nz-nz*A; 'PART (d) y=filter(z,dz,xu) ; xi=cos 'Interpolated signal suffers delay of about 5 samples and its 'gain sbould be 0.707 times the required gain because we chose 'sthe 3-dB frequency as Fc_ second plot confirns tbis_ 'NOTE: better result is by FFT (bandlimited) interpolation X=fft(x);Y-[X(1:10) zeros (1,80) X(11:20)]; 19.36 (Solution) Uses the ADSP routines s2zni nundig 'PROBLEM 19.36 n=poly( [-0.5;-1.5]) ;d-poly( [-1;-2;-4.5;-8;-12]) ; analog lpP (x, Design freq
```

```
%2=[1 2 0 . 75] [1 27.5 261.5 1039 1668 864] ; [nz dz] =s2zni (n,d,100,'trap' ) ;dz7-numdig(dz,7) ; ;d=
```

```
plot (F ,abs( [Hl;H2] )) ,grid,pause abs ( [roots(dz) roots(dz7)J) 'Display [true_ "truncated"] filter roots B=O;dr-2*ones (size(dz)) ; 'Pick roots 1 Assune dynanic range is 1 format B , Coeffs=[dz(:) dzr(:)] format long,
```

## 19.37 (Solution) The mapping rules for the three algorithms are

<!-- formula-not-decoded -->

Refer to the following MATLAB code for plotting the frequency response.

<!-- formula-not-decoded -->

```
'PROBLEM 19.37 Uses the ADSP routine polymap nl=[1 n2= [1 0 -1] ;d2-[1 4 1]+ts/3; 23= [1 0 0 ~1];d3=[1 3 3 1]*3+ts/8; Hl=freqz(nz1 plot (F abs ( [Hl;H2;H3])) ,grid,'pause abs (roots(dzl)) ,abs(roots(d22)) ,abs(roots(dz3))
```

'Frequency response looks similar up to about F=0.25 . Adans-Moulton 'response resemnbles a lovpass filter and leads to Only

<!-- formula-not-decoded -->

<!-- image -->

```
19.39 (Solution)
```

```
'PROBLEM 19.38 Uses the ADSP routines bodelin, s2zni _ s2zinvar 'From Prob 12.17, H(s)=10(1+s/v1)/[(1+s/w2) (1+s/u3)] semilogx(Ha(:,1)/2/pi,Ha(;,2)) set (gca, 'xtickmode manual xtick' [50 500 2122]) grid,pause 'PART (b) S-30000; [Nz1 Dz1]-s2zinvar (N ,D,8,'i' ,1000) ; 'PART (c) [Nz2,Dz2] =s2zni (N,D,S,'bili' ,1000) ; 'PARI (d) subplot(2,1,2) ,Plot (f ,angle (HA) ,F*S ,angle(HDI) F#S,angle (HD2) ) 'Magnitude response for both is close Only bilinear phase is close Uses the ADSP routines lPP, lpZiir, blt2ord 'PRDBLEM 19.39 a n2,d2,5,300) 'a' ,22,d2,5,3000) ; 'Passband edge is 3000 Hz Hl=freqz(nzl_ plot (S*F abs ( [HI;H2;H3;H4])) ,grid 'To adjust the gain over +12 dB to ~12dB , the linear gain of each 'transfer function needs be changed from 4 to 0.25 ,grid
```

## FIR DIGITAL FILTERS

## 20.1 (Solution) Refer to the sketches.

<!-- image -->

- (a) Type 1: h[n] ={{,o,1} H(z) = 1+z-2 [H(o)| = 2, = 0,
- (b) H(F) =1 + = Now, |H(O)| = 6, JH (0.5)| =0 LPF Type 4 2-3 e-j3 F So,
- (c) Type 3: h[n] = H(z) = 1 \_ 2-2 H(F) =1 [H (0.25)| = 2, |H(0.5)| = 0. BPF =e-j4tF So,
- (d) Type 4: h[n] = {~1,2,-2,1} H(z) = -1 +22-1 2z -2 H(F) =-1+ = Now, |H(o)| = 0, =6 HPF +2-3 je-j3TF So,

## 20.2 (Solution)

- (a) A lowpass filter can be designed with types 1,2 and 4 sequences
- (b) A highpass filter can be designed with types 1 and 4 sequences
- (c) A bandpass flter can be designed with types 1,2 and 4 sequences
- (d) A bandstop filter can be designed with only a type 1 sequence

- Fc = 0.25, h[n] = 2Fcsinc(2nFc) = 0.5sinc(0.5n) (a) Bartlett window: N = 7, ~3 &lt;n &lt; 3.

We tabulate the impulse response, window and windowed impulse response:

Index

n

Impulse response

Windov

Windowed response

- 1 0.318 2/3 0.212
- 0.318 2/3 0.212
- 1/3 0

0.5

1

0.5

S0, hw [n] = {0.212, 0.5, 0.212} For &amp; causal sequence; delay by 1 sample (or 0.05 ms)

<!-- formula-not-decoded -->

- (b) vonHann window N = 8, n =-3.5,~2.5, 2.5,3.5 We tabulate the impulse response, window and windowed impulse response.

<!-- formula-not-decoded -->

S0, hw[n] = {~0.017, 0.092, 0.428, 0.428, 0.092, -0.017}. For a causal sequence; delay by 2.5 samples (or 2.5ts =

<!-- formula-not-decoded -->

- (c) Hamming window N = 9, w[n] = 0.54 + 0.46 cos( We tabulate the impulse response; window and windowed impulse response:.

<!-- formula-not-decoded -->

hw [n] = (or 3ts = 0.15 ms) So,

## 20.4 (Solution)

~3

~0.106

2

0

1/3

- 3 ~0.106

<!-- formula-not-decoded -->

- 50 Fp = 0.25, Fs = 0.1 hLP[n] = 0.5 ~ = 0.25, Fis = = 0.4.

To convert LPP to

- 40 kHz.

First, ensure arithmetic symmetry about fo = 8 kHz relocate the stopband edges to [fs1, fs2] = [4,12] kHz (assuming a fixed passband) . So,

Tbe digital frequencies are: Fp = [0.15, 0.25], Fs = [0.1, 0.3], specs: Fip = 0.5(0.25 0.15) 0.05, Fis = 0.5(0.3 0.1) = 0.1

0.2

First, ensure arithmetic symmetry about fo = 12 kHz. relocate the stopband edges to [fs1, fs2] = [10, 14] kHz (assuming a fixed passband) . So,

The digital frequencies are: Fp = [0.2, 0.4], Fs = [0.25, 0.35], Fo = 0.3

These give the LPP specs: Fip = 0.5(0.35 0.25) = 0.05, Fis = 0.5(0.4 - 0.2) = 0.1

To convert LPP to BSF, use hBPln] = 6[n]

## 20.5 (Solution)

<!-- formula-not-decoded -->

- Fr = Fs - Fp = 0.25 0.125 = 0.125. S0 (from Table 20.4), N =

~ 46

- (c) Tbe transition widths are and 1258\_ the smaller one, Fr = = 0.08. Table 20.4), N = ~ 44 Using

S0 (from Fr 5.08

- (d) BSF: fp = [2,12] kHz, fs = [4,8] kHz, 5 = 25 kHz, and a Hamming window.

The transition widths are 42 and the smaller one; Fr = g = 0.08. So (from Table 20.4), N = ~ 44. But; bandstop filters require an odd length. So, N = 45 . Using

- 20.6 (Solution) For a lowpass half-band filter, Fc = 0.25. So, with N = 1l;

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For tbe von Hann window, w[n] = 0.5 + 0.5 cos( 2) ~5 &lt; n &lt;5

<!-- formula-not-decoded -->

Element-wise multiplication gives the windowed impulse response sequence as

<!-- formula-not-decoded -->

The transfer function of the causal filter (using the minimum delay for a causal sequence) is

<!-- formula-not-decoded -->

## 20.7 (Solution)

<!-- formula-not-decoded -->

S0, h[n] = 0.5sinc(0.5n) , &lt; 7. Compute kaiser window w[n] with ß = 1.0808 and multiply to obtain the balf-band filter hw[n] The results are tabulated below.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We tabulate h[n] = O.5sinc(0.5n)   w[n] (with ß = 1.4431), hw{n] and h#Pln] = (~1)"hw[n] for -9 &lt; n &lt; 9

<!-- formula-not-decoded -->

- (c) BPF: fp = [2,3] kHz, fs = [1,4] kHz, Ap = 1 dB, As = 35 dB.

The specs have arithmetic symmetry  Choose $ = 4f0 = 10 kHz

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We tabulate h[n} = 2Fcsinc(2Fcn) = 0.2sinc(0.2n), w[n] with ß = 0.8858,hw[n] and hBP[n] =

<!-- formula-not-decoded -->

- (d) BSF: fp = [1,4] kHz, fs = [2,3] kHz, Ap = IdB, As 35 dB. The specs have arithmetic symmetry. Choose $ = 4fo = 10 kHz

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We tabulate h[n] = 2Fcsinc(2Fcn) = 0.2sinc(0.2n), w[n] with ß = 0.8858, hw [n] and hBs[n] = 2cos(2rnFo)hw [n] = 2cos(0.5nr)hw [n} for -10 &lt;n &lt; 10.

| n   | h[n]    |   w[n] | hw[n}   | hBP[n]   |
|-----|---------|--------|---------|----------|
|     |         | 0.2438 |         | 0        |
| 49  | ~0.0200 | 0.3421 | ~0.0471 | 0        |
| 48  |         | 0.4458 | ~0.0169 | 0.0337   |
| 47  | ~0.0432 | 0.551  | ~0.0238 | 0        |
| 46  | ~0.0312 | 0.6535 |         | ~0.0408  |
| 45  | 0       | 0.7942 | 0       | 0        |
| 44  | 0.0468  | 0.8339 | 0.0390  | ~0.0780  |
| 43  | 0.1009  | 0.9041 | 0.0912  |          |
| 42  | 0.1514  | 0.9565 | 0.1448  | 0.2896   |
| 4   | 0.1871  | 0.989  | 0.1850  | 0        |
|     | 0.2000  | 1      | 0.2000  | 0.6000   |

## 20.8 (Solution)

- (a) Refer to the sketch.

<!-- image -->

N=8, Fc = 0.25, Ftequency spacing AF = We let H(0) = 1.

The DFT requires H(7) = H*(1) and H(6) = H (2) for a real h[n]

<!-- formula-not-decoded -->

Tbe phase shift to make a causal sequence is ø[k] = ~Tk(N 1)/N = ~Tku/8.

<!-- formula-not-decoded -->

- (b) Tbe IDFT of the &amp;-sample H[k] gives h[n] = {0.0708, ~0.1474,0.0439,0.5327,0.5327,0.0439,~0.1474,0.0708}

<!-- formula-not-decoded -->

- 20.9 (Solution) Fp = 0.1, Fs = 0.4

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Rational approximations to œ =

The best approximation (with smallest M) is œ = ? = #

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 20.10 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The windowed impulse response is hw[n] = h[n}w[n] -

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The windowed impulse response is hw [n] = h[nJw[n] = {~0.04,0.54,0,-0.54,0.04} .

## 20.11 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 20.12 (Solution) For a three-stage interpolator with an overall passband attenuation of 3 dB, each stage should have an attenuation of 1 dB. For an overall stopband attenuation of at least 50 dB, each stage could have the same stopband attenuation (50 dB)
- (a) if type 1: h[n] = {2, -3, 4, 1, 4, -3, 2} (even symmetry; N = 7)
- (c) if type 3: h[n] = {2, ~2} (odd symmetry; N = 9)
- 3, ~2} (odd symmetry; N = 8)
- 20.14 (Solution) h[n] bas real coefficients with all its at z = 0. ~(œ+ 1} is an even symmetric sequence poles
- (b) If h[n] is phase its zeros must always lie on the unit circle. FALSE (the poles may be reciprocals e.g. z = 2, 0.5) linear
- (a) If all the zeros lie on the unit circle, h[n] must be linear phase. TRUE.
- (c) If h[n] is odd symmetric; there must be an odd number of zeros at 2 = 1. TRUE.

## 20.15 (Solution)

- = 1, it must be a type 3 sequence. FALSE. For example; a zero at z = ~1 and two zeros at 2 = 1 give H(z) = (z2 2z + 1)(z + 1) whicb is not type 3 (bas even symmetry)
- ~1} wbich is not type 2 (bas odd symmetry) .
- (c) If h[n] has zeros at z = 1 it must be a type 4 sequence. FALSE. For example, two zeros at 2 = 1 give H(z) = 2z + 1), wbich is not type 4 (has even symmetry) (z2

## 20.16 (Solution)

- (a) No zeros at z = 41. Only even symmetry and odd length. type 1. S0,
- Iwo zeros at z = -1, one zero at 2 = 1. Only odd symmetry and even length. type 4. () One zero at z = 1, none at z = -1. Only odd symmetry and even length. So, type 4. So,
- (b) One zero at z = -1, none at z = 1. Only even symmetry and even length. So, type 2
- (e) Two zeros at z = 1, none at z = ~1. Only even symmetry and odd length. type 1\_ So,
- (g) Two zeros at z = 1, one zero at z ~1 Only even symmetry and even length.
- (f) One zero at z = 1, one zero at z = -1. Only odd symmetry and odd length. So, type 3.
- (b) if type 2: h[n] = {2, ~3, 4, 1, 1, 4,

## 20.17 (Solution)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) Zero location: z = 257 Odd symmetry. Even length. = 1) (type 4)

<!-- formula-not-decoded -->

- (d) Zero location: = 0.5ej0.257 Odd symmetry- Odd lengthH(z) = (z \_ )(z 25* ) (z
- 20.18 (Solution) The zeros of various finite length linear phase filters are given. Assuming the smallest length; identify the sequence type; find the transfer function of each filter and identify the filter type
- (a) Zero location: = By conjugate reciprocal symmetry; 251 )(z 2e-j0.257) (type 1) 25r ) (z 2ej0.
- (b) Zero location: z = By conjugate symmetry 0.5e-j0.25*) (type 1)
- (c) Zero locations: 2 = 0.5, conjugate reciprocal symmetry H(z) = (z - 0.5ej0.2 0.5)(z ~ 2) (type 1) ej0.255 By
- (d) Zero locations: z = 0.5, 2 =1 Odd symmetry. By conjugate reciprocal symmetry H(z) = (z - 0.5)(z - 2)(z - 1) (type 4)
- (e) Zero locations: 2 = 0.5, 2 =1 Even symmetry.

By conjugate reciprocal symmetry

## 20.19 (Solution)

- (a) Refer to the figure
- b) Here is the sequence of operations

<!-- image -->

Folded signal

Filter output

Folded output = y|n] # Yi(-F) =X(F)H(-F)

<!-- formula-not-decoded -->

- (c) Since Y(F) is X(F) multiplied by a real quantity; the signal y[n] shows no phase distortion.

## 20.20 (Solution) Refer to the figure. S = 10 kHz

<!-- image -->

<!-- image -->

<!-- image -->

- (a) Passband ripple &amp;p 0.25 (from linear magnitude). Stopband ripple is 60 dB. So, 8, 0.001
- (c) Fp = 0.1 (from linear plot) and Fs = 0.15 (from dB plot)
- (b) As = 60 dB. With peak = 1 and minimum passband = = 0.75, we find Ap = ~20 log(0.75) ~ 2.5 dB gain gain
- (d) Delay = 0'(F) 0' (F) = (slope from phase plot). So, delay 17 ~18 samples. 0.37 Now,
- (e) For a linear phase sequence with a delay of 18, filter length N = 2(18) + 1 =37
- (g) this filter could bave been designed the optimal method (which yields equiripple passband and stopband). Yes, using
- (f) This filter could not have been designed using tbe window method because the ripples in the passband are of equal magnitude (as are the ripples in the stopband) .

## COMPUTATION AND DESIGN

## 20.21 (Solution) the ADSP routine firvind Uses

'PROBLEM 20.21

'Ihe specifications require:

As]=[1 55] dB fp=10 kHz , fs=15 kHz and S=44.1 kHz '[Ap

'Use firvind and 2 kaiser vindow Ihis shows N=34;

'You can reduce N . Choose [N 0.26533 , 1.6241] at Proupt Fc ,

b=firwind('lp' [1 55] 44.1,10,15 ,'kais')

'NOTE:

You could also use dfirgui.

'Svitch to manual mode to enter specs Iben svitch to auto to design.

'Tbe results are shown for auto Svitch to to adjust values

<!-- image -->

## 20.22 (Solution) Uses the ADSP routine firwind

```
'PROBLEM 20.22 'B=35;fi-60; S-150; 'Need S>2B S0 let S-150 'The specifications require As=40 dB_ choose the folloving % As]=[0.1 40] fp=35 Hz , fs=50 kHz and S=150 kHz 'Use firvind and bamning vindow_ Ibis sbows N-33; Fc=0 .28621 b=firvind( 'lp' [0.1 40] ,150,35 ,50_ hamn ) ; 'Hit enter after prorpts 'PART (d): test tbe filter (12O*pi*n/S) ; y=filter(h,1,xn) ; 'Plot after delaying the linear phase output y 'The design objectives are even if we increase the noise level S0 , [Ap
```

```
20.23 (Solution) Uses the ADSP routines firvind, dfdiir 'The specifications are [Ap ,As] =[1,40] dB [fp,fs]-[4 5] kHz S-40 kHz 'Use firvind and Ihis shows N-33; Fc-0.28621 bl-firvind('lp [1 40] ,40,4,5 , 'Choose N-104 b2=firwind('lp= [1 40] 40,4,5 , kais') ; 'Choose N=79 [1 40] 40 ,4,5) ; 'Hit enter (N=61) [nb,db]-dfdiir( 'bv' lp' bili' [1 40] 40,4,5) ; [ne,de]-dfdiir('el' '1p 'bili [1 40] 40,4,5) ; [lengtb(db) length(de)]-1 'Display orders F-0:0.001:0.5;W-2*pi*F;L-length(F); DH-freqz(hl,1,W) ;DK-freqz(h2,1,W) ; DO-freqz(h3,1,W) ;DB-freqz (nb,db ,W) ;DE-freqz(ne,de,W) ; (F,20*10g10(abs( [DH;DK;DO;DB;DEJ))) ,axis( [0 0.5 ~80 5]) ,grid,pause 'Pick passband range to compute delay DH-grpdelay(hl 1,W) ;DK-grpdelay(h2,1 ,W) DO-grpdelay(h3,1,W) ;DB=grpdelay(nb ,db,W) ;DE-grpdelay (ne,de W) ; plot (F [DH ; DK;DO;DB;DE] ) 20.24 (Solution) Uses the ADSP routine dfdiir, firpm 'PROBLEM 20.24 A= [1 50] ; lp bili' ,A,S,fp fs) ; [ne,deJ=dfdiir('el' ,'lp= 'bili' ,A,S,fP,fs); 'Gives length 21 filter F=0:0.005:0.5;W=2*pi*F; DB-grpdelay(nb , K) ;DE-grpdelay(ne de,W) ;DO=grpdelay(ho,1 ,W) ; plot (F , [DB ;DE;DO] ) ,pause 'PART (b) NB-DB (1) ,NE-DE(1) ,NO-DO(1); plot(n,X,n,yb,P,ye) ,grid,pause 'Without delay (n,x,n-NB,yb,n-NE_ ye, n-NO ,yo) 'PART (c) Assume filter vith zero-phase and use the sane 'as the passband to find output Comnpare vith the real output . 'If the two line uP , the distortion is due to attenuation WP=pi* [0.03,0.09,0.15] H-abs(freqz(nb,db ,WP)) ; 'For Butterworth phase distortion present H-abs (freqz(ne,de,WP)); 'For elliptic firpm, plot 'grid db , plot 'grid gain gain
```

```
(n-ME,ye,n,ye1),grid,pause 'No natch, even more pbase distortion H-abs (freqz(ho,1,WP)) ; 'For optimal ~') ,grid 'ear perfect match no phase distortion_ 20.25 (Solution) Uses the ADSP routine lpsig 'PROBLEM 20.25 R=0.2;h2-hi.*cos(2*n*pi#R#Fc)./(1-16*n.*n*R*R#Fc*Fc) ;H2-freqz(h2,1,W) ; plot (F abs ( [HI;H2;H5 ;H9] ) ) ,grid,pause 'We divide by zero for n-5 (in bl) and n=2 (in h5) 'So,replace those values by limiting values (0.05 and 0) R=0.2;h2-hi R=0.5;b5=hi R=0.9;h9=hi #cos H2 ;H5 H9]) ) ,grid,pause [hi;h2;b5;b9] are balf-band for Fc=0.25 and linear phase [AI,P,f]-lpsig(hi) 'Find and plot amplitude spectrum of each filter axis( [0 1 ~0.2 1.2]) 20.26 (Solution) Uses the ADSP routine interpol_ firpmn subplot (2,1,1) ,dtplot (n,X,' .') ,N) ;subplot(2,1,2) ,dtplot(nl,xu, ') ,pause 'PART (b) A=N 'PART (c) Design optimal filter Fs=1.25*FP , [Ap,As]= [0.1,50] dB h=firpn('lp' 'PART (d) y-filter(b,1,xu) ; xiscos(2*pi*Fctnl); subplot (2,1 ,2) 'LInterpolated signal suffers 2 delay of D samples plot get plot ,grid
```

```
'Tbe interpolated signal does not quite match better result is by FFT (bandlinited) interpolation X-fft(x);Y=[X(1:10) zeros (1,80) X(11:20)]; 20.27 (Solution) Uses the ADSP routine firpn 'PROBLEM 20.27 'PART (a) N=4;fs=S-B; h=firpm('lp' 'PARI (b) 'Distribute passband gains [0.5*Ap As] ,N2*S1 ,B,fs) ;b2=h2*N2; 12-length(hl)+length(h2) 'PART (c) The 2-stage design requires tvo length 44 and length 8 filters %Ibis is better than the 76-long filter for single stage design 'PART (d) Use FIR compensating filter (of Prob 15.75) after final stage 20.28 (Solution) Uses the ADSP routine firpm 'PROBLEM 20.28 %1-Stage 'Single stage '2-Stage 2 x 3 distributed gains hl=firpm( 'lp' N2-3;S1=N1*S;fs-S1-B; h2-firpn('lp 12-length(hl)+length(h2) '2-Stage 3 x 2 h3=firpm('lp' 13-length(h3)+lengtb(h4) 'The 2-stage (2 X 3) is best, vitb combined filter length of 36 _ gain [Ap ,
```

```
20.29 (Solution) the ADSP routine 'PROBLEM 20 .29 '1-Stage N-6 ;fs=(S/N)-B; [Ap,As] ,8,B,fs) ; 'Single stage %2-Stage 2 x 3 'Ivo stage vith distributed gains hl-firpn('lp' [Apl,As] ,S1,B,fs); h2-firpn('lp [Apl,As] 52,B,fs) ; 12=length(hl)+length(h2) '2-Stage 3 2 blsfirpn('lp' [Apl ,As] S1,B,fs) ; 'The 2-stage (3 tbe minimum conbined length (36) 20.30 (Solution) Uses the ADSP routines firpm, tinefreq, dtplot 'PROBLEM 20.30 'PART (a) b=f 'irpn('lp [1 ,50] ,1 ,0.1,0.15) enter at prompt subplot (2,2,1) (n/600,abs (fft(x))),axis( [0 0.5 0 inf]). subplot (2,2,3) ,tínefreq(x) ; subplot (2,2,2) ,plot (n/600 ,abs (fft(xf))) ,axis( [0 0.5 0 inf]) subplot (2,2,4) , tinefreq(xf) ;pause subplot,dtplot (n,xf) ,axis([0 100 ~1 1]) ,pause 'PART (b) n1=0:199 ';y=[cos(0.l+nl*pi) cos(0.4*nl*pi) cos(O.7*nl*pi)]; yf=filter(b,1,y); subplot (2,2,1) ,plot(n/600_ abs (fft(y))),axis( [0 0.5 0 inf]) subplot (2,2,3) ,tiuefreq(y) ; subplot (2,2,2) (n/600 ,abs (fft(yf))),axis( [0 0.5 0 inf]) subplot (2,2,4) ,timefreq(yf) ;pause subplot,dtplot yf) ,axis( [0 100 ~1 'Timefreq shovs the spectrum as it evolves in time FFI does not Uses firpm design ,Plot ,Plot (n,
```

## 20.31 (Solution) Uses the ADSP routine and data file nysteryl.mat firpm

```
'PROBLEM 20.31 load nysteryl; clf ,L-length(uysteryl);plot (nysteryl) pause 'PARI (b) 'Pick passband [0.06 0.2] stopband [0.02 0.24] and As]=[1 60] [1 60],1 , [0.06 0.2] [0.02 0.24]) ; grid,pause subplot (2,1,1) ,plot (sigl) '%Can nake out Message says subplot (2,1,2) ,plot (sig2) ,pause 'Can nake vith better result 'PART (c) i-find(abs (HM)>3000) H2-HM;H2(i)=O*i; subplot (2,1,1) ,Plot (F abs (HM) ) ,subplot (2,1,2) ,plot (F_ abs (H2) ) pause mys=real(ifft(H2)); 'Mystery signal minus low freq signal 'Pick Fp=0.0.2, Fs=0.25 to design filter b2-firpn('lp' [1 60] ,1,0.2, 0.25) ; subplot (2,1,1) ,Plot (sig3) subplot (2,1,2) ,plot(siga) 'PART (d) Better detection with (c) by both filt and filtfilt [Ap out part
```

## 20.32 (Solution) Uses the ADSP routines timefrea cbirp, firpm,

```
'PRDBLEM 20.32 'PART (a-b) [1,40] 1,0.04,0.1) ;yl=filtfilt(h,1,x) ; 'Hit enter at' prompt subplot(2,2,1) ,Plot(n/600,abs(fft(x))),axis( [0 0.5 0 inf]) subplot (2,2,3) timefreq(x) ;axis( [0 0.25 0 1]) 0 inf]) subplot (2,2,4) ,tinefreq(yl) ;axis( [0 0.25 0 1]) ,pause 'PARI (c) h2-firpn('bp' [1,40] ,1,0.06,0.01) ;y2-filtfilt(b2,1,x) ; enter at prompt 0 inf]) subplot (2,2,3) ,timefreq(x) ;axis( [0 0.25 0 1]) 0 inf]) plot (,x,n,y2)
```

```
20.33 (Solution) Uses the ADSP routine Psdvelch, timefreq, dtplot 'PROBLEM 20.33 'PART (a-b) subplot(2,1,1) ,Plot(n,*) subplot (2,1,2) ,plot (/N _ abs (fft(x))) ,pause h=firpn('lp [1,40] ,1,0.08,0.25) ;yl=filtfilt(h,1,x); 'Hit enter at subplot (2,2,1) Psdwelcb(x) ;axis( [0 0.5 0 inf]) subplot (2,2,3) ,tinefreq(x) subplot (2,2,2) ,Psdvelch(yl) ;axis( [O 0.5 0 inf]) subplot(2,2,4) ,timefreq(yl) ;pause subplot ,plot (n,yl) ,pause 'PART (c) [1,40] ,1,0.25,0.08) ;y2-filtfilt(h2,1,x); 'Hit enter at prompt 0 inf]) subplot (2,2,3) ,timefreq (x) subplot (2,2,2) ,Psdwelch (y2) ;axis ( [0 0.5 0 inf]) subplot (2,2,4) ,timefreq (y2) ;pause subplot ,dtplot (n,y2 , ) axis( [0 50 -1 1]) 'Can identify period as 10 20.34 (Solution) Uses the ADSP routines firbb 'PROBLEM 20.34 'hl-firpn('lp' [2 40],140,5,10) ; 'Choose odd hl-firpn('lp' [2 42] 140,5,10) ; 'Actually N=41 and Ap=42 meets specs h2=firhb('bp' [2 40] 140, [30 40] [20 50] kais' ) ; 'Hit enter at if rem(1 engtb(hl) ,2) error('Select odd length for optinal filter') return,end n=0,5* (length(hl)-length(h2)) ; 'Add hl and h2 by naking their lengtb equal if 2>0, elseif n<O , else H=freqz(h,1,W) H=abs (H) H-H/max (H) ; [0 70] [-2 -2] :g') , axis( [0 70 20.35 (Solution) Uses the ADSP routines lp2iir , bltZord 'PROBLEM 19.39 b2-firpn('bp= [1 40],8, [300 _ 1000] [5 1250]) ; à3-firpn('bp [1 40] ,S , [1000 ,3000] [300 3700]) ; [1 40] ,S,3000,2000) ; 'Passband edge is 3000 Hz firpm, firpm, grid firpm,
```

```
subplot (2,1,1) ,plot (S*F abs ( [H1 H2 ;H3;H4] ) ) ,grid,pause 'Repeat using firvind. Now , for IIR filter [n2 ,d2]=lpp('bw' ,2,3) ; 'a' n2,d2,S,300) ; [nz4 ,dz4]=lp2iir('bp= subplot(2,1,2) ,plot (StF ,abs ( [H1 H2 ;H3 ;H4] )) 'Ihe FIR realization is much more. complex! ! ,grid
```