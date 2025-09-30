<!-- image -->

## Molecular Energetics

This page intentionally left blank

## Molecular Energetics

## Condensed-Phase Thermochemical Techniques

## José A. Martinho Simões Manuel E. Minas da Piedade

<!-- image -->

<!-- image -->

Oxford University Press, Inc., publishes works that further Oxford University's objective of excellence in research, scholarship, and education.

Oxford NewYork Auckland Cape Town Dar es Salaam Hong Kong Karachi Kuala Lumpur Madrid Melbourne Mexico City Nairobi NewDelhi Shanghai Taipei Toronto

With offices in Argentina Austria Brazil Chile Czech Republic France Greece Guatemala Hungary Italy Japan Poland Portugal Singapore South Korea Switzerland Thailand Turkey Ukraine Vietnam

Copyright © 2008 by Oxford University Press, Inc.

Published by Oxford University Press, Inc. 198 Madison Avenue, New Y ork, New Y ork 10016

www.oup.com

Oxford is a registered trademark of Oxford University Press

All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior permission of Oxford University Press.

Library of Congress Cataloging-in-Publication Data Sim ˜ oes, J. A. Martinho. Molecular energetics : condensed-phase thermochemical techniques /c José A. Martinho Sim ˜ oes and Manuel E. Minas de Piedade. p. cm. Includes bibliographical references and index. ISBN 978-0-19-513319-6 1. Thermochemistry. 2. Thermodynamics. 3. Condensed matter. 4. Molecular dynamics. I. Piedade, M. E. Minas da (Manuel E. Minas) II. Title. QD511.S56 2008 541 ′ .36-dc22 2007060128

9 8 7 6 5

4

3

2

1

Printed in the United States of America on acid-free paper

## Preface

Thermochemistry has been closely associated with techniques such as reactionsolution and combustion calorimetry, although it has long been recognized that thermochemical information can also be obtained from noncalorimetric methods, such as equilibrium and kinetics experiments.

Historically, some of those approaches have been developed with a considerable degree of independence, leading to a proliferation of thermochemical concepts and conventions that may be difficult to grasp. Moreover, the past decades have witnessed the development of new experimental methods, in solution and in the gas phase, that have allowed the thermochemical study of neutral and ionic molecular species not amenable to the classic calorimetric and noncalorimetric techniques. Thus, even the expert reader (e.g., someone who worksonthermochemistryorchemicalkinetics) is often challenged by the variety of new and sophisticated methods that have enriched the literature. For example, it is not uncommon for a calorimetrist to have no idea about the reliability of mass spectrometry data quoted from a paper; many gas-phase kineticists ignore the impact that photoacoustic calorimetry results may have in their own field; most experimentalists are notoriously unaware of the importance of computational chemistry; computational chemists often compare their results with less reliable experimental values; and the 'consistency' of thermochemical data is a frequently ignored issue and responsible for many inaccuracies in literature values.

For the nonexpert reader, the state of thermochemistry can even be more confusing. A synthetic chemist, for instance, is often distressed when attempting to assess the driving force of a reaction from the energies associated with breaking andformingchemicalbonds.Datamaybeavailableorpredictablebutarereported in a variety of (sometimes ill-defined) formats: bond dissociation enthalpies or energies (BDEs), bond enthalpy terms, intrinsic bond enthalpies or energies, mean bond dissociation enthalpies or energies, and so on.

A book offering a comprehensive discussion of the thermodynamic stability of molecules and bonds, together with a description of experimental and computational methodologies that have been used to obtain that information, could therefore be useful and timely. This was our reasoning when we proposed this book to Oxford University Press in 1997, together with our colleagues and friends Drs. Karl K. Irikura and Russell D. Johnson III from the National Institute of Standards and Technology (Gaithersburg, Maryland). However, after some years of planning and writing, we concluded that to keep the book within a reasonable

size and be able to discuss each one of the methods with appropriate detail (to be truly useful for the reader), we could not cover all the gas-phase, solution-phase, theoretical, and empirical methodologies. We have therefore decided to concentrate on condensed-phase methods, because in the meantime excellent works on computational thermochemistry and the main gas-phase methods have appeared. This option, however, did not affect our main goals: to provide a critical view of the most important thermochemical concepts and methods and, above all, to convey useful guidelines on how to choose the 'best' data and use it to understand chemistry.

The book assumes some basic knowledge of physical chemistry, and thus it is recommended for advanced undergraduate or for graduate courses. On the other hand, it contains examples drawn from many areas in chemistry, from organometallic to food chemistry and a commented compilation of the main databases. It may therefore appeal to a broad range of practicing chemists and particularly to those interested in energetics-structure-reactivity relationships.

We finally acknowledge several colleagues who read parts of the manuscript and made many valuable suggestions: Dr. Karl K. Irikura, Dr. Russell D. Johnson III, and Dr. Patrick A. G. O'Hare, from the National Institute of Standards and Technology; Dr. Hermínio P . Diogo, from Instituto Superior Técnico, Lisbon; Dr. Rui M. Borges dos Santos, from the University of Algarve; and Dr. Paulo M. Nunes, Dr. Rui C. Santos, Dr. Miroslav Leskiv, and Dr.Ana L. Lagoa fromtheUniversityofLisbon.AndwewishtothankEdwardSears,JeremyLewis, DaynePoshusta, StephanieAttia, and the staff of Oxford University Press for their assistance in producing this book.

## Contents

## Part I Introduction

| Thermochemistry and Molecular Energetics   | Thermochemistry and Molecular Energetics                         |   3 |
|--------------------------------------------|------------------------------------------------------------------|-----|
| The Thermodynamic Background               | The Thermodynamic Background                                     |   7 |
| 2.1                                        | Units                                                            |   7 |
| 2.2                                        | Nomenclature                                                     |   7 |
| 2.3                                        | Standard States                                                  |   8 |
| 2.4                                        | Enthalpies of Reaction and Standard Enthalpies of Formation      |   9 |
| 2.5                                        | The Selection of Thermochemical Data and More on Standard States |  16 |
| 2.6                                        | The Uncertainties in Thermochemical Data                         |  19 |
| 2.7                                        | Standard Enthalpies of Phase Transition                          |  22 |
| 2.8                                        | Lattice Energy and Ion Solvation Enthalpy                        |  26 |
| 2.9                                        | The Gibbs Energy: First and Second Law Methods                   |  31 |
| 2.10                                       | The Gibbs Energy: Third Law Method                               |  36 |
| The Kinetic Background                     | The Kinetic Background                                           |  38 |
| 3.1                                        | Reactions in the Gas Phase                                       |  38 |
| 3.2                                        | Reactions in Solution                                            |  43 |
| Gas-Phase Ion Energetics                   | Gas-Phase Ion Energetics                                         |  47 |
| 4.1 Ionization Energy and Electron         | Affinity                                                         |  47 |
| 4.2                                        | Appearance Energy                                                |  50 |
| 4.3                                        | Proton Affinity, Basicity, and Acidity                           |  55 |
| Bond Energies                              | Bond Energies                                                    |  58 |
| 5.1                                        | Bond Dissociation Enthalpies and Energies                        |  58 |
| 5.2                                        | Stepwise and Mean Bond Dissociation Enthalpies                   |  64 |
| 5.3 Bond Strengths                         | Bond Enthalpy Contributions and                                  |  68 |
| 5.4                                        | The Laidler Terms                                                |  74 |
| to Part I                                  |                                                                  |  76 |

| viii                                       |                                            | Contents                                     |     |
|--------------------------------------------|--------------------------------------------|----------------------------------------------|-----|
| Part II Condensed Phase Methods            | Part II Condensed Phase Methods            | Part II Condensed Phase Methods              |     |
| 6                                          | Overview of Condensed Phase Methods        | Overview of Condensed Phase Methods          | 83  |
| 7                                          | Combustion Calorimetry                     | Combustion Calorimetry                       | 87  |
|                                            | 7.1                                        | Static-Bomb Combustion Calorimetry in Oxygen | 87  |
|                                            | 7.2                                        | Moving-Bomb Combustion Calorimetry in Oxygen | 108 |
|                                            | 7.3                                        | Flame Combustion Calorimetry in Oxygen       | 114 |
|                                            | 7.4                                        | Fluorine Combustion Calorimetry              | 120 |
| 8                                          | Isoperibol Reaction-Solution Calorimetry   | Isoperibol Reaction-Solution Calorimetry     | 125 |
| 9                                          | Heat Flow Calorimetry                      | Heat Flow Calorimetry                        | 137 |
| 10                                         | Photocalorimetry                           | Photocalorimetry                             | 147 |
| 11                                         | Titration Calorimetry                      | Titration Calorimetry                        | 156 |
|                                            | 11.1                                       | Isoperibol Continuous Titration Calorimetry  | 158 |
|                                            | 11.2                                       | Heat Flow Titration Calorimetry              | 167 |
| 12                                         | Differential Scanning Calorimetry (DSC)    | Differential Scanning Calorimetry (DSC)      | 171 |
|                                            | 12.1                                       | Thermodynamic Data from DSC Experiments      | 175 |
| 13                                         | Photoacoustic Calorimetry                  | Photoacoustic Calorimetry                    | 190 |
| 14                                         | Equilibrium in Solution                    | Equilibrium in Solution                      | 207 |
| 15                                         | Kinetics in Solution                       | Kinetics in Solution                         | 219 |
| 16                                         | Electrochemical Measurements               | Electrochemical Measurements                 | 227 |
|                                            | 16.1                                       | Electrochemistry and Thermodynamics          | 229 |
|                                            | 16.2                                       | Cyclic Voltammetry                           | 231 |
| 16.3 Photomodulation References to Part II | 16.3 Photomodulation References to Part II | 16.3 Photomodulation References to Part II   |     |
|                                            |                                            |                                              | 247 |
| Appendix A: Units, Conversion Factors, and | Appendix A: Units, Conversion Factors, and | Fundamental Constants                        | 267 |
| Appendix B: Thermochemical Databases       | Appendix B: Thermochemical Databases       | Appendix B: Thermochemical Databases         | 270 |
| Index                                      | Index                                      | Index                                        | 283 |

## PART I INTRODUCTION

This page intentionally left blank

1

## Thermochemistry and Molecular Energetics

Thermochemistry has been defined in one of the most popular physical chemistry textbooks as 'the study of the heat produced or required by chemical reactions' [1]. The use of heat , instead of the more general word energy , immediately suggests a close association between thermochemistry and calorimetry-the oldest experimental technique for investigating the thermodynamics of chemical reactions. This view is, in fact, shared by many of our students and some of their teachers, together with the belief that thermochemistry, founded in the eighteenth century by Black, Lavoisier, and Laplace, has seen few major developments since the days of Berthelot and Thomsen, over 100 years ago [2].

The notion that calorimetric studies are almost the sole source of thermochemical information prevails beyond the classroom. Also, the idea of thermochemistry as a science of the past is even conveyed by distinguished scientists and lecturers. Figure 1.1, taken from a delightful account by Herschbach, depicts thermochemistry as a mountain that was necessary to climb to conquer the structure and dynamics summits [3] and reach the ultimate goal-the understanding of chemical synthesis. The picture is enlightening, but the timeline suggests that the climax of the thermochemical era dates back to the early decades of the last century, coinciding with the publication of Lewis and Randall's Thermodynamics and the Free Energy of Chemical Substances [4]. However, the golden years of calorimetry started in the 1930s, thanks to the work on organic compounds and key molecules, such as water and carbon dioxide, by Rossini and his colleagues at the National Bureau of Standards [5], and continued in the 1960s and 1970s. Thermochemical studies of organometallic compounds were pioneered by Skinner and his coworkers at Manchester University [6,7].

Figure 1.1 can also be regarded from a different perspective, which is more correct and probably in keeping with Herschbach' s thoughts: Thermochemistry is not only the first mountain to climb but also the solid ground from which the remaining heights can be reached. The heaven, or the perfect understanding of chemical synthesis, rests on a detailed knowledge of thermochemistry, structure, dynamics, and their relationships.

Figure 1.1 The modern eras of physical chemistry, according to Herschbach [3]. Illustration by Shah Koshbin; courtesy of Professor Herschbach and the Nobel Foundation.

<!-- image -->

In our reading, figure 1.1 clearly shows the importance of thermochemistry in chemical science. This conclusion has never really been in question. There is no chemist or chemical engineer who denies it. Instead, the unresolved true issue raised by figure 1.1 is whether the golden decades of calorimetry provided enough ground to support our understanding of chemical reactivity. Should we spend more time and effort in the measurement of new values, or can they be predicted reliably from earlier results?

This book will provide abundant evidence that the gaps in thermochemical information are still immensely wider than the plateaus and that calorimetry is but one among many experimental methods in modern thermochemistry.As we shall see, 'old' calorimetric methods cannot be used to investigate the thermochemistry of species like short-lived free radicals or gas-phase ions, which are essential for our understanding of reaction dynamics. To address these and other issues, a plethora of new experimental techniques (see figure 1.2) appeared throughout the past two decades, yielding vast amounts of new data that could not have been predicted from the early databases. Thanks to the wealth of results derived from those techniques, and from increasingly powerful and accurate quantum chemistry calculations, further golden years of thermochemistry lie also ahead.

The word energetics , rather than thermochemistry , was adopted in figure 1.2 and in the book title to emphasize that most of the methods displayed do not involve the experimental determination of 'heat.' Furthermore, the use of energetics avoids the traditional link between thermochemistry and calorimetry (which is semantically correct because thermo is the Greek designation for 'heat'). The word molecular , on the other hand, stresses that this book will be mainly concerned with single molecules. Properties like enthalpies of phase transition, which depend on intermolecular interactions, are very important data in their own right, but the methods used to derive them will not be comprehensively covered.

The main purpose of molecular energetics is therefore to investigate the thermodynamic stability of individual molecules and their chemical bonds. Stability , however, is a fairly ambiguous concept. A water molecule, which meets our intuitive criteria of endurance, is promptly destroyed in the presence of sodium atoms. Methane, with its four strong carbon-hydrogen bonds, is easily consumed in a flame by reaction with oxygen. The very reactive methyl radical may survive forever under appropriate conditions. In short, when stating that a given molecule is either thermodynamically 'stable' or 'unstable,' it is essential to specify its physical and chemical environments.

As described in any elementary physical chemistry textbook [8], thermodynamics provides a framework to discuss molecular stability. But to apply that theoretical background we need reliable data, obtained either in the laboratory or through quantum chemical calculations. Both the data and the methods to determine them are the chief concerns of the present book. We will examine all the physical parameters, together with some experimental condensed-phase techniques that are useful to probe the thermodynamic stability of molecules. The diversity of those parameters justifies, in part, what is perhaps the most striking feature of figure 1.2-the large number of techniques that have supplied molecular energetics data. Another, less obvious, reason for such variety is that investigating the stability of a molecule often requires a careful selection of the tools to be used. As we shall see throughout the book, the choice of a given technique is dictated not only by the type of information required but also by the electrical charge and the lifetime of the molecule, the nature of its atoms, the physical state of the substance, and even the amount of available sample.

Figure 1.2 Experimental and computational methods in molecular energetics. Illustration by Rui Alexandre.

<!-- image -->

To keep this volume within a reasonable size and, at the same time, ensure that each one of the thermochemical methods covered would be described with appropriate detail, we have decided not to include gas-phase and quantum chemistry methods. These have been extensively reviewed in recent publications [9-12].

## 2

## The Thermodynamic Background

Thethree laws of thermodynamics provide the theoretical basis required to master nearly all the concepts that are relevant in discussions of molecular energetics. We shall not dwell on those laws, because they are mandatory in any general physical chemistry course [1,8], but we will ponder some of their outcomes. It is also necessary to agree on basic matters, such as units, nomenclature, standard states, thermochemical consistency, uncertainties, and the definition of the most common thermochemical quantities.

## 2.1 UNITS

The International Union of Pure and Applied Chemistry (IUPAC) recommends the use of the International System of Units (SI) in all scientific and technical publications [13]. Appendix A list the names and symbols adopted for the seven SI base units, together with several SI derived units, which have special names and are relevant in molecular energetics.Among the base units, the kelvin (symbol K) and the mole (mol), representing thermodynamic temperature and amount of substance, respectively, are of particular importance. Derived units include the SI unit of energy, the joule (J), and the SI unit of pressure, the pascal (Pa).

It is generally acknowledged that the International System has brought order out of the previous multisystem chaos. The IUPAC recommendations regarding units will therefore be followed in the present book. In some countries, like the United States, units like the calorie, the torr, and the atmosphere, for example, are still common, but they have gradually been replaced by their SI equivalents [14]. However, non-SI units, such as the electronvolt (eV) and the hartree ( E h ) are more convenient to use in many cases. These units, particularly the eV , are prevalent in a large number of recent publications on molecular energetics.

Alist of some non-SI units, together with their SI values, and a table containing the 'best' values of some fundamental physical constants are given in appendixA.

## 2.2 NOMENCLATURE

The names and symbols of physical chemical quantities have also been recommended by the IUPAC [13]. It would be tedious to list even a minor fraction of the

suggestions on symbols, subscripts, and superscripts, in italic, Roman, or Greek fonts. But these matters have importance, and a few common symbols will be described here. Others will be mentioned whenever necessary.

The usual symbols U , H , G , S , and Cp will be adopted for internal energy, enthalpy, Gibbs energy, entropy, and heat capacity at constant pressure, respectively. A change in these thermodynamic quantities is indicated by using the symbol /Delta1 followed by a subscript (specifying the process to which the quantity refers). For instance, a reaction Gibbs energy is represented by /Delta1 r G , a combustion enthalpy by /Delta1 c H , a solution enthalpy by /Delta1 sln H , a vaporization entropy by /Delta1 vap S , and so on. Standard states (see following discussion) will be denoted by a superscript o, as in /Delta1 f H o (H2O, l), the standard enthalpy of formation of liquid water. Although a subscript m has been recommended to indicate a molar quantity, as in /Delta1 f H o m (H2O, l), this subscript will be omitted here.

No symbol has been approved by the IUPAC for dissociation energy in the chemical thermodynamics section [13]. Under 'Atoms and Molecules,' either E d or D is indicated. The latter is more common, and IUPAC recommends D 0 and D e for the dissociation energy from the ground state and from the potential minimum, respectively. Because the 'bond energy' concept will be omnipresent in this book and can be explored in a variety of ways, some extra names and symbols are required. This matter will be handled whenever needed, but for now we agree to use DU o T for a standard bond dissociation internal energy and DH o T for a standard bond dissociation enthalpy , both at a temperature T . In cases where it is clear that the temperature refers to 298.15 K, a subscript T will be omitted.

## 2.3 STANDARD STATES

The values included in thermochemical databases (see appendix B) are normally referred to the substances in their standard states . The standard state notion, which is a consequence of the mathematical formalism used to describe the thermodynamics of reaction and phase equilibria [1], greatly simplifies the calculation of thermochemical quantities for the infinite variety of 'real' processes, that is, those where one or more substances are not in their standard states. This situation will be exemplified in several chapters of the present book, but several case studies are discussed here.

The standard state (and thus any standard thermodynamic property) of a pure solid refers to the pure substance in the solid phase under the pressure p of 1 bar (0.1 MPa). The standard state of a pure liquid refers to the pure substance in the liquid phase at p = 1 bar. When the substance is a pure gas, its standard state is that of an ideal gas at p = 1 bar (or, which is equivalent, that of a real gas at p = 0).

It must be stressed that the temperature is not included in the definition of standard state. Nevertheless, all modern thermochemical databases list the values at 298.15 K, so this is now regarded as a 'reference' temperature. As shown in appendix B, very few data compilations give values at any other temperature.

Thecase of liquid solutions is more complicated because the conventions vary. These are always stated in introductory chapters of the thermochemical databases and deserve a careful reading. In most tables and in the present book, it is agreed that the standard state for the solvent is the pure solvent under the pressure of 1 bar (which corresponds to unit activity). For the solute, the standard state may refer to the substance in a hypothetical ideal solution at unit molality (the amount of substance of solute per kilogram of solvent) or at mole fraction x = 1.

## 2.4 ENTHALPIES OF REACTION AND STANDARD ENTHALPIES OF FORMATION

A few thousand years before the word biotechnology was coined, vinegar had been obtained from the bacterial oxidation of the ethanol contained in natural products like wine, cider, or malt. A pure dilute solution of acetic acid can also be made by the same method when aqueous ethanol is the starting material. The net reaction is represented by:

<!-- formula-not-decoded -->

One of the issues of the industrial process design is related to the heat released by this reaction. A temperature rise will decrease the acetic acid yield, not only because the equilibrium constant becomes lower (the reaction is exothermic; see section 2.9) but also because it will reduce the enzyme activity. It is therefore important to keep the reaction temperature within a certain range, for instance, by using a heat exchanger. However, to design this device we need to know the reaction enthalpy under the experimental conditions, and this quantity cannot be easily found in the chemical literature.

Theproblemcanbetackledbyconsideringreaction2.2,whereallreactantsand products are the pure species in their standard states at 298.15 K, and evaluating /Delta1 r H o ( 2.2 ) from data, which are easily found in thermochemical compilations. These data are the standard enthalpies of formation of the substances involved.

<!-- formula-not-decoded -->

The notion of standard enthalpy of formation of pure substances ( /Delta1 f H o ) as well as the use of these quantities to evaluate reaction enthalpies are covered in general physical chemistry courses [1]. Nevertheless, for sake of clarity, let us review this matter by using the example under discussion. The standard enthalpies of formation of C2H5OH(l), CH3COOH(l), and H2O(l) at 298.15 K are, by definition, the enthalpies of reactions 2.3, 2.4, and 2.5, respectively, where all reactants and products are in their standard states at 298.15 K and the elements are in their most stable physical states at that 'conventional' temperature-the so-called reference states at 298.15 K.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By subtracting reaction 2.3 from the sum of reactions 2.4 and 2.5, we obtain the net reaction 2.2. Hence,

<!-- formula-not-decoded -->

In summary,thestandardenthalpyofformationofapuresubstanceat298.15K is the enthalpy of the reaction where 1 mol of that substance in its standard state is formed from its elements in their standard reference states, all at 298.15 K. A standard reaction enthalpy can be calculated from the values of /Delta1 f H o for reactants and products by using equation 2.7 (Hess' s law):

<!-- formula-not-decoded -->

where ν i are the stoichiometric coefficients, which are negative for the reactants and positive for the products.

It is obvious from the definition of standard enthalpy of formation that these quantities do not represent the 'absolute' enthalpic stability of compounds. They merely reflect their enthalpic stability relative to that of the chemical elements in standard reference states (to which /Delta1 f H o = 0 has been arbitrarily assigned). It is thus unreasonable to state that a given substance is more stable than another just because it has a lower standard enthalpy of formation. We can only use /Delta1 f H o values to make such direct comparisons when we are assessing the relative stability of isomers.

Could we have avoided the convention of /Delta1 f H o = 0 for the elements in their standard reference states? Although this assumption brings no trouble, because we always deal with energy or enthalpy changes , it is interesting to point out that in principle we could use Einstein' s relationship E = mc 2 to calculate the absolute energy content of each molecule in reaction 2.2 and derive /Delta1 r H o from the obtained /Delta1 E . However, this would mean that each molar mass would have to be known with tremendous accuracy-well beyond what is available today. In fact, the enthalpy of reaction 2.2, -492.5 kJ mol -1 (see following discussion) leads to /Delta1 m = /Delta1 E / c 2 of approximately -5.5 × 10 -9 g mol -1 . Hence, for practical purposes, Lavoisier' s mass conservation law is still valid.

The first step toward the resolution of our initial question-the enthalpy of reaction 2.1-has therefore been given by equation 2.6. The second stepreplacing the standard enthalpies of formation by their literature values-is often not trivial. The reason has to do with the consistency of thermochemical data, a subject that will be discussed in section 2.5. For now, we accept the following 'best' values: /Delta1 f H o (CH3COOH, l) = -484.3 ± 0.2 kJ mol -1 [15] /Delta1 f H o (H2O,l) = -285.830 ± 0.040kJmol -1 [16], and /Delta1 f H o (C2H5OH,l) = -277.6 ± 0.3 kJ mol -1 [15], leading to /Delta1 r H o ( 2.2 ) = -492.5 ± 0.4 kJ mol -1 (the calculation of the uncertainty will be addressed in section 2.6).

Toproceed, we need to relate the enthalpy of reaction 2.2 to that of reaction 2.1. As shown by the cycle in figure 2.1 and by equation 2.8, which are based on the fact that the enthalpy is a state function , this turns out to be a simple exercise.

∆

Figure 2.1 Thermochemical cycle, showing how to relate the enthalpy of the experimental reaction 2.1 with reaction 2.2, where reactants and products are in their standard states.

<!-- image -->

All we need to know are the solution enthalpies /Delta1 sln H ( 1 ) , /Delta1 sln H ( 2 ) , /Delta1 sln H ( 3 ) , and /Delta1 sln H ( 4 ) .

<!-- formula-not-decoded -->

Let us suppose that the acetic acid content of the final aqueous solution is 5%, corresponding to a ratio of approximately 1 mol of CH3COOH to 60 mol of H2O. As the yield of reaction 2.1 will be near 100% (recall that reaction 2.2 is rather exothermic, implying a very high equilibrium constant; see section 2.9), the same value will be used for the molar ratio n ( H2O )/ n ( C2H5OH ) , despite the increased total amount of substance of water in the reaction products. In the present case, the difference of 1 mol of water between the product and the reactant mixtures has a negligible enthalpic effect. The enthalpies associated with the solution of ethanol and acetic acid in 60 mol of water are derived from literature data [17] as /Delta1 sln H ( 1 ) = -10.0 ± 0.1 kJ mol -1 and /Delta1 sln H ( 3 ) = -1.0 ± 0.1 kJ mol -1 . This calculation will be detailed in section 2.5.

The state function property of the enthalpy should be kept in mind for the next move of our discussion. In figure 2.1 we have decomposed reaction 2.1 in a series of steps whose net effect must correspond to the overall reaction. This means that the correct value for /Delta1 sln H ( 2 ) is the solution enthalpy of 1 mol of oxygen in the (ethanol + water) mixture described-and not the solution enthalpy of the gas in pure water. Unfortunately, solution enthalpy data in organic liquid mixtures are not abundant in the chemical literature. So, either we are lucky to find them, we have the equipment to measure them in the laboratory, or we assume that the values will be identical to the ones in the pure solvent. The validity of this assumption depends on the system under discussion and on the accuracy needed for the final result, but in the present case it seems fair. Leaving further discussion to section 2.5, we shall take /Delta1 sln H ( 2 ) = -12 ± 4 kJ mol -1 [17].

Finally, in the stepwise method of 'constructing' the final state of reaction 2.1, we can consider that the solution of 1 mol of water in pure water preceded the

addition of the acetic acid, so that we have /Delta1 sln H ( 4 ) = 0. Therefore, the final outcome of our exercise is, from equation 2.8,

<!-- formula-not-decoded -->

that is, the reaction enthalpy under experimental conditions is some 20 kJ mol -1 less negative than the reaction with all substances in their standard states.

We have assumed throughout the previous discussion that the temperature of reaction 2.1 is 298.15 K. What if the reaction enthalpy at a different temperature is required? Let us assume, for instance, that we need to evaluate /Delta1 r H ( 2.1 ) at 310 K. As shown by the cycle in figure 2.2 or by equation 2.9, the first step in this exercise is to evaluate the temperature effect on the standard state reaction 2.2.

<!-- formula-not-decoded -->

Note that /Delta1 r H o 310 and /Delta1 r H o 298 are both standard enthalpies of reaction, albeit at different temperatures. Their difference is given in terms of the enthalpies /Delta1 H ( 1 ) , /Delta1 H ( 2 ) , /Delta1 H ( 3 ) , and /Delta1 H ( 4 ) , which represent the heat required to raise the temperature of each reactant and product from 298.15 K to 310 K and can be calculated from the general equation 2.10.

<!-- formula-not-decoded -->

As shown by equation 2.11, known as the Kirchhoff equation, the standard reaction heat capacity ( /Delta1 r C o p ) is the difference between the standard heat capacities of the products and reactants (recall that ν i are the stoichiometry coefficients-negative for the reactants and positive for the products):

<!-- formula-not-decoded -->

<!-- image -->

2

2

Figure 2.2 Thermochemical cycle relating the enthalpies of reaction 2.2 at 298.15 K and 310 K.

For our example, we have:

<!-- formula-not-decoded -->

To use equation 2.10 correctly, we need to know how the heat capacities vary in the experimental temperature range. However, these data are not always available. A perusal of the chemical literature (see appendix B) will show that information on the temperature dependence of heat capacities is much more abundant for gases than for liquids and solids and can be easily obtained from statistical mechanics calculations or from empirical methods [11]. For substances in condensed states, the lack of experimental values, even at a single temperature, is common. In such cases, either laboratory measurements, using techniques such as differential scanning calorimetry (chapter 12) or empirical estimates may be required.

We said ' may be required' because the most correct use of equation 2.10 is not always necessary. In our example involving formation of acetic acid, the temperature range is very narrow. Hence, it is fair to assume that /Delta1 r C o p is temperature independent and make /Delta1 r H o 310 -/Delta1 r H o 298 ≈ /Delta1 r C o p (310 -298.15).

It is convenient that the temperature correction to the enthalpy of reaction 2.2 is rather small, because it suggests that the difference /Delta1 r H 310 -/Delta1 r H 298 for reaction 2.1 will also be negligible. In fact, we would be in some trouble to evaluate the temperature correction for the process under the experimental conditions, as some of the necessary data are not readily available. To calculate the solution enthalpies shown in figure 2.1 at 310 K (from the values at 298.15 K), both the (known) values of the heat capacities of the pure substances and the (unknown) values of these quantities in solution are required.

Another argument that supports the neglect of /Delta1 r C o p change with T in our case study is that this quantity is not very large for reaction 2.2. By using C o p data (at 298.15 K) from the literature [17], one obtains /Delta1 r C o p = 58.78 J K -1 mol -1 . This leads to 0.70 kJ mol -1 for the difference /Delta1 r H o 310 -/Delta1 r H o 298 , a value that is smaller than the uncertainty in /Delta1 r H o 298 ( ± 4.0 kJ mol -1 ).

Information on partial molar heat capacities [1,18] is indeed very scarce, hindering the calculation of the temperature correction terms for reactions in solution. In most practical situations, we can only hope that these temperature corrections are similar to those derived for the standard state reactions. Fortunately, due to the upper limits set by the normal boiling temperatures of the solvents, the temperatures of reactions in solution are not substantially different from 298.15 K, so large /Delta1 r Cp ( T -298.15 ) corrections are uncommon.

In contrast to the acetic acid case study, there are many important reactions wherein the temperature has a significant effect on the enthalpies. Consider, for example, reaction 2.13, which represents one of the industrial processes for manufacturing acetylene using methane (from natural gas) as the starting material.

<!-- formula-not-decoded -->

Reaction 2.13 is conducted at a temperature of ca. 1500 K. However, this high temperature can only last a few milliseconds, otherwise the decomposition of

acetylene itself will occur. The pyrolysis of methane is thus immediately followed by water cooling. The thermodynamic analysis of the industrial process is a very interesting exercise, but here we will concentrate on calculating the enthalpy of reaction 2.13 at 1500 K. We shall also suppose that the total pressure is maintained at 1 bar.

The strategy to evaluate /Delta1 r H ( 2.13 ) is similar to that adopted for reaction 2.1. First, with equation 2.7, we calculate the standard enthalpy of reaction at 298.15 K as /Delta1 r H o 298 ( 2.13 ) = 377.0 ± 1.1 kJ mol -1 , by using the 'best' values for the standard enthalpies of formation: /Delta1 f H o ( C2H2, g ) = 228.2 ± 0.7 kJ mol -1 and /Delta1 f H o (CH4, g) = -74.4 ± 0.4 kJ mol -1 [15]. Second, as shown in figure 2.3, to derive /Delta1 r H o 1500 weneedtocalculatetheenthalpies /Delta1 H ( 1 ) , /Delta1 H ( 2 ) , and /Delta1 H ( 3 ) , which account for the temperature rise of reactants and products from 298.15 K to 1500 K. This can be done with equations 2.10 and 2.11, using standard heat capacity data in that temperature interval. In the present case, however, not only are these data available, but it is also possible to avoid the numerical (or graphical) integration of equation 2.10, because the quantities H o 1500 -H o 298 are tabulated in the literature for the three substances involved in the reaction. For each compound this difference represents the heat associated with the temperature change, that is,

<!-- formula-not-decoded -->

The literature values for H o 1500 -H o 298 are 78.153 kJ mol -1 (for CH4), 77.572 kJ mol -1 (C2H2 ) , and 36.290 kJ mol -1 (H2 ) [19], leading to /Delta1 r H o 1500 -/Delta1 r H o 298 = 30.1 kJ mol -1 and /Delta1 r H o 1500 ( 2.13 ) = 407.1 kJ mol -1 . The uncertainty in this value is probably less than ± 2.0 kJ mol -1 .

Should we regard 407.1 ± 2.0 kJ mol -1 as the final value for the enthalpy of reaction 2.13 under the experimental conditions? Recall that the starting assumption was p = 1 bar and the standard state conditions refer to the ideal gases at that pressure or to the real gases at zero pressure. The ideal gas model (or the ideal gas equation) describes very well the behavior of most gases at 1 bar, so it is

Figure 2.3 Thermochemical cycle relating the enthalpies of reaction 2.13 at 298.15 K and at 1500 K.

<!-- image -->

expected that the pressure correction is negligible. Y et there are many important reactions at higher pressures for which the correction turns out to be larger than the uncertainty in the standard reaction enthalpy. Keeping these circumstances in mind, we will illustrate the calculation procedure for the case of methane.

Thepressure correction to the enthalpy of a substance, at constant temperature, is given by

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where V is the molar volume. For an ideal gas, pV = RT and (∂ H /∂ p ) T = 0. However, let us assume that the p , V , T data for that substance are not consistent with the ideal gas equation of state. We then have to find a suitable equation of state from which we can derive the integral in equation 2.16 at the temperature of interest. If the search is unsuccessful, then at least we can try to make estimates, for example, by using either one of the virial equations [1,20]:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where B and C in equation 2.17, the so-called second and third virial coefficients, respectively, are tabulated as a function of temperature for many gases [20,21]. Notethatequation2.18ismoreconvenientthan2.17,becausewewishtocalculate (∂ V /∂ T ) p . The coefficients B ′ and C ′ are related to the virial coefficients by simple relationships. For instance, B ′ = B / RT .

The higher the pressure, the larger the number of terms we have to consider in equations 2.17 and 2.18. Let us assume that the pressure is such that only the second term needs to be considered. Then because the virial coefficients depend only on the temperature, we have:

<!-- formula-not-decoded -->

Let us take the case of methane at p = 1 bar. The second virial coefficient at 300 K is -42 × 10 -3 dm 3 mol -1 [20] and a crude estimate of dB / dT around this temperature is ca. -0.5 × 10 -3 dm 3 K -1 mol -1 . Therefore, (∂ H /∂ p ) T ≈ 0.19 dm 3 mol -1 and H ( p = 1bar ) -H ( p = 0 ) = -19 × 10 -3 kJ mol -1 . This is indeed an insignificant value and shows that we do not need to worry about pressure corrections in reaction enthalpies for processes that occur at low enough pressures. But it is always a good idea to check, even if only by using a crude estimate.

Wehave illustrated how standard enthalpy of formation values can be handled to yield data for practical conditions. The procedure always involves thermochemical cycles, relating the standard state processes with those observed in or

the plant or in the laboratory. The cycles should be designed to use values that either are available in databases or can be estimated. There are, however, a few additional issues that should be carefully considered. (1) It is important to understand the meaning of the quantities tabulated in thermochemical compilations and examine the assumptions regarding standard states. As stated in section 2.3, this can usually be achieved by reading the introductory chapters of those publications. (2) The values selected from the literature should be thermochemically 'consistent.' (3) We should always try to assign uncertainty intervals to the final results. These three issues will be addressed next.

## 2.5 THE SELECTION OF THERMOCHEMICAL DATA AND MORE ON STANDARD STATES

We have attempted to collect in appendix B a list of the most used thermochemical databases. Each one has been built with a particular class of substances and a specific set of properties in mind. We can find compilations of thermochemical values for gas-phase ions, for condensed and gas-phase pure organic compounds, for organometallic molecules, for gas-phase organic free radicals, for inorganic substances, and so on. Most are available in printed form, some are distributed in a software package, and a few can be used online, through the World Wide Web.

Adatabase is not usually a mere collection of values quoted from the literature. It commonly involves some critical assessment of those values and an effort to present a consistent set of data. It is important to clarify what we mean by consistency . Suppose that 40 years ago, somebody made a careful determination of the standard enthalpy of combustion of anthracene (reaction 2.20) and obtained /Delta1 c H o (C14H10, cr) = X kJ mol -1 .

<!-- formula-not-decoded -->

To calculate the standard enthalpy of formation of the crystalline compound, our imaginary author would have used the 'best' available values at the time, which were quoted from the widely adopted NBS Circular 500 [22]: /Delta1 f H o (CO2, g) = -394.907 kJ mol -1 and /Delta1 f H o (H2O, l) = -286.131 kJ mol -1 . The final value reported in his publication was, therefore (see equation 2.7), /Delta1 f H o (C14H10, cr) = -6959.4 -X kJ mol -1 .

Though the old and the new experiments led to exactly the same value of the enthalpy of combustion (X) of anthracene, the reported standard enthalpies of

Now suppose that a different group decided in 1995 to check the reliability of the early experiments on the combustion enthalpy of anthracene and obtained exactly the same value (X) for /Delta1 c H o (C14H10, cr). The present recommended values for /Delta1 f H o (CO2, g) and /Delta1 f H o (H2O, l), -393.51 ± 0.13 kJ mol -1 and -285.830 ± 0.040 kJ mol -1 [16] respectively, were chosen by the authors, leading to /Delta1 f H o (C14H10, cr) = -6938.3 -X kJ mol -1 .

formation differ by 21.1 kJ mol -1 ! With this fictitious example we wish to stress that enthalpies of reaction, rather than standard enthalpies of formation, are the true experimental quantities. The latter are anchored on standard enthalpies of formation of other compounds. Therefore, two literature values for the standard enthalpy of formation of a given compound may differ markedly only because they were derived with different ancillary data. In a consistent database, all the standard enthalpies of formation have been recalculated from the original values reported for the reaction enthalpies, on the basis of a single set of auxiliary data that, itself, is internally consistent (and should also be listed). This is the only way to ensure that the errors illustrated above will not affect any reaction enthalpy derived from the standard enthalpies of formation tabulated in the database.

The choice of a given database as source of auxiliary values may not be straightforward, even for a thermochemist. Consistency is a very important criterion, but factors such as the publication year, the assignment of an uncertainty to each value, and even the scientific reputation of the authors or the origin of the database matter. For instance, it would not be sensible to use the old NBS Circular 500 [22] when the NBSTables of Chemical Thermodynamic Properties [17], published in 1982, is available. If we need a value for the standard enthalpy of formation of an organic compound, such as ethanol, we will probably prefer Pedley's Thermodynamic Data and Structures of Organic Compounds [15], published in 1994, which reports the error bars. Finally, if we are looking for the standard enthalpy of formation of any particular substance, we should first check whether it is included in CODATA KeyValues for Thermodynamics [16] or in the very recent Active Thermochemical Tables [23,24].

When we are calculating a reaction enthalpy from the standard enthalpies of formation of reactants and products, we frequently need values from more than one database.The selection is therefore more complicated and requires additional caution to ensure thermochemical consistency. Let us use the discussion after reaction 2.1 to illustrate this point.

The guidelines have been followed to select the standard enthalpies of formation of water (quoted from CODATA ), ethanol, and acetic acid (both from Pedley' s 1994 compilation). These tables are mutually consistent, so the choice brings no problem. However, we were interested in evaluating the enthalpy of reaction 2.1 under given experimental conditions, which involved aqueous solutions with nearly identical mole ratios (ca. 60:1) ethanol:water and acetic acid:water. These solutions can be represented as C2H5OH:nH2O and CH3COOH:mH2O. Reaction 2.1 can thus be rewritten as

( C2H5OH:60H2O )( sln ) + O2 ( sln ) → ( CH3COOH:61H2O )( sln ) + H2O(l) (2.21)

Note that this equation appears to be unbalanced, but this is just the result of the regular notation. Each mole of acetic acid formed will be dissolved in 61 moles of water, because water is a reaction product. As such, this 1 mol of water must also appear separately in the right-hand side of the equation.

The standard enthalpies of formation of all the reactants and products of reaction 2.21 can be found in the NBS Tables of Chemical Thermodynamic Properties [17]: /Delta1 f H o (C2H5OH:60H2O, sln) = -287.72 kJ mol -1 ,

/Delta1 f H o (CH3COOH:61H2O, sln) = -485.46 kJ mol -1 , /Delta1 f H o (H2O, l) = -285.83 kJ mol -1 , and /Delta1 f H o (O2, ao) = -12 kJ mol -1 . The abbreviation 'ao' means 'aqueous solution, unionized substance, standard state 1 mol kg -1 ' (unit molality) [17], and we assume that the standard enthalpy of formation of O2 under the experimental conditions of reaction 2.21 is similar to /Delta1 f H o (O2, ao). The values lead to /Delta1 r H (2.21) = -471.57 kJ mol -1 , which is only less than 0.1 kJ mol -1 more exothermic than the result derived in section 2.4, where a much more complicated procedure was used.

Why did we prefer to use the cycle in figure 2.1 instead of the easier method after equation 2.21? Simply because we had considered that the best data for the standard enthalpies of formation of pure ethanol and acetic acid are those recommended in Pedley's tables [15]. The values ( -277.6 kJ mol -1 and -484.3 kJ mol -1 , respectively) are both about 1 kJ mol -1 less negative than those in the NBS Tables , and their difference nearly cancels when the reaction enthalpy is calculated. But of course, we are seldom so lucky. Using data from different databases may lead to much larger discrepancies.

Havingthus settled on Pedley' s tables for the pure organic compounds, we have then decided to use NBS Tables to derive the solution enthalpies in figure 2.1. The values can be easily evaluated from the differences between the standard enthalpies of formation of the compounds in solution and the standard enthalpies of formation of pure substances, viz .

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

The important point to be noted here is that the calculation uses NBS data only. Had we combined Pedley's standard enthalpies of formation for the pure compounds with the NBS values for the solutions, we would have obtained incorrect results.

In summary, we selected one database (Pedley' s) to quote the standard enthalpies of formation of the pure organic compounds and another database (NBS) to derive the solution enthalpies. Although these databases are not mutually consistent, that did not affect our final result because the 'experimental' enthalpies of solution were calculated with NBS data only.The exercise illustrates the sort of caution one should keep in mind whenever two or more nonconsistent databases are used.

In the foregoing calculation of /Delta1 sln H ( 1 ) and /Delta1 sln H ( 3 ) , we have used the tabulated values for the standard enthalpies of formation of ethanol and acetic acid aqueous solutions. This looks sensible (after the definitions given in section 2.3), because the standard states of ethanol and acetic acid solutions in water correspond to 1 mol of C2H5OH or CH3COOH in about

62.5 mol of water, which is rather close to the experimental ratios. However, a perusal of the NBS Tables [17] shows, for example, that standard enthalpies of formation are also tabulated for (ethanol + water) mixtures with a variety of compositions, for example, /Delta1 f H o (C2H5OH:10H2O, sln) = -284.78 kJ mol -1 , /Delta1 f H o (C2H5OH:100H2O, sln) = -288.01 kJ mol -1 , and /Delta1 f H o (C2H5OH:1000H2O, sln) = -288.27 kJ mol -1 . Strictly speaking, these values do not refer to standard states, but they illustrate a common and convenient practice in thermochemistry: Solution data are often given so that we can derive solution (or dilution) enthalpies. For instance, /Delta1 sln H ( 1 ) refers to the process:

<!-- formula-not-decoded -->

/Delta1 f H o (C2H5OH:60H2O, sln) is, therefore, the apparent molar enthalpy [25] of ethanol in a solution containing 60 mol of water. In other words, the value relies on identical enthalpy contents for the water molecules in solution and as a pure liquid. A dilution enthalpy, for example, from C2H5OH:60H2O to C2H5OH:100H2O, calculated as

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

corresponds to

<!-- formula-not-decoded -->

## 2.6 THE UNCERTAINTIES IN THERMOCHEMICAL DATA

The random uncertainties in thermochemical measurements have been discussed by several authors, notably Rossini and Deming [26], Rossini [27], and Olofsson [28]. The accepted thermochemical convention [29], summarized next, follows the procedure suggested in the first two of these publications.

Assuming that only random errors affect the laboratory determinations of a given reaction enthalpy, the overall uncertainty interval associated with the mean value 〈 /Delta1 r H 〉 of a set of n experiments is usually taken as twice the standard deviation of the mean ( σ m):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where /Delta1 r H i are the values from the individual experiments.Although the factor 2 that multiplies the standard deviation of the mean is a convention, we may note that it is close to Student' s t -factors for n = 5, 6, and 7 ( t = 2.132, 2.015, and 1.943, respectively) and for a probability of 90% [30]. Indeed, for many years it was a common practice in thermochemical studies to consider that the result

〈 /Delta1 r H 〉 ± 2 σ m referred to at least five independent experiments. Unfortunately, this convention has often been forgotten in recent publications, particularly those that do not involve calorimetry. Some authors simply consider the standard deviation of the mean as the experimental uncertainty or multiply σ m by Student's t -factor; others do not provide details about how the uncertainties were evaluated.

Equation 2.26 must be used to derive the overall uncertainty of the enthalpy of any reaction, calculated from the standard enthalpies of formation of reactants and products.

<!-- formula-not-decoded -->

2 σ i are the uncertainties of the standard enthalpies of formation, and ν i are the reaction stoichiometric coefficients. We illustrate this simple calculation with reaction 2.2. The uncertainties assigned to /Delta1 f H o (CH3COOH, l), /Delta1 f H o (C2H5OH, l), and /Delta1 f H o (H2O, l) were 0.2 kJ mol -1 , 0.3 kJ mol -1 , and 0.040 kJ mol -1 , respectively. Therefore, the overall uncertainty of the reaction enthalpy is (0.2 2 + 0.3 2 + 0.040 2 ) 1 / 2 = 0.4 kJ mol -1 .

Equation 2.26 is also used to evaluate the uncertainty of a standard enthalpy of formation, calculated from a reaction enthalpy. Consider, for instance, a selected value for the standard enthalpy of combustion of ferrocene, /Delta1 c H o [Fe( η 5 -C5H5 ) 2, cr] = -5891.5 ± 4.2 kJ mol -1 [31].

<!-- formula-not-decoded -->

Using selected data for /Delta1 f H o (Fe3O4, cr) = -1117.1 ± 2.1 kJ mol -1 [32], /Delta1 f H o (CO2, g) = -393.51 ± 0.13 kJ mol -1 [16], and /Delta1 f H o (H2O, l) = -285.830 ± 0.040 kJ mol -1 [16], we obtain 154.9 ± 4.5 kJ mol -1 for the standard enthalpy of formation of ferrocene, where the uncertainty was calculated from {4.2 2 + [(1/3) × 2.1] 2 + (10 × 0.13) 2 + ( 5 × 0.040 ) 2 } 1 / 2 .

<!-- formula-not-decoded -->

Assigning uncertainties to experimental (or even theoretical [33]) results is a very important issue and deserves careful consideration. As already pointed out, this is not observed in many recent publications, hindering (to some extent) a reliable assessment of the data given there. If the accepted rules are followed, we may draw useful conclusions from the error bars. For instance, when the difference between two literature values for the enthalpy of the same reaction is larger than the sum of the respective uncertainties, it is likely that at least one of the results is affected by systematic errors. This is the case, for example, of two literature values for /Delta1 c H o [Fe( η 5 -C5H5 ) 2, cr], -5891.5 ± 4.2 kJ mol -1 and -5877.7 ± 5.0 kJ mol -1 [31]. On the other hand, if the difference between a pair of values is smaller than the sum of the uncertainties, as in /Delta1 f H o (LiOC2H5, cr), -477.1 ± 4.0 kJ mol -1 and -473.1 ± 2.5 kJ mol -1 [25], we may conclude that systematic errors are probably absent in both results.

Acommonissuerelatedtothepreviousexampleishowtocalculatetheaverage of several results that are not affected by any systematic errors. The correct procedure involves the calculation of the weighed mean, given by:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For instance, the two values of the enthalpy of formation of LiOC2H5, quoted before, lead to a weighed mean of -474.2 ± 2.1 kJ mol -1 .

One of the best examples of the significance of errors in thermochemistry is provided by methane. This substance is the principal constituent of natural gas, having a mole fraction in the range of ca. 0.70-0.96, the remaining components being nitrogen, ethane, propane, carbon dioxide, and so on.The commercial value of natural gas, which is an important domestic and industrial fuel, is determined by its calorific value , defined as the enthalpy of combustion in air of a specified quantity of gas, under given conditions (usually at 273.15 K and 1 atm). If the water produced is referred to the liquid state, we talk about the superior calorific value; if that water is in the vapor state, then the inferior calorific value is considered. The two quantities are of course related through the enthalpy of vaporization of water.

The calculation of the calorific value for a given composition of natural gas relies on the standard enthalpies of combustion of their components. Among these data, /Delta1 c H o (CH4, g) is by far the most important. Let us suppose, for sake of simplicity, that only methane is present in the natural gas to be exported from the Republic of Easyprofit to the Hardwork Kingdom. In the course of the negotiation, the parties agreed to pay 0.5 cents (US$) per megajoule of superior calorific value. However, the Hardwork Kingdom representative declares that the calculation of this latter quantity should rely on -74.81 kJ mol -1 for the standard enthalpy of formation of CH4, as recommended in a publication by the the former National Bureau of Standards [17], whereas the Republic of Easyprofit executive claims that the most accurate value for /Delta1 f H o (CH4, g) = -74.4 ± 0.4 kJ mol -1 is given in Pedley' s compilation [15]. In other words, the seller claims that the combustion enthalpy of the natural gas is -890.77 kJ mol -1 , whereas the buyer maintains that -890.36 kJ mol -1 is correct. Now, Hardwork wants to import 50,000 million cubic meters per year. At 0 ◦ C and 1 atm, this corresponds to 2,230,749 million moles of methane and, according to their favorite value for the combustion enthalpy, costs US$9,930,848,400. However, based on the more negative value, Easyprofit asks US$9,935,421,435, that is, some US$4.6 million more.

The previous example (which incidentally is not entirely fictional) shows that a discrepancy of 0.4 kJ mol -1 in the standard enthalpy of formation of methane has some economic impact. To avoid disputes like this one, the International Organization for Standardization (ISO) has issued an International Standard on the subject [34]. The 46-page publication includes a detailed discussion of the

procedures for evaluating the calorific value of natural gas from its composition, together with an assessment of the experimental results for the standard enhalpy of combustion of methane. The recommended value, /Delta1 c H o (CH4, g) = -890.63 ± 0.53 kJ mol -1 , is consistent with /Delta1 f H o (CH4, g) = -74.54 ± 0.55 kJ mol -1 . It can be argued that this selection is slightly unfavorable to Easyprofit.

## 2.7 STANDARD ENTHALPIES OF PHASE TRANSITION

The enthalpies of phase transition, such as fusion ( /Delta1 fus H ) , vaporization ( /Delta1 vap H ) , sublimation ( /Delta1 sub H ) , and solution ( /Delta1 sln H ) , are usually regarded as thermophysical properties, because they refer to processes where no intramolecular bonds are cleaved or formed.As such, a detailed discussion of the experimental methods (or the estimation procedures) to determine them is outside the scope of the present book. Nevertheless, some of the techniques addressed in part II can be used for that purpose. For instance, differential scanning calorimetry is often applied to measure /Delta1 fus H and, less frequently, /Delta1 vap H and /Delta1 sub H . Many of the reported /Delta1 sub H data have been determined with Calvet microcalorimeters (see chapter 9) and from vapor pressure against temperature data obtained with Knudsen cells [35-38]. Reaction-solution calorimetry is the main source of /Delta1 sln H values. All these auxiliary values are very important because they are frequently required to calculate gas-phase reaction enthalpies and to derive information on the 'strengths' of chemical bonds (see chapter 5)-one of the main goals of molecular energetics. It is thus appropriate to make a brief review of the subject in this introduction.

The standard enthalpy of transition of a substance A from a phase α to a phase β ( /Delta1 trs H o ) is the enthalpy associated with the process:

<!-- formula-not-decoded -->

where A is in its standard state, in both phases. The way this definition is given makes it rather useful because the standard enthalpy of transition is simply the difference between the standard enthalpies of formation of A in the phases β and α :

<!-- formula-not-decoded -->

We have already illustrated equation 2.32 for a solution enthalpy (of liquid ethanol; see section 2.5). We now apply it to another phase transition: the vaporization of a pure substance.

Although calorimetric methods are usually regarded as yielding the most accurate enthalpies of vaporization [39], the measurement of the saturation vapor pressures of a liquid as a function of temperature is also widely used for the same purpose and may afford good quality data. Among these so-called vapor pressure methods [35], differential ebulliometry is probably one of the most reliable. Briefly, the ebulliometric method consists in measuring the boiling temperatures of a liquid at different pressures. In the differential set-up, the pressure over the

sample is determined by measuring the boiling temperature of a reference liquid (for which the pressure-temperature curve is accurately known) contained in a second ebulliometer.

One of the critical issues in vapor pressure methods is the choice of the procedure to calculate the vaporization enthalpy. For instance, consider the vapor pressures of ethanol at several temperatures in the range 309-343 K, obtained with a differential ebulliometer [40]. The simplest way of deriving an enthalpy of vaporization from the curve shown in figure 2.4 is by fitting those data with the integrated form of the Clausius-Clapeyron equation [1]:

<!-- formula-not-decoded -->

where A is a constant. This equation assumes that (1) /Delta1 vap H is constant in the experimental temperature range and therefore refers to the mean temperature of that interval ( Tm = 326 K) and to the corresponding vapor pressure (7848 Pa); (2) the molar volume of liquid ethanol is negligible compared with the molar volume of the vapor; (3) the vapor obeys to the ideal gas model.

Using the data of figure 2.4, the plot of ln p against 1/ T leads to a excellent straight line (inset of figure 2.4; correlation coefficient 0.9999) and allows the enthalpy of vaporization of ethanol to be derived as 41.8 kJ mol -1 from the slope of that line ( -5024.27).

As mentioned, /Delta1 vap H refers to 326 K and to 7848 Pa, that is, the calculated value is not the standard enthalpy of vaporization. The correction to the standard states (at 326 K) could be estimated with equation 2.16, but there are more

<!-- image -->

T

/K

Figure 2.4 Vapor pressures of ethanol in the 309-343 K temperature range, obtained by an ebulliometric technique [40].

convenient alternatives. One of these makes use of equation 2.34, where Z is the compressibility factor of the vapor ( Z = pV / RT ):

<!-- formula-not-decoded -->

The ideal gas hypothesis is avoided by equation 2.34. Moreover, to derive this equation, it has been assumed that the quotient /Delta1 vap H / Z is constant in the experimental temperature range. Now this ratio divided by the gas constant ( R ) is equal to the slope of the correlation, which implies that /Delta1 vap H can be evaluated at a given temperature if Z is known.

The calculation of compressibility factors of gaseous ethanol can be made with equation 2.18, because the second virial coefficient ( B ) is available at different temperatures [20] and the saturation vapor pressures can be interpolated or extrapolated from the experimental data (figure 2.4). One obtains Z = 0.991 at 298.15 K ( p = 7848.0 Pa) and Z = 0.975 at 326 K ( p = 33778 Pa) [40], leading to /Delta1 vap H = 41.4 kJ mol -1 and 40.7 kJ mol -1 , respectively. Note that none of these values are standard enthalpies of vaporization. We can anticipate that the corrections will be negligible, but let us make a quick check, using /Delta1 vap H at 298.15 K.

The pressure effect on the enthalpy of liquid ethanol can be estimated from equation 2.15, now written in terms of the coefficient of thermal expansion, α :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where

Therefore,

<!-- formula-not-decoded -->

The molar volume ( V ) is calculated as 58.4 cm 3 mol -1 [30], α is taken as 11.2 × 10 -4 K -1 [1], and the saturation pressure at 298.15 K was given above ( p sat = 78.48 × 10 -3 bar). We do not need to worry about finding the 'best' literature values for these quantities, because the enthalpy correction will be very small (actually, the values of V and α refer to 273.15 K). In fact, making T = 298.15 K, we obtain H ( 1 bar ) -H ( p sat ) = 4.6 × 10 -3 kJ mol -1 for liquid ethanol.

In summary, the correction of the enthalpy of vaporization at 298.5 K for the standard states of the liquid and the vapor is /Delta1 vap H o -/Delta1 vap H =

The pressure effect on the enthalpy of gaseous ethanol, on the other hand, can be estimated from equation 2.19. We shall use B = -2.935 dm 3 mol -1 [20] and d B /d T = 0.0341 dm 3 K -1 mol -1 [40]. Therefore, (∂ H /∂ p ) T = -13.1 dm 3 mol -1 and the correction for the standard state ( p = 0) amounts to -13.1 × 10 -3 × ( 0 -7848 ) = 0.103 kJ mol -1 .

( 0.103 -0.0046 ) = 0.098 kJ mol -1 ; this one-tenth of a kilojoule is only a fraction of the experimental uncertainty in this case ( ∼ 0.5 kJ mol -1 [40]).

There are more sophisticated methods to evaluate /Delta1 vap H (and thus, /Delta1 vap H o ) than by using equation 2.34. They all assume nonlinear correlations between ln p and 1/ T . For instance, the vapor pressures in figure 2.4 can be fitted with the Antoine equation, which has three adjustable parameters ( A , B , and C ; equation 2.38), or even to expressions involving a larger number of parameters, such as Riedel' s equation (equation 2.39) [41].

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In both cases, the variation of the vaporization enthalpy with temperature is implicit. /Delta1 vap H is now calculated, at any temperature, from equation 2.40, and the correction to the standard states, if required, is made as already described.

<!-- formula-not-decoded -->

Equations 2.39 and 2.40 lead to /Delta1 vap H o (C2H5OH) = 42.4 ± 0.5 kJ mol -1 [40], which agrees with the mean of the calorimetric results for the same liquid, 42.30 ± 0.04 kJ mol -1 [39]. Note that the less sophisticated approach (equation 2.33) apparently underestimates the vaporization enthalpy by 0.6 kJ mol -1 . However, this is not true because /Delta1 vap H = 41.8 kJ mol -1 refers to the mean temperature, 326 K. A temperature correction is possible in this case, because the molar heat capacities of liquid and gaseous ethanol are available as a function of T [40]. That correction can be obtained as:

<!-- formula-not-decoded -->

Therefore, the calculation with equation 2.33 actually overestimates by 0.8 kJ mol -1 the value derived with the most accurate procedure.

Low cost is one of the main advantages of the vapor pressure methods, as compared with calorimetric techniques. An apparatus to measure the vapor pressures of low boiling temperature liquids can be built easily in an undergraduate chemistry laboratory. However, the same is not quite true if we want to measure the vapor pressures of low-volatility substances, such as most solids. In these cases, Knudsen cells are usually the method of choice, but they require more expensive high-vacuum equipment [36].

The vapor pressure against temperature data obtained with a Knudsen cell set-up are handled as already described for a low boiling temperature liquid. The main difference stems from the very low pressure of the vapor in equilibrium with the solid, which justifies the adoption of the ideal gas model in this case. /Delta1 sub H o at the mean temperature can then be derived from equation 2.40 (with Z = 1) and the correction to 298.15 K can be made with an equation similar to 2.41.

Thissection is concluded by discussing another type of phase transition, known as solvation , which refers to the dissolution of a gaseous substance in a liquid solvent. We already met this concept when we were deriving the enthalpy of reaction 2.1 (see figure 2.1 and sections 2.4 and 2.5): the solution enthalpy of gaseous O2 in water, /Delta1 sln H ( 2 ) , can also be called the solvation enthalpy of O2 in water. Note that when the solvent is water, the word solvation is often replaced by hydration .

The standard enthalpy of solvation of any substance A, therefore, is the difference between its standard enthalpy of formation in solution and its standard enthalpy of formation in the gas phase:

<!-- formula-not-decoded -->

If A is a gas at ambient temperature and pressure, /Delta1 solv H o can be determined experimentally by calorimetric methods or from measurements of the solubility change with temperature [42-44]. When A is a liquid or a solid, its solvation enthalpy in a given solvent is usually calculated from its standard solution enthalpy ( /Delta1 sln H o ) and its standard vaporization or sublimation enthalpy:

<!-- formula-not-decoded -->

or

<!-- formula-not-decoded -->

Most of the methods for estimating reaction enthalpies are applicable only to the gas phase. Solvation enthalpy data are thus particularly important because they allow gas-phase estimates to be extended to reactions in solution-which is the most common medium for reactions of practical interest. However, solvation enthalpies are not very abundant and must often be estimated. Unfortunately, this can be a difficult exercise, especially when A is a solid, because sublimation enthalpies are scarce and hard to estimate. Thus, /Delta1 sub H o ( A ) is usually the unknown term in equation 2.44. The solution enthalpy term, /Delta1 sln H o ( A ) , is generally small and can often be predicted-or determined with a calorimeter.

Solvation enthalpy data for neutral short-lived species, like radicals, are even more scant than for long-lived 'stable' molecules. They can only be experimentally determined through indirect methods, namely, by comparing the enthalpies of reactions of those species in solution and in the gas phase. The former are obtained, for instance, by using the photoacoustic calorimetry technique (see chapter 13), and the latter by several gas-phase methods.

## 2.8 LATTICE ENERGY AND ION SOLVATION ENTHALPY

Mass spectrometric measurements coupled with solution thermochemical results are the sources of solvation enthalpy values for anions and cations. These data are related to the lattice energy , which is a parameter used to assess the ionic character of solids and predict their standard enthalpies of formation.An introduction to that

concept can be found in general chemistry textbooks, and more comprehensive discussions are included in inorganic chemistry publications [45-47]. Here, we approach the subject through another case study.

Consider figure 2.5, which is a thermochemical scheme involving crystalline lithium methoxide (LiOCH3) as the starting substance. The lattice energy, /Delta1 lat U o ( LiOCH3), is the internal energy associated to the following process, at 298.15 K:

<!-- formula-not-decoded -->

In other words, /Delta1 lat U o ( LiOCH3 ) is the energy required to destroy the crystalline network, yielding the gas-phase ions. As the cation and the anion are infinitely separated, the gas phase can be described by the ideal gas model and the enthalpy corresponding to the same process is given by

<!-- formula-not-decoded -->

where /Delta1ν = 2.

The enthalpy of reaction 2.45 cannot be determined directly. As shown in figure 2.5, it is calculated by using several experimental quantities: the standard enthalpy of formation of the solid alkoxide, the standard sublimation enthalpy and the ionization energy of lithium, and the standard enthalpy of formation and the adiabatic electron affinity of gaseous methoxy radical (equation 2.47).

<!-- formula-not-decoded -->

The last two terms in equation 2.47, the ionization energy of Li and the adiabatic electron affinity of CH3O, respectively, will be discussed in section 4.1. For now, it is enough to note that both processes are referred to T = 0 and that 2.5 RT in figure 2.5 is an approximate correction to 298.15 K. Notice also that this correction cancels out in equation 2.47.

By using the data accepted in the original publication where this subject was addressed [48], namely, /Delta1 f H o ( LiOCH3, cr) = -433.0 ± 2.4 kJ mol -1 , /Delta1 f H o ( CH3O, g) = 18 ± 4 kJ mol -1 , /Delta1 sub H o ( Li) = 159.4 kJ mol -1 , E i ( Li ) = 526.4 kJ mol -1 , and E ea ( CH3O) = 151.4 ± 2.1 kJ mol -1 , /Delta1 lat H o ( LiOCH3 ) is derived as 985.4 ± 5.0 kJ mol -1 . However, this value is not by itself very informative. A large number suggests strong ionic bonding (or a strong coulombic interaction) between lithium cation and the methoxy anion. But how high is 985 kJ mol -1 ? Consider the data for other lithium alkoxides and particularly for lithium hydroxide.Table 2.1 shows that /Delta1 lat H o ( LiOCH3 ) is only 5% smaller than the lattice enthalpy of LiOH, which is a rather ionic compound. It is observed, on the other hand, that /Delta1 lat H o decreases with the length of the n -alkyl chain and the bulkier tert -butoxide has a lower lattice enthalpy than its linear analog.

Lattice enthalpies of ionic solids can be predicted from several equations, which account for the coulombic interactions [45-47,49]. The estimates can then be used to derive the standard enthalpies of formation, by equation 2.47. However,

Figure 2.5 The Born-Haber cycle for lithium methoxide and the hydration enthalpies of the ions.

<!-- image -->

Table 2.1 Lattice enthalpies at 298.15 K. Data from [48].

| Solid           | /Delta1 lat H o /(kJ mol - 1   |
|-----------------|--------------------------------|
| LiOH            | 1033 ± 4                       |
| LiOCH 3         | 985 ± 5                        |
| LiOC 2 H 5      | 975 ± 6                        |
| LiO- i -C 3 H 7 | 956 ± 5                        |
| LiOC 4 H 9      | 964 ± 15                       |
| LiO- t -C 4 H 9 | 919 ± 8                        |

it is appropriate to mention here that those equations yield lattice enthalpies at T = 0 ( /Delta1 lat U o 0 ) and not at T = 298.15 K.The calculation of /Delta1 lat H o from /Delta1 lat U o 0 is made with equations similar to 2.10 or 2.14 (section 2.4), that is, it relies on heat capacity data. As this information is not always available, estimates may be required, both for the solid and for the gas-phase ions. Fortunately, the difference /Delta1 lat H o -/Delta1 lat U o 0 is often fairly small-comparable to the uncertainty that usually affects experimental values of the lattice enthalpy. For instance, in the case of LiOH, using data from the NBSTables [17],

<!-- formula-not-decoded -->

Figure 2.5 shows yet another way of 'destroying' the lattice: The ionic solid can be dissolved in water and the ions become hydrated . This solution enthalpy, /Delta1 sln H o (LiOCH3, cr), which is related to the lattice enthalpy by

<!-- formula-not-decoded -->

could yield the sum of the hydration entalpies of the ions. In reality, however, the solution enthalpy term in equation 2.49 is not experimentally measurable; lithium methoxide reacts promptly with water, yielding lithium hydroxide and methanol.

'Reactive' ionic compounds are therefore useless to derive hydration enthalpies (or more generally, solvation enthalpies). Fortunately, there are many alternatives. Take lithium chloride, for example, and data from the NBS Tables [17]. The enthalpy of solution of this solid in water, at infinite dilution, is given by

<!-- formula-not-decoded -->

where 'ai' means 'aqueous solution, ionized substance, m = 1 mol kg -1 ' [17]. By writing an equation similar to 2.49 for LiCl,

<!-- formula-not-decoded -->

it is now possible to obtain the sum of the hydration enthalpies, because the value for the lattice enthalpy is available. However, we aim to derive the hydration enthalpy for the separate cation and anion, rather than their sum. But this goal is unreachable by using the lattice energies combined with solution enthalpies: When lithium chloride (or any other solid ionic compound) is dissolved in water, the lattice is destroyed and both ions become hydrated. Solution enthalpies therefore refer to the overall processes and reflect the solvation of the cation and the anion. How can we untangle these quantities?

Each hydration enthalpy is simply the difference between the standard enthalpies of formation of the substance in water and in the gas phase. Because /Delta1 f H o ( Li + , g) and /Delta1 f H o ( Cl -, g) are both experimentally known, the unknown quantities are /Delta1 f H o ( Li + , ao) and /Delta1 f H o ( Cl -, ao). In other words, the central issue is the determination of standard enthalpies of formation of aqueous ions. The usual approach is simple to describe; it is agreed that the standard enthalpy of formation of aqueous H + is arbitrarily zero, /Delta1 f H o ( H + , ao) = 0.

Consider the dissolution of hydrochloric acid in water. The enthalpy of formation of aqueous HCl at infinite dilution can be described as /Delta1 f H o ( H + , ao) + /Delta1 f H o ( Cl -, ao). Accepting the convention /Delta1 f H o ( H + , ao) = 0, /Delta1 f H o ( HCl, ai) = /Delta1 f H o ( Cl -, ao) = -167.16 kJ mol -1 . This value can then be used to derive a relative number for /Delta1 f H o ( Li + , ao):

<!-- formula-not-decoded -->

A similar exercise can be made with other anions and cations, producing a list of relative values of standard enthalpies of formation, anchored on /Delta1 f H o ( H + , ao) = 0. This database is rather useful, because it allows the enthalpies of formation (equation 2.53) and the lattice enthalpies (equation 2.47) of many crystalline ionic salts to be predicted, since their solution enthalpies are usually easy to measure.

<!-- formula-not-decoded -->

The inconvenience of the convention /Delta1 f H o ( H + , ao) = 0 is, of course, that it does not provide absolute values of the ion hydration enthalpies-only relative numbers can be evaluated. In other words, it tells nothing about the real size of the difference between the energetics of gas-phase and solution ions. Y et given the uncertainty that still affects the value of /Delta1 f H o ( H + , ao) [50], the convention is a sensible option.

## 2.9 THE GIBBS ENERGY: FIRST AND SECOND LAW METHODS

Our attention has so far been focused on the discussion of enthalpy and internal energy changes. Both quantities are offsprings of the first law of thermodynamics [1] and can be determined for many chemical processes by evaluating the heat released by the system under study, either at constant volume or at constant pressure. This 'direct' procedure of determining the change of enthalpy or internal energy, involving a calorimeter, is known as the first law method .

The introduction of the entropy concept through the second law of thermodynamics led to the understanding of the direction of spontaneous changes and unveiled the basis of chemical equilibria [1]. Furthermore, it extended the experimental tools of molecular energetics by providing new methodologies to determine enthalpies or internal energies. The purpose of the present section is to review the thermodynamic background of these so-called second law methods .

Perhaps the two most important outcomes of the first and the second laws of thermodynamicsforchemistryarerepresentedbyequation2.54,whichrelatesthe standard Gibbs energy ( /Delta1 r G o ) with the equilibrium constant ( K ) of a chemical reaction at a given temperature, and by equation 2.55, which relates /Delta1 r G o with the standard reaction enthalpy ( /Delta1 r H o ) and the standard reaction entropy ( /Delta1 r S o ) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equations 2.54 and 2.55 are used to calculate the yields of chemical reactions and how they vary with temperature and pressure. It is appropriate to recall that reliable results for the equilibrium constant demand very accurate /Delta1 r G o values. This stems, of course, from the exponential dependence of K on /Delta1 r G o . Figure 2.6 offers a graphical view of how a typical error bar in /Delta1 r G o ( ± 4 kJ mol -1 ) affects K at 298.15 K. Curve b is a plot of K against the 'accurate' /Delta1 r G o values. Curve a , which represents the upper limit of the uncertainty in K , was obtained by plotting K against ( /Delta1 r G o -4) kJ mol -1 . Curve c , the lower limit, shows K versus ( /Delta1 r G o + 4) kJ mol -1 . This exercise was restricted to Gibbs energies in the range of 0 to -10 kJ mol -1 because for more exergonic ( /Delta1 r G o &lt; 0) reactions the values of K are such that the yields are close to 100%. Consider, for instance, the isomerization reaction

<!-- formula-not-decoded -->

For /Delta1 r G o = -12 kJ mol -1 , K = 126.6, and 99.2% of A is converted into B. If /Delta1 r G o becomes -8 kJ mol -1 , K = 25.21, and the yield is 96.2%; with /Delta1 r G o = -16 kJ mol -1 , K = 635.4, and the yield is 99.8%. Thus, although the errors in K are enormous, the yields do not vary that much-they are all near 100%. In other words, when /Delta1 r G o becomes more negative, its inaccuracy leads to huge errors in the equilibrium constants, but this is not important because the conversion of A into B is almost complete. By contrast, for reactions that have /Delta1 r G o values closer to zero, the uncertainty has a dramatic influence on the yield. For /Delta1 r G o = -4 ± 4 kJ mol -1 , K varies between 1 and 25.21, and the yield correspondingly ranges from 50% to 96%.

<!-- image -->

r

Figure 2.6 How does a ± 4 kJ mol -1 error bar in the reaction Gibbs energy affect the value of the equilibrium constant? Curve b represents the 'accurate' data; curves a and c show the upper and lower limits, respectively.

It will be shown in several chapters of this book that equations 2.54 and 2.55 are also employed to derive /Delta1 r H o and /Delta1 r S o from equilibrium constant data at several temperatures. The simplest procedure involves van't Hoff equation written as

<!-- formula-not-decoded -->

where the subscript T indicates that the reaction enthalpy and entropy may not necessarily refer to 298.15 K. Equation 2.57 is strictly valid at a single temperature. However, if a plot of ln K against 1/ T leads to an acceptable straight line, it is normally assumed that the reaction enthalpy and entropy remain approximately constant over the experimental temperature range (i.e., /Delta1 r C o p ≈ 0). Thus, /Delta1 r H o T and /Delta1 r S o T can be derived from the slope and the intercept of the line, respectively, and both refer to the mean temperature of that range. The problem with this method is the unknown effect of the 'straightness' of the line on the accuracy of the derived values. Slight curvatures of statistically sound straight lines are easy to overlook. Therefore, a safer approach in handling the experimental data is to use the general form of the van't Hoff equation, which allows one to obtain /Delta1 r H o T at any given temperature from the plot of ln K versus 1 / T :

<!-- formula-not-decoded -->

Equation 2.58 is applied to any suitable function fitted to the data. For instance, the equation

<!-- formula-not-decoded -->

where A , B , and C are adjustable parameters, accounts for temperature changes of the reaction enthalpy and entropy but assumes that the reaction heat capacity ( /Delta1 r C o p ) is constant in the experimental temperature range. Although this approximation is usually good, it can be avoided by using more complex fitting equations (similar, e.g., to equation 2.39). Note, however, that because the determination of a /Delta1 r H o T value requires a derivative of the curve, nonlinear fits often require very accurate data to yield reliable results.

Once /Delta1 r H o T is determined at a given temperature, equations 2.54 and 2.55 can be used to obtain /Delta1 r S o T at the same temperature (but that is often found in practice to be unreliable). To calculate the standard reaction enthalpy at 298.15 K, we can use the procedures described after equations 2.10 or 2.14. On the other hand, the standard reaction entropy at 298.15 K can be derived from

<!-- formula-not-decoded -->

The possibility of evaluating both the reaction enthalpy and entropy is the main-but not the only-advantage of the second law over the first law method. Consider, for instance, the thermochemical study of a reaction that is part of a complex, multireaction network of solution equilibria. In this case, first law methods are inappropriate if that reaction cannot be isolated from the others, thus hindering the determination of its enthalpy change with a calorimeter. However, if the temperature change of the equilibrium constant of the reaction can be obtained (and it often can), the second law method affords the required data. Another frequent situation, easier to handle by a second law than a first law method, is that of a low-yield reaction. 'Batch' calorimetry results are always more reliable for high-yield (near 100%) reactions. For a low-yield reaction, the characterization of the final state (nature and amount of the species present) is not always straightforward and may lead to a significant error in the reaction enthalpy. A simple rule, which results from equation 2.54 and how K is related to the reaction yield (see the discussion after reaction 2.56), is that most first law methods are better suited to probe exergonic reactions ( /Delta1 r G o T more negative than ca. -12kJmol -1 ), whereas second law methods can be used when /Delta1 r G o T is closer to zero.A final advantage of second law methods is that they do not demand rather specific (thermochemical) instrumentation. Apart from temperature control and measurement devices, the determination of an equilibrium constant generally involves analytical equipment found in a chemical laboratory.

The previous comparison between first and second law methods may give the false impression that the latter should always be preferred. Second law methods can be unreliable, even if a sophisticated equation is used to fit the experimental data.The problem lies in the evaluation of the equilibrium constant, which must be defined in terms of the activities of reactants and products [1].The activity concept

has been introduced to extend to 'real' situations the chemical thermodynamics formalism used to describe perfect gas mixtures and ideal solutions. For example, the chemical potential ( µ i ) of a solute i in an ideal solution can by expressed by equation 2.61, where µ o i is the standard chemical potential of i at the solution temperature (i.e., the chemical potential for m i = 1 mol per kg of solvent), m i is the molality of the species in the solution, and m o = 1 mol kg -1 .

<!-- formula-not-decoded -->

The case of a real solution, shown by equation 2.62, is handled by introducing a dimensionless correction, called the activity coefficient ( γ i ). In the high dilution limit ( m i → 0), γ i = 1, and equation 2.62 reduces to 2.61. The activity of species i is simply a i = γ i m i / m o .

<!-- formula-not-decoded -->

Here µ ∗ i represents the chemical potential of solute i at unit molality and γ i = 1. The equilibrium constant of a reaction is defined in terms of the standard chemical potentials of reactants and products and thus can be expressed in terms of activities:

<!-- formula-not-decoded -->

As mentioned before, ν i are the stoichiometric coefficients of the reaction (positive for products and negative for reactants).

Equation 2.63 is valid for any homogeneous or heterogeneous reaction. The only difference is in the definition of activities. For a species in a perfect gasphase mixture a i = p i / p o , where p i is the partial pressure of species i and p o is the standard pressure (1 bar). For a real gas-phase mixture a i = f i / p o , where f i is the fugacity of i. The fugacity concept was developed for the same reason as the activity: to extend to real gases the formalism used to describe perfect gas mixtures. In the low total pressure limit ( p → 0 ) , f i = p i .

The previous summary of activities and their relation to equilibrium constants is not intended to replace lengthier discussions [1,18,25,51]. Y et it is important to emphasize some points that unfortunately are often forgotten in the chemical literature. One is that the equilibrium constants, defined by equation 2.63, are dimensionless quantities . The second is that most of the reported equilibrium constants are only approximations of the true quantities because they are calculated by assuming the ideal solution model and are defined in terms of concentrations instead of molalities or mole fractions. Consider, for example, the reaction in solution:

<!-- formula-not-decoded -->

The prevalent method of obtaining a value of the equilibrium constant is by measuring the molar equilibrium concentrations (in mol dm -3 ) and using equation 2.65. This equilibrium constant is designated by Kc :

<!-- formula-not-decoded -->

It is easily shown that equation 2.65 is a fair approximation only if the ideal solution model is valid and A, B, and C are in very low concentrations. By accepting unity activity coefficients for all the species, equation 2.63 leads one to the equilibrium constant calculated from the molalities ( Km ):

<!-- formula-not-decoded -->

For very dilute solutions the solute concentrations ( c i ) are proportional to molalities: m i = c i /ρ , ρ being the density of the solution [18]. Therefore

<!-- formula-not-decoded -->

Because m o = 1 mol kg -1 , Kc is numerically equal to Km divided by the density of the solution. If the solvent is water, then ρ ≈ 1 kg dm -3 and Kc ≈ Km . For other solvents, however, the difference between the two equilibrium constants is larger.

Equation 2.67 indicates that the standard enthalpy and entropy of reaction 2.64 derived from Kc data may be close to the values obtained with molality equilibrium constants. Because /Delta1 r H o T is calculated from the slope of ln Kc versus 1/ T , it will be similar to the value derived with Km data provided that the density of the solution remains approximately constant in the experimental temperature range. On the other hand, the 'error' in /Delta1 r S o T calculated with Kc data can be roughly estimated as R ln ρ (from equations 2.57 and 2.67). In the case of water, this is about zero; for most solvents, which have ρ in the range of 0.7-2 kg dm -3 , the corrections are smaller (from -3 to 6 J K -1 mol -1 ) than the usual experimental uncertainties associated with the statistical analysis of the data.

The general relationship between Kc and Km is given by equation 2.68. Note that Kc = Km when the sum of the stoichiometric coefficients is zero.

Although there is no theoretical reason to consider the second law method a less reliable way of evaluating thermochemical values in solution compared to the first law method, in practice we are compelled to make a number of assumptions that may lead to significant errors. Unfortunately, we are seldom aware of the uncertainties caused by accepting the ideal solution model. Because activity coefficient data are extremely scarce, nearly all literature studies reporting applications of the second law method use Kc or, less frequently, Km , even if the concentration or the nature of the substances involved makes it inadvisable to do so. Bearing all this in mind, it is not surprising to find examples that show significant discrepancies between solution data obtained by the first and the second law methods [52].

<!-- formula-not-decoded -->

The application of the second law method to gas-phase reactions is less problematic than for reactions in solution. As described, a i = p i / p o can be used when the perfect gas model is valid (at low enough pressures). For higher pressures, the real gas model implies a i = f i / p o . Either one of these relationships can be

used to derive the equilibrium constant at several temperatures and obtain the standard reaction enthalpy and entropy. The difficulty in the case of real mixtures is knowing the fugacities of reactants and products. Fugacities are usually not tabulated, and their accurate calculation at a given temperature requires information on how the molar volume of each species in the mixture varies with the total pressure [18]. These data are seldom available, and their measurement represents a considerable experimental effort. Fortunately, in cases where the pressure is not too high (lower than about 10 bar), we can apply Lewis and Randall' s rule, which states that the fugacity of the species i in the mixture ( f i) is equal to the product of its mole fraction ( y i), and the fugacity of the pure substance ( f ′ i ) at the same temperature and total pressure as the mixture [4,18]:

<!-- formula-not-decoded -->

The fugacity of the pure substance can be derived by means of equation 2.70,

<!-- formula-not-decoded -->

where Z = pV / RT is the compressibility factor and p ′ is the total pressure of the mixture. The integral in this equation can be numerically evaluated with experimental ( p , V , T ) data or, more commonly, calculated by using virial equation 2.18.

## 2.10 THE GIBBS ENERGY: THIRD LAW METHOD

Besides the second law method, there is another way of extracting reaction enthalpies from gas-phase equilibrium constants. This alternative involves the determination of a single value of an equilibrium constant at a given temperature and the calculation of the reaction entropy at the same temperature. From equations 2.54 and 2.55, we obtain

<!-- formula-not-decoded -->

Once again we use subscript T to indicate that the reaction enthalpy and entropy may not refer to 298.15 K. The subscript p in the equilibrium constant indicates that we are accepting the perfect gas model and therefore Kp is defined in terms of partial pressures, not fugacities.

Statistical mechanics affords an accurate method to evaluate /Delta1 r S o T , provided that the necessary structural and spectroscopic parameters (moments of inertia, vibrational frequencies, electronic levels, and degeneracies) are known [1]. As this computation implicitly assumes that the entropy of a perfect crystal is zero at the absolute zero, and this is one of the statements of the third law of thermodynamics, the procedure is called the third law method .

Although equation 2.71 can be directly applied to derive a reaction enthalpy at the temperature T , and the correction to 298.15 K (or to any other temperature)

can be made by the usual method (see equations 2.10 or 2.14), it is convenient to summarize these steps in a final equation:

<!-- formula-not-decoded -->

where /Delta1 r Φ o T (sometimes called the standard Giauque function of the reaction), is given by

<!-- formula-not-decoded -->

H o 298 is the integrated heat capacity of species i (see equation 2.14) at 298.15 K, and G o T ( = H o T -TS o T ) is the corresponding Gibbs energy at temperature T .

The advantage of equation 2.72, compared with 2.71, is that Φ o T = ( G o T -H o 298 )/ T is tabulated (or readily calculated) for many common gaseous substances as a function of temperature, thus saving some computational work [53,54]. The only point to consider is that some of those compilations actually list the data for another function, Φ o 0 = ( G o T -H o 0 )/ T , which is useful to derive the standard reaction enthalpy at the absolute zero:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

the relationship between Φ o T and Φ o 0 being

<!-- formula-not-decoded -->

Therefore, Φ o T is easily derived from Φ o 0 data.

It is generally agreed that the third law method yields more accurate values than the second law method because it does not require any assumption regarding the temperature variation of the reaction enthalpy and entropy. The usual procedure to obtain third law data is to calculate the reaction enthalpy and entropy for each experimental value of Kp and take the average of all the values derived for a given temperature.

where

## The Kinetic Background

Kinetic studies in solution and in the gas phase have been playing an increasingly important role as a source of thermochemical data (see examples in chapter 15). Here we discuss how to relate thermochemical and kinetic information by approaching the subject as we did in the previous chapter: by highlighting important practical issues and reducing to a minimum the description of theoretical models. In other words, the present chapter also relies on the material usually covered at the undergraduate level [1]. Further details can be found in more specialized books [55-59].

## 3.1 REACTIONS IN THE GAS PHASE

The transition-state theory (TST) provides the framework to derive accurate relationships between kinetic and thermochemical parameters. Consider the common case of the gas-phase bimolecular reaction 3.1, where the transient activated complex C ‡ is considered to be in equilibrium with the reactants and the products:

<!-- formula-not-decoded -->

From the rate law of this reaction in the forward direction, defined in terms of concentrations,

<!-- formula-not-decoded -->

and the TST, it is possible to derive equation 3.3, which assumes the perfect gas model, and relates the rate constant k 1 with the standard enthalpy of activation (/Delta1 ‡ H o 1 ) and the standard entropy of activation (/Delta1 ‡ S o 1 ) of the forward reaction at a given temperature ( T ):

<!-- formula-not-decoded -->

Here k B and h are the Boltzmann and the Planck constants, respectively, and p o is the standard pressure (1 bar). Now consider reaction 3.1 in the reverse direction. The rate law

<!-- formula-not-decoded -->

and the TST lead to

<!-- formula-not-decoded -->

At equilibrium, ν 1 = ν -1 and, from 3.2 and 3.4,

<!-- formula-not-decoded -->

That is, the ratio between the forward and the reverse rate constants is equal to the equilibrium constant Kc . It can be easily shown that the perfect gas model implies

<!-- formula-not-decoded -->

where /Delta1ν is the difference between the stoichiometric coefficients of products and reactants. In the case of reaction 3.1, /Delta1ν = 0 and Kc = Kp . Therefore, the 'thermochemical kinetics' relationships can be found by combining equations 2.57, 3.3, and 3.5 (see figure 3.1):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We now consider a unimolecular reaction and its rate law in the forward direction:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In this case, the TST gives

<!-- formula-not-decoded -->

Figure 3.1 A reaction profile, showing how the thermodynamic and kinetic quantities are related. X can be any state function (enthalpy, Gibbs energy, entropy, volume, etc.).

<!-- image -->

For the reverse reaction, which involves the equilibrium between the species D, E, and the activated complex, equation 3.5 remains valid. Consequently,

<!-- formula-not-decoded -->

and by comparing equation 3.14 with equation 2.57, the relationships 3.8 and 3.9 are again obtained.

In summary, the foregoing examples show that for a given elementary reaction, the standard reaction enthalpy is derived from the difference between the enthalpies of activation of the forward and the reverse process. An identical conclusion is drawn for the entropic terms. If, in the cases of reactions 3.1 and 3.10, the rate constants k 1 and k -1 are known as a function of temperature, those kinetic parameters may be determined by plotting ln ( k / T 2 ) or ln ( k / T ) versus 1 / T ( k = k 1 or k -1 ) . This analysis is known as an Eyring plot, and the resulting activation enthalpies and entropies refer to the mean temperature of the experimental range.

When the temperature ranges of k 1 and k -1 data are not approximately coincident, it may be necessary to correct the activation parameters to the same mean temperature by using heat capacity data. This correction can be estimated by statistical mechanics, after finding (e.g., by quantum chemistry methods) a structure for the activated complex.

An alternative and more common procedure for deriving energetic data from rate constants involves an Arrhenius plot . It relies on the empirical Arrhenius equation,

<!-- formula-not-decoded -->

where A is the pre-exponential (or frequency) factor and E a is the Arrhenius activation energy. Equation 3.15 assumes that both A and E a are constant in the experimental temperature range for which k data are available. Although this is a valid assumption for many reactions, equation 3.16 is a more general relationship for defining the activation energy because it does not imply Arrhenius behavior of the reaction kinetics, or temperature invariance of A and E a [1]:

<!-- formula-not-decoded -->

Equation 3.16 can be applied to equations 3.3 and 3.5 to relate the forward and reverse standard activation enthalpies of reaction 3.1 with theArrhenius activation energies at a given temperature, yielding equations 3.17 and 3.18, respectively.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Note that these equations do not depend on any assumption regarding the temperature dependence of the activation enthalpy and entropy. In fact, when calculating each d ln k / dT value, the temperature dependences of /Delta1 ‡ H o (/Delta1 ‡ C o p ) and /Delta1 ‡ S o (/Delta1 ‡ C o p / T ) cancel. Hence, the reaction enthalpy at the temperature T is given by

<!-- formula-not-decoded -->

The same exercise applied to reaction 3.10, which is unimolecular in the forward direction and bimolecular in the reverse direction, leads to

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The reaction enthalpies in equations 3.19 and 3.22 refer to the same temperature as E a,1 and E a, -1. If the activation energies are obtained by simple Arrhenius plots (equation 3.15), then T in these equations will be the mean value of the experimental temperature range.As stated, this may not be coincident for E a,1 and E a, -1, and a heat capacity correction will be needed to refer /Delta1 ‡ H o 1 and /Delta1 ‡ H o -1 to a single temperature.

It is also possible to apply a nonlinear fit to ln k versus 1/ T , which is known as a modified Arrhenius plot . For instance, one can use an equation such as

<!-- formula-not-decoded -->

where A , B , and C are adjustable parameters. In this case, according to the definition of E a (equation 3.16), the activation energy is obtained as a function of T :

<!-- formula-not-decoded -->

The modified Arrhenius method yields more accurate results for E a than the linear plot because it does not include the assumption that this parameter is constant with the temperature. Nevertheless, the linear plot is widely adopted because for many reactions, the variation of E a with T is small. Also, linear plots are more suitable than nonlinear plots to handle low-precision data. In either case, the procedure to derive the activation enthalpies and the reaction enthalpies is as described.

Once the activation enthalpies are known, the corresponding activation entropies can be easily obtained from the (simple or modified) Arrhenius plot by combining equations 3.15 or 3.23 with the appropriate TST equation (3.3, 3.5, 3.12). The reaction entropy at temperature T is then calculated with equation 3.9.

Before turning our attention to reaction kinetics in solution, a few general comments are appropriate.

First, the perfect gas model has been accepted throughout the discussion. It is possible (and simple) to work out the equations that refer to fugacities. Y et

the results could seldom be applied in practice due to lack of auxiliary data. In addition, most gas-phase studies of thermochemical kinetics involve pressure ranges for which the perfect gas assumption is reasonable.

The second comment is that we have chosen the most prevalent elementary processes (unimolecular and bimolecular reactions) to illustrate how to relate thermochemical with kinetic data. Different molecularities will naturally change many equations just presented, but the basic relations 3.8 and 3.9 will not be affected.

The third and final note is concerned with a rather common experimental situation; for a large number of reactions, it is not simple to determine both /Delta1 ‡ H o 1 and /Delta1 ‡ H o -1 . In these cases, it is sometimes appropriate to make some sort of assumption regarding /Delta1 ‡ H o -1 . For instance, when D and E in reaction 3.10 are radicals whose recombination is diffusion-controlled, it is expected that /Delta1 ‡ H o -1 ≈ 0. This hypothesis has, however, some subtleties that are important to mention. What is really assumed in these cases is that the internal energy of activation is zero at the absolute zero, that is, /Delta1 ‡ U o -1 ( 0 ) = 0 [60]. Starting with equation 3.20, we can write the following series of equalities, where /Delta1 ‡ n = 1 -m , m being the molecularity of the forward reaction ( m = 1 and /Delta1 ‡ n = 0 in the case of reaction 3.10):

<!-- formula-not-decoded -->

All these quantities refer to the temperature T , but they can be adjusted to any other temperature.Thus, /Delta1 ‡ U o 1 canbeexpressedintermsof /Delta1 ‡ U o 1 ( 0 ) byusingtheaverage heat capacity difference between the activated complex and the reactant A, 〈 /Delta1 ‡ C o V ,1 〉 , in the temperature range 0 K to T :

<!-- formula-not-decoded -->

On the other hand, /Delta1 ‡ U o 1 ( 0 ) can be related with the same parameter for the reverse reaction and with the standard reaction internal energy at 0 K:

<!-- formula-not-decoded -->

When this relationship is introduced in equation 3.26, we obtain

<!-- formula-not-decoded -->

/Delta1 r U o 0 can be related to /Delta1 r U o T , the reaction internal energy at the temperature T , by using the average reaction heat capacity, 〈 /Delta1 r C o V 〉 . This, in turn, can be given as the difference:

<!-- formula-not-decoded -->

Introducing these relationships in equation 3.28, and recalling that /Delta1 ‡ U o -1 ( 0 ) = 0, we obtain, for reaction 3.10,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In conclusion, under the hypothesis that the reaction has no barrier in excess of its endoergicity, /Delta1 ‡ U o -1 ( 0 ) = 0, the enthalpy of reaction 3.10 is given by the Arrhenius activation energy for the forward reaction minus a heat capacity term. Thistermcanbeestimatedbyusingstatisticalmechanics,providedthatastructure for the activated complex is available. It is often found that T 〈 /Delta1 ‡ C o V , -1 〉 is fairly small, ca. -1kJmol -1 at 298.15 K [60], and therefore, the alternative assumption of E a,1 ≈ /Delta1 r H o T is commonly accepted if T is not too high. Finally, note that either E a,1 ≈ /Delta1 r H o T or /Delta1 ‡ U o -1 ( 0 ) = 0 are not equivalent (see equation 3.22) to another current (but probably less reliable) postulate, E a, -1 = 0.

## 3.2 REACTIONS IN SOLUTION

Thermochemical quantities can also be related to kinetic data in solution, and the bridges are still provided by the TST. We consider the same types of elementary reactions addressed in the previous section, namely,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Let us start with the bimolecular reaction 3.32. Its rate law has the same form as for the analogous gas-phase reaction and so has the TST equation, which combines the rate constant with the equilibrium constant between the reactants and the activated complex:

<!-- formula-not-decoded -->

The differences between the gas-phase and solution algorithms appear from this point on. To derive equation 3.3, the perfect gas mixture was assumed, and K ‡ related to an equilibrium constant given in terms of the partial pressures of the reactants and the activated complex [1]. This Kp is then easily connected with /Delta1 ‡ H o 1 and /Delta1 ‡ S o 1 . As stated, the perfect gas model is a good assumption for handling the results of the large majority of gas-phase kinetic experiments.

In solution reactions, K ‡ is also defined in terms of concentrations ofA, B, and C ‡ , which means, of course, that the ideal solution model is adopted, no matter the nature or the concentrations of the solutes and the nature of the solvent. There is no way of assessing the validity of this assumption besides chemical intuition. Even if the activity coefficients could be determined for the reactants, we would still have to estimate the activity coefficient for the activated complex, which is impossible at present. Another, less serious problem is that the appropriate quantity to be related with the activation parameters should be the equilibrium constant defined in terms of the molalities of A, B, and C ‡ . As discussed after equation 2.67, /Delta1 ‡ S o 1 will be affected by this correction more than /Delta1 ‡ H o 1 (see also the following discussion).

and

In conclusion, the TST yields the following equation for the rate constant of reaction 3.32 in the forward direction:

<!-- formula-not-decoded -->

The procedure then follows exactly what has been described for the gas phase. An Eyring plot, that is, ln ( k 1 / T ) versus 1 / T , affords /Delta1 ‡ H o 1 and /Delta1 ‡ S o 1 . On the other hand, for reaction 3.32 in the reverse direction, an equation identical to 3.35 is obtained, allowing us to derive /Delta1 ‡ H o -1 and /Delta1 ‡ S o -1 . The activation parameters refer to the mean temperatures of the experimental ranges. If these do not coincide, then, as mentioned for the gas-phase process, it is necessary to make a heat capacity correction to refer them both to the same temperature. Fortunately, although this correction is difficult (or even impossible) to apply accurately to species in solution, it is likely to be rather small in most cases. The experimental temperature ranges cannot vary as dramatically as in the gas phase because in solution, they are limited by the freezing and boiling temperatures of the solvents. Hence, the reaction enthalpy and entropy can be calculated with the general relationships 3.8 and 3.9 (see also figure 3.1), by using an average of the temperatures assigned to the forward and the reverse activation parameters. Finally, because reaction 3.32 is bimolecular in both directions, the error caused by the use of concentrations (instead of molalities) to define the equilibrium constant K ‡ , cancels out when equations 3.8 and 3.9 are applied.

The procedure and most of these comments apply also to the unimolecular reaction 3.33. There is only one difference: The TST equation for relating k 1 with the equilibrium between the reactant and the activated complex,

<!-- formula-not-decoded -->

indicates that in this case, K ‡ has the same value on the concentration and the molality scales, implying that no correction is needed.Y et as the reverse reaction is bimolecular, the error is now transferred to the final thermochemical quantities, obtained by equations 3.8 and 3.9.

We now deal with the Arrhenius plots. It is easy to show that when equation 3.16 is combined with equation 3.35, which is valid for the unimolecular and the bimolecular cases, we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The method is thus identical to the one described for gas-phase reactions. Thus, the activation energies of the forward and reverse reactions can be obtained at a temperature T from either simple or modified Arrhenius plots, and their difference is equal to the reaction enthalpy at the same temperature. Note, however, that equation 3.39 is valid for any elementary reaction in solution, whatever the molecularity, whereas in the case of gas-phase reactions, the equivalent expression depends on the reaction molecularity (see equations 3.19 and 3.22).

At the end of section 3.1 we addressed a common circumstance in gas-phase thermochemical kinetics studies. For many reactions, there is not enough experimental information to determine /Delta1 ‡ H o -1 , and a negligible barrier for the product recombination reaction is often assumed. The same ideas can be applied for reactions in solution: When D and E are radicals, it is frequently accepted that the reverse of reaction 3.33 is diffusion controlled and that /Delta1 ‡ H o -1 has a value of ∼ 8 kJ mol -1 .

Solution chemistry is considerably more complex than gas-phase chemistry. The solvent often plays a crucial role in determining molecular reactivity, so it is not surprising that the reaction mechanism and energetics are also affected. For example, when we represent a unimolecular decomposition in solution as reaction 3.33, we may be ignoring at least one important step: the formation of a cage pair [D-E], a pair of radicals D and E formed by cleavage of a chemical bond in the reactant A that are trapped inside a cavity in the solvent for some period of time. The species D and E in the cage pair can either move away from each other as they escape from that cavity to yield the reaction products or recombine to regenerate A. The relative efficiency of these two competitive processes depends on the solvent properties, in particular the viscosity.

The concept of cage effects in reaction kinetics is over 60 years old, but the attempts made to apply it to thermochemical kinetics are much more recent. Here, we will briefly address the model reported by Koenig, Hay, and Finke [61]. According to these authors, a better representation of reaction 3.33 is

<!-- formula-not-decoded -->

where C ′ ‡ is a second transition state in the reaction profile (see figure 3.2). The main conclusion drawn from this model is that reaction 3.33 is no longer an elementary process. Hence, the reaction enthalpy is not given simply by the difference /Delta1 ‡ H o 1 -/Delta1 ‡ H o -1 , but rather by

<!-- formula-not-decoded -->

Figure 3.2 An enthalpy profile for a unimolecular reaction in solution, involving the formation of a radical pair inside a solvent cage. Adapted from [61].

<!-- image -->

All these quantities are shown in figure 3.2, where /Delta1 ‡ H o c is the the activation enthalpy for the cage radical pair recombination and /Delta1 ‡ H o d is the activation enthalpy for diffusive cage escape.

The practical application of the model is not simple, for we must relate the observed (net) activation enthalpy with the elementary quantities in equation 3.41 and these with the reaction enthalpy. However, at the very least, it stresses that only a judicious use of experimental kinetic data in solution will afford reliable thermochemical information.

A detailed analysis of Koenig, Hay, and Finke' s model is outside the scope of this book. Only one of its main conclusions is quoted here. If, for a given solvent, F is the recombination efficiency of D and E in the cage ( 0 ≤ F ≤ 1 ) , then

<!-- formula-not-decoded -->

where /Delta1 ‡ H o obs is the experimental activation enthalpy (for practical purposes, the same as our /Delta1 ‡ H o 1 in the concerted mechanism). Because the second term in equation 3.42 is proportional to F , and this parameter is expected to increase with the solvent viscosity, we should not expect a constant 'correction' for all solvents ( ∼ 8 kJ mol -1 ; see foregoing discussion).

## Gas-Phase Ion Energetics

The experimental methods designed to investigate the energetics of gas-phase ions have been another important source of thermochemical data, particularly throughout the past two or three decades [9,10]. In this chapter, we discuss the main quantities that are measured experimentally and lead to reaction enthalpy values.

## 4.1 IONIZATION ENERGY AND ELECTRON AFFINITY

The adiabatic ionization energy of any moleculeAB (mono-, di-, or polyatomic), represented by E i (AB), is the minimum energy required to remove an electron from the isolated molecule at 0 K:

<!-- formula-not-decoded -->

The proviso T = 0 signifies that AB is in its electronic, vibrational, and rotational ground states and has no translational energy. The word isolated indicates the perfect gas model. The 'minimum energy' condition ensures that AB + is also in its electronic, vibrational, and rotational ground states and the translational energies of AB + and e -are both zero; it also indicates that the products in reaction 4.1 do not interact, that is, they also conform with the perfect gas model.

In short, the adiabatic ionization energy is the standard internal energy or the standard enthalpy of reaction 4.1, at 0 K:

<!-- formula-not-decoded -->

Suppose we wish to relate E i(AB) with the standard enthalpies of formation of the species involved at 298.15 K. First we have to correct the reaction enthalpy from T = 0 to T = 298.15 K, for example, by using the integrated heat capacities (see equation 2.14) of reactants and products:

<!-- formula-not-decoded -->

Let us designate the difference ( H o 298 -H o 0 ) AB + -( H o 298 -H o 0 ) AB by /Delta1 and ( H o 298 -H o 0 ) e -by X . We can write:

<!-- formula-not-decoded -->

To apply this equation to calculate the difference between the standard enthalpies of formation of AB and AB + , we need to know the values of /Delta1 f H o ( e -, g ) , /Delta1 , and X . The heat capacities of AB and AB + are easily evaluated from statistical mechanics calculations, provided that their structures and vibrational frequencies are available. Usually, /Delta1 ≈ 0. However, with regard to /Delta1 f H o ( e -, g ) and X , the apparently simple task of assigning their values has been a source of controversy involving two scientific communities: the calorimetrists and the mass spectrometrists.

According to the calorimetrists' view, if we consider an electron as a particle that takes part in chemical reactions as any other chemical element, then it is fair to agree on /Delta1 f H o ( e -, g ) = 0, at any temperature. Moreover, because we regard the electron as a regular 'monoatomic' perfect gas, Boltzmann statistics or the equipartition principle [1] imply that C o p = C o V + R = 5 R / 2 (three translational degrees of freedom) or X = ( H o 298 -H o 0 ) e - = 298.15 × C o p = 6.197 kJ mol -1 . This value of X is the outcome of the so-called thermal electron convention or just electron convention , adopted in many textbooks and data compilations (see, e.g., references 22, 29, and 40 in appendix B). Equation 4.4 becomes:

<!-- formula-not-decoded -->

An alternative position, embraced by the mass spectrometry community (see, e.g., references 32, 33, and 37 in appendix B), known as the stationary electron convention or the ion convention , does not consider the electron as a chemical element. Therefore, its standard enthalpy of formation is not zero at all temperatures; at T = 0, /Delta1 f H o ( e -, g ) = 0, but at 298.15 K, /Delta1 f H o ( e -, g ) = X . When we apply these results in equation 4.4, we obtain

<!-- formula-not-decoded -->

The reasoning we have just used to derive equation 4.6 was taken from the introductory chapter of a popular data compilation [62]. However, as pointed out by the authors of this database, the true historical origin of the ion convention is less complicated: Although the mass spectrometrists were willing to accept that /Delta1 f H o ( e -, g ) = 0 at all temperatures, they justly (see following discussion) felt uneasy about the value assigned to X . To avoid this uncertainty, they have postulated X = 0 and obtained equation 4.6.

In conclusion, /Delta1 f H o ( AB + , g ) calculated by the electron convention will be 6.197 kJ mol -1 higher (at 298.15 K) than the value derived by the ion convention. In practical terms, this indicates that we must be alert when using enthalpy of formation data from several sources because they may have been derived by accepting either one of those conventions.

A discussion of the electron and the ion conventions has been made by Bartmess [63], who centered the attention in the key issue of the dispute: the value of X . His main point was that because electrons are fermions, an electron gas

should be described by Fermi-Dirac rather than by Boltzmann statistics. We designate this new proposal, which leads to X = 3.145 kJ mol -1 , as electron FD convention .

All of the previous discussion applies, with minor changes, to the second important concept we wish to address: the adiabatic electron affinity , E ea . For any molecule AB (mono-, di-, or polyatomic), E ea (AB) is the minimum energy required to remove an electron from the isolated anion at 0 K. In other words, E ea (AB) is the standard enthalpy of reaction 4.7 at T = 0.

<!-- formula-not-decoded -->

This definition may appear somewhat counterintuitive, because the word affinity suggests that we should be referring to the reverse process.That is why E ea is often given as the negative of the enthalpy of reaction 4.8 at T = 0 [62]. The definitions are, of course, equivalent and ensure that in most cases, electron affinities will have positive values.

<!-- formula-not-decoded -->

By following the same steps as for the ionization energy, it is very simple to conclude that

<!-- formula-not-decoded -->

where /Delta1 ′ = ( H o 298 -H o 0 ) AB - -( H o 298 -H o 0 ) AB. The application of the three conventions just described implies that /Delta1 f H o ( AB -, g ) calculated by the ion convention (at 298.15 K) will now be 6.197 kJ mol -1 greater than the value calculated by the electron convention and 3.145 kJ mol -1 greater than the value obtained by the electron FD convention.

The situation depicted by figure 4.1, where the minima of the three curves occur at nearly identical values of r (the A-B bond length), indicates that the electrons removed from AB -and from AB belong essentially to nonbonding molecular orbitals. A different case is illustrated by figure 4.2, where the cation curve minimum is shifted toward higher values of r , indicating that the electron is removed from a bonding molecular orbital in AB. According to the Franck-Condon principle [1], the most probable transition in figure 4.2 corresponds to AB( v = 0) → AB + ( v = 2 ) , and this energy difference is called the vertical ionization energy . This quantity, an upper limit of the adiabatic ionization energy, is experimentally easier to determine than E ea . Consequently, many of the values tabulated as 'ionization energies' are in fact for the less thermodynamically important vertical ionization energies.

The potential energy curves of the species AB, AB + , and AB -are used in figure 4.1 to summarize the definitions of the adiabatic ionization energy and electron affinity of AB. Note that the arrows start and end at vibrational ground states (vibrational quantum number v = 0).

<!-- image -->

r

<!-- image -->

r

## 4.2 APPEARANCE ENERGY

Consider a di- or a polyatomic molecule AB in the gas phase, at T = 0. By means of an electron or a photon, this molecule can be ionized and excited to a state AB +∗ , which subsequently decomposes into the fragments A + and B:

<!-- formula-not-decoded -->

If A + and B are formed in their ground states and if these species and the electron have zero translational energies, then the standard enthalpy of reaction 4.10 at T = 0 is equal to the appearance energy of A + at T = 0, AE 0 ( A + / AB ) . It becomes obvious from this definition that when reporting a value for an appearance energy, it is essential to state the parent molecule (indicated by /AB). Otherwise, we cannot identify the remaining species in the net reaction 4.10.

Figure 4.1 Potential energy curves for the molecules AB, AB + , and AB -, showing the ionization energy and electron affinity of AB; r is the A-B bond length, and v represents the vibrational quantum number.

Figure 4.2 Potential energy curves for the molecules AB and AB + showing the vertical and the adiabatic ionization energies of AB. r is the A-B bond length, and v represents the vibrational quantum number.

The appearance energy (formerly known as appearance potential) is a widely usedconceptin threshold massspectrometryexperiments, which involve measuring the minimum energy required to cause a certain process. However, there are a number of theoretical and practical problems associated with the determination of reliable values of AE 0 ( A + / AB ) . In the following paragraphs we summarize the discussion of this subject made by the groups of Traeger for photoionization [64,65] and Holmes for electron impact [66].

The first question regards the temperatures assigned to the reactant and the products of reaction 4.10. The parent molecule AB will be at a given temperature T , but the products result from a unimolecular decomposition so their temperature, which we designate by T ∗ , is hard to define (e.g., the decomposition involves an unknown distribution of vibrational and rotational energy levels). Therefore, in practice, the experimental appearance energy, AE exp ( A + / AB ) or E thr , is not an isothermal process (see figure 4.3). On the other hand, as noted by Traeger and McLoughlin [64], we can identify the experimental appearance energy with an enthalpy change, /Delta1 r H ∗ , because at threshold the products are formed with zero translational energy, which implies that the expansion work is zero.

It can be shown that if AE exp ( A + / AB ) is obtained by linear extrapolation of the ionization efficiency curve [64], the products have only the translational energy required to conserve momentum, and the relationship between AE exp ( A + / AB ) (or /Delta1 r H ∗ ) and AE 0 ( A + / AB ) is

<!-- formula-not-decoded -->

where 〈 E i 〉 is the average rotational and vibrational energy of AB at temperature T , effective in dissociation. According to Traeger and McLoughlin [64], all the rotational and vibrational energy is effective in the decomposition. Hence,

Figure 4.3 Thermochemical cycle, showing how the experimental appearance energy of A + ( AE exp ) is related to the appearance energies at 0 K and temperature T . /Delta1 H ( 1 ) , /Delta1 H ( 2 ) , and T * are defined in the text. Adapted from [64].

<!-- image -->

〈 E i 〉 can be calculated from the rotational and vibrational heat capacities of AB, C o p ,rot ( AB ) and C o p ,vib ( AB ) :

<!-- formula-not-decoded -->

Now figure 4.3 shows that another relation between AE exp ( A + / AB ) and AE 0 ( A + / AB ) is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where and -/Delta1 H ( 2 ) is the enthalpy released by cooling the products from T ∗ to 0 K. By comparing equations 4.11 and 4.12 with 4.13 and 4.14, we conclude that

<!-- formula-not-decoded -->

It is now simple to calculate the appearance energy at any temperature T :

<!-- formula-not-decoded -->

Finally, the standard enthalpy of formation of A + at 298.15 K is given by

<!-- formula-not-decoded -->

where /Delta1 f H o ( e -, g ) = 0 and X = ( H o 298 -H o 0 ) e -. Recall that the final value of /Delta1 f H o ( A + , g ) depends on the conventions described in section 4.1: According to the electron convention, the ion convention, and the electron FD convention, X 1 1

takes the values 6.197 kJ mol -, 0, and 3.145 kJ mol -, respectively.

The use of equation 4.17 to calculate the standard enthalpy of formation of A + raised some controversy in the mass spectrometry community. Holmes [66] pointed out that in electron impact experiments (i.e., when reaction 4.10 is

induced by an electron) an accurate linear extrapolation of the ionization efficiency curve is usually impossible due to the energy spread of the electron beam. This questions the validity of equation 4.11 for electron impact results. On the other hand, as also noted by Holmes, it is doubtful that 'all or even a major fraction' of the internal energy of a polyatomic parent molecule is effective for dissociation. In other words, 〈 E i 〉 may be smaller than given by equation 4.12, and the term 2.5 RT (equation 4.16) may actually represent a lower limit of the true correction.

The determination of accurate AE 0 ( A + / AB ) or /Delta1 f H o ( A + , g ) data is also complicatedbyotherproblems.Oneofthemisrelatedtotherateofdecomposition of the ion AB + and how this rate varies with the internal energy of the ion. Suppose that when the energy matches the true (threshold) appearance energy, the decomposition is too slow for this ion to be observed in the mass spectrometer. To detect A + , the energy of AB + has to be increased by raising the energy of the photon or the electron beam. Therefore, the measured AE exp ( A + / AB ) will be an upper limit of the true appearance energy (see figure 4.4). The difference between the two values, appropriately called kinetic shift ( E kin), is more significant when the decomposition rate is not strongly dependent on the energy of AB + . In this case, the detection of A + will require a larger excess energy than when the rate has a steep variation with the internal energy of AB + .

Asecond likely error source in the experimental determination of the appearance energy has also a kinetic origin. As shown in figure 4.4, recombination of the products A + and B may involve an activation barrier ( E rec). Therefore, even if E kin = 0, when E rec is not negligible the measured appearance energy will be an upper limit of the true (thermodynamic) value.

In summary, both the kinetic shift and the recombination barrier lead to thermodynamic values of the appearance energy that are too large and to upper limits of /Delta1 f H o ( A + , g ) . We now illustrate the procedures and conventions just described

<!-- image -->

Reaction coordinate

Figure 4.4 An energy profile for the unimolecular decomposition of AB + , showing a reverse activation barrier ( E rec ) and a kinetic shift ( E kin ) . Adapted from [65].

to calculate the standard enthalpies of formation of the ethyl cation and the ethyl radical.

The appearance energy of C2H + 5 has been measured by many groups using a variety of precursors and experimental techniques [67]. One of the values obtained for AE exp ( C2H + 5 / C2 H5Br ) , 1067.1 ± 1.0 kJ mol -1 ( 11.06 ± 0.01eV ) , was reported by Traeger and McLoughlin [64] and refers to reaction 4.18:

<!-- formula-not-decoded -->

Assuming that the parent ethyl bromide sample was at a temperature of 298.15 K, we can apply equation 4.17 to evaluate the standard enthalpy of formation of the ethyl cation:

<!-- formula-not-decoded -->

Using the relevant auxiliary data, namely, /Delta1 f H o ( C2H5Br, g ) = -61.9 ± 1.6 kJ mol -1 [ 15 ] , /Delta1 f H o ( Br, g ) = -111.87 ± 0.12 kJ mol -1 [ 16 ] , ( H o 298 -H o 0 ) C2H + 5 = 11.3 kJ mol -1 [65], and ( H o 298 -H o 0 ) Br = 6.197 kJ mol -1 [17], we are led to the three values of /Delta1 f H o ( C2H + 5 , g ) shown in table 4.1, which differ according to the convention accepted for X = ( H o 298 -H o 0 ) e -.

The bridge to relate /Delta1 f H o ( C2H + 5 , g ) with /Delta1 f H o ( C2H5, g ) is provided by equation 4.4, which can be rewritten as

<!-- formula-not-decoded -->

This equation requires the adiabatic ionization energy of the ethyl radical, the enthalpy correction /Delta1 , and again, the value of X . E i ( C2H5 ) = 783.2 ± 0.8 kJ mol -1 ( 8.117 ± 0.008 eV ) was selected from the NIST Chemistry WebBook [67] and /Delta1 = ( H o 298 -H o 0 ) C2H + 5 -( H o 298 -H o 0 ) C2H5 wastakenas11.3 -13.0 = -1.7 kJ mol -1 [65].

When each one of the three results for the difference /Delta1 f H o ( C2H + 5 , g ) -/Delta1 f H o ( C2H5, g ) , displayed in table 4.1, is subtracted from the corresponding /Delta1 f H o ( C2H + 5 , g ) , we are led to same value for /Delta1 f H o ( C2H5, g ) . In other words,

Table 4.1 The standard enthalpy of formation of C 2 H + 5 and C 2 H 5 according to the different conventions ( T = 298.15 K). Data in kJ mol -1 .

| Convention   | /Delta1 f H o ( C 2 H + 5 , g )   | /Delta1 f H o ( C 2 H + 5 , g ) - /Delta1 f H o ( C 2 H 5 , g )   | /Delta1 f H o ( C 2 H 5 , g )   |
|--------------|-----------------------------------|-------------------------------------------------------------------|---------------------------------|
| Electron     | 910.8 ± 1.9                       | 787.7 ± 0.8                                                       | 123.1 ± 2.1                     |
| Ion          | 904.6 ± 1.9                       | 781.5 ± 0.8                                                       | 123.1 ± 2.1                     |
| ElectronFD   | 907.7 ± 1.9                       | 784.6 ± 0.8                                                       | 123.1 ± 2.1                     |

the enthalpy of formation of the neutral species (the ethyl radical), calculated from appearance energy and ionization energy data, is independent of the convention. This stems from the cancellation of X when equations 4.19 and 4.20 are combined.

As noted after equation 4.17, the procedure to evaluate standard enthalpies of formation from appearance energies is somewhat controversial. When the threshold energies are determined from electron impact experiments, it has been argued that the correction terms ( H o 298 -H o 0 ) A + + ( H o 298 -H o 0 ) B -6.197 in equation 4.17 should not be included in the calculation [66]. Consider, for instance, reactions 4.21, and 4.22 where the ion CH2OH + was produced from the decomposition of 1-propanol or methanol.

<!-- formula-not-decoded -->

The experimental appearance energies of CH2OH + , 1080.6 kJ mol -1 (11.20 eV) and 1127.9 kJ mol -1 (11.69 eV), respectively, were measured in both cases by using a monoenergetic electron beam [68,69]. Because they have been directly identified with the enthalpies of reactions 4.21 and 4.22 at 298.15 K, we can write

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The second equation, together with /Delta1 f H o ( H, g ) = 218.0 kJ mol -1 [ 16 ] , /Delta1 f H o ( CH3OH,g ) = -201.5 ± 0.2 kJ mol -1 [15], and X = 0 (the ion convention), yields /Delta1 f H o ( CH2OH + , g ) = 708.4 kJ mol -1 . When this result is introduced in equation 4.23, together with /Delta1 f H o ( C3H7OH,g ) = -255.1 ± 0.4 kJ mol -1 [15] and X = 0, we obtain /Delta1 f H o ( C2H5, g ) = 117.1 kJ mol -1 .

The value calculated from electron impact data is only 6 kJ mol -1 smaller than the one in table 4.1. Interestingly, when the correction terms ( H o 298 -H o 0 ) A + + ( H o 298 -H o 0 ) B -6.197 are included in equations 4.23 and 4.24, the net correction to /Delta1 f H o ( C2H5, g ) adds up to ( H o 298 -H o 0 ) C2H5 -( H o 298 -H o 0 ) H = 13.0 -6.2 = 6.8 kJ mol -1 , bringing the two values to a close match. Nevertheless, according to Holmes, there are many other examples showing that electron impact enthalpies of formation would be too low by as much as 21 kJ mol -1 if those corrections were applied [66].

## 4.3 PROTON AFFINITY, BASICITY, AND ACIDITY

In addition to the concepts reviewed in the last two sections (appearance energy, ionization energy, and electron affinity), three others are relevant in gas-phase molecular energetics, namely, proton affinity , gas-phase basicity , and gas-phase acidity .

The proton affinity of any species A in the gas phase, abbreviated by PA (A), is defined as the negative of the standard enthalpy of reaction 4.25 at 298.15 K. The minus sign ensures that proton affinities always have positive values.

<!-- formula-not-decoded -->

The gas-phase basicity of A, which we represent by GB (A), is the standard Gibbs energy of reaction 4.25. It is also usually defined at T = 298.15 K and it is related to PA (A) by equation 4.26.

<!-- formula-not-decoded -->

Finally, the gas-phase acidity of the molecule AH, represented by /Delta1 acid G o ( AH ) , is the standard Gibbs energy of reaction 4.27 (usually at 298.15 K).

<!-- formula-not-decoded -->

Note that the standard enthalpy of this reaction, /Delta1 acid H o ( AH ) , is equal to the proton affinity of the anion, PA (A -). As shown in figure 4.5, this quantity can be related to PA (A) by using the adiabatic ionization energy of AH and the adiabatic electron affinity of A. The result is also expressed by equation 4.28 (derived from equations 4.4 and 4.9), where /Delta1 = ( H o 298 -H o 0 ) AH + -( H o 298 -H o 0 ) AH and /Delta1 ′ = ( H o 298 -H o 0 ) A - -( H o 298 -H o 0 ) A.Thesethermalcorrections are often smaller than the usual experimental uncertainties of proton affinity data (ca. 4 kJ mol -1 ) .

<!-- formula-not-decoded -->

It is important to stress that the energetics of reactions 4.25 and 4.27 are usually not amenable to direct experimental investigation. Indeed, proton affinities, gas-phase basicities, and gas-phase acidities reported in the literature were not

Figure 4.5 Thermochemical cycle ( T = 298.15 K), showing how the proton affinities of A and A -are related. E i ( AH ) is the adiabatic ionization energy of AH, and E ea ( A ) is the adiabatic electron affinity of A. /Delta1 , /Delta1 ′ , and X are thermal corrections (see text).

<!-- image -->

obtained from measurements performed on those reactions. For instance, the proton affinity of a molecule A is derived in practice from the energetics of a reaction such as

<!-- formula-not-decoded -->

The standard enthalpy of this reaction is equal to the difference PA (A) -PA (B). Thus, the determination of PA (A) requires PA (B). The proton affinity of B will rely, in turn, on the proton affinity of some other molecule and so on. A scale of relative values of proton affinities is thus built. To derive absolute data, a reliable anchor must be found. The one most frequently used is the proton affinity of ammonia, PA (NH3 ) , which is now accepted to be 853.6 kJ mol -1 [67]. This is in excellent agreement with the result of a benchmark calculation by Martin and Lee, PA (NH3 ) = 853.1 ± 1.3 kJ mol -1 [70].

When comparing literature data for the quantities addressed in this section, it is therefore essential to check if those data are consistent , that is, if they are based on the same value for the anchor. On the other hand, note that proton affinity, basicity, and acidity values do not depend on whether we follow the electron convention, the ion convention, or the electron FD convention. This is clearly evidenced by reactions 4.25 and 4.27, which do not involve the electron as a reactant or product species. However, it is also obvious that the values of the standard enthalpies of formation of AH + and A -, calculated from PA (A) and /Delta1 acid H o ( AB ) , respectively, will vary with the convention used to derive the standard enthalpy of formation of the proton.

## 5

## Bond Energies

Although standard enthalpies of formation provide information about the net stability of molecules and their transformations, they do not always indicate stability of individual bonds. This analysis normally involves parameters, loosely called 'bond energies,' that reflect the amount of energy required to cleave chemical bonds.

Bond energies are essential for understanding the nature of chemical bonds. They can be used to assess the results from quantum chemistry calculations (or from other, less sophisticated theoretical models) and thus support or oppose the descriptions of those bonds. Moreover, bond energy values also enable us to estimate the driving forces of chemical reactions by considering the strengths of all the bonds that are cleaved and formed. In fact, there are many reactions for which the standard enthalpies of formation of all reactants and products are not available (and cannot be easily estimated) but whose energetics can be predicted from the appropriate bond energies.

In the previous chapters, we attempted to review all the important parameters in molecular energetics, but to avoid unnecessary distraction, we deliberately omitted bond energies from the discussion. The literature is plagued with a variety of concepts that fall into that designation but are not always synonymous. We can find names like bond strengths , bond enthalpies , bond energies , bond dissociation enthalpies , bond dissociation energies , bond disruption enthalpies , bond enthalpy terms , intrinsic bond energies , and symbols like D , D , 〈 D 〉 , E , BDE, and so on. The meaning of these concepts it not always obvious and, unfortunately, some are occasionally misused. Now we look into each one of them.

## 5.1 BOND DISSOCIATION ENTHALPIES AND ENERGIES

Consider a molecule AB, where A and B can be atoms or groups of atoms. The A-B bond dissociation enthalpy , represented by DH o T (A-B), is defined as the standard enthalpy of the gas-phase reaction where the only event is the cleavage of that bond at a given temperature:

<!-- formula-not-decoded -->

TheA-B bond dissociation energy , on the other hand, is the standard internal energy of reaction 5.1. It is abbreviated by DU o T (A-B) and its relation with DH o T (A-B) is given by

<!-- formula-not-decoded -->

As stated in section 2.2, the subscript T will be omitted whenever the temperature refers to 298.15 K. In this case,

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

There are numerous publications where the standard enthalpy of reaction 5.1 is called bond dissociation energy and abbreviated by BDE or by D (A-B). However, this designation (as well as the abbreviations) can be misleading, and we favor the nomenclature just indicated. It should also be recalled (see section 2.2) that the International Union of Pure and Applied Chemistry (IUPAC) recommends D 0 for the dissociation energy at T = 0 (therefore, D 0 = DU o 0 = DH o 0 ) and D e for the hypothetical dissociation energy from the potential minimum [13].

Bearing in mind that a bond dissociation enthalpy is simply the standard enthalpy of a particular reaction, the relationship between two values of DH o T (A-B) at different temperatures is easily obtained as

<!-- formula-not-decoded -->

Note that at 298.15 K, DH o ( A -B ) &gt; DH o 0 (A-B), because the sum of the last three terms in equation 5.5 is positive. This is easily shown by using the equipartition principle [1]. Consider, for example, A = B = CH3. When the methyl radicals are produced (reaction 5.1), there is a net gain of three translational degrees of freedom and three rotational degrees of freedom and a net loss of six normal vibration modes. The upper limit of DH o (CH3 -CH3) DH o 0 (CH3 -CH3) can be found by recalling that at 298.15 K, translational and rotational degrees of freedom are fully excited (hence, the equipartition principle is valid) and by assuming that the vibrational degrees of freedom of C2H6 and CH3 are completely 'frozen' at the same temperature. Therefore, /Delta1 r C o V = 3 R / 2 + 3 R / 2 = 3 R , /Delta1 r C o p = /Delta1 r C o V + R /Delta1 r n = 4 R , and ( H o 298 -H o 0 ) CH3 + ( H o 298 -H o 0 ) CH3 -( H o 298 -H o 0 ) C2H6 = 4 RT = 9.9 kJ mol -1 . This theoretical upper limit is 1 kJ mol -1 higher than the correct value, DH o (CH3 -CH3) -DH o 0 (CH3 -CH3) = 8.9 kJ mol -1 [17]. The discrepancy, which can be accurately predicted by statistical mechanical calculations, is due to the contribution of the hindered internal rotation of the methyl groups to C o V of ethane and also to the fact that the lost vibrational modes have a nonnegligible contribution to /Delta1 r C o V at 298.15 K.

A similar analysis can be made to evaluate the upper limit of DH o (A-B) DH o 0 (A-B) for any other bond. This upper limit will vary according to the

Table 5.1 Upper limits of DH o (A-B) DH o 0 (A-B) for some molecules, estimated by the equipartition principle (EP), compared with the correct values [17]. Data in kJ mol -1 .

| Molecule   | DH o (A-B) - DH o 0 (A-B) EP upper limit   |   DH o (A-B) - DH o 0 (A-B) |
|------------|--------------------------------------------|-----------------------------|
| H-Br       | 1.5 RT = 3.72                              |                         3.7 |
| H-OH       | 2 RT = 4.96                                |                         5.1 |
| H-CH 3     | 2.5 RT = 6.20                              |                         6.6 |
| HO-OH      | 3 RT = 7.44                                |                         6.8 |
| OH-CH 3    | 3.5 RT = 8.68                              |                         7.8 |
| CH 3 -CH 3 | 4 RT = 9.92                                |                         8.9 |

structural characteristics of AB, A, and B (linear or nonlinear; mono-, di-, or polyatomic), as illustrated in table 5.1. In the simplest case of the dissociation of a diatomic molecule AB, there is a gain of three translational degrees of freedom and a loss of two rotational degrees of freedom plus one vibration mode. Applying the foregoing method and assumptions, we obtain /Delta1 r C o V = 3 R / 2 -2 R / 2 = 0.5 R , /Delta1 r C o p = 1.5 R , and ( H o 298 -H o 0 ) A + ( H o 298 -H o 0 ) B -( H o 298 -H o 0 ) AB = 1.5 RT = 3.7 kJ mol -1 . At first sight, it may appear surprising that this upper limit is at variance with the data for some molecules, such as HCl and H2, for which DH o (H-H) -DH o 0 (H-H) = 3.9 kJ mol -1 and DH o (H-Cl) -DH o 0 (H-Cl) = 3.8 kJ mol -1 [17].Y et both cases are explained by statistical mechanics [1,11,71]. Dihydrogen is a mixture of ortho - and para -H2, which differ in their nuclear spin states and lead to a heat capacity that at 298.15 K is slightly lower than predicted by the equipartition principle. The heat capacity of chlorine atoms, on the other hand, is higher ( C o p = 21.840 J K -1 mol -1 [17]) than anticipated by its three translational degrees of freedom ( C o p = 20.786 J K -1 mol -1 ) , due to a small electronic contribution.

Although the upper limits of DH o (A-B) DH o 0 (A-B), set by the equipartition principle, must be regarded with caution (see table 5.1), they are indeed applicable to many molecules because, as stated, the vibrational degrees of freedom are not totally frozen at 298.15 K. For instance, when A and B are heavy atoms, like cesium, the vibration frequency is small enough to ensure that the vibration mode is considerably excited, for example, DH o (Cs-Cs) DH o 0 (Cs-Cs) is only 1.4 kJ mol -1 [17].

According to the definition of the A-B bond dissociation enthalpy, reactants and products in reaction 5.1 must be in the gas phase under standard conditions. That is to say that those species are in the ideal gas phase, implying that intermolecular interactions do not exist. DH o T (A-B) refers, therefore, to the isolated moleculeAB,anditdoesnotcontain any contribution from intermolecular forces. Though this is obviously the correct way of defining the energetics of any bond, there are many literature examples where 'bond dissociation enthalpies' have been reported in solution.

In order to distinguish solution from gas-phase bond dissociation enthalpies, we shall use the subscript sln. Thus, DH o T ,sln (A-B) represents the standard enthalpy of the reaction in solution, where the only event is the cleavage of the A-B bond, at a given temperature:

<!-- formula-not-decoded -->

The relationship between DH o (A-B) and DH o sln (A-B) is shown in figure 5.1 and summarized by equation 5.7 (as usual, we dropped the subscript T to indicate that the temperature is 298.15 K). Here, /Delta1 solv H o are the standard enthalpies of solvation of reactants and products (see section 2.7).

<!-- formula-not-decoded -->

Equation 5.7 indicates that DH o (A-B) = DH o sln (A-B) when the solvation terms cancel out. This is seldom observed in practice, but there is some experimental evidence that the net solvation effect on the enthalpy of reaction 5.6 may be small. For instance, it has been shown that the solvation enthalpies of an alkyl radical (R) and the parent hydrocarbon (RH) are similar both in polar and in nonpolar solvents [72]. Hence, the solvation terms in equation 5.7 are approximated by /Delta1 solv H o ( RH ) -/Delta1 solv H o ( R ) -/Delta1 solv H o ( H ) ≈ -/Delta1 solv H o ( H ) . Surprisingly, the solvation enthalpy of the hydrogen atom is not readily available in the literature. Estimates based on the relationship /Delta1 solv H o ( H ) ≈ /Delta1 solv H o ( H2 ) yield /Delta1 solv H o ( H ) ≈ 5 kJ mol -1 in most organic solvents and /Delta1 solv H o ( H ) ≈ -4 kJ mol -1 in water [73].

The scarcity of solvation enthalpy data for species A and B, which are usually free radicals, is the main hindrance to relating DH o (A-B) with DH o sln (A-B).Yet if our goal is to just compare several solution phase bond dissociation enthalpies in a series of molecules from the same family, it may be reasonable to assume that

Figure 5.1 Thermochemical cycle ( T = 298.15 K), showing how solution and gas-phase bond dissociation enthalpies are related. /Delta1 solv H o are standard enthalpies of solvation.

<!-- image -->

the observed trend will be the same in the gas phase. One of the best literature examples involving this assumption concerns the energetics of the O-H bond in phenol and substituted phenols.

Let us start with phenol itself. Although experimental values reported for the PhO-H(Ph = C6H5)bonddissociationenthalpyinthegasphasespanabout30kJ mol -1 (figure 5.2), two different critical evaluations of the data led to the recommended values DH o (PhO-H) = 371.3 ± 2.3 kJ mol -1 [73] and DH o (PhO-H) = 362.8 ± 2.9 kJ mol -1 [74]. These values still differ by 9 kJ mol -1 , but the choice of either one does not affect the following discussion. Bond dissociation enthalpies in solution, DH o sln (PhO-H), in several solvents, are also available in the literature, the most reliable being probably those obtained by photoacoustic calorimetry (see chapter 13). These and gas-phase values are plotted in figure 5.2. It is noted that DH o sln (PhO-H) is always higher than DH o (PhO-H), the differences varying with the solvent.

The trend DH o sln (PhO-H) &gt; DH o (PhO-H), shown in figure 5.2, can be easily explained by using the thermochemical cycle in figure 5.1 with AB = PhOH, A = PhO, and B = H. Equation 5.7 becomes

<!-- formula-not-decoded -->

There is no direct experimental information regarding the last two terms in equation 5.8. However, if we accept the estimate mentioned for /Delta1 solv H o ( H )

<!-- image -->

340

Figure 5.2 Experimental data for the PhO-H bond dissociation enthalpy, in solution (only photoacoustic calorimetry values) and in the gas phase. A recommended gas-phase value is indicated by the solid line and its error limit by dashed lines. Adapted from [75].

( ∼ 5 kJ mol -1 in most organic solvents), then we conclude that the difference DH o sln (PhO-H) -DH o (PhO-H) is determined by the difference /Delta1 solv H o ( PhOH ) -/Delta1 solv H o ( PhO ) .

As discussed by Wayner et al. [76], acetonitrile and ethyl acetate are strong Lewis bases, acting as proton acceptors from phenol.The hydrogen bond between PhOHandthesolventmakes /Delta1 solv H o ( PhOH ) morenegativethan /Delta1 solv H o ( PhO ) . The remaining solvents included in figure 5.2 (benzene, carbon tetrachloride, and isooctane) are weaker Lewis bases and their interactions with PhOH and PhO are more similar.

Suppose that we want to investigate the effect of one or several ring substituent groups on the phenolic O-H bond dissociation enthalpy. As discussed, this analysis should rely on gas-phase values only. However, a perusal of the experimental information available in the literature reveals that DH o (O-H) in phenolic compounds are known for just a few compounds [73]. Therefore, to widen our database we have to consider solution values and assume that DH o sln (O-H) follows the same trend as DH o (O-H). This implies that for any phenolic compound considered (which we can represent by ArOH), the difference between the solvation enthalpies of ArOH and ArO is identical to /Delta1 solv H o ( PhOH ) -/Delta1 solv H o ( PhO ) . This can be a reasonable hypothesis, particularly when the whole series of DH o sln (ArO-H) values examined was derived from experiments in weakly interacting solvents like benzene, isooctane, or carbon tetrachloride. Y et the assumption would definitely be less reliable if the data referred to a strong hydrogen acceptor solvent or if it had been obtained in various solvents. In the case under discussion, there are values of DH o sln (ArO-H) for several phenolic compounds in benzene, obtained by photoacoustic calorimetry [73,77]. A few selected examples are shown in table 5.2.

Note that the values in table 5.2 are not absolute solution phase bond dissociation enthalpies. Because the purpose of the exercise is to probe the substituent

Table 5.2 ArO-H bond dissociation enthalpies of para -monosubstituted phenols in benzene ( T = 298.15 K) relative to DH o sln (PhO-H) [73]. Data in kJ mol -1 .

| Substituent                 | DH o sln (ArO-H) - DH o sln (PhO-H)   |
|-----------------------------|---------------------------------------|
| OCH 3 t -C 4 H H Cl CF 3 CN | - 24.9 ± 4                            |
| 9                           | - 8.2 ± 4                             |
|                             | 0                                     |
|                             | 1.7 ± 4                               |
|                             | 13.7 ± 4                              |
|                             | 20.9 ± 4                              |

effect on the stability of the phenolic O-H bond, DH o sln (ArO-H)aregiven relative to DH o sln (PhO-H). This alternative way of reporting results, referred to a given bond dissociation enthalpy (the so-called anchor), is rather common, not only for solution but also for gas-phase data. Perhaps the main reason why relative bond dissociation enthalpies are often preferred to the absolute values is that they may have smaller error bars. Consider, for instance, a series of experiments involving the determination of the enthalpies of reaction 5.9, where ArOH is, as before, a substituted phenol.

<!-- formula-not-decoded -->

The enthalpies of reactions 5.9 are identified with DH o sln (ArO-H) -DH o sln (PhO-H) for each ArOH. Suppose that the uncertainty assigned to these relative values is ± 4kJ mol -1 . To derive the absolute DH o sln (ArO-H) data, we need a value for DH o sln (PhO-H).Assuming that this is known with an error of ± 8 kJ mol -1 , then the uncertainty assigned to each absolute DH o sln (ArO-H) value will be ( 4 2 + 8 2 ) 1 / 2 = 8.9 kJ mol -1 -possibly too large to allow a discussion of small substituent effects.

There is an additional advantage in using relative solution phase bond dissociation enthalpies. In most cases, solution phase bond dissociation enthalpies do not refer to standard states (see section 2.3), and the required corrections are hard to predict. When we consider relative bond dissociation enthalpies in a series of similar molecules in solution it is likely that the unknown corrections to standard states are nearly constant.

Though some more traditional thermodynamicists will be dismayed by the concept of solution phase bond dissociation enthalpy , the fact is that the database involving these quantities is growing fast. When used judiciously, they may provide important chemical insights-as is indeed the case for the stability of the O-H bond in phenolic compounds. Although solution phase bond dissociation enthalpies are not true bond dissociation enthalpies, because they include some contribution from intermolecular forces, a series of solution values like those in table 5.2 may be (and often is) taken as a good approximation of the trend in the gas-phase.

## 5.2 STEPWISE AND MEAN BOND DISSOCIATION ENTHALPIES

Experimental values of bond dissociation enthalpies are scarce compared with the data available for standard enthalpies of formation. This is not surprising because most chemical reactions that have been studied thermochemically involve the cleavage and the formation of several bonds. The measured standard reaction enthalpies are thus enthalpy balances of various bond dissociation enthalpies, whose individual values are often unknown. Consider, for example, reaction 5.10, where the arene ring in ( η 6 -benzene)chromium tricarbonyl is replaced by three carbonyl ligands. The enthalpy of this reaction at 298.15 K,

calculated as -143.8 ± 9.6 kJ mol -1 by using selected literature data for standard enthalpies of formation [15,16,31], can be given by the bond dissociation enthalpy balance in equation 5.11 (see figure 5.3).

<!-- formula-not-decoded -->

To derive the chromium-benzene bond dissociation enthalpy, the values of several stepwise bond dissociation enthalpies in chromium hexacarbonyl are

<!-- image -->

6

Figure 5.3 Thermochemical cycle, illustrating how the enthalpy of reaction 5.10 can be given as a bond dissociation enthalpy balance.

required. Taking Cr(CO)6 as the starting molecule, we need the first, the second, and the third Cr-CO bond dissociation enthalpies. These can be denoted DH o 1 (Cr-CO), DH o 2 (Cr-CO), and DH o 3 (Cr-CO), respectively, referring to the enthalpies of the following processes:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

There are several literature values for DH o 1 (Cr-CO), DH o 2 (Cr-CO), and DH o 3 (Cr-CO), but the error bars are quite large [31]. Here we will select DH o 1 ( Cr -CO ) = 154 ± 13 kJ mol -1 , DH o 2 ( Cr -CO ) = 167 ± 63 kJ mol -1 , and DH o 3 (Cr-CO) = 84 ± 63 kJ mol -1 , which lead to DH o [(CO)3Cr-C6H6] = 261 ± 91 kJ mol -1 . Although the uncertainty is large, it does not matter if, for example, we are investigating the energetics of chromium-arene bonding in a series of ( η 6 -arene)chromium tricarbonyl complexes. In this case we would only be interested in relative Cr-arene bond dissociation enthalpies and the constant DH o 1 (Cr-CO) + DH o 2 (Cr-CO) + DH o 3 (Cr-CO) = 405 ± 90 kJ mol -1 would cancel out. Incidentally, there is a more precise experimental value for the sum of these stepwise bond dissociation enthalpies, viz . 393 ± 42 kJ mol -1 [31], 1

Now suppose that no data were available for the stepwise Cr-CO bond dissociation enthalpies and we wanted to estimate DH o [(CO)3Cr-C6H6]. A simple approach starts by considering reaction 5.15, where all the Cr-CO bonds are cleaved.

yielding DH o [(CO)3Cr-C6H6] = 249 ± 43 kJ mol -.

<!-- formula-not-decoded -->

Although we ignore the values for some of the six stepwise Cr-CO bond dissociation enthalpies in chromium hexacarbonyl, their sum is equal (equation 5.16) to the enthalpy of reaction 5.15, which is calculated as 641.7 ± 4.8 kJ mol -1 (at 298.15 K) from the well-known standard enthalpies of formation of all the species involved [16,17,31].

<!-- formula-not-decoded -->

the 'best' value mentioned, 249 ± 43 kJ mol -.

If 641.7 kJ mol -1 is required to break the six Cr-CO bonds in Cr(CO)6, we may consider that on average, the cleavage of one bond corresponds to (641.7 ± 4.8 )/ 6 = 107.0 ± 0.8 kJ mol -1 . Therefore, breaking three bonds will require about 321 ± 2 kJ mol -1 . If we now assume that this value applies to the cleavage of the three Cr-CO bonds in Cr(CO)3(C6H6), we obtain DH o [(CO)3Cr-C6H6] = 177 ± 11 kJ mol -1 . Unfortunately, this result is some 72 kJ mol -1 lower than 1

In the previous exercise (whose outcome was not very successful), we used a new concept to assess the thermodynamic stability of chemical bonds: the mean bond dissociation enthalpy (also known as mean bond disruption enthalpy ). It o o is represented by DH or by 〈 DH 〉 (the symbol we adopt). As indicated, for

chromium hexacarbonyl the Cr-CO mean bond enthalpy is given by one-sixth of the enthalpy of reaction 5.15:

<!-- formula-not-decoded -->

The ∼ 72 kJ mol -1 discrepancy observed for DH o [(CO)3Cr-C6H6] alerts us to two important issues: (1) Stepwise bond dissociation enthalpies are often very different from their mean; (2) bond dissociation enthalpy values may not be transferable from one molecule to another. In other words, how can we assess the assumption that 3 〈 DH o 〉 (Cr-CO) in Cr(CO)6 is similar to DH o 1 (Cr-CO) + DH o 2 (Cr-CO) + DH o 3 (Cr-CO) in Cr(CO)3(C6H6 ) ? This question will be discussed in section 5.3. With regard to the former issue, the data in figure 5.4 provide further illustration for some first-row hydrides. The values shown in the plot are results from ab initio calculations for the species involved, in excellent agreement with the most accurate experimental data [78].

We conclude this section by giving, for the sake of clarity, the most general definition of mean bond dissociation enthalpy. For any molecule AYmXn, where A is a central atom and X and Y are any mono- or polyatomic groups, the A-X

Figure 5.4 Stepwise bond dissociation enthalpies in several first-row hydrides. For each compound, the light gray bars, starting on the left, represent DH o 1 (A-H), DH o 2 (A-H), etc. The dark gray bars represent the respective mean bond dissociation enthalpies, 〈 DH o 〉 (A-H). Data at T = 0 from [78].

<!-- image -->

mean bond dissociation enthalpy is defined as 1/n times the enthalpy of reaction 5.17 at 298.15 K:

<!-- formula-not-decoded -->

That is,

<!-- formula-not-decoded -->

If A is bonded to a single type of ligand, as in AXn, then

<!-- formula-not-decoded -->

Finally, it is noted that the concepts of mean and stepwise bond dissociation enthalpies can also be defined in solution (see discussion in section 5.1).

## 5.3 BOND ENTHALPY CONTRIBUTIONS AND BOND STRENGTHS

We have shown that the result of replacing stepwise bond dissociation enthalpies by mean bond dissociation enthalpies and 'transferring' bond dissociation enthalpies from one molecule to another can be deceptive:The assumption that in Cr(CO)3(C6H6 ) , DH o 1 (Cr-CO) + DH o 2 (Cr-CO) + DH o 3 (Cr-CO) ≈ 3 〈 DH o 〉 (CrCO) led to an error of ∼ 72 kJ mol -1 in DH o [(CO)3Cr-C6H6]. Y et this error cancels out if the same procedure is applied to derive relative Cr-arene bond dissociation enthalpies in a series of ( η 6 -arene)chromium tricarbonyl complexes.

There are alternative ways of viewing the previous problem that are closer to the idealized concept of chemical bond strength . Consider reaction 5.20, where all the chromium-ligand bonds are cleaved simultaneously. The enthalpy of this disruption reaction at 298.15 K, calculated as 497.9 ± 10.3 kJ mol -1 by using enthalpy of formation data [15-17,31], can be given as a sum of three chromium-carbonyl and one chromium-benzene bond enthalpy contributions (equation 5.21).

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Bond enthalpy contributions, also named bond enthalpy terms , which we represent by E , have been used to investigate the bonding energetics of many molecules, including organometallic complexes. The case of metal-ligand bonds in substituted metal-carbonyl complexes was first discussed by Skinner and Pilcher [79] and Connor [80]. Because metal-carbonyl stepwise bond dissociation enthalpy data were not available, these authors followed the procedure described in section 5.2, that is, for the example under discussion they have assigned 3 〈 DH o 〉 (Cr-CO) in Cr(CO)6 to the enthalpy associated with the cleavage of the three Cr-CO bonds in Cr(CO)3(C6H6 ) . The authors were, however, aware that 3 〈 DH o 〉 (Cr-CO) could be significantly different from DH o 1 (Cr-CO) + DH o 2 (CrCO) + DH o 3 (Cr-CO). Therefore, to stress that the quantities involved in the

discussion were not true bond dissociation enthalpies, they proposed the bond enthalpy contribution concept. By making E (Cr-CO) = 〈 DH o 〉 (Cr-CO) = 107.0 ± 0.8 kJ mol -1 , we obtain E (Cr-C6H6 ) = 177 ± 11 kJ mol -1 .

Apparently, there is not much advantage in using bond enthalpy contributions to discuss bonding energetics in a series of similar complexes. As already stated, we could have selected any value for DH o 1 (Cr-CO) + DH o 2 (CrCO) + DH o 3 (Cr-CO) and then derived chromium-arene bond dissociation enthalpies in Cr(CO)3(arene) compounds, all based on the same anchor. The trend would not be affected by our choice. Nevertheless, besides emphasizing that the absolute values so obtained should not be regarded as bond dissociation enthalpies, the bond enthalpy contribution concept attempts to consider a pertinent issue in molecular energetics: the transferability of bond enthalpies.

The problem has been stated: What are the grounds for deciding whether a bond dissociation enthalpy can be 'transferred' from one molecule to another? The most obvious guideline would be based on bond lengths. For a chemical bond involving the same atoms, its length and strength vary in opposite directions. This has been known for many years, is taught in every freshman chemistry course, and is illustrated in textbooks, for instance with single, double, and triple carboncarbon bonds [81]. But how is a bond strength evaluated? In the case of diatomic molecules, it appears simple: The bond strength can be ascribed to the bond dissociation enthalpy. In polyatomic molecules, however, this cannot be done. Let us see why.

Consider the molecules phenol and ethanol and their O-H bond lengths in the gas phase, 95.6 pm and 97.1 pm, respectively [82]. The distances are comparable, so we could expect (if the bond strength-bond length relation holds) that their bond strengths are similar or even that the O-H bond in phenol is a little stronger than in ethanol. Nevertheless, it is observed that the bond dissociation enthalpies are in the reverse order: DH o (PhO-H) = 371.3 ± 2.3 kJ mol -1 [73] and DH o (EtO-H) = 439.6 ± 4.0 kJ mol -1 [83]. We can attempt to reconcile this trend with the expected bond length-bond strength relationship by considering figure 5.5.

Figure 5.5 depicts hypothetical thermochemical cycles where the dissociation of the O-H bond in phenol and ethanol is the result of two independent steps. In the first step the bond is cleaved, but the fragment retains the structural and electronic configuration of the parent alcohol. The second step represents the relaxation of the starred (unrelaxed) fragment to the ground state of the phenoxyl or the ethoxyl radical. With this procedure, we are assuming that a bond dissociation enthalpy (the net process) contains some contribution that is extrinsic to the O-H bond strength, which is due to the reorganization of the fragment species. The 'intrinsic' bond strengths will therefore be given by E s(PhO-H) and E s(EtO-H). We have added the subscript s to stress that these bond enthalpy contributions are calculated through thermochemical cycles that involve bond dissociation enthalpies and the reorganization energies ER (PhO*) and ER (EtO*). Later we address other methods to evaluate bond enthalpy contributions.

Figure 5.5 Thermochemical cycles relating O-H bond enthalpy contributions ( E s ) with bond dissociation enthalpies ( DH o ) in phenol and ethanol. ER are reorganization energies (see text).

<!-- image -->

<!-- image -->

To calculate E s(PhO-H) and E s(EtO-H), sometimes called bond-snap enthalpies , we need the values of ER (PhO*) and ER (EtO*), which are not experimentally available. But can we estimate them (at 298.15 K) through computational methods [11]? Let us use density functional theory (B3L YP/ccpVTZ) to derive those quantities. The procedure, illustrated for phenol, is as follows. First the structure of PhOH is optimized through an energy minimization; second, the hydroxylic hydrogen atom is removed while keeping the initial structural parameters of phenol, and the energy of PhO ∗ , E ( PhO ∗ , g ) , is computed; finally, the structure of the fragment PhO is optimized and the corresponding energy, E (PhO, g), obtained. Assuming that contributions due to zero point energy and thermal corrections to 298.15 K are identical for PhO and PhO ∗ , the reorganization energy is given by

<!-- formula-not-decoded -->

The value obtained for the reorganization energy of PhO ∗ , -29.3 kJ mol -1 , together with the PhO-H bond dissociation enthalpy, lead to

<!-- formula-not-decoded -->

For ethanol, the same procedure yields ER (EtO ∗ ) = -9.2 kJ mol -1 and Es (EtO-H) = 449 kJ mol -1 . This value is still some 48 kJ mol -1 higher than the value obtained for phenol, questioning our initial assumption that the bond strengths should be similar in both compounds. Y et we have forgotten two import issues: the resonance stabilization of the phenoxyl radical and the hyperconjugation of the ethoxyl radical.

The problem is that relaxation energies ER (PhO ∗ ) and ER (EtO ∗ ) just calculated do not contain the electronic stabilization of the radicals; they merely account for the structural rearrangements of PhO ∗ and EtO ∗ when they relax to their ground states. In fact, when the density functional theory is used to compute the energies of the fragments PhO ∗ and EtO ∗ the molecular orbital framework is the same as in the relaxed radicals PhO and EtO. Therefore, the energies of PhO ∗ and EtO ∗ already include most of the electronic stabilization of the radicals.

As computational chemistry provides no help in solving this problem, we can use our initial assumption to estimate the total stabilization energies of the phenoxyl and ethoxyl radicals. The O-H bond lengths in phenol and ethanol are also very close to the O-H bond length in water (95.7 pm [82]), indicating that in the absence of stabilization effects, the bond dissociation enthalpies should be similar in the three molecules. In water DH o (HO-H) = 497.1 ± 0.3 kJ mol -1 [83], which is 126 kJ mol -1 higher than DH o (PhO-H) and 58 kJ mol -1 higher than DH o (EtO-H).Thenegativesofthesevaluesthusmeasurethe total relaxation energies of PhO* and EtO ∗ , respectively.

In summary, the previous example shows that bond dissociation enthalpies should not be correlated with bond lengths unless the relaxation energies of the fragments are comparable. On the other hand, when two bonds between the same pairs of atoms have identical bond lengths, it is sensible to assume that they have similar bond enthalpy contributions. Hence, in this case, a bond enthalpy contribution can be transferred from one molecule to another.

There are many other examples in the literature where the concept of bond enthalpy contribution (either E or E s) has been applied. Let us return to the case of Cr(CO)3(C6H6 ) and examine the procedure to estimate E s(Cr-C6H6 ) . This is much more complex than the case of the O-H bond in phenol and ethanol, as suggested by figure 5.6.

Let us concentrate on the thermochemical cycle of figure 5.6 that involves the disruption of the complex Cr(CO)3(C6H6 ) . The enthalpy of this reaction, previously calculated as 497.9 ± 10.3 kJ mol -1 from standard enthalpy of formation data, can be related (equation 5.24) to the bond enthalpy contributions E s(Cr-CO) and E s(Cr-C6H6 ) through the reorganization energies ER (CO ∗∗ ) and ER (C6H ∗∗ 6 ). Two asterisks indicate that the fragment has the same structure as

Figure 5.6 Thermochemical cycles to estimate the Cr-C 6 H 6 bond enthalpy contribution ( E s ) in Cr(CO) 3 (C 6 H 6 ). ER are reorganization energies. One asterisk indicates that the fragment has the same structure as in Cr(CO) 6 , and two asterisks mean that the fragment has the same structure as in Cr(CO) 3 (C 6 H 6 ).

<!-- image -->

in Cr(CO)3(C6H6). Note that because we only consider the geometrical relaxation of the fragments, the reorganization energies of atoms are zero, that is, ER (Cr) = 0.

<!-- formula-not-decoded -->

To derive E s(Cr-C6H6 ) , we need a value for E s(Cr-CO).This can be estimated by using data for Cr(CO)6. However, the geometries of the Cr(CO)3 fragment in this complex and in Cr(CO)3(C6H6 ) [84] are different, implying different Cr-CO bond enthalpy contributions. The second cycle in figure 5.6, leading to equation 5.25, allows us to estimate this difference. One asterisk indicates that the fragment has the same structure as in Cr(CO)6, E ′ s ( Cr -CO ) is the bond enthalpy contribution in this complex, and ER [ Cr(CO) 3 ∗ ] is the energy difference between the geometries of the Cr(CO)3 moiety in Cr(CO)3(C6H6 ) and Cr(CO)6.

<!-- formula-not-decoded -->

Weare now left with the evaluation of E ′ s ( Cr -CO ) , the Cr-CO bond enthalpy contribution in Cr(CO)6. The third thermochemical cycle in figure 5.6 shows how this bond enthalpy contribution can be evaluated from the Cr-CO mean bond dissociation enthalpy (107.0 ± 0.8 kJ mol -1 ; see section 5.2) and the reorganization energy ER (CO ∗ ).

All these steps, based on the cycles in figure 5.6, can be summarized by equation 5.26, where it is observed that most of the reorganization energies cancel out.

<!-- formula-not-decoded -->

The choice of the computational method to estimate ER [ Cr(CO) 3 ∗ ] and ER ( C6H6 ∗∗ ) is, of course, a relevant issue. Here we accept the published results of extended Hückel calculations, viz . ER [ Cr(CO) 3 ∗ ] ≈ -72 kJ mol -1 and ER ( C6H6 ∗∗ ) ≈ -24 kJ mol -1 [84], leading to E s ( Cr -C6H6 ) ≈ 129 kJ mol -1 .

According to the extended Hückel method, E s ( Cr -C6H6 ) is therefore some 48 kJ mol -1 lower than the even cruder calculation made at the beginning of the present section, E ( Cr -C6H6 ) = 177 kJ mol -1 . This large discrepancy is due to fact that E s bond enthalpy contributions rely on a procedure where the 'transfer' of bond enthalpies was carefully considered not only on the basis of bond lengths but also on the basis of bond angles. For instance, the error of assigning the Cr-CO bond enthalpy contribution in Cr(CO)6 to the Cr-CO bond enthalpy contribution in Cr(CO)3(C6H6 ) can be estimated as 34 kJ mol -1 by using equation 5.25 and ER (CO*) ≈ -8 kJ mol -1 , ER (CO ∗∗ ) ≈ -18 kJ mol -1 , and ER [Cr(CO) ∗ 3 ] ≈ -72 kJ mol -1 [84]. Incidentally, the fact that E s ( Cr -CO ) is considerably larger than E ′ s ( Cr -CO ) is in keeping with the Cr-CO bond lengths in the complexes: 191.6 pm in Cr(CO)6 and 184.5 pm in Cr(CO)3(C6H6 ) [84].

Thermochemical cycles like those in figures 5.5 and 5.6 were proposed in the early 1980s to calculate bond enthalpy contributions from bond dissociation enthalpies and reorganization energies [85,86], but the idea of trying to 'adjust' bond enthalpy contributions with bond lengths and angles is older. For example, it had been applied by Skinner in 1945 to discuss the energetics of several types of bonds [87]. He found that plots of bond enthalpy contributions ( E ) versus bond lengths ( r ) could be described by equation 5.27, where A and n are empirical constants (e.g., for carbon-carbon bonds A = 1410 kJ mol -1 Å n and n = 3.14,

with r in ångstrom [86]). Interestingly, Skinner' s analysis provided an estimated value for the enthalpy of sublimation of carbon (quite uncertain at the time) as 711 kJ mol -1 . The currently accepted value is 716.68 ± 0.45 kJ mol -1 [16].

<!-- formula-not-decoded -->

Early applications of thermochemical cycles involving reorganization energies were hindered mainly by the lack of computer power. The computation of the reorganization energies of large polyatomic fragments was beyond the reach of most thermochemists or, at best, could be made only through a low-level calculation (such as the extended Hückel method, used above). To avoid this difficulty, an operational procedure has been developed [85,86,88] based on the Laidler terms for organic compounds [89].

## 5.4 THE LAIDLER TERMS

The so-called Laidler scheme was developed as a tool to estimate standard enthalpies of formation of organic compounds [90]. It relies on the bondadditivity concept, that is, it assumes that the standard enthalpy of atomization of a given molecule in the gas phase ( /Delta1 at H o , defined as the standard enthalpy of the reaction where all the chemical bonds are cleaved, yielding the gaseous ground-state atoms) can be evaluated by adding the relevant bond enthalpy terms . For instance, in the case of phenol, its standard enthalpy of atomization, or simply its enthalpy of atomization , refers to reaction 5.28 at 298.15 K:

<!-- formula-not-decoded -->

The Laidler terms needed to estimate /Delta1 at H o (PhOH, g) are given in the equation:

<!-- formula-not-decoded -->

To 'atomize' the phenol molecule, we have to cleave six carbon-carbon bonds in the aromatic ring (Cb -Cb ) , five carbon-hydrogen bonds (Cb -H), one carbonoxygen bond (Cb -O), and one oxygen-hydrogen bond (O-H). The symbol E L has been adopted is this equation (instead of the more used symbol E ) to avoid confusion with the quantities discussed in the previous section.

The most reliable values of Laidler terms that can applied to a wide variety of compounds are those recommended by Cox and Pilcher [89]. They were derived from a consistent database that includes experimentally determined standard enthalpies of formation for hundreds of organic compounds. This lengthy but simple exercise involves the choice of a set of bond enthalpy terms that affords the best agreement between experimental and calculated standard enthalpies of

atomization. Using the values for the terms in equation 5.29, we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The standard enthalpy of formation of phenol can be derived as /Delta1 f H o (PhOH, g) = -94.2 kJ mol -1 from /Delta1 at H o (PhOH, g) and the standard enthalpies of formation of the gaseous atoms, viz . /Delta1 f H o (C, g) = 715.05kJmol -1 , /Delta1 f H o (H, g) = 217.99 kJ mol -1 , and /Delta1 f H o (O, g) = 249.20 kJ mol -1 [89]. The 1

It is important to note that /Delta1 f H o (PhOH, g) = -94.2 kJ mol -1 relies on the values of the standard enthalpies of formation of the gaseous elements tabulated by Cox and Pilcher [89], rather than on the currently accepted data, viz . /Delta1 f H o (C, g) = 716.68 kJ mol -1 , /Delta1 f H o (H, g) = 217.998 kJ mol -1 , and /Delta1 f H o (O, g) = 249.18 kJ mol -1 [16]. Without this precaution, the calculation would have been another example of thermochemical inconsistency (see section 2.5); the Laidler terms in Cox and Pilcher' s book were evaluated by using a given set of values for the standard enthalpies of formation of the gaseous elements, hence the same data must be used when estimating standard enthalpies of formation of organic compounds. In the case of PhOH, if the values recommended by CODATA [16] were used, we would have obtained /Delta1 f H o (PhOH, g) = -84.4 kJ mol -1 , almost 10 kJ mol -1 higher than the experimental result.

experimental /Delta1 f H o (PhOH, g) is -96.4 ± 0.9 kJ mol -[15].

As mentioned, the Laidler scheme has an empirical origin, and it is not simple to ascribe a physical meaning to E L. To be an intrinsic bond strength, the E L(R-H)valuefor any molecule RH should always be larger than the corresponding bond dissociation enthalpy, DH o ( R -H ) . Otherwise, as can be concluded from a scheme similar to the ones in figure 5.5 (or from an equation like 5.23), the reorganization energy of R ∗ would be positive-which, of course, makes no sense. The simple example of ethane, where E L(Et-H) = 410.8 kJ mol -1 [89] and DH o ( Et -H ) = 423.0 ± 1.7 kJ mol -1 [91], implying ER (Et ∗ ) = 12 kJ mol -1 , demonstrates that in fact, Laidler terms are not intrinsic bond strengths. As a comparison, the (structural) reorganization energy of Et* obtained with density functional theory (B3L YP/cc-pVTZ) is -29.8 kJ mol -1 , yielding E s(Et-H) = 453 kJ mol -1 . As already discussed, the computed ER (Et ∗ ) is a high limit because it does not include the stabilization (by hyperconjugation) of the ethyl radical.

Despite some lack of physical meaning, the empirical Laidler terms have a rather successful predictive power. That justified their use in the past as replacements for Es values [85,86,88], when computational methods were not readily available. It also justifies recent efforts to develop the Laidler scheme by using a larger number of parameters (accounting, e.g., for intramolecular repulsions) [92].

## References to Part I

1. P. W. Atkins, J. de Paula. Physical Chemistry (8th ed.). Oxford University Press: Oxford, 2006.
2. K. J. Laidler. The World of Physical Chemistry . Oxford University Press: Oxford, 1995.
3. D. R. Herschbach. Chemical Reaction Dynamics and Electronic Structure . In The Chemical Bond : Structure and Dynamics ; A. Zewail, Ed.; Academic Press: San Diego, 1992; chapter 8.
4. G. N. Lewis, M. Randall. Thermodynamics and the Free Energy of Chemical Substances . McGraw-Hill: NewYork, 1923.
5. F. D. Rossini. Fifty Years of Thermodynamics and Thermochemistry . J. Chem. Thermodynamics 1976 , 8 , 805-834.
6. H. A. Skinner. The Thermochemistry of Organometallic Compounds . J. Chem. Thermodynamics 1978 , 10 , 309-320.
7. G. Pilcher. Obituary: Professor H. A. Skinner (30 January 1916-14 May 1996) . J. Chem. Thermodynamics 1996 , 28 , 1195.
8. P. W. Atkins, J. de Paula. The Elements of Physical Chemistry (4th ed.). Oxford University Press: Oxford, 2005.
9. K. M. Ervin. Experimental Techniques in Gas-Phase Ion Thermochemistry . Chem. Rev. 2001 , 101 , 391-444.
10. R. M. Caprioli, M. L. Gross, Eds. The Encyclopedia of Mass Spectrometry . Elsevier: Amsterdam, 2004.
11. K. K. Irikura, D. J. Frurip, Eds. Computational Thermochemistry: Prediction and Estimation of Molecular Thermodynamics . ACS Symposium Series 677; American Chemical Society: Washington, DC, 1998.
12. P. R. Schleyer, P . R. Schreiner, N. L. Allinger, T. Clark, J. Gasteiger, P . Kollman, H. F. Schaefer III, Eds. Encyclopedia of Computational Chemistry . Wiley: Chichester, 1998.
13. IUPAC-Physical Chemistry Division. Quantities, Units and Symbols in Physical Chemistry (2nd ed.). Blackwell Scientific Publications: Oxford, 1993. A provisional document of the 3rd ed. of this work is available online at www.iupac.org/reports/provisional/abstract05/stohner\_310306.html (May 2006).
14. B. N. Taylor. Guide for the Use of the International System of Units ( SI ). NIST Special Publicaton 811; U.S. Government Printing Office: Washington, DC, 1995. See also www.nist.gov/servb.htm.
15. J. B. Pedley. Thermochemical Data and Structures of Organic Compounds . Thermodynamics Research Center Data Series, vol. 1; Thermodynamics Research Center: College Station, 1994.
16. J. D. Cox, D. D. Wagman, V . A. Medvedev, Eds. CODATA Key Values for Thermodynamics . Hemisphere: New Y ork, 1989.

17. D. D. Wagman, W. H. Evans, V . B. Parker, R. H. Schumm, I. Halow, S. M. Bailey, K. L. Churney, R. L. Nuttall. The NBS Tables of Chemical Thermodynamic Properties: Selected V alues for Inorganic and C 1 and C 2 Organic Substances in SI Units . J. Phys. Chem. Ref. Data 1982 , 11 , suppl. 2.
18. K.Denbigh. ThePrinciplesofChemicalEquilibrium (4th ed.). Cambridge University Press: Cambridge, 1981.
19. NIST-JANAFThermochemicalTables (4th ed.). M. W . Chase Jr., Ed.; J. Phys. Chem. Ref. Data 1998 , 1-1951; Monograph 9.
20. J. H. Dymond, E. B. Smith. The Virial Coefficients of Pure Gases and Mixtures: A Critical Compilation . Clarendon Press: Oxford, 1980.
21. H.V . Kehiaian. Virial Coefficients of Selected Gases . In CRCHandbookofChemistry and Physics ; D. R. Lide, Ed.; CRC Press: Boca Raton, 2005; pp. 6.23-6.42.
22. F. D. Rossini, D. D. Wagman, W. H. Evans, S. Levine, I. Jaffe. Selected Values of Chemical Thermodynamic Properties . NBS Circular 500; U.S. Department of Commerce: Washington, DC, 1952.
23. B. Ruscic, R. E. Pinzon, M. L. Morton, G. von Laszevski, S. J. Bittner, S. G. Nijsure, K. A. Amin, M. Minkoff, A. F. Wagner. Introduction to Active Thermochemical Tables: Several ' Key ' Enthalpies of Formation Revisited . J. Phys. Chem. A 2004 , 108 , 9979-9997.
24. B. Ruscic, R. E. Pinzon, G. von Laszewski, D. Kodeboyina, A. Burcat, D. Leahy, D. Montoya, A. F. Wagner. Active Thermochemical Tables: Thermochemistry for the 21st Century . J. Physics: Conference Series 2005 , 16 , 561-570.
25. M. L. McGlashan. Chemical Thermodynamics . Academic Press: London, 1979.
26. F. D. Rossini, W . E. Deming. The Assignment of Uncertainties to the Data of Chemistry and Physics, with Specific Recommendations for Thermochemistry . J. Wash. Acad. Sci . 1939 , 29 , 416-441.
27. F. D. Rossini. Assignment of Uncertainties to Thermochemical Data . In Experimental Thermochemistry , vol. I; F . D. Rossini, Ed.; Interscience: New Y ork, 1956; chapter 14.
28. G. Olofsson. Assignment of Uncertainties . In Experimental Chemical Thermodynamics , vol. 1; S. Sunner, M. Månsson, Eds.; IUPAC-Pergamon Press: Oxford, 1979; chapter 6.
29. A Guide to Procedures for the Publication of Thermodynamic Data . J. Chem. Thermodynamics 1972 , 4 , 511.
30. D. R. Lide, Ed. CRC Handbook of Chemistry and Physics . CRC Press: Boca Raton, 2005.
31. J. A. Martinho Simões. Organometallic Thermochemistry Data . In NIST Chemistry WebBook ; NIST Standard Reference Database no. 69; P . J. Linstrom, W . G. Mallard, Eds.; National Institute of Standards and Technology: Gaithersburg, June 2005 (webbook.nist.gov).
32. V. P . Glushko, Ed. ThermalConstantsofSubstances ; vols. 1-10.Academy of Science, USSR: Moscow, 1965-1982.
33. K. K. Irikura, R. D. Johnson III, R. Kacker. Uncertainty Associated with Virtual Measurements from Computational Quantum Chemistry Models . Metrologia 2004 , 41 , 369-375.
34. Natural Gas-Calculation of Calorific V alues, Density, Relative Density and Wobbe Index from Composition . ISO 6976:1995(E).
35. G. W. Thomson. Determination of Vapor Pressure . In Technique of Organic Chemistry ; vol. I, part 1, Physical MethodsofOrganicChemistry (3rd. ed.);A.Weissberger, Ed.; Interscience: New Y ork, 1965; chapter 9.

36. J. L. Margrave, Ed. The Characterization of High Temperature Vapors . Wiley: NewYork, 1967.
37. E. D. Cater. The Effusion Method at Age 69: Current State of the Art . NBS Special Publication 561; National Bureau of Standards: Gaithersburg, 1979.
38. Y. A. Lebedev, E. A. Miroshnichenko. Thermochemistry of Organic Compounds Evaporation . In Thermochemistry and Equilibria of Organic Compounds , book II; M. Frenkel, Ed.; VCH: New Y ork, 1993; chapter 2.
39. V. Majer, V . Svoboda. Enthalpies of V aporization of Organic Compounds. A Critical Review and Data Compilation . IUPAC Chemical Data Series no. 32; Blackwell: Oxford, 1985.
40. H. P . Diogo, R. C. Santos, P . M. Nunes, M. E. Minas da Piedade. Ebulliometric Apparatus for the Measurement of Enthalpies of Vaporization . Thermochim. Acta 1995 , 249 , 113-120.
41. B. E. Poling, J. M. Prausnitz, J. P . O'Connell. The Properties of Gases and Liquids (5th ed.). McGraw-Hill: New Y ork, 2001.
42. E. Wilhelm, R. Battino. Thermodynamic Functions of the Solubilities in Liquids at 25 ◦ C . Chem. Rev. 1973 , 73 , 1-9.
43. E. Wilhelm, R. Battino, R. J. Wilcock. Low-Pressure Solubilities of Gases in Liquid Water . Chem. Rev. 1977 , 77 , 219-262.
44. P. G. T. Fogg, W . Gerrard. Solubility of Gases in Liquids . Wiley: Chichester, 1991.
45. P. W. Atkins, T. Overton, J. Rourke, M. Weller, F. Armstrong. Inorganic Chemistry (4th ed.). Oxford University Press: Oxford, 2006.
46. D. A. Johnson. Some Thermodynamic Aspects of Inorganic Chemistry (2nd ed.). Cambridge University Press: Cambridge, 1982.
47. W.E.Dasent. Inorganic Energetics:An Introduction (2nded.). Cambridge University Press: Cambridge, 1982.
48. J. P. Leal, J. A. Martinho Simões. Standard Molar Enthalpies of Formation of Lithium Alkoxides . J. Organometal. Chem . 1993 , 460 , 131-138.
49. H.D.B.Jenkins, H. K. Roobottom. Lattice Energies . In CRCHandbookofChemistry and Physics ; D. R. Lide, Ed.; CRC Press: Boca Raton, 2005.
50. M.D.Tissandier, K.A. Cowen, W.Y. Feng, E. Gundlach, M. H. Cohen,A. D. Earhart, J. V . Coe, T. R. Tuttle Jr. The Proton's Absolute Aqueous Enthalpy and Gibbs Free Energy of Solvation from Cluster-Ion Solvation Data . J. Phys. Chem. A 1998 , 102 , 7787-7794.
51. Standard Quantities in ChemicalThermodynamics. Fugacities,Activities, and Equilibrium Constants for Pure and Mixed Phases . IUPAC Recommendations 1994; Pure &amp; Appl. Chem. 1994 , 66 , 533-552.
52. H. Naghibi, A. Tamura, J. M. Sturtevant. Significant Discrepancies Between van't Hoff and Calorimetric Enthalpies . Proc. Natl. Acad. Sci. USA 1995 , 92 , 5597-5599.
53. L.V . Gurvich, I.V .Veyts, C. B.Alcock, Eds. Thermodynamic Properties of Individual Substances (4th ed.). vols. 1 and 2; Hemisphere: New Y ork, 1989 and 1991; vol. 3; CRC Press: Boca Raton, 1994.
54. V. P . Glushko, Ed. Thermodynamic Properties of Individual Substances (3rd ed.); vols. 1-4. Nauka: Moscow, 1978-1982.
55. S. W. Benson. Thermochemical Kinetics (2nd ed.). Wiley: New Y ork, 1976.
56. K. J. Laidler. Chemical Kinetics (3rd ed.). Harper &amp; Row: New Y ork, 1987.
57. J. I. Steinfeld, J. S. Francisco, W . L. Hase. Chemical Kinetics and Dynamics (2nd ed.). Prentice Hall: New Jersey, 1999.
58. M. J. Pilling, P . W . Seakins. Reaction Kinetics . Oxford University Press: Oxford, 1995.

59. J. W . Moore, R. G. Pearson. Kinetics and Mechanism (3rd ed.). Wiley: New Y ork, 1981.
60. D. F. McMillen, D. M. Golden. Hydrocarbon Bond Dissociation Energies . Ann. Rev. Phys. Chem. 1982 , 33 , 493-532.
61. T. W. Koenig, B. P . Hay, R. G. Finke. Cage Effects in Organotransition Metal Chemistry: Their Importance in the Kinetic Estimation of Bond Dissociation Energies in Solution . Polyhedron 1988 , 7 , 1499-1516.
62. S. G. Lias, J. E. Bartmess, J. F . Liebman, J. L. Holmes, R. D. Levin, W . G. Mallard. Gas Phase Ion and Neutral Thermochemistry . J. Phys. Chem. Ref. Data 1988 , 17 , suppl. 1.
63. J. E. Bartmess. Thermodynamics of the Electron and the Proton . J. Phys. Chem . 1994 , 98 , 6420-6424; ibid. 1995 , 99 , 6755.
64. J. C. Traeger, R. G. McLoughlin. Absolute Heats of Formation for Gas-Phase Cations . J. Am. Chem. Soc. 1981 , 103 , 3647-3652.
65. J. C. Traeger, B. M. Kompe. Thermochemical Data for Free Radicals from Studies of Ions . In Energetics of Organic Free Radicals ; J. A. Martinho Simões, A. Greenberg, J. F . Liebman, Eds.; Blackie: London, 1996; chapter 3.
66. J. L. Holmes. ThePresentStateandUtilityofIonThermochemistry . J. Mass Spectrom. Ion. Proc. 1992 , 118/119 , 381-394.
67. S. G. Lias. Ionization Energy Data . In NIST Chemistry WebBook ; NIST Standard Reference Database no. 69; P . J. Linstrom, W . G. Mallard, Eds.; National Institute of Standards and Technology: Gaithersburg, June 2005 (webbook.nist.gov).
68. J. L. Holmes, F. P . Lossing, A. Maccoll. Heats of Formation of Alkyl Radicals from Appearance Energies . J. Am. Chem. Soc. 1988 , 110 , 7339-7342.
69. F. P . Lossing. Heats of Formation of Some Isomeric [ C n H 2n + 1 O ] + Ions: Substitutional Effects on Ion Stability . J. Am. Chem. Soc. 1977 , 99 , 7526-7530.
70. J. M. L. Martin, T. J. Lee. The Atomization Energy and Proton Affinity of NH 3 : An Ab Initio Calibration Study . Chem. Phys. Lett. 1996 , 258 , 136-143.
71. B. J. McClelland. Statistical Thermodynamics . Science Paperbacks: London, 1973.
72. J. M. Kanabus-Kaminska, B. C. Gilbert, D. Griller. Solvent Effects on the Thermochemistry of Free-Radical Reactions . J. Am. Chem. Soc . 1989 , 111 , 3311-3314.
73. R. M. Borges dos Santos, J. A. Martinho Simões. Energetics of the O-H Bond in Phenol and Substituted Phenols: A Critical Evaluation of Literature Data . J. Phys. Chem. Ref. Data 1998 , 27 , 707-739.
74. P. Mulder, H.-G. Korth, D. A. Pratt, G. A. DiLabio, L. Valgimigli, G. F. Pedulli, K. U. Ingold. Critical Re-evaluation of the O-H Bond Dissociation Enthalpy in Phenol . J. Phys. Chem. A 2005 , 109 , 2647-2655.
75. M. M. Bizarro, B. J. Costa Cabral, R. M. Borges dos Santos, J. A. Martinho Simões. Substituent Effects on the O-H Bond Dissociation Enthalpies in Phenolic Compounds: Agreements and Controversies . Pure Appl. Chem. 1999 , 71 , 1249-1256.
76. D. D. M. Wayner, E. Lusztyk, D. Pagé, K. U. Ingold, P . Mulder, L. J. J. Laarhoven, H. S. Aldrich. Effects of Solvation on the Enthalpies of Reaction of tert-Butoxyl Radicals with Phenol and on the Calculated O-H Bond Strength in Phenol . J. Am. Chem. Soc . 1995 , 117 , 8737-8744.
77. D. D. M. Wayner, E. Lusztyk, K. U. Ingold, P . Mulder. Application of Photoacoustic Calorimetry to the Measurement of the O-H Bond Strength in Vitamin E ( α - and δ -Tocopherol) and Related Phenolic Antioxidants . J. Org. Chem. 1996 , 61 , 6430-6433.

78. J. M. L. Martin. BenchmarkAb Initio Calculations of the Total Atomization Energies of the First-Row Hydrides AH n ( A = Li-F ) . Chem. Phys. Lett. 1997 , 273 , 98-106.
79. G. Pilcher, H. A. Skinner. Thermochemistry of Organometallic Compounds . In The Chemistry of the Metal-Metal Bond ; F . R. Hartley, S. Patai, Eds.; Wiley: New Y ork, 1982; chapter 2.
80. J. A. Connor. Thermochemical Studies of Organo-transition Metal Carbonyls and Related Compounds . Top. Curr. Chem. 1977 , 71 , 71-110.
81. P. W. Atkins, J. A. Beran. General Chemistry (2nd ed.). Scientific American: NewYork, 1992.
82. Bond Lengths and Angles in Gas-Phase Molecules . In CRCHandbook of Chemistry and Physics ; D. R. Lide, Ed.; CRC Press: Boca Raton, 2005; pp. 9.15-9.41.
83. B. Ruscic, J. E. Boggs, A. Burcat, A. G. Csaszar, J. Demaison, R. Janoschek, J. M. L. Martin, M. L. Morton, M. J. Rossi, J. F . Stanton, P . G. Szalay, P . R. Westmoreland, F . Zabel, T. J. Berces. IUPACCritical Evaluation ofThermochemical Properties of Selected Radicals. Part I . J. Phys. Chem. Ref. Data 2005 , 34 , 573-656.
84. M.J. Calhorda, C. F. Frazão, J.A. Martinho Simões. Metal-Carbon ' BondStrengths ' in Cr ( CO ) 6 , Cr (η -C 6 H 6 ) 2 , and Cr ( CO ) 3 (η -C 6 H 6 ) . J. Organometal. Chem. 1984 , 262 , 305-314.
85. A. R. Dias, M. S. Salema, J. A. Martinho Simões. Enthalpies of Formation of Ti (η -C 5 H 5 ) 2 ( OR ) 2 Complexes ( R = C 6 H 5 , 2 -CH 3 C 6 H 4 , 3 -CH 3 C 6 H 4 , 4 -CH 3 C 6 H 4 , and 2 -ClC 6 H 4 ) . J. Organometal. Chem. 1981 , 222 , 69-78.
86. A. R. Dias, J. A. Martinho Simões. On the Evaluation of Metal-Ligand ' Bond Strengths ' in M (η -C 5 H 5 ) 2 L 2 Complexes . Rev. Port. Quím. 1982 , 24 , 191-199.
87. H. A. Skinner. A Revision of Some Bond-Energy Values and the Variation of BondEnergy with Bond Length . Trans. Faraday Soc. 1945 , 41 , 645-662.
88. J. A. Martinho Simões, J. L. Beauchamp. Transition Metal-Hydrogen and MetalCarbon Bond Strengths: The Keys to Catalysis . Chem. Rev. 1990 , 90 , 629-688.
89. J. D. Cox, G. Pilcher. Thermochemistry of Organic and Organometallic Compounds . Academic Press: London, 1970.
90. K. J. Laidler. A System of Molecular Thermochemistry for Organic Gases and Liquids . Can. J. Chem. 1956 , 34 , 626-648.
91. S. J. Blanksby, G. B. Ellison. Bond Dissociation Energies of Organic Molecules . Acc. Chem. Res. 2003 , 36 , 255-263.
92. J. P. Leal. Additive Methods for Prediction of Thermochemical Properties . The Laidler Method Revisited. 1. Hydrocarbons. J. Phys. Chem. Ref. Data 2006 , 35 , 55-76.

## PART II

## CONDENSED PHASE METHODS

This page intentionally left blank

6

## Overview of Condensed Phase Methods

This part includes a discussion of the main experimental methods that have been used to study the energetics of chemical reactions and the thermodynamic stability of compounds in the condensed phase (solid, liquid, and solution). The only exception is the reference to flame combustion calorimetry in section 7.3. Although this method was designed to measure the enthalpies of combustion of substances in the gaseous phase, it has very strong affinities with the other combustion calorimetric methods presented in the same chapter.

Most published enthalpies of formation and reaction in the condensed phase were determined by calorimetry (see databases indicated in appendix B). It is therefore not surprising that the discussion of calorimetric methods occupies a large fraction of part II.

The heart of a calorimeter is the calorimeter proper (also called measuring system or sample cell ), which contains the reaction vessel , where the chemical reaction or phase transition under study occurs. Sometimes the calorimeter proper coincides with the reaction vessel. For example, in the setup shown in figure 6.1a, which is typical of many combustion calorimeters, the reaction vessel is placed inside the calorimeter proper. In the arrangement of figure 6.1b, used in many reaction-solution calorimeters, the calorimeter proper is also the reaction vessel. Normally, a controlled-temperature jacket surrounds the calorimeter proper. Other parts besides thermometers, commonly found in calorimeters, are stirring, heating, cooling, and ignition devices. Some of these devices are placed inside the calorimeter proper or cross its boundaries and are also considered to be part of it. In modern instruments, the data acquisition and many steps of the calorimetric experiments are usually computer-controlled.

Calorimeters of many different designs have been constructed and operated. However, these are all variations of a few basic categories [1-6]. For example, based on the heat exchange mode between the calorimeter proper and the surrounding jacket, it is convenient to distinguish three main classes of calorimeters: adiabatic , heat conduction , and isoperibol . In a perfectly adiabatic calorimeter (figure 6.2a) no heat is transferred between the calorimeter proper and the jacket (the corresponding heat flow rate Φ = dQ / dt = 0, where Q represents the heat exchanged and t is time). Because no perfect adiabatic calorimeter can be built, the term adiabatic usually designates an instrument where the jacket temperature, T j, is controlled to follow the temperature of the calorimeter proper, T c.

<!-- image -->

b

Figure 6.1 Examples of calorimeters in which the calorimeter proper (a) contains the reaction vessel and (b) coincides with the reaction vessel.

During an experiment, the difference between T c and T j is kept as small as possible ( T c ≈ T j ) to minimize the heat transfer between the calorimeter proper and the jacket. In isoperibol instruments (figure 6.2b), a constant temperature jacket surrounds the calorimeter proper and, in general, T c /negationslash= T j during an experiment. The heat transfer between the calorimeter proper and the jacket is small and calculable by Newton's cooling law. Isoperibol is a Greek word meaning 'constant environment'; the term was coined by Kubaschewski and Hultgren [1]. Finally, in an ideal heat conduction (or heat flow) calorimeter, sketched in figure 6.2c, heat is completely exchanged by conduction between the calorimeter proper and the jacket. This condition is therefore opposite to the adiabatic case. In practice, the thermal conductivity of the interspace is made large by placing a thermopile between the calorimeter proper and the jacket. The jacket has a very high heat capacity compared with that of the calorimeter proper and acts as a heat sink, that is, T j is not affected by the total amount of thermal energy being transferred. In general, T c = T j in the initial and the final state of the calorimetric experiment.

The calorimetry lexicon also includes other frequently used designations of calorimeters. When the calorimeter proper contains a stirred liquid, the calorimeter is called stirred-liquid . When the calorimeter proper is a solid block (usually made of metal, such as copper), the calorimeter is said to be aneroid . For example, both instruments represented in figure 6.1 are stirred-liquid isoperibol calorimeters. The term scanning calorimeter is used to designate an instrument where the temperatures of the calorimeter proper and/or the jacket vary at a programmed rate.

The energy change associated with the process under study induces an energy change of the calorimeter proper, which can be determined by monitoring a corresponding temperature change or heat flux. In some calorimeters the reaction occurs in a closed vessel whose volume does not vary in the course of the experiment. This happens, for example, in bomb combustion calorimetry, where the reaction takes place inside a pressure vessel called the 'bomb,' and in

<!-- image -->

c

Figure 6.2 Schematic representation of (a) an adiabatic calorimeter, (b) an isoperibol calorimeter, and (c) a heat conduction (or heat flow) calorimeter. T c and T j are the temperatures of the calorimeter proper and the external jacket, respectively, and Φ is the heat flow rate between the calorimeter proper and the external jacket.

some differential scanning calorimetry experiments where the sample is inside a sealed capsule. In these cases, the primarily derived quantity from an experiment is the internal energy of reaction, /Delta1 r U . On the other hand, when constant pressure calorimeters are used, the experimental measurements primarily lead to the enthalpy of reaction, /Delta1 r H . The values of /Delta1 r H and /Delta1 r U are related by

<!-- formula-not-decoded -->

where /Delta1 r V is the difference in molar volume between products and reactants at constant pressure, p . In the case of reactions where both reactants and products are in the condensed phase, the p /Delta1 r V term in equation 6.1 is quite small (usually within the uncertainty of the calorimetric experiment) and can be neglected. For example, typical values of p = 0.1 MPa and /Delta1 r V = 1cm 3 mol -1 yield p /Delta1 r V = 0.1 J mol -1 . This value is much smaller than the errors found in the determination

of /Delta1 r H and /Delta1 r U that, depending on the reaction and the calorimeter used, are at least in the range of 10 J mol -1 to 1 kJ mol -1 . For reactions involving gaseous reactants or products, however, the p /Delta1 r V term may be significant. Assuming ideal gas behavior, it can be concluded from equation 6.1 that

<!-- formula-not-decoded -->

were /Delta1 r ν is the difference between the stoichiometric number of gaseous products and reactants. For example, in the combustion of methane according to reaction 6.3, /Delta1 r ν = -2 and RT /Delta1 r ν = -4.96 kJ mol -1 ( T = 298.15 K).

<!-- formula-not-decoded -->

The 'classical' calorimetric methods addressed in chapters 7-9, 11, and 12 were designed to study thermally activated processes involving long-lived species. As discussed in chapter 10, some of those calorimeters were modified to allow the thermochemical study of radiation-activated reactions. However, these photocalorimeters are not suitable when reactants or products are shortlived molecules, such as most free radicals. To study the thermochemistry of those species, the technique of photoacoustic calorimetry was developed (see chapter 13). It may be labeled as a nonclassical calorimetric technique because it relies on concepts that do not fit into the classification schemes just outlined.

Thethermochemistryofbothlong-andshort-lived molecules can be examined through the methods described in the last three chapters of part II, namely, equilibrium , kinetic , and electrochemical methods . Equilibrium and kinetic studies in solution are widely used in thermochemistry, and both rely on the determination of molar concentrations by suitable analytical techniques. Electrochemical methods have a somewhat wider scope, providing information about the energetics of both neutral and ionic species in solution.

## Combustion Calorimetry

Calorimetric studies of combustion reactions in oxygen and fluorine atmospheres have been a major source of enthalpy of formation data, particularly for organic and inorganic compounds.

As referred to in the previous chapter, in bomb combustion calorimetry the reaction proceeds inside a pressure vessel-the bomb-at constant volume, and in this case the derived quantity is /Delta1 c U o . In flame calorimetry the reaction occurs in a combustion chamber, which is in communication with the atmosphere, and the measurements lead to /Delta1 c H o . The methods of combustion calorimetry will be described in the following paragraphs.

'Conventional' combustion calorimeters operate on a 'macro' scale, that is, they require samples of 0.5-1.0 g per experiment. Unfortunately, many interesting compounds are available only in much smaller amounts. In the case of oxygen combustion calorimetry, however, several combustion microcalorimeters that only demand 2-50 mg samples have been developed in recent years. The achievements and trends in this area through 1999 have been reviewed [710], and interested readers are directed to these publications. Since then, a few new apparatus have been reported [11-17]. Nevertheless, it should be pointed out that the general principles and techniques used to study compounds at the micro scale are not greatly different from those used in macro combustion calorimetry.

## 7.1 STATIC-BOMB COMBUSTION CALORIMETRY IN OXYGEN

Static-bomb combustion calorimetry is particularly suited to obtaining enthalpies of combustion and formation of solid and liquid compounds containing only the elements C, H, O, and N. The origins of the method can be traced back to the work of Berthelot in the late nineteenth century [18,19].

Most static-bomb calorimeters used are of the isoperibol type, such as the one in figure 7.1. Here, the bomb A is a pressure vessel of ∼ 300 cm 3 internal volume. Combustion bombs are usually made of stainless steel and frequently have an internal platinum lining to prevent corrosion. In a typical high-precision experiment, the platinum ignition wire B connects the two electrodes C, which are affixed to the bomb head. A cotton thread fuse D (other materials such as polyethene are also used), of known energy of combustion, is weighed to a precision of ± 10 -5 -10 -6 g and tied to the platinum wire. A pellet E of the compound

Figure 7.1 Scheme of a macro static-bomb isoperibol combustion calorimeter (see text).

<!-- image -->

( ∼ 1.0 g) is placed inside the platinum crucible F, after being weighed to a precision of ± 10 -5 -10 -6 g. The crucible is supported by the ring G, and the cotton thread fuse is placed in contact with the pellet of the compound without touching the sides of the crucible. Deionized water is added to the bomb body (typically 0.3 cm 3 per 100 cm 3 of internal bomb volume) to maintain an H2O saturated vapor phase throughout the experiment, so that liquid water is formed in the combustion reaction. The bomb is closed and purged by charging it with very pure oxygen at a pressure of 1.01 MPa and then venting the overpressure (this operation is done twice to remove nitrogen present as air, which also participates in the combustion process). After purging, the bomb is finally charged with oxygen, usually at a pressure of 3.04 MPa and T = 298.15 K, and a few minutes are allowed for equilibration before closing the gas inlet valve H. The bomb is transferred to the inside of the calorimeter proper I, the electrical connections J of the firing circuit are attached to the bomb head, and the calorimeter proper is filled with a weighed amount of distilled water. The calorimeter proper is closed and placed inside the thermostated jacket K, where the temperature is controlled, usually at T ≈ 298 K, to a precision of ± 10 -3 K or better. The stirrer L of the calorimeter proper is started, and the system is left to equilibrate. The temperature of the calorimeter proper is monitored as a function of time by means of a thermometer M, with a resolution of ± 10 -4 K or better (usually a platinum resistance thermometer, a quartz-crystal thermometer, or a thermistor). The reaction is initiated by the discharge of a capacitor through the platinum wire B, which ignites the cotton thread fuse D and subsequently the sample E. From the temperature-time data acquired during the experiment, it is

possible to derive the adiabatic temperature rise /Delta1 T ad , which corresponds to the temperature change that would have been observed if the calorimeter proper were an adiabatic system. This calculation affords the reaction initial, T i , and final, T f , temperatures, and a correction, /Delta1 T corr , due to the nonadiabaticity of the process. The reason for obtaining these parameters will be apparent shortly.

In the bomb process, reactants at the initial pressure p i and temperature T i are converted to products at the final pressure p f and temperature T f . The primary goal of a combustion calorimetric experiment, however, is to obtain the change of internal energy, /Delta1 c U o ( T R ) , associated with the reaction under study, with all reactants and products in their standard states ( p i = p f = 0.1MPa ) and under isothermal conditions at a reference temperature T R (usually 298.15 K). Once /Delta1 c U o ( 298.15K ) is known, it is possible to derive the standard enthalpy of combustion, /Delta1 c H o ( 298.15K ) , and subsequently calculate the standard enthalpy of formation of the compound of interest from the known standard enthalpies of formation of the products and other reactants.

Note that in addition to the main reaction, the bomb process includes contributions from ignition and all side reactions. These contributions have to be included in the calculation of the energy change associated with the main reaction. Two side reactions normally considered are the combustion of the cotton fuse and the formation of nitric acid from the oxidation of traces of atmospheric N2 that remain inside the bomb even after purging.

As mentioned, the addition of a small amount of water to the bomb ensures that the vapor phase remains saturated throughout the experiment, so that liquid water is produced in the combustion reaction. It also ensures that the mixture of nitric oxides formed by the oxidation of the N2 will be converted to NO -3 (aq), which is simple to determine.

The calculation of /Delta1 c U o ( 298.15K ) from the experimental data involves the following steps: (1) determination of /Delta1 T ad ; (2) calculation of the internal energy change associated with the bomb process under isothermal bomb conditions at 298.15 K ( /Delta1 U IBP, equation 7.1); (3) reduction of /Delta1 U IBP to the standard state, also known as the Washburn corrections after E. W . Washburn, who first proposed them in 1933 [20]; (4) subtraction of the energy contributions from all side reactions included in the bomb process from the standard state /Delta1 U o IBP value.

<!-- formula-not-decoded -->

## Determination of /Delta1 T ad

The basic output from a combustion experiment made with an isoperibol calorimeter is a temperature-time curve, such as the one represented in figure 7.2. In the initial or fore period (between t a and t i ) and in the final or after period (between t f and t b ) , the observed temperature change is governed by the heat of stirring, the heat dissipated by the temperature sensor, and the heat transfer between the calorimeter proper and the jacket. The reaction or main period begins at t i, when, on ignition, a rapid temperature rise results from the exothermic

Figure 7.2 A typical temperature-time curve from a combustion reaction studied with an isoperibol combustion calorimeter.

<!-- image -->

combustion reaction. In figure 7.2, T j represents the temperature of the thermostat jacket (which is a heat sink), and T ∞ is the temperature that the calorimeter proper would attain if the final period were extended indefinitely. Note that T ∞ is higher than T j due to the heat of stirring and the heat dissipated by the temperature sensor.

The observed temperature change of the calorimeter proper during the main period, T f -T i, is not exclusively determined by the amount of heat released in the bombprocess. It is also due to the heat exchanged with the surroundings, the heat of stirring, and the heat dissipated by the temperature sensor. The observed temperature change must therefore be corrected for these contributions by an amount represented by /Delta1 T corr in equation 7.2 to obtain the adiabatic temperature rise:

<!-- formula-not-decoded -->

A number of procedures have been developed to evaluate /Delta1 T ad [21-34]. The most widely used, which is discussed in this section, is known as the RegnaultPfaundler method.

In well-designed isoperibol calorimeters, the heat transfer between the calorimeter proper and the jacket takes place according to Newton' s law, with conduction being the dominant mechanism [3,21,35-38]. In this case, the rate of temperature change during the initial and final periods, g , is given by

<!-- formula-not-decoded -->

where T is the temperature of the calorimeter proper at a given time t , T j is the jacket temperature, k is the cooling constant, and u represents the sum of all constant secondary thermal effects due to the heat of stirring, Joule (resistive) heating by the temperature sensor, and so on. When T = T ∞ , dT / dt = 0 and equation 7.3 leads to

<!-- formula-not-decoded -->

Introducing this result in equation 7.3 we obtain

<!-- formula-not-decoded -->

Thevalueof /Delta1 T corr in equation 7.2 can be calculated by integration of equation 7.5 over the reaction period:

<!-- formula-not-decoded -->

where T m is the average temperature of the calorimeter proper within this period, which is given by

<!-- formula-not-decoded -->

The value of T m can be found by using any standard procedure for numerical integration of equation 7.7. If n values of T are acquired at constant time intervals /Delta1 t during the reaction period, the trapezoidal equation 7.8 can be used:

<!-- formula-not-decoded -->

The maximum permissible value of /Delta1 t may vary for different calorimetric experiments. Typically, /Delta1 t ≤ 15 s.

To calculate /Delta1 T ad from equations 7.2, 7.6, and 7.8, it is therefore necessary to determine t i , t f , T i , T f , k , and T ∞ . The ignition time, t i, is defined by the operator. The value of t f is empirically obtained, based on the criterion that /Delta1 T ad becomes constant for t &gt; t f . The smallest t f value that gives the limiting /Delta1 T ad should be chosen.

Thevalues of k , T ∞ , T i, and T f can be obtained from the temperature-time data for the initial and final periods. Integration of equation 7.5 over these periods gives

<!-- formula-not-decoded -->

where T 0 is the temperature reading for t = 0 (i.e., T 0 = T a in the initial period and T 0 = T f in the final period). A power-series expansion of the exponential function in equation 7.9 leads to

<!-- formula-not-decoded -->

If kt /lessmuch 1, the terms in k 2 t 2 and higher can be neglected, yielding a linear relation of slope g = k ( T ∞ -T 0 ) (see also equation 7.5):

<!-- formula-not-decoded -->

The hypothesis kt /lessmuch 1 is frequently confirmed in practice, that is, the temperature-time variations in the initial and final periods are well represented

by equation 7.11. In these cases, it is common to calculate T i , T f , k , and T ∞ as follows. First, equations 7.12 and 7.13,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

are fitted to the experimental data of the fore and after periods, respectively, yielding the slopes g i and g f . The obtained correlations are then used to calculate the values of T i and T f from the corresponding values of t i and t f , and also the values of the temperatures T i and T f corresponding to the midpoints of the initial and final periods, t i and t f , respectively. If k and T ∞ are identical for the initial and final periods, it can be concluded from equation 7.5 that

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equations 7.14 and 7.15 lead to the values of k and T ∞ , which are needed to derive T m, /Delta1 T corr, and /Delta1 T ad from equations 7.8, 7.6, and 7.2, respectively.

When significant curvature of the initial and final periods is observed, k , T ∞ , T i, and T f should be determined by fitting equation 7.9 to the experimental data (see, e.g., [30-33]). The fitting can be made according to the following iterative method. (1) An approximate value for the cooling constant k is obtained based on equations 7.12-7.14. (2) This value is used to determine T ∞ and T f from a least squares fit of the final period data to a plot of T versus exp ( -kt ) . (3) The value of k is refined by fitting the equation

<!-- formula-not-decoded -->

to the initial period data, using the T ∞ value obtained in step 2. (4) Steps 2 and 3 are repeated until a negligible difference between two successive values of T ∞ is obtained. The values of T i and T f are derived from the accepted correlations, and /Delta1 T ad is finally calculated as described.

## Calculation of /Delta1 U IBP at 298.15 K: Calibration

The strategy used to derive /Delta1 U IBP at 298.15 K from the internal energy change of the actual bomb process, /Delta1 U exp, is summarized in the thermodynamic cycle of figure 7.3. It is assumed that first the temperature of the calorimeter is changed from 298.15 K to T i, with a corresponding energy variation of /Delta1 U 1. The bomb process is started at T i, and the temperature of the system rises from T i to T f . This step is accompanied by the internal energy change /Delta1 U exp. The system is finally brought from T f to 298.15 K, the corresponding internal energy change and

Figure 7.3 General scheme of the calculation of /Delta1 U IBP at 298.15 K from the internal energy change of the actual bomb process, /Delta1 U exp .

<!-- image -->

being /Delta1 U 2. The values of /Delta1 U 1, /Delta1 U exp, and /Delta1 U 2 are given by

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In these equations, /Delta1 U ign is the energy supplied for ignition, which is given by

<!-- formula-not-decoded -->

where C is the capacitance of the condenser, V i is the initial potential of the condenser, and V f is the potential of the condenser after discharge. The terms (ε o + ε ci ) and (ε o + ε cf ) represent the energy equivalent of the calorimetric system in the initial and final states, respectively. According to normal practice they are given as a sum of two parts. The first, ε o, corresponds to the bulk calorimeter proper, which remains unchanged in all experiments (the calorimeter can with a fixed amount of water plus the bomb with its permanent fittings, such as the electrodes, the thermometer, heating and cooling devices, etc.) and must be found by calibration. The second part, ε ci or ε cf , corresponds to the sum of heat capacities of the bomb contents (sample, gases, bomb solution, Pt fuse wire, crucible, and other nonpermanent fittings) and can be calculated for each experiment as described below. The heat capacities of the contents vary between the initial ( ε ci ) and the final state ( ε cf ) as a result of the chemical changes taking place inside the bomb.

It should be noted that if the process under study took place under perfect adiabatic conditions and if no work of any type was done on the system by the surroundings, then /Delta1 U exp = 0. Under isoperibol operation, however, the heat exchanged with the surroundings, ( ε o + ε cf )/Delta1 T corr, and the energy supplied for ignition, /Delta1 U ign, have to be considered as indicated in equation 7.18. Other contributions such as those due to heat dissipation in the temperature sensor or stirring are kept as small and constant as possible by design and, as described in the previous section, are accounted for in the calculation of /Delta1 T corr .

Because /Delta1 U IBP = /Delta1 U 1 + /Delta1 U exp + /Delta1 U 2, equations 7.17-7.19 lead to

<!-- formula-not-decoded -->

The determination of T i , T f , and /Delta1 T corr has been described in the previous section. As mentioned, the energy equivalent of the calorimeter ε o can be obtained by calibration. Each calibration experiment also requires the recording of a temperature-time curve such as that in figure 7.2.

In the case of an electrical calibration, at the beginning of the main period a potential V is applied to a resistance inside the calorimeter proper, causing a current of intensity I to flow over a period t . As a result, an amount of heat Q = VIt is dissipated in the calorimeter proper, causing the observed temperature rise. If the calibration is carried out on the reference calorimeter proper (without 'contents'), then ε ci = ε cf = 0 and the internal energy change of the calorimetric system during the main period is

<!-- formula-not-decoded -->

Rearranging equation (7.22) it can be concluded that

<!-- formula-not-decoded -->

The energy equivalent of the calorimeter, ε o, can therefore be calculated from equation 7.23 after determination of the corresponding adiabatic temperature rise.

Alternatively, the combustion of a certified reference material can be used. Since 1934, benzoic acid has been the internationally accepted primary standard material for determination of the energy equivalent of oxygen-bomb calorimeters [39,40]. In this case,

<!-- formula-not-decoded -->

where m (BA) is the mass of benzoic acid burned; /Delta1 c u ( BA ) is the massic energy of combustion of benzoic acid at 298.15 K and under the conditions of the actual bomb process; ∑ i /Delta1 c U i is the energy associated with all side reactions at 298.15 K; and /Delta1 U ign is the energy of the ignition process. Equation 7.24 is readily deduced from equation 7.21 by noting that in the calibration process /Delta1 U IBP = m ( BA ) [ /Delta1 c u ( BA ) ] + i /Delta1 c U i .

∑ The energy of combustion of benzoic acid determined by standardizing laboratories normally refers to the following certification conditions [21,25,39-43]: (1) The benzoic acid sample is burned in a bomb at constant volume, in pure oxygen at an initial pressure of 3.04 MPa; (2) the mass of sample burned, expressed in grams, is equal to three times the internal volume of the bomb in dm 3 ; (3) the amount of water inside the bomb, expressed in grams, is also equal to three times the internal volume of the bomb in dm 3 ; (4) the combustion reaction is referred to 298.15 K. If calibrations are not made strictly under the certification conditions, the value of /Delta1 c u ( BA ) under the actual bomb conditions should

be determined from /Delta1 c u ( BA,cert ) , the energy of combustion of benzoic acid under standard certificate conditions. For relatively small departures from these certificate conditions, the correction proposed by Jessup [41] can be used:

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

In equation 7.26, p represents the initial pressure (expressed in MPa), V is the bomb volume (in dm 3 ) , m ( BA ) is the mass of benzoic acid (in g), m ( H2O) is the mass of water initially placed inside the bomb (in g), and T R is the temperature to which the combustion reaction is referred (in K). As mentioned, equation 7.26 is strictly applicable for relatively small departures from certification conditions. The maximum error in f will not exceed 1.5 × 10 -5 if p , m (BA )/ V , m ( H2O) / V , and T R are, respectively, in the following ranges: 2.03-4.05 MPa, 2-4 g dm -3 , 2 -4 g dm -3 , and 293.15-303.15 K [21,25,39,41-43].A better alternative, which is also valid for larger departures from the certification conditions, consists in (1) calculating the standard massic energy of combustion of the reference material, /Delta1 c u o ( BA ) , by reduction to standard states of the certification condition value, /Delta1 c u ( BA, cert ) ; (2) deriving the corresponding massic energy of combustion under the actual bomb conditions, /Delta1 c u ( BA ) , by applying the reduction to standard states in reverse to /Delta1 c u o ( BA ) :

<!-- formula-not-decoded -->

For the certification conditions indicated, /Delta1 c u o ( BA) -/Delta1 c u ( BA,cert) = 20.4 Jg -1 [42].

Electrical calibration has the advantage of being more flexible. It can afford ε o through equation 7.23 if it is done on the reference calorimeter proper. However, it can also be performed on the initial or final state of the actual experiment leading to ( ε o + ε ci) or ( ε o + ε cf ), respectively. Twenty or 30 years ago the electrical calibration required very expensive instrumentation that was not readily available except in very specialized places, such as the national standards laboratories. Although the very accurate electronic instrumentation that is available today at moderate prices may change the situation, most users of combustion calorimetry still prefer to calibrate their apparatus with benzoic acid.

Typically, for the combustion of benzoic acid the terms ε ci and ε cf can be derived from equations 7.27 and 7.28, respectively. Similar equations can be employed for other types of combustion reactions.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In equations 7.27 and 7.28 m ( BA), m ( cot), m ( crbl), and m ( wr) are the masses of benzoicacidsample,cottonthreadfuse,platinumcrucible,andplatinumfusewire initially placed inside the bomb, respectively; n (O 2 ) is the amount of substance of oxygen inside the bomb; n (CO 2 ) is the amount of substance of carbon dioxide formed in the reaction; /Delta1 m ( H2O) is the difference between the mass of water initially present inside the calorimeter proper and that of the standard initial calorimetric system; and cV (BA), cV (Pt), cV (cot), CV (O 2 ), and CV (CO 2 )are the heat capacities at constant volume of benzoic acid, platinum, cotton, oxygen, and carbondioxide,respectively.The terms ε i ( H2O)and ε f (sln) represent the effective heat capacities of the two-phase systems present inside the bomb in the initial state (liquid water + water vapor) and in the final state (final bomb solution + water vapor), respectively. In the case of the combustion of compounds containing the elements C, H, O, and N, at 298.15 K, these terms are given by [44]

<!-- formula-not-decoded -->

where B = 2301.2 J K -1 mol -1 and A is expressed in J K -1 g -1 :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In equations 7.29-7.31, m i (H 2 O,tot) and n i (H 2 O,g) are the total mass of water and the amount of substance of gaseous water initially present inside the bomb, respectively; m f ( H2O,g ) and n f (H 2 O,g) are the mass and amount of substance of gaseous water in the final state; m f ( sln) is the mass of the final bomb solution; and w ( HNO3 ) represents the mass fraction of HNO3 (in percentage) in solution. As indicated, due to a secondary combustion reaction, aqueous HNO3 almost always exists in the final state.

The calculation of ε ci and ε cf may involve more or fewer terms than those included in equations 7.27 and 7.28, depending on the particular calorimetric system used and on the reaction studied.

The values of (ε o + ε ci ) and (ε o + ε cf ) are slightly temperature-dependent. To ensure that they can be transferred from the calibration to the main experiment, it is convenient for T i and T f (figure 7.2) to be as close as possible in both runs. Aiming to keep the error due to differences in these values below 0.01%, it is recommended that [42]

<!-- formula-not-decoded -->

∣

∣

and

## The Correction of /Delta1 UIBP to the Standard State (Washburn Corrections)

<!-- formula-not-decoded -->

Thenature of theWashburn corrections is illustrated by the thermochemical cycle in figure 7.4. It can be concluded from this cycle that

<!-- formula-not-decoded -->

where /Delta1 U W = /Delta1 U Wi + /Delta1 U Wf corresponds to the sum of all energy changes associated with the Washburn corrections.

It should be noted that the reaction under consideration (to be reduced to standard states) is the net process occurring inside the bomb. This includes the main reaction and all secondary reactions. All these are brought to their standard states at the reference temperature of 298.15 K. The standard state energy of combustion of the main reaction at 298.15 K is obtained by subtracting the standard state energies of all side reactions from /Delta1 U o IBP .

A detailed scheme for calculating the Washburn corrections in experiments with organic compounds of general formula CaHbOcNd has been published [45,46]. The scheme is shown in figures 7.5 and 7.6. It is immediately apparent that it involves quite lengthy (and maybe confusing!) mass and energy balances. A step-by-step analysis of the Washburn corrections for one of the combustion experiments on 4-cyanopyridine N-oxide (C6H4ON2) carried out by Ribeiro da Silva et al. [47] will be described next, to illustrate the calculation sequence and the relative magnitude of the various internal energy changes indicated in figures 7.5 and 7.6. The mass balance part of the Washburn corrections will not be given here; interested readers are referred to the more specialized literature [45,46]. The calculated masses and amounts of substance of the species

Figure 7.4 Reduction of combustion calorimetric results to standard states.

<!-- image -->

Figure 7.5 General scheme of the initial-state Washburn corrections for a combustion reaction involving a Ca H b O c N d compound.

<!-- image -->

relevant to this particular example are given in table 7.1, along with other auxiliary data [45,47-53]. The values of the internal energy changes associated with each step of the Washburn corrections are discussed below and collected in table 7.2.

The solid 4-cyanopyridine N-oxide was burned in pellet form. To avoid incomplete combustion, it was necessary to burn the compound in conjunction with n -hexadecane. The bomb of 340 cm 3 internal volume was charged

Figure 7.6 General scheme of the final-state Washburn corrections for a combustion reaction involving a Ca H b O c N d compound.

<!-- image -->

with 3.04 MPa of oxygen and contained 1 cm 3 of water. The reaction was started at 298.15 K by discharging a 700 µ F capacitor through a platinum wire, which ignited a cotton thread fuse and subsequently the sample (4-cyanopyridine N-oxide plus n -hexadecane). In the experiment under discussion, the substance in figure 7.5, which we denote by CaHbOcNd, consisted of 0.40611 g of 4-cyanopyridine-N-oxide, 0.21835 g of n -hexadecane (C16H34), and 0.00377 g of cotton thread (CH1.686O0.843 ) . The standard massic energies of combustion of the n -hexadecane and the cotton had been previously determined (table 7.1).

Table 7.1 Auxiliary data for the Washburn corrections associated with the combustion of 4-cyanopyridine N-oxide (see text and figures 7.5 and 7.6)

## Results of the Mass Balance

<!-- formula-not-decoded -->

Initial State

<!-- formula-not-decoded -->

Final State

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Compression Terms

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

( w = mass fraction of HNO 3 , in percentage) [52]

Internal Energy Changes at 298.15 K

/Delta1

vap

/Delta1

sln

U

U

/Delta1

sln

/Delta1

(H 2 O)

(O 2 )

U

dil

U

/Delta1

dec

/Delta1

41511 J mol

J mol

=

/

-

1

-

1

[53]

= -

13388.8 + 2217.5[

(CO 2 )

/

J mol

(HNO 3 , aq)

U

(HNO 3 , aq)

c

u

o (aux)

1

c

16945.2 + 836.8[

=

= -

-

53.843 J mol

(HNO 3 , aq)/(mol dm

c

1

[45]

=

-

59700 J mol

= -

47156.9

±

1.2 J g

-

[45]

[47]

1

1

-

-

(HNO 3 , aq)/(mol dm

c

u

-

3 )] [45]

3 )] [45]

o (fuse)

= -

16250 J g

-

1

[47]

/Delta1

Table 7.2 Washburn corrections for the combustion of 4-cyanopyridine N-oxide (see text and figures 7.5 and 7.6)

|      | Initial State         | Final State            | Final State            |
|------|-----------------------|------------------------|------------------------|
| Step | /Delta1 U / J         | Step                   | /Delta1 U / J          |
| 1    | - 0.465               | 10                     | 1.821                  |
| 2    | 4.515 × 10 - 5        | 11                     | 0                      |
| 3    | 19.838                | 12                     | 0.551                  |
| 4    | 7.812 × 10 - 2        | 13                     | 0                      |
| 5    | 0                     | 14                     | 0.369                  |
| 6    | 0                     | 15                     | 3.842 × 10 - 2         |
| 7    | - 83.513              | 16                     | 42.602                 |
| 8    | - 0.223               | 17                     | 0                      |
| 9    | - 0.466               | 18                     | 0                      |
|      |                       | 19                     | 93.959                 |
|      |                       | 20                     | 0                      |
|      |                       | 21                     | 0                      |
|      |                       | 22                     | 0                      |
|      |                       | 23                     | - 7.970 × 10 - 2       |
|      |                       | 24                     | - 20.241               |
|      |                       | 25                     | - 4.606 × 10 - 5       |
|      |                       | 26                     | 0                      |
|      | /Delta1 U Wi 64.751 J | /Delta1 U Wf 119.020 J | /Delta1 U Wf 119.020 J |

= -

=

Confirmation that complete combustion had been attained was made by gravimetric analysis of the CO2 formed in the reaction [54]. The final bomb gases were discharged through a sequence of three tubes, the first containing magnesium perchlorate, for removing water, and two others containing ascarite (sodium hydroxide on asbestos), which quantitatively absorbs carbon dioxide.The mass of CO2 wasevaluated from the increase in mass of the tubes containing ascarite [54]. In the present example, the ratio of the mass of CO2 produced by the combustion of 4-cyanopyridine N-oxide, the cotton thread fuse, and n -hexadecane, to the mass of CO2 expected on the basis of the masses of those substances burned was 1.0000.

For any C, H, O, N compound, the standard state combustion reaction is

<!-- formula-not-decoded -->

The Washburn corrections for the initial state, /Delta1 U Wi (figure 7.5) correspond to the energy changes for bringing the bomb contents from their standard state to the initial bomb conditions. The traces of N2 inevitably present as an impurity in the O2 are ignored in the computation.

Step 1

The substance in its standard state at 298.15 K is compressed from the standard state pressure p o = 0.1 MPa to the initial pressure p i = 3.04 MPa. The change of internal energy is given by

<!-- formula-not-decoded -->

where m represents the mass and ′ , ′′ , and ′′′ refer to 4-cyanopyridine N-oxide, n -hexadecane, and cotton, respectively. From the data in table 7.1, it can be calculated that /Delta1 U 1 = -0.465 J (table 7.2).

Steps 2-4

Part of the liquid water introduced into the bomb in its standard state at 298.15 K is first isothermally decompressed from 0.1 MPa to its saturation pressure, p sat , vaporized, and finally decompressed from p sat to a negligibly small pressure ( p = 0 ) . The corresponding changes of internal energy are

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where n i ( H2O, g)is the amount of substance of water that undergoes vaporization. As indicated in table 7.2, in this case, /Delta1 U 2 = 4.515 × 10 -5 J, /Delta1 U 3 = 19.838 J, and /Delta1 U 4 = 7.812 × 10 -2 J. The two decompression terms are negligible and, in practice, only /Delta1 U 3 needs to be considered in the calculation.

Step 5

The oxygen contained inside the bomb, in the ideal gas state at 298.15 K, is decompressed from 0.1 MPa to a negligibly small pressure: /Delta1 U 5 = 0.

Step 6

Part of the O2 gas from step 5, n i ( O2, g), is mixed with the gaseous water from step 4, n i ( H2O, g), at 298.15 K and at a negligibly small pressure: /Delta1 U 6 = 0.

Step 7

The mixture of step 6, n i ( gas) = n i ( O2, g) + n i ( H2O, g), is compressed within the bomb volume available for the gas phase from p = 0 to the pressure p i = 3.04 MPa. The effect of the small concentration of H2O vapor can be neglected, and the corresponding change of internal energy is

<!-- formula-not-decoded -->

In the current example, /Delta1 U 7 = -83.513 J.

Step 8

n i ( H2O, l) moles of liquid water are compressed from 0.1 MPa to the initial pressure p i = 3.04 MPa. The corresponding energy change is given by

<!-- formula-not-decoded -->

In our example, /Delta1 U 8 = -0.223 J.

Step 9

n i ( O2, sln) moles of gaseous oxygen are dissolved in the liquid water. The corresponding energy change is

<!-- formula-not-decoded -->

In the present example, /Delta1 U 9 = -0.466 J.

Step 9 completes the Washburn corrections for bringing the reactants to the initial bomb conditions:

<!-- formula-not-decoded -->

The bomb process is then considered to occur isothermally at 298.15 K, with a corresponding energy change /Delta1 U IBP ( 298.15 K). In the final state the bomb contents are a gaseous mixture of O2, N2, CO2, and H2O, and an aqueous solution of O2, N2, CO2, and HNO3 (figure 7.6). The Washburn corrections for the final state include the following steps.

As shown in table 7.2, /Delta1 U Wi = -64.751 J is obtained.

Steps 10 and 11

The dissolved CO2 is allowed to escape from the aqueous phase and expand to a negligibly small pressure and is subsequently compressed as an ideal gas to the standard state pressure.

<!-- formula-not-decoded -->

In the present example /Delta1 U 10 = 1.821 J and /Delta1 U 11 = 0.

Steps 12 and 13

The dissolved O2 and N2 are allowed to escape from the liquid phase, decompressed to a negligibly small pressure ( p = 0), and finally compressed as an ideal gas mixture to the standard state pressure. The (O2 + N2 ) mixture is treated as if it were pure O2 (the amount of N2 is very small and the internal energies of solution of O2 and N2 are very similar [55]) and the energy changes associated with steps 12 and 13 are

<!-- formula-not-decoded -->

In this case /Delta1 U 12 = 0.551 J and /Delta1 U 13 = 0.

Step 14

The remaining aqueous HNO3 solution is decompressed from p f to 0.1 MPa. The corresponding energy change is given by

<!-- formula-not-decoded -->

and in our example /Delta1 U 14 = 0.369 J.

Step 15

The aqueous HNO3 solution is diluted (or concentrated) to 0.1 mol dm -3 :

<!-- formula-not-decoded -->

This yields /Delta1 U 15 = 3.842 × 10 -2 J.

Step 16

The aqueous nitric acid at a concentration of 0.1 mol dm -3 is decomposed at 0.1 MPa and 298.15 K, according to the reaction

<!-- formula-not-decoded -->

The internal energy of reaction 7.48 is given by

<!-- formula-not-decoded -->

and /Delta1 U 16 = 42.602 J.

Steps 17 and 18

The (O2 + N2 ) (g) and H2O(l) of step 16 are added to the remaining standard state (O2 + N2 ) (g) and H2O(l) inside the bomb. There are no changes of internal energy in these steps: /Delta1 U 17 = /Delta1 U 18 = 0.

Step 19

The gaseous phase containing O2, N2, CO2, and H2O is expanded to a negligibly small pressure. The change of internal energy is given by

<!-- formula-not-decoded -->

where x denotes mole fraction. In this case /Delta1 U 19 = 93.959 J.

Steps 20-22

The gaseous mixture is separated to CO2, (O2 + N2 ) , and H2O, and each component is brought to its standard state. There is no internal energy change in these steps.

Steps 23-26

The water vapor is compressed to its saturation pressure, condensed to liquid, compressed to 0.1 MPa, and finally added to the remaining liquid water inside the bomb.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where n f ( H2O, g) is the amount of substance of water that undergoes condensation. As indicated in table 7.2, in this case /Delta1 U 23 = -7.970 × 10 -2 J, /Delta1 U 24 = -20.241 J, /Delta1 U 25 = -4.606 × 10 -5 J, and /Delta1 U 26 = 0. Note that the two compression terms are always negligible, and in practice, only /Delta1 U 24 needs to be considered in the calculation.

Step 26 completes the Washburn corrections that bring the products from the final bomb conditions to their standard states. For our example,

<!-- formula-not-decoded -->

It is observed in table 7.2 that the most important terms in the reduction to standard states are the decomposition of aqueous nitric acid ( /Delta1 U 16), the compression of the initial gaseous phase (O2 + H2O)fromanegligibly small pressure to the initial pressure ( /Delta1 U 7 ) , the decompression of the final gaseous phase (O2 + N2 + CO2 + H2O) from the final pressure to a negligibly small pressure ( /Delta1 U 19 ) , and the evaporation of CO2 from the final aqueous phase ( /Delta1 U 10). The terms relative to the vaporization and condensation of liquid water ( /Delta1 U 3 -/Delta1 U 24) almost cancel out.

As shown in table 7.2, /Delta1 U Wf = 119.019 J.

It is common practice to separate the term relative to the decomposition of nitric acid from all other Washburn corrections, usually represented by /Delta1 U W. The net correction is denoted by /Delta1 U /Sigma1 :

<!-- formula-not-decoded -->

In our example, /Delta1 U /Sigma1 = 11.7 J.

## Final Results and Assignment of Uncertainties

Once the values of /Delta1 U IBP and /Delta1 U /Sigma1 are known, the standard massic energy of combustion of 4-cyanopyridine N-oxide can be derived from

<!-- formula-not-decoded -->

] where /Delta1 c u o ( aux ) and /Delta1 c u o ( fuse ) are the standard massic energies of combustion of n -hexadecane and the cotton fuse, respectively; /Delta1 dec U o ( HNO3 ) is the

standard molar energy of decomposition of HNO3 ( aq, 0.1 mol dm -3 ) , according to equation 7.48; and finally, m f ( C ) is the mass of carbon soot formed if incomplete combustion occurs (which is not the case in the present example) and /Delta1 c u o ( C ) = -33000 J g -1 [21] is the corresponding standard massic energy of combustion.

Table 7.3 shows a summary of the results of six independent combustion calorimetry experiments with 4-cyanopyridine N-oxide [47]. Note that the value of /Delta1 U ign, which represents the energy change associated with ignition (equation

7.20), is included in the value of /Delta1 U IBP.

The mean and standard deviation of the mean of the massic standard energy of combustion from the results in table 7.3 is /Delta1 c u o ( 4-CNPyNO ) = -25781.3 ± 3.4 Jg -1 . The corresponding standard molar energy of combustion is /Delta1 c U o ( 4-CNPyNO ) = -3096.6 ± 1.1 kJ mol -1 , where the error quoted is twice the overall uncertainty ( σ overall ) , which includes contributions from the calibration of the calorimeter with benzoic acid and the combustion of n -hexadecane. The value of σ overall is derived from [56,57]:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where σε , σ BA, σ aux, and σ cpd are the standard deviations of the mean of ε o, /Delta1 c u ( BA,cert ) , /Delta1 c u o ( aux ) , and /Delta1 c u o ( 4-CNPyNO ) , respectively; /Delta1 U IBP, /Delta1 U ( aux ) , and /Delta1 U ( 4-CNPyNO ) are the means of the corresponding individual values in table 7.3. For our example, ε o = 15911.2 ± 1.5 J K -1 [47], -/Delta1 c u ( BA,cert ) = 26431.8 ± 1.5 Jg -1 [47], -/Delta1 c u o ( aux ) = 47156.9 ± 1.2 J g -1 [47], -/Delta1 c u o ( 4-CNPyNO ) = 25781.3 ± 3.4 J g -1 , -/Delta1 U IBP = 19569.6 J, -/Delta1 U ( aux ) = 9149.0 J, and -/Delta1 U ( 4-CNPyNO ) = 10309.4 J. Therefore, from equation 7.57, σ overall = 4.49 J g -1 . The molar mass of 4-cyanopyridine N-oxide is 120.11064 g mol -1 , so the uncertainty associated with /Delta1 c U o ( 4-CNPyNO ) is 1

The mean value of the standard molar energy of combustion of 4-cyanopyridine N-oxide indicated refers to reaction 7.58 at 298.15 K:

given by 2 σ overall = 1.1 kJ mol -.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In this case /Delta1 r ν = 0.5 mol (equation 6.2) and therefore /Delta1 r H o = /Delta1 r U o + 0.5 RT = -3095.4 ± 1.1 kJ mol -1 . Using /Delta1 f H o (CO 2 , g) = -393.51 ± 0.13 kJ mol -1 [58] and /Delta1 f H o (H 2 O, l) = -285.830 ± 0.040 kJ mol -1 [58], we finally 1

The standard enthalpy of sublimation of 4-cyanopyridine N-oxide was mea1

obtain /Delta1 f H o (4-CNPyNO, cr) = 162.7 ± 1.4 kJ mol -.

sured as /Delta1 sub H o (4-CNPyNO) = 104.4 ± 4.3 kJ mol -[47] by the drop

Table 7.3 Combustion of 4-cyanopyridine N-oxide (denoted by 4-CNPyNO) at T = 298.15 K and p o = 0.1 MPa

|                                         |      Run #1 |      Run #2 |      Run #3 |      Run #4 |      Run #5 |      Run #6 |
|-----------------------------------------|-------------|-------------|-------------|-------------|-------------|-------------|
| m ′ (4-CNPyNO)/g                        |     0.40611 |     0.40226 |     0.39969 |     0.34306 |     0.42907 |     0.41911 |
| m ′′ (aux)/g                            |     0.21835 |     0.07456 |     0.21762 |     0.25192 |     0.24295 |     0.15867 |
| m ′′′ (fuse)                            |     0.00377 |     0.00411 |     0.00367 |     0.0034  |     0.00343 |     0.00303 |
| 10 4. n f (HNO 3 )/mol                  |     7.136   |     6.801   |     6.901   |     7.069   |     7.504   |     6.851   |
| /Delta1 m (H 2 O / )g                   |     0.1     |     0.2     |     0       |    -0.1     |     0       |     0       |
| ε ci / (J K - 1 )                       |    15.15    |    15.15    |    15.14    |    15.47    |    15.55    |    15.35    |
| ε cf / (JK - 1 )                        |    15.79    |    15.34    |    15.79    |    16.18    |    16.27    |    15.83    |
| T i / K                                 |   298.152   |   298.151   |   298.152   |   298.151   |   298.151   |   298.151   |
| T f / K                                 |   299.55    |   299.136   |   299.544   |   299.553   |   299.656   |   299.413   |
| /Delta1 T ad / K                        |     1.31131 |     0.8791  |     1.29845 |     1.30816 |     1.42076 |     1.15434 |
| /Delta1 U ign / J                       |     1       |     1       |     1.1     |     1.1     |     1.2     |     1       |
| - /Delta1 U IBP / J                     | 20884.8     | 14000.8     | 20679.3     | 20833.9     | 22627.9     | 18384.2     |
| /Delta1 U /Sigma1 / J                   |    11.7     |     9.6     |    11.5     |    10.6     |    12.5     |    11.1     |
| /Delta1 dec U (HNO 3 ) / J              |    42.6     |    40.6     |    41.2     |    42.2     |    44.8     |    40.9     |
| - /Delta1 U (C)                         |     0       |     6.6     |     0       |     0       |     0       |     0       |
| - /Delta1 c U (aux) / J                 | 10296.7     |  3516       | 10262.3     | 11879.8     | 11456.8     |  7482.4     |
| - /Delta1 c U (fuse) / J                |    61.3     |    66.8     |    59.6     |    55.3     |    55.7     |    49.2     |
| - /Delta1 c U (4-CNPyNO) / J            | 10472.5     | 10374.4     | 10304.7     |  8846       | 11058.1     | 10800.6     |
| - /Delta1 c u o (4-CNPyNO) / (J g - 1 ) | 25787.3     | 25790.3     | 25781.7     | 25785.6     | 25772.3     | 25770.3     |

calorimetric method (see chapter 9), leading to /Delta1 f H o (4-CNPyNO, g) = 267.1 ± 4.5 kJ mol -1 [47]. This result permitted the N + -O -bond dissociation enthalpy in 4-cyanopyridine N-oxide to be determined; it corresponds to the enthalpy of the following reaction:

<!-- formula-not-decoded -->

DH o (N + -O -) = 265.6 ± 4.6 kJ mol -1 was calculated from the result for the standard enthalpy of formation of gaseous 4-cyanopyridine N-oxide, together with /Delta1 f H o (4-CNPy, g) = 283.5 ± 1.0 kJ mol -1 [59] and /Delta1 f H o (O, g) = 249.18 ± 0.10 kJ mol -1 [58]. The same approach was used by Ribeiro da Silva et al. to determine DH o (N + -O -) in other pyridine N-oxide derivatives [47].

## 7.2 MOVING-BOMB COMBUSTION CALORIMETRY IN OXYGEN

The final products of the combustion in a static bomb are usually very difficult to characterize for organic compounds containing sulfur, halogens, metals, and other elements different from C, H, O, and N. In the case of organosulfur compounds, for example, a mixture of sulfur dioxide, sulfur trioxide, and aqueous sulfuric acid (whose concentration varies throughout the bomb) is formed [60-62]. The composition of this mixture changes in each experiment and is virtually impossible to determine with good accuracy. Analogous situations occur in the combustion of fluorine-containing compounds, which may lead to HF and CF4 [61-63], and in the combustion of organochlorine and organobromine compounds, which produce mixtures of the free halogen and the halogen hydracid [61,62,64-66]. Organoiodine compounds, however, may in principle be studied by the static-bomb method because their combustion leads exclusively to the formation of I2 [61,62,67] (see following discussion). Table 7.4 shows typical mass fractions of the halogenated products found in the combustion of organohalogen compounds [42,64]. In static-bomb experiments involving organometallic compounds there is frequently the additional difficulty of achieving complete oxidation of the metal to a single well-defined oxide [68-72].

Table 7.4 Typical mass fractions, w , of the halogenated products found in the combustion of organohalogen compounds [42,64]

|    | w         | w         | w         |
|----|-----------|-----------|-----------|
| X  | HX        | X 2       | CX 4      |
| F  | 0.20-1.00 | 0.00      | 0.80-0.00 |
| Cl | 0.80-0.85 | 0.20-0.15 | 0.00      |
| Br | 0.03-0.10 | 0.97-0.90 | 0.00      |
| I  | 0.00      | 1.00      | 0.00      |

The attempts to overcome these problems led to the development of movingbomb calorimeters [19], following the pioneering work by Popoff and Schirokich in 1933 [73]. In most modern instruments of this type, such as the isoperibol calorimeter represented in figure 7.7, water or an aqueous reagent is initially placed inside the bomb. After extinction of the flame of the combustion reaction, the bomb is simultaneously rotated about its axial and longitudinal axes. The rotation causes efficient mixing of the bomb contents. In a well-designed experiment, a homogeneous solution is obtained in the final state and can be analyzed accurately.

The energy produced in the calorimeter proper as a result of friction in the rotating mechanism and stirring of the calorimetric liquid by the rotation of the bomb may be substantial.Y et provided that this effect is constant, its contribution to the energy of the calorimetric process can be accurately subtracted. If the bomb is rotated during the calibration and the sample runs, and if the rotation is started and ended at the same instants of the respective main periods, then the energy

Figure 7.7 Scheme of an isoperibol macro rotating-bomb combustion calorimeter. A: calorimeter proper; B: bomb; C: thermostatic bath; D: motors for rotation of the bomb; E: drive shaft; F: stirrer of the calorimeter proper; G: motor that drives the stirrer F; H: motor that drives the stirrer of the thermostatic bath; I: miter gear; J: gas outlet valve; K: gas inlet valve; L: crucible.

<!-- image -->

of rotation will be included in the energy equivalent of the calorimeter and will cancel out when both runs are compared. Alternatively, the experiment may be conducted so that the effect of the bomb rotation is automatically included in the calculation of the adiabatic temperature rise [23,25,28,74]. This can be achieved, for example, if the rotation is started during the reaction period at a time t s defined by [23,28,74]

<!-- formula-not-decoded -->

and maintained until the end of the final period. Here, T denotes the temperature of the calorimeter proper during the reaction period, which begins at time t i and temperature T i, and ends at time t f andtemperature T f (see figure 7.2). Because the bomb rotates during the final period, the temperature that the calorimeter proper would attain if this period were extended indefinitely ( T ∞ ) will be different from the value derived from the initial period. Thus,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where, as in section 7.1, the subscripts i and f refer to the initial and final periods, respectively; T is the temperature of the calorimeter proper; T j is the jacket temperature; u is the sum of all constant secondary thermal effects due to the heat of stirring, resistive heating at the temperature sensor, and so on; and v is the thermal effect associated with the rotation of the bomb. In this case, the term /Delta1 T corr in equation 7.2, necessary to derive the adiabatic temperature rise, is given by

<!-- formula-not-decoded -->

where the temperature T refers to the main period. Combining equation 7.60 with 7.63 we obtain

<!-- formula-not-decoded -->

Therefore, by using equation 7.64 it is possible to automatically include the energy of rotation in the calculation of /Delta1 T corr. As indicated in section 7.1, it is frequently observed that the temperature of the calorimeter proper during the initial and final periods is, to a good approximation, a linear function of time. In this case, the values of g i and g f in equation 7.64 are derived from a linear least squares fit to the experimental temperature-time data obtained during those periods. When significant departures from linearity are observed, T ∞ i and T ∞ f

should be found by nonlinear fitting of equation 7.9 to the experimental data and k should be determined from the equation

<!-- formula-not-decoded -->

which can be derived by subtracting equation 7.62 from 7.61. The values of T i , g i , T f , and g f are also calculated from those nonlinear fittings and correspond to the midtimes of the initial and final periods, respectively.An approximate value of t s is always used in practice. This can be selected according to the following procedure [28]. Several preliminary experiments are done in which the substance understudyisburnedwithoutbombrotation,andthecorresponding /Delta1 T corr values are calculated by the Regnault-Pfaundler method addressed in section 7.1. These values are then used to derive t s from equation 7.64.

The advantage of rotating the bomb throughout the final period is that v in equation 7.62 must be held constant only within each individual experiment. If the bomb rotation is stopped during the reaction period, the energy of rotation will be included as part of the energy equivalent of the calorimeter and must therefore remain the same throughout a series of calibration and main experiments. This requirement can, however, be avoided if the motor driving the rotation is placed inside the calorimeter proper and the electrical energy supplied to the motor is measured in each experiment. This strategy was adopted in the micro rotating-bomb aneroid calorimeter sketched in figure 7.8 [75,76].

The corrections due to the bomb rotation can also be eliminated by using a dynamic calorimeter , in which the whole calorimeter is rotated and the rotation mechanism is outside the calorimeter proper. An example of such instrument is the aneroid calorimeter developed by Adams, Carson, and Laye [77], shown in figure 7.9.

In the case of compounds containing sulfur, the quantitative conversion of all sulfur dioxide and sulfur trioxide formed in the combustion to aqueous sulfate ion can be achieved by leaving some air inside the bomb before charging it with oxygen (i.e., by not purging the bomb) [60-64]. During the bomb process, sufficient amounts of nitrogen oxides are generated from the atmospheric nitrogen

Figure 7.8 Scheme of a micro rotating-bomb aneroid combustion calorimeter [75,76].

<!-- image -->

Figure 7.9 Scheme of the aneroid dynamic combustion calorimeter designed by Adams, Carson, and Laye [77]. A: jacket; B: jacket lid; C: motor that drives the rotation of calorimetric system; D: rotation system; E: bomb (which is also the calorimeter proper); F: channels to accommodate the temperature sensor, which is a copper wire resistance wound around the bomb; G: crucible; H: electrode; I: gas valve. Adapted from [77].

<!-- image -->

present to catalyze the oxidation of sulfur to aqueous SO 2 -4 , as in the industrial production of sulfuric acid by nitrogen oxide methods (e.g., the lead chamber and tower processes) [78]. Usually, 10 cm 3 of water is initially placed in a bomb of ∼ 300 cm 3 volume. This volume of water is generally adequate to wash the interior of the bomb and yield a homogeneous H2SO4 solution. The combustion of compounds of the general formula CaHbOcSd in the standard state is normally referred to the following reaction:

<!-- formula-not-decoded -->

The combustion of an organic fluorine compound in a bomb containing water (typically 10 cm 3 for a bomb of ∼ 300 cm 3 total volume) can be represented by the equation [61-63]

<!-- formula-not-decoded -->

where x is the fraction of fluorine that is converted to CF4. Unless the sample is highly fluorinated, no CF4 is formed and all the fluorine present in the compound under study appears as HF in the reaction products [63]. In the combustion of fluorocarbons, however, as much as 80% of the fluorine initially present may lead to CF4 (see table 7.4). The fraction x is roughly dependent on the ratio d/b and, in general, if d/b &lt; 1 only HF is produced [61]. The amount of CF4 formed can be decreased if the compound is burned together with a hydrogen-containing auxiliary material, such as hydrocarbon oil or polyester film. Although other fluorinated products may in principle be generated (e.g., hexafluoroethane), HF and CF4 were the only products found by mass spectrometric analysis of the gaseous products from the combustion of several organofluorine compounds [63,74,79].

Organochlorine or -bromine compounds are burned in the presence of aqueous solutions of arsenious oxide (As2O3 ) or hydrazine hydrochloride (N2H4.2HCl). These solutions are effective in reducing the elemental chlorine or bromine formed to the chloride or bromide ions according to the reactions (X = Cl, Br) [61,62,64-66]:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Therefore, all chlorine and bromine present in the compound under study should be converted to Cl -( aq ) and Br -( aq ) during the bomb process. The contribution of reactions 7.68-7.70 to the internal energy change of the bomb process can be taken into account, after their extent has been determined by chemical analysis of the final bomb solution.

The combustion of organochlorine or -bromine compounds is commonly referred to the following standard state reaction (normally n = 600):

<!-- formula-not-decoded -->

There is evidence that the platinum lining of the bomb can catalyze the decomposition of reactions of As2O3(aq) and N2H4.2HCl(aq) prior to the ignition of the sample [80,81]. This problem can be overcome by initially enclosing the solution in a glass or plastic dish inside the platinum-lined bomb. Alternatively, the bomb may be lined with tantalum, which shows no catalytic activity toward the decomposition of As2O3 and N2H4.2HCl.

As indicated, only elemental iodine is found in the combustion products of organoiodine compounds[61,62,67].Theiodineformedinastaticbombismostly in the crystalline state, but some is present in the aqueous and in the gaseous phases. The thermal corrections for dissolution and sublimation are very small and, therefore, static-bomb calorimeters may be used to study organoiodine compounds. However, to avoid the uncertainty in the final state due to the distribution

of I2 among solid, aqueous, and gaseous phases, it has been recommended that a moving bomb containing an aqueous solution of KI be used in the study of organic iodine compounds [82]. The standard energy of combustion of organic compounds of general formula CaHbOcId is generally reported in terms of the following reaction:

<!-- formula-not-decoded -->

Rotating bomb combustion calorimetry has also been successfully applied to organic compounds containing heteroatoms, such as boron, phosphorus, and selenium [61,62,83-85]. The application of combustion calorimetry to organometallic compounds was reviewed by Pilcher [71]. The critical analysis made in this review indicates that reliable results have been obtained by the moving-bomb method for organometallic compounds of Si, Ge, As, Bi, and Pb and also for Mn2CO10 [86] and W( η 5 -C5H5 ) 2Cl2 [87]. Static-bomb calorimetry seems to have success only for organometallic compounds of Hg and Sn [71].

Detailed schemes for calculating the Washburn corrections in experiments with organic compounds of general formulas CHOS and CHONX (X = halogen) have been published [28,45,51,63,66,88,89]. However, for substances containing more than one type of halogen or some other heteroatoms and for organometallic compounds, the complete set of auxiliary data needed to calculate the Washburn corrections is usually not known with sufficient accuracy. This problem may be solved by so-called comparison experiments. In these experiments an effective energy equivalent of the calorimeter is determined, usually by burning benzoic acid and another substance of well-defined energy of combustion, so that the composition of the final state is approximately the same as in the combustion experiments of the compound under investigation. Any error in the calculation of the Washburn corrections is largely eliminated if one uses this effective energy equivalent to derive /Delta1 U IBP in the main combustion experiments.

## 7.3 FLAME COMBUSTION CALORIMETRY IN OXYGEN

Flame combustion calorimetry in oxygen is used to measure the enthalpies of combustionofgasesandvolatileliquids at constant pressure [54,90]. Some highly volatile liquids (e.g., n -pentane [91]) have also been successfully studied by staticbomb combustion calorimetry. In general, however, the latter technique is much more difficult to apply to these substances than flame combustion calorimetry. In bomb combustion calorimetry, the sample is burned in the liquid state and must be enclosed in a container prior to combustion. Encapsulation may be difficult, because it is necessary to minimize the amount of vaporized compound inside the container as much as possible. In addition, volatile liquids tend to burn violently under a pressure of 3.04 MPa of oxygen, which leads to incomplete combustion. These problems are avoided in flame combustion calorimetry, where the sample is carried to the combustion zone as a vapor and burned under controlled conditions at atmospheric pressure.

Particularly important compounds have been studied by flame combustion calorimetry. Methane [92-94], ethanol [95], diethyl ether [96], carbon monoxide [92,93,97], hydrochloric acid [98], and water [93,97,99] are representative examples. With a few exceptions (HCl, H2O, D2O [100], SO2 [101], cyanogen [102,103], and some lower chloroalkanes [104,105]), measurements by flame combustion calorimetry have been limited to substances of general formula CaHbOc.

Precursors of the modern oxygen flame calorimeter had already been described in the late nineteenth century by Favre and Silberman and byThomsen [19]. Flame combustion calorimetry in oxygen was, however, developed into a high-precision technique by Rossini around 1930. All accurate results reported since then were obtained by using instrumentation and techniques based on those introduced by Rossini [54,90]. Some major contributions to the field of flame combustion calorimetry were also made by Pilcher and co-workers during the 1960s and early 1970s, such as the development of an apparatus to study organochlorine compounds [90,105].

Figure 7.10 shows the flame combustion calorimeter used by Rossini in 1931 to determine the enthalpy of formation of liquid water, from the direct reaction of hydrogen with oxygen [54,99]:

<!-- formula-not-decoded -->

The study of reaction 7.73 is one of the most important thermochemical experiments ever made, and it will be briefly analyzed here to illustrate the flame combustion calorimetry method. The application of flame combustion calorimetry to hydrocarbons and other organic compounds containing oxygen, nitrogen, or chlorine is covered in detail in the review by Pilcher [90].

Rossini' s apparatus is similar to an isoperibol bomb combustion calorimeter in which a burner vesselA inside the calorimeter proper B has replaced the bomb. Some openings at the top of the calorimeter proper and of the thermostatic bath C allow the connection of the burner to the gas supply lines D, E, F, and G, and to the exit gas line H. Before admission into the calorimeter, the reactant gases are purified by passing through a sequence of three tubes I, J, and K, containing Ascarite (a sodium hydroxide-asbestos mixture used for removing CO2 ) , magnesium perchlorate (for removing water vapor), and P2O5 (to eliminate the last traces of water vapor), respectively. The gas flows are determined by using the flow meters L.

In flame calorimetry, it is not easy to measure directly with good accuracy the mass of reactants consumed in the combustion. Therefore, the results are always based on the quantitative analysis of the products and the stoichiometry of the combustion process. In the case of reaction 7.73, the H2O produced was determined from the increase in mass of absorption tubes such as M, containing anhydrous magnesium perchlorate and phosphorus pentoxide [54,99]. When organic compounds are studied by flame combustion calorimetry, the mass of CO2 formed is also determined. As in bomb calorimetry, this is done by using absorption tubes containing Ascarite [54,90].

Figure 7.10 Scheme of the isoperibol flame combustion calorimeter used by Rossini to determine the enthalpy of formation of water [54,97]. A: burner vessel; B: calorimeter proper; C: thermostatic bath; D, E, F, G: gas inlets; H: gas outlet; I: purifying tube containing Ascarite (a sodium hydroxide-asbestos mixture), for removing CO 2 ; J: purifying tube containing Mg(ClO 4 ) 2 .3H 2 O, for removing water vapor; K: purifying tube containing P2 O 5 , to eliminate the last traces of water vapor; L: flow meter; M: tube containing Mg(ClO 4 ) 2 .3H 2 O and P2 O 5 , for absorption of water; N: guard tube containing P2 O 5 ; O: calibration heater; P: thermometer; Q: stirrers. Adapted from [54,99].

<!-- image -->

For the combustion of hydrogen in an excess of oxygen the inlets D and F were connected to a H2 and a O2 cylinder, respectively. Inlet G was connected to a second O2 cylinder. This oxygen supply was used to flush the apparatus and vaporize the liquid water present in the burner vessel at the end of the experiment, so that it would be absorbed in the tube M and gravimetrically analyzed (see following discussion). Inlet E was not used in these experiments.

The burner vessel (figure 7.11) is made of Pyrex glass, except for the tip of the tube A that carries the flame, which is made of silica. The reaction is started by discharging a high-voltage spark across the two platinum wire electrodes B and C and a stable flame, about 5 mm long, burns at the tip of A and inside the combustion chamber D. The gases exit the combustion chamber at E and pass through a heat exchange spiral F. The major part of the water formed in the reaction condenses and remains in the burner vessel as a liquid, particularly

Figure 7.11 Details of the burner vessel used by Rossini to determine the enthalpy of formation of water [54,99]. A: burner tube; B and C: platinum electrodes; D: reaction chamber; E: exit tube; F: heat-exchange spiral; G: condensing chamber; H and I: gas inlet tubes; J: gas outlet. Adapted from [54,99].

<!-- image -->

inside the condensing chamber G. As mentioned, this water can be flushed out of the apparatus at the end of the experiment by passing dry oxygen through the burner and collected in an absorption tube for gravimetric analysis. The amount of gaseous water present inside the burner vessel at the end of the experiment is calculated from the volume of the vessel (51.5 cm 3 in this case) and the vapor pressure of water at the final temperature of the experiment. Any water vapor carried out of the calorimeter by the excess gas during the reaction period is quantitatively absorbed at the tube M shown in figure 7.10 and also gravimetically determined. Thus the total mass of water formed in the liquid and gaseous state can be evaluated.

The experimental data and the calculations involved in the determination of a reaction enthalpy by isoperibol flame combustion calorimetry are in many aspects similar to those described for bomb combustion calorimetry (see section 7.1): It is necessary to obtain the adiabatic temperature rise, /Delta1 T ad , from a temperaturetime curve such as that in figure 7.2, to determine the energy equivalent of the calorimeter in an separate experiment and to compute the enthalpy of the isothermal calorimetric process, /Delta1 H ICP, by an analogous scheme to that used in the case of equations 7.17-7.19 and /Delta1 U IBP. The corrections to the standard state are, however, much less important because the pressure inside the burner vessel is very close to 0.1 MPa.

If, as chosen by Rossini, the reference temperature T R of the reaction is taken as the average temperature of the main period, T R = ( T f + T i ) /2 (see figure 7.2), then /Delta1 H ICP can be calculated from the enthalpy of the actual calorimetric process, /Delta1 H exp as follows. It is assumed that first the reactant gases entering the calorimeter at room temperature, T room, are brought to T R with a corresponding enthalpy variation of /Delta1 H 1. Then the temperature of the calorimeter is changed

from T R to T i, and the enthalpy changes by /Delta1 H 2. The bomb process is started at T i and the temperature of the system rises from T i to T f . This step is accompanied by the enthalpy change /Delta1 H exp. The system is finally brought from T f to T R, the corresponding internal energy change being /Delta1 H 3. The values of /Delta1 H 1, /Delta1 H exp, /Delta1 H 2 and /Delta1 H 3 are given by

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The ignition enthalpy, /Delta1 H ign, is directly measured in independent experiments. The term ε o represents the energy equivalent of the standard calorimetric system, which consists of the calorimeter proper with a fixed amount of water, and the dry burner filled with oxygen. The contribution, ε ci, of the contents of the calorimetric system in the initial state to the energy equivalent of the calorimeter can be calculated from the amount of substance of inflowing hydrogen, n (H 2 ), and oxygen, n (O 2 ), and the values of Cp (H 2 ) and Cp (O 2 ). It is reasonable for this purpose to derive n (H 2 ) and n (O 2 ) from the ideal gas law by using the gas volume obtained from the readings given by the flow meters L (figure 7.10) and the duration of the gas inflow. No thermal correction equivalent to /Delta1 H 1 is required for the outflowing gases, because on average, they leave the calorimeter at the temperature T R.The term ε cf is the contribution of the final contents of the burner to the energy equivalent of the calorimeter. In the case of reaction 7.73, the value of ε cf is calculated from the masses of liquid and gaseous water remaining inside the burner at the end of the experiment and from the corresponding massic heat capacities.

The enthalpy of reaction 7.73 at T R is given by

<!-- formula-not-decoded -->

where n represents the total amount of substance of water generated in the experiment. According to reaction 7.73 this water must be in the liquid state, and the term m (H 2 O,g) /Delta1 vap h o (H 2 O) is the correction due to the condensation of the quantity of water that is formed in the gaseous state during the calorimetric process. The term /Delta1 vap h o (H 2 O) is the standard massic enthalpy of vaporization of water and m (H 2 O,g) represents the total mass of the gaseous water that remains in the burner vessel at the end of the experiment and of water vapor that escapes and

from the calorimeter during the main period. These masses are determined as already indicated.

The calorimeter in figure 7.10 was electrically calibrated [54,99] by using the heater O. Flame calorimeters are, however, most frequently calibrated on the basis of the reaction of hydrogen with oxygen, which has been recommended for this purpose by IUPAC [39].

To obtain the standard enthalpy of reaction 7.73 at 298.15 K, /Delta1 c H o (298.15K), from /Delta1 c H ( T R) it is necessary to account for the enthalpy changes /Delta1 H 4 and /Delta1 H 5:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where /Delta1 H 4 and /Delta1 H 5 are usually very small compared with /Delta1 c H ( T R), but nevertheless are taken into account in accurate work. /Delta1 H 4 corresponds to the standard state correction and can be calculated by considering the enthalpy contributions H o -H ( p R) associated with bringing the gaseous reagents from the pressure p R inside the reaction chamber to p = 0, at the constant temperature T R. Those contributions can be derived from equation 2.16 if the appropriate equations of state are known. In Rossini' s experiments, the pressure inside the reaction chamber varied between 0.977 and 0.995 bar and therefore p R was taken as 0.1 MPa. The corresponding standard state corrections are [ H o -H (0.1 MPa)] H2 = -0.48 J mol -1 [99] and [ H o -H (0.1 MPa)] O2 = 8.06 J mol -1 [99], leading to

<!-- formula-not-decoded -->

The calculation of /Delta1 H 5 requires the heat capacities of the reactants and products. It is relatively simple, however, to design the experiment so that T R ≈ 298.15Kand,undertheseconditions, /Delta1 H 5 is negligible. In Rossini' s experiments, for example, T R varied between 298.22 K and 298.30 K, and the corresponding /Delta1 H 5 values varied between 3 and 5 J mol -1 .

The standard enthalpy of formation of water originally proposed by Rossini, /Delta1 f H o (H2O, l) = -285.753 ± 0.036 kJ (int) mol -1 [93,99], is given in international joules and corresponds to a standard pressure of 1 atm and a molar mass of water of 18.0156 g mol -1 . The unit international joule was used until about 1948 to report thermochemical data and is related to the SI joule by 1 J = 0.999835 J (int) [106]. Rossini' s result for /Delta1 f H o (H2O, l) has been adjusted to account for changes in the auxiliary data (e.g., the molar mass of water) and in the adopted standard state conditions. However, despite the changes in /Delta1 f H o (H2O, l), the enthalpy of reaction 7.73 reported by Rossini, /Delta1 c H ( T R), has endured the test of time. The standard enthalpies of formation of liquid water currently recommended in the CODATA and NIST-JANAF compilations /Delta1 f H o (H2O, l) = -285.830 ± 0.042 kJ mol -1 [58,107], and in the very recent ATcT Tables /Delta1 f H o (H2O, l) = -285.823 ± 0.033 kJ mol -1 [108], are based on that value and on later results by King and Amstrong [109], which confirmed Rossini' s data.

Rossini' s paper on the enthalpy of formation of water [99] is a masterpiece in terms of careful description of the experiment and presentation of data. It makes us wonder if the publication of all those details, which have been essential for updating the value of /Delta1 f H o (H2O, l) over the years, would still be accepted by most modern journals. If the current tendency to eliminate from publications the reporting of primary results and basic experimental details had prevailed in the 1930s, Rossini' s work on water would probably have had to be repeated by later investigators.

## 7.4 FLUORINE COMBUSTION CALORIMETRY

Combustion calorimetry in fluorine, chlorine, and bromine atmospheres was developed essentially to study inorganic substances that are resistant to O2 oxidation or lead to mixtures of products that are difficult to characterize on reaction with O2 [110-116]. Other halogenating agents were also proposed for combustion calorimetry and, for example, a method where fluorination was achieved by using solid XeF2 inside a metal bomb has been described [112,114]. As referred to in sections 7.1 and 7.2, the standard enthalpies of formation of most organic compounds, including those containing halogens, can satisfactorily be obtained by oxygen combustion calorimetry, and in only a few cases was their determination attempted by a different combustion method; for example, the measurement, by Jessup, McCoskey, and Nelson [117], of the enthalpy of formation of CF4, from the direct reaction of methane with fluorine in a flame calorimeter; the studies of CF4 by Domalski and Armstrong [118] and by Greenberg and Hubbard [119] using fluorine bomb calorimeters; and the fluorine bomb calorimetric study of polytetrafluoroethylene by Domalski and Armstrong [118].

There have been far more thermochemical experiments carried out in fluorine than in any other halogen atmosphere, the large majority of them by fluorine bomb calorimetry [110-116]. Thus, only fluorine combustion calorimetry will be covered in this section with a strong emphasis on bomb calorimetry. Note, however, that many technical details and safety precautions mentioned here for fluorine combustion calorimetry also apply to combustion in other halogens.

The first reported attempt to use fluorine in calorimetric measurements is probably Berthelot and Moissan's study of the reaction between K2SO3(aq) and F2(g), in 1891 [19,120]. Modern fluorine bomb calorimetry, however, was started in the 1960s by Hubbard and co-workers [110,111,121], while in the same period Jessup andArmstrong and their colleagues [109,115-117] developed the method of fluorine flame calorimetry to a high degree of accuracy and precision.

Fluorine bomb calorimetry is in many aspects similar to oxygen bomb calorimetry. The experiments are carried out in isoperibol instruments, which, except for the bomb, are basically identical to those described in sections 7.1 and 7.2. The procedure used to calculate /Delta1 c U o (298.15 K ) from the experimental results is also analogous to that discussed for oxygen bomb calorimetry in section 7.1. Thus, a temperature-time curve, such as the one in figure 7.2, is first acquired, and the corresponding adiabatic temperature rise, /Delta1 T ad , is derived.

The obtained /Delta1 T ad value and the energy equivalent of the calorimeter, ε , are then used to calculate the energy change associated with the isothermal bomb process, /Delta1 U IBP. Conversion of /Delta1 U IBP to the standard state, and subtraction from /Delta1 U o IBP of the thermal corrections due to secondary reactions, finally yield /Delta1 c U o (298.15 K ) . The energy equivalent of the calorimeter, ε , is obtained by electrical calibration or, most commonly, by combustion of benzoic acid in oxygen [110,111,113]. The reduction of fluorine bomb calorimetric data to the standard state was discussed by Hubbard and co-workers [110,111].

The major differences between the fluorine and oxygen combustion calorimetry methods arise from the exceptional reactivity and toxicity of fluorine. The substances studied by oxygen combustion calorimetry are normally stable when kept inside a bomb at 298.15 K and under ≈ 3 MPa of O2. Oxygen- and moisturesensitive compounds can also be studied because various types of containers are available to prevent their reaction with O2 prior to ignition. Common examples are glass ampules, which are inert toward the combustion process and, more commonly, Melinex bags or polyethene ampules, which burn cleanly to CO2 and H2O. As carbon dioxide and water are also generated in the combustion of the sample, no extra complexity is introduced in the analysis of the final state of the bomb process by the use of those plastic containers.

Most substances are attacked to some extent by F2. Therefore, combustion calorimetric samples must be isolated from fluorine until the start of the reaction period. However, it is virtually impossible to find protective materials that can be easily sealed around the sample, that are inert to fluorine, or that do not lead to complex mixtures of products on fluorination. The use of a two-compartment bomb, such as the one represented in figure 7.12, enabled these problems to be overcome and became the preferred option in most fluorine combustion calorimetric studies [111,113,114,122,123]. Fluorine is contained in tank A, which surrounds the bomb body B. The bomb head C is attached to the bomb body by the cylindrical screw collar D. The bomb, in an inverted position (figure 7.12),

Figure 7.12 Scheme of a two-chamber bomb used in fluorine combustion calorimetry.

<!-- image -->

A: fluorine tank; B: bomb body; C: bomb head; D: screw

collar; E: valve;

F: connecting tube; G: sample;

H: crucible; I: tungsten saucer;

J: electrodes; K: holes. Adapted from [111,113].

is placed inside a water-filled calorimeter. Opening the valve E allows the fluorine ( p ≈ 1 MPa) to expand through the connecting tube F and into the bomb where, at p ≈ 0.6 MPa, it comes in contact with the sample G. Fluorine combustion calorimetric bombs are made of Monel or nickel and are initially exposed to F2 to coat the interior with a thin film of NiF2, which protects the surface from further chemical attack. Gaskets are made of gold, lead, or Teflon, and Orings are made of Teflon. The most common sample container is a prefluorinated nickel crucible [110,111,113]. In the case of figure 7.12, the crucible H rests on the bomb lid. Solid substances such as sulfur, selenium, tellurium, phosphorus, arsenic, and SiS2, which spontaneously and quantitatively react with F2, are simply burned inside a nickel crucible. These substances are said to be hypergolic toward fluorine ('hypergolic' denotes a combination of fuel and oxidizer that ignites spontaneously on contact with each other). If the sample does not spontaneously ignite on contact with F2, a hypergolic material is used as the fuse to initiate the reaction. A small amount of sulfur sprinkled on top of the sample is frequently employed for this purpose. Sulfur is a very convenient fuse because it immediately and quantitatively reacts on contact with an excess of F2:

<!-- formula-not-decoded -->

The gaseous product (SF6 ) does not interfere with the analysis of solids that form in the main bomb process. Furthermore, the contribution of reaction 7.82 to /Delta1 U o IBP can be accurately calculated from the mass of sulfur and the value of /Delta1 r U o (7.82) at 298.15 K [124]. It may also be necessary, in some cases, to use an auxiliary substance to promote complete combustion of the compound under study [111,113]. Tungsten is a very common combustion aid; it reacts cleanly with excess fluorine according to

<!-- formula-not-decoded -->

Tungsten has been used to induce complete combustions, for example, in the studies of WTe2 [123], Mo5Si3 [125], and Si3N4 [126]. In these cases, the sample was typically arranged as shown in figure 7.12. The compound under study (G), with the sulfur fuse sprinkled on top was placed in a thin tungsten saucer (I), supported by a nickel crucible (H) with holes in the sides (K) to allow rapid circulation of the fluorine around the combustible materials as the reaction proceeded.

The reader may be wondering by now why there are electrodes J in the bomb of figure 7.12, because spontaneous ignition of the sample usually occurs on contact with fluorine. Calorimetric samples of tungsten, molybdenum, and zirconium, for example, have been ignited using electrically heated wires of the same materials [110]. The electrodes are also necessary for the calibration experiments where, as indicated, the energy equivalent of the calorimeter is obtained from the combustion of benzoic acid in oxygen. In this case, discharging a condenser through a platinum wire connecting the two electrodes produces ignition of the calibrant (see section 7.1).

The main auxiliary apparatus needed to perform fluorine combustion calorimetry consists of a fluorine still, a bomb charging and discharging manifold, and a glove box [110,111,113]. The fluorine still and the manifold should

be installed in a well-ventilated hood. The bomb must be kept completely dry to avoid the reaction of H2O with fluorine. Thus, it is always assembled inside a glove box. In a typical experiment where the bomb in figure 7.12 was used [113], the tankA was attached to the charging manifold, pumped to a low pressure, filled with F2 (pressures up to ∼ 3 MPa can be used), checked for leaks, and transferred to a glove box containing a nitrogen atmosphere. The sample, crucible, and so on were weighed and loaded in the bomb inside the glove box. The bomb was closed, connected to the tank, and the assembly was removed from the glove box. It was then attached to the manifold, evacuated to eliminate the N2 remaining inside, and finally transferred to the calorimeter where it was immersed in a weighed amount of water inside the calorimeter proper. The valve connecting the fluorine tank to the bomb (E in figure 7.12) was attached to the remote opening mechanism, and the experiment proceeded as usual with isoperibol calorimetry. As indicated, the reaction was started by admission of fluorine to the bomb.The bomb was removed from the calorimeter at the end of the experiment and attached to the manifold. The excess F2 and the product gases were discharged through the manifold and condensed in a liquid nitrogen trap; a series of freezing, pumping, and thawing cycles removed F2 so that only the gaseous fluorides formed in the combustion remained in the trap. These were transferred to an infrared cell attached to the manifold and spectroscopically analyzed. The vacuum pump of the manifold is protected from fluorine by a large column containing activated Al2O3. Fluorine is retained in the trap by reacting with the alumina

<!-- formula-not-decoded -->

After removal of the gaseous products, the bomb is transferred to the glove box, opened, and inspected for the presence of solid products. If a residue is found it is weighed and analyzed. The crucible is also reweighed to determine if NiF2 was formed in the combustion, and a correction for this side reaction is applied, if needed.

Much of the discussion of oxygen flame calorimetry presented in section 7.3 is directly applicable to fluorine flame calorimetry. As in the case of bomb calorimetry, however, the special properties of fluorine combustion systems and problems associated with handling fluorine require a somewhat different experimental method [109,115,116]. Thus, for example, a metal burner should be used. Also, the fact that the mixing of many gases with F2 may lead to spontaneous ignition hinders the use of a premixed flame. Fluorine combustion calorimetry has been used to study the thermochemistry of important reactions, such as

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

which lead to the enthalpies of formation of HF(g) [115,116], HF(aq), and OF2(g) [109]. Reactions 7.86 and 7.87 were studied by using the two-stage reaction vessel shown in figure 7.13. The flame reaction occurs in the upper chamber A, where

Figure 7.13 Combustion chamber and primary solution vessel of a fluorine flame calorimeter. A: combustion chamber; B: electrode; C: solution vessel; D: gas dispersion system; E: gas inlets; F: gas outlet. Adapted from [115].

<!-- image -->

the reactant gases are mixed and ignited by a spark from the nickel electrode B. The flow of excess hydrogen subsequently carries the products to the solution chamber C, where the gas dispersion system D forces the gaseous mixture to bubble through water, thus producing a homogeneous solution of hydrofluoric acid.

As illustrated in this section, the problems associated with using fluorine in combustion calorimetry seem to have been largely overcome. The fluorine bomb and flame calorimetry methods have been perfected to such an extent that, provided the chemistry of the process under study is well characterized, results of very good accuracy and precision can be obtained routinely.

## Isoperibol Reaction-Solution Calorimetry

The determination of enthalpies of reaction in solution, using isoperibol reactionsolution calorimetry, is often the easiest and most accurate method of determining enthalpies of formation of compounds that cannot be studied by combustion calorimetry. The technique was pioneered by Thomsen who, between 1882 and 1886, performed thermochemical measurements involving the solution of various substances in liquids (e.g., diluted acids) [127]. Many types of isoperibol reactionsolution calorimeters have been developed since then [29,128]. The designs vary according to the nature of the reactions of interest. One of the most widely used consists of a vessel, such as the one shown in figure 8.1, immersed in a thermostatic water bath.The sample is sealed inside a thin-walled glass ampuleA, fixed to an ampule breaking system B in the calorimeter head C. The calorimeter head also supports the temperature sensor D, the stirrer E, and an electrical resistance F , used for calibration of the apparatus.The Dewar vessel G, containing the solution to be reacted with the sample, is adjusted to C. The assembled calorimetric vessel is transferred to the thermostatic bath, and from then on, the experimental procedure closely follows that already described in section 7.1 for isoperibol static-bomb combustion calorimetry.

The reaction is initiated at the end of the fore period by pushing down the plunger H and breaking the ampule against a pin situated at the bottom of the ampule breaking system B. As a result of the calorimetric experiment, a temperature-time curve such as the one in figure 7.2 is obtained. Note that figure 7.2 is typical of an exothermic process. In the case of an endothermic process, a decrease of the temperature of the calorimetric system is observed during the reaction period.

The experiments are usually carried out at atmospheric pressure and the initial goal is the determination of the enthalpy change associated with the calorimetric process under isothermal conditions, /Delta1 H ICP, usually at the reference temperature of 298.15 K. This involves (1) the determination of the corresponding adiabatic temperature change, /Delta1 T ad , from the temperature-time curve just mentioned, by using one of the methods discussed in section 7.1; (2) the determination of the energy equivalent of the calorimeter in a separate experiment. The obtained /Delta1 H ICP value in conjunction with tabulated data or auxiliary calorimetric results is then used to calculate the enthalpy of an hypothetical reaction with all reactants and products in their standard states, /Delta1 r H o , at the chosen reference temperature. This is the equivalent of the Washburn corrections in combustion calorimetry

Figure 8.1 Scheme of a Dewar vessel isoperibol reactionsolution calorimeter. A: ampule containing the sample; B: ampule breaking system; C: calorimeter head; D: temperature sensor; E: stirrer; F: electrical resistance; G: Dewar vessel; H: plunger of the ampule breaking system; I, J: inlets; K: plug connecting the calibration resistance to the calibration circuit.

<!-- image -->

(see section 7.1), but it generally involves a much simpler thermodynamic cycle. In reaction-solution calorimetry, it is normally a very good approximation to assume that the experiment occurs at pressure of 0.1 MPa, and therefore the pressure corrections are usually negligible. A detailed discussion of general strategies for the reduction of reaction-solution calorimetric results to the standard state has been presented by Vanderzee [129,130]. Finally, the enthalpy of formation of the compound of interest is derived from the obtained /Delta1 r H o value and the enthalpies of formation of all other species participating in the standard state reaction.

To obtain /Delta1 H ICP it can be assumed that the calorimetric system, with an energy equivalent ε i, is first brought from the reference temperature T R to the initial temperature T i with a corresponding enthalpy change of ε i ( T i -T R). The reaction is initiated at T i, and the temperature of the system varies from T i to T f . The enthalpy change associated with this step is ε f /Delta1 T corr + ∑ i /Delta1 Hi . Here, ε f represents the energy equivalent of the calorimetric system in the final state;

/Delta1 T corr is the correction due to the heat exchange with the surroundings, the heat of stirring, and the heat dissipated by the temperature sensor (equation 7.2); the term ∑ i /Delta1 Hi represents the sum of several contributions, notably, in welldesigned experiments, the heat dissipated during the breaking of the ampule and the heat associated with the evaporation of the solvent that occurs after breaking the ampule (for example, an ampule containing a solid sample may also contain dry air, and after breaking, solvent will be vaporized to saturate the corresponding vapor space) [129].The system is finally brought from T f to T R, the corresponding internal energy change being ε f ( T R -T f ) . The enthalpy change associated with the isothermal calorimetric process is the sum of the enthalpy changes of the three steps:

<!-- formula-not-decoded -->

The value of ε ( ε i or ε f ) is usually determined by electrical calibration (note that contrary to combustion calorimetry, it is not common practice to separate the initial and final energy equivalents of the calorimeter into the contribution of the reference calorimeter, ε o, and those of the contents present in the initial, ε ci , and, final, ε cf , states; see section 7.1). In the case of the calorimeter in figure 8.1, a current I is passed trough the resistance F for a known period of time t and the potential change V across F is measured. Then:

<!-- formula-not-decoded -->

where VIt represents the energy dissipated as heat in the resistance F during the calibration. Equation 8.2 yields ε i if the calibration run ends strictly at T R and ε f if T R is the starting temperature.A scheme of the calibration circuit is represented in figure 8.2, where R1 corresponds to the resistance F shown in figure 8.1; R2 is a standard resistance of accurately known value R 2, which is placed outside the calorimetric vessel. The circuit also includes a power supply P , a timer used to set the calibration time, a switch S, and a multimeter. Changing the switch between positions 1 and 2 allows the potential drops across R1 or R2, respectively, to be measured by the multimeter. The value of I in equation 8.2 is calculated from I = V 2/ R 2, where V 2 is the potential change across R2. Details of several other calibration circuits have been described elsewhere [128].

Ideally, the energy equivalents ε i and ε f should be measured over the same temperature range of the reaction run, to avoid errors from their variation with temperature and to achieve maximum compensation for errors in the calibration of the temperature sensor [26,128,129]. These errors are, however, frequently negligible in the temperature ranges involved, and the measurement of ε i or ε f is normally performed outside the T i → T f interval. This procedure saves time because there is no need to readjust the initial temperature of the calorimeter between the calibration and main experiment runs. It is therefore a common practice, even when an exothermic reaction is studied, to measure ε i before the reaction and ε f after the reaction and adjust the experimental conditions so that T R is the midpoint between T i and T f . In this case, the temperature of the thermostatic

<!-- image -->

Figure 8.2 Scheme of a typical calibration circuit used in isoperibol reaction-solution calorimetry. P: power supply; S: switch; R 1 : electrical resistance inside the calorimetric vessel (F in figure 8.1); R 2 : standard resistance.

<!-- image -->

Time

a

<!-- image -->

b

Figure 8.3 Typical temperature-time curves obtained when two calibrations are made in isoperibol reaction-solution calorimetric studies of (a) an exothermic reaction and (b) an endothermic reaction. A: fore period of the first calibration experiment; B: main period of the first calibration experiment; C: after period of the first calibration experiment and fore period of the reaction experiment; D: main period of the reaction experiment; E: after period of the reaction experiment and fore period of the second calibration experiment; F: main period of the second calibration experiment; G: after period of the second calibration experiment.

jacket of the calorimeter is fixed at a value above T R and the experiments are set so that the temperature variation in the calibrations and in the reaction runs are as similar as possible (figure 8.3). This method is thought to minimize the errors due to the temperature dependence of the energy equivalent of the calorimeter. However, it is possible for ε i to have different temperature dependence from ε f due to changes in the composition of the solution [129].

In some cases /Delta1 H ICP is calculated from

<!-- formula-not-decoded -->

where 〈 ε 〉 = (ε i + ε f )/ 2. Equation 8.3 results from equation 8.1 by replacing ε i and ε f by 〈 ε 〉 and noting that /Delta1 T ad = T f -T i -/Delta1 T corr (equation 7.2).

Theterm ∑ i /Delta1 Hi in equations 8.1 and 8.3 is frequently very small compared to the uncertainty in the determination of /Delta1 H ICP and in many instances can safely be neglected.This should of course be tested by performing blank experiments under normal operating conditions. For example, the enthalpy associated with breaking an ampule (independently from the contribution from vaporization effects) can be determined by breaking ampules partially filled with the calorimetric solvent in the calorimetric solvent. For many systems this contribution is negligible, provided that a well-designed breaker mechanism and ampules ensure that the dissipation of heat is reduced to a minimum. The importance of vaporization effects can be evaluated as described by Vanderzee [129].

It is also a very common procedure to make a single calibration immediately before the reaction and set the experimental conditions so that the complete run ends as close as possible to the reference temperature (figure 8.4). Recalling the discussion of equations 7.17-7.19, it can be concluded that in this case, if the term ∑ i /Delta1 Hi is neglected one obtains

<!-- formula-not-decoded -->

Although this method ignores the variation of the energy equivalent of the calorimeter with temperature, it is a good approximation for many systems.

In general, reaction-solution calorimeters such as the one represented in figure 8.1 are suitable to study reactions which are complete within 10 to 20 minutes [29,128,131].Typically, when 'clean' reactions are investigated in aqueous solution, a precision of 0.2-0.5% can be attained [29,128,131]. It is possible to achieve a better precision (0.01-0.1% [29,132]) by using the glass calorimetric vessel shown in figure 8.5 inside an evacuated brass can surrounded by a thermostatic water jacket. This set-up is the basis of the LKB reactionsolution calorimeter [132], which was developed from early designs by Sunner and Wadsö [131]. The thermistor A, used as the temperature sensor, and the resistance B, used for calibration, are positioned at opposite sides of the vessel. The stirrer C, which is also the ampule holder, can be pushed down, without stopping the rotation, to break cylindrical glass ampule D against the sapphire pin E.

Various substances and reactions have been used to test the accuracy of reaction-solution calorimeters [39,40].The solution of tris(hydroxymethyl)aminomethane (THAM or TRIS) in 0.1 mol dm -3 HCl(aq), which was first proposed by Wadsö and Irving [133] in 1964 and recommended by the Standards Committee of the U.S. Calorimetry Conference in 1966 [134,135], is perhaps the most widely used method. Several problems encountered in the use of theTHAM+HCl (aq) reaction to assess the accuracy of reaction-solution calorimeters have been

<!-- image -->

pointed out [39,40,135-138]. The method seems to be reliable, however, provided that the procedure described by Prosen and Kilday [135] is strictly followed [39,40]. An alternative system, which has been considered superior to the THAM+HCl(aq) reaction by some authors, is the solution of 5-amino pyridine in HClO4(aq) [139-141]. This reaction was recently recommended by IUPAC and the ICTAC Thermochemistry Working Group to test the accuracy of reaction-solution calorimeters [39,40].

The reaction-solution calorimetric method will be illustrated with two examples: the determination of the enthalpy of formation of Mo ( η 5 -C5H5 ) 2 ( C2H4 ) [142] and Ca0.289Na0.361Al0.940Si5.060O12.000 · 3.468H2O [143]. The first compound belongs to the bis (cyclopentadienyl) family, M( η 5 -C5H5 ) Ln (M = Ti, Zr, Hf, V , Nb, Ta, Mo, W; L = H, halogen, CO, alkyl, alkene, aryl, alkoxide, thiolate, phosphine, etc.; n = 1-3), which has been extensively used as a model to investigate the general trends of the M-L bond dissociation enthalpies in group 4-6 transition metals [72,144-150]. The second is the naturally occurring zeolite mordenite.

Organotransition metal compounds are perhaps one of the best examples of substances for which the success of combustion calorimetry has been very limited up to now, due to a considerable number of experimental difficulties [71,72]. The multiple structural combinations of metals and ligands found in this type of molecules hinder the development of combustion methods that can be systematically applied to a large number of compounds. Many organotransition metal compounds, such as the one in our example, are extremely sensitive to oxygen and require an efficient protection from the atmosphere inside the bomb prior to combustion. Explosions or incomplete combustions frequently plague attempts to burn these compounds in oxygen. More than one type of metal oxide can sometimes be produced in the combustion, and the oxides are normally difficult to dissolve in the calorimetric solutions used in rotating bombs within the duration of the main period. If fluorine combustion calorimetry is used, mixtures of fluorocarbons are formed. Thus, complex final states, practically impossible to analyze with good accuracy, are usually obtained when combustion calorimetry is applied to organotransition metal compounds. By contrast, many organometallic compounds have been successfully studied using isoperibol reaction-solution calorimetry.

The determination of the enthalpy of formation of Mo ( η 5 -C5H5 ) 2 ( C2H4 ) was based on the thermodynamic cycle shown in figure 8.6. First, reaction 8.5 was studied in toluene, using a reaction-solution calorimeter and a calibration circuit essentially identical to the ones in figures 8.1 and 8.2, respectively [142]. The calorimetric vessel was immersed in a water bath maintained at 298.15 K with a temperature stability better than ± 10 -4 K. The compound was sealed in glass ampules under argon atmosphere [151]. The calorimetric vessel was filled with a solution containing 0.2723 g of iodine in 125 cm 3 of toluene, closed, and placed in the thermostatic bath. The air inside the vessel was purged by introducing a glass pipette connected to an argon line through inlet I (figure 8.1), and bubbling argon through the solution for ∼ 40 minutes. The reaction was initiated after the electrical calibration and a curve similar to the one in figure 8.4a was obtained. At the end of the experiments samples of the liquid and gaseous phases were taken with a syringe, through a septum existing in the inlet J, and injected in a gas-liquid chromatograph. The GC analyses indicated that on average, the ratio of the amounts of substance of ethylene present in the liquid and gaseous phases at the end of the experiments was 8:2. It was assumed that the precipitation of Mo( η 5 -C5H5 ) 2I2(cr) was quantitative, because no enthalpy change was detected by breaking ampules containing different amounts of this product in solutions of

Figure 8.6 Thermochemical cycle used to derive the enthalpy of formation of Mo( η 5 -C 5 H5) 2 (C 2 H4) in the crystalline state.

<!-- image -->

Table 8.1 Results of the calorimetric study of the reaction Mo( η 5 -C 5 H5) 2 (C 2 H4) (cr) + I 2 (sln) in toluene, at 298.15 K. In the calculation of the enthalpy of reaction, the molar mass of Mo( η 5 -C 5 H5) 2 (C 2 H4) was taken as 254.17956 g mol -1 . Data from [142].

| Calibration   | Calibration   | Calibration   | Calibration      | Calibration   | Reaction   | Reaction         | Reaction                             |
|---------------|---------------|---------------|------------------|---------------|------------|------------------|--------------------------------------|
| V /V          | I /A          | t /s          | /Delta1 T ad / K | ε /(J K - 1 ) | m /mg      | /Delta1 T ad / K | - /Delta1 r H o ( 8.5 )/ (kJ mol - 1 |
| 2.7043        | 0.0571        | 250           | 0.15748          | 245.14        | 27.78      | 0.08181          | 183.50                               |
| 2.7014        | 0.0571        | 250           | 0.15985          | 241.24        | 43.92      | 0.13542          | 189.06                               |
| 2.7080        | 0.0572        | 250           | 0.16151          | 239.76        | 36.72      | 0.11312          | 187.74                               |
| 2.7064        | 0.0572        | 250           | 0.16045          | 241.21        | 35.94      | 0.10822          | 184.61                               |
| 2.7022        | 0.0571        | 250           | 0.15947          | 241.88        | 24.42      | 0.07358          | 185.25                               |

various concentrations of I2 in toluene. The formation of the diiodide complex had been previously confirmed by IR spectroscopy.

The results of the calibration and reaction experiments are shown in table 8.1 [142]. In this table, t is the time during which a current of intensity I flows through the calibration resistance, V the measured potential drop across the resistance, and m the mass of sample. The values of /Delta1 T ad for the calibration and reaction experiments were determined from the corresponding temperature-time data, using the Regnault-Pfaundler method with T i , T f , k , and T ∞ calculated from equations 7.12-7.15 (section 7.1).

The energy equivalent of the calorimeter, ε , and the enthalpy of the isothermal calorimetric process, /Delta1 H ICP, were derived from equations 8.2 and 8.4, respectively. The standard enthalpy of reaction 8.5 was computed as /Delta1 r H o ( 8.5 ) = /Delta1 H ICP / n , where n is the amount of substance of Mo ( η 5 -C5H5 ) 2 ( C2H4 ) used in the experiment. The data in table 8.1 lead to a mean value /Delta1 r H o ( 8.5 ) = -186.0 ± 2.1 kJ mol -1 , where the uncertainty is twice the standard deviation of the mean (section 2.6). This value was used to calculate the enthalpy of reaction (8.6), where all reactants and products are in their standard reference states, at 298.15 K, from

<!-- formula-not-decoded -->

which results from the cycle represented in figure 8.6. By using /Delta1 sln H o 1 = 15.92 ± 0.16 kJ mol -1 [152] and /Delta1 sln H o 2 = -8.8 ± 0.5 kJ mol -1 [153], it is concluded that /Delta1 r H o ( 8.6 ) = -163.0 ± 2.1 kJ mol -1 . Note that because the mass of Mo( η 5 -C5H5 ) 2(C2H4 ) used in the calorimetric experiments listed in table 8.1 is not constant, the concentration of I2 in the final state varies, and the enthalpy of the solution formed in each experiment is not strictly the same. No systematic variation of /Delta1 sln H o 1 wasfound,however, when the mass of I2 dissolved in 100 cm 3 of toluene in an LKB-8700 calorimeter changed from 0.09441 g to 0.28289 g [152b], and the heat effect associated with these differences in concentration was therefore neglected.

Thestandard enthalpy of formation of Mo( η 5 -C5H5 ) 2(C2H4 ) in the crystalline state is given by

<!-- formula-not-decoded -->

Using /Delta1 f H o [Mo( η 5 -C5H5 ) 2I2, cr] = 69.8 ± 7.8 kJ mol -1 [142] and /Delta1 f H o (C2H4, g) = 52.5 ± 0.3 kJ mol -1 [59], /Delta1 f H o [Mo( η 5 -C5H5 ) 2(C2H4 ) , cr] = 285.3 ± 8.1 kJ mol -1 was obtained. From this result and an estimated value of the enthalpy of sublimation of Mo( η 5 -C5H5 ) 2(C2H4 ) , /Delta1 sub H o [Mo ( η 5 -C5H5 ) 2(C2H4 ) ] = 77 ± 10 kJ mol -1 [142], it was possible to derive /Delta1 f H o [Mo( η 5 -C5H5 ) 2(C2H4 ) , g] = 362.3 ± 12.9 kJ mol -1 and DH o ( Mo -C2H4 ) = 59 ± 20 kJ mol -1 [142]. This value, in conjunction with bond dissociation enthalpy data for other Mo( η 5 -C5H5 ) 2Rn complexes (n = 1, R = diphenylacetylene; n = 2, R = H, CH3, C2H5, n -C4H9 ) , also obtained from reaction-solution calorimetric experiments, was used by Calhorda et al. [142] to discuss several aspects of the molybdenum-carbon bonding energetics.

The determination of the enthalpy of formation of mordenite illustrates a case that involves more precise measurements and requires a more complicated thermodynamic cycle [143]. The experiments were made in an LKB-8700 calorimeter, with a reaction vessel and stirrer constructed of gold, and involved the reaction of mordenite with 100 cm 3 of an approximately 24.4 mass percentage HF aqueous solution. The obtained results are shown in table 8.2, where m is the mass of sample, 〈 ε 〉 is the energy equivalent of the calorimeter, /Delta1 T ad is the adiabatic temperature change, ∑ i /Delta1 Hi includes the contributions of opening the ampule and vaporizing the solvent into the free volume of the ampule, and /Delta1 r H o 1 = /Delta1 H ICP / n is the enthalpy of reaction 1 in table 8.3. In this case /Delta1 H ICP was calculated through equation 8.3.The energy equivalent of the calorimeter was obtained from electrical calibrations performed before and after each reaction experiment. The calibrations covered the same temperature range as the corresponding enthalpy

Table 8.2 Results of the calorimetric study of the reaction Ca 0.289 Na 0.361 Al 0.940 Si 5.060 O 12.000 · 3.468H 2 O(cr) + HF(aq). In the calculation of the enthalpy of reaction the molar mass of Ca 0.289 Na 0.361 Al 0.940 Si 5.060 O 12.000 · 3.468H 2 O was taken as 441.827 g mol -1 . Data from [143].

|    m /g |   〈 ε 〉 / (J K - 1 ) |   /Delta1 T ad / K |   ∑ i /Delta1 H i / J |   - /Delta1 r H o 1 / (kJ mol - 1 |
|---------|------------------------|--------------------|-----------------------|-----------------------------------|
| 0.1451  |                 403.2  |            0.74815 |                  0.09 |                            918.26 |
| 0.145   |                 402.66 |            0.74852 |                  0.09 |                            918.11 |
| 0.14469 |                 403.26 |            0.7457  |                  0.09 |                            917.98 |
| 0.14458 |                 402.64 |            0.74541 |                  0.09 |                            916.91 |
| 0.1456  |                 403.21 |            0.75045 |                  0.09 |                            917.94 |
| 0.14587 |                 402.66 |            0.75359 |                  0.09 |                            918.82 |

of reaction measurements, and the mean temperature of all such experiments was 298.15 ± 0.01 K.

The results shown in table 8.2 lead to a mean value /Delta1 r H o 1 = -918.00 ± 0.50 kJ mol -1 . The uncertainty quoted is twice the standard deviation of the mean. It was assumed that CaF2(cr) was quantitatively obtained in the final state because no enthalpy change was observed in a series of experiments where pure calcium fluoride was dissolved in HF(aq) [143].

Themassofsampleusedwas,onaverage,0.14514g(3.28500 × 10 -4 mol)and essentially constant in the six experiments made (0.14458 g &lt; m &lt; 0.14587 g). The volume of HF solution inside the calorimetric vessel contained 26.3984 g of HFand 81.7569 g of H2O. This corresponds to 4016.68 mol of HF and 13815.01 mol of H2O, respectively, or 4016.68 mol of (HF · 3.439410 H2O ) (aq) per mole of Ca0.289Na0.361Al0.940Si5.060O12.000 · 3.468H2O.

Also listed in table 8.3 are the enthalpy data for the auxiliary reactions, which, in conjunction with the enthalpy of reaction 1, were used to calculate the enthalpy of the standard state reaction:

<!-- formula-not-decoded -->

where subscripts 1-6 refer to the reactions in table 8.3.

Table 8.3 Thermochemical equations and data used for the derivation of the enthalpy of reaction 8.9. Data from [143].

| Reaction                                                                                                        | /Delta1 r H o / (kJ mol - 1 )   |
|-----------------------------------------------------------------------------------------------------------------|---------------------------------|
| 1. Ca 0.289 Na 0.361 Al 0.940 Si 5.060 O 12.000 · 3.468 H 2 O(cr) + 4016.68(HF · 3.439410 H 2 O )( aq ) = [ A ] | - 918.00 ± 0.50                 |
| 2. 5.060SiO 2 (cr, silicalite) + 4015.74(HF · 3.440845H 2 O )( aq ) = [ B ]                                     | - 732.69 ± 0.51                 |
| 3. 0.940Al(OH) 3 (cr, gibbsite) + [B] = [C]                                                                     | - 155.51 ± 0.29                 |
| 4. 0.361NaF(cr) + [C] = [D]                                                                                     | - 1.75 ± 0.12                   |
| 5. 0.289CaF 2 (cr) + [D] = [A]                                                                                  | 0.00 ± 0.06                     |
| 6. 4016.68(HF · 3.439410H 2 O ) (aq) + 5.764H 2 O(l) = 4016.68(HF · 3.440845H 2 O ) (aq)                        | - 2.40 ± 0.24                   |

[A] = 0.289CaF 2 (cr) + [0.361NaF · 0.940AlF 3 · 5.060H2 SiF 6 · 3982.56HF · 13830.48H2 O](aq).

[C] = [0.940AlF 3 · 5.060H2 SiF 6 · 3982.56HF · 13830.48H2 O](aq).

[B] = [5.060H 2 SiF 6 · 3985.38HF · 13827.66H2 O](aq).

[D] = [0.361NaF · 0.940AlF 3 · 5.060H2 SiF 6 · 3982.56HF · 13830.48H2 O](aq).

The values of /Delta1 r H o 2 to /Delta1 r H o 6 were calorimetrically measured or taken from the literature by the authors [143]. The enthalpy of formation of mordenite is related with /Delta1 r H o (8.9) by

```
/Delta1 f H o ( Ca0.289 Na 0.361 Al 0.940 Si 5.060 O 12.000 · 3.468 H2 O, cr ) = -/Delta1 r H o ( 8.9 ) + 0.289 /Delta1 f H o ( CaF2, cr ) + 0.361 /Delta1 f H o ( NaF, cr ) + 0.940 /Delta1 f H o [ Al(OH) 3 , cr, gibbsite ] + 5.060 /Delta1 f H o ( SiO2 , cr, silicalite ) + 2.530 /Delta1 f H o ( H2O,l ) -0.94 /Delta1 f H o ( HF · 3.440845 H 2 O, aq ) (8.11)
```

Using /Delta1 f H o ( CaF2, cr) = -1225.9 ± 6.3 kJ mol -1 [107], /Delta1 f H o (NaF, cr) = -575.4 ± 0.8 kJ mol -1 [107], /Delta1 f H o [Al(OH) 3 , cr, gibbsite] = -1294.9 ± 1.2 kJ mol -1 [143], /Delta1 f H o ( SiO2, cr, silicalite) = -905.20 ± 0.84 kJ mol -1 [154], /Delta1 f H o ( H2O, l ) = -285.830 ± 0.040 kJ mol -1 [58], and /Delta1 f H o (HF · 3.440845 H2O, aq) = /Delta1 f H o (HF · 3.441H2O, aq) = -320.95 ± 0.67 kJ mol -1 [143,155] it is possible to derive /Delta1 f H o ( Ca0.289Na0.361Al0.940Si5.060O12.000 · 3.468H2O, cr ) = -6755.3 ± 4.8 kJ mol -1 .

Johnson et al. [143] also studied the dehydrated form of mordenite by reactionsolution calorimetry. Their results and the foregoing enthalpy of formation data lead to /Delta1 f H o ( Ca0.289Na0.361Al0.940Si5.060O12.000, cr ) = -5661.7 ± 4.8 kJ mol -1 . From the enthalpies of formation of both forms of mordenite and the enthalpy of formation of liquid water already quoted ( -285.830 ± 0.040 kJ mol -1 ), it is possible to conclude that at 298.15 K, the enthalpy of dehydration of mordenite, which corresponds to the reaction

<!-- formula-not-decoded -->

is /Delta1 r H o (8.12) = 29.5 ± 2.0 kJ mol -1 per mole of water. This corresponds to the average binding enthalpy of zeolitic H2O in mordenite.

Johnson et al. [143] used low-temperature adiabatic calorimetry and hightemperature drop calorimetry to obtain the heat capacity of both forms of mordenite as a function of the temperature. These results and the results of the reaction-solution calorimetric studies discussed herein, enabled the tabulation of the thermodynamic properties ( C o p , S o , /Delta1 f H o , and /Delta1 f G o ) of mordenite from 0 K to 500 K and dehydrated mordenite from 0 K to 900 K.

## Heat Flow Calorimetry

Heat flow calorimeters, also known as 'heat flux,' 'heat conduction,' or 'heat leakage' calorimeters, are instruments where the heat output or input associated with a given phenomenon is transferred between a reaction vessel and a heat sink (recall figure 6.2). This heat transfer can be monitored with high thermal conductivity thermopiles containing large numbers of identical thermocouple junctions regularly arranged around the reaction vessel (the cell ) and connecting its outside wall to the heat sink (the thermostat ).

The determination of the heat flow relies on the so-called Seebeck effect. An electric potential, known as thermoelectric force and represented by E , is observed when two wires of different metals are joined at both ends and these junctions are subjected to different temperatures, T 1 and T 2 (figure 9.1a). Several thermocouples can be associated, forming a thermopile (figure 9.1b). For small temperature differences, the thermoelectric force generated by the thermopile is proportional to T 1 -T 2 and to the number of thermocouples of the pile ( n ) :

<!-- formula-not-decoded -->

where ε ′ is the thermoelectric power of a single thermocouple ( ε ′ = dE / dT ) .

<!-- formula-not-decoded -->

Assuming that the heat transfer is made by conduction through the thermocouple wires, the heat flow rate ( Φ = dQ / dt , where t is time) between the systems at temperatures T 1 and T 2 is also directly related to the difference T 1 -T 2:

λ being the average thermal conductivity of the metal wires. Therefore,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In conclusion, the area of a plot of E against time (the measuring curve or thermogram ) will be proportional to the net heat input or output ( Q ) . In practice, the proportionality constant ( λ/ n ε ′ ) is determined in a separate calibration experiment (see following discussion).

and

<!-- image -->

The reverse of the Seebeck effect is called the Peltier effect and results from flowing an electric current through the circuits of figure 9.1. If the junctions are initially at the same temperature, a temperature gradient will be developed; for instance, in the case of figure 9.1a, one of the junctions will cool and the other will warm. Associated with this electric current there will also be a Joule (resistive) effect, so that the net power ( P ) produced at each junction is given by

<!-- formula-not-decoded -->

where i is the electric current, Π the Peltier coefficient, and R the electric resistance. The Peltier effect can thus be used as a cooling device, by controlling i . If i = i 0 when P = 0 (the heating caused by the Joule effect is balanced by the Peltier cooling in one of the junctions), then Π i 0 = Ri 2 0 and i 0 = Π/ R . For i &lt; i 0, the Peltier effect will prevail, that is, P &lt; 0 in the cooler junction.

The first heat flow calorimeter based on Seebeck, Peltier, and Joule effects was built by Tian at Marseille, France, and reported in 1923 [156-158]. The set-up included two thermopiles, one to detect the temperature difference T 1 -T 2 and the other to compensate for that difference by using Peltier or Joule effects in the case of exothermic or endothermic phenomena, respectively. This compensation (aiming to keep T 1 = T 2 during an experiment) was required because, as the thermopiles had a low heat conductivity, a significant fraction of the heat transfer would otherwise not be made through the thermopile wires and hence would not be detected.

Tian's instrument had several important advantages over other types of calorimeter available at the time, such as isoperibol or adiabatic instruments: (1) It could monitor rather small temperature changes (less than 10 -4 K) and therefore minute samples could be used; (2) it could be applied to investigate the thermochemistry of very slow phenomena (up to about 24 h); and (3) the use of the compensating Peltier cooling or Joule heating allowed one to investigate the

'thermokinetics' (change of heat input or output with time) of a process under isothermal conditions.

Tian's instrument was refined by Calvet and his co-workers (figure 9.2) at the Marseille laboratory [156-159]. One of the most important improvements resulted from a regular arrangement of a large number of identical thermocouples connecting the cell to the heat sink, which allowed the heat flow to be related to the measured thermoelectric force, independently of the temperature distribution at the outside wall of the cell and no matter which fraction of the heat was transferred through the wires. This is easily shown by considering that a single thermocouple element is responsible for conducting a fraction ( x ) of the total heat transferred

Figure 9.2 A schematic diagram of a Calvet's calorimeter, adapted from [157]. Only one of the twin calorimetric units (A), with its thermopiles (T) is shown. These units fit into highconductivity metal blocks (B). C are cones for equipartition of thermal fluctuations; D is a thick metal cylinder surrounded by a series of canisters (E). H is an electric heater, and the outer cylinder (I) is a thermal insulator.

<!-- image -->

from an 'elementary' area of the outside wall of the cell, where the temperature ( T 1 ) is assumed to be uniform [156,157]. For each thermocouple (i):

<!-- formula-not-decoded -->

This equation, together with equation 9.1 for a single thermocouple,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

As all the thermocouples are identical, x ε ′ /λ is constant. Therefore, the thermoelectric force of the pile formed by the n thermocouples connected in series is given by

<!-- formula-not-decoded -->

which shows that the measured E is proportional to the total heat transferred between the cell and the heat sink, no matter what the temperature distribution may be at the cell wall. Actually, equation 9.9 is not strictly valid because the thermocouples do not cover the whole area of the cell wall, but it holds as a good approximation, particularly when the wall of the calorimeter has a high thermal conductivity, thus avoiding cold and hot spots [2].

Another problem related to the validity of equation 9.9 is that equation 9.6 applies only to heat conduction. If T 1 -T 2 is large, some significant fraction of heat will be transferred by convection and radiation and thus will not be monitored by the thermopile. Consequently, the use of partial compensating Peltier or Joule effects was essential in the experiments involving Calvet' s calorimeter, whose thermopiles had a fairly low thermal conductivity.

As a practical consequence of equation 9.9, the contents of the cell do not need to be stirred to achieve a uniform temperature. This is a clear advantage whenever the heat output or input and the heat of stirring are comparable.

A second improvement in Calvet's calorimeter is that a differential set-up was adopted that aimed to suppress temperature drifts and fluctuations of the heat sink. This was achieved by coupling two calorimetric units in opposition to each other, so the measured thermoelectric force was the difference between the thermoelectric forces of the sample cell and the reference cell . The latter may remain at the temperature of the thermostat while the heat output or input related to the event under investigation occurs in the sample cell.

A much more detailed discussion of the advantages of Calvet's design, as well as the underlying theoretical background, were reported by Calvet himself [157-159]. For instance, whereas in Tian' s calorimeter a water bath was used, in Calvet' s this was replaced by a metal block, allowing thermochemical studies at high temperatures (above 1000 ◦ C). Longer experiments (over a month) were also possible due to the improved stability of Calvet' s calorimeter. Finally, its higher sensitivity ( ∼ 0.2 µ W) allowed the use of even smaller samples.

leads to

Very high sensitivity and the concomitant use of minute samples justify the descriptor 'microcalorimeter' for many heat flow instruments. In general, a calorimeter can be labeled a microcalorimeter when its sensitivity is better than ∼ 10 µ W. Note, however, that some authors adopt a tighter definition, indicating 1 µ Wasthe sensitivity upper limit [160]. The cell volume is usually in the range of 0.5-25 cm 3 .

Building a heat flow microcalorimeter is not trivial. Fortunately, a variety of modern commercial instruments are available. Some of these differ significantly from those just described, but the basic principles prevail. The main difference concerns the thermopiles, which are now semiconducting thermocouple plates instead of a series of wire thermocouples. This important modification was introduced by Wadsö in 1968 [161]. The thermocouple plates have a high thermal conductivity and a low electrical resistance and are sensitive to temperature differences of about 10 -6 K. Their high thermal conductivity ensures that the heat transfer occurs fast enough to avoid the need for the Peltier or Joule effects.

Modern heat flow microcalorimeters employ a diversity of heat sinks and cells, depending on the applications for which they were designed. The heat sinks can be water baths, kept at a constant temperature ( ± 5 × 10 -4 K) and typically operating in the range of 20-80 ◦ C, or metal blocks, allowing much wider temperature ranges (e.g., -196 ◦ C to 200 ◦ C, 20 ◦ C to 1000 ◦ C). In some cases it is possible to scan the temperature at a predetermined rate (see chapter 12).

All modern heat flow calorimeters have twin cells; thus, they operate in the differential mode. As mentioned earlier, this means that the thermopiles from the sample and the reference cell are connected in opposition, so that the measured output is the difference between the respective thermoelectric forces. Because the differential voltage is the only quantity to be measured, the auxiliary electronics of a heat flux instrument are fairly simple, as shown in the block diagram of figure 9.3. The main device is a nanovoltmeter interfaced to a computer for instrument control and data acquisition and handling. The remaining electronics of a microcalorimeter (not shown in figure 9.3) are related to the very accurate temperature control of the thermostat and, in some cases, with the

<!-- image -->

electrical calibration of the instrument. This calibration is made by using a sample cell containing a precision resistance ( R ) , which releases a known amount of heat ( Q ) when an electric current i flows during a given period of time t ( Q = Ri 2 t ) [162]. A very stable power supply and an accurate timer are therefore required.

Bearing in mind the features of heat flow microcalorimeters, in particular their high sensitivity and small sample requirements, it is not surprising that they have been widely applied to investigate the energetics of chemical and biochemical phenomena. Here we will illustrate the technique with the reactions involving the organometallic complexes bis (butadiene) iron carbonyl, Fe(CO)(1,3-C4H6 ) 2, and chromium hexacarbonyl, Cr(CO)6.

The thermochemistry of thermal decomposition of Fe(CO)(1,3-C4H6 ) 2, in the temperature range of 418-439 K, was investigated by Brown et al. [163] with a Calvet twin-cell microcalorimeter and an experimental procedure known as the 'drop calorimetric technique' [164]. In this procedure, a known mass of sample contained in a small glass capillary at room temperature is dropped into the sample cell of the calorimeter (Figure 9.4). To compensate for the heat effect of dropping the glass capillary into the sample cell, an identical but empty capillary is simultaneously dropped into the reference cell. This allows one to calculate the heat effect associated solely with the process taking place in the sample cell. As shown in Figure 9.4, the experiment can be done under an inert atmosphere of nitrogen or argon.

A sketch of the thermogram obtained for the thermal decomposition of Fe(CO)(1,3-C4H6 ) 2 at 418 K is shown in figure 9.5 [163]. The endothermic part reflects the heating (from 298 K to 418 K) and the melting of the sample and probably also some thermal decomposition. The exothermic peak of the thermogram was attributed to the polymerization of butadiene. Because area B is larger than A, the overall process (equation 9.10) is exothermic.

<!-- formula-not-decoded -->

Figure 9.4 Scheme of a reaction vessel used for the drop technique. Adapted from [164].

<!-- image -->

Figure 9.5 Thermogram (plot of the measured thermoelectric force versus time) of the thermal decomposition of Fe(CO)(1,3-C 4 H 6 )2 at 418 K. Adapted from [163].

<!-- image -->

Torelate the difference between the areasA and B with the enthalpy of reaction 9.10, a calibration had to be performed.As discussed, this calibration can be made by generating a known amount of heat in a resistor in the reaction vessel. Alternatively, we can make a 'chemical calibration,' involving a procedure that mimics the main experiment. For instance, if a known mass of iodine is dropped through the inlet system (and a similar empty capillary is dropped into the reference cell), the thermogram of the following process can be recorded:

<!-- formula-not-decoded -->

The enthalpy of this process can be accurately calculated from literature data. The standard enthalpy of sublimation of iodine is known at 298.15 K (62.42 ± 0.08 kJ mol -1 [58]), so we have (see section 2.4):

<!-- formula-not-decoded -->

where the enthalpy increment of gaseous iodine, the last term in the equation, can be obtained, for instance, from the JANAF Tables [107].

It is observed in figure 9.6 that the calibration thermogram has two peaks associated with endothermic effects. The first (C) reflects the heating and some sublimation of I2. The second (D), recorded after connecting both the sample and reference cells to an auxiliary vacuum line, accounts for the sublimation of the remaining sample and its removal from the cell. The calibration constant, ε , is simply the ratio between /Delta1 r H o ( 9.11 ) and the total area (C + D).

Let us return to the thermal decomposition of Fe(CO)(1,3-C4H6 ) 2. Once the calibration constant is known, the enthalpy of the net process 9.10 can be calculated as the product of ε and the area (A + B). The next step is to correct this value to 298.15 K by using heat capacity data. This exercise is, however, complicated by the cyclobutadiene polymerization. Brown et al. analyzed the reaction products by mass spectrometry and found several oligomers, in particular the dimer (C4H6 ) 2 and the trimer (C4H6 ) 3 [163]. With such a mixture, it is difficult to ascribe the observed enthalpy change to a well-defined chemical reaction. This is discussed in the paper by Brown and colleagues, who were nevertheless able to recommend a value for the standard enthalpy of formation of the iron-olefin

Figure 9.6 A sketch of a calibration thermogram (sublimation of iodine).

<!-- image -->

complex.The discussion and the results do not concern us here. With this example we just wish to illustrate one of the most serious problems encountered in thermochemical studies involving thermal decompositions: These processes often yield products that are difficult to quantify. Fortunately, many thermal decompositions are 'clean' and afford accurate thermochemical data. In addition, the drop method can be applied to other reactions besides thermal decompositions. To illustrate this, we consider the example involving chromium hexacarbonyl.

AheatflowcalorimeterandthedropcalorimetricmethodwereusedbyConnor, Skinner, and Virmani to investigate the thermal decomposition of Cr(CO)6 at 514 K (the calibration was made with iodine as described above) [164]. The only peak observed corresponded to an endothermic process:

<!-- formula-not-decoded -->

The mean enthalpy observed for this reaction, based on six experiments, was 308.1 ± 4.7 kJ mol -1 . To correct this result to 298.15 K, an equation similar to 9.12 can be derived:

<!-- formula-not-decoded -->

The result obtained for /Delta1 f H o [ Cr ( CO ) 6 , cr ) ] is some 50 kJ mol -1 more positive than the recommended value, -980.0 ± 2.0 kJ mol -1 [149], a weighted mean of experimental results determined with several types of calorimeter. The large discrepancy is not due to an ill-assigned thermal decomposition reaction but to a slow adsorption of carbon monoxide by the chromium mirror that covered the vessel wall. This is an exothermic process and lowered the measured /Delta1 r H o ( 9.13 ) .

Using ( H o 514 -H o 298 ) Cr,cr = 5.46 kJ mol -1 and ( H o 514 -H o 298 ) CO,g = 6.35 kJ mol -1 [107], we obtain /Delta1 r H o 298 ( 9.13 ) = 264.5 ± 4.7 kJ mol -1 . Finally, taking the standard enthalpy of formation of carbon monoxide, /Delta1 f H o ( CO,g ) = -110.53 ± 0.17 kJ mol -1 [58], we calculate /Delta1 f H o [ Cr ( CO ) 6 , cr ) ] = -(264.5 ± 4.7) + 6 × ( -110.53 ± 0.17) = -927.7 ± 4.8 kJ mol -1 .

To avoid the formation of the metallic mirror and thus the adsorption process, Connor, Skinner, and Virmani used the microcalorimeter to examine the iodination of chromium hexacarbonyl at 514 K:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The experimental procedure was as described, the only difference being that a capillary containing a suitable amount of I2 was dropped into the reaction vessel (and the calorimeter allowed to stabilize) before the Cr(CO)6 sample was dropped.After recording the thermogram corresponding to reaction 9.15, the cell was removed and the contents analyzed to determine n (which varied from 0.30 to 0.38 in five separate experiments).

The enthalpy observed for each run involving reaction 9.15 can be adjusted for n = 0. This can be done by considering reaction 9.16 for n = 1/2.

<!-- formula-not-decoded -->

The standard enthalpies of formation of CrI2 and CrI3 at 298.15 K are tabulated in the NBS Tables of Chemical Thermodynamic Properties [165] as -156.9 ± 8.0 kJ mol -1 and -205.0 ± 8.0 kJ mol -1 , respectively (the uncertainty intervals are estimates). Using /Delta1 f H o ( I2, g ) = 62.42 ± 0.08 kJ mol -1 [58], we obtain /Delta1 r H o ( 9.16 ) = 79.3 ± 11.3 kJ mol -1 ( n = 1 / 2 ) .

Connor, Skinner, andVirmani assumed that the /Delta1 r H o ( 9.16 ) value at 298.15 K would be the same at 514 K. This assumption can be checked because the heat capacities of all the species are now available [166]. The standard heat capacities of the reaction ( /Delta1 r C o p ) at 298.15 K and 514 K are 19.55 J mol -1 K -1 and 18.89 J mol -1 K -1 , respectively. Using the average value, 19.22 J mol -1 K -1 , we obtain

<!-- formula-not-decoded -->

which is small compared with the uncertainty interval in /Delta1 r H o ( 9.16 ) , ± 11.3 kJ mol -1 . Nevertheless, we use this adjustment to evaluate the enthalpy of reaction 9.18.

<!-- formula-not-decoded -->

The calculation was made by adding /Delta1 r H o ( 9.15 ) to 2 n /Delta1 r H o 514 ( 9.16 ) for each experimental value of n given in the paper by Connor, Skinner, and Virmani, and it leads to /Delta1 r H o ( 9.18 ) = 142.4 ± 4.4 kJ mol -1 , where the error bar does not include the estimated uncertainty in /Delta1 r H o 514 ( 9.16 ) .

Wecan now proceed to the final step before obtaining the standard enthalpy of formation of chromium hexacarbonyl. The enthalpy of reaction 9.18 at 298.15 K is related to /Delta1 r H o ( 9.18 ) by

<!-- formula-not-decoded -->

Using ( H o 514 -H o 298 ) I2 ,g = 8.04 kJ mol -1 , ( H o 514 -H o 298 ) CO,g = 6.35 kJ mol -1 [107],and ( H o 514 -H o 298 ) CrI2,cr = 16.43kJmol -1 [166],weobtain /Delta1 r H o 298 ( 9.18 ) = 95.9 ± 4.4 kJ mol -1 . Finally, taking the standard enthalpies of formation of CO, I2(g), and CrI2 already quoted, we calculate /Delta1 f H o [ Cr ( CO ) 6 , cr ) ] = -978.4 ± 9.2 kJ mol -1 , in good agreement with the recommended value, -980.0 ± 2.0 kJ mol -1 [149].

The greatest advantage of the drop calorimetric technique developed by the Manchester group is that it requires very little sample. Typically, less than 2 mg

is needed for each run. This is particularly important for many organometallic complexes, which are difficult to prepare and purify in large quantities. Nevertheless, as illustrated by the previous examples, the technique should be applied with caution because side reactions or other phenomena (such as adsorption) may occur. This is particularly true for thermal decompositions. The halogenation reactions are less prone to errors, and indeed they were widely used by the Manchester group to study the thermochemistry of a wealth of organometallic complexes [144,149,167]. The halogenation included reactions with not only iodine but also bromine. For instance, the standard enthalpy of formation of Cr(CO)6 was also obtained through its reaction with Br2 [168], and the result agrees with the one determined here.

A marginal but very important application of the drop calorimetric method is that it also allows enthalpies of vaporization or sublimation [162,169] to be determined with very small samples. The procedure is similar to that described for the calibration with iodine-which indeed is a sublimation experiment. Other methods to determine vaporization or sublimation enthalpies using heat flow calorimeters have been described [170-172]. Although they may provide more accurate data, the drop method is often preferred due to the simplicity of the experimental procedure and to the inexpensive additional hardware required. The drop method can also be used to measure heat capacities of solids or liquids above ambient temperature [1,173].

The drop calorimetric method is by no means the only application of heat flow microcalorimetry used to investigate the energetics of molecules. Other microcalorimeter designs, also relying on the heat flow principle, have been used to study the thermochemistry of reactions in solution [174,175] and oxygencombustion reactions [17,171,176-178]. Once again, their main advantages relative to the more common isoperibol calorimeters (see chapters 7 and 8) are the considerable reduction in the sample size and the possibility of examining 'slow' reactions (i.e., those reactions that take more than about 15 minutes to reach equilibrium).

## 10

## Photocalorimetry

Most experimental techniques addressed in the present book are suitable for investigating the thermochemistry of thermally activated reactions, that is, those reactions whose activation barrier can be overcome by increasing the thermal energy of the reactants. This thermal energy, which is the average sum of molecular translational, rotational, and vibrational energies, can be changed by varying the temperature of the reactants.

Some chemical reactions, however, do not occur by thermal activation. They require larger energy inputs-big enough to raise the electronic energy of at least one of the reactants and even induce the cleavage of a chemical bond. This 'surgical' energy promotion is only attainable by electromagnetic radiation with a suitable wavelength. Visible light (420-700 nm) or ultraviolet radiation are typically used because the energies involved are in the same range of electronic excitation energies and of bond dissociation enthalpies, for example, a 700 nm photon corresponds to an energy of 170.9 kJ mol -1 (see conversion factors in appendix A).

The reactions initiated by electromagnetic radiation are said to be photochemically activated . Note that only the initiation step may require the absorption of one or more photons (a photochemical reaction ). Subsequent steps of the mechanism may be 'dark reactions,' proceeding by thermal activation.

The thermochemical study of photochemical or photochemically activated processes is not amenable to most of the calorimeters described in this book, simply because they do not include a suitable radiation source or the necessary auxiliary equipment to monitor the electromagnetic energy absorbed by the reaction mixture. However, it is not hard to conceive how a calorimeter from any of the classes mentioned in chapter 6 (adiabatic, isoperibol, or heat flow) could be modified to accommodate the necessary hardware and be transformed into a photocalorimeter .

A general discussion of the basic principles of photocalorimetry, which we closely follow in the ensuing discussion, was made by Teixeira and Wadsö [179]. An amount of radiant energy E is supplied to the calorimetric cell and absorbed by the reaction mixture, initiating a chemical reaction. Assuming that the process occurs at constant pressure, and representing the enthalpy change of that reaction by /Delta1 obs H , the energy balance inside the cell is simply

(10.1)

where Q is the heat measured by the calorimetric system. Note that the quantities in this equation are those directly involved in the experiment and therefore are not given in molar units.

It is possible that only a fraction of the radiant energy supplied to the calorimeter would be absorbed by the reaction mixture. Part of that radiation can be reflected ( E r) and, if the reaction vessel is transparent, another fraction can be transmitted to the surroundings ( E t ). Furthermore, the electronically excited states of the reactants may decay by luminescence, so more energy ( E l) may be lost to the surroundings. If these three contributions are taken into account, equation 10.1 becomes

<!-- formula-not-decoded -->

To obtain /Delta1 obs H we need to evaluate E and the last three terms in equation 10.2. This can be done in a separate experiment (where the same radiant energy E is supplied), by measuring Q for a process whose /Delta1 obs H is accurately known, or, morecommonly,bymeasuring Q whenanonphotoreactivesubstanceiscontained in the reaction cell. In this case /Delta1 obs H = 0 and we have

<!-- formula-not-decoded -->

where the prime indicates the quantities for the reference experiment. Subtracting this equation from equation 10.2 we arrive at

<!-- formula-not-decoded -->

For a well-designed set-up, and if the main and reference experiments are performed under the same conditions, it is fair to assume that the reflected energies will be small and that E ′ r ≈ E r. With regard to the transmittance and the luminescence energies, we have to consider two possibilities. If the calorimetric cell is opaque, then these terms will all be zero, that is,

<!-- formula-not-decoded -->

On the other hand, if the calorimetric cell is transparent, then E t , E ′ t , E l, and E ′ l have to be determined for example by using data for the transmittance of the media and fluorescence and phosphorescence quantum yields (see following discussion).

Once /Delta1 obs H is known, then the molar enthalpy of the reaction under study is given by

<!-- formula-not-decoded -->

n being the amount of substance of the limiting reactant converted into products. This conversion efficiency can be directly obtained by chemical analysis of the final state of the reaction mixture or calculated from the overall quantum yield of the reaction (number of reactant molecules that react for each photon absorbed [180]), Φ :

<!-- formula-not-decoded -->

where N is the number of photons absorbed and N A is Avogadro's number. Because the quantum yield refers to radiation with a single wavelength λ , we can apply equation 10.7 to determine n only when monochromatic radiation with the same wavelength is used in the calorimetric experiment.

Avalue of N can be obtained from the reference experiment. Assume that the radiant energies ( E ) supplied during the main and the reference experiments are identical. Now recall equation 10.3, and suppose that E ′ r is negligible, and that the nonphotoreactive substance does not decay by fluorescence or phosphorescence ( E ′ l = 0). Because its transmittance ( T ) is easily measurable and E ′ t = TE , equation 10.3 becomes

<!-- formula-not-decoded -->

The radiation energy supplied to the reference cell ( E ) can be computed using this equation. As

<!-- formula-not-decoded -->

where h is Planck' s constant and c the speed of light, N can be calculated. Note that if the cell is opaque, then E ′ t = 0 and equation 10.8 simplifies to E = Q ′ .

The theory just described was the basis of photocalorimetric experiments reported in the literature, involving several types of instruments and addressing a variety of problems [179].To the best of our knowledge, the first photocalorimeter was built by Magee et al. in the late 1930s and applied to the determination of the quantum yield of photosynthesis by green algae [181]. Here we have chosen to illustrate the principles of photocalorimetry with two examples, one involving an isoperibol photocalorimeter developed by Adamson et al. [182-184] and another based on a heat flow calorimeter built by Teixeira and Wadsö [185].

The instrument described by Adamson and colleagues is shown in figure 10.1. The latest reported version consisted of a 10 cm 3 glass reaction vessel that contained a bar for magnetic stirring and was separated from a thermostated jacket by an evacuated shell. The jacket temperature could be maintained at 25.000 ± 0.001 ◦ C. Monochromatic radiation entered the reaction vessel through

<!-- image -->

reaction vessel

Figure 10.1 A reaction-solution isoperibol photocalorimeter, built by Adamson et al. Adapted from [182].

two quartz windows. The remaining calorimetric components (a thermistor to measure temperature and an electrical resistance to determine the calibration constant) are common in many other isoperibol calorimeters (see chapters 7 and 8). The main optical hardware of the calorimeter was a 1 kW mercury-xenon lamp with stabilized output ( ± 1%), a collimator, filters (e.g., a filter containing water to absorb infrared radiation and a glass filter to block short-wavelength ultraviolet radiation), a shutter, and a monochromator. The bandwith at half-maximum intensity, for example, for a 4 mm slit, was 15 nm at 366 nm.

The thermochemistry of the ligand replacement reaction 10.10, where 'pip' indicates piperidine, was investigated by Adamson' s group, using cyclohexane as solvent [183].

<!-- formula-not-decoded -->

The procedure may start with the reference experiment, which, in the case under analysis, involved a solution of ferrocene in cyclohexane (ferrocene is a nonphotoreactive substance that converts all the absorbed 366 nm radiation into heat). With the shutter closed, the calorimeter was calibrated using the Joule effect, as described in chapter 8, yielding the calibration constant ε ′ . The same solution was then irradiated for a given period of time t ′ (typically, 2-3 min), by opening the shutter. The heat released during this period ( Q ′ ) , determined from the temperature against time plot and from the calibration constant (see chapter 8), leads to the radiant power (radiant energy per second) absorbed by the solution, P = Q ′ / t ′ .

Note that according to equation 10.8,

<!-- formula-not-decoded -->

the transmittance should also be accurately measured. However, the authors used solutions with optical densities in the range of 1-1.5 cm -1 . Because the optical path length of the 10 cm 3 cell was 3.5 cm, practically 100% of the radiation was absorbed ( T = 0). Hence, Q ′ = Pt ′ = E .

The main experiment followed a similar procedure. The Joule calibration yields ε . The cyclohexane solution of Cr(CO)6 and piperidine was irradiated for a period t . The heat released ( Q ) provided /Delta1 obs H via equation 10.5. If t ′ /negationslash= t , then Q ′ derived from the reference experiment needs to be multiplied by t / t ′ . Alternatively, we can simply derive the rate of temperature increase during the irradiation. This rate multiplied by ε is equal to rate of heat production ( Q / t ), which Adamson and co-workers called F . The difference between the radiant power ( P ) and F gives /Delta1 obs H / t .

To calculate /Delta1 r H ( 10.10 ) , it is necessary to know n , the amount of substance of Cr(CO)6 consumed during period t . This is best done by analyzing the final reaction mixture, but as mentioned, it can also rely on the reaction quantum yield, Φ . From equations 10.6, 10.7, and 10.9 we obtain

<!-- formula-not-decoded -->

Because /Delta1 obs H = Q ′ -Q and E = Q ′ this becomes

<!-- formula-not-decoded -->

where N A hc /λ for 366 nm photons corresponds to 326.8 kJ mol -1 . The alternative equation to 10.13 (using the quantities P and F ) is

<!-- formula-not-decoded -->

where f = ( P -F )/ P represents the coefficient of conversion of light into chemical energy [182].

The data obtained by Nakashima and Adamson for reaction 10.10 were f = 0.0174 and Φ = 0.58 ± 0.01 [186]. This reaction quantum yield was actually derived from the analytical determination of n ( n = P Φ ), and therefore the final value /Delta1 r H ( 10.10 ) = 9.8 ± 4.2 kJ mol -1 is probably more accurate than if it had relied on a literature value for the quantum yield. The uncertainty recommended by the authors includes the experimental errors in P and F values.

The isoperibol reaction-solution photocalorimeter shown in figure 10.1 has been applied to study the thermochemistry of a number of reactions involving coordination and organometallic complexes and also organic compounds [182-184,186-188]. Although, as stated by Harel and Adamson, a typical error bar in f is ± 0.01 [184], implying, for example, an uncertainty of only 6 kJ mol -1 in /Delta1 r H when λ = 366 nm and Φ = 0.58, several larger disagreements with literature values were noted. In other cases, the agreement is good. As recognized by Adamson and co-workers, the method suffers from several error sources. For instance, a low precision is expected when the reaction quantum yield is also low, even if n is very accurately determined by chemical analysis (see equation 10.14 and bear in mind that the experimental error in f will be divided by a small value of Φ ). On the other hand, the radiation wavelength will affect both the precision and the accuracy of the final /Delta1 r H result. Shorter wavelength photons not only multiply the error in f but also affect the accuracy of f itself (a variation of the radiation intensity from the reference to the main experiment will lead to more serious errors in the case of high-energy photons). Another (probably minor) error source intrinsic to the photocalorimeter of figure 10.1 results from the use of magnetic stirring. A speed-controlled mechanical stirrer would ensure a more constant heat of stirring.

Some of these problems can be overcome with a different calorimetric design (see later discussion). Other problems, which are more dependent on the chemistry and physics of the process under study than on the instrumentation, require careful attention. Unnoticed side reactions or secondary photolysis are examples, but one of the most serious error sources in photocalorimetry is caused by the quantum yield values, particularly, as explained, when they are small. Unfortunately, many literature quantum yields are unreliable, and it is a good practice to determine n for each photocalorimetric run. Errors in Φ are often caused by 'inner filter effects,' that is, photon absorption by reaction products.

Because the instrument sketched in figure 10.1 is an isoperibol calorimeter, it only allows the study of fairly rapid processes (less than about 15 min). This

handicap disappears with the heat flow photocalorimeter built by Teixeira and Wadsö, shown in figure 10.2 [185].The instrument relies on a commercial version of a microcalorimeter developed by Wadsö's group [189,190]. It consists of two twin calorimetric units immersed in a thermostatic bath controlled to ± 10 -4 K, each one containing a radiation-absorbing cell and a reference cell . One of the units (P) is used to determine the heat flow associated with the photochemical process under study and the other (R) monitors the radiant power supplied to the system. As in other heat flow calorimeters (see chapter 9), the thermopiles of the two cells in each unit are connected in opposition, so that the measured output represents the difference between the respective thermoelectric forces. This differential signal from each unit is amplified, recorded, and integrated by a computer.

Theradiation source for the twin calorimeter of figure 10.2 is a 100 W tungsten lamp. The wavelength is selected by a monochromator, and the light is split in two parts and led into the radiation-absorbing cells of each unit by three light cables. With a 2 mm slit, the band pass is about 13 nm, and for radiation with λ = 436 nm the power delivered to each cell is about 60 µ W. The reference cells are simply steel rods and receive no light.

Figure 10.2 The twin unit version of a heat flow photocalorimeter, built by Teixeira and Wadsö. Adapted from [185].

<!-- image -->

The radiation-absorbing cell of the main unit (P) is the photochemical reactor, that is, it contains the solution to be examined. It is a Teflon-coated steel vessel with a volume of only 3 cm 3 , provided with mechanical stirring. The other radiation-absorbing cell, in the reference unit (R), is a steel rod with three holes for the optical fibers.

The calibration of the calorimetric unit P , leading to the calibration constant ε (see chapter 9), can be made by the Joule effect, with a resistor inserted into the photochemical reactor cell. As justified shortly (equation 10.16), no calibration is required for the photoinert cell in unit R.

Before the experiment, the photochemical reactor is filled, for example, with the solvent of the sample solution, and both radiation-absorbing cells are irradiated typically for a period of less than 1 h. Because the cells are not transparent, all the radiation supplied is quantitatively converted to heat. The thermograms (see chapter 9) of units P and R are recorded and integated. The ratio of their areas, respectively A P0 and A R0, yields the so-called constant of the instrument, C λ :

<!-- formula-not-decoded -->

For the photochemical experiment reactor P is charged with the solution of interest, and again both radiation-absorbing cells are irradiated. The area of the thermogram from the reference unit R ( A R1) multiplied by C λ is proportional to the radiant energy ( E ) supplied to the photochemical reactor. On the other hand, the area of the thermogram from unit P ( A P1) will reflect not only that radiant energy but also the enthalpy change of the photochemically activated process ( /Delta1 obs H ). Therefore,

<!-- formula-not-decoded -->

Finally, the molar enthalpy of the reaction can be calculated as described, dividing /Delta1 obs H by the amount of substance of the limiting reactant converted to products ( n ; see equation 10.6). Alternatively, the value of the quantum yield and equation 10.13 can be used ( Q ′ = A R1 C λε and Q = A P1 ε ).

As shown by equation 10.15, C λ measures the ratio of the radiant energies supplied to the units P and R. To ensure that this ratio remains constant, so C λ can be used in equation 10.16, the geometry of the optical hardware, particularly the connections of the light cables to the monochromator, should not be changed. With this condition in mind, another advantage of the twin unit arrangement as compared with the calorimeter in figure 10.1 is now obvious: Light source intensity fluctuations will cancel out.

Other error sources discussed for the isoperibol instrument are not a problem in Teixeira and Wadsö' s microcalorimeter. For instance, as shown by equations 10.15 and 10.16, the radiation wavelength does not influence the precision or the accuracy of the final /Delta1 r H result. However, the precision is still affected when the reaction quantum yield is low, because the experimental error will be divided by a small value of n . On the other hand, problems like side reactions or secondary photolysis, already mentioned, that are not related to the instrumental design may also lead to large errors.

The number of chemical reactions that have been examined with the heat flow microcalorimeter of figure 10.2 is still fairly small. We have selected reaction 10.17, the photochemical isomerization of trans - to cis -azobenzene, to illustrate the method.

<!-- formula-not-decoded -->

Although the instrumentation used by Dias et al. [191] to study the thermochemistry was in most respects similar to the one just described, the authors made a significant change in the experimental procedure. Instead of the two calorimetric units P and R, they used only one unit. In this single unit, one of the cells was the photocalorimetric reactor and the other was the photoinert cell. The main disadvantage of the new arrangement is that the experimental results may be affected by intensity variations in the light source because equation 10.15 no longer applies. In addition, the new set-up requires that the amount of light entering the two cells remain constant over the whole irradiation period. As stated by the authors, this condition was achieved by adjusting the lamp position (with solvent in the photochemical reactor), so that the net signal was zero. In a heat flow calorimeter, where the thermopiles are connected in opposition (see foregoing discussion and also chapter 9), this means that the heat power produced in each cell is the same. If the balanced geometry is maintained, it should also take care of slight intensity fluctuations because these will not affect the fraction of the beam supplied to each cell.

It is pertinent to ask why Dias et al. decided to use one unit instead of two (we add that their microcalorimeter has not two but four of those units!). The cost was obviously not an issue in their case. However, by testing this new approach they have shown that it is possible to use other types of heat flow microcalorimeters-containing only two cells (or one unit)-in photocalorimetric studies.

The experimental procedure adopted in the thermochemical study of reaction 10.17 was fairly simple. First, an electrical calibration was made. Then, after balancing the light input to the cells, 2.7 cm 3 of a 7 × 10 -3 mol dm -3 solution of trans -azobenzene in heptane was added to the photochemical reactor. This solution was irradiated for a certain period (1.5-3.8 h) with 436 nm light, and the thermogram was recorded. The area of this thermogram multiplied by the calibration constant ( ε ) gives /Delta1 obs H .

The calculation of the molar enthalpy of reaction 10.17, /Delta1 r H ( 10.17 ) , requires the amount of substance of trans -azobenzene consumed. In seven independent experiments, n was determined spectroscopically and varied between ∼ 4 × 10 -7 mol and 15 × 10 -7 mol [191]. Note that it was not possible to use equation 10.13, evenif the quantum yield were known, because the the radiant energy ( E ) supplied to the photochemical reactor was not measured.

The mean value obtained for /Delta1 r H ( 10.17 ) was 48.9 ± 2.3 kJ mol -1 [191], which is in excellent agreement with another photocalorimetric result, 49.0 ± 5.4 kJ mol -1 , reported by Adamson et al. [182], who used the calorimeter of figure 10.1 and cyclohexane as solvent.

The enthalpy of the reverse of reaction 10.17, the cis → trans isomerization reaction is thermally activated and thus can be determined by isoperibol reactionsolution calorimetry (however, because the reaction is slow, a catalyst must be used). These experiments were also made by Dias et al. and led to -49.1 ± 1.0 kJ mol -1 for reaction 10.18.

<!-- formula-not-decoded -->

The enthalpies of solution of cis - and trans -azobenzene in heptane (29.1 ± 0.7kJ mol -1 and 25.4 ± 0.4 kJ mol -1 , respectively) were also determined by reaction solution calorimetry and can be coupled with /Delta1 r H ( 10.17 ) = 48.9 ± 2.3 kJ mol -1 to yield /Delta1 r H ( 10.18 ) = -45.2 ± 2.4 kJ mol -1 . This value differs by some 4 kJ mol -1 from the photocalorimetric results.

Although the difference between the photocalorimetric and the reactionsolution results is small (the values agree within the combined uncertainties), it would be useful to compare data from other sources. Unfortunately, as noted by Dias and colleagues, combustion calorimetry does not seem to provide a good alternative because the available results are themselves in disagreement. Combustion studies by Cole and Gilbert [192] lead to /Delta1 f H o ( cis -PhNNPh, cr ) = 362.8 ± 3.0 kJ mol -1 and /Delta1 f H o ( trans -PhNNPh, cr ) = 320.5 ± 2.3 kJ mol -1 , yielding /Delta1 r H ( 10.18 ) = -42.3 ± 3.8 kJ mol -1 . Schulze et al. [193], on the other hand, obtained /Delta1 f H o ( cis -PhNNPh, cr ) = 367.2 ± 2.2 kJ mol -1 and /Delta1 f H o ( trans -PhNNPh, cr ) = 311.3 ± 3.0 kJ mol -1 , which afford /Delta1 r H ( 10.18 ) = -55.9 ± 3.7 kJ mol -1 . The standard enthalpy of formation of the crystalline trans -isomer was also redetermined by combustion calorimetry by Dias et al. and the result (308.6 ± 1.9 kJ mol -1 ) is in better agreement with the value recommended by Schulze et al.

Whatcanweconcludefromallthesedata?Althoughthetwophotocalorimetric values are in excellent agreement with each other, these values are problably less accurate than the reaction-solution calorimetric result. In any case, the 4 kJ mol -1 discrepancy is not a cause of concern regarding the general usefulness and reliability of carefully made photocalorimetry experiments.

## 11

## Titration Calorimetry

Titration calorimetry is a method in which one reactant inside a calorimetric vessel is titrated with another delivered from a burette at a controlled rate. This technique has been adapted to a variety of calorimeters, notably of the isoperibol and heat flow types [194-198]. The output of a titration calorimetric experiment is usually a plot of the temperature change or the heat flow associated with the reaction or physical interaction under study as a function of time or the amount of titrant added.

A primary use of titration calorimetry is the determination of enthalpies of reaction in solution. The obtained results may of course lead to enthalpies of formation of compounds in the standard state by using appropriate thermodynamic cycles and auxiliary data, as described in chapter 8 for reaction-solution calorimetry. Moreover, when reactions are not quantitative, both the equilibrium constant and the enthalpy of reaction can often be determined from a single titration run [197-206]. This also yields the corresponding /Delta1 r G o and /Delta1 r S o through equations 2.54 and 2.55.

Extensive use has been made of titration calorimetry as an analytical tool. These applications, which are outside the scope of this book, have been covered in various reviews [194,197,198,203,204,207].

The historical development of titration calorimetry has been addressed by Grime [197]. The technique is credited to have been born in 1913, when Bell and Cowell used an apparatus consisting of a 200 cm 3 Dewar vessel, a platinum stirrer, a thermometer graduated to tenths of degrees, and a volumetric burette to determine the end point of the titration of citric acid with ammonia from a plot of the observed temperature change against the volume of ammonia added [208]. The capabilities of titration calorimetry have enormously evolved since then, and the accuracy limits of modern titration calorimeters are comparable to those obtained in conventional isoperibol (chapter 8) or heat-flow instruments (chapter 9) [195,198].

The titration procedures described in the literature can be classified as continuous or incremental, depending on the mode of titrant addition. In the first case the titrant is continuously introduced in the reaction vessel at a programmed (not necessarily constant) rate during a run. The application of this method requires apparatus with quick response to temperature changes and can be used only to study fast reactions. Slow reactions (i.e., those with a reaction time longer than the equilibrium time of the reaction vessel) may be accurately studied by the

incremental method. In this case, the titrant is added in steps to the titrate, and the reaction is left to equilibrate between two consecutive additions. The incremental method is frequently used in conjunction with heat flow calorimeters, which, as discussed in chapter 9, are particularly suited for the study of slow reactions.

Computer-controlled motorized syringe-type precision burettes are generally employed nowadays for addition of titrant. The burettes are calibrated by weighing the amounts of distilled water they deliver over various time intervals. The delivery rate in units of volume per unit time is determined from the mass rate delivery using the density of water at the calibration temperature.

The accuracy of a titration calorimeter is normally assessed using the reactions of NaOH(aq) with HCl(aq) or HClO4(aq) [209,210]. The dissolution of crystalline tris(hydroxymethyl)aminomethane (THAM) in HCl(aq) has also been employed when the apparatus is equipped with a system for the introduction of solid samples (e.g., an ampule breaking device) [210]. As mentioned in chapter 8, the latter method is commonly recommended for testing conventional reaction-solution calorimeters [39,40].

Figure 11.1a shows a scheme of a widely used reaction vessel for isoperibol titration calorimetry [211]. It consists of a silvered glass Dewar A, which can be adjusted to a lid B supporting a stirrer C, a resistance D for electrical calibration, a thermistor E for temperature measurement, and a Teflon tube F for titrant delivery. The assembled Dewar and lid set-up is immersed in a constant

Figure 11.1 (a) Scheme of an isoperibol titration calorimetry apparatus: A: Dewar vessel; B: lid; C: stirrer; D: electrical resistance; E: thermistor; F: titrant delivery tube; G: O-ring seal. (b) Vessel for isothermal operation: A: stainless-steel, platinum, or tantalum cup; B: water-tight stainless steel container; C: heater; D: Peltier thermoelectric cooler; E: O-ring seal; F: heater and cooler leads. Adapted from [211].

<!-- image -->

temperature bath and the titrant delivery is controlled by means of a motorized buret. The lid B can also be adapted to a metal vessel suitable for heat flow isothermal calorimetry (figure 11.1b). This consists of a stainless-steel, platinum or tantalum cup A inside a watertight stainless steel container B. Under the cup and inside the container are a heater C and a Peltier thermoelectric cooler D (for a discussion of the Peltier effect see chapter 9), which are used to maintain a constant temperature inside A. The Peltier cooler removes heat from the system at constant rate, and the heat flux from the heater required to ensure a constant temperature inside the cup throughout a run is measured as a function of time.

The principles of titration calorimetry will now be introduced using isoperibol continuous titration calorimetry as an example. These principles, with slight modifications, can be adapted to the incremental method and to techniques based on other types of calorimeters, such as heat flow isothermal titration calorimetry. This method, which has gained increasing importance, is covered in section 11.2.

## 11.1 ISOPERIBOL CONTINUOUS TITRATION CALORIMETRY

Figure 11.2 shows a typical temperature-time curve for a continuous isoperibol titration calorimetry experiment involving an exothermic process. In the initial and final periods (between points a and b, and c and d, respectively), the observed temperature change is determined by the heat of stirring, the heat dissipated by the temperature sensor, and the difference between the temperature of the calorimetric vessel and the temperature of the thermostatic bath. The titration

Figure 11.2 Typical temperature-time curve for an isoperibol continuous titration calorimetric experiment involving an exothermic process.

<!-- image -->

takes place between points b and c. The reaction, however, is complete between points b and q. The region between points q and c corresponds to the addition of excess titrant.

## Determination of /Delta1 H ICP

Asdiscussed in chapters 7 and 8, the initial step of the data analysis of a isoperibol calorimetry experiment is the determination of the enthalpy of the isothermal calorimetric process, /Delta1 H ICP, usually at the reference temperature of 298.15 K. The value of /Delta1 H ICP corresponding to any point p along the titration period is given by (recall the discussion of equation 8.1)

<!-- formula-not-decoded -->

where ε i is the initial energy equivalent of the calorimeter, ε p is the energy equivalent of the calorimeter at point p, T R is the reference temperature, and /Delta1 H exch is the enthalpic contribution due to the heat exchanged with the surroundings between points b and p. The term /Delta1 H tr results from the titrant being introduced into the reaction vessel at a temperature T s /negationslash= T R and can be computed from

<!-- formula-not-decoded -->

where V A denotes volume of titrant solution of mass density ρ A and massic heat capacity cp (A), added to the titrate up to the instant t p. An appropriate strategy to eliminate /Delta1 H tr and the need for the values of ρ A and cp (A) is to set the temperature of the thermostatic bath, T j, at the reference temperature (i.e., T j = T R ) and maintain the titrant immersed in the bath throughout the titration, thereby making T s = T j = T R.

Asusual, the energy equivalent of the calorimetric system, ε , must be obtained by calibration. The most common procedure to calibrate a titration calorimeter is supplying a known amount of electrical energy through a resistance heater, as described in chapter 8 for reaction-solution calorimetry. In titration calorimetry experiments, however, ε varies with the amount of titrant added during a run. Two methods have been used to determine ε as a function of the volume of calorimetric solution, thus enabling the evaluation of ε i and ε p in equation 11.1 [197,200]. Method 1 consists in the direct measurement of ε after various additions of titrant have been made. Method 2 is based on the separation of the energy equivalent of the calorimeter in two terms: ε o, which refers to the empty calorimetric vessel, and ε c, which corresponds to the sum of the heat capacities of the contents of the reaction vessel for a particular amount of titrant added. The latter approach is similar to that traditionally used in isoperibol combustion calorimetry (chapter 7). The value of ε c is generally computed from

<!-- formula-not-decoded -->

where V A, ρ A, and cp ( A ) are the volume, mass density, and massic heat capacity at constant pressure of the titrant, respectively, and V B, ρ B, and cp ( B ) are the corresponding quantities for the titrate. Equation 11.3 relies on the assumption

that ε c can be obtained by adding up the heat capacities of the titrate and the titrant. This is normally a good approximation because dilute solutions are frequently used in the experiments. Otherwise, to evaluate ε c, the heat capacity of the calorimetric solution as a function of the composition must be known.

The value of ε o is only constant for a fixed volume V of solution inside the calorimetric vessel. The change of ε o with V is primarily due to an increase of the reaction vessel wall in contact with the liquid as the liquid volume increases [197,200].This change, d ε o / dV , which is constant for well-designed calorimeters [197,200], can be determined by measuring ε o as a function of V . Because it has been found that as expected, ε o and d ε o / dV are independent of the nature of the liquid used in the calorimeter, they are normally determined by performing electrical calibrations with the calorimeter filled with different volumes of water [200]. The energy equivalent of the calorimeter at any point during a titration can therefore be calculated from

<!-- formula-not-decoded -->

Equation11.4isusuallyappliedundertheassumptionthatidealmixingoccurs, that is, V = V A + V B. As mentioned, this is a good approximation provided that diluted solutions of titrant and titrate are used.

Method 1 is the more accurate from the two methods because the energy equivalent of the calorimeter is directly measured as a function of V for each system under study. Method 2 is less time-consuming because once ε o and d ε o / dV have been determined, no further calibrations are necessary as long as the data needed to evaluate ε c are available.

The term /Delta1 H exch in equation 11.1 is given by

<!-- formula-not-decoded -->

where ( dQ / dt ) represents the heat flow rate to or from the surroundings, ε is the energy equivalent, g = ( dT / dt ) is the rate of temperature change of the calorimeter proper, and the subscript r refers to the titration period. As seen in chapter 7, for isoperibol calorimeters that obey Newton' s law of cooling, g is given by (equation 7.3)

<!-- formula-not-decoded -->

where k is the cooling constant, and u represents the contribution of all secondary thermal effects, such as the heat of stirring, resistive heating by the temperature sensor, etc. In titration calorimetry ε , k , and u continuously change along the titration period, as a result of the variation of the volume of solution inside the reaction vessel. Consequently, a different strategy from the one used in chapters 7 and8(where k and u weregenerally assumed to be constant) is required to account for /Delta1 H exch . Here, we closely follow the method described by Hansen et al. [212].

The rate of temperature change of the calorimeter proper during the initial and final periods and at any point during the titration period (denoted by the subscripts i, f, and r, respectively) are given by

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The dependence of k on the volume of liquid inside the calorimetric vessel can be determined by making electrical calibrations for different values of V . For each calibration, k i = k f and u i = u f , and equation

<!-- formula-not-decoded -->

may,forexample,beusedtoobtainthecorrespondingvalueof k (recall the discussion of equation 7.14 and alternative equations in chapter 7). In equation 11.10, g i and g f represent the slopes of the temperature versus time curve at midpoints of the initial and final periods, respectively, which correspond to the temperatures T i and T f (figure 11.2). It is usually possible to set the experiments so that k varies linearly with V . Figure 11.3 shows results obtained by Hansen et al. [212] for a small calorimetric vessel filled with water. In this example, it is a good approximation to express k as

<!-- formula-not-decoded -->

provided the volume of water in the vessel stays in the range 2.5-3.0 cm 3 .

The variation of u with V can be found by plotting g i as a function of ( T j -T i ) for different volumes of liquid inside the vessel.The intercepts at ( T j -T i ) = 0 for the various plots give the corresponding values of u . In the case of the calorimeter used by Hansen et al. [212] it was found that

<!-- formula-not-decoded -->

where β is a constant.

An equation giving g r in terms of experimentally measurable quantities can be derived as follows. Introducing equations 11.11 and 11.12 in 11.8 yields

<!-- formula-not-decoded -->

<!-- image -->

V

/cm 3

Figure 11.3 Variation of the cooling constant, k , with the volume of water, V , inside a small isoperibol calorimetric vessel [212].

Elimination of u i between equations 11.7 and 11.13 leads to

<!-- formula-not-decoded -->

From equations 11.9, 11.11, 11.12, and 11.14 it is finally possible to conclude that

<!-- formula-not-decoded -->

To calculate g r from equation 11.15, it is necessary to know α , β , V , g i , g f , T i , T f , and T j. The values of α and β are obtained as described. The volume of liquid inside the vessel can be calculated from the initial volume of titrate and the volume of titrant added. The temperature of the thermostatic jacket T j must be independently measured. The values of g i and T i , g f and T f are usually taken at the midpoints of the fore and after periods, respectively, although ε i refers to point b in the curve of figure 11.2.

Equation 11.5 can be solved once an analytical expression relating ε r g r with time has been fitted to the ε r g r values obtained for all data points of the curve in figure 11.2, collected up to point p. A simpler and usually adequate method consists in applying the trapezoidal rule:

<!-- formula-not-decoded -->

as in the case of the Regnault-Pfaundler method described in chapter 7. Note that for r = 0, ε r = ε i and g r = g i .

Hansen and colleagues found that the variation of k and u with the volume was particularly significant for vessels with volumes smaller than 25 cm 3 [212]. When these variations are negligible it can be concluded from equations 11.7-11.9 that

<!-- formula-not-decoded -->

because k i = k f = k r and u i = u f = u r. The use of equation 11.17 involves a simpler experimental procedure than equation 11.15, because it does not require monitoring T j and the determination of α and β . However, even for large vessels ( V &gt; 25 cm 3 ), its validity depends on experimental conditions such as the total increase of V in the titration and, of course, on the accuracy desired for the results. Hence, when we cannot rely on previous experience, it is prudent to check the validity of equation 11.17.

It is normally a very good approximation to assume that the titration process under study occurs under a pressure of 0.1 MPa. Therefore, the pressure corrections involved in the conversion of /Delta1 H ICP to the standard state are usually negligible, and in many cases, it is licit to make /Delta1 H ICP = /Delta1 H o ICP . When appropriate, other corrections, such as those related to solution standard states, can be applied as described by Vanderzee [129,130].

## Determination of Enthalpies of Reaction and Equilibrium Constants

Once /Delta1 H o ICP is known, the enthalpy of the reaction of interest in the standard state can be obtained from

<!-- formula-not-decoded -->

where n is the amount of substance of the reference compound consumed or formed from the start of titration to point p (figure 11.2), /Delta1 dil H o is the enthalpy contribution to /Delta1 H o ICP due to the change in the concentrations of the species present as the titration proceeds, and the term ∑ i n i /Delta1 r H o i refers to the contributions of all side reactions where amounts of substance n i of compounds i are involved. The values of /Delta1 dil H o and ∑ i n i /Delta1 r H o i must be measured in separate experiments or calculated from literature data. For a quantitative reaction, n can be derived from the amounts of titrate and titrant reacted up to point p. For reactions that do not go to completion, n must be determined from a mass balance involving all species present in the reaction vessel at point p. This in turn requires knowledge of the equilibrium constant of the reaction, which usually also needs to be determined.

The methods for simultaneous determination of /Delta1 r H o and K in a titration calorimetry experiment have been reviewed [199-202,206]. One of the simplest cases corresponds to the association reaction

<!-- formula-not-decoded -->

Let us assume that n refers to the speciesAB and that no side reactions are present. In this case, equation 11.18 can be rewritten as

<!-- formula-not-decoded -->

where V is the total volume of solution present in the system at a given point p, [AB] is the corresponding concentration of the species AB, and Q = /Delta1 H o ICP -/Delta1 dil H o . The concentration of AB throughout a run can be computed from the equations

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where [A] and [B] are the molar concentrations of the species A and B, and the subscript t denotes a total concentration. Equations 11.21-11.23 lead to

<!-- formula-not-decoded -->

from which it can be concluded that

<!-- formula-not-decoded -->

(the other root of equation 11.24 cannot be accepted). Several trial-and-error methods have been proposed to obtain both /Delta1 r H o and K c for reaction 11.19 [199,202]. In the method described by Christensen et al. [199], for example, a first guess of K c is made and the corresponding [AB] calculated by equation 11.25. Equation 11.20 is then used to obtain /Delta1 r H o for every point p along the titration period. If the correct value of K c was selected, all the obtained /Delta1 r H o results should be approximately identical. This is to be expected because /Delta1 r H o and K c are constant for a given temperature T and ionic strength I and, in general, T and I do not vary considerably during a run. If significant variations of /Delta1 r H o are observed from point to point, new values of K c are chosen and the trialand-error process is repeated until the correct values of K c and /Delta1 r H o are found. The corresponding /Delta1 r G o and /Delta1 r S o are then determined through equations 2.54 and 2.55.

The method just described can only be applied in the simplest cases, where a single reaction is present. The equivalent of equation 11.20 for the general case of i equilibrium reactions inside the calorimetric vessel is

<!-- formula-not-decoded -->

where [X i ] represents the concentration of a given species X i involved in a reaction whose standard enthalpy is /Delta1 r H o i . In this case, the 'best' values of K c, i and /Delta1 r H o i are determined by a least squares fit of equation 11.26 to the experimental data, as described elsewhere [200,202].

It should be pointed out that to obtain the equilibrium constant and the enthalpy of a given reaction by isoperibol titration calorimetry, the values of K c and /Delta1 r H o must be within a certain range. Figure 11.4 shows the effect of the magnitudes of K c and /Delta1 r H o on the shape of a plot of Q versus the volume of titrant added for reaction 11.19. The curves were obtained using equations 11.20 and 11.25, and assuming that a titrant A(aq) of concentration 0.1 mol dm -3 was progressively added to 100 cm 3 of a titrate B(aq) with a concentration of 0.01 mol dm -3 . At constant /Delta1 r H o (figure 11.4a) the shape of the curves becomes less and less different as K c increases. In this example, for K c /greaterorsimilar 10 3 the differences may be small enough to make the accurate determination of the equilibrium constant difficult. On the other hand, for K c /lessorsimilar 5 very little heat is evolved, and the observed temperature change may not be large enough to ensure results of good precision (an overall temperature change of at least 0.01 K is usually required to obtain a reproducibility of 0.2% in the experiments [199]). Note, however, that the current sensitivity levels of some heat flow isothermal titration microcalorimeters (see section 11.2) allows, in some cases, the determination of equilibrium constants in the range 10 8 -10 9 [195]. The observed value of Q is directly proportional to /Delta1 r H o (equation 11.20). Hence, as K c decreases, /Delta1 r H o must increase, so reliable values of these two quantities can be calculated from the measured Q results. The effect of changes in /Delta1 r H o on Q is illustrated in figure 11.4b.

The simultaneous determination of K c and /Delta1 r H o becomes increasingly difficult as the number of competing reactions increases. The analysis of multiple

<!-- image -->

b

)

/(J mol -1

Q

140

120

100

80

60

40

20

0

∆

o

kJ mol -1

r

H

200

150

100

50

10

0

5

K

c

=

100

10

V

15

3

A /cm

Figure 11.4 Results of a hypothetical titration calorimetry study of the reaction A(aq) + B(aq) /harpoonleftright AB(aq), showing the dependence of the curve shape on the values (a) of the equilibrium constant for /Delta1 r H o = 100 kJ mol -1 , and (b) of the enthalpy of reaction, for K c = 100 (see text).

equilibria systems is often ambiguous, and the correct interpretation of the data may usually be helped by results of noncalorimetric techniques (e.g., previous knowledge of the equilibrium constants of some of the reactions, obtained by potenciometry or spectrophotometry). In addition, several carefully planned titration experiments at different concentrations of titrant and titrate and different temperatures are usually required. A number of experimental strategies for dealing with complex systems have been discussed by Oscarson et al. [198]. Detailed worked examples of data analysis in isoperibol titration calorimetry have been described in the literature [197,199,201,203].

The applications of isoperibol titration calorimetry to molecular thermochemistry studies are numerous and diverse [194,207]. A few examples are presented next.

The concepts of acidity and basicity are routinely used to discuss the reactivity of chemical compounds. Angelici and colleagues [213,214] probed the basicity

20

25

of organometallic complexes by determining the enthalpies of the protonation reaction,

<!-- formula-not-decoded -->

at 298.15 K in 1,2-dichloroethane. In equation 11.27, MLn represents an organometallic species where M = Cr, Mo, W, Re Fe, Ru, Os, and Ir, and Ln is a combination of n ligands such as CO, phosphine, phosphite, halogen, cyclopentadienyl, cyclooctadiene, indenyl, and so on. Analysis of /Delta1 r H o ( 11.27 ) trends for various series of complexes lead, for example, to the conclusion that within a group, the basicity increases with the atomic number of the metal. This is expected, because the basicity is likely to correlate with the electron richness of the metal. The dependence of the basicity on the electronic and steric properties of the ligands was also investigated by Angelici and colleagues.

Isoperibol titration calorimetry was also extensively used by Drago' s group [215] to determine enthalpies and equilibrium constants of a variety of reactions where acid-base adducts are formed.These results are the source of Drago' s ECW model, which has been widely used to rationalize chemical reactivity [216-218].

Arnett and colleagues [219,220] measured the enthalpies of a considerable number of processes where a resonance-stabilized carbenium ion R + 1 was reacted with a resonance stabilized carbanion, oxanion, thioanion, or nitroanion, R -2 , in mixtures of sulfolane (95%) and 3-methylsulfolane (5%), at 298.15 K:

<!-- formula-not-decoded -->

The enthalpies of the reverse of reaction 11.28 were used by these authors as a measure of the enthalpies of the R1 -R2 bond heterolysis. By combining the obtained -/Delta1 r H o ( 11.28 ) values with data for the reduction potentials of the carbenium ions and the oxidation potentials of the anions, it was also possible to derive the corresponding enthalpies for the R1 -R2 bond homolysis [219221]. The approximations involved in this approach are discussed in [221] and also in chapter 16. The work of Arnett' s group led to an extensive tabulation of enthalpies of bond heterolysis and homolysis, which was used to analyze how the energetics of R1 -R2 bonds vary with the nature of R1 and R2. An identical methodology was followed by Cheng and co-workers to establish relative scales of homolytic and heterolytic O-NO and N-NO bond dissociation enthalpies in solution [222,223]. The authors hoped that their results could be used to discuss the biological activity of NO. Nitric oxide, the simplest intraand intercellular signaling molecule currently known, is a radical and therefore cannot exist freely in large quantities in the human body. Hence, its role in regulating physiological functions, probably depends on its ability to be 'stored' in certain carrier molecules and be released, in a suitable environment, to another site of the same molecule or to a different receptor molecule. The driving force of NO to migrate should therefore strongly depend on its bonding energetics.

## 11.2 HEAT FLOW TITRATION CALORIMETRY

As mentioned above, titration methods have also been adapted to calorimeters whose working principle relies on the detection of a heat flow to or from the calorimetric vessel, as a result of the phenomenon under study [195-196,206]. Heat flow calorimetry was discussed in chapter 9, where two general modes of operation were presented. In some instruments, the heat flow rate between the calorimetric vessel and a heat sink is measured by use of thermopiles. Others, such as the calorimeter in figure 11.1, are based on a power compensation mechanism that enables operation under isothermal conditions.

Figure 11.5 shows a typical curve obtained for a continuous titration calorimetry experiment involving a quantitative exothermic reaction, using the calorimeter in figure 11.1, operating under isothermal mode. In the initial and final periods (between points a and b, and c and d, respectively), the heat generated by stirring and self-heating of the thermistor used to monitor and control the temperature is removed from the system at constant rate ( dQ / dt ) c using a Peltier thermoelectrical cooler (the Peltier effect was discussed in chapter 9). The offset of the cooling and heat production rates is balanced by heat input ( dQ / dt ) h from a variable heater, so a constant temperature is maintained in the reaction

<!-- image -->

Time

Figure 11.5 Typical curve for a continuous titration calorimetry study of an exothermic reaction, using the calorimeter of Figure 11.1 in the heat flow isothermal mode of measurement. f is the frequency of the constant energy pulses supplied to the heater C in Figure 11.1b. Adapted from [196,197].

vessel. The heat is supplied with constant energy pulses and the pulse frequency f , in terms of counts per second, is recorded as a function of time. As titrant is added (between points b and c), f is adjusted to keep the temperature constant inside the vessel. The region between points q and c corresponds to the addition of excess titrant. The form of the curve in this region reflects the heat effects already present in the initial period (stirring, self-heating of the thermistor) plus any other due to continuous addition of titrant. The constant rate increase in the volume of solution inside the calorimetric vessel along the titration period, leads to a progressive change of the heat effect due to stirring. This causes a linear change of the baseline during the titration period and a baseline shift between the initial and final periods.

The reactions are usually carried out at a constant pressure and the value of /Delta1 H ICP corresponding to a given point p of the titration period is given by

<!-- formula-not-decoded -->

where ε is a calibration constant that is used to convert the f values from counts per second to J s -1 . The value of ε is usually independent of the volume or type of liquid in the reaction vessel [199]. It can be determined in a calibration experiment where a constant current I is supplied to the calibration heater (D in figure 11.1a) for a given period of time t , and the corresponding voltage V is determined. Then

<!-- formula-not-decoded -->

Thecalibration experiments are performed with a constant amount of liquid inside the calorimetric vessel and, in this case, no baseline shift is observed between the initial and final periods.

If the calorimeter could respond instantaneously to the heat effects associated with the addition of titrant, then the measured curve would coincide with the dashed lines in figure 11.5. The deviation of the data from this ideal behavior corresponds to periods in which the isothermal condition is not observed. When necessary, however, it is possible to use deconvolution techniques to generate the input function represented by the dashed line from the observed experimental curve.

The enthalpy of the reaction under study in the standard state can be obtained from

<!-- formula-not-decoded -->

where n is the amount of substance of the reference compound consumed or formed up to point p, and the terms /Delta1 H tr , /Delta1 dil H o , and ∑ i n i /Delta1 r H o i , represent the contributions to /Delta1 H o ICP due to the temperature difference between titrant and titrate, the change in the concentrations of the species present as the titration proceeds, and the enthalpic effects of all side reactions where amounts of substance

n i of compounds i are involved. The methods used to handle these terms have been discussed in section 11.1.

Many isoperibol titration calorimetry measurements can also be performed using heat flow instruments. The choice of the 'best' method-isoperibol or heat flow-largely depends on the nature of the systems to be studied. For example, if the products of a reaction slowly decompose with time, it may be necessary to use a calorimeter with a fast response. In this case, an isoperibol instrument may be preferable. However, if a very slow reaction is to be studied, then isoperibol calorimetry will not be adequate, because accurate computation of heat-loss corrections over long periods of time is virtually impossible. Slow reactions are best studied using heat flow calorimeters and an incremental titration method. Thesensitivity of heat flow instruments is also much greater that that of isoperibol apparatus. As mentioned in section 11.1, there are titration heat flow calorimeters sufficiently sensitive to measure heat effects associated with reactions where only nanomoles of reactants are involved and that can be applied to determine equilibrium constants, K c, as high as 10 8 -10 9 [195]. The high sensitivity of heat flow instruments has made them particularly useful to investigate molecular interactions of biological interest. These studies frequently have to be made with very limited quantities of sample and often correspond to processes with large equilibrium constants. Heat flow titration calorimetry has, for example, been used by Jansson and co-workers [224] to probe the interaction of insulin growth factor-I receptor (IGF-I R ) with insulin growth factor-I (IGF-I). IGF-I R is a transmembrane glycoprotein; IGF-I is also a protein that functions as a major regulator of both cellular growth and metabolism through interaction with IGF-I R . Experiments were performed at three different temperatures and led to the values of /Delta1 r H o , /Delta1 r S o , /Delta1 r G o , and /Delta1 r C o p for the binding process. The analysis of the thermodynamic data indicated that the interaction of the two proteins involves a 1:1 complex and the signal transduction across the cell membrane may be associated with conformational changes experienced by IGF-I R on binding to IGF-I.

Another area where titration calorimetry has found intensive application, and where the importance of heat flow versus isoperibol calorimetry has been growing, is the energetics of metal-ligand complexation. Morss, Nash, and Ensor [225], for example, used potenciometric titrations and heat flow isothermal titration calorimetry to study the complexation of UO 2 + 2 and trivalent lanthanide cations by tetrahydrofuran-2,3,4,5-tetracarboxylic acid (THFTCA), in aqueous solution. Their general goal was to investigate the potential application of THFTCA for actinide and lanthanide separation, and nuclear fuels processing. The obtained results (table 11.1) indicated that the 1:1 complexes formed in the reaction (M = La, Nd, Eu, Dy, and Tm)

<!-- formula-not-decoded -->

had a considerably higher stability (more negative /Delta1 r G o ) than the complex obtained in the process:

<!-- formula-not-decoded -->

Table 11.1 Results of the titration calorimetry study of reactions 11.32 and 11.33 at 298.15 K and ionic strength I = 0.1 M (NaClO 4 ). Data from [225].

| M n +    | /Delta1 r H o / (kJ mol - 1   | ) T /Delta1 r S o / (kJ mol - 1 ) a   | - /Delta1 r G o / (kJ mol - 1   |
|----------|-------------------------------|---------------------------------------|---------------------------------|
| La 3 +   | 0.16 ± 0.59                   | 23.9 ± 0.7                            | 23.7 ± 0.4                      |
| Nd 3 +   | - 4.14 ± 1.44                 | 24.5 ± 1.7                            | 28.6 ± 0.9                      |
| Eu 3 +   | - 2.52 ± 1.16                 | 29.4 ± 1.3                            | 31.9 ± 0.5                      |
| Dy 3 +   | 2.71 ± 0.48                   | 39.4 ± 0.5                            | 36.7 ± 0.2                      |
| Tm 3 +   | 5.42 ± 0.72                   | 40.9 ± 0.7                            | 35.5 ± 0.2                      |
| UO 2 + 2 | 18.2 ± 0.1                    | 36.0 ± 0.2                            | 17.8 ± 0.2                      |

a Calculated from T /Delta1 r S o = /Delta1 r H o -/Delta1 r G o .

As noted in table 11.1, the ability of THFTCA to separate UO 2 + 2 from trivalent lanthanide ions is mainly of enthalpic origin. Reaction 11.33 has a considerably more unfavorable enthalpic contribution than reaction 11.32. The complexation is, however, predominantly entropy driven because the T /Delta1 r S o term dominates the /Delta1 r H o contribution for all systems. The large positive entropy changes observed for reactions 11.32 and 11.33 result from the release of water molecules coordinated to the metal on complexation with the tridentate THFTCA 2 -ligand. Note that a negative entropy contribution would be expected if these reactions were truly 2 particle = 1 particle reactions [226].

## Differential Scanning Calorimetry (DSC)

Physical and chemical changes may often be induced by raising or lowering the temperature of a substance. Typical examples are phase transitions, such as fusion, or chemical reactions, such as the solid state polymerization of sodium chloroacetate, which has an onset at 471 K [227]:

<!-- formula-not-decoded -->

Differential scanning calorimetry (DSC) was designed to obtain the enthalpy or the internal energy of those processes and also to measure temperature-dependent properties of substances, such as the heat capacity. This is done by monitoring the change of the difference between the heat flow rate or power to a sample (S) and to a reference material (R), /Delta1Φ = Φ S -Φ R = ( dQ / dt ) S -( dQ / dt ) R, as a function of time or temperature, while both S and R are subjected to a controlled temperature program [5,228-230]. The temperature is usually increased or decreased linearly at a predetermined rate, but the apparatus can also be used isothermally. In some cases DSC experiments may provide kinetic data [231].

According to Wunderlich [232], differential scanning calorimeters evolved from the differential thermal analysis (DTA) instruments built by Kurnakov at the beginning of the twentieth century. In these early DTA apparatus, the temperature difference between a sample and a reference, simultaneously heated by a single heat source, was measured as a function of time. No calorimetric data could be derived, and the instruments were used, for example, to determine the temperatures of phase transitions and to identify metals, oxides, minerals, soils, and foods. The attempts to obtain calorimetric data from DTA instruments eventually led to the development of DSC [229,230]. The term differential scanning calorimetry and the acronym DSC were coined in 1963 when the first commercial instrument of this type became available [233,234]. This apparatus was easy to operate, enabled fast experiments, and required only small samples (typically 5-10 mg). Its importance for materials characterization was immediately demonstrated and the DSC technique soon experienced a boom. New user-friendly commercial instruments were developed, and new applications were explored. It is, however, somewhat ironic that the method ows its still growing popularity to analytical rather than calorimetric uses. In most current applications, DSC is still employed as a thermometer (a quite expensive one!), for example, to detect the onset of phase transitions or reactions or in quality control checks. As will be discussed,

reliable calorimetric data can nevertheless be obtained by DSC, provided that adequate experimental procedures and data analysis methods are followed.

Theprospects of DSC, have been reviewed in a special issue of Thermochimica Acta , which includes a collection of articles on advances of thermal analysis in the twentieth century and expected future developments [232,235,236]. This journal and the Journal of Thermal Analysis and Calorimetry , where research articles about DSC and its applications are often published, are very useful sources of information on the technique. Although relatively old, the reviews by McNaughton and Mortimer [237] and by Mortimer [238] contain excellent examples of applications of DSC to molecular thermochemistry studies. The analytical uses of DSC, which are outside the scope of this book, can be surveyed, for example, in biannual reviews that appear in the journal Analytical Chemistry [239].

Two general types of DSC apparatus, which differ on the operation principle, are available [5]: heat flux DSC , with two main variants, viz . disk-type and cylinder-type measuring system; and power compensation DSC . In a heat flux DSC, the temperature difference between the sample S and the reference R is recorded and converted to a difference in heat flow rate to the sample and to the reference, using a suitable calibration factor. In disk-type heat flux DSC (figure 12.1), the crucibles containing S and R are placed on a disk A (normally made of a metallic or ceramic material) inside a block furnace, B, whose temperature can be programmed. The temperature difference between the two specimens, /Delta1 T , is measured with sensors, C, embedded in the disk or contacting the disk surface. In a cylinder-type heat flux DSC (figure 12.2), the sample and the reference are located inside tubular cells, A, surrounded by the block furnace B.The temperature difference between the cells and the furnace is measured by thermopiles or thermoelectrical semi-conducting sensors, C, and /Delta1 T is also monitored through a differential connection, D, of the thermopiles.

In a power compensation DSC (figure 12.3), the sample and the reference crucible holders consist of two small furnaces, AS and AR, each one equipped with a temperature sensor, BS or BR, and a heat source, CS or CR. The furnaces

Figure 12.1 Scheme of a disk-type heat flux differential scanning calorimeter. A: cell; B: furnace; C: temperature sensors; S: sample; R: reference.

<!-- image -->

Figure 12.2 Scheme of a cylinder-type heat flux differential scanning calorimeter. A: cell; B: furnace; C: thermopile; D: differential connection of the thermopiles; S: sample; R: reference.

<!-- image -->

Figure 12.3 Schemeofapowercompensationdifferential scanning calorimeter. A S : sample furnace; A R : reference furnace; B S : temperature sensor of the sample furnace; B R : temperature sensor of the reference furnace; C S : resistance heater of the sample furnace; C R : resistance heater of the reference furnace; D: cell; S: sample; R: reference.

<!-- image -->

are located inside a cell D whose temperature is not monitored. It is convenient to consider that the system of furnaces is controlled by two separate loops, one for average temperature control and the other for differential temperature control. The average temperature control loop ensures that the average of the sample and reference temperatures is increased at a programmed rate β . If the sample undergoes an endothermic or exothermic transformation or a heat capacity change, a temperature difference, /Delta1 T , will tend to develop between AS and AR. The differential control loop automatically adjusts the power supplied to each furnace, so that /Delta1 T is maintained as small as possible during an experiment (the value of /Delta1 T is actually never zero because the working principle of the control system is based on the existence of a small error signal). The recorded output signal of the calorimeter is proportional to the difference /Delta1Φ between the heat flow rates supplied to the sample and the reference.

Modern heat flow or power compensation DSC instruments are invariably connected to a computer for programming of the experiments, data acquisition, and data analysis. As mentioned, the results are usually displayed as a plot of /Delta1Φ against time or temperature (figures 12.1-12.3). Positive heat flow rates are assigned to endothermic effects and the corresponding peaks point to the positive direction of the /Delta1Φ axis. Conversely, exothermic processes are assigned to negative heat flow rates and the resulting peaks point to the negative direction of the /Delta1Φ axis.

In addition to conventional DSC, several other related techniques that will not be covered here have been developed. Perhaps the most important is temperaturemodulateddifferential scanning calorimetry (TMDSC) [229,230,232], which was introduced in the early 1990s [240-242]. In TMDSC an oscillating (usually sinusoidal) temperature change profile is overlaid on the customary linear temperature program to yield a curve in which the average sample temperature continuously changes with time but not in a linear fashion. The net effect of this more complex heating or cooling program can be regarded as if two experiments were simultaneously run on the sample: one using the linear (average) temperature change and the other employing a periodic (instantaneous) temperature variation. This method, whose full potential is still to be explored [232,235], has been intensively used, for example, to investigate complex phase transitions, such as the crystallization of metastable crystalline structures prior or during melting [230,232]. Also worth mentioning is the coupling of DSC with several analytical techniques that help in the assignment of the transformations experienced by the sample. Examples are DSC-microscopy, DSC-X-ray diffraction, and DSC-mass spectrometry [230].

The operational temperature ranges of DSC instruments typically lie in the interval 100-1000 K. The available heating rates frequently vary between 0.1 K min -1 and 50 K min -1 , with 5 K min -1 and 10 K min -1 perhaps the most common. The slower heating rates are normally needed when large samples are used, so that the thermal lag within the sample is small (i.e., the temperature of the sample closely follows the programmed temperature; see ensuing discussion). Sample masses usually vary between 1 mg and 100 mg. The smaller masses are normally sufficient to measure 'large' heat effects, such as those associated with fusion and many chemical reactions. The larger masses may be necessary for the measurement of smaller heat effects, such as those involved in the determination of heat capacities. The samples are enclosed in crucibles, which may or may not be hermetically sealed, and exist in a variety of shapes, depending on the type of apparatus and application. Crucibles are usually made of high thermal conductivity materials, and aluminum is by far the most widely used. As illustrated in figures 12.1-12.3, the reference normally consists of an empty crucible identical to the sample crucible. During the experiments, a purging gas (e.g., helium, argon, nitrogen) is flowed through the cell at a constant rate to ensure that the atmospheric conditions are as uniform as possible in all experiments. Changing the nature or flow of the gas will change the thermal conductivity of the spaces between the crucibles and the furnace walls, thus affecting the measured heat flow rate difference.

## 12.1 THERMODYNAMIC DATA FROM DSC EXPERIMENTS

Two general strategies have been used to obtain enthalpies and internal energies of phase transitions or reactions, and heat capacities, by DSC [243-249]: (i) the dynamic or nonisothermal method , in which the apparatus is run in a continuous temperature scanning mode, and (ii) the isothermal method , which involves a slow stepwise temperature scanning procedure. The dynamic method is more widely used because it corresponds to the traditional mode of operation of the instrument and the experiments are generally faster. Most of the following discussion will therefore be concentrated on this method. It should be noted that at the scan rates normally selected for dynamic operation (5-10 K min -1 ) , the conditions of a run are far from reversible. As mentioned before, lower rates are possible, but most users tend to avoid them because they usually lead to noisier signals and the duration of the experiment increases. The reliability of the thermodynamic data obtained from DSC measurements at these high scan rates critically depends on the use of appropriate calibration and data analysis procedures. The isothermal method also requires a careful calibration of the apparatus, but the conditions of the experiments are much closer to equilibrium than in case of the dynamic method.

DSC studies are often carried out using hermetically sealed crucibles and therefore occur at constant volume (neglecting the expansion of the crucible with the temperature). This is overlooked by most users, who invariably express their results as Cp , /Delta1 trs H , or /Delta1 r H , whereas constant volume studies strictly lead to CV , /Delta1 trs U , or /Delta1 r U (see chapter 6). However, taking Cp = CV , /Delta1 trs H = /Delta1 trs U , or /Delta1 r H = /Delta1 r U is, in general, an excellent approximation because most DSC studies refer to processes involving only condensed phases. It should nevertheless be kept in mind that if, for example, gaseous products are formed in the decomposition of a solid sample at constant volume, the error of making /Delta1 r H = /Delta1 r U may not be negligible. The primarily derived quantity in this case is /Delta1 r U , and the corresponding /Delta1 r H can be calculated by using equations 6.1 or 6.2.

The versatility of the DSC method and the high speed of the experiments have costs in terms of accuracy. For example, the best accuracy in the determination of heat capacities of solids by DSC is typically 1% [3,248-250], at least one order of magnitude worse than the accuracy of the corresponding measurements by adiabatic calorimetry [251]. This accuracy loss may, however, be acceptable for many purposes, because DSC experiments are much faster and require much smaller samples than adiabatic calorimetry experiments. In addition, they can be performed at temperatures significantly above ambient, which are outside the normal operating range of most adiabatic calorimeters.

## The Dynamic Method

Figure 12.4 shows a typical DSC curve for the study of an endothermic process by the dynamic method. The heating program is started at the time t st, after an isothermal baseline has been recorded, and ends at the time t end . The reaction or

<!-- image -->

Time

Figure 12.4 Scheme of an ideal DSC curve for the study of an endothermic process by the dynamic method. Also shown are the programmed temperature ( T p) line and the zero line. The zero line is obtained in a separate experiment, where the sample and the reference crucibles are empty and the heating program used in the main experiment is maintained.

phase transition undergone by the sample originates the peak with onset at t 2 and offset at t 4. In this case, the initial and final baselines are not collinear. As it will soon be apparent, this is due to a significant change in the heat capacity of the sample during the transformation. Also shown in figure 12.4 are the programmed temperature line and the zero line . The zero line corresponds to a curve obtained in a separate experiment, with the sample and reference crucibles empty, and using a temperature program identical to that of the main experiment.

Two main problems need to be considered in the determination of the enthalpy or the internal energy of a given process from a DSC curve such as that in figure 12.4: (i) the assignment of a reference temperature to the process and (ii) the definition of the peak area that best represents the heat associated with the process.Addressing these problems requires a careful calibration of the apparatus in terms of temperature and in terms of heat flow (ordinate calibration) or of heat (peak area calibration). It also implies the definition of a suitable interpolated baseline, that is, a baseline connecting the peak onset and offset. Routine DSC procedures use a straight line joining two arbitrarily selected peak onset and outset points (e.g., k and d in figure 12.4). However, as can be inferred from the following discussion, this is only strictly valid if the heat capacity change during the transformation is negligible (i.e., the initial and final baselines are collinear) and not in a case like the one illustrated in figure 12.4.

Let us first address the question of the accurate measurement of the temperature of the sample in DSC experiments [252-255]. As illustrated in figure 12.4, the programmed temperature, T p, usually varies linearly with the time t , and can

easily be obtained from

Distance

<!-- formula-not-decoded -->

where T st is the starting temperature and β the scan rate. However, the temperature of the sample, T s, and not T p, needs to be known to assign a correct value for /Delta1 trs H or /Delta1 r H . The temperature sensors, which are used to monitor the temperature of the sample cell and ensure that T s follows T p as closely as possible during a run, are situated relatively remote from the sample. As a result, a temperature difference, T s -T p, between the sample and the sensor location will tend to develop, even under isothermal conditions. The magnitude of T s -T p will change during a scan, due to an additional dynamic thermal lag, which increases with β , and is negative on heating ( T s &lt; T p) and positive on cooling ( T s &gt; T p). Moreover, if the thickness of the sample is large in relation to its thermal conductivity, a temperature gradient within the sample itself will also exist, because in most DSCinstruments the sample is heated through the basis of the crucible in contact with the sample cell. A simplified diagram of the temperature gradient along a DSC cell, on heating, under steady state conditions, is illustrated in figure 12.5.

In practice, the temperature of the transformation is normally given in terms of the extrapolated onset temperature , T 3, corresponding to point h in figure 12.4 [254,256-260]. This temperature is taken to represent the temperature of the sample surface in contact with the crucible at the beginning of the transformation [249,254]. However, because of the unknown difference T s -T p just discussed, a careful calibration of the temperature scale of the apparatus is needed before the obtained T 3 represents to a good approximation the true equilibrium temperature of the sample at the onset of the transformation. The choice of T 3 as reference temperature is particularly convenient for exothermic events. In this case, due to the heat released, the sample temperature will, during the transformation, become higher by an unknown amount than the programmed temperature indicated by the instrument.

The most widely recommended calibration method for dynamic DSC operation involves the determination of the extrapolated onset temperature for the fusion of several standard substances, using various heating rates [255,256].

Figure 12.5 Simplified scheme of the temperature gradient along the sample cell of a DSC instrument, on heating and under steady state conditions. A: heating

<!-- image -->

element; B: heat conduction path; C: crucible; D: temperature sensor;

S: sample.

Recommended calibration substances cover the temperature range 120-1800 K [254,257,261]. Various runs should be carried out at each heating rate, using different masses of sample (in the range typically employed in the experiments), to ensure that the measurements are not significantly affected by factors other than the scan rate, such as the mass of sample and the sample position. For each standard substance the obtained T 3 values are plotted as a function of β and extrapolated to zero heating rate. For many standards a linear relationship between T 3 and β is observed, making the extrapolation straightforward. The obtained T β = 0 3 is compared with the equilibrium temperature of the transition, T eq , given by the supplier of the reference material, and the difference

<!-- formula-not-decoded -->

is computed. The δ T versus T 3 data obtained for the various standards can be used to construct a calibration table or fitted to an equation such as

<!-- formula-not-decoded -->

where T is the temperature reading given by the instrument. The form and complexity of the equation needed for the fitting depends on several factors, such as the nature of the apparatus, the number of calibrant points used, the magnitude of the temperature range covered by the calibration, and the required accuracy. In some cases, a linear relation may be sufficient if the temperature range of interest is not too large. In modern instruments, the results of the calibration can be stored in a computer and the necessary temperature corrections automatically taken into account by the software.After calibration, the experiments with the sample under study are performed at different heating rates, and the corresponding T β = 0 3 is found. The true equilibrium onset temperature is then estimated from

<!-- formula-not-decoded -->

with δ T computedfromequation12.4orobtainedbyinterpolationfromthedatain a calibration table. If carefully applied this method is expected to give equilibrium onset temperatures with a precision and accuracy of ± 0.1 K [249,254,256]. Alternative methods of estimating T 3 have been discussed, for example, by Sarge [255], Poe β necker [262,263], and Schawe [264]. It should be stressed that regardless of the method chosen, each temperature calibration is strictly valid for a given set of experimental conditions. For accurate work, a new temperature calibration will be required if, for example, the type of crucible or the nature of the purge gas are changed. It is also generally accepted that when conducting DSC experiments in the cooling mode, for reaching the best possible measurement uncertainty it is advisable to perform the calibration of the instrument also in the cooling mode [265].

As mentioned, the calorimetric applications of DSC involve the conversion of a peak area into the energy associated with a chemical reaction or with a physical process (e.g., fusion, vaporization). Because the trace of the peak does not by itself define an area, an appropriate baseline must be found. The complexities of the baseline construction and their influence on the measurement of heat by

DSChavebeenthoroughlydiscussed by several authors [244-247,249,266-268]. Here we closely follow the method proposed by Flynn and Guttman [244-247], to illustrate the determination of heat from a curve such as the one depicted in figure 12.4. It will be assumed that the experiment occurs at constant pressure, so that the measured heat corresponds to an enthalpy change. This method has the advantage of avoiding a curve analysis in terms of a hypothetical thermokinetic mechanismforthetransformationunderstudy,whichisdifficulttohandlewithout considerable simplifications [230]. It also leads in a straightforward manner to the enthalpy of the transformation under isothermal conditions at a given reference temperature, which is usually the desired quantity in thermochemical studies. This point is often overlooked by DSC users. As mentioned in chapters 7 and 8, when a chemical reaction is studied calorimetrically, the enthalpy change of interest normally refers to a process where all reactants and products are in their standard states ( p reactants = p products = 0.1MPa ) , and at the same reference temperature, for example, T 3 in figure 12.4. Analogously, the reported enthalpies of phase transitions in pure substances correspond to an isothermic process and should refer to a standard state. Note that the apparent extension of the DSC peak corresponding to the fusion of a very pure substance over a temperature range (several degrees) is merely an artifact, due to the time needed to transfer the necessary heat into the sample and the fact that the instrument does not record the true temperature of the sample during the transition. This is indicated by the decrease of the peak width when the heating rate is decreased. Thus, in conclusion, when a chemical or physical event is observed in a DSC experiment at constant pressure, between two temperatures T i and T f , the corresponding enthalpy change at the selected reference temperature must be extracted from the overall enthalpy change H f -H i .

To our knowledge, the question of the standard state corrections in DSC experiments has never been addressed. These corrections may in general be negligible, because most studies only involve condensed phases and are performed at pressures not too far from atmospheric. This may not be the case if, for example, a decomposition reaction of a solid compound that generates a gas is studied in a hermetically closed crucible, or high pressures are applied to the sample and reference cells. The strategies for the calculation of standard state corrections in calorimetric experiments have been illustrated in chapter 7 for combustion calorimetry.

The general features of the curve in figure 12.4 and the underlying principles of the method of curve analysis proposed by Flynn and Guttman [244-247] will be discussed by using a simple model of the DSC apparatus.

Under ideal conditions, the true overall heat flow rate into the sample cell Φ a = ( dQ / dt ) a can be divided in three terms: (i) the heat flow rate into the crucible, Φ ca = ( dQ / dt ) ca ; (ii) the heat flow rate into the sample itself, Φ s = ( dQ / dt ) s; and (iii) the remaining heat flow rate into the cell, Φ ra :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where m s and m ca are the masses of the sample and of the sample crucible, respectively, and c s and c ca are the corresponding massic heat capacities. Similarly, if the reference cell is assumed to contain an empty crucible of mass m cb and of the same material as the sample crucible:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The heat flow rate difference corresponding to a run where both the sample and the reference crucibles are empty (zero line) is given by

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In practice, the true heating rates ( dT / dt ) ca and ( dT / dt ) cb are assumed to be equal to the programmed scan rate β , and the true heat flow rate difference (Φ a -Φ b ) 0 is proportional to the recorded zero line heat flow rate difference, /Delta1Φ 0, which reflects the intrinsic thermal asymmetry of the differential measuring system:

<!-- formula-not-decoded -->

Here k Φ represents a proportionality factor, which can be found by calibration (heat flow calibration, see following discussion).

It can be concluded from equations 12.11 and 12.12 that the small deviation of the zero line relative to the isothermal baseline under the same scanning conditions is proportional to the heating rate and the difference in heat capacities of the two empty crucibles. This deviation can be positive (as in figure 12.4) or negative, depending on the magnitude of the intrinsic thermal asymmetry of the system under scanning conditions and the relative masses of the two crucibles.

When the sample is introduced in the sample crucible,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Therefore, considering equations 12.10 and 12.12, the heat supplied to the sample between the times t 1 and t 4 is given by

<!-- formula-not-decoded -->

where A represents the area [ abcde ] in figure 12.4 and kQ is the energy equivalent of the calorimeter, which must be obtained by calibration.

Thefactor k Φ in equations 12.12, 12.15, and 12.16 is not a constant, because the true heat flow rate differences (Φ a -Φ b ) 0 and (Φ a -Φ b ) are not linearly related

to the measured /Delta1Φ 0 and /Delta1Φ , respectively [269]. Thus in DSC experiments different proportionality factors exist for the ordinate to heat flow ( k Φ) and the area to energy ( kQ ) conversions; consequently, there are two ways of determining Q from equation 12.16. Either k Φ , /Delta1Φ , and /Delta1Φ 0 are explicitly measured as a function of t and the product k Φ(/Delta1Φ -/Delta1Φ 0 ) integrated in the interval t 4 -t 1, or the area A is evaluated and the product kQA computed.

The heat flux and energy calibrations are usually performed using electrically generated heat or reference substances with well-established heat capacities (in the case of k Φ) or enthalpies of phase transition (in the case of kQ ) . Because k Φ and kQ are complex and generally unknown functions of various parameters, such as the heating rate, the calibration experiment should be as similar as possible to the main experiment. Very detailed recommendations for a correct calibration of differential scanning calorimeters in terms of heat flow and energy have been published in the literature [254,258-260,269].

It was assumed that the experiment occurred at constant pressure. Hence, equation 12.16 can also be written as

<!-- formula-not-decoded -->

where HT 4 -HT 1 represents the enthalpy change of the sample between the temperatures T 1 and T 4, which correspond to times t 1 and t 4. Equation 12.17 yields HT 4 -HT 1 once kQ and A are known. Recall, however, that as stated, the main goal of the experiment is not the determination of HT 4 -HT 1 but the enthalpy, /Delta1 HT 3 , of a hypothetical transformation experienced by the sample under isothermal conditions at a given reference temperature, which is usually taken as T 3 in figure 12.4. Both quantities are related by

<!-- formula-not-decoded -->

where Cp ,i and Cp ,f are the overall heat capacities ( Cp = m s cp ) of the sample in the initial and final states, respectively. Assuming that the true heating rate of the sample can be replaced by the programmed rate,

<!-- formula-not-decoded -->

Equation 12.19 requires the determination of the heat capacity of the initial and final states of the transformation as a function of the temperature. The general method used in the determination of Cp or CV by DSC will be outlined next. Now, we note that according to equations 12.10-12.15, between t 1 and t 2:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

If stable initial and final baselines are observed, it is expected that they can both be extrapolated to t 3 (lines bh and dg , respectively, in figure 12.4), thus defining the and between t 4 and t end :

variation of the heat capacities of the initial and final states with the temperature in the ranges t 1 → t 3 and t 3 → t 4, respectively. In this case, the two integrals in equation 12.19 will be given by

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where B and C represent the areas [ abhf ] and [ fgde ] in figure 12.4, respectively. Hence,

<!-- formula-not-decoded -->

In the case of figure 12.4, the baseline corresponds to the stepped line khgd , and the method gives the desired enthalpy of the process under study by multiplying the resulting area ( A -B -C ) by the energy equivalent kQ . If the zero line is not recorded, a reasonable approximation of the enthalpy of the transformation can usually be obtained simply by considering the area [ icd ] in figure 12.4. The error of this approximation decreases as the areas [ kjh ] and [ jgi ] become identical. Once /Delta1 HT 3 has been determined, the enthalpy of the transformation at any other temperature can be calculated by using the generalized form of equation 2.14.

Asillustrated in figure 12.6, the determination of the heat capacity as a function of the temperature usually involves three consecutive measurements [229,270].

Heat flow rate difference

<!-- image -->

Time

Figure 12.6 Themeasurementofheatcapacity by DSC, under dynamic operating conditions.

First, the zero line is recorded using two empty crucibles. Next, a calibrant substance (usually alumina, i.e., synthetic sapphire) is placed in the sample crucible and the temperature program is repeated. Finally, the calibrant is replaced by the sample under study (keeping the crucible) and the temperature program run a third time. Based on equations 12.20 and 12.21, it can be concluded that the ordinate difference between the traces of the calibrant curve and of the zero line obtained for a given time t leads to the corresponding value of k Φ :

<!-- formula-not-decoded -->

where Cp ( cal ) represents the heat capacity of the calibrant. Once the variation of k Φ with the time and consequently with the temperature is known, the heat capacity of the sample, Cp ( S ) , can be derived from the difference between the traces of the sample curve and the zero line:

<!-- formula-not-decoded -->

If, as illustrated in figure 12.6, the isothermal starting lines of the various curves do not coincide, then /Delta1Φ 0, /Delta1Φ cal, and /Delta1Φ s are measured from the interpolated dotted lines. These displacements occur if the conditions of heat transfer change between runs, for example, due to a variation in the purge gas flow or the fact that it is virtually impossible to relocate the crucible containing the sample exactly in the position used for the calibrant run (normally the reference crucible remains in place throughout a series of runs). Note that a similar correction should have been used in the computation of heat flow or area quantities if, in the example of figure 12.4, the isothermal baselines of the main experiment and the zero line were not coincident.

The determination of the heat capacity of a substance as a function of the temperature is by itself a very important application of DSC, because it may lead to values of the thermodynamic functions S o T , H o T -H o 0 , and G o T , mentioned in chapter 2. An example is the study of C60 carried out by Wunderlich and co-workers [271]. The application of DSC in the area of molecular thermochemistry has been particularly important to investigate trends in transition metal-ligand bond dissociation enthalpies. The typical approach used in these studies, and its limitations, can be illustrated through the analysis of the reaction 12.27, carried out by Mortimer and co-workers [272]:

<!-- formula-not-decoded -->

where α -pic is α -picoline (see figure 12.7). In this case, full details of the criteria for the selection of the peak baseline and the computation of the enthalpy of the isothermal calorimetric process were given by the authors, which, by the way, is seldom the case when DSC results are reported. The method used by Mortimer andco-workersintheanalysis of the results is similar to that of Flynn and Guttman already discussed. The experiments were carried out under a dynamic flow of dry nitrogen (30 mL min -1 ) using a scan speed of 16 K min -1 . The samples, with masses in the range 2-6 mg, were contained in aluminum pans whose lids did

Figure 12.7 Typical DSC curves obtained in the study of reaction 12.27 (see text).

<!-- image -->

not provide a hermetic seal. Hence, the gaseous ligand escaped from the cell during the reaction, leading to a decrease of the heat capacity of the system in the final state, which was apparent in the lowering of the final baseline relative to the initial baseline. A typical result is illustrated in figure 12.7 where x represents the zero line, y is the final baseline, and z the initial baseline. The experiment was started at T st and ended at T end . The decomposition reaction 12.27 had an onset at T a = 480 K and an offset at T b = 560 K. The enthalpy of reaction was computed from the area of the peak defined by the linear interpolated baseline connecting the points a and b in figure 12.7 and, as will be explained, refers to the temperature T m = ( T a + T b )/ 2 corresponding to the midpoint of the peak interval. The calculation was based on the following premises: (i) In the initial state a mass m of Co( α -pic)2Cl2(cr) was present in the system at T a . (ii) In the final state the cell contained a mass m ′ of CoCl2(cr) at the temperature T b. (iii) The determination of the mass change of the DSC pans before and after the experiments indicated that the ligand α -pic(g) was totally removed from the cell between T a and T b. The authors assumed that the mass loss occurred at a constant rate. (iv) The heat capacities of reactant and products were temperatureindependent over the temperature range of the experiment. (v) The area B ≈ C in figure 12.7. It can be concluded from these assumptions that if the initial temperature T a is selected as the reference temperature, the enthalpy of reaction corresponding to the decomposition of a mass m of Co( α -pic)2Cl2(cr) will be given by

<!-- formula-not-decoded -->

where cp represents the massic heat capacity and Q is the heat associated with the calorimetric process given by

<!-- formula-not-decoded -->

In equation (12.29) A , B , C , and D represent the areas indicated in figure 12.7, and kQ is the energy equivalent of the calorimeter, which was determined by using the fusion of indium.

Alternatively, if T m is chosen as the reference temperature, and recalling that T m = ( T a + T b )/ 2, hence ( T m -T a ) = ( T b -T a )/ 2, the enthalpy of reaction will be written as

<!-- formula-not-decoded -->

Introducing /Delta1 r HT a , given by equation 12.28 in equation 12.30, one obtains

<!-- formula-not-decoded -->

Using

<!-- formula-not-decoded -->

(recall that B ≈ C was assumed), it can finally be derived that

<!-- formula-not-decoded -->

The enthalpy of reaction per mole of Co( α -pic)2Cl2(cr) is then given by:

<!-- formula-not-decoded -->

where M is the molar mass of the complex. Hence, provided that the assumptions madebytheauthorsarevalid,when T m is selected as the reference temperature the enthalpy of the isothermal reaction corresponds to the area of the peak defined by the baseline connecting points a and b , which is easy to delimit. The uncertainty caused by the approximation B ≈ C is difficult to assess because it depends on the importance of the difference between the areas B and C compared to the total peak area. That difference depends on the peak shape and may vary from one experiment to another. Instead of a linear interpolated baseline, a sigmoid baseline (which accounts better for the variation of the heat capacity of the sample during the reaction) can be defined [266-268].

Mortimer and co-workers extended these studies to many other CoL2X2 compounds and, using estimated or measured enthalpies of sublimation and heat capacities of the complexes and the ligands, were able to derive the corresponding Co-L mean bond dissociation enthalpies [238].

There are several interesting application examples of DSC to molecular thermochemistry of organic molecules. One of them involves the energetics of the interconversion of the benzene valence isomers having the composition (CCF3 ) 6, namely, the prismane (1), Dewar benzene (2), benzene (3), and benzvalene (4), derivatives shown in figure 12.8 [273]. Although very few details of the data analysis procedure are given by the authors, this study led to thermochemical and kinetic data from which the energy profile indicated in figure 12.8 could be drawn. Another example is the thermochemical and kinetic investigation of the molecular rearrangements in esters of (hydroxymethyl)hydridosilanes (X = C, S, or P; R, R ′ = H, CH3, C6H5, or (CH3 ) 3SiCH2; R ′′ = Cl, CH3, CF3, or C6H5 ) [274,275].

<!-- image -->

In this case, although the reported enthalpy of reaction refers to the difference HT b ( B ) -HT a ( A ) , where T a and T b represent the selected temperatures of the peak onset and offset, respectively, an approach based on the thermokinetic analysis of the measured curve was used to compute the peak baseline, and a very detailed description of the method used to derive the thermodynamic and kinetic data is given by the authors. Finally, a general and very important application of

<!-- image -->

Reaction coordinate

Figure 12.8 Energy profile for the interconversion of benzene valence isomer derivatives.

DSC in biochemistry is the study of the energetics of thermally induced protein unfolding [276].

## The Isothermal Method

The essence of the isothermal method is illustrated in figure 12.9 [245,246, 249,254]. When studying a phase transition or a chemical reaction, it is possible to begin the experiment slightly below the expected onset (e.g., 0.5 K) and increase the temperature in very small steps (typically 0.1 K) over an interval large enough to include the event under investigation. A peak will be originated by each temperature change, and the corresponding trace will be allowed to return to the baseline before each new increment. The transformation undergone by the sample (which, in the case of figure 12.9, corresponds to an endothermic process) is represented by the large peak observed between ( T e -0.1K ) and T e in figure 12.9a.

The overall enthalpy change of the sample in an arbitrary temperature interval, T b -T a , comprising the transformation, is given by

<!-- formula-not-decoded -->

where A represents the sum of the areas of all peaks recorded in the main experiment between T a and T b, and B is the analogous sum for the zero line. The corresponding enthalpy change under isothermal conditions, at the reference temperature T e, can be derived from

<!-- formula-not-decoded -->

where m is the mass of sample, and cp ,i and cp ,f the corresponding massic heat capacities in the initial and final states of the transformation, respectively. These heat capacities may be obtained as a function of the temperature by comparing the areas of series of peaks recorded before and after the transformation, with the areas of the corresponding peaks in the zero line:

<!-- formula-not-decoded -->

where Ai is the area of the i th peak in the sample curve; Bi is the corresponding peak in the zero line; T a, i and T b, i are the initial and final temperatures of the peak, respectively; and c p , Ti ( S ) is the heat capacity of the sample at Ti , the midpoint of the T b, i -T a, i interval. Note that this procedure can be applied as an alternative to the determination of heat capacities of substances by the dynamic method already described.

If, as shown in figure 12.9a, the whole transformation strictly occurs in the interval ( T e -0.1K ) → T e, then the corresponding enthalpy change HT e -HT e -0.1 can be calculated from equation 12.37 by using the areas of two peaks only: (i) the large peak recorded in the main experiment between T e -0.1K and T e, and (ii) the corresponding peak for the zero line. In this case, the process is quasi-isothermic because the initial and final temperatures differ by only 0.1 K. Therefore, unless

Figure 12.9 Scheme of a DSC curve for the study of an endothermic process by the isothermal method (a) and of the corresponding zero line (b). The numbers represent differences to the temperature T e .

<!-- image -->

the transformation is accompanied by a very large heat capacity change, the heat capacity corrections required to obtain the enthalpy of the transformation at T e can safely be neglected and /Delta1 HT e ≈ HT e -HT e -0.1 .

Analogously to the dynamic method, the energy equivalent of the calorimeter, kQ , can be obtained by performing calibration experiments in the isothermal mode of operation, using electrically generated heat or the fusion of substances with well-known /Delta1 fus H . Recommendationsforthecalibrationofthetemperaturescale of DSC instruments for isothermal operation have also been published [254,270].

In principle, any system studied by the dynamic method can also be studied by the isothermal method, provided that the kinetics of the process is not too slow at the onset temperature. Very slow events result in shallow and broad peaks, which may be difficult to integrate accurately.

## Photoacoustic Calorimetry

'Any chemical species, which under ambient conditions (i.e., a temperature around 25 ◦ C, and a pressure close to 1 atm) will, for a combination of kinetic and thermodynamic reasons, decay on a timescale ranging from microseconds, or even nanoseconds, to a few minutes' can be classified as a short-lived compound. According to this definition, suggested by Almond [277], it is clear that the experimental methods described in previous chapters can only be used to study the thermochemistry of long-lived substances.

Thetechniquethatweaddresshere,knownasphotoacousticcalorimetry(PAC) or laser-induced optoacoustic calorimetry (LIOAC), is suitable for investigating the energetics of molecules with lifetimes smaller than about 1 µ s. It relies on the photoacoustic effect, which was discovered by Bell more than 100 years ago.With the assistance of Tainter, he was able to 'devise a method of producing sounds by the action of an intermittent beam of light' and conclude that the method 'can be adapted to solids, liquids, and gases' [278]. Figure 13.1 shows a photophone , 'an apparatus for the production of sound by light,' used by Bell to investigate the photoacoustic effect. The controversy around the origin of this phenomenon was settled by Bell himself and by Lord Rayleigh; their views were rather close to our present understanding: When a light pulse is absorbed by a substance, a given amount of heat is deposited, producing a local thermal expansion; this thermal expansion propagates through the medium, generating sound waves (see figure 13.2).

The basic theory of the photoacoustic effect was described by Tam and Patel [279,280] and some of its applications were presented in a review by Braslavsky and Heibel [281]. The first use of PAC to determine enthalpies of chemical reactions was reported by the groups of Peters and Braslavsky [282,283]. The same groups have also played an important role in developing the methodologies to extract those thermodynamic data from the experimentally measured quantities [282-284]. In the ensuing discussion, we closely follow a publication where the use of the photoacoustic calorimety technique as a thermochemical tool was examined [285].

Consider the elementary design of a photoacoustic calorimeter, shown in figure 13.3.The cell contains the sample, which is, for instance, a dilute solution of a photoreactive species. When the laser pulse travels throughout the cell, part of its energy is absorbed by the photoreactive compound and initiates the process of interest, while the remaining excess laser energy is deposited in the solution

Figure 13.1 Bell's photophone. Two similarly perforated disks (B), one stationary and the other subject to rapid rotation (note another good application of a sewing machine) were used to produce the pulsed light beam. This beam was aimed at a parabolic reflector. A glass vessel containing 'lampblack or other sensitive substance' was placed at the reflector's focus and connected to a hearing tube. 'In operating the instrument, musical signals like the dots and dashes of the Morse alphabet are produced from the sensitive receiver (A) by slight motions of the mirror (C) about its axis (D).' Adapted from [278].

<!-- image -->

Figure 13.3 A simplified diagram of a photoacoustic calorimeter. Adapted from [285].

<!-- image -->

as heat. As stated, this abrupt and localized heating causes the solution to expand locally, thus producing a wave that propagates through the fluid at the speed of sound. Being an acoustic wave, it can be detected by a simple microphoneoscilloscope arrangement. Moreover, because the photoacoustic phenomenon is very fast (typically in the microsecond range), the microphone is an ultrasonic piezoelectric transducer, and the oscilloscope is a very fast digital one. The amplitude S of the acoustic wave thus measured (figure 13.4) is, in a first analysis, proportional to the volume increase ( /Delta1 v ) of the irradiated region of the sample, as shown by equation 13.1.

<!-- formula-not-decoded -->

Here, the proportionality constant K d is a function of the geometry of the calorimeter and other instrument parameters (e.g., laser beam shape and its position relative to the transducer).

The volume increase is in turn due to the thermal expansion mechanism referred to above. It can be quantified by equation 13.2,

<!-- formula-not-decoded -->

which states that /Delta1 v is proportional to the laser energy absorbed by the solution, given by ( 1 -T ) E , where T is the sample transmittance and E the laser pulse energy. The yield of this conversion from radiant to thermal energy is the interesting experimental quantity. It is represented by φ nr and indicates the fraction of the laser energy released nonradiatively in thermal relaxation processes. The adiabatic expansion coefficient of the solvent ( χ ) is related to some of its

with

Figure 13.4 Atypical photoacoustic signal. S is the amplitude of the first sound wave to be observed. The other (smaller) waves are reflections of the main sound wave in the cell walls and so reach the detector later. Adapted from [285].

<!-- image -->

thermophysical properties: the density ( ρ ), the heat capacity ( Cp ) , and the thermal expansion coefficient ( α) :

<!-- formula-not-decoded -->

Note that the parameter χ should refer to the solution and not the solvent. However, the use of dilute solutions in most PAC experiments makes that approximation acceptable. This subject is further discussed next.

Theworkingequation for photoacoustic calorimetry is simply the combination of equations 13.1 and 13.2:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The calibration constant K strongly depends on the instrumental specifications, geometry of the calorimeter ( K d ) , and the solvent thermoelastic properties ( χ ). It can be determined through a comparative assay made under the same conditions as the main experiment but using a photoacoustic calibrant instead of the sample compound. The calibrants are substances that have known values of φ nr from independent measurements, or more conveniently, substances that dissipate all of the absorbed energy as heat ( φ nr = 1), like ferrocene [286] or ortho -hydroxybenzophenone [287]. Note that the computation of K is not really needed, because a direct comparison of the signals obtained with sample and calibration compounds allows it to be eliminated from the calculations.

The desired enthalpic information for the phenomenon under investigation is obtained through a simple energy balance, whose terms obviously depend on the processes that occur in each specific system. The general form of that balance is given by equation 13.6,

<!-- formula-not-decoded -->

where E m is the molar energy input, corresponding to the laser photon energy N A h ν (e.g., E m = 354.87 kJ mol -1 for λ = 337.1 nm, the wavelength of a nitrogen laser), Φ f E f corresponds to the energy loss by fluorescence, and Φ u E u designates the 'useful' energy, the one used to drive the process of interest. For instance, in the simplest example of a single photochemical reaction, Φ u E u is equal to Φ r /Delta1 r H , Φ r being the reaction quantum yield. In this case, and in the absence of fluorescence, the energy balance is therefore given by equation 13.7:

<!-- formula-not-decoded -->

If the reaction quantum yield is known, its enthalpy ( /Delta1 r H ) can be determined after the amount of heat dissipated in solution ( /Delta1 obs H ) is obtained from the photoacoustic experiment by equation 13.8,

<!-- formula-not-decoded -->

Recall that the calculation of φ nr relies on equation 13.4. It is important to emphasize that the validity of this equation rests on two assumptions.The first is a direct consequence of the way the microphone responds to the rate of the process, as it originates the photoacoustic wave. All the 'fast' processes yield a measured waveform with the same time profile; all the 'slow' processes produce virtually no signal. Between these two extremes an intermediate regime exists, in which the time profile of the measured waveform varies to reflect the rate of the process. The fast and slow process rates are defined in relation to the intrinsic response of the microphone, determined by its characteristic oscillation frequency ν .

Consider figure 13.5, which displays simulated waveforms for a process that occurs at different rates (i.e., with different lifetimes). If τ represents the lifetime of the reactive intermediate, for processes with τ /lessmuch 1 /ν (fast processes, usually classified as 'prompt'), the wave amplitude will depend only on the amount of heat deposited during the process (see curves for 1 ns and 200 ns). As long as both experiment and calibration meet this time constraint, allowing a direct comparison between the two signals, equation 13.4 can be used. If, on the other hand, the process being measured is not fast enough (e.g., τ ≈ 1 /ν ; see curve for 1 µ s), the measured waveform will broaden to track its time profile, and its amplitude will decrease because of that (and not because of less heat being deposited), thus invalidating equation 13.4. Finally, slow processes ( τ /greatermuch 1 /ν) that may happen after the process of interest can be dismissed from the energy balance (see curve for 200 µ s), which is one of the main advantages of this technique. For instance, recall the case of a photochemical reaction and consider that the products are transient species, for example, radicals. The process of interest (the reaction) is the only prompt one, the only one that takes place during

Figure 13.5 Simulated responses of a 0.5 MHz transducer for a process that occurs at different rates. The simulation was made with a simplified mathematical model. Adapted from [285].

<!-- image -->

the experimental time window, and can be quantified by the equations already presented.Although the radicals formed will be involved in subsequent chemistry, those processes will often be too slow to contribute to the signal, so they do not need to be considered in the energy balance.

In practice, the time constraint condition may be met by a careful choice of appropriate experimental conditions for a given transducer. Kinetic data for the process of interest is of great help in choosing those conditions. The validity of τ /lessmuch 1 /ν can easily be verified experimentally for the system of interest, by comparing the time profile of the calibration and sample waveforms or by varying conditions (e.g., sample concentration) until the experimental waveform reaches a maximum in amplitude.

The second assumption of equation 13.4 is that the photoacoustic wave is generated exclusively by thermal expansion of the irradiated region. The first assumption, just discussed, may often be met by carefully chosen experimental conditions, whereas this second one is usually more difficult to handle and was overlooked in the early applications of PAC, as pointed out by Hung and Grabowski [288] and by Clark et al. [289]. In addition to the thermal expansion mechanism for photoacoustic wave generation, the processes studied by PAC are frequently accompanied by 'intrinsic volume changes,' a phenomenon that also results in sound wave emission. Examples of such processes include the production of excited states with large changes in polarity and chemical reactions such as photodissociations. The production of sound waves through this mechanism is analogous to that caused by thermal expansion, but now the expansion of the material is chemically induced when the solvent molecules rearrange themselves around the space occupied by the new chemical species. Although both mechanisms are responsible for the photoacoustic signal, only the thermal contribution

is related to the enthalpy of the process, and application of equation 13.4 without explicitly separating the intrinsic volume contribution can lead to significant errors. Equation 13.4 must be modified to allow for both contributions. This can simply be made by replacing the 'true' nonradiative yield ( φ nr ) with φ obs , the 'apparent' (or 'observed') fraction of photon energy released as heat:

<!-- formula-not-decoded -->

The correct derivation of the remaining working equations involves replacing equation 13.1, which only takes into account the thermal volume increase, with equation 13.10, where both contributions are considered. The thermal volume change in equations 13.1 and 13.2 was renamed /Delta1 th v to distinguish it from the intrinsic (or 'chemical') volume change /Delta1 chem v .

<!-- formula-not-decoded -->

Similarly to equation 13.2, the intrinsic volume change can be expressed in terms of measurable quantities, according to equation 13.11:

<!-- formula-not-decoded -->

where /Delta1 chem V is the molar intrinsic volume change and the quotient is the amount of substance of photoexcited molecules (assuming single-photon excitation). Both volume contributions (equations 13.2 and 13.11) can now be introduced in equation 13.10, yielding equation 13.12:

<!-- formula-not-decoded -->

Finally, combining equations 13.5, 13.9, and 13.12, the experimentally accessible quantity ( φ obs ) is related to the fraction actually converted into heat ( φ nr ) :

<!-- formula-not-decoded -->

Equation 13.13 shows that the enthalpic contribution can be distinguished from the reaction volume by measuring φ obs as a function of the adiabatic expansion coefficient ( χ ). A number of experimental methodologies have been developed to exploit this relationship. In the case of aqueous solutions, there are several examples in the literature where both contributions have been determinedbystudyingthephotoacousticsignalasafunctionoftemperature[290,291] because the χ of water has a large temperature dependence. For organic solvents, where χ varies only slightly with temperature, Hung and Grabowski have shown that the same information can be obtained by using a series of solvents (with different values of χ ), for which it is expected that /Delta1 chem V and /Delta1 r H (or φ nr ) remain constant (e.g., a series of alkanes) [288]. Alternatively, it is possible to vary χ of a solvent by changing the pressure. This has been done by Farrell and Burkey, who used a photoacoustic calorimeter with a hydrostatic apparatus capable of achieving high pressures [292].

In some instances the volume contribution can be estimated or indirectly derived by separate experiments using auxiliary reactions [293]. In either case, the experimentally accessible quantity is φ obs and not φ nr. The observed fraction of photon energy is then related by equation 13.14 to the observed heat deposited in solution ( /Delta1 obs H ) . For the simple case of the single photochemical reaction (equation 13.7), the reaction enthalpy is calculated from /Delta1 obs H through the energy balance in equation 13.15, where the correction for the reaction volume term was carried over from equation 13.13 and related to the true reaction volume change, /Delta1 r V , defined in equation 13.16.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Note that Φ r is the total quantum yield for the formation of freely diffusing products (in contrast with the primary quantum yield for the extremely fast formation inside the solvent cage), because that is the process that takes place during the experimental time window.

It should also be pointed out that the approximations of equation 13.4 hold for the special group of substances that are chosen as photoacoustic calibrants. As already mentioned, these are substances that dissipate all of the absorbed energy as heat, but they do so entirely via a thermal mechanism (no net volume change) that is also very fast (prompt).

Let us now describe in more detail the main components of a photoacoustic calorimeter and later use this account to illustrate how an experiment can be done. There are several designs of photoacoustic calorimeter, but the most important variations concern the cell. For instance, the cells built by Lynch and Endicott [294] and by Arnault et al. [295] are quite different from the rather simple (and commercially available) flow-through quartz cell used by Griller and co-workers [296]. This type of cell was also adopted in the instrument outlined in figure 13.6.

The photoacoustic calorimeter of figure 13.6 can be divided into three subsets of instruments converging on the sample cell. The first set is used to initiate the photophysical process in the cell; the second allows the detection and measurement of the photoacoustic signal produced; the third is used to measure the solution transmittance. A flow line conducts the solution throughout the system. The calorimeter can operate under inert atmosphere conditions, and the temperature variation during an experiment is less than 0.5 K.

The initiation system consists of a nitrogen laser and the necessary optics to lead the beam to the sample cell. The laser emits pulses at 337.1 nm with 800 ps duration, with a typical repetition rate of less than 5 Hz. The optical components, aligned between the laser and the calorimetric cell, consist of an iris (I), a support for neutral density filters (F), and a collimating lens (L). The iris is used to cut out most of the laser output and allow only a thin cylinder of light to pass through its aperture, set to ∼ 2 mm. The laser energy that reaches the cell is further

Figure 13.6 Diagram of a photoacoustic calorimeter. The components are described in the text. Adapted from [285].

<!-- image -->

controlled by means of one or more neutral-density filters. The collimating lens focuses the beam just before the calorimetric cell, where it arrives with a width of ∼ 1 mm. This focusing operation is critical in obtaining a good photoacoustic wave. The sample cell is a standard quartz flow-through cuvette with 10 mm path length and is placed atop a piezoelectric transducer (PZT).

One important aspect of any PAC set-up concerns the width of the beam as it arrives at the cell. The extremely high photon density at the beam focus can cause multiphotonic processes that invalidate equation 13.4 (and hence 13.9). On the other hand, a beam too wide can lead to more than one photoacoustic generation site, also invalidating the assumptions made in deriving equation 13.4. The laser energy reaching the cell is measured with a pyroelectric probe (see following discussion) when the cell is filled with a transparent solvent. In the calorimeter of figure 13.6, that energy is ∼ 30 µ J.

Thephotoacousticmeasuringsystemconsistssimplyofthepiezoelectrictransducer connected to a digitizing oscilloscope through a preamplifier. The oscilloscope, together with the remaining main measuring devices of the calorimeter, is interfaced with a personal computer (PC) that controls the data acquisition during the photoacoustic experiments. The transducer has a characteristic frequency of 0.5 or 1 MHz, which, as explained before, determines the time window of the calorimeter. The photoacoustic signals detected by the transducer are first amplified and then digitized and stored in the oscilloscope. Usually at least 32 laser shots are used to produce one waveform like the one displayed in figure 13.4, and five of these waveforms are averaged to produce a single data point for analysisthe amplitude of the photoacoustic signal S . This amplitude is arbitrarily defined as the first peak-to-peak distance (instead of, for instance, the height of the first peak), which avoids the need to define the position of the baseline.

In the calorimeter depicted in figure 13.6 there are two independent systems to measure the sample transmittance. Both have advantages and disadvantages, and both have been adopted in other photoacoustic calorimeters described in the literature. When used simultaneously, they provide a straightforward way to test whether the assumptions of equation 13.1 are being met (e.g., testing for multiphoton effects) and generally allow for more confidence in the experimental results.

The first system for measuring transmittance uses a pyroelectric probe that monitors the laser beam intensity just after the calorimetric cell.The signal is then amplified and stored in an energy meter. This is then connected to the computer for data acquisition and control. The same number of laser shots as before are used for each reading of laser energy, and the results of five readings are averaged to produce a single data point for analysis, according to the calculation methods described. The detection limit of this system is 1 µ J.

Thesecondsystemfor measuring the transmittance incorporates a spectrophotometer tuned at the laser wavelength, whose sample cell is also a standard flow-through quartz cuvette, identical to the calorimetric cell from which the solution flows. This option needs a reference system to allow the normalization of the photoacoustic signal, because the laser energy varies slightly from pulse to pulse. It should be recalled that what is measured with the photoacoustic calorimeter is the relation between the photoacoustic signal and the solution transmittance (equation 13.9). In the first system, involving the pyroelectric probe, the normalization is unnecessary as both measurements are made simultaneously at the same site, and the beam for the transmittance measurement is the same one that drives the photoacoustic signal. Therefore, variations in the beam energy will affect both measurements to the same extent and will cancel. When the spectrophotometer is used, the two measurements are made independently, so a system that compensates for laser energy fluctuations in the photoacoustic signal generation is required. This reference system is basically a laser energy measuring device. The normalization consists simply of dividing the photoacoustic signal by the laser energy of the pulse that originated it, measured with the reference system. In the calorimeter sketched in figure 13.6, the laser energy is monitored by means of the photoacoustic effect itself. Part of the laser energy is deflected with a beam splitter (BS) to a duplicate of the principal photoacoustic measuring system, which includes a reference cell, a piezoelectric transducer, and a preamplifier, all identical to their principal counterparts, and connected in the same way to the oscilloscope. The reference cell contains a solution of a photoacoustic calibrant (e.g., ortho -hydroxybenzophenone in iso -octane).

It should be pointed out that a certain amount of reference solution must be kept flowing through the reference cell, otherwise the signal amplitude diminishes gradually with time. This effect should correspond to a local depletion of ortho -hydroxybenzophenone at the laser illuminated region in the cell. In the calorimeter of figure 13.6 , the solution is circulated by a peristaltic pump and flows from a glass reservoir through the cell and again to the reservoir in a closed loop.

The sample flow line is the last part of the calorimeter of figure 13.6 worth mentioning here. The reason that the sample solution must be kept flowing is to avoid local sample depletion. The flow line starts at a specially designed Schlenktype glass reservoir and includes a number of valves (V1, V2) and a syringe (S). The solution is pushed through the calorimeter by means of a small positive pressure of argon in the reservoir. The samples are prepared in this container, usually by dilution of stock solutions, and have absorbance values typically between 0.01 and 0.13. Further details of the photoacoustic calorimeter shown in figure 13.6 were described by Borges dos Santos et al. [285]. Now let us see how a typical experiment is done.

As mentioned previously, a photoacoustic calorimetry experiment consists of two consecutive runs, the calibration and the experiment. In the first one, a photoacoustic calibrant is used to determine the proportionality constant K in equation 13.9. Then the procedure is repeated with the sample of interest, ensuring that the time constraint referred to is met and also that the experimental conditions are as close as possible to the calibration (maintaining constant the factors that affect K ) . Because the procedure is identical for both calibration and experiment, it will be illustrated here for the simpler case of the calibration ( φ nr = φ obs = 1 ) for which equation 13.9 reduces to equation 13.17:

<!-- formula-not-decoded -->

This equation shows that to determine K , one can either plot the photoacoustic signal amplitude S against the transmittance factor (1 -T ), keeping the laser energy E constant, or against E if (1 -T ) is kept constant. These two calculation methods correspond to two possible experimental procedures: varying the solution transmittance and varying the laser energy. Both have been described in detail in the literature [285], and here we only briefly discuss the latter.

The laser energy can be changed by the interposition of different neutral density filters and measured using the pyroelectric probe, despite being positioned after the cell, because the solution is the same throughout the experiment ( T is constant). To keep the experimental conditions identical between calibration and experiment, the measurements have to be normalized by the transmittance factor, according to equation 13.18.

<!-- formula-not-decoded -->

Ideally, the solutions used in the experiment and calibration should be optically matched (i.e., their transmittances should differ by less than ∼ 2%).

The experimental procedure starts by acquiring the data for the blank conditions, and so the calorimeter cells are filled with argon-purged blank solution. The corresponding average values of photoacoustic signal S 0, laser energy E 0, and reference signal S R0 are recorded. An argon-purged sample solution with the appropriate concentration (usually with an absorbance near 0.100) is flowed through the calorimeter cell, and S 1, E 1, and S R1 are recorded. Other data points ( S i , E i, and S Ri ) are obtained by interposition of the appropriate neutral

density filter. Analysis of these values is made with equations 13.19 and 13.20, corresponding to calibration (C) and experiment (E ) respectively.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The transmittance values for the calibration and experiment solutions can be measured either with the spectrophotometer or with the pyroelectric probe. In the first case, this reading can obviously be done at any time after the calorimeter is filled with the solution. In the latter case, the value is computed by using equation 13.21.

<!-- formula-not-decoded -->

/ Note that in this equation the laser energy is normalized with the reference signal (R), thus canceling eventual laser fluctuations between measurements for the blank and first data point measurements.

Figure 13.7 shows the application of this method for a typical calibration and experiment, respectively. A value of φ obs = 1.060 is obtained by the ratio between the slopes of the lines (b) and (a), which refer to equations 13.20 and 13.19, respectively.

The procedure described, involving the variation of the laser energy, has some advantages relative to the alternative method of using several solutions with different transmittances. First, it provides a check for multiphoton effects simply by analyzing the quality of the linear correlations obtained. It should be stressed that the excellent correlations in figure 13.7 are typical, that is, correlation factors are usually better than 0.9995. Second, the method requires considerably less sample (only one solution is needed). Third, the analysis of experimental data is also conceptually simpler, because no normalization is required.

What are the main error sources in PAC experiments? One of them may result from the calibration procedure. As happens with any comparative technique, the conditions of the calibration and experiment must be exactly the same or, more realistically, as similar as possible. As mentioned before, the calibration constant depends on the design of the calorimeter (its geometry and the operational parameters of its instruments) and on the thermoelastic properties of the solution, as shown by equation 13.5. The design of the calorimeter will normally remain constant between experiments. Regarding the adiabatic expansion coefficient ( χ ), in most cases the solutions used are very dilute, so the thermoelastic properties of the solution will barely be affected by the small amount of solute present in both the calibration and experiment. The relevant thermoelastic properties will thus be those of the solvent. There are, however, a number of important applications where higher concentrations of one or more solutes have to be used. This happens, for instance, in studies of substituted phenol compounds, where one solute is a photoreactive radical precursor and the other is the phenolic substrate [297]. To meet the time constraint imposed by the transducer, the phenolic

Figure 13.7 (a) Results of calibration using a solution of ferrocene in benzene (correlation coefficient 0.9998). (b) Results of an experiment involving the abstraction of the hydroxylic hydrogen in phenol by tert -butoxyl radicals, in benzene (correlation coefficient 0.99998). Adapted from [285].

<!-- image -->

<!-- image -->

substrate must sometimes be used in relatively high concentrations. For these experimentally more complex applications, it is important to stress the assumptions on which the calculations presented are based: The thermoelastic properties are those of the solvent, and the optical properties are those of the photoreactive solute. Any deviation from these conditions (strong influence of the solute on the thermoelastic properties of the solution or considerable absorption of the substrate) will lead to errors in the final result.

Further complications may arise when more concentrated solutions are used, even before reaching the limiting conditions that invalidate equations 13.4 or 13.9. The most noticeable problem is the appearance of multiphoton effects, for which the relation between photoacoustic signal and energy absorbed is no longer linear. As mentioned, this phenomenon is easily detected by a deviation

from linearity in the plots illustrated in figure 13.7, and can be avoided either by diluting the photoreactive compound or by decreasing the laser energy supplied to the solution. Absorption by the photoproducts may also lead to nonlinear plots [295]. Other problems usually associated with the use of more concentrated solutions include auto-quenching processes, oxygen quenching (if the purging of the solution was inefficient), and reabsorption processes (if the substance is strongly fluorescent) [281]. For the specific case of the photoacoustic study of reactions involving radical species, the use of high concentrations not only of the photoreactive compound but also of the substrate will strongly influence the decay kinetics of the metastable species, complicating the analysis of the results.

To illustrate an application of PAC, we chose reaction 13.22, which has been suggested as a 'test reaction' for photoacoustic calorimetry, that is, as a procedure to assess the reliability of the instrument [285]. Wayner et al. [293] made a very careful PAC study of this reaction in several solvents.

<!-- formula-not-decoded -->

Reaction 13.22 is the net result of two steps, the first being the photochemical cleavage of the O-O bond in ditert -butylperoxide (reaction 13.23), followed by the abstraction of the hydroxylic hydrogen in phenol by the tert -butoxyl radical (reaction 13.24).

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In a typical experiment, the sample is a solution (e.g., in benzene) of both the tert -butoxyl radical precursor (ditert -butylperoxide) and the substrate (phenol). The phenol concentration is defined by the time constraint referred to before. The net reaction must be complete much faster than the intrinsic response of the microphone. Because reaction 13.23 is, in practical terms, instantaneous, that requirement will fall only on reaction 13.24. The time scale of this reaction can be quantified by its lifetime τ r, which is related to its pseudo-first-order rate constant k [PhOH] and can be set by choosing an adequate concentration of phenol, according to equation 13.25:

<!-- formula-not-decoded -->

The actual limit value of τ r, below which the time constraint is met for a given transducer, is somewhat ambiguous. For a 0.5 MHz transducer (response time 2 µ s), Mulder et al. [297] set this limit at 60 ns, based on the observation of a maximum of amplitude of the photoacoustic wave with the concentration of phenol and calculating τ r from the rate constant of reaction 13.24, k = 3.3 × 10 8 mol -1 dm 3 s -1 [298]. Later, Wayner et al. [293] empirically choose 100 ns as that limit and used laser flash photolysis results to adjust the phenol concentration until the lifetime of reaction 13.24 was less than that limit. In any case, the safest way of ensuring that the time constraint is being met is to verify it experimentally by varying the concentration of substrate until the observed waveform reaches a maximum (or, equivalently, until the final /Delta1 obs H value reaches a maximum).

It is important to stress that the experiment must be preceded by a calibration made with the calibrant dissolved in the same phenol solution used in the experiment, to ensure that the thermoelastic properties of the fluid will be as close as possible in the two runs.

The results derived from the PAC study of the reaction between phenol and ditert -butylperoxide are shown in figure 13.7 and lead to φ obs = 1.060, as mentioned before. Using equation 13.14, we obtain /Delta1 obs H = 376.2 kJ mol -1 . The final value of /Delta1 obs H (average of five independent experiments) was 374.7 ± 4.7 kJ mol -1 [285].

The enthalpy of reaction 13.22 can then be calculated as -7.4 ± 10.0 kJ mol -1 by using equation 13.15 and selected values of Φ r (0.83 ± 0.03), /Delta1 r V (13.4 ± 4 cm 3 mol -1 ) , and χ (0.813 cm 3 kJ -1 ) [285]. That reaction enthalpy may now be used to derive information on the phenolic O-H bond dissociation enthalpy and on the solvation energetics of the phenoxy radical, according to the procedures discussed in section 5.1.

One may be somewhat disappointed by the error bars in /Delta1 obs H and /Delta1 r H , which are larger then most obtained by 'classical' calorimetric methods, such as reaction-solution or combustion calorimetry. However, the comparison is unfair because PAC deals with species that have lifetimes smaller than a microsecond, not amenable to those classical methods. Although the quality of the photoacoustic measurements is rather good, as shown by the correlations obtained (see figure 13.7), a realistic error in the ratio of the slopes ( φ obs ) is ∼ 1-2%, which implies an uncertainty in /Delta1 obs H of 4 to 8 kJ mol -1 . This error bar is particularly serious when the reaction quantum yield is low (recall equation 13.15).

One of the main limitations of the experimental methodology described above is related to the time constraint. It hinders the study of many interesting reactions that are too slow to ensure that the amplitude of the photoacoustic wave is independent of the kinetics of the process. This is the case, for instance, of transient lifetimes in the range of 100 ns to 0.1 ms for a 0.5 MHz transducer. Fortunately, there is an alternative procedure to deal with those cases where the condition τ /lessmuch 1 /ν does not hold. The procedure, known as time-resolved PAC (TR-PAC), was developed by Peters and co-workers [282,284,299] and considers that the observed wave, S exp ( t ) , reflects the kinetics of the true heat deposition, S ( t ) , as well as the detector response wave, T ( t ) . In other words, S exp ( t ) is the convolution of S ( t ) with the transducer function, T ( t )

<!-- formula-not-decoded -->

To derive S ( t ) , a deconvolution procedure is required. The transducer function is easily obtained by running an experiment where the photoactive species decays with τ /lessmuch 1 /ν , which is the case of the photoacoustic calibrants mentioned. Recall that when this condition applies, the photoacoustic wave does not depend on the decay kinetics of the transient.

The deconvolution algorithms were developed by Rudzki et al. [284,300] and are now commercially available as computer software [301]. For instance, in the case of two sequential reactions (equation 13.27) producing two heat decays,

the first being very fast, S ( t ) is the sum of S 1 ( t ) and S 2 ( t ) , which are given by equations 13.28 and 13.29, respectively.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Anexample of the deconvolution process applied to reactions 13.23 and 13.24 is shown in figure 13.8. The method consists of finding the best set of the parameters φ 1, φ 2, k 1, and k 2 that fit S exp ( t ) . Note that the nonradiative yields for the first and the second processes ( φ 1 and φ 2, respectively) are φ obs and not φ nr . Once φ 1 and φ 2 are known, the respective enthalpies are calculated from equations 13.14 and 13.15. Equation 13.15 can be written as

<!-- formula-not-decoded -->

where the subscripts 1 and 2 refer to the first and second reactions. Equation 13.30 can also be given as the sum of equations 13.31 and 13.32. Note that the latter represents the energy balance for the second (nonphotochemical) process. Therefore, the molar photon energy is not included in the balance ( E m = 0).

Figure 13.8 Deconvolution process applied to reactions 13.23 and 13.24. a is the experimental waveform, S exp ( t ) ; b is the calculated waveform for t -BuOOBut photolysis; and c is the calculated waveform for the hydrogen abstraction from PhOH. Note that c is phase shifted to a longer time because it refers to a 'slow' process.

<!-- image -->

It should also be pointed out that equation 13.32 assumes that the yield of the second reaction is 100%, that is, all the reactive species B decays into C.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/Delta1 obs H 1 and /Delta1 obs H 2 are calculated with two equations similar to 13.14 (making φ obs equal to φ 1 and φ 2, respectively).

Let us look at an example involving the ligand exchange reactions 13.33 and 13.34 [149,302,303]:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The first of these reactions is the photochemical cleavage of one Cr-CO bond, which is followed by the coordination of a solvent molecule (S) to Cr(CO)5. This coordination process is extremely fast (it takes less than 25 ps). The second (slower) step is the replacement of the solvent molecule by ligand L (reaction 13.34). /Delta1 r V was assumed to be negligible for both reactions.

As the enthalpy of reaction 13.34 can be given as a solution phase bond dissociation enthalpy difference,

<!-- formula-not-decoded -->

results for a series of L, in the same solvent S, afford DH sln [ Cr(CO) 5 -L ] data relative to a constant DH sln [ Cr(CO) 5 -S ] value. By applying the deconvolution procedure, Y ang, Peters, and Vaida were able to derive the values of φ 1, φ 2, and k 2 for several ligands, such as tetrahydrofuran, ethanol, and acetone. For S = n -heptane and L = acetonitrile, and assuming a quantum yield of 0.67, the experimental values of φ 1 and φ 2 lead to /Delta1 r H ( 13.33 ) = 112.1 ± 4.5 kJ mol -1 and /Delta1 r H ( 13.34 ) = -76.1 ± 4.5 kJ mol -1 , respectively [302]. However, these quantities were subsequently recalculated using a revised value of 0.74 for the quantum yield of Cr(CO)5 -CO dissociation in n -heptane [149], leading to significantly different results: /Delta1 r H ( 13.33 ) = 101.5 ± 4.5 kJ mol -1 and /Delta1 r H ( 13.34 ) = -68.9 ± 4.5 kJ mol -1 . These discrepancies illustrate the importance of Φ r in obtaining accurate reaction enthalpies from PAC experiments.

Time-resolved PAC has also been applied to investigate the thermochemistry of reactions involving the cleavage of C-H, O-H, and S-H bonds by a method similar to the one described by equations 13.23 and 13.24 [304-310]. In these cases, the hydrogen abstraction reactions were too slow to be examined by non-time-resolved PAC. Other advantages of using TR-PAC were described by Correia et al. [308]. Finally, it is noted that TR-PAC can also be used to derive rate constants of hydrogen abstraction reactions [311].

## Equilibrium in Solution

Ageneral discussion of the second and third law methods, including their advantages and limitations relative to first law techniques, was presented in sections 2.9 and 2.10. Now, after a summary of that introduction, we examine some examples that apply the second law method to the thermochemical study of reactions in solution. Recall that the third law method is only practical for reactions in the gas phase.

Both the second and third law methods rely on the experimental determination of equilibrium constants. As shown in section 2.9, the equilibrium constant ( K ) of a reaction is defined in terms of the activities ( a i ) of reactants and products:

<!-- formula-not-decoded -->

where ν i are the stoichiometric coefficients of the reaction. In most real situations, the activity values are difficult to obtain, so they are replaced by other quantities. In the case of reactions in solution, if the ideal model is assumed, we have seen that K is identified with Km , the equilibrium constant defined in terms of the molalities ( m i ) of reactants and products:

<!-- formula-not-decoded -->

m o being the standard molality, equal to 1 mol kg -1 .

Althoughmolalities are simple experimental quantities (recall that the molality of a solute is given by the amount of substance dissolved in 1 kg of solvent) and havetheadditionaladvantageofbeingtemperature-independent,mostsecondlaw thermochemicaldatareported in the literature rely on equilibrium concentrations . This often stems from the fact that many analytical methods use laws that relate the measured physical parameters with concentrations, rather than molalities, as for example the Lambert-Beer law (see following discussion). As explained in section 2.9, the equilibrium constant defined in terms of concentrations ( Kc ) is related to Km by equation 14.3, which assumes that the solutes are present in very small amounts, so their concentrations ( c i ) are proportional to their molalities: m i = c i /ρ ( ρ is the density of the solution).

<!-- formula-not-decoded -->

Therefore, Km is numerically equal to Kc when the sum of stoichiometric coefficients is zero or when ρ = 1.

When a simple van't Hoff plot is applied (i.e., when ln Km is plotted against 1 / T ) , the reaction enthalpy and entropy at the mean temperature T of the experimental temperature interval are calculated from the slope and the intercept of equation 14.4:

<!-- formula-not-decoded -->

If Km is replaced by Kc , then this equation becomes ( m o = 1 mol kg -1 )

<!-- formula-not-decoded -->

range of 0.7-2 kg dm -3 (typical of many organic solvents). In this case, the last term of equation 14.5, -R ln ρ , is in the range of -3 to 6 J K -1 mol -1 . As pointed out before, although this value is usually smaller than most experimental uncertainty intervals associated with the reaction entropy, the correction should not be neglected when the van't Hoff plots rely on Kc data.

Even if we assume a negligible temperature effect on the density, when ∑ i ν i /negationslash= 0 a plot of ln Kc versus 1 / T and the use of equation 14.5 without the last term lead to an error of several J K -1 mol -1 in the reaction entropy calculated from the intercept. This was illustrated in section 2.9 for ∑ i ν i = -1 and ρ in the

Any analytical method [312] suitable for determining equilibrium compositions of a reaction mixture at several temperatures can be used to obtain the enthalpy and the entropy of that reaction. The first example we describe involves a common analytical technique (infrared absorption spectroscopy) and addresses the energetics of the hydrogen bond between phenol and acetonitrile. This careful study on the equilibrium 14.6 was made by Sousa Lopes and Thompson more than 30 years ago [313].

<!-- formula-not-decoded -->

The solvent was tetrachloroethylene, and the equilibrium concentrations of reactants and products were determined in the temperature range of 23-79 ◦ C.

At each temperature, the equilibrium concentration of the product was obtained as the difference between the initial and the equilibrium concentrations of phenol, respectively, [PhOH] o and [PhOH]. The latter was determined from the maximum absorbance of the free O-H stretching band.A similar method was used to evaluate the equilibrium concentration of the acceptor acetonitrile, [CH3CN], which is given by the difference between the initial concentration of this acceptor, [CH3CN] o , and the concentration of the product, obtained before. In summary, the equilibrium constant can be represented by equation 14.7:

<!-- formula-not-decoded -->

It is important to note that the calculation of the initial concentrations of phenol ( ∼ 10 -2 mol dm -3 ) and acetonitrile (possibly ∼ 1 mol dm -3 ) were corrected for the density of the solvent at each temperature. The temperature effect on the molar absorption coefficient ( ε ) was also considered when relating [PhOH] to the absorbance of the O-H free band. This was empirically made by measuring the absorbances ( A ) of a phenol solution (in the same solvent and with a concentration similar to that used in the equilibrium study) over the experimental temperature range. For each temperature, the Lambert-Beer law [312],

<!-- formula-not-decoded -->

afforded the product ε l , where l is the absorbing path length. Each ε l value so obtained could then be used at the respective temperature to derive c = [PhOH] in the equilibrium experiments from equation 14.8.

To check that phenol was not self-associated at the concentration used, Sousa Lopes andThompsonrepeated the 'calibration' experiments (i.e., the study of the temperature variation of ε l ) for several phenol concentrations. Good linear plots of A against c at each temperature were observed, indicating that the LambertBeer law is valid and that the self-association is negligible.

One set of Kc values at several temperatures, obtained by Sousa Lopes and Thompson, is shown in table 14.1 and plotted in figure 14.1. This van't Hoff plot leads to equation 14.9.

<!-- formula-not-decoded -->

Here, the uncertainty intervals are standard deviations multiplied by Student' s t factor for 95% probability and 5 degrees of freedom ( t = 2.571) [48].

Values of /Delta1 r H o T and /Delta1 r S o T at the mean temperature T = 323 K can now be calculated by comparing equations 14.5 and 14.9. If we neglect the last term in equation 14.5, we obtain /Delta1 r H o 323 = -22.4 ± 1.2 kJ mol -1 and /Delta1 r S o 323 = -60.2 ± 3.7 J K -1 mol -1 .

Table 14.1 Equilibrium constants ( Kc ) of reaction 14.6 at several temperatures. Data from [313].

|   t / ◦ C |   K c |
|-----------|-------|
|        23 |  6.25 |
|        33 |  4.93 |
|        43 |  3.65 |
|        53 |  2.8  |
|        63 |  2.11 |
|        73 |  1.7  |
|        77 |  1.61 |

Figure 14.1 A van't Hoff plot for reaction 14.6. Data from [313].

<!-- image -->

Although we are not dealing with very dilute solutions, we may use the density term in equation 14.5 to estimate a correction to these values. However, we need to bear in mind that this estimate can be considered at several approximation levels. The most simple is to assume that ln ρ is constant in the experimental temperature range, and thus only the reaction entropy is affected. Using the value for the pure solvent, ρ = 1.6227 kg dm -3 (at 20 ◦ C) [48], we obtain /Delta1 r S o 323 = -56.2 J K -1 mol -1 . A more accurate calculation would include the variation of ln ρ with the temperature, which, in the absence of experimental data, can be estimated from the coefficient of thermal expansion of the solvent, α :

<!-- formula-not-decoded -->

where V is the molar volume of the solvent. It is easily seen that

<!-- formula-not-decoded -->

Because α is quite small for liquid solvents (ca. 10 -3 to 10 -4 K -1 ) [180,314], the change of ln ρ with T will have a negligible effect on the calculated /Delta1 r H o 323 and /Delta1 r S o 323 values.

The second example concerns the equilibrium study of reaction 14.12 in benzene over the temperature range of 6-80 ◦ C, which was reported by Bercaw and co-workers [315].

<!-- formula-not-decoded -->

In this equilibrium (a ' σ bond metathesis reaction'), the scandium-hydrogen bond in bis (pentamethylcyclopentadienyl)scandium hydride is replaced by a scandium-carbon bond in phenyl bis (pentamethylcyclopendienyl) scandium

<!-- image -->

L

=

H or C 6 H5

Figure 14.2 Structure of a bis (pentamethylcyclopendienyl) scandium complex.

(figure 14.2). Therefore, the reaction enthalpy reflects the difference between solution phase Sc-H and Sc-Ph bond dissociation enthalpies, and Kc is given by

<!-- formula-not-decoded -->

The ratio [ Sc ( Cp ∗ ) 2 Ph ] / [ Sc ( Cp ∗ ) 2H ] was obtained from relative heights of 1 H nuclear magnetic resonance (NMR) peaks, and [C6H6] was calculated from the density of benzene.The determination of [H2] was more complicated because this substance is also involved in a gas-liquid equilibrium. The procedure used by the authors is as follows.

If the volumes of the vapor and the liquid phase in the (sealed) NMR tube where the equilibrium was achieved are v 1 and v 2, respectively, and it is assumed that the vapor obeys the ideal model, the total amount of substance of H2 in the tube is given by

<!-- formula-not-decoded -->

where p H2 is the hydrogen pressure. The amounts of H2 in the two phases are related by Henry' s law [180,316],

<!-- formula-not-decoded -->

K being Henry's constant of hydrogen in benzene and x H2 the H2 mole fraction in the liquid phase. Now let us assume that Henry' s constant for the reaction mixture has the same value as for pure benzene at the same temperature. As the amount of H2 in the solvent will be very small, [H2] is proportional to its molar fraction [316], that is,

<!-- formula-not-decoded -->

where M is the molar mass of the solvent (benzene) and ρ the density of the solution. Equations 14.15 and 14.16 show that [H2] is proportional to the pressure, the proportionality constant being equal to ρ/( KM ) . Because the solubility of H2 in benzene is known as a function of temperature for p H2 = 1 atm [153], the

equilibrium hydrogen concentration can be derived from equation 14.17 (with p H2 in atmospheres):

<!-- formula-not-decoded -->

Replacing p H2 by the value given by equation 14.14, we obtain, after some rearrangement,

<!-- formula-not-decoded -->

which was the working equation reported by Bercaw and co-workers to calculate [H2]. To understand how n total was determined, we need to consider some technical details. The experiment started by introducing about 5.4 × 10 -5 mol of Sc(Cp*)2CH3 in 0.5 cm 3 of benzene. The solution was then cooled to -196 ◦ C and H2 at a pressure of 700 Torr was introduced. The tube was allowed to warm to 25 ◦ C and the solution stirred, so that the hydride complex, Sc(Cp*)2H, was nearly quantitatively produced, according to reaction 14.19.

<!-- formula-not-decoded -->

The next step involved cooling the reaction mixture to -196 ◦ C, removing the H2 at low pressure, and sealing the tube. This sealed tube was then used in the equilibrium measurements. When it warmed up, a fraction of the hydride complex reacted with benzene, yielding H2 and the phenyl complex, according to equilibrium 14.12. Therefore, the total amount of substance of H2 in equation 14.18 is given by the sum of the initial amount of substance of H2 ( n 0 ) and the amount of substance of Sc(Cp*)2Ph in equilibrium. The latter is easily calculated from the relative concentrations of Sc(Cp*)2Ph and Sc(Cp*)2H determined by 1 H NMR, and the known initial concentration of Sc(Cp*)2H (5.4 × 10 -5 × 1000/0.5 = 0.108 mol dm -3 ) . To evaluate the initial amount of substance of H2, consider the experimental procedure before and after reaction 14.19 takes place. When this reaction occurs (at 25 ◦ C) a certain amount of H2 remains in solution, and it can be calculated by an equation similar to 14.17. This amount will be equal to n 0, by assuming that (1) there is no further H2 solubilization when the tube is rapidly cooled to -196 ◦ C, and (2) only the H2 dissolved in the frozen reaction mixture is not removed by the evacuation procedure.

The previous description illustrates well the complications that may arise in second law studies when phase and reaction equilibria occur simultaneously. A number of assumptions are usually made, some of which may influence the final thermochemical results. For instance, it is possible that the equilibrium concentration of hydrogen obtained in the study by Bercaw and co-workers is not very accurate, because n 0 may be underestimated (the cooling to -196 ◦ C will increase the amount of H2 in the condensed phase). Nevertheless, this error, which is constant for all the measurements at different temperatures (average T = 316 K), will probably have a negligible effect on the calculated /Delta1 r H o 316 and /Delta1 r S o 316 values, 28.3 ± 1.9 kJ mol -1 and -5.3 ± 6.1 J K -1 mol -1 , respectively. These values were obtained from equation 14.20, which is a linear fit of the

Figure 14.3 Avan't Hoff plot for reaction 14.12. Data from [315].

<!-- image -->

van't Hoff plot shown in figure 14.3 (note that the value for /Delta1 r S o 316 does not need to be corrected with the last term of equation 14.5 because ∑ i ν i = 0 for reaction 14.12). The uncertainty intervals are standard deviations multiplied by Student' s t factor for 95% probability and 3 degrees of freedom ( t = 3.182) [48].

<!-- formula-not-decoded -->

The equilibrium pressure of hydrogen in the experiments by Bercaw and co-workers was rather small, allowing the use of the ideal gas model in equation 14.14. Although that pressure was not reported by the authors, the conclusion is obvious from the very low values of Kc shown in figure 14.3. Higher hydrogen pressures, even as low as 1 bar, would lead to the formation of Sc(Cp*)2H with nearly 100% yield, and thus equilibrium 14.12 could not be examined.

The ideal gas model cannot be used at high pressures. Under these conditions, as pointed out in section 2.9, we have to deal with fugacities. Neglecting this and other correction parameters may lead to large errors. The point can be illustrated with results obtained by Oldani and Bor, who studied equilibrium 14.21 in hexane over the temperature range of -21.5 to 19.6 ◦ C and under a CO pressure of 198 bar [317].

<!-- formula-not-decoded -->

The equilibrium concentrations of Rh2(CO)8 and Rh4(CO)12 were determined by infrared spectroscopy by monitoring the absorbance of the band at 1886.8 cm -1 , which corresponds to the stretching of the bridging carbonyls of the tetrarhodium complex. More details of the experimental procedure can be found in the original papers. For our purpose, it is enough to say that the equilibrium concentrations of the rhodium complexes were quite low ( &lt; 10 -3 mol dm -3 ) , but the same was not true for the CO concentration ( ∼ 2 mol dm -3 ; see

following discussion). In the absence of activity data, let us assume that the ideal solution model is valid, that is, that Km will be a good approximation of the true equilibrium constant:

<!-- formula-not-decoded -->

Because the concentration of CO is not negligible, we can no longer apply the simple relationship between molality and concentration ( m i = c i /ρ) to write the equilibrium constant in terms of concentrations.The correct relationship between these two quantities is now given by equation 14.23, where M and n are the molar mass and the amount of substance of the solvent, respectively, and M i and n i are the corresponding quantities for the three solutes.

<!-- formula-not-decoded -->

This equation can be simplified because as indicated, the contribution of the terms for the rhodium complexes will be negligible:

<!-- formula-not-decoded -->

Therefore, the relationship between Km and Kc is given by

<!-- formula-not-decoded -->

To determine the amount of substance and the concentration of carbon monoxide in solution, we have to relate these quantities to the CO pressure. That can be done as described by using Henry's law. The only (important) difference is that now the CO pressure is too high to justify use of the ideal gas model. Hence, for the present case, equation 14.15 becomes [316]

<!-- formula-not-decoded -->

where f CO is the fugacity of carbon monoxide at the experimental temperature and pressure. Once again, the relationship between [CO] and x CO is not as simple as equation 14.16 because the amount of carbon monoxide in solution is not small [316]:

<!-- formula-not-decoded -->

When this result and equation 14.26 are introduced in equation 14.25, we obtain

<!-- formula-not-decoded -->

or

Equation 14.28 would be the correct one to evaluate the equilibrium constant of reaction 14.21 at each temperature. However, instead of using this equation, Oldani and Bor calculated the equilibrium constant at each temperature from

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where s is the 'solubility factor' of CO in hexane under the experimental conditions, and ( 1 + 0.001 p CO ) is a 'correction due to the increase of the solution volume with the CO pressure' [317]. It is easily seen that this equation is equivalent to equation 14.29, because ( nM + n CO M CO ) / [ ρ ( n + n CO ) ] is the solution molar volume at the experimental temperature and pressure.

Theproblem of using any of the previous equations is that the solubility data of COinhexane are scarce [318]. Oldani and Bor estimated values for the solubility factors of CO in hexane based on literature data for other alkanes, for example, s = 0.012 mol dm -3 bar -1 at 20 ◦ C [319]. Note that this value implies that [CO] in hexane is about 2 mol dm -3 under the experimental conditions ( p CO = 198 bar).

<!-- formula-not-decoded -->

Based on these estimates and literature values for the fugacity, Oldani and Bor obtained equation 14.31, from which they derived the reaction enthalpy and entropy at the mean temperature of the experimental temperature range ( T = 272 K): /Delta1 r H o 272 = 58.6 ± 2.6 kJ mol -1 and /Delta1 r S o 272 = 304 ± 10 J K -1 mol -1 . The uncertainty intervals are standard deviations multiplied by Student' s t factor for 95% probability and 18 degrees of freedom ( t = 2.101) [48].

It is instructive to compare the thermochemical values with those obtained by the same authors when they assumed the ideal gas model (i.e., f CO = p CO ) and neglected the CO solubility change with temperature: /Delta1 r H o 272 = 45.5 kJ mol -1 and /Delta1 r S o 272 = 267 J K -1 mol -1 .

It is difficult to discuss the accuracy of the thermochemical results reported by Oldani and Bor, because they rely on some estimated data of unknown reliability. Based on a simple model that is used to predict reaction entropy changes, we anticipate that the entropy of reaction 14.21 would be considerably larger than 300 J K -1 mol -1 , possibly even higher than 400 J K -1 mol -1 [226].

What main conclusions can we draw from the three examples discussed here? First, although van't Hoff plots should involve Km rather than Kc data, the use of the latter may afford sensible and possibly accurate thermochemical values (always under the assumption of ideal solutions!), particularly if the density term of equation 14.5 is considered in the calculation of the reaction entropy. Second, due to the lack of gas solubility data, the second law method is much

more difficult to apply when phase and reaction equilibria occur simultaneously, particularly if high pressures are involved. Third, it is stressed that although the results of van't Hoff plots should always be referred to the mean temperature of the experimental range, they are usually reported at 298.15 K without any correction. This correction should not be ignored if a high-accuracy result is desired. For example, a small reaction heat capacity, for example, /Delta1 r C o p = 20 J K -1 mol -1 , and a 30 K temperature difference lead to a 0.6 kJ mol -1 change in the reaction enthalpy.

Single-temperature equilibrium constant values may also yield quantitative information about reaction enthalpies, provided that the entropy term can be estimated. Take, for example, reaction 14.32, which involves hydrogen transfer between two substituted phenols (ArOH andAr'OH; see examples in figure 14.4). Note that Kc = Km in this case.

<!-- formula-not-decoded -->

Second law studies by Lucarini, Pedulli, and Cipollone, using electron paramagnetic resonance spectroscopy, have shown that the entropy of this reaction in

<!-- image -->

toluene, at 298.15 K, for the phenols ArOH = 2 and 3 (figure 14.4) is very close to zero, namely /Delta1 r S o = -6.9 ± 1.5 J K -1 mol -1 and -3.0 ± 2.6 J K -1 mol -1 , respectively [320]. Therefore, by measuring at a single temperature (298.15 K) equilibrium constants for other reactions in benzene or toluene and assuming /Delta1 r S o = 0, the same group was able to report the reaction enthalpies for a series of substituted phenols [320,321]. Because each reaction enthalpy is equal to the difference between the solution phase bond dissociation enthalpies DH sln ( ArO -H ) and DH sln ( Ar ′ O -H ) , the authors were able to study the effect of the nature and the position of the substituent(s) on the phenolic O-H bond dissociation enthalpy (see also section 5.1).

It should be stressed that the condition /Delta1 r S o T ≈ 0 is not required to derive a series of relative values of reaction enthalpies from single-temperature equilibrium constants. We only need to ensure that /Delta1 r S o T remains constant. Consider, for example, the case of reaction 14.33 (see figure 14.5):

<!-- formula-not-decoded -->

Kc ( = Km ) values at 298.15 K were determined in tetrahydrofuran for several ligands (X), by Bryndza et al. [322]. If we write equation 14.5 for two such ligands (X and X') and subtract, we obtain

<!-- formula-not-decoded -->

Hence, if /Delta1 r S o T ( X ) ≈ /Delta1 r S o T ( X ′ ) ,

<!-- formula-not-decoded -->

that is, the ratio of the equilibrium constants will provide the difference between the reaction enthalpies. This was the approach followed by Bryndza et al.; by assuming constant reaction entropies for different X, the authors could derive a series of reaction enthalpies relative to /Delta1 r H o T = 0 for X = OH. Because each one of these /Delta1 r H o T values is related to the difference between DH sln ( Ru -OH ) and DH sln ( Ru -X ) , a series of relative Ru-X solution phase bond dissociation enthalpies could be obtained.

<!-- image -->

A final word of caution regarding the use of single-temperature equilibrium constants. Although this is a rather expeditious method to derive reaction enthalpies, the obtained values may be quite inaccurate. For instance, a 'small' 10 J K -1 mol -1 error in the estimated /Delta1 r S o T yields a 3 kJ mol -1 error in /Delta1 r H o T at 298.15 K.

## Kinetics in Solution

The main equations used to extract thermochemical data from rate constants of reactions in solution were presented in section 3.2. Here, we illustrate the application of those equations with several examples quoted from the literature. First, however, recall that the rate constant for any elementary reaction in solution, defined in terms of concentrations, is related to the activation parameters through equations 15.1 or 15.2.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation 15.1 yields the enthalpy and the entropy of activation respectively from the slope and the intercept of a ln ( k / T ) versus 1 / T plot (an Eyring plot). Equation 15.2 leads to the Arrhenius activation energy and the frequency factor, respectively, from the slope and the intercept of a ln k versus 1 / T plot (an Arrhenius plot). All the parameters refer to the mean temperature of the plot, and /Delta1 ‡ H o is related to E a by equation 15.3.

<!-- formula-not-decoded -->

Finally, recall that if the activation parameters are available for the forward (subscript 1) and the reverse (subscript -1) reaction, the enthalpy of this reaction is calculated by equation 15.4.

<!-- formula-not-decoded -->

In the preceding chapter on equilibrium in solution, it was pointed out that any analytical method suitable for determining equilibrium compositions of a reaction mixture at several temperatures can be used to obtain the enthalpy and entropy of that reaction. A similar statement can be made here: Any analytical method suitable for monitoring concentration changes with time at several temperatures can be used to derive the activation parameters of a reaction. Therefore, the analytical techniques used in equilibrium experiments are also applied in nonequilibrium (kinetics) studies. However, in this case, the choice of the analytical method will have an additional and important restriction, for it must consider the reaction rate. An instrumental technique suitable for determining the concentration of a given species under equilibrium conditions may be inappropriate for determining a fast concentration change of the same species.

Figure 15.1 The stable 2,2-diphenyl-1-picrylhydrazyl radical is used as a radical trap in a large number of kinetic studies.

<!-- image -->

The first example we address is taken from a paper by Bawn and Mellish, published some 50 years ago [323]. It reports kinetic studies of the thermal decomposition of benzoyl peroxide in several solvents (reaction 15.5), over the temperature range of 49-76 ◦ C. Here, we analyze the data obtained in toluene over the temperature range of 49.0-70.3 ◦ C.

<!-- formula-not-decoded -->

The method used by Bawn and Mellish relies on the presence of a 'radical trap' in the reaction mixture, that is, a compound that reacts very fast with the acyl radicals produced, thus preventing their recombination. This substance was the 'vivid colored' 2,2-diphenyl-1-picrylhydrazyl radical (figure 15.1). When these nitrogen-centered radicals, herein abbreviated by P, react with an acyl radical (reaction 15.6), the solution color change can be monitored with a spectrophotometer.

<!-- formula-not-decoded -->

A simple kinetic analysis of reactions 15.5 and 15.6 leads to equations 15.7 (where the stationary state assumption was applied to the acyl radical concentration) and 15.8.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Replacing [PhC(O)O] in equation 15.8 with the value given by equation 15.7, we obtain

<!-- formula-not-decoded -->

In their experiments, the authors used a large excess of the peroxide relative to P (see table 15.1). Therefore, the right-hand member of equation 15.9 was approximately constant, and k 1 could be determined by the slope of a linear plot between [P] and t at each temperature. As mentioned, the concentration of P at any instant could be monitored with a spectrophotometer by measuring

the absorbance of the reaction mixture. However, as stated after equation 15.8 (the Lambert-Beer law) in the preceding chapter, a more rigorous procedure for obtaining [P] would require that 'calibration' experiments be performed aiming to determine the change of ε l with temperature. It is not obvious from the original publication that this calibration was done, but it may be fair to accept that ε l remained nearly constant over the experimental temperature range.

Several possible complications in the kinetic analysis were pondered and ruled out by the authors. For instance, they demonstrated that the direct reaction of the peroxide with P did not occur because a change of concentration of this radical trap did not affect the reaction rate.

Table 15.1 shows the results obtained for k 1 at several temperatures, and figure 15.2 displays the Eyring and the Arrhenius plots (with k 1 in s -1 ) . These

Table 15.1 Rate constants ( k 1 ) of reaction 15.5 in toluene at several temperatures. The initial concentration of the radical trap was 5.83 × 10 -5 M. Data from [323].

|   t / ◦ C |   [PhC(O)OO(O)CPh]/mM |   k 1 × 10 2 / h - 1 |
|-----------|-----------------------|----------------------|
|      70.3 |                  3.92 |                4.02  |
|      70.3 |                  7.8  |                3.91  |
|      65.1 |                  7.97 |                2.05  |
|      60.2 |                  8.34 |                1.02  |
|      60.2 |                 17    |                1.02  |
|      55.1 |                 32.7  |                0.475 |
|      49   |                 33.8  |                0.221 |
|      49   |                 52.5  |                0.213 |

Figure 15.2 The Eyring (circles) and the Arrhenius (squares) plot for reaction 15.5.

<!-- image -->

plots lead to equations 15.10 and 15.11, respectively, where the uncertainty intervals are standard deviations multiplied by Student' s t factor for 95% probability and 6 degrees of freedom ( t = 2.447) [48]. The uncertainty in the data points is assumed to be less important than the scatter in the fit and is ignored here.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The quantities /Delta1 ‡ H o T and /Delta1 ‡ S o T at the mean temperature T = 333 K can now be calculated by comparing equations 15.10 and 15.1, as /Delta1 ‡ H o 333 = 123.6 ± 2.9 kJ mol -1 and /Delta1 ‡ S o 333 = [ ( 26.01 ± 1.31 ) -ln ( k B / h ) ] R = 18.7 ± 10.9 J K -1 mol -1 . The Arrhenius plot (equations 15.2 and 15.11) leads to A = 1.8 × 10 14 s -1 , E a = 126.3 ± 3.6 kJ mol -1 and, using equation 15.3, to /Delta1 ‡ H o 333 = 123.6 ± 3.6 kJ mol -1 .

Bawn and Mellish's experiments in other solvents (benzene, carbon tetrachloride, nitrobenzene, methyl acetate, and ethylacetate) produced similar values for the activation enthalpy, with an average E a = 123.8 kJ mol -1 [323], which corresponds to /Delta1 ‡ H o 333 = 121.0 kJ mol -1 .

How can we use the previous result to derive thermochemical data? The most correct procedure would probably the one described by Koenig, Hay, and Finke [324], briefly covered in section 3.2, which accounts for cage effects. However, this model involves parameters that are not available for the example under analysis. Therefore, we follow a cruder (but more typical) approach.

If we make the assumption that the reverse of reaction 15.5 is diffusioncontrolled and assume that the activation enthalpy for the acyl radicals recombination is ∼ 8 kJ mol -1 , the enthalpy of reaction 15.5 will be equal to ( 121 -8 ) = 113 kJ mol -1 . This conclusion helps us derive other useful data. Assuming that the thermal correction to 298.15 K is small and that the solvation enthalpies of the peroxide and the acyl radicals approximately cancel, we can accept that the enthalpy of reaction 15.5 in the gas phase is equal to 113 kJ mol -1 with an estimated uncertainty of, say, 15 kJ mol -1 . Therefore, as the standard enthalpy of formation of gaseous PhC(O)OO(O)CPh is available ( -271.7 ± 5.2 kJ mol -1 [59]), we can derive the standard enthalpy of formation of the acyl radical: /Delta1 f H o [PhC(O)O, g] ≈ -79 ± 8 kJ mol -1 . This value can finally be used, together with the standard enthalpy of formation of benzoic acid in the gas phase ( -294.0 ± 2.2 kJ mol -1 [59]), to obtain the O-H bond dissociation enthalpy in PhC(O)OH: DH o [PhC(O)O -H] = 433 ± 8 kJ mol -1 .

Asignificant contribution to the uncertainty interval assigned to the O-H bond dissociation enthalpy in benzoic acid comes from the estimate of the activation enthalpy for the radical recombination. The experimental determination of this quantity is not easy because diffusion-controlled recombination rate constants are very high (10 9 mol -1 dm 3 s -1 or larger) [180]. Therefore, most thermochemical data derived from kinetic experiments in solution rely on some similar assumptions.

A second problem that may affect the reliability of thermochemical kinetics data concerns the postulate of a mechanism for the reaction under investigation. In contrast to equilibrium studies, where the reactants and products can be unambiguously identified, the interpretation of kinetic data relies on a postulated set of elementary steps that are consistent with the observed rate law. While the experimental evidence for many reaction mechanisms is strong, many of these physical models have been refined throughout the years as a result of new experimental evidence, for example, the disclosure of new intermediates and the consideration of the cage effects already referred to. Although this may happen to the mechanism described in our following example, Brinkmann, Luinstra, and Saenz provided good evidence that the net reaction involving the two titanium complexes 1 and 6 shownin figure 15.3 (isomerization of the η 3 -coordinated allyl ligand to the trans -1-propenyl ligand) proceeds through the four intermediates displayed [325]. In their kinetic study, the authors used 1 H NMR to monitor the concentration changes of compounds 1 -6 in benzene over the temperature range of 10-45 ◦ C. The rate constants for both the forward and reverse processes were determined by a numerical analysis program and lead to a quantitative picture of the reaction energy profile. As an example, the Eyring plots for the first step,

Figure 15.3 Reaction mechanism proposed for the isomerization 1 /harpoonleftright 6 . Cp ∗ is pentamethylcyclopentadienyl. Adapted from [325].

<!-- image -->

involving the allyl ( 1 ) and the allene ( 2 ) complexes, are shown in figure 15.4 and correspond to equations 15.12 and 15.13,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Asusual, the uncertainty intervals are standard deviations multiplied by Student' s t factor for 95% probability and 3 and 2 degrees of freedom ( t = 3.182 and 4.303), respectively [48]. The reaction enthalpy and entropy at the average temperature ( ∼ 298 K) can therefore be determined for the case under discussion without any assumptions regarding the reverse reaction, as /Delta1 r H o = 4.4 ± 17.7 kJ mol -1 and /Delta1 r S o = 22.8 ± 59.0 J K -1 mol -1 . These error bars are overestimated because k 1 and k -1 are strongly correlated, that is, changing either one during the fitting procedure will require the other to change also. Therefore, a better procedure to extract the reaction enthalpy and entropy is to use the equilibrium constant data, given by K = k 1 / k -1. This van't Hoff plot leads to equation 15.14 and to /Delta1 r H o = 8.0 ± 3.3 kJ mol -1 and /Delta1 r S o = 35.3 ± 11.2 J K -1 mol -1 .

<!-- formula-not-decoded -->

It is interesting to note that the first step of the mechanism in figure 15.3 is entropy controlled. In other words, 2 is thermodynamically more stable than 1 despite the endothermicity of the process. The positive entropy change is consistent with the internal rotation increase when the η 4 -fulvene ring in 1 yields the η 5 -pentamethylcyclopentadienyl ligand. It is also interesting to note that the enthalpy of reaction 1 → 6 is -17 kJ mol -1 [325]. This value represents the difference betweenTiη 3 -C3H5 andTi-CHCHCH3 solution phase bond dissociation enthalpies.

Figure 15.4 Eyring plots for reaction 1 /harpoonleftright 2 (see figure 15.3) in the forward (squares) and reverse (circles) directions.

<!-- image -->

The third and last example in this chapter illustrates a case where kinetic data were used to derive relative enthalpies for a series of similar reactions. Consider the ligand (phosphine) exchange reaction 15.15 (see figure 14.5 for the structure of the complex),

<!-- formula-not-decoded -->

Using 31 PNMRasanalyticaltechnique, Bryndza et al. investigated the kinetics of this reaction in benzene for a variety of ligands X (see figure 15.5) [326,327].Their experimentsdemonstratedthatthephosphineexchangeproceedsbyadissociative pathway, that is,

<!-- formula-not-decoded -->

The rate constants of this reaction were determined by the authors at several temperatures, and the activation enthalpies ( /Delta1 ‡ H o 1 ) were derived from Eyring plots. To estimate the reaction enthalpies through equation 15.4, Bryndza et al. made the reasonable assumption that the reverse activation enthalpies ( /Delta1 ‡ H o -1 ) are not only small (as expected for the recombination of PMe3 with the 16-electron unsaturated complex) but also predicted to be nearly constant for the different ligands X. Therefore, whereas the assumption /Delta1 r H o ≈ /Delta1 ‡ H o may lead to inaccurate /Delta1 r H o values, the trend observed in figure 15.5 will probably hold for the reaction enthalpies. Note that these reaction enthalpies can be identified with the solution phase bond dissociation enthalpies DH o sln [Ru(Cp ∗ )(PMe3 ) (X) -PMe3] and that the values in figure 15.5 span almost 80 kJ mol -1 . As the authors point out, the Ru-PMe3 bond dissociation enthalpy decreases for bulky substituents,

Figure 15.5 Activation enthalpy values of reaction 15.16 for different X. Data from [327]

<!-- image -->

for example, DH o sln [Ru(Cp ∗ )(PMe3 ) (X)-PMe3] for X = MeandX = CH2SiMe3 differ by some 25 kJ mol -1 . It is even possible that this difference is actually a lower limit because, as also remarked by Bryndza et al., the recombination barrier ( /Delta1 ‡ H o -1 ) 'is likely to be larger for adding phosphine to the sterically congested center' [327].

## Electrochemical Measurements

Electrochemical measurements have been playing an increasingly important role in the thermodynamic study of reactions in solution, not only because they provide data that are difficult (or even impossible) to obtain by other methods [328] but also because these data can often be compared with the values determined for the analogous gas-phase reactions, thus yielding information on solvation energetics.

Figure 16.1 was adapted from a scheme proposed by Griller et al. [329]. It summarizes the thermochemical information on the R-X bond that can be probed by electrochemical methods. The vertical arrows represent homolytic cleavages, and the horizontal arrows depict reduction or oxidation potentials. The authors have appropriately called the scheme in figure 16.1 a 'mnemonic,' rather than a 'thermochemical cycle,' because not all arrow combinations define thermochemical cycles. This can be made more clear by inspecting figure 16.2, where true thermochemical cycles are defined. For example, the enthalpy of reaction 7 is not the sum of the enthalpies of reactions 1 and 4 (as might be suggested by figure 16.1) but their sum minus the enthalpy of reaction 12 (see figure 16.2). In fact, true thermochemical cycles in figure 16.1 can only be defined by considering parallelograms confined either to the upper or the lower part of the mnemonic. For instance, the enthalpy of reaction 7 is given by the enthalpy of reaction 4 plus the enthalpy of reaction 9 minus the enthalpy of reaction 3, but it is not equal to the enthalpy of reaction 6 minus the enthalpy of reaction 11 plus the enthalpy of reaction 10. Also, the enthalpy of reaction 1 (the homolytic dissociation of the R-X bond in the neutral molecule RX) can be given by the sum of the enthalpies or reaction 5 and 11 minus the enthalpy of reaction 3 or, for example, by the sum of the enthalpies of reactions 7 and 12 minus the enthalpy of reaction 4.

The attractive feature of the mnemonic in figure 16.1 (or the thermochemical cycles in figure 16.2) is that it depicts the seven possible R-X cleavage reactions of RX, RX -, and RX + , as well as their relationships. Now suppose that we want to know the energetics of all those processes. What experimental techniques should we use and how many parameters (e.g., reaction enthalpies or Gibbs energies) should we determine to assign values to all the remaining reactions? The answer to the first question justifies the statement made at the beginning of this chapter. With exception of reaction 1 (whose thermochemistry could be investigated by techniques such as photoacoustic calorimetry or kinetic methods) and reactions 8 and 9 (which could be studied, for instance, by equilibrium methods [330]; see

Figure 16.2 Thermochemical cycles involving the heterolytic and homolytic cleavages of the R-X bond, and reduction or oxidation processes. The reaction numbers are the same as in figure 16.1.

<!-- image -->

chapter 14), the energetics of the remaining processes can only be probed by using electrochemical techniques. As to the number of independent measurements we need to quantify the energetics of all the thirteen processes, the answer was given by Griller et al. [329]: The only measurements required are indicated in figure 16.1 by reaction 1 and by the horizontal arrows-that is, we only need to

knowtheenergetics of the R-X bond in the neutral molecule RX and six reduction potentials . In other words, to have the complete thermochemical information on the thirteen reactions in figures 16.1 or 16.2, the values of at least seven quantities are required.

As pointed out by Wayner and Parker [328], thermochemical cycles involving electrode potentials have been used by several groups to determine heterolytic or homolytic bond dissociation enthalpies or Gibbs energies in solution. Those cycles reported in the literature are subsets of the general cycles of figures 16.1 or 16.2 and their application was fostered by the publications by Breslow and co-workers, starting in the late 1960s, which included, for example, estimates of the p K a values of weak carbon acids based on reduction potential measurements [331]. Recall that the p K a of an acid RH is equal to the Gibbs energy of reaction 9 in figure 16.1 (for X = H) divided by 2.303 RT , that is, p K a = -log K a , where K a is the equilibrium constant of that reaction [180].

Several electrochemical techniques may yield the reduction or oxidation potentials displayed in figure 16.1 [332-334]. In this chapter, we examine and illustrate the application of two of those techniques: cyclic voltammetry and photomodulation voltammetry. Both (particularly the former) have provided significant contributions to the thermochemical database. But before we do that, let us recall some basic ideas that link electrochemistry with thermodynamics. More in-depth views of this relationship are presented in some general physicalchemistry and thermodynamics textbooks [180,316]. A detailed discussion of theory and applications of electrochemistry may be found in more specialized works [332-334].

## 16.1 ELECTROCHEMISTRY AND THERMODYNAMICS

An electrical potential difference between the electrodes of an electrochemical cell (called the cell potential ) causes a flow of electrons in the circuit that connects those electrodes and therefore produces electrical work. If the cell operates under reversible conditions and at constant composition, the work produced reaches a maximum value and, at constant temperature and pressure, can be identified with the Gibbs energy change of the net chemical process that occurs at the electrodes [180,316]. This is only achieved when the cell potential is balanced by the potential of an external source, so that the net current is zero. The value of this potential is known as the zero-current cell potential or the electromotive force (emf) of the cell, and it is represented by E . The relationship between E and the reaction Gibbs energy is given by

<!-- formula-not-decoded -->

where n is the number of electrons transferred according to the half-cell reactions (or simply half-reactions ; see following discussion), and F is the Faraday constant (the product of the elementary charge by the Avogadro constant; see appendix A).

Now consider that reaction 16.2 represents the half-reaction that occurs at the cathode and the reverse of reaction 16.3 is the half-reaction that occurs at

the anode (Ox1, Ox2 and Red1, Red2 are the oxidized and the reduced forms of species 1 and 2 and form two redox couples , abbreviated by Ox1/Red1 and Ox2/Red2). Both processes are written as reductions, according to the accepted convention [180]. Reaction 16.4 is the cell reaction.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The Gibbs energy of reaction 16.4 is given by

<!-- formula-not-decoded -->

where a i are the activities of the reactants and products and /Delta1 r G o is the standard Gibbs energy change, that is, the Gibbs energy of the reaction when a i = 1 for all the species. Because /Delta1 r G can be expressed in terms of the cell potential (equation 16.1), we obtain the Nernst equation:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

representing the standard cell potential, that is, the zero-current cell potential when all reactants and products are in their standard states ( a i = 1 ) . Note that E o may be given as the difference between the standard electrode potential of the half-reaction that occurs at the cathode (reduction) and the standard electrode potential of the half-reaction that occurs at the anode (oxidation):

<!-- formula-not-decoded -->

Introducing this result in equation 16.7, we obtain

<!-- formula-not-decoded -->

Hence, for the cathode (reduction),

<!-- formula-not-decoded -->

and for the anode (oxidation),

<!-- formula-not-decoded -->

Under equilibrium conditions, E = 0 in equation 16.6, and the activity ratio in the second member is equal to the equilibrium constant K . Therefore,

<!-- formula-not-decoded -->

with

The equilibrium constant (or the standard Gibbs energy) of reaction 16.4 can thus be determined by measuring E o . However, this does not afford the target quantities, that is, the individual standard redox potentials of species 1 and 2, E o ( Ox1 / Red1 ) and E o ( Ox2 / Red2 ) . In fact, it is impossible to measure electrode potentials of half-reactions-we can only obtain differences between these potentials. The practical solution of the problem consists in assigning an arbitrary value of zero (at any temperature) to the standard electrode potential of half-reaction 16.13, which represents the standard (or normal ) hydrogen electrode (SHE), and using this reaction in place of 16.3. Recall that the word standard implies unit activities for aqueous H + and for gaseous H2 (i.e., p H2 = 1 bar).

<!-- formula-not-decoded -->

Reaction 16.4, can thus be written as ( n = 1 )

<!-- formula-not-decoded -->

anda relative value of the standard reduction potential of species 1 may be derived from the measurement of the standard cell potential.

Because the SHE anchors the potentials tabulated for all the remaining electrodes, it is the most important reference electrode. Although it is not difficult to build [332], its use is not always convenient. For instance, if we are interested in the reduction potential of species 1 in a solvent other than water (as in reaction 16.14), we will wish to use a reference electrode whose potential is accurately known in that solvent (see following discussion).

## 16.2 CYCLIC VOLTAMMETRY

Voltammetry is a technique by means of which the electrical current is measured as a function of the potential applied to an electrode (called the workingelectrode ). This potential may be varied during an experiment, and the shape of its plot against time (the potential waveform ) characterizes each particular type of voltammetry [332-334]. For instance, the potential may be subject to a fast linear increase with time (linear sweep voltammetry) or may grow by steps or pulses (e.g., normal pulse voltammetry). Here, we concentrate on a waveform that is shaped as shown in figure 16.3 and is the basis of cyclic voltammetry (CV). The potential starts at a preset value E i and increases linearly with time, at a given scan rate v (usually up to 100 V s -1 , but sometimes much higher), until it reaches the switching potential , E S. From here on the potential decreases at the same rate v , until it returns to E i. As indicated in figure 16.3 by the dashed line, the cycle can be repeated several times.

Before discussing the voltammogram obtained with the triangular waveform of figure 16.3, which is simply a plot of the observed current intensity versus the applied potential, it is useful to describe some experimental details of a cyclic voltammetry experiment [335-337] and to recall some basic theory of dynamic electrochemistry [180,332]. A typical cell (figure 16.4) consists of

<!-- image -->

three electrodes-a working electrode, a reference electrode, and an auxiliary (or counter ) electrode. As mentioned, the half-reaction to be studied takes place at the working electrode (e.g., a platinum or gold electrode) whose potential is measured relative to the potential of the reference electrode. That is often a saturated calomel or a silver/silver halide electrode, which can be isolated from the solution by a salt bridge. The role of the auxiliary electrode (e.g., a platinum wire or foil) is to prevent current from flowing through the reference electrode, which would polarize it (i.e., change its potential).

The simple electrochemical cell for CV experiments, outlined in figure 16.4, is used by Tilset' s group [335]. It is a modified test tube with a Teflon stopper in which five holes were drilled: three for the electrodes, one for an argon inlet tube, and another for venting the inert gas. As an electrode potential varies with the temperature, the cell should be thermostated for high-accuracy work, but usually the errors caused by small temperature changes are negligible compared with the uncertainties of the experimental redox potential values. The argon (or nitrogen) flow removes the dissolved oxygen from the liquid and maintains an inert atmosphere in the cell throughout the experiment. This is very important for several reasons [332]: (1) the reduction of O2, which occurs at a potential between 0.05 V

and -0.9 V relative to the saturated calomel electrode (depending on the solvent and the working electrode), may contribute to the measured current; (2) the oxygen may oxidize the electrode surface; and (3) the oxygen may react (or produce species that do) with species of the half-reaction under investigation.

Adiagram of the remaining hardware required for a CV set-up is displayed in figure 16.5. It consists of a waveform generator that produces the excitation signal (figure 16.3) and drives a potentiostat. This applies the potential waveform to the working electrode, relative to the reference electrode, and allows the measurement of the electrical current that flows between the working and the auxiliary electrodes. The output of the potentiostat can be sent to an oscilloscope (or an XY recorder). The oscilloscope and the waveform generator can be interfaced to a computer to control the experiment and for data acquisition and handling.

Let us now suppose that the waveform of figure 16.3 is applied to study the reversible oxidation of a species R -to R in a given solvent. The reaction occurs at the working electrode (anode), and E o ( R / R -) is the standard potential of the R/R -couple. Because the standard potential of the reference electrode in our cell is known accurately relative to the standard potential of the SHE ( E o = 0 by definition), we can write the cell reaction and the Nernst equation as

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and

Note that we had to multiply the cell potential by -1 because the net equilibrium 16.15 does not follow the accepted convention, that is, the SHE is not the anode. Equation 16.16 becomes

<!-- formula-not-decoded -->

showing that the ratio between the activities of R and R -will change according to the applied potential E . However, the electrical current measured in our experiment will be determined by concentrations of those species, rather than by their

Figure 16.5 Typical instrumentation for cyclic voltammetry. Adapted from [337].

<!-- image -->

activities (see following discussion). Therefore, it is useful to rewrite equation 16.17 as

<!-- formula-not-decoded -->

where γ represents an activity coefficient (see section 2.9; note that now these coefficients are expressed in dm 3 mol -1 rather than kg mol -1 ) .

It is important to stress that the activity coefficients (and the concentrations) in equation 16.18 refer to the species close to the surface of the electrode, and so can be very different from the values in the bulk solution. This is portrayed in figure 16.6, which displays the Stern model of the double layer [332]. One (positive) layer is formed by the charges at the surface of the electrode; the other layer, called the outer Helmholtz plane (OHP), is created by the solvated ions with negative charge. Beyond the OHP , the concentration of anions decreases until it reaches the bulk value. Although more sophisticated double-layer models have been proposed [332], it is apparent from figure 16.6 that the local environment of the species that are close to the electrode is distinct from that in the bulk solution. Therefore, the activity coefficients are also different. As these quantities are not

Figure 16.6 The Stern model of the double layer. The outer Helmholtz plane (OHP) and the width of the diffusion layer ( δ ) are indicated. The shaded circles represent solvent molecules. The drawing is not to scale: The width of the diffusion layer is several orders of magnitude larger than molecular sizes.

<!-- image -->

available, the usual practice is to absorb the last term of equation 16.18 into E o ( R / R -) :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

is the so-called formal potential . Note that in contrast to the standard potential, the formal potential is not constant for a given couple. However, the activity coefficient ratio can be made approximately invariable by introducing into the cell a supporting electrolyte , that is, a solution containing a high concentration of inert ions. This concentration is at least two orders of magnitude higher than that of the species under investigation [332] and ensures that the local environment of this species is similar throughout the cell.

The formal potential is the quantity determined from the analysis of a voltammogram, but the true thermodynamic quantity (the standard potential) can be derived by obtaining E o ′ ( R / R -) for different bulk concentrations ( c ) and extrapolating to c = 0 (unit activity coefficients). The procedure is, however, seldom adopted; in practice, E o ′ ( R / R -) is identified with the standard potential. Thelowertheconcentrationoftheelectroactive species, the better the assumption.

Equation 16.19 is essential for relating the shape of the response signal (figure 16.7) to the waveform in figure 16.3. Y et it is not enough. We also need to consider how the current is produced, and this is determined by the kinetics of the electrode reactions [332].

<!-- image -->

E

/ V

Figure 16.7 A reversible cyclic voltammogram obtained with the waveform shown in figure 16.3.

where

The current intensity depends on the rate of the electron transfer reaction at the electrode and on the rate of mass transport of the electroactive species from the bulk solution to the electrode surface. In a reversible process, the former is much higher than the latter, that is, the current will be determined by the mass transport, and the nernstian equilibrium will be established throughout the experiment. Although several types of mass transport are possible in an electrochemical experiment, viz . diffusion, convection, and electromigration, the experiments are designed so that only diffusion is relevant. Convection is eliminated by not stirring the solution, by avoiding temperature gradients, and by limiting the time of the experiments. Electromigration of the electroactive species is substantially reduced by the supporting electrolyte mentioned above, as the effect of the electrode' s potential is dissipated by all the ions in solution [338]. The stationary planar electrodes adopted in cyclic voltammetry experiments usually have a much larger diameter than the width of the diffusion layer, ensuring that the transport of the electroactive species occurs by linear diffusion [335]. The width of the diffusion layer ( δ in figure 16.6), which increases with time, is defined as the distance from the electrode surface to the plane where the concentration of the electroactive species reaches the bulk concentration (see figure 16.6).

If only linear diffusion is the operating mass transport process, it has been shown that the current ( i ) in a planar electrode is related to the concentration ( c ) gradient at the surface of the electrode ( x = 0 ) by [332]

<!-- formula-not-decoded -->

Here, n is the number of electrons of the half-reaction, F is the Faraday constant, A is the electrode area, D is the diffusion coefficient of the electroactive species, and x is the distance from the electrode.

A qualitative understanding of the voltammogram in figure 16.7 can be achieved with equations 16.19 and 16.21. During the first part of the curve (a) no current is detected because the applied potential ( E ) is much smaller than E o ′ ( R / R -) , that is, [ R -] /greatermuch [ R ] or [ R ] ≈ 0. In other words, the concentrations of R -at the electrode surface and in the bulk solution are equal. When E increases, the concentration of R -at the surface decreases and an anodic current starts to develop (b).This current rises sharply (c) with the applied potential because R -is rapidly consumed at the surface and there is an increasing concentration gradient in the diffusion layer (equation 16.21). The fast consumption of R -and the high slope of part c reflect the logarithmic variation of E with the concentration of this species (equation 16.19), that is, a small potential variation leads to a large concentration change. As the current moves toward a maximum (d), it passes through the potential value for which E = E o ′ ( R / R -) . It is shown by equation 16.19 that this occurs when [ R -] = [ R ] . At a given value of the applied potential ( E p,a ) , there is a a substantial depletion of R -at the surface, and the gradient ( ∂ [ R -] /∂ x ) x = 0 reaches a maximum, corresponding to the anodic current peak value ( i p,a ) . From here on, the rather high (compared to E o ′ ( R / R -)) and rising potential implies that not only is the concentration of R -close to the electrode

essentially zero but also that this species is being increasingly exhausted in the expanding diffusion layer (recall that δ increases with time). This results in a decreasing gradient ( ∂ [ R -] /∂ x ) x = 0 and a decreasing current (e). In other words, the mass transport to the electrode surface becomes less efficient in this region of the voltammogram, and the current decreases. At the preset switching potential (f ) the potential starts to decrease, and the cathodic wave of the voltammogram begins. The shape of this wave, which corresponds to the reduction of R to R -, is explained by considerations similar to those used for the anodic wave.

Some of the parameters that can be extracted from the cyclic voltammogram, all shown in figure 16.7, are the anodic and cathodic peak currents ( i p,a and i p,c ) , the anodic and cathodic peak potentials ( E p,a and E p,c ) , the anodic and cathodic half-peak potentials ( E p / 2,aand E p / 2,c ) , and the half-wave potential ( E 1 / 2 ) . For our purposes, E 1 / 2 is the most important. It is defined as the average of E p,a and E p,c ,

<!-- formula-not-decoded -->

and is related to the formal potential by [332]

<!-- formula-not-decoded -->

where D R and D R -are the diffusion coefficients of R and R -. Because D R ≈ D R -, E 1 / 2 is usually a very good approximation of E o ′ ( R / R -) .

Further details and a more quantitative discussion of cyclic voltammetry can be found in more specialized books [332-334]. Here, before proceeding to a numerical example, we summarize the reversibility criteria in cyclic voltammtery and point out some factors that may lead to unreliable values of E o ′ ( R / R -) [335].

First the reversibility criteria [332]: (1)The anodic and cathodic peak potentials must be independent of the scan rate ν ; (2) the difference between the anodic and cathodic peak potentials must be such that ∣ ∣ E p,a -E p,c ∣ ∣ = 59 mV at 298.15 K and for n = 1; (3) the difference between the anodic or cathodic peak potential and the corresponding half-peak potential must be 57 mV at 298.15 K and for n = 1, for example, ∣ ∣ E p,a -E p / 2,a ∣ ∣ = 57 mV; (4) the anodic and cathodic peak currents must be equal, that is, ∣ ∣ i p,a / i p,c ∣ ∣ = 1; and (5) the peak currents must be proportional to the square root of the scan rate, i p ∝ ν 1 / 2 .

As stated by Tilset, 'It would indeed be nice if all cyclic voltammograms adhered to the criteria for nernstian waves . . . . However, voltammograms may appear dramatically different from the ideal one . . . due to a wide variety of reasons' [335]. The main factors that complicate the shape and the analysis of a voltammogram were discussed by the same author and include (1) nonlinear diffusion when the electrode diameter is not much larger than the width of the diffusion layer; (2) nonfaradaic current, that is, current that only charges the double layer electrical capacitor and does not yield the half-reaction under study; (3) the so-called iR or ohmic drop , which is caused by the electrical resistance of the solution and leads to a difference between the value of potential applied by the potentiostat and the potential actually sensed by the working electrode;

(4) any chemical reaction that consumes the product of the half-reaction, which may cause a kinetic potential shift ; and (5) slow heterogeneous electron transfer, which hinders the equilibrium described by the Nernst equation.

Some of these complicating factors may be minimized by carefully choosing the experimental or instrumental conditions. For instance, the ohmic drop is lowered by reducing the distance between the reference electrode and the working electrode, by using a better-conducting supporting electrolyte, and by decreasing the scan rate or the electrode area. It may also be minimized by compensating electronic circuitry. Other factors may be more difficult to avoid. If, in our example, there is a very fast chemical reaction that consumes R produced at the electrode (the so-called EC mechanism ; 'E' for electrochemical followed by 'C' for chemical), no peak will appear in the cathodic scan simply because there is no R available for reduction. By increasing the scan rate it may be possible to observe both the anodic and the cathodic waves (i.e., the voltammogram approaches reversibility), but the anodic peak will be shifted to higher values (see following discussion). With a slow scan rate, the anodic peak potential would therefore represent an lower limit of the true (reversible) value. This lower limit can be understood on thermodynamic grounds (equation 16.19): The follow-up reaction consumes R very fast, so that the electrode reaction is driven to the right and a smaller potential is required to oxidize R -and reach equilibrium concentrations.

Despite the problems that can afflict experimental cyclic voltammograms, when the method for deriving standard redox potentials is used with caution it affords data that may be accurate within a few tens of mV (10 mV corresponds to about 1 kJ mol -1 ) , as remarked byTilset [335]. Kinetic shifts are usually the most important error source: The deviation ( /Delta1 E p ) of the experimental peak potential from the reversible value can be quite large. However, it is possible to estimate /Delta1 E p if the rate constant of the chemical reaction is available. For instance, in the case of a second order reaction (e.g., a radical dimerization) with a rate constant k , the value of /Delta1 E p at 298.15 K is given by equation 16.24 [328,339]:

<!-- formula-not-decoded -->

With k = 10 10 mol -1 dm 3 s -1 , a scan rate ν = 0.1 V s -1 , and [ R ] = 10 -3 mol dm -3 , it is concluded that the observed anodic peak potential will be 128 mV lower (corresponding to about 12 kJ mol -1 ) than the reversible value. The kinetic shift for a first order reaction is larger (equation 16.25); /Delta1 E p = 287 mV (28 kJ mol -1 ) at 298.15 K, when k = 10 10 s -1 and ν = 0.1 V s -1 [328].

<!-- formula-not-decoded -->

The analysis of a cyclic voltammogram is simplified today, thanks to the availability of commercial software that produces simulated voltammograms [333,335]. Derivative cyclic voltammetry (DCV) is another improvement of the technique, where plots of di / dE versus E are obtained (i.e., the derivative of the

curve in figure 16.7) [340]. DCV presents several advantages over CV . For thermochemical purposes, only one is mentioned here: The derivative plots allow a more accurate assignment of the peak potentials.

As remarked before, reduction potential values have been used abundantly to discuss the energetics of the reactions displayed in figures 16.1 or 16.2. One of the most common situations concerns the determination of the homolytic R-H bond dissociation enthalpy, R being an organic or an organometallic moiety. Let us assume that E o ′ ( R / R -) has been determined from a CV experiment and identified with the standard reduction potential of R, E o ( R / R -) . We also suppose that the p K a of RH (which we now call p K RH ) is known. Equation 16.26, which shows the relationship between the R-H bond dissociation Gibbs energy and those two quantities, can be inferred from figure 16.8. Note that we have used the subscripts SHE(aq) and S to stress that the potentials are relative to the standard aqueous hydrogen electrode, but they refer to the half-reaction in a given solvent S.

<!-- formula-not-decoded -->

The application of equation 16.26 requires an estimate of the reduction potential of H + in the same solvent in which the experiments were carried out. This subject was discussed by Parker, and values of E o SHE ( aq ) ( H + / H ) S in several solvents were reported [341]. Although the details of his discussion will not be repeated here, it is simple to conclude (figure 16.9 and equation 16.27) that E o SHE ( aq ) ( H + / H ) S can be calculated from the thermodynamic parameters of the gaseous hydrogen atom (the standard Gibbs energy of formation and the standard Gibbs energy of solvation in the solvent S) and of the proton (the standard Gibbs energy of transfer from S to water).

<!-- formula-not-decoded -->

| RH(sln)     |     | R - (sln) + H + (sln)   | 2.303 RT p K RH          |
|-------------|-----|-------------------------|--------------------------|
| R - (sln)   |     | R(sln) + e -            | FE o SHE(aq) (R/R - ) S  |
| H + (sln) + | e - | H(sln)                  | -FE o SHE(aq) (H + /H) S |
| RH(sln)     |     | R(sln) + H(sln)         | DG o (R-H)               |

sln (R-H)

Figure 16.8 Thermochemical cycle showing how standard electrode potentials and p K a are related to a bond dissociation Gibbs energy.

<!-- formula-not-decoded -->

Figure 16.9 Thermochemical cycle that leads to equation 16.27.

Nowthe R-H bond dissociation enthalpy in the solvent S is related to the R-H bond dissociation Gibbs energy by equation 16.28.

<!-- formula-not-decoded -->

Because and

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

it is simple to derive equation 16.31, after some manipulation of equations 16.26, 16.27, and 16.28.

<!-- formula-not-decoded -->

Finally, the R-H bond dissociation enthalpy in the gas phase can be obtained by using the general thermochemical cycle shown in figure 5.1 (R = A and H = B), which includes the solvation enthalpies of RH and R:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The calculation of the solution and gas-phase R-H bond dissociation enthalpies through equations 16.31 and 16.32 requires several values besides the experimental data for p K RH and E o SHE ( aq ) ( R / R -) S. Some of those values (the standard enthalpy of formation of H and the standard entropies of gaseous R, RH, and H2 ) are readily available in the literature or can be accurately calculated using statistical mechanics. However, some of the remaining terms, such as the solution entropies and the solvation enthalpies of R and H, are usually unknown and therefore require some estimates and some simplifying assumptions. The assumptions are /Delta1 sln S o ( R, g ) ≈ /Delta1 sln S o ( RH,g ) and /Delta1 sln H o ( R, g ) ≈ /Delta1 sln H o ( RH,g ) , and the estimates refer to /Delta1 tr G o ( H + , S → aq ) and /Delta1 sln H o ( H, g ) . Values of the Gibbs energy of proton transfer are available in the literature [341], and the enthalpy of solvation of the hydrogen atom has been estimated as 5 kJ mol -1 in most organic solvents and -4 kJ mol -1 in water (see section 5.1).

For many species and solvents these assumptions are thought to be sensible, whereas in some cases they may lead to significant errors (see following discussion). Nevertheless, this was the approach used by Bordwell and co-workers [342]. They combined most of the terms of equation 16.32 in a single constant, C , which was empirically adjusted to give better agreement with gas-phase data [343-345]. Equation 16.33 illustrates this procedure; C = 306.7 kJ mol -1 is valid for S = dimethylsulfoxide (DMSO) and when the oxidation potential of R -is anchored on the ferrocenium/ferrocene Fc + /Fc) couple instead of the SHE in water.

<!-- formula-not-decoded -->

The use of the ferrocenium/ferrocene couple as a reference deserves some comment. As stated before, electrochemists prefer to use a reference electrode other than the SHE. To check the standard potential of the chosen reference electrode under the experimental conditions it is common (and advocated [335]) to derive the Fc + /Fc half-wave potential and compare it with literature values (the ferrocene voltammogram is reversible). Then, if necessary, the experimental values of the half-wave potential ( E 1 / 2) for the system under investigation can then be corrected. Alternatively, ferrocene is added to the cell containing the sample and used as an internal standard to 'calibrate' the potential scale. In the CV work by Bordwell's group, E 1 / 2 = 0.875 V for Fc + /Fc was measured in DMSO with 0.1 mol dm -3 of Et4NBF4 as the support electrolyte [343]. The reference electrode used in the experiments was AgI/Ag,I -, whose standard potential in DMSOrelative to SHE in water is -0.125V . Therefore, as can be concluded from figure 16.10 or from equations 16.34 and 16.35, the experimental E 1 / 2 value for Fc + /Fc relative to the SHE in water (identified with E o SHE ( aq ) ( Fc + / Fc ) DMSO ) is 0.875 -0.125 = 0.750 V . The electrode potential value to use in equation 16.33 should thus be obtained by subtracting this amount from the half-wave potential of the system under study (relative to the SHE,aq) or alternatively by subtracting 0.875 V from the measured half-wave potential (which is relative to AgI/Ag,I -) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 16.10 Diagram showing how values of the standard electrode potential of the couple R/R -referenced to several standard electrode potentials (SHE, AgI/Ag,I -, and ferrocenium/ferrocene) are derived. See equations 16.34 and 16.35.

<!-- image -->

Bordwell and colleagues have been the major users of the electrochemical (CV) methodology to derive homolytic bond dissociation enthalpies in organic compounds, and Tilset and Parker pioneered the method for organotransition metal hydrides [328]. According to Bordwell and Liu [345], the results are, with few exceptions, accurate to within ± 13 kJ mol -1 . In fact, the agreement with other literature results is in general better than anticipated, considering that most of the reported standard potentials of the R/R -couples were identified with the anodic peak potentials assigned from irreversible voltammograms (see, e.g., [345] and [346]). As already stated and also remarked by several authors, the irreversibility of the oxidation of R -can be the major error source of the electrochemical method [219,328]. Take, for example, the couple PhO/PhO -. The measurements are complicated by the short lifetime of the phenoxy radical, by the fact that PhO is more easily oxidized than the phenolate, and also by secondary reactions, such as the dimerization of the radical [347] (this is, by the way, the most common fate of the free radicals formed on oxidation or reduction of ions in solution [328]). As shown

by equation 16.24, the dimerization reaction leads to a kinetic shift of the measured anodic peak potential, which is used to evaluate E o Fc + / Fc ( PhO / PhO -) DMSO. Nevertheless, because equation 16.33 is 'calibrated' against gas-phase data obtained with other methods, the empirical constant C must include some 'average kinetic shift correction' of the peak potential. Actually, the equation leads to a DH o ( PhO -H ) result that is even some 7 kJ mol -1 greater than the recommended value; by using the most recent data for p K PhOH (18.0) and E o Fc + / Fc ( PhO / PhO -) DMSO ( -0.325 V) [348], we obtain DH o ( PhO -H ) = 378.1 kJ mol -1 at 298.15 K, compared with 371.3 ± 2.3 kJ mol -1 [349]. Note, however, that when the oxidation of a species R -is reversible, the kinetic shift does not occur, and the bond dissociation enthalpies derived with equation 16.33 will be too large.

The different solvation energetics of R and R -will also lead to errors in the bond dissociation enthalpies calculated with equation 16.33. For instance, in the case of phenol, whose interactions with proton-acceptor solvents (like DMSO) are obviously stronger than those for the phenoxy radical, a negative correction should be applied to the value of DH o ( PhO -H ) calculated from equation 16.33 (see also equation 16.32). It is probably unwise to ascribe the 7 kJ mol -1 difference between the 'electrochemical' and the recommended DH o ( PhO -H ) value to the differential solvation effects. Although this discrepancy is in the correct direction, it lies within the suggested uncertainty of the method.

In conclusion, therefore, a judicious use of CV methodology may lead to absolute thermodynamic data that are accurate to ca. ± 15 kJ mol -1 . Relative values (i.e., differences between bond dissociation enthalpies in similar compounds) can be more reliable, but the approximations described suggest that some caution be exercised when using the results to draw conclusions that rely on small differences between bond dissociation enthalpies. This is the case, for example, for ring substituent effects on the O-H bond dissociation enthalpies in substituted phenols [346,349].

## 16.3 PHOTOMODULATION VOLTAMMETRY

As already stated, other electrochemical techniques have been used to derive thermodynamic data, some of them considered to yield more reliable (reversible) redox potentials than cyclic voltammetry. This is the case, for instance, of second harmonic alternating current voltammetry (SHACV) [219,333]. Savéant and co-workers [339], however, concluded that systems that appear irreversible in slow-scan CV are also irreversible in SHACV experiments. We do not dwell on these matters, important as they are. Instead, we concentrate on a different methodology to obtain redox potentials, which was developed by Wayner and colleagues [350-352].

The conception and building of a photomodulation voltammetry (PV) apparatus was stimulated by the need to measure redox potentials of short-lived

species, like free radicals, and derive thermochemical data for those species. Unlike the CV approach, where the electroactive species are the anions R -, in photomodulation voltammetry the electroactive species can be the neutral radicals themselves.

Oneof the methods used in PV to produce the free radicals is similar to the one illustrated in chapter 13, that is, when a substance like ditert -butylperoxide is irradiated with energy of a suitable wavelength, the O-O bond is cleaved and two tert -butoxyl radicals are generated. These radicals can then abstract a hydrogen atom from another molecule RH, yielding the radical R.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

An alternative method used to produce the radicals is through the photodecomposition of the ketone RC(O)R:

<!-- formula-not-decoded -->

The main feature of a PV apparatus (figure 16.11) is a pulsed radiation beam obtained by interposing a chopper between the lamp (a 1000 W Hg/Xe arc lamp) and the three-electrode electrochemical cell (provided with quartz windows). Only a small concentration of radicals is produced. If a continuous radiation source is used, the output signal of the potentiostat due to the oxidation of R would be difficult or even impossible to discern from other phenomena in the cell. Pulsing the beam ensures that the radical concentration oscillates at the same frequency as the chopper, allowing the small oscillating component of the signal to be amplified selectively. The amplification is made by a phase-sensitive detector, which uses the chopping frequency (29-200 Hz) as a reference. The signal-tonoise enhancement may reach 10 4 . According to Wayner and co-workers, the system can detect concentrations of R as low as 10 -8 mol dm -3 and average lifetimes as short as 1 ms [351].

A source of problems in PV experiments is that the signals of other species associated with the production of R, including that of the precursor, may interfere

Figure 16.11 Diagram of a photomodulation voltammetry apparatus. Adapted from [351].

<!-- image -->

with the signal to be recorded because their concentrations also fluctuate with the same frequency. As remarked by Wayner and co-workers, the issue is usually taken care of by monitoring R in applied potential regions where the other species are not affected [351].

In a typical experiment, the radicals R are produced as described in acetonitrile containing an appropriate electrolyte (e.g., 0.1 mol dm -3 of tetrabutylammonium perchlorate). The sample solution is kept flowing (2-3 cm 3 min -1 ) through the 500 µ L cell to avoid substrate depletion or product accumulation. The potential of a gold minigrid working electrode is then scanned at a rate of 10-20 mV s -1 (against a saturated calomel electrode), until the reduction or oxidation of the radicals is observed.At this point, the resulting oscillating (ac) current is amplified and recorded or the signal fed into a computer. Further details of the procedure and optimization of the experimental parameters can be found in the original literature [351].

An example of a voltamogram obtained with the PV apparatus is displayed in figure 16.12. It shows two waves, corresponding to the oxidation and reduction of R. The shape of these waves can be easily understood qualitatively on the basis of the discussion in section 16.2. Take, for instance, the anodic wave, where R is oxidized to R + . As explained before, when the increasing potential reaches a given value, the current starts to increase. However, after a sharp rise (note the direction of the scales in figure 16.12), the current reaches a plateau instead of going through a maximum as in figure 16.7.To account for this different behavior, we have to recall two details. The first one is that in PV the potential applied to the working electrode varies linearly with time, as in CV , but now the scan rate is considerably lower. Second, the mass transport in the cell is no longer determined by diffusion only, because the solution is kept under constant flow. Under these conditions, the width of the diffusion layer remains constant (i.e., the diffusion layer does not expand with time, as in CV) [332,338], because forced convection keeps the bulk concentration at a fixed distance δ (see figure 16.6) from the electrode. Therefore, the maximum value of the current is observed when the concentration of R at the electrode surface is essentially zero, corresponding

<!-- image -->

E

/ V

Figure 16.12 Voltammogram obtained in a photomodulation voltammetry experiment.

to the highest value of (∂ [ R ] /∂ x ) x = 0 ; but because the diffusion layer does not expand, this gradient will remain steady and a plateau is reached. The cathodic wave of figure 16.12 (reduction of R to R -) can be similarly explained, but now the applied potential decreases with time.

The electrochemical technique used in PV is known as linear sweep voltammetry with a slow sweep rate. It can be shown [332] that under the conditions just described (a constant δ ) and for a reversible process, the applied potential ( E ) is related to the measured current ( i ) by

<!-- formula-not-decoded -->

where E 1 / 2, the half-wave potential, is identified with the formal potential, E o ′ ( R + / R ) or E o ′ ( R / R -) , and i lim is the limiting current (i.e., the value of i when E → ∞ ) . Deviations from equation 16.39 indicate irreversibility, and the constant RT /( nF ) is replaced by the factor C = 2.110 RT /( nF α) [351], where α is the charge transfer coefficient . This basic parameter, which varies between 0 and 1, reflects the symmetry of the activation barriers for the anodic and cathodic electrode reactions (e.g., α = 0.5 for a one-electron transfer signifies that the barrier is symmetric relative to the oxidized and the reduced species) [180,332]. Note that C ≈ RT /( nF ) only when α ≈ 0.5. The irreversibility of the electrode process increases when α becomes lower or higher than 0.5.

Wayner and colleagues stated in their publication that the voltammograms obtained for the species investigated are not reversible. However, the redox potentials derived from the half-wave potentials are generally in good agreement (within 100 mV) with the data determined from other methods [351]. The application of E o ′ ( R + / R ) and E o ′ ( R / R -) values in thermochemical cycles that are subsets of those in Figures 16.1 or 16.2 can be found, for example, in the review by Wayner and Parker [328].

## References to Part II

1. O. Kubaschewski, R. Hultgren. Metallurgical andAlloyThermochemistry . In Experimental Thermochemistry , vol. 2; H. A. Skinner, Ed.; Interscience: New Y ork, 1962; chapter 16.
2. I. Wadsö. Microcalorimeters . Quart. Rev. Biophys. 1970 , 3 , 383-427.
3. W.Hemminger,G.Höhne. Calorimetry:FundamentalsandPractice . Verlag Chemie: Weinheim, 1984.
4. J. Roquerol,W . Zielenkiewicz. Suggested Practice for Classification of Calorimeters . Thermochim. Acta 1986 , 109 , 121-137.
5. W. Hemminger, S. M. Sarge. Definitions, Nomenclature, Terms and Literature . In Handbook of Thermal Analysis and Calorimetry , vol. 1: Principles and Practice ; M. E. Brown, Ed.; Elsevier: New Y ork, 1998; chapter 1.
6. C. Teixeira. Photocalorimetry . Methods and Applications . In Energetics of Stable Molecules and Reactive Intermediates ; M. E. Minas da Piedade, Ed.; NATO ASI Series C, Kluwer: Dordrecht, 1999; 105-136.
7. M. Månsson. Miniaturization of Bomb Combustion Calorimetry . In Experimental Chemical Thermodynamics , vol. 1: Combustion Calorimetry ; S. Sunner, M. Månsson, Eds.; IUPAC-Pergamon Press: Oxford, 1979; chapter 17.
8. M. Månsson. Thermochemistry: Some Recent Lines of Development . Pure Appl. Chem. 1983 , 55 , 417-426.
9. R. Sabbah. Microcombustion: An Important Tool for Thermochemical Investigation of Organic Compounds . Indian J. Technol. 1992 , 30 , 545-552.
10. M. E. Minas da Piedade. Oxygen Bomb Combustion Calorimetry: Principles and Applications to Organic and Organometallic Compounds . In Energetics of Stable Molecules and Reactive Intermediates ; M. E. Minas da Piedade, Ed.; NATO ASI Series C, Kluwer: Dordrecht, 1999.
11. Y. Nagano, T. Sugimoto. Micro-combustion Calorimetry Aiming at 1 mg Samples . J. Therm. Anal. Cal. 1999 , 57 , 867-874.
12. M. Sakiyama, T. Kiyobayashi. Micro-bomb Combustion Calorimeter Equiped with an Electric Heater for Aiding Complete Combustion . J. Chem. Thermodynamics 2000 , 32 , 269-279.
13. J. Z. Dávalos, M. V . Roux. The Design, Construction and Testing of a Microcombustion Calorimeter Suitable for Organic Compounds Containing C, H and O . Meas. Sci. Technol. 2000 , 11 , 1421-1425.
14. A. Xu-wu, H. Jun. Mini-bomb Combustion Calorimeter . Thermochim. Acta 2000 , 352-353 , 273-277.
15. A. Rojas-Aguilar. An Isoperibol Micro-bomb Combustion Calorimeter for Measurement of the Enthalpy of Combustion. Application to the Study of Fullerene C 60 . J. Chem. Thermodynamics 2002 , 34 , 1729-1743.

16. A. Rojas, A. Valdés. An Isoperibol Micro-bomb Calorimeter for Measurement of the Enthalpy of Combustion of Organic Compounds. Application to the Study of Succinic Acid and Acetanilide . J. Chem. Thermodynamics 2003 , 35 , 1309-1319.
17. A. Rojas-Aguilar, A. Valdés-Ordoñez. Micro-combustion Calorimetry Employing a Calvet Heat Flux Calorimeter . J. Chem. Thermodynamics 2004 , 36 , 619-626.
18. M. Ducros, H. Tachoire. Calorimétrie de Combustion à Volume Constant dans l'Oxygène ( 1ère Partie ). L'Actualité Chim. 1978 , 9 .
19. E. S. Domalski. From the History of Combustion Calorimetry . In Experimental Chemical Thermodynamics , vol. 1: Combustion Calorimetry ; S. Sunner, M. Månsson, Eds.; IUPAC-Pergamon Press: Oxford, 1979; chapter 18.
20. E. W. Washburn. Standard States for Bomb Calorimetry . J. Res. Nat. Bur. Stand. 1933 , 10 , 525-558.
21. J. Coops, R. S. Jessup, K. van Nes. Calibration of Calorimeters for Reactions in a Bomb at Constant Volume . In Experimental Thermochemistry , vol. 1; F . D. Rossini, Ed.; Interscience: New Y ork, 1956; chapter 3.
22. I. Wadsö. Calculation Methods in Reaction Calorimetry . Science Tools 1966 , 13 , 33-39.
23. S. R. Gunn. On the Calculation of the Corrected Temperature Rise in Isoperibol Calorimetry. Modifications of the Dickinson Extrapolation Method of Treatment of Thermistor-Thermometer Resistance Values . J. Chem. Thermodynamics 1971 , 3 , 19-34.
24. S. Sunner. Basic Principles of Combustion Calorimetry . In Experimental Chemical Thermodynamics , vol. 1: Combustion Calorimetry ; S. Sunner, M. Månsson, Eds.; IUPAC-Pergamon Press: Oxford, 1979; chapter 2.
25. C. Mosselman, K. L. Churney. Calibration of Combustion Calorimeters . In Experimental Chemical Thermodynamics , vol. 1; Combustion Calorimetry ; S. Sunner, M. Månsson, Eds.; IUPAC-Pergamon Press: Oxford, 1979; chapter 3.
26. C. E. Vanderzee. Evaluation of Corrections from Temperature-Time Curves in Isoperibol Calorimetry under Normal and Adverse Operating Conditions . J. Chem. Thermodynamics 1981 , 13 , 1139-1150.
27. Y. Luo. Study on the Cooling Correction in Bomb Calorimetry . Fuel 1983 , 62 , 845-848.
28. S. N. Hajiev. Bomb Calorimetry . In Thermochemistry and Equilibria of Organic Compounds , book 1; M. Frenkel, Ed.; VCH Publishers: New Y ork, 1993; chapter 6.
29. E. H. P . Cordfunke, W . Ouweltjes. Solution Calorimetry for the Determination of Enthalpies of Reaction of Inorganic Substances at 298.15 K . In Experimental Thermodynamics , vol. 4: Solution Calorimetry ; K. N. Marsh, P . A. G. O'Hare, Eds.; Blackwell Scientific Publications: Oxford, 1994; chapter 14.
30. R. N. Goldberg, R. L. Nuttall, E. J. Prosen, A. P . Brunetti. Digital Data Acquisition and Computer Computation Applied to Calorimetric Experiments . Nat. Bur. Stand. Report 1971 , 10437.
31. A. P. Brunetti, E. J. Prosen, R. N. Goldberg. The Enthalpy of Reaction of Tris ( hydroxymethyl ) aminomethane with Hydrochloric Acid . J. Res. Nat. Bur. Stand. 1973 , 77A , 599-606.
32. M. Månsson. A 4.5 cm 3 Bomb Combustion Calorimeter and an Ampoule Technique for 5 to 10 mg Samples with V apour Pressures Below Approximately 3 kPa ( 20Torr ). J. Chem. Thermodynamics 1973 , 5 , 721-732.
33. C. P . Fitzsimmons, C. B. Kirkbride. APrecision Enthalpy of Solution Calorimeter for Slow Rates of Solution. The Enthalpy of Solution of Vitreous Silica in Hydrofluoric Acid . J. Chem. Thermodynamics 1970 , 2 , 265-273.

34. S. G. Canagaratna, J. Witt. Calculation ofTemperature Rise in Calorimetry . J. Chem. Educ. 1988 , 65 , 126-129.
35. W.P.White. The Modern Calorimeter . Chemical Catalog Company: NewY ork, 1928.
36. A. R. Chaloner, H. A. Gundry, A. R. Meetham. An Electrically Calibrated Bomb Calorimeter . Phil. Trans. Roy. Soc. London Ser. A 1955 , 553-581.
37. J. Coops, K. van Nes, A. Kentie, J. W . Dienske. Researches on Heat of Combustion. I: Method and Apparatus for the Accurate Determination of Heats of Combustion . Rec. Trav. Chim. Pays-Bas 1947 , 66 , 113-130.
38. J. Coops, K. van Nes, A. Kentie, J. W . Dienske. Researches on Heat of Combustion. II: Internal Lag and Method of Stirring in Isothermally Jacketed Calorimeters . Rec. Trav. Chim. Pays-Bas 1947 , 66 , 131-141.
39. Recommended Reference Materials for the Realization of Physicochemical Properties . K. N. Marsh, Ed.; IUPAC-Blackwell Scientific Publications: Oxford, 1987.
40. Reference Materials for Calorimetry and Differential Thermal Analysis . R. Sabbah, Ed.; Thermochim. Acta 1999 , 331 , 91-204.
41. R. S. Jessup. Heat of Combustion of Benzoic Acid with Special Reference to the Standardization of Bomb Calorimeters . J. Res. Nat. Bur. Stand. 1942 , 29 , 247-270.
42. J. D. Cox, G. Pilcher. Thermochemistry of Organic and Organometallic Compounds . Academic Press: London, 1970.
43. S. N. Hajiev. Bomb Calorimetry . In Thermochemistry and Equilibria of Organic Compounds , book 1; M. Frenkel, Ed.; VCH Publishers: New Y ork, 1993; chapter 3.
44. Equation 7.31 was derived from a least squares fit to the data given in W . N. Hubbard, D.W. Scott, G. Waddington. Standard States Corrections for Combustions in a Bomb at Constant Volume . In Experimental Thermochemistry , vol. 1; F . D. Rossini, Ed.; Interscience: New Y ork, 1956; p. 93.
45. W. N. Hubbard, D. W . Scott, G. Waddington. Standard States Corrections for Combustions in a Bomb at Constant V olume . In Experimental Thermochemistry , vol. 1; F. D. Rossini, Ed.; Interscience: New Y ork, 1956; chapter 5.
46. E. J. Prosen. Combustion in a Bomb of Compounds Containing, Carbon, Hydrogen, Oxygen, and Nitrogen . In Experimental Thermochemistry , vol. 1; F . D. Rossini, Ed.; Interscience: New Y ork, 1956; chapter 6.
47. (a) M. D. M. C. Ribeiro da Silva, M. A. R. Matos, M. C. Vaz, L. M. N. B. F. Santos, G. Pilcher, W . E. Acree Jr., J. R. Powell. Enthalpies of Combustion of the Pyridine N-oxide Derivatives: 4-Methyl-, 3-Cyano-, 4-Cyano-, 3-Hydroxy-, 2-Carboxy-, 4Carboxy-, and 3-Methyl-4-Nitro, and of the Pyridine Derivatives: 2-Carboxy- and 4Carboxy-.The Dissociation Enthalpies of the N-O Bonds . J. Chem.Thermodynamics 1998 , 30 , 869-878. (b) M. D. M. C. Ribeiro da Silva, personal communication.
48. D. R. Lide, Ed. CRC Handbook of Chemistry and Physics. CRC Press: Boca Raton, 2005.
49. H. P . Diogo, G. Persy, M. E. Minas da Piedade, J. Wirz. The Enthalpy of Formation of Pyracylene . J. Org. Chem. 1996 , 61 , 6733-6734.
50. Calculated from (∂ U /∂ p ) T = -T (∂ B /∂ T ) p , where B is the second virial coefficient, by using the B data in ref. [48].
51. M. Månsson, W. N. Hubbard. Strategies in the Calculation of Standard-State Energies of Combustion from the Experimentally Determined Quantities . In Experimental Chemical Thermodynamics , vol. 1: Combustion Calorimetry ; S. Sunner, M. Månsson, Eds.; IUPAC-Pergamon Press: Oxford, 1979; chapter 17.
52. Obtained from a least squares fit to the data at 298.15 K given in W . N. Hubbard, D.W. Scott, G. Waddington. Standard States Corrections for Combustions in a Bomb

- at Constant Volume . In Experimental Thermochemistry , vol. 1; F . D. Rossini, Ed.; Interscience: New Y ork, 1956; chapter 5.
53. H.Y. Afeefy, J. F . Liebman, S. Stein. Neutral Thermochemical Data . In NIST Chemistry WebBook ; NIST Standard Reference Database Number 69; P . J. Linstrom, W. G. Mallard, Eds.; National Institute of Standards and Technology: Gaithersburg, June 2005 (webbook.nist.gov).
54. F. D. Rossini. Calibrations of Calorimeters for Reactions in a Flame at Constant Pressure . In Experimental Thermochemistry , vol. 1; F . D. Rossini, Ed.; Interscience: NewYork, 1956; chapter 4.
55. E. Wilhelm, R. Battino, R. J. Wilcock. Low-Pressure Solubilities of Gases in Liquid Water . Chem. Rev. 1977 , 77 , 219-262.
56. G. Olofsson. Assignment of Uncertainties . In Experimental Chemical Thermodynamics , vol. 1: Combustion Calorimetry ; S. Sunner, M. Månsson, Eds.; IUPACPergamon Press: Oxford, 1979; chapter 6.
57. L. Bjellerup. OntheAccuracyofHeatofCombustionDataObtainedwithaPrecision Moving-Bomb Calorimetric Method for Organic Bromine Compounds . Acta Chem. Scand. 1961 , 15 , 121-140.
58. J. D. Cox, D. D. Wagman, V . A. Medvedev, Eds. CODATA Key Values for Thermodynamics . Hemisphere: New Y ork, 1989.
59. J. B. Pedley. Thermochemical Data and Structures of Organic Compounds . Thermodynamics Research Center Data Series, vol. 1; Thermodynamics Research Center: College Station, 1994.
60. G. Waddington, S. Sunner, W. N. Hubbard. Combustion in a Bomb of Organic Sulfur Compounds . In Experimental Thermochemistry , vol. 1; F . D. Rossini, Ed.; Interscience: New Y ork, 1956; chapter 7.
61. A. J. Head, W. D. Good. Combustion of Liquid/Solid Organic Compounds with Non-metallic Hetero-atoms . In Experimental Chemical Thermodynamics , vol. 1: Combustion Calorimetry ; S. Sunner, M. Månsson, Eds.; IUPAC-Pergamon Press: Oxford, 1979; chapter 9.
62. S. N. Hajiev. Bomb Calorimetry . In Thermochemistry and Equilibria of Organic Compounds , book 1; M. Frenkel, Ed.; VCH Publishers: New Y ork, 1993; chapter 4.
63. W. D. Good, D. W . Scott. Combustion in a Bomb of Organic Fluorine Compounds . In Experimental Thermochemistry , vol. 2; H. A. Skinner, Ed.; Interscience: New Y ork, 1962; chapter 2.
64. L. Smith, W . N. Hubbard. Combustion in a Bomb of Organic Chlorine Compounds . In ExperimentalThermochemistry , vol. 1; F . D. Rossini, Ed.; Interscience: NewY ork, 1956; chapter 8.
65. L. Smith, L. Bjellerup. Combustion in a Bomb of Organic Bromine Compounds . In Experimental Thermochemistry , vol. 1; F . D. Rossini, Ed.; Interscience: New Y ork, 1956; chapter 9.
66. L. Bjellerup. Combustion in a Bomb of Organic Bromine Compounds . In Experimental Thermochemistry , vol. 2; H. A. Skinner, Ed.; Interscience: New Y ork, 1962; chapter 3.
67. L. Smith. Combustion in a Bomb of Organic Iodine Compounds . In Experimental Thermochemistry , vol. 1; F . D. Rossini, Ed.; Interscience: NewY ork, 1956; chapter 10.
68. W. D. Good, D. W . Scott. Combustion in a Bomb of Organometallic Compounds . In Experimental Thermochemistry , vol. 2; H. A. Skinner, Ed.; Interscience: New Y ork, 1962; chapter 4.
69. C. E. Holley Jr., E. J. Huber Jr. Combustion Calorimetry of Metals and Simple Metallic Compounds . In Experimental Chemical Thermodynamics , vol. 1: Combustion

- Calorimetry ; S. Sunner, M. Månsson, Eds.; IUPAC-Pergamon Press: Oxford, 1979; chapter 10.
70. H. A. Skinner. Combustion Calorimetry of Organometallic Compounds . In Experimental Chemical Thermodynamics , vol. 1: Combustion Calorimetry ; S. Sunner, M. Månsson, Eds.; IUPAC-Pergamon Press: Oxford, 1979; chapter 11.
71. G. Pilcher. Combustion Calorimetry of Organometallic Compounds . In Energetics of Organometallic Species ; J. A. Martinho Simões, Ed.; NATO ASI Series C; Kluwer: Dordrecht, 1991; chapter 2.
72. I. B. Rabinovich, V . P. Nistranov, V . I. Telnoy, M. S. Sheiman. Thermochemical andThermodynamic Properties of Organometallic Compounds . Begell House: New York, 1999.
73. M. M. Popoff, P . K. Schirokich. Ein Calorimeter zum Verbrennen von Chlor- und Bromderivaten . Z. Phys. Chem. A 1933 , 167 , 183-187.
74. W. D. Good, D. W. Scott, G. Waddington. Combustion Calorimetry of Organic Fluorine Compounds by a Rotating-Bomb Method . J. Phys. Chem. 1956 , 60 , 1080-1089.
75. H. P . Diogo, M. E. Minas da Piedade. A Micro-combustion Calorimeter Suitable for Samples of Mass 10 mg to 50 mg. Application to Solid Compounds of C, H, and O, and of C, H, O, and N. J. Chem. Thermodynamics 1995 , 27 , 197-206.
76. R. C. Santos, H. P . Diogo, M. E. Minas da Piedade. TheDeterminationoftheStandard Molar Enthalpy of Formation of 4-Chlorobenzoic Acid by Micro Rotating-Bomb Combustion Calorimetry . J. Chem. Thermodynamics 1999 , 31 , 1417-1427.
77. G. P . Adams,A. S. Carson, P . G. Laye. Heats of Combustion of Organo-metallic Compounds using a Vacuum-Jacketed, Rotating, Aneroid Calorimeter . Trans. Faraday Soc. 1969 , 65 , 113-120.
78. Ullmann's Encyclopedia of Industrial Chemistry (5th ed.), vol. A25; B. Elvers, S. Hawkins, W. Russey, Eds.; VCH: Weinhein, 1994; 676-677.
79. J. D. Cox, H. A. Gundry, A. J. Head. Thermodynamic Properties of Fluorine Compounds. Part 1. Heats of Combustion of p-Fluorobenzoic Acid, Pentafluorobenzoic Acid, Hexafluorobenzene, and Decafluorocyclohexene . Trans. Faraday Soc. 1964 , 60 , 653-665.
80. N. K. Smith, D. W. Scott, J. P . McCullough. Combustion Calorimetry of Organic Chlorine Compounds. The Heat of Combustion of 2,3,5,6-Tetrachloro-p-xylene . J. Phys. Chem. 1964 , 68 , 934-939.
81. G. J. Stridh. On the Slow Oxidation of Arsenic ( III ) Oxide to Arsenic ( V ) Oxide in Aqueous Solution by Elemental Oxygen and its Effect on the Precise Determination of Energies of Combustion of Organic Chloro- and Bromo-compounds . J. Chem. Thermodynamics 1975 , 7 , 703-705.
82. A. S. Carson, P . G. Laye, J. B. Pedley, A. M. Welsby. The Enthalpies of Formation of Iodomethane, Diiodomethane, Triiodomethane, and Tetraiodomethane by Rotating Combustion Calorimetry . J. Chem. Thermodynamics 1993 , 25 , 262-269.
83. D. R. Kirklin, E. S. Domalski. Enthalpies of Combustion of Triphenylphosphine and Triphenylphosphine Oxide . J. Chem. Thermodynamics 1988 , 20 , 743-754.
84. D. R. Kirklin, E. S. Domalski. Energy of Combustion of Triphenylphosphate . J. Chem. Thermodynamics 1989 , 21 , 449-456.
85. D. R. Kirklin, E. S. Domalski. Enthalpy of Formation of Triphenylphosphine Sulfide . Struct. Chem. 1996 , 7 , 355-361.
86. W. D. Good, D. M. Fairbrother, G. Waddington. Manganese Carbonyl: Heat of Formation by Rotating-Bomb Calorimetry . J. Phys. Chem. 1958 , 62 , 853-856.

87. M. E. Minas da Piedade, L. Shaofeng, G. Pilcher. Enthalpy of Formation of Dycyclopentadienyltungsten Dichloride by Rotating-Bomb Calorimetry . J. Chem. Thermodynamics 1987 , 19 , 195-199.
88. A.T.Hu,G.C.Sinke,M.Månsson,B.Ringnér. Test Substances for Bomb Combustion Calorimetry. p-Chlorobenzoic Acid . J. Chem. Thermodynamics 1972 , 4 , 283-299.
89. Z. -C. Tan, A. Kamaguchi, Y. Nagano, M. Sakiyama. Standard Enthalpy of Formation of 2-Chloro-6-( trichloromethyl ) pyridine . J. Chem. Thermodynamics 1989 , 21 , 615-623.
90. G.Pilcher. OxygenFlameCalorimetry . In Experimental ChemicalThermodynamics , vol. 1: Combustion Calorimetry ; S. Sunner, M. Månsson, Eds.; IUPAC-Pergamon Press: Oxford, 1979; chapter 14.
91. E. J. Prosen, F. D. Rossini. Heats of Combustion of Eight Normal Paraffin Hydrocarbons in the Liquid State . J. Res. Nat. Bur. Stand. 1944 , 33 , 255-272.
92. F. D. Rossini. The Heats of Combustion of Methane and Carbon Monoxide . J. Res. Nat. Bur. Stand. 1931 , 6 , 37-49.
93. F. D. Rossini. The Heat of Formation of Water and the Heats of Combustion of Methane and Carbon Monoxide. A Correction . J. Res. Nat. Bur. Stand. 1931 , 7 , 329-330.
94. D.A. Pittam, G. Pilcher. Measurements of Heats of Combustion by Flame Calorimetry. Part 8. Methane, Ethane, Propane, n-Butane and 2-Methylpropane . J. Chem. Soc. Faraday Trans. I 1972 , 68 , 2224-2229.
95. F. D. Rossini. The Heats of Combustion of Methyl and Ethyl Alcohols . J. Res. Nat. Bur. Stand. 1932 , 8 , 119-139.
96. G. Pilcher, H. A. Skinner, A. S. Pell, A. E. Pope. Measurements of Heats of Combustion by Flame Calorimetry. Part 1. Diethyl Ether, Ethyl Vinyl Ether and Divinyl Ether . Trans. Faraday Soc. 1963 , 59 , 316-330.
97. F. D. Rossini. Heat and Free Energy of Formation of Water and Carbon Monoxide . J. Res. Nat. Bur. Stand. 1939 , 22 , 407-414.
98. F. D. Rossini. The Heat of Formation of Hydrogen Chloride and Some Related Thermodynamic Data . J. Res. Nat. Bur. Stand. 1932 , 9 , 679-702.
99. F. D. Rossini. The Heat of Formation of Water . J. Res. Nat. Bur. Stand. 1931 , 6 , 1-35.
100. F. D. Rossini, J. W . Knowlton, H. L. Johnston. Heat and Free Energy of Formation of Deuterium Oxide . J. Res. Nat. Bur. Stand. 1946 , 24 , 369-388.
101. J. R. Eckman, F. D. Rossini. The Heat of Formation of Sulphur Dioxide . J. Res. Nat. Bur. Stand. 1929 , 3 , 597-618.
102. H. von Wartenberg, H. Schütza. DieVerbrennungswarme des Cyans . Z. Phys. Chem. 1933 , A164 , 386-388.
103. J. W . Knowlton, E. J. Prosen. Heat of Combustion and Formation of Cyanogen . J. Res. Nat. Bur. Stand. 1951 , 46 , 489-495.
104. D. W. H. Casey, S. Fordham. AnAll-Glass Calorimeter, and the Heat of Combustion of Ethyl Chloride . J. Chem. Soc. 1951 , 2513-2516.
105. R. A. Fletcher, G. Pilcher. Measurements of Heats of Combustion by Flame Calorimetry. Part 7. Chloromethane, Chloroethane, 1-Chloropropane, 2-Chloropropane . Trans. Faraday Soc. I 1971 , 67 , 3191-3201.
106. F. D. Rossini. Unit of Energy; Fundamental Constants . In Experimental Thermochemistry , vol. 1; F . D. Rossini, Ed.; Interscience: New Y ork, 1956; chapter 2.
107. NIST-JANAFThermochemicalTables (4th ed.). M. W . Chase Jr., Ed.; J. Phys. Chem. Ref. Data 1998 , 1-1951; Monograph 9.
108. B. Ruscic, R. E. Pinzon, M. L. Morton, G. von Laszevski, S. J. Bittner, S. G. Nijsure, K. A. Amin, M. Minkoff, A. F. Wagner. Introduction to Active Thermochemical

- Tables: Several ' Key ' Enthalpies of Formation Revisited . J. Phys. Chem.A 2004 , 108 , 9979-9997.
109. R. C. King, G.T.Armstrong. Constant Pressure Flame Calorimetry with Fluorine II. The Heat of Formation of Oxygen Difluoride . J. Res. Nat. Bur. Stand. 1968 , 72A , 113-131.
110. W. N. Hubbard. Fluorine Bomb Calorimetry . In Experimental Thermochemistry , vol. 2; H. A. Skinner, Ed.; Interscience: New Y ork, 1962; chapter 6.
111. W. N. Hubbard, G. K. Johnson, V .Y. Leonidov. Combustion Calorimetry in Fluorine and Other Halogens . In Experimental Chemical Thermodynamics , vol. 1: Combustion Calorimetry ; S. Sunner, M. Månsson, Eds.; IUPAC-Pergamon Press: Oxford, 1979; chapter 12.
112. V. Ya. Leonidov, P . A. G. O'Hare. Fluorine Combustion Calorimetry: Progress in RecentYears and Possibilities of Further Development . Pure Appl. Chem. 1992 , 64 , 103-110.
113. P. A. G. O'Hare. The Nuts and Bolts and Results of Fluorine Bomb Calorimetry . In Energetics of Stable Molecules and Reactive Intermediates ; M. E. Minas da Piedade, Ed.; NATO ASI Series C, Kluwer: Dordrecht, 1999; 55-75.
114. V. Ya. Leonidov, P . A. G. O'Hare. Fluorine Calorimetry . Begell House: New Y ork, 2000.
115. G. T. Armstrong. Fluorine Flame Calorimetry . In Experimental Thermochemistry , vol. 2; H. A. Skinner, Ed.; Interscience: New Y ork, 1962; chapter 7.
116. G.T.Armstrong,R.C.King. FluorineFlameCalorimetry . In ExperimentalChemical Thermodynamics , vol. 1: Combustion Calorimetry ; S. Sunner, M. Månsson, Eds.; IUPAC-Pergamon Press: Oxford, 1979; chapter 15.
117. R. S. Jessup, R. E. McCoskey, R. A. Nelson. The Heat of Formation of Tetrafluoromethane . J. Am. Chem. Soc. 1955 , 77 , 244-245.
118. E. S. Domalski, G. T. Armstrong. The Heats of Combustion of Polytetrafluoroethylene ( Teflon ) and Graphite in Elemental Fluorine . J. Res. Natl. Bur. Stand. 1967 , 71A , 105-118.
119. E. Greenberg, W . N. Hubbard. Fluorine Bomb Calorimetry. XXIII. The Enthalpy of Formation of Carbon Tetrafluoride . J. Phys. Chem. 1968 , 72 , 222-227.
120. M. Berthelot, H. Moissan. Chaleur de Combination du Fluor avec l'Hydrogéne . Ann. Chim. Phys. 1891 , 23 , 570-574.
121. E.Greenberg,J.L.Settle, H. M. Feder,W . N. Hubbard. FluorineBombCalorimetry. I. The Heat of Formation of Zirconium Tetrafluoride . J. Phys. Chem. 1961 , 65 , 1168-1172.
122. R. L. Nuttall, S. Wise, W. N. Hubbard. Combustion Bomb Reaction Vessel for Spontaneously Combustible Materials . Rev. Sci. Instrum. 1961 , 32 , 1402-1403.
123. P. A. G. O'Hare, G. A. Hope. Thermodynamic Properties of Tungsten Ditelluride ( WTe 2 ) II. Standard Molar Enthalpy of Formation at the Temperature of 298.15 K . J. Chem. Thermodynamics 1992 , 24 , 639-647.
124. P. A. G. O'Hare, S. Susman, K. J. Volin, S. C. Rowland. Combustion Calorimetry of Rhombohedral Sulfur in Fluorine: A Question of Impurities. The Standard Molar Enthalpies of Formation of SF 6 ( g ) and SO 2 -4 ( aq ) at the Temperature of 298.15 K . J. Chem. Thermodynamics 1992 , 24 , 1009-1017.
125. I. Tomaszkiewicz, G. A. Hope, C. M. Beck II, P. A. G. O'Hare . Thermodynamic Properties of Silicides. VI. Pentamolybdenum Trisilicide ( Mo 5 Si 3 ) . Fluorine Combustion Calorimetric Determination of the Standard Molar Enthalpy of Formation at the Temperature of 298.15 K. J. Chem. Thermodynamics 1997 , 29 , 87-98.

126. P. A. G. O'Hare, I. Tomaszkiewicz, C. M. Beck II, H-J. Seifert. Thermodynamics of Silicon Nitride. I. Standard Molar Enthalpies of Formation /Delta1 f H o m at theTemperature of 298.15 K of α -Si 3 N 4 and β -Si 3 N 4 . J. Chem.Thermodynamics 1999 , 31 , 303-322.
127. J. Thomsen. Thermochemische Untersuchungen , vol. 4; Barth: Leipzig, 1882-86.
128. H. A. Skinner, J. M. Sturtevant, S. Sunner. The Design and Operation of Reaction Calorimeters . In Experimental Thermochemistry , vol. 2; H. A. Skinner, Ed.; Interscience: New Y ork, 1962; chapter 9.
129. C. E. Vanderzee. Reduction of Results to the Isothermal Calorimetric Process and to the Standard-State Process in Solution-Reaction Calorimetry . J. Chem. Thermodynamics 1981 , 13 , 947-983.
130. C. E. Vanderzee. Reduction of Experimental Results to Standard State Quantities . In Experimental Thermodynamics , vol. 4: Solution Calorimetry ; K. N. Marsh, P . A. G. O'Hare, Eds.; Blackwell Scientific Publications: Oxford, 1994; chapter 2.
131. S. Sunner, I. Wadsö. On the Design and Efficiency of Isothermal Reaction Calorimeters . Acta Chem. Scand. 1959 , 13 , 97-108.
132. Instruction Manual of LKB 8700-1 Precision Calorimetry System for Reaction and Solution Calorimetry . LKB-Produkter AB, Sweden.
133. I. Wadsö, R. J. Irving. Use of Tris ( hydroxymethyl ) aminomethane as a Test Substance in Reaction Calorimetry . Acta Chem. Scand. 1964 , 18 , 195-201.
134. Standards Committee. U.S. Calorimetry Conference, 1966.
135. E. J. Prosen, M. V . Kilday. Enthalpies of Reaction of Tris ( hydroxymethyl ) aminomethane in HCl ( aq ) and in NaOH ( aq ). J. Res. Natl. Bur. Stand. 1973 , 77A , 581-597.
136. M. V . Kilday. Systematic Errors in an Isoperibol Solution Calorimeter Measured with Standard Reference Reactions . J. Res. Natl. Bur. Stand. 1980 , 85 , 449-465.
137. R. L. Montgomery, R. A. Melaugh, C.-C. Lau, G. H. Meier, H. H. Chan, F. D. Rossini. Determination of the Energy Equivalent of a Water Solution Calorimeter with a Standard Substance . J. Chem. Thermodynamics 1977 , 9 , 915-936.
138. C. E. Vanderzee, D. H. Waugh, N. C. Haas. The Influence of Grinding Stress and ThermalAnnealingontheEnthalpyofSolutionofTris ( hydroxymethyl ) aminomethane and its Use as a Test Substance in Solution Calorimetry . J. Chem. Thermodynamics 1981 , 13 , 1-12.
139. A. E. Van Til, D. C. Johnson. A New Calorimetric Standard. 4-Aminopyridine . Thermochim. Acta 1977 , 20 , 177-193.
140. T. E. Burchfield, L. G. Hepler. Enthalpies of Solution of 4-Aminopyridine inAqueous Perchloric Acid at 298.15 and 303.15 K: Possible Use of 4-Aminopyridine as an Exothermic Reference Reaction for Solution Calorimetry . J. Chem.Thermodynamics 1981 , 13 , 513-518.
141. M. J. Akello, M. I. Paz-Andrade, G. Pilcher. Enthalpies of Solution of Three Crystalline Aminopyridines in Aqueous Perchloric Acid and in Water at 298.15 K: The Solution of 4-Aminopyridine as a Reference Reaction for Solution Calorimetry . J. Chem. Thermodynamics 1983 , 15 , 949-956.
142. (a) M. J. Calhorda, M. A. A. F. de C. T. Carrondo, A. R. Dias, A. M. Galvão, M. H. Garcia, A. M. Martins, M. E. Minas da Piedade, C. I. Pinheiro, C. C. Romão, J. A. Martinho Simões, L. F. Veiros. Syntheses, Electrochemistry, and Bonding of Bis ( cyclopentadienyl ) molybdenum Alkyl Complexes. Molecular Structure of Mo ( η 5 C 5 H 5 ) 2 ( C 4 H 9 ) 2 . Thermochemistry of Mo ( η 5 C 5 H 5 ) 2 R 2 and Mo ( η 5 C 5 H 5 ) 2 L ( R = CH 3 , C 2 H 5 , C 4 H 9 , and L = Ethylene, Diphenylacetylene ). Organometallics 1991 , 10 , 483-494. (b) M. E. Minas da Piedade. Tese de Doutoramento . Instituto Superior Técnico: Lisboa, Portugal, 1988.

143. G.K.Johnson,I.R.Tasker,H.E.Flotow,P .A.G.O'Hare,W.S.Wise. Thermodynamic Studies of Mordenite, Dehydrated Mordenite and Gibbsite . Am. Mineral. 1992 , 77 , 85-93.
144. G. Pilcher, H. A. Skinner. Thermochemistry of Organometallic Compounds . In The Chemistry of the Metal-Carbon Bond ; F. R. Hartley, S. Patai, Eds.; John Wiley: NewYork, 1982; chapter 2.
145. A. R. Dias, J. A. Martinho Simões. On the Evaluation of Metal-Ligand ' Bond Strengths ' in M (η -C 5 H 5 ) 2 L 2 Complexes . Rev. Port. Quim. 1982 , 24 , 191-199.
146. A.R.Dias,J.A.MartinhoSimões. Thermochemistry of M (η 5 -C 5 H 5 ) 2 Ln Complexes . Polyhedron 1988 , 16/17 , 1531-1544.
147. J. A. Martinho Simões, J. L. Beauchamp. Transition Metal-Hydrogen and MetalCarbon Bond Strengths : The Keys to Catalysis . Chem. Rev. 1990 , 90 , 629-688.
148. H. P . Diogo, J. A. Simoni, M. E. Minas da Piedade, A. R. Dias, J. A. Martinho Simões. Thermochemistry of Zirconium and Niobium Organometallic Compounds . J. Am. Chem. Soc. 1993 , 115 , 2764-2774.
149. J. A. Martinho Simões. Organometallic Thermochemistry Data . In NIST Chemistry WebBook ; NIST Standard Reference Database Number 69; P . J. Linstrom, W. G. Mallard, Eds.; National Institute of Standards and Technology: Gaithersburg, June 2005 (webbook.nist.gov).
150. V. I. Tel'noi' I. B. Rabinovich. Thermochemistry of Organic Compounds of the Transition Metals . Russ. Chem. Rev. 1977 , 46 , 689-705.
151. M. E. Minas da Piedade, A. R. Dias, J. A. Martinho Simões. Filling Ampules with Air-Sensitive Compounds without a Glove Box . J Chem. Educ. 1991 , 68 , 261.
152. (a) J. C. G. Calado, A. R. Dias, J. A. Martinho Simões, M. A. V . Ribeiro da Silva. Metal-Hydrogen and Metal-Iodine Bond-Enthalpy Contributions in [ M (η -C 5 H 5 ) 2 L 2 ] Compounds ( M = Mo, W; L = H, I ). Rev. Port. Quim. 1979 , 21 , 129-131. (b) J. A. Martinho Simões. Tese de Doutoramento . Instituto Superior Técnico: Lisboa, Portugal, 1981.
153. E. Wilhelm, R. Battino. Thermodynamic Functions of the Solubilities of Gases in Liquids at 25 ◦ C . Chem. Rev. 1973 , 73 , 1-9.
154. G. K. Johnson, I. R. Tasker, D. A. Howell, J. V . Smith. Thermodynamic Properties of Silicalite . J. Chem. Thermodynamics 1987 , 19 , 617-632.
155. G. K. Johnson, P . N. Smith, W . N. Hubbard. The Enthalpies of Solution and Neutralization of HF ( l ) ; Enthalpies of Dilution and Derived Thermodynamic Properties of HF ( aq ). J. Chem. Thermodynamics 1973 , 5 , 793-809.
156. E. Calvet, H. Prat. Microcalorimétrie. Applications Physico-Chimiques et Biologiques . Masson: Paris, 1956.
157. E. Calvet, H. Prat. Récents Progrès en Microcalorimétrie . Dunod: Paris, 1958.
158. E. Calvet. Microcalorimetry of Slow Phenomena . In ExperimentalThermochemistry , vol. 1; F . D. Rossini, Ed.; Interscience: New Y ork, 1956; chapter 12.
159. E. Calvet. Récents Progrès en Microcalorimétrie . In ExperimentalThermochemistry , vol. 2; H. A. Skinner, Ed.; Interscience: New Y ork, 1962; chapter 17.
160. I. Wadsö. Some Problems in Calorimetric Measurements on Cellular Systems . In Biological Microcalorimetry ; A. E. Beezer, Ed.; Academic Press: London, 1980; 247-274.
161. I. Wadsö. Design and Testing of a Micro Reaction Calorimeter . Acta Chem. Scand. 1968 , 22 , 927-937.
162. T. Kiyobayashi, M. E. Minas da Piedade. The Standard Molar Enthalpy of Sublimation of η 5 -Bis-pentamethylcyclopentadienyl Iron Measured with an Electrically

- Calibrated V acuum-Drop Sublimation Microcalorimetric Apparatus . J. Chem. Thermodynamics 2001 , 33 , 11-21.
163. D. L. S. Brown, J. A. Connor, M. Y. Leung, M. I. Paz-Andrade, H. A. Skinner. The Enthalpies of Thermal Decomposition of Iron-Olefin Complexes, and the Strengths of Iron-Olefin Bonds . J. Organometal. Chem. 1976 , 110 , 79-89.
164. J. A. Connor, H.A. Skinner,Y.Virmani. Microcalorimetric Studies.Thermal Decomposition and Iodination of Metal Carbonyls . J. Chem. Soc., Faraday Trans. I 1972 , 68 , 1754-1763.
165. D. D. Wagman, W. H. Evans, V . B. Parker, R. H. Schumm, I. Halow, S. M. Bailey, K. L. Churney, R. L. Nuttall. The NBS Tables of Chemical Thermodynamic Properties: Selected V alues for Inorganic and C 1 and C 2 Organic Substances in SI Units . J. Phys. Chem. Ref. Data 1982 , 11 , Suppl. 2.
166. A. Roine. Outokumpu HSC Chemistry for Windows . Version 3.02, Outokumpu Research Oy: Finland, 1997.
167. J. A. Connor. Thermochemical Studies of Organo-transition Metal Carbonyls and Related Compounds . Top. Curr. Chem. 1977 , 71 , 71-110.
168. G. Al-Takhin, J. A. Connor, H. A. Skinner, M. T. Zafarani-Moattar. Thermochemistry of Arenetricarbonylchromium Complexes Containing Toluene, Anisole, N,N-Dimethylaniline, Acetophenone and Methylbenzoate . J. Organometal. Chem. 1984 , 260 , 189-197.
169. F. A. Adedeji, D. L. S. Brown, J. A. Connor, M. L. Leung, I. M. Paz-Andrade, H. A. Skinner. Thermochemistry of Arene Chromium Tricarbonyls and the Strengths of Arene-Chromium Bonds . J. Organometal. Chem. 1975 , 97 , 221-228.
170. R. Sabbah, I. Antipine, M. Coten, L. Davy. Quelques Reflexions de la Mesure Calorimétrique de l'Enthalpie de Sublimation ou V aporisation . Thermochim. Acta 1987 , 115 , 153-165.
171. P. Knauth, R. Sabbah. Thermochemistry of Organic Compounds-A Review on Experimental Methods and Present-Day Research Activities . Bull. Soc. Chim. Fr. 1990 , 127 , 329-346.
172. S. Murata, M. Sakiyama, S. Seki. Construction and Testing of a Sublimation Calorimetric System Using a Calvet Microcalorimeter . J. Chem. Thermodynamics 1982 , 14 , 707-721.
173. C.E.S.Bernardes,L.M.N.B.F.Santos,M.E.MinasdaPiedade . A New Calorimetric SystemtoMeasureHeatCapacitiesofSolidsbytheDropMethod . Meas.Sci.Technol. 2006 , 17 , 1405-1408.
174. J. T. Landrum, C. D. Hoff. The Heats of Hydrogenation of the Metal-Metal Bonded Complexes [ M ( CO ) 3 C 5 H 5 ] 2 ( M = Cr, Mo, W ). J. Organometal. Chem. 1985 , 282 , 215-224.
175. S. P. Nolan, C. D. Hoff. The Heats of Reaction of Phosphines with TolueneMolybdenum Tricarbonyl. Importance of Both Steric and Electronic Factors in Determining the Mo-PR 3 Bond Strength . J. Organometal. Chem. 1985 , 290 , 365-373.
176. R. Sabbah, M. Coten. Utilisation du Microcalorimètre CRMT en Calorimétrie de Combustion . Thermochim. Acta 1981 , 49 , 307-317.
177. M. Laffitte. Trends in Combustion Calorimetry. The Use of the Tian-Calvet Microcalorimeter for Combustion Measurements . In Experimental Chemical Thermodynamics , vol. 1; S. Sunner, M. Månsson, Eds.; IUPAC-Pergamon Press: Oxford, 1979; chapter 17:3.
178. A. Rojas-Aguilar, M. Martínez-Herrera. Enthalpies of Combustion and Formation of Fullerenes by Micro-combustion Calorimetry in a Calvet Calorimeter . Thermochim. Acta 2005 , 437 , 126-133.

179. C. Teixeira, I. Wadsö. Solution Photocalorimeters . Netsu Sokutei 1994 , 21 , 29-39.
180. P. W. Atkins, J. de Paula. Physical Chemistry (8th ed.). Oxford University Press: Oxford, 2006.
181. J. L. Magee, T. M. DeWitt, E. C. Smith, F. Daniels. A Photocalorimeter. The Quantum Efficiency of Photosynthesis in Algae . J. Am. Chem. Soc. 1939 , 61 , 3529-3533.
182. A. W. Adamson,A. Vogler, H. Kunkely, R. Wachter. Photocalorimetry. Enthalpies of Photolysis of trans-Azobenzene, Ferrioxalate and Cobaltioxalate Ions, Chromium Hexacarbonyl, and Dirhenium Decacarbonyl . J. Am. Chem. Soc. 1978 , 100 , 1298-1300.
183. Y. Harel, A. W . Adamson. Photocalorimetry. 2. Enthalpies of Ligand Substitution Reactions of Some Group 6 Metal Carbonyl Complexes in Solution . J. Phys. Chem. 1982 , 86 , 2905-2909.
184. Y. Harel, A. W . Adamson. Photocalorimetry. 4. Enthalpies of Substitution Reactions of Rhodium ( III ) and Iridium ( III ) Pentaammine Halides and of Ruthenium ( II ) Hexaammine . J. Phys. Chem. 1986 , 90 , 6690-6693.
185. C. Teixeira, I. Wadsö. A Microcalorimetric System for Photochemical Processes in Solution . J. Chem. Thermodynamics 1990 , 22 , 703-713.
186. M. Nakashima, A. W. Adamson. Photocalorimetry. 3. Enthalpies of Substitution Reactions of Some Cr ( III ) Ammines and Cr ( III ) and Co ( III ) Cyano Complexes in Aqueous Solution . J. Phys. Chem. 1982 , 86 , 2910-2912.
187. Y. Harel, A. W . Adamson. Photocalorimetry. 5. Enthalpies of Reaction of M 2 ( CO ) 10 ( M=Mn, Re ) Compounds with Iodine in Cyclohexane Solution at 25 ◦ C . J. Phys. Chem. 1986 , 90 , 6693-6696.
188. Y. Harel, A. W . Adamson, C. Kutal, P . A. Grutsch, K.Y asufuku. Photocalorimetry. 6. Enthalpies of Isomerization of Norbornadiene and of Substituted Norbornadienes to Corresponding Quadricyclenes . J. Phys. Chem. 1987 , 91 , 901-904.
189. J. Suurkuusk, I. Wadsö. A Multichannel Microcalorimetric System . Chem. Scripta 1982 , 20 , 155-163.
190. N. M. Görman, J. Laynez, A. Schön, J. Suurkuusk, I. Wadsö. Design andTesting of a New Microcalorimetric Vessel for Use with Living Cellular Systems and in Titration Experiments . J . Biochem. Biophys. Methods 1984 , 10 , 187-202.
191. A. R. Dias, M. E. Minas da Piedade, J. A. Martinho Simões, J. A. Simoni, C. Teixeira, H. P . Diogo, Y. Meng-Y an, G. Pilcher. Enthalpies of Formation of cis-Azobenzene and trans-Azobenzene . J. Chem. Thermodynamics 1992 , 24 , 439-447.
192. L. G. Cole, E. C. Gilbert. The Heats of Combustion of Some Nitrogen Compounds and the Apparent Energy of the N-N Bond . J. Am. Chem. Soc. 1951 , 73 , 5423-5427.
193. F. W. Schulze, H. J. Petrick, H. K. Cammenga, H. Z. Klinge. Thermodynamic Properties of the Structural Analogues Benzo[c]cinnoline, trans-Azobenzene and cis-Azobenzene . Z. Phys. Chem. 1977 , 107 , 1-19.
194. R. M. Izatt, E. H. Redd, J. J. Christensen. Application of Solution Calorimetry to a Wide Range of Chemical and Physical Problems . Thermochim. Acta 1983 , 64 , 355-372.
195. E. Freire, O. L. Mayorga, M. Straume. Isothermal Titration Calorimetry . Anal. Chem. 1990 , 62 , 950A-959A.
196. J. J. Christensen. Techniques and Theory of Titration Calorimetry . In Thermochemistry and Its Applications to Chemical and Biochemical Systems ; M. A. V . Ribeiro da Silva, Ed.; NATO ASI Series C, Riedel: Dordrecht, 1984; 1-16.
197. J. K. Grime, Ed. Analytical Solution Calorimetry . In Chemical Analysis , vol. 79; P. J. Elving, J. D. Winefordner, Eds.; Wiley: New Y ork, 1985.

198. J. L. Oscarson, R. M. Izatt, J. O. Hill, P . R. Brown. ContinuousTitration Calorimetry . In Experimental Thermodynamics , vol. 4: Solution Calorimetry ; K. N. Marsh, P . A. G. O'Hare, Eds.; Blackwell Scientific Publications: Oxford, 1994; chapter 10.
199. J. J. Christensen, J. Ruckman, D. J. Eatough, R. M. Izatt. Determination of Equilibrium Constants by Titration Calorimetry: Part I, Introduction to Titration Calorimetry . Thermochim. Acta 1972 , 3 , 203-218.
200. D. J. Eatough, J. J. Christensen, R. M. Izatt. Determination of Equilibrium Constants byTitration Calorimetry: Part II, Data Reduction and CalculationTechniques . Thermochim. Acta 1972 , 3 , 219-232.
201. D. J. Eatough, R. M. Izatt, J. J. Christensen. Determination of Equilibrium Constants by Titration Calorimetry: Part III, Application of the Method to Several Chemical Systems . Thermochim. Acta 1972 , 3 , 233-246.
202. G. Arena, R. Calí, G. Macarrone, R. Purrello. Critical Review of the Calorimetric Method for Equilibrium Constant Determination . Thermochim. Acta 1989 , 155 , 353-376.
203. D. J. Eatough, J. J. Christensen, R. M. Izatt. Experiments in Thermometric Titrimetry and Titration Calorimetry . BrighamYoung University Press: Provo, 1974.
204. J. J. Christensen. Applications of Titration Calorimetry . In Thermochemistry and Its Applications to Chemical and Biochemical Systems ; M. A. V . Ribeiro da Silva, Ed.; NATOASI Series C, Riedel: Dordrecht, 1984; 17-30.
205. J. J. Christensen. Metal-Ligand Heats and Related Thermodynamic Quantities by Titration Calorimetry . In Thermochemistry and Its Applications to Chemical and Biochemical Systems ; M. A. V . Ribeiro da Silva, Ed.; NATO ASI Series C, Riedel: Dordrecht, 1984; 253-273.
206. L. Indyk, H. F . Fisher. TheoreticalAspects of IsothermalTitration Calorimetry . Meth. Enzymol. 1998 , 295 , 350-364.
207. H. F. Ferguson, D. J. Frurip, A. J. Pastor, L. M. Peerey, L. F . Whiting. A Review of Analytical Applications of Calorimetry . Thermochim. Acta 2000 , 363 , 1-21.
208. J. M. Bell, C. F. Cowell. Methods for the Preparation of Neutral Solutions of Ammonium Citrate . J. Am. Chem. Soc. 1913 , 35 , 49-54.
209. D. J. Eatough, J. J. Christensen, R. M. Izatt. Determination of the Enthalpy of Solution of Tris-( hydroximethyl ) aminomethane in 0.1 M HCl Solution and the Enthalpy of Neutralization of HClO 4 with NaOH at Low Ionic Strengths by Use of an Improved Titration Calorimeter . J. Chem. Thermodynamics 1975 , 7 , 417-422.
210. J. D. Hale, R. M. Izzat, J. J. Christensen. ACalorimetric Study of the Heat of Ionization of Water at 25 ◦ C. J. Phys. Chem. 1963 , 67 , 2605-2608.
211. Instruction Manual of Tronac Model 550 Isothermal and Isoperibol Calorimeter System . Tronac Incorporated.
212. L. D. Hansen, T. E. Jensen, S. Mayne, D. J. Eatough, R. M. Izatt, J. J. Christensen. Heat-Loss Corrections for Small Isoperibol Calorimeter Reaction V essels . J. Chem. Thermodynamics 1975 , 7 , 919-926.
213. R. J. Angelici. Basicities of Transition Metal Complexes from Studies of their Heats of Protonation: A Guide to Complex Reactivity . Acc. Chem. Res. 1995 , 28 , 51-60.
214. R. J. Angelici. Titration Calorimetry for the Determination of Basicities ofTransition Metal Complexes . In Energetics of Stable Molecules and Reactive Intermediates ; M. E. Minas da Piedade, Ed.; NATO ASI Series C, Kluwer: Dordrecht, 1999; 77-103.
215. T. F . Bolles, R. S. Drago. A Calorimetric Procedure for Determining Free Energies, Enthalpies and Entropies for the Formation of Acid-BaseAdducts . J. Am. Chem. Soc. 1965 , 87 , 5015-5019.

216. R. S. Drago, B. B. Wayland. A Double-Scale Equation for Correlating Enthalpies of Lewis Acid-Base Interactions . J. Am. Chem. Soc. 1965 , 87 , 3571-3577.
217. G. C. Vogel, R. S. Drago. The ECW Model . J. Chem. Ed. 1996 , 73 , 701-707.
218. R. S. Drago. Applications of Electrostatic-Covalent Models in Chemistry . Surfside: Gainesville, 1994.
219. E. M. Arnett, R. A. Flowers II. Bond Cleavage Energies for Molecules and Their Associated Radical Ions . Chem. Soc. Rev. 1993 , 22 , 9-15.
220. E. M.Arnett. The Relevance of Calorimetry to Physical Organic Chemistry . J. Chem. Thermodynamics 1999 , 31 , 711-723.
221. E. M. Arnett, K. Amarnath, N. G. Harvey, J.-P . Cheng. Determination and Interrelation of Bond Heterolysis and Homolysis Energies in Solution . J. Am. Chem. Soc. 1990 , 112 , 344-355.
222. J.-P . Cheng, M. Xian, K. Wang, X.-Q. Zhu, Z. Yin, P . G. Wang. Heterolytic and HomolyticY-NO Bond Energy Scales of Nitroso-Containing Compounds: Chemical Origin of NO Release and NO Capture . J. Am. Chem. Soc. 1998 , 120 , 10266-10267.
223. M.Xian,X.-Q.Zhu,J. Lu, Z.Wen, J.-P . Cheng. TheFirst O-NO Bond Energy Scale in Solution: Heterolytic and Homolytic Cleavage Enthalpies of O-Nitrosyl Carboxylate Compounds . Org. Lett. 2000 , 2 , 265-268.
224. M. Jansson, D. Hallén, H. Koho, G. Andersson, L. Berghard, J. Heidrich, E. Nyberg, M. Uhlén, J. Kördel, B. Nilsson. Characterization of Ligand Binding of a Soluble Human Insulin-Like Growth Factor I Receptor Variant Suggests a Ligand-Induced Conformational Change . J. Biol. Chem. 1997 , 272 , 8189-8197.
225. L. R. Morss, K. L. Nash, D. D. Ensor. Thermodynamics of Lanthanide and Uranyl Complexes with Tetrahydrofuran-2,3,4,5-tetracarboxylic Acid ( THFTCA ). J. Chem. Soc., Dalton Trans. 2000 , 285-291.
226. M. E. Minas da Piedade, J. A. Martinho Simões. Energetics of Organometallic Species: The Entropic Factor . J. Organometal. Chem. 1996 , 518 , 167-180.
227. O. Herzberg, M. Epple. Formation of Polyesters by Thermally Induced Polymerization Reactions of Molecular Solids . Eur. J. Inorg. Chem. 2001 , 1395-1406.
228. G. W. H. Höhne, W. F. Hemminger, H.-J. Flammersheim. Differential Scanning Calorimetry (2nd. ed.). Springer-Verlag: Berlin, 2003.
229. B. Wunderlich. Thermal Analysis . Academic Press: San Diego, 1990.
230. P. J. Haines, M. Reading, F . W . Wilburn. Differential Thermal Analysis and Differential Scanning Calorimetry . In HandbookofThermalAnalysis and Calorimetry , vol 1: Principles and Practice ; M. E. Brown, Ed.; Elsevier: Amsterdam, 1998; chapter 5.
231. K. Galwey, M. E. Brown. Kinetic Background to Thermal Analysis and Calorimetry . In Handbook of Thermal Analysis and Calorimetry , vol 1: Principles and Practice ; M. E. Brown, Ed.; Elsevier: Amsterdam, 1998; chapter 3.
232. B. Wunderlich. Temperature Modulated Calorimetry in the 21st Century . Thermochim. Acta 2000 , 355 , 43-57.
233. E. S. Watson, M. J. O'Neil, J. Justin, N. Brenner. ADifferential Scanning Calorimeter for Quantitative Differential Thermal Analysis . Anal. Chem. 1964 , 36 , 1233-1238.
234. M. J. O' Neill. The Analysis of a Temperature-Controlled Scanning Calorimeter . Anal. Chem. 1964 , 36 , 1238-1245.
235. V. B. F. Mathot. Thermal Analysis and Calorimetry Beyond 2000: Challenges and New Routes . Thermochim. Acta 2000 , 355 , 1-33.
236. T. Ozawa. Thermal Analysis-Review and Prospect . Thermochim. Acta 2000 , 355 , 35-42.
237. J. L. McNaughton, C. T. Mortimer. Differential Scanning Calorimetry . In International Review of Science , series 2, Physical Chemistry, vol. 10: Thermochemistry

- and Thermodynamics ; H. A. Skinner, Ed.; Butterworths: London &amp; Boston, 1975; chapter 1.
238. C. T. Mortimer. Differential Scanning Calorimetry . In Thermochemistry and Its Applications to Chemical and Biochemical Systems ; M. A. V . Ribeiro da Silva, Ed.; NATOASI Series C, Riedel: Dordrecht, 1984; 47-60.
239. S. Vyazovkin. Thermal Analysis . Anal. Chem. 2006 , 78 , 3875-3886.
240. M. Reading, D. Elliot, V . L. Hill. A New Approach to the Calorimetric Investigation of Physical and Chemical Transitions . J. Thermal Anal. 1993 , 40 , 949-955.
241. P. S. Gill, S. R. Sauerbrunn, M. Reading. Modulated Differential Scanning Calorimetry . J. Thermal Anal. 1993 , 40 , 931-939.
242. M. Reading. Modulated Differential Scanning Calorimetry-A NewWay Forward in Materials Characterization . Trends Polym. Sci. 1993 , 1 , 248-253.
243. J. E. Callanan, S. A. Sullivan. Development of Standard Operating Procedures for Differential Scanning Calorimeters . Rev. Sci. Instrum. 1986 , 57 , 2584-2592.
244. C. M. Guttman, J. H. Flynn. On the Drawing of the Baseline for Differential Calorimetric Calculation of Heats of Transition . Anal. Chem. 1973 , 45 , 408-410.
245. J. H. Flynn. Thermodynamic Properties from Differential Scanning Calorimetry by Calorimetric Methods . Thermochim. Acta 1974 , 8 , 69-81.
246. J. H. Flynn. Theory of Differential Scanning Calorimetry-Coupling of Electronic and Thermal Steps . In Analytical Calorimetry , vol. 3; R. S. Porter, J. F . Johnson, Eds.; Plenum: New Y ork, 1974; 17-44.
247. J. H. Flynn. Analysis of DSC Results by Integration . Thermochim. Acta 1993 , 217 , 129-149.
248. M. J. Richardson. The Derivation of Thermodynamic Properties by DSC: Free Energy Curves and Phase Stability . Thermochim. Acta 1993 , 229 , 1-14.
249. M. J. Richardson. Quantitative Aspects of Differential Scanning Calorimetry . Thermochim. Acta 1997 , 300 , 15-28.
250. S. M. Sarge, W . Poe β necker. The Influence of Heat Resistances and HeatTransfers on the Uncertainty of Heat Capacity Measurements by Means of Differential Scanning Calorimetry . Thermochim. Acta 1999 , 329 , 17-21.
251. D. Stull, E. Westrum Jr., G. Sinke. The Chemical Thermodynamics of Organic Compounds . Wiley: New Y ork, 1969.
252. M. J. Richardson, P. Burrington. Thermal Gradients in Differential Scanning Calorimetry . J. Thermal Anal. 1974 , 6 , 345-354.
253. M. J. Richardson, N. G. Savill. Temperatures in Differential Scanning Calorimetry . Thermochim. Acta 1975 , 12 , 213-220.
254. M. J. Richardson, E. L. Charsley. Calibration and Standardisation in DSC . In Handbook of Thermal Analysis and Calorimetry , vol 1: Principles and Practice ; M. E. Brown, Ed.; Elsevier: Amsterdam, 1998; chapter 13.
255. S. M. Sarge. Determination of Characteristic Temperatures with the Scanning Calorimeter . Thermochim. Acta 1991 , 187 , 323-334.
256. G.W.H.Höhne,H.K.Cammenga,W.Eysel,E.Gmelin,W.Hemminger. TheTemperature Calibration of Differential Scanning Calorimeters . Thermochim. Acta 1990 , 160 , 1-12.
257. H. K. Cammenga, W. Eysel, E. Gmelin, W. Hemminger, G. W. H. Höhne, S. M. Sarge. The Temperature Calibration of Scanning Calorimeters. Part 2. Calibration Substances . Thermochim. Acta 1993 , 219 , 333-342.
258. E. Gmelin, S. M. Sarge. Calibration of Differential Scanning Calorimeters . Pure Appl. Chem. 1995 , 67 , 1789-1800.

259. E. Gmelin, S. M. Sarge. Temperature, Heat and Heat Flow Rate Calibration of Differential Scanning Calorimeters . Thermochim. Acta 2000 , 347 , 9-13.
260. S. M. Sarge, G. W . H. Höhne, H. K. Cammenga, W . Eysel, E. Gmelin. Temperature, Heat and Heat Flow Rate Calibration of Differential Scanning Calorimeters in the Cooling Mode . Thermochim. Acta 2000 , 361 , 1-20.
261. E. L. Charsley, P . G. Laye, V . Palakollu, J. J. Rooney, B. Joseph. DSC Studies on Organic Melting PointTemperature Standards . Thermochim.Acta 2006 , 446 , 29-32.
262. W. Poe β necker. Theoretical Investigations of the Heat Transfer at Quantitative DSC-Measurements and Its Influence on the Determination of the Thermal and Calorimetrical Properties . Thermochim. Acta 1991 , 187 , 309-322.
263. W. Poe β necker. A Theoretical Investigation of the Preconditions for Obtaining the True Thermodynamic Transition Temperature from Only One DSC Measurement . Thermochim. Acta 1993 , 219 , 325-332.
264. J. E. K. Schawe. A New Method to Estimate Transition Temperatures and Heats by Peak Form Analysis . Thermochim. Acta 1993 , 229 , 69-84.
265. H. K. Cammenga, K. Gehrich, S. M. Sarge. 4,4'-Azoxyanisole for Temperature Calibration of Differential Scanning Calorimeters in the Cooling Mode-Yes or No? . Thermochim. Acta 2006 , 446 , 36-40.
266. W. P . Brennan, B. Miller, J. Whitwell. An Improved Method of Analyzing Curves in Differential Scanning Calorimeters . Ind. Eng. Chem. Fundam. 1969 , 8 , 314-318.
267. W. F. Hemminger, S. M. Sarge. The Baseline Construction and its Influence on the Measurement of Heat with Differential Scanning Calorimeters . J. Thermal Anal. 1991 , 37 , 1455-1477.
268. H. M. Heuvel, K. C. J. B. Lind. ComputerizedAnalysis and Correction of Differential Scanning Calorimetric Data for Effects Due to Thermal Lag and Heat Capacity Changes . Anal. Chem. 1970 , 42 , 1044-1048.
269. S. M. Sarge, E. Gmelin, G. W. H. Höhne, H. K. Cammenga, W. Hemminger, W. Eysel. The Caloric Calibration of Scanning Calorimeters . Thermochim. Acta 1994 , 247 , 129-168.
270. M. J. Richardson. The Application of Differential Scanning Calorimetry to the Measurement of Specific Heat . In Compendium of Thermophysical Properties Measurement Methods , vol 2; K. D. Maglic, A. Cezairliyan, V . E. Peletsky, Eds.; Plenum: NewYork, 1992; chapter 18.
271. Y. Jin, J. Cheng, M. Varma-Nair, G. Liang, Y. Fu, B. Wunderlich, X.-D. Xiang, R. Mostovoy, A. Zettl. Thermodynamic Characterization of C 60 by Differential Scanning Calorimetry . J. Phys. Chem. 1992 , 96 , 5151-5156.
272. G. Beech, C. T. Mortimer, E. G. Tyler . Thermochemistry of Transition-metal Complexes. Part I. CoLnX 2 Complexes; n = 4 or 2; L = Pyridine, α -, β -, γ -Picoline, Quinoline, and Aniline; X = Cl, Br, I . J. Chem. Soc. ( A ) 1967 , 925-928.
273. D. M. Lemal, L. H. Dunlap. Kinetics and Thermodynamics of ( CCF 3 ) 6 Valence Isomer Interconversions . J. Am. Chem. Soc. 1972 , 94 , 6562-6564.
274. S. Sarge, H. K. Cammenga, B. Becker, R. Rohr-Aehle. Energetic and Kinetic Investigation of Thermally Induced Molecular Rearrangements of Esters of ( Hydroxymethyl ) hydridosilanes by DSC . J. Thermal Anal. 1988 , 33 , 1185-1192.
275. H. K. Cammenga, M. Epple. Basic Principles of Thermophysical Techniques and Their Applications in Preparative Chemistry . Angew. Chem. Int. Ed. Engl. 1995 , 34 , 1171-1187.
276. B. Chowdhry, S. Leharne. Simulation and Analysis of Differential Scanning Calorimetry Output: Protein Unfolding Studies 1 . J. Chem. Educ. 1997 , 74 , 236-241.
277. M. J. Almond. Short-Lived Molecules . Ellis Horwood: London, 1990.

278. A. G. Bell. Upon the Production of Sound by Radiant Energy . Philos. Mag. ( Fifth Series ) 1881 , 11 , 510-528.
279. C. K. N. Patel, A. C. Tam. Pulsed Optoacoustic Spectroscopy of Condensed Matter . Rev. Mod. Phys. 1981 , 53 , 517-550.
280. A. C.Tam. Applications of Photoacoustic SensingTechniques . Rev. Mod. Phys. 1986 , 58 , 381-431.
281. S. E. Braslavsky, G. E. Heibel. Time-Resolved Photothermal and Photoacoustic MethodsApplied to Photoinduced Processes in Solution . Chem.Rev. 1992 , 92 , 13811410.
282. L. J. Rothberg, J. D. Simon, M. Bernstein, K. S. Peters. Pulsed Laser Photoacoustic Calorimetry of Metastable Species . J. Am. Chem. Soc. 1983 , 105 , 3464-3468.
283. S. E. Braslavsky, R. M. Ellul, R. G. Weiss, H.Al-Ekabi, K. Schaffner. Photoprocesses in Biliverdin Dimethyl Ester in Ethanol Studied by Laser-Induced Optoacoustic Spectroscopy ( LIOAS ). Tetrahedron 1983 , 39 , 1909-1913.
284. J. E. Rudzki, J. L. Goodman, K. S. Peters. Simultaneous Determination of Photoreaction Dynamics and Energetics Using Pulsed, Time-Resolved Photoacoustic Calorimetry . J. Am. Chem. Soc. 1985 , 107 , 7849-7854.
285. R. M. Borges dos Santos, A. L. C. Lagoa, J. A. Martinho Simões. Photoacoustic Calorimetry. An Examination of a Non-classical Thermochemistry Tool . J. Chem. Thermodynamics 1999 , 31 , 1483-1510.
286. A. Maciejewski, A. Jaworska-Augustyniak, Z. Szeluga, J. Wojtczak, J. Karolczak. Determination of FerroceneTriplet Lifetime by MeasuringT 1 → T 1 EnergyTransfer to Phenylosazone-D-Glucose . Chem. Phys. Lett. 1988 , 153 , 227-232.
287. S.-Y. Hou, W . M. Hetherington III, G. M. Korenowski, K. B. Eisenthal. Intramolecular ProtonTransfer and Energy Relaxation in ortho-Hydroxybenzophenone . Chem. Phys. Lett. 1979 , 68 , 282-284.
288. R. R. Hung, J. J. Grabowski. Enthalpy Measurements in Organic Solvents by Photoacoustic Calorimetry:A Solution to the ReactionV olume Problem . J. Am. Chem. Soc. 1992 , 114 , 351-353.
289. K. B. Clark, D. D. M. Wayner, S. H. Demirdji, T. H. Koch. Bond Dissociation Energies of 3,5,5- and 4,5,5-Trimethyl-2-oxomorpholines by Photoacoustic Calorimetry. An Assessment of the Additivity of Substituent Effects . J. Am. Chem. Soc . 1993 , 115 , 2447-2453.
290. J. A. Westrick, J. L. Goodman, K. S. Peters. A Time-Resolved Photoacoustic Calorimetry Study of the Dynamics of Enthalpy and Volume Changes Produced in the Photodissociation of Carbon Monoxide from Sperm Whale Carboxymyoglobin . Biochemistry 1987 , 26 , 8313-8318.
291. M. S. Herman, J. L. Goodman. Reaction Volumes of Excited-State Processes: Formation and Complexation of the Pt 2 ( P 2 O 5 H 2 ) 4 -4 Excited State . J. Am. Chem. Soc. 1989 , 111 , 9105-9107.
292. G. Farrell, T. J. Burkey. HowStrong are Metal-Alkane Bonds? Separation ofThermal and Molecular Contributions to Photoacoustic Signals Using High Pressure . Abstr. Pap. Am. Chem. Soc . 1994 , 208 , 523-INOR.
293. D. D. M. Wayner, E. Lusztyk, D. Pagé, K. U. Ingold, P . Mulder, L. J. J. Laarhoven, H. S. Aldrich. Effects of Solvation on the Enthalpies of Reaction of tert-Butoxyl Radicals with Phenol and on the Calculated O-H Bond Strength in Phenol . J. Am. Chem. Soc. 1995 , 117 , 8737-8744.
294. D. Lynch, J. F. Endicott. A Pulsed Photoacoustic Microcalorimeter for the Detection of Upper Excited-State Processes and Intersystem Crossing Yields . Appl. Spectroscopy 1989 , 43 , 826-833.

295. L. G. Arnault, R. A. Caldwell, J. E. Elbert, L. A. Melton. Recent Advances in Photoacoustic Calorimetry:Theoretical Basis and Improvements in Experimental Design . Rev. Sci. Instrum. 1992 , 63 , 5381-5389.
296. T. J. Burkey, M. Majewsky, D. Griller. Heats of Formation of Radicals and Molecules by a Photoacoustic Technique . J. Am. Chem. Soc. 1986 , 108 , 2218-2221.
297. P. Mulder, O. W. Saastad, D. Griller. O-H Bond Dissociation Energies in paraSubstituted Phenols . J. Am. Chem. Soc. 1988 , 110 , 4090-4092.
298. J. A. Howard, J. C. Scaiano, H. Fischer, Eds. Landolt-Börnstein, New Series II/B . Springer-Verlag: New Y ork, 1984.
299. K. S. Peters. Time-Resolved Photoacoustic Calorimetry: From Carbenes to Proteins . Angew. Chem. Int. Ed. Engl. 1994 , 33 , 294-302.
300. J. Rudzki Small, L. J. Libertini, E. W . Small. Analysis of Photoacoustic Waveforms Using the Nonlinear Least Squares Method . Biophys. Chem. 1992 , 42 , 29-48.
301. Sound Analysis . Version 1.50D; Quantum Northwest: Spokane, 1999.
302. G. K. Yang, K. S. Peters, V . Vaida. Strength of the Metal-Ligand Bond in LCr ( CO ) 5 Measured by Photoacoustic Calorimetry. Chem. Phys. Lett. 1986 , 125 , 566-568.
303. G. K. Yang, V . Vaida, K. S. Peters. Application of Time-Resolved Photoacoustic Calorimetry to Cr-CO Bond Enthalpies in Cr ( CO ) 5 -L . Polyhedron 1988 , 7 , 16191622.
304. R. M. Borges dos Santos, V . S. F. Muralha, C. F. Correia, R. C. Guedes, B. J. Costa Cabral, J. A. Martinho Simões. S-HBondDissociation Enthalpies inThiophenols: A Time-Resolved Photoacoustic Calorimetry and Quantum Chemistry Study . J. Phys. Chem. A 2002 , 106 , 9883-9889.
305. C. F. Correia, R. C. Guedes, R. M. Borges dos Santos, B. J. Costa Cabral, J. A. Martinho Simões. O-H Bond Dissociation Enthalpies in Hydroxyphenols. A Time-Resolved Photoacoustic Calorimetry and Quantum Chemistry Study . Phys. Chem. Chem. Phys. 2004 , 6 , 2109-2118.
306. V. S. Muralha, R. M. Borges dos Santos, J. A. Martinho Simões. Energetics of Alkylbenzyl Radicals: A Time-Resolved Photoacoustic Calorimetry Study . J. Phys. Chem. A 2004 , 108 , 936-942.
307. C. F. Correia, R. M. Borges dos Santos, S. G. Estácio, J. P . Telo, B. J. Costa Cabral, J. A. Martinho Simões. Reaction of para-Hydroxyl-substituted Diphenylmethanes with tert-Butoxy Radical . Chem. Phys. Chem. 2004 , 5 , 1217-1221.
308. C. F. Correia, P . M. Nunes, R. M. Borges dos Santos, J. A. Martinho Simões. GasPhase Energetics of Organic Free Radicals Using Time-Resolved Photoacoustic Calorimetry . Thermochim. Acta 2004 , 420 , 3-11.
309. G. C. Justino, C. F . Correia, L. Mira, R. M. Borges dos Santos, J.A. Martinho Simões, A. M. Silva, C. Santos, B. Gigante. Antioxidant Activity of a Catechol Derived from Abietic Acid . J. Agric. Food Chem. 2006 , 54 , 342-348.
310. P. M. Nunes, F. Agapito, B. J. Costa Cabral, R. M. Borges dos Santos, J. A. Martinho Simões. Enthalpy of Formation of the Cyclopentadienyl Radical: Photoacoustic Calorimetry and Ab Initio Studies . J. Phys. Chem. A 2006 , 110 , 5130-5134.
311. P. M. Nunes, C. F. Correia, R. M. Borges dos Santos, J. A. Martinho Simões. Time-resolved Photoacoustic Calorimetry as a Tool to Determine Rate Constants of Hydrogen Abstraction Reactions . Int. J. Chem. Kinet. 2006 , 38 , 357-363.
312. D.A. Skoog, F. J. Holler, T. A. Nieman. Principles of Instrumental Analysis (5th ed.). Saunders: Philadelphia, 1998.
313. M. C. Sousa Lopes, H. W. Thompson. Hydrogen Bonding between Phenols and Cyanides . Spectrochim. Acta 1968 , 24A , 1367-1383.

314. J. Timmermans. Physico-Chemical Constants of Pure Compounds , vol. 2. Elsevier: Amsterdam, 1965.
315. M. E. Thompson, S. M. Baxter, A. R. Bulls, B. J. Burger, M. C. Nolan, B. D. Santarsiero,W . P . Schaefer, J. E. Bercaw. ' σ BondMetathesis ' for C-H Bonds of Hydrocarbons and Sc-R ( R = H, alkyl, aryl ) Bonds of Permethylscandocene Derivatives. Evidence for Noninvolvement of the π System in Electrophilic Activation of Aromatic and Vinylic C-H Bonds . J. Am. Chem. Soc. 1987 , 109 , 203-219.
316. K.Denbigh. ThePrinciplesofChemicalEquilibrium (4th ed.). Cambridge University Press: Cambridge, 1981.
317. F. Oldani, G. Bor. Fundamental Metal Carbonyl Equilibria. II. A Quantitative Study of the Equilibrium between Dirhodium Octacarbonyl andTetrarhodium Dodecacarbonyl under Carbon Monoxide Pressure . J. Organomet. Chem. 1983 , 246 , 309-324; ibid. 1985 , 279 , 459-460.
318. P. G. T. Fogg, W . Gerrard. Solubility of Gases in Liquids: A Critical Evaluation of Gas/Liquid Systems in Theory and Practice . Wiley: Chichester, 1991.
319. G. Bor, U. K. Dietler, P . Pino, A. Poë. Kinetics and Mechanism of the Reaction of Tetracobalt Dodecacarbonyl with Carbon Monoxide under Pressure . J. Organomet. Chem. 1978 , 154 , 301-315.
320. M. Lucarini, G. F. Pedulli, M. Cipollone. Bond Dissociation Enthalpy of α -Tocopherol and Other Phenolic Antioxidants . J. Org. Chem. 1994 , 59 , 5063-5070.
321. M. Lucarini, P . Pedrielli, G. F . Pedulli, S. Cabiddu, C. Fattuoni. Bond Dissociation Energies of O-H Bonds in Substituted Phenols from Equilibration Studies . J. Org. Chem. 1996 , 61 , 9259-9263.
322. H. E. Bryndza, L. K. Fong, R. A. Paciello, W . Tam, J. E. Bercaw. Relative MetalHydrogen, -Oxygen, -Nitrogen, and -Carbon Bond Strengths for Organoruthenium and Organoplatinum Compounds; Equilibrium Studies of Cp* ( PMe 3 ) 2 RuX and ( DPPE ) MePtX Compounds . J. Am. Chem. Soc. 1987 , 109 , 1444-1456.
323. C. E. H. Bawn, S. F. Mellish. A Method of Determination of the Rate of Molecular Dissociation in Solution. Parts I and II-The Rate of Dissociation of Benzoyl Peroxide and 2,2'-Azo-bis ( isobutyronitrile ) inVarious Solvents . Trans. Faraday Soc. 1951 , 47 , 1216-1227.
324. T. W. Koenig, B. P . Hay, R. G. Finke. Cage Effects in Organotransition Metal Chemistry: Their Importance in the Kinetic Estimation of Bond Dissociation Energies in Solution . Polyhedron 1988 , 7 , 1499-1516.
325. P. H. P. Brinkmann, G. A. Luinstra, A. Saenz. Isomerization of an η 3 -Allyl to an ( E ) -1-Propenyl in ( C 5 Me 5 ) ( C 5 Me 4 CH 2 ) TiC 3 H 5 : Mechanism, Kinetics and Thermodynamics . J. Am. Chem. Soc. 1998 , 120 , 2854-2861.
326. H. E. Bryndza, P . J. Domaille, W . Tam, L. K. Fong, R. A. Paciello, J. E. Bercaw. Comparison of Metal-Hydrogen, -Oxygen, -Nitrogen and -Carbon Bond Strengths and Evaluation of Functional GroupAdditivity Principles for Organoruthenium and Organoplatinum Compounds . Polyhedron 1988 , 7 , 1441-1452.
327. H. E. Bryndza, P . J. Domaille, R. A. Paciello, J. E. Bercaw. Kinetics and Mechanism of Phosphine Exchange for Ruthenium ( II ) Complexes in the Series ( η 5 -C 5 Me 5 )( PMe 3 ) 2 RuX. Ancillary Ligand Effects on Dative Ligand Dissociation . Organometallics 1989 , 8 , 379-385.
328. D. D. M. Wayner, V . D. Parker. Bond Energies in Solution from Electrode Potentials and Thermochemical Cycles. A Simplified and General Approach. Acc. Chem. Res. 1993 , 26 , 287-294.
329. D. Griller, J. A. Martinho Simões, P . Mulder, B. A. Sim, D. D. M. Wayner. Unifying the Solution Thermochemistry of Molecules, Radicals, and Ions . J. Am. Chem. Soc. 1989 , 111 , 7872-7876.

330. F. G. Bordwell. Equilibrium Acidities in Dimethyl Sulfoxide Solution . Acc. Chem. Res. 1988 , 21 , 456-463.
331. M. R. Wasielewski, R. Breslow. Thermodynamic Measurements on Unsubstituted Cyclopropenyl Radical and Anion, and Derivatives, by Second Harmonic Alternating Current V oltammetry of Cyclopropenyl Cations . J. Am. Chem. Soc. 1976 , 98 , 4222-4229.
332. C. M. A. Brett, A. M. O. Brett. Electrochemistry. Principles, Methods, and Applications . Oxford University Press: Oxford, 1993.
333. A. J. Bard, L. R. Faulkner. Electrochemical Methods. Fundamentals and Applications . Wiley: New Y ork, 1980.
334. R. Greef, R. Peat, L. M. Peter, D. Pletcher, J. Robinson. Instrumental Methods in Electrochemistry . Ellis Horwood: Chichester, 1985.
335. M. Tilset. Energetics of Transition Metal-X Bonding Probed by Electrochemical Techniques . M. E. Minas da Piedade, Ed.; NATO ASI Series C, Kluwer: Dordrecht, 1999; chapter 7.
336. G. A. Mabbott . An Introduction to Cyclic V oltammetry . J. Chem. Educ. 1983 , 60 , 697-702.
337. P. T. Kissinger, W . R. Heineman. Cyclic Voltammetry . J. Chem. Educ. 1983 , 60 , 702-706.
338. J. T. Maloy. Factors Affecting the Shape of Current-Potential Curves . J. Chem. Educ. 1983 , 60 , 285-289.
339. C. P. Andrieux, P. Hapiot, J. Pinson, J.-M. Savéant. Determination of Formal Potentials of Chemically Unstable Redox Couples by Second-Harmonic Alternating Current Voltammetry and Cyclic Voltammetry. Application to the Oxidation of Thiophenoxide Ions . J. Am. Chem. Soc. 1993 , 115 , 7783-7788.
340. M. Tilset. Derivative Cyclic V oltammetry: Applications in the Investigation of the Energetics of Organometallic Electrode Reactions . In Energetics of Organometallic Species ; J. A. Martinho Simões, Ed.; NATO ASI Series C, Kluwer: Dordrecht, 1991; chapter 8.
341. V. D. Parker. Homolytic Bond ( H-A ) Dissociation Free Energies in Solution. Applications of the Standard Potential of the ( H + /H · ) Couple . J. Am. Chem. Soc. 1992 , 114 , 7458-7462; ibid. 1201.
342. F. G. Bordwell, J.-P . Cheng, J.A. Harrelson Jr. Homolytic Bond Dissociation Energies in Solution from Equilibrium Acidity and Electrochemical Data . J. Am. Chem. Soc. 1988 , 110 , 1229-1231.
343. F. G. Bordwell, J.-P . Cheng, G.-Z. Ji, A. V . Satish, X. Zhang. Bond Dissociation Energies in DMSO Related to the Gas Phase . J. Am. Chem. Soc. 1991 , 113 , 9790-9795.
344. F. G. Bordwell, X.-M. Zhang. From Equilibrium Acidities to Radical Stabilization Energies . Acc. Chem. Res. 1993 , 26 , 510-517.
345. F. G. Bordwell, W .-Z. Liu. Solvent Effects on Homolytic Bond Dissociation Energies of Hydroxylic Acids . J. Am. Chem. Soc. 1996 , 118 , 10819-10823.
346. F. G. Bordwell, J.-P . Cheng. Substituent Effects on the Stabilities of Phenoxyl Radicals and the Acidities of Phenoxyl Radical Cations . J. Am. Chem. Soc. 1991 , 113 , 1736-1746.
347. J. Lind, X. Shen, T. E. Eriksen, G. Merényi. The One-Electron Reduction Potential of 4-Substituted Phenoxyl Radicals in Water . J. Am. Chem. Soc. 1990 , 112 , 479-482.
348. F. G. Bordwell, X.-M. Zhang. Acidities and Homolytic Bond Dissociation Enthalpies of 4-Substituted-2,6-di-tert-Butylphenols . J. Phys. Org. Chem. 1995 , 8 , 529-535.

349. R. M. Borges dos Santos, J. A. Martinho Simões. Energetics of the O-H Bond in Phenol and Substituted Phenols: A Critical Evaluation of Literature Data . J. Phys. Chem. Ref. Data 1998 , 27 , 707-739.
350. D. D. M. Wayner, D. Griller. Oxidation and Reduction Potentials of Transient Free Radicals . J. Am. Chem. Soc. 1985 , 107 , 7764-7765.
351. D. D. M. Wayner, D. J. McPhee, D. Griller. Oxidation and Reduction Potentials of Transient Free Radicals . J. Am. Chem. Soc. 1988 , 110 , 132-137.
352. D. Griller, D. D. M. Wayner. RadicalThermochemistry and Organic Reactions . Pure Appl. Chem. 1989 , 61 , 717-724.

## Appendix A

## Units, Conversion Factors, and

## Fundamental Constants

There are several publications dealing with units and symbols of physical chemical quantities. Some also list the values of the fundamental physical constants, as recommendedbytheCommitteeonDatafor Science andTechnology (CODATA) in 2005 [1]. The following tables contain the information that is relevant for molecular energetics [1, 2].

Four rather useful conversion factors (calculated from the fundamental constants below), which are not given in the tables, are

```
1 eV corresponds to 96.4853377 kJ mol -1 1 hartree corresponds to 2625.49963 kJ mol -1 1 cm -1 corresponds to 1.19626565 × 10 -2 kJ mol -1 13 1
```

- 1 Hz corresponds to 3.99031269 × 10 -kJ mol -

(Not all the digits are significant. They are given to minimize round-off errors).

Table A1 Names and symbols for some SI units

| Physical Quantity         | Name     | Symbol (Expression in Terms of Other SI Units)   |
|---------------------------|----------|--------------------------------------------------|
| Base quantity             |          |                                                  |
| length                    | meter    | m                                                |
| mass                      | kilogram | kg                                               |
| time                      | second   | s                                                |
| electric current          | ampere   | A                                                |
| thermodynamic temperature | kelvin   | K                                                |
| amount of substance       | mole     | mol                                              |
| luminous intensity        | candela  | cd                                               |

Table A1 ( Continued )

Physical Quantity

## Derived quantity

| frequency                     | hertz          | Hz (s - 1 )                           |
|-------------------------------|----------------|---------------------------------------|
| force                         | newton         | N (m kg s - 2 )                       |
| pressure                      | pascal         | Pa (Nm - 2 =m - 1 kg s - 2 )          |
| energy, work, heat            | joule          | J(Nm=m 2 kg s - 2 )                   |
| power                         | watt           | W(J s - 1 =m 2 kg s - 3 )             |
| electric charge               | coulomb        | C (s A)                               |
| electric potential difference | volt           | V (J C - 1 =m 2 kg s - 3 A - 1 )      |
| electric resistance           | ohm            | /Omega1 (VA - 1 =m 2 kg s - 3 A - 2 ) |
| capacitance                   | farad          | F (CV - 1 =m - 2 kg - 1 s 4 A 2 )     |
| magnetic flux density         | tesla          | T (m - 2 sV = kg - 1 s - 2 A - 1 )    |
| inductance                    | henry          | H (VA - 1 s=m 2 kg s - 2 A - 2        |
| Celsius temperature           | degree Celsius | ◦ C (K)                               |

Table A2 Some common non-SI units and their conversion factors

| Physical Quantity                                                                              | Name of Unit                                                                                                                                                           | Symbol                                                | SI Value                                                                                                                                                          |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| time time length volume pressure pressure pressure pressure energy energy energy energy energy | minute hour ångstrom a liter bar torr a millimeter of mercury (conventional) a atmosphere a erg a electronvolt hartree calorie, thermochemical a international joule b | min h Å L, l bar Torr mmHg atm erg eV E h cal J (int) | 60 s 3600 s 10 - 10 m 10 - 3 m 3 10 5 Pa (101325/760) Pa 13.5951 × 980.665 × 10 101325 Pa 10 - 7 J ≈ 1.60218 × 10 - 19 J 4.3597442 × 10 - 18 J 4.184 J 1.000165 J |

a The IUPAC does not recommend the use of this unit [2].

b The unit international joule was used until about 1948 to report thermochemical data.

Name

Symbol (Expression in Terms of Other SI Units)

Table A3 Some fundamental physical constants

| Quantity                                                                                                                                                                                                                                                                               | Symbol                                                                                                  | Value a                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| speed of light in vacuum vacuum permeability vacuum permittivity Planck constant elementary charge electron rest mass proton rest mass neutron rest mass atomic mass constant Avogadro constant Boltzmann constant Faraday constant gas constant zero of the Celsius scale Bohr radius | c 0 µ 0 ε 0 = 1 / ( µ 0 c 2 0 ) h /planckover2pi1 = h / 2 π e m e m p m n m u = 1 u L , N A k B F R a 0 | 299792458 ms - 1 4 π × 10 - 7 Hm - 1 8.854187817 × 10 - 12 Fm - 1 6.6260693(11) × 10 - 34 J s 1.05457168(18) × 10 - 34 J s 1.60217653(14) × 10 - 19 C 9.1093826(16) × 10 - 31 kg 1.67262171(29) × 10 - 27 kg 1.67492728(29) × 10 - 27 kg 1.66053886(28) × 10 - 27 kg 6.0221415(10) × 10 23 mol - 1 1.3806505(24) × 10 - 23 JK - 1 96485.3383(83) C mol - 1 8.314472(15) J K - 1 mol - 1 273.15 K 0.5291772108(18) × 10 - 10 m |

a The digits in parentheses represent the uncertainty in the last digits of the value.

## REFERENCES

1. P. J. Mohr, B. N. Taylor. CODATA RecommendedValues of the Fundamental Physical Constants: 2002 . Rev. Mod. Phys. 2005 , 77 , 1-107. See also physics.nist.gov/constants (November 2006).
2. IUPAC-Physical Chemistry Division. Quantities, Units and Symbols in Physical Chemistry (2nd ed.). Blackwell Scientific Publications: Oxford, 1993. A provisional document of the 3rd edition of this work is available at www.iupac.org/reports/provisional/abstract05/stohner\_310306.html (November 2006).

## Appendix B

## Thermochemical Databases

Table B1 shows a selection of thermochemical databases that have been released over the past five decades.

When can a set of data be regarded as a database? Guidelines such as the number of records or the publication medium may not be useful. CODATA values, for example, which are the recommended starting point for any database (or any thermochemical calculation, for that matter), involve only about 150 species. Also, the CODATA reports have been printed in regular scientific journals before the final set was released as a book and later posted on the Internet. Second, we could have distinguished between 'databases' and 'data compilations.' The former involve recalculation of quantities such as standard enthalpies of formation to ensure a consistent set of values (see section 2.5). Databases may also include data assessment, leading to recommended values. Data compilations, on the other hand, are just collections of literature values. Although this distinction is important (see table B1), a data compilation can be rather useful for the expert user and save many hours of literature search.

Ideally, updated online databases containing primary experimental data (e.g., enthalpies of reaction, heat capacities), from which other thermodynamic properties (e.g., enthalpies of formation, entropies) can be derived and permanently revised should be available. Though this is by no means the general case at the present time, the database development efforts seem to be evolving towards that goal. The Active Thermochemical Tables, for example (see following discussion), store experimental enthalpies of reaction, bond dissociation enthalpies, and so on, and report a variety of internally consistent data for a given species (e.g., the enthalpy of formation), obtained from a statistical analysis of the complete network of thermochemical information available for that species. The database is expanded by inserting additional thermochemical results, and a consistent set of derived thermochemical values can be kept updated. A single thermodynamic database of this type, congregating the efforts of the data compilers from several institutions, should become available!

Usefulness to the reader, based on our own experience, was in fact the main criterion to build table B1, which lists, in chronological order, the works available as books, included in software packages, or that can be consulted through

Table B1 Main thermochemical databases

| Database                             | Contents   | Form   | Consistent   | /Delta1 f H o   | /Delta1 f H o ( 0K   | D      | /Delta1 trs H o   | S o    | C o p   | o T - H o 298   | PA     | E i           | AE E ea   | Errors   | Exp. Data   | Refs.   |
|--------------------------------------|------------|--------|--------------|-----------------|----------------------|--------|-------------------|--------|---------|-----------------|--------|---------------|-----------|----------|-------------|---------|
| NIST Chemistry WebBook [1-12]        | IN,O,OM    | O      |              | /check          |                      |        | /check            | /check | /check  |                 | /check | /check /check | /check    | /check   | /check      | /check  |
| Active                               | IN,O       | P,O    | /check       | /check          | /check               | /check | /check            | /check | /check  | /check          | /check | /check /check | /check    | /check   | /check      | /check  |
| Thermochemical Tables [13] DIPPR 801 | IN,O,OM    | S      | /check       | /check          |                      |        | /check            | /check | /check  | /check          |        |               |           | /check   |             |         |
| Database [14] CRC Handbook [15-17]   | IN,O,OM    | P      |              | /check          |                      | /check | /check            | /check | /check  | /check          |        | /check        | /check    | /check   |             |         |
| Luo 03 [18]                          | O,OM       | P      |              | /check          |                      | /check |                   |        |         |                 |        |               |           | /check   |             | /check  |
| Zábranský et al. [19,24]             | IN,O       | P      |              |                 |                      |        |                   |        | /check  |                 |        |               |           | /check   | /check      | /check  |
| Leonidov and O'Hare [20]             | IN         | P      | /check       | /check          |                      |        |                   |        |         |                 |        |               |           | /check   |             | /check  |
| Rabinovich et al. [21]               | OM         | P      | /check       | /check          |                      | /check | /check            | /check | /check  | /check          |        |               |           | /check   |             | /check  |
| NIST-JANAF Tables [22,31]            | IN,O       | P,S    | /check       | /check          | /check               |        | /check            | /check | /check  | /check          |        |               |           | /check   |             | /check  |
| HSC Chemistry [23]                   | IN,O,OM    | S      |              | /check          |                      |        |                   | /check | /check  | /check          |        |               |           |          | /check      | /check  |
| Domalski and                         | O,OM       | P      |              |                 |                      |        | /check            | /check | /check  |                 |        |               |           | /check   | /check      | /check  |
| Hearing [25] Pedley 94 [26]          | O          | P      | /check       | /check          |                      |        |                   |        |         |                 |        |               |           | /check   |             | /check  |

continued

Table B1 ( Continued )

| Database                            | Contents   | Form   | Consistent   | /Delta1 f H o   | /Delta1 f H o ( 0K   | D      | /Delta1 trs H   | o S    | o C o p   | o T - H o 298   | E i AE        | E ea   | Errors   | Exp. Data   | Refs.   |
|-------------------------------------|------------|--------|--------------|-----------------|----------------------|--------|-----------------|--------|-----------|-----------------|---------------|--------|----------|-------------|---------|
| NIST Structures and Properties [27] | IN,O,OM    | S      | /check       | /check          |                      |        |                 | /check | /check    |                 | /check /check |        | /check   |             | /check  |
| NIST Therm [28]                     | O          | S      | /check       | /check          |                      |        |                 | /check | /check    |                 |               |        |          |             |         |
| Gurvich Tables [29]                 | IN,O,OM    | P      | /check       | /check          | /check               | /check | /check          | /check | /check    | /check          |               |        | /check   | /check      | /check  |
| Frenkel et al. [30]                 | IN,O       | P      | /check       | /check          |                      |        |                 | /check | /check    | /check          |               |        |          |             | /check  |
| NIST Positive Ion Energetics [32]   | IN,O,OM    | S      | /check       | /check          |                      |        |                 | /check | /check    |                 | /check /check |        | /check   | /check      | /check  |
| NIST Negative Ion Energetics [33]   | IN,O,OM    | S      | /check       | /check          |                      | /check |                 | /check |           |                 |               | /check | /check   | /check      | /check  |
| NBS 82 [34,40]                      | IN,O,OM    | P,S    | /check       | /check          | /check               |        |                 | /check | /check    | /check          |               |        |          |             |         |
| Barin 93 [35]                       | IN         | P      | /check       | /check          |                      |        |                 | /check | /check    | /check          |               |        |          |             |         |
| CODATA [36]                         | IN         | P      | /check       | /check          |                      |        |                 | /check |           | /check          |               |        | /check   | /check      | /check  |
| GIANTTables [37]                    | IN,O,OM    | P      | /check       | /check          |                      | /check |                 |        |           |                 | /check        | /check | /check   | /check      | /check  |
| Pedley 86 [38]                      | O          | P      | /check       | /check          |                      |        | /check          |        |           |                 | /check        |        | /check   | /check      | /check  |
| Majer and                           | O          | P      |              |                 |                      |        | /check          |        |           |                 |               |        | /check   | /check      | /check  |
| Svoboda [39]                        |            |        |              |                 |                      |        |                 |        |           |                 |               |        |          |             |         |
| Levin and Lias 82 [41]              | IN,O,OM    | P      | /check       |                 |                      |        |                 |        |           |                 | /check /check |        | /check   | /check      | /check  |
| Glushko Tables I [42]               | IN,O,OM    | P      | /check       | /check          | /check               | /check | /check          | /check | /check    | /check          |               |        | /check   | /check      | /check  |
| Glushko Tables II [43]              | IN,O,OM    | P      |              |                 |                      |        |                 |        |           |                 |               |        |          |             |         |
| NBSTechnical Note 270 [44]          | IN,O,OM    | P      | /check       | /check          | /check               |        |                 | /check | /check    | /check          |               |        |          |             |         |

273

Pedley 77 [45]

Rosenstock 77 [46]

Benson 76 [47]

CATCHTables

[48,50-53]

Hultgren 73 [49]

Cox and Pilcher [54]

Karapet'yants [55]

Darwent 70 [56]

Stull, Westrum, and

Sinke [57]

Franklin 69 [58]

Gaydon 68 [59]

NBS Circular 500 [60]

Bichowsky and

Rossini [61]

O,OM

IN,O,OM

IN,O

IN,OM

IN

O,OM

IN,O,OM

IN,O

IN,O

IN,O,OM

IN

IN,O,OM

IN,O,OM

P

P

P

P

P

P

P

P

P

P

P

P

P

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

/check

the Internet. Some references are primarily of historical interest. The following information was included.

1. A short designation of the database and its reference number.
2. The types of compounds covered by the database (IN = inorganic; O = organic; OM = organometallic).
3. The publishing medium (P = printed; S = software; O = online).
4. The thermochemical consistency of the databases values ( /check ). The absence of a check mark indicates nonconsistent data or that the comment does not apply. It may also mean that not all the database values are consistent.
5. The types of values reported in the database: standard enthalpies of formation at 298.15 K and 0 K, bond dissociation energies or enthalpies ( D ) at any temperature, standard enthalpy of phase transition-fusion, vaporization, or sublimation-at 298.15 K, standard entropy at 298.15 K, standard heat capacity at 298.15 K, standard enthalpy differences between T and 298.15 K, proton affinity, ionization energy, appearance energy, and electron affinity. The absence of a check mark indicates that the data are not provided. However, that does not necessarily mean that they cannot be calculated from other quantities tabulated in the database.
6. Uncertainties have been associated to each value ( /check ). The absence of a check mark indicates that no individual uncertainties have been assigned.
7. The original (experimental) literature data (e.g., enthalpies of reaction used to derive standard enthalpies of formation) are given in the database ( /check ). The absence of a check mark indicates that this information is not provided for all the values included.
8. The source of each value is indicated by literature references ( /check ). The absence of a check mark indicates that this information is not provided for all the values included.

Further comments on each database have been added, whenever necessary, after the complete literature reference.

## REFERENCES

1. NIST Chemistry WebBook . NIST Standard Reference Database Number 69; P. J. Linstrom, W. G. Mallard, Eds.; National Institute of Standards and Technology: Gaithersburg, June 2005 (webbook.nist.gov).

The NIST Chemistry WebBook is probably the most extensive of all chemical compilations. It supersedes many of NIST databases [32, 33, 37, 41, 46, 58] and it is composed by several chapters, some of which [2-12] include thermochemical information on a variety of substances. It is regularly updated, with either new values or new chapters. Not all of these chapters have thermochemical consistency. For instance, the Neutral Thermochemical Data [3] quotes the

standard enthalpies of formation directly from the original publications. However, because the experimental reaction enthalpies are also provided, the user can easily derive the correct values.

2. J. A. Martinho Simões. Organometallic Thermochemistry Data . In NIST Chemistry WebBook ; NIST Standard Reference Database Number 69; P. J. Linstrom, W. G. Mallard, Eds.; National Institute of Standards and Technology: Gaithersburg, June 2005 (webbook.nist.gov).
3. H.Y.Afeefy, J. F. Liebman, S. E. Stein. Neutral Thermochemical Data . In NIST Chemistry WebBook ; NIST Standard Reference Database Number 69; P . J. Linstrom, W . G. Mallard, Eds.; National Institute of Standards and Technology: Gaithersburg, June 2005 (webbook.nist.gov).
4. J. E. Bartmess. Negative Ion Energetics Data . In NIST Chemistry WebBook ; NIST Standard Reference Database Number 69; P . J. Linstrom, W . G. Mallard, Eds.; National Institute of Standards and Technology: Gaithersburg, June 2005 (webbook.nist.gov).
5. E. P . Hunter, S. G. Lias. Proton Affinity Data . In NIST Chemistry WebBook ; NIST Standard Reference Database Number 69; P . J. Linstrom, W . G. Mallard, Eds.; National Institute of Standards and Technology: Gaithersburg, June 2005 (webbook.nist.gov).
6. S. G. Lias. Ionization Energy Data . In NIST Chemistry WebBook ; NIST Standard Reference Database Number 69; P . J. Linstrom, W . G. Mallard, Eds.; National Institute of Standards and Technology: Gaithersburg, June 2005 (webbook.nist.gov).
7. S. G. Lias, H. M. Rosenstock, K. Draxl, B. W . Steiner, J. T. Herron, J. L. Holmes, R. D. Levin, J. F . Liebman, S. A. Kafafi. Ionization Energetics (IE, AE) Data . In NIST Chemistry WebBook ; NIST Standard Reference Database Number 69; P . J. Linstrom, W. G. Mallard, Eds.; National Institute of Standards and Technology: Gaithersburg, June 2005 (webbook.nist.gov).
8. M. Meot-Ner (Mautner), S. G. Lias. Thermochemistry of Cluster Ion Data . In NIST Chemistry WebBook ; NIST Standard Reference Database Number 69; P . J. Linstrom, W. G. Mallard, Eds.; National Institute of Standards and Technology: Gaithersburg, June 2005 (webbook.nist.gov).
9. Entropy and Heat Capacity of Organic Compounds Compiled by Glushko Thermocenter, Moscow . In NIST Chemistry WebBook ; NIST Standard Reference Database Number 69; P . J. Linstrom, W . G. Mallard, Eds.; National Institute of Standards and Technology: Gaithersburg, June 2005 (webbook.nist.gov).
10. J. S. Chickos. Heat of Sublimation Data . In NIST Chemistry WebBook ; NIST Standard Reference Database Number 69; P . J. Linstrom, W . G. Mallard, Eds.; National Institute of Standards and Technology: Gaithersburg, June 2005 (webbook.nist.gov).
11. J. S. Chickos, W. E. Acree Jr., J. F. Liebman, Students of Chem 202 (Introduction to the Literature of Chemistry), University of Missouri-St. Louis. Heat of Fusion Data . In NIST Chemistry WebBook ; NIST Standard Reference Database Number 69; P. J. Linstrom, W. G. Mallard, Eds.; National Institute of Standards and Technology: Gaithersburg, June 2005 (webbook.nist.gov).
12. E. S. Domalski, E. D. Hearing. Condensed Phase Heat Capacity Data . In NIST Chemistry WebBook ; NIST Standard Reference Database Number 69; P . J. Linstrom, W. G. Mallard, Eds.; National Institute of Standards and Technology: Gaithersburg, June 2005 (webbook.nist.gov).
13. (a) B. Ruscic, R. E. Pinzon, M. L. Morton, G. von Laszevski, S. J. Bittner, S. G. Nijsure, K. A. Amin, M. Minkoff, A. F. Wagner. Introduction to Active Thermochemical Tables: Several ' Key ' Enthalpies of Formation Revisited . J. Phys. Chem. A 2004 , 108 , 9979-9997. (b) B. Ruscic, R. E. Pinzon, G. von Laszewski,

- D. Kodeboyina, A. Burcat, D. Leahy, D. Montoya, A. F. Wagner. Active Thermochemical Tables: Thermochemistry for the 21st Century . J. Physics: Conf. Ser. 2005 , 16 , 561-570. November 2006 (cmcs.ca.sandia.gov/cmcs/portal).

The Active Thermochemical Tables (ATcT) are the result of an effort to derive accurate, reliable, and internally consistent thermochemical values based on a thermochemical network approach. They contain data for over 350 compounds. Recommended values for key compounds such as CO 2 (g), H 2 O(g), and CH 4 (g) are slightly different from those given by CODATA.

14. DIPPR 801 Database. Design Institute for Physical Properties, November 2006 (dippr.byu.edu).

The DIPPR 801 Database contains evaluated data on about 2000 industrially important chemical compounds.

15. D. R. Lide, Ed. CRC Handbook of Chemistry and Physics . CRC Press: Boca Raton, 2005.

This handbook contains a variety of thermochemical data, most of which quoted from other major compilations mentioned in table B1.

16. J. A. Kerr. Strengths of Chemical Bonds . In CRC Handbook of Chemistry and Physics ; D. R. Lide, Ed.; CRC Press: Boca Raton, 2005.

A compilation of bond dissociation enthalpies and enthalpies of formation of free radicals.

17. H. D. B. Jenkins, H. K. Roobottom. Lattice Energies . In CRC Handbook of Chemistry and Physics ; D. R. Lide, Ed.; CRC Press: Boca Raton, 2005.

A compilation of lattice energies of crystalline salts.

18. Y. R. Luo. Handbook of Bond Dissociation Energies in Organic Compounds . CRC Press: Boca Raton, 2003.

A compilation of bond dissociation enthalpies in organic compounds and enthalpies of formation of free radicals.

19. M. Zábranský, V . R˚ užiˇ cka Jr., E. S. Domalski. Heat Capacity of Liquids: Critical Review and Recommended Values. Supplement I . J. Phys. Chem. Ref. Data 2002 , 30 , 1199-1689.

A critically evaluated compilation of the heat capacities of pure liquid organic and some inorganic compounds. It covers data published between 1993 and 1999 and some data of 2000 as well as some data from older sources. This paper is an update of reference [24].

20. V.Y. Leonidov, P . A. G. O'Hare. Fluorine Calorimetry . Begell House: NewY ork, 2000.

This book is an updated English version of Ftornaya Kalorimetriya , which was published in Russian in 1978. It contains a critically analyzed survey of enthalpies of formation of inorganic compounds obtained by fluorine combustion calorimetry up to 1996.

21. I. B. Rabinovich, V. P. Nistratov, V. I. Telnoy, M. S. Sheiman. Thermochemical and Thermodynamic Properties of Organometallic Compounds . Begell House: NewYork, 1999.

This monograph contains enthalpies of formation, heat capacities, entropies, and metal-ligand bond dissociation enthalpies of organometallic compounds of transition and main group elements.

22. M. W. Chase Jr. NIST-JANAF Thermochemical Tables (4th ed.). J. Phys. Chem. Ref. Data 1998 , Monograph No. 9.

This is one of the most widely used thermochemical databases for inorganic compounds. The first and second editions of JANAF (Joint Army, Navy and Air Force) Tables date from 1964 and 1971, respectively. Supplements of the latter were released in 1974, 1975, 1978, and 1982. The third edition was published in 1985.

23. A.Roine. OutokumpuHSCChemistryforWindows . Version 3.02; Outokumpu Research Oy: Finland, 1997.

This is a rather useful computer program that allows the user to make several types of calculations, including reaction enthalpies, heat balances, equilibrium compositions, and phase stability diagrams.The noncritically evaluated database contains more than 11,000 compounds. Updated versions are now available.

24. M. Zábranský , V . R˚ užiˇ cka Jr., V . Majer, E. S. Domalski. Heat Capacity of Liquids, Critical Review and Recommended Values , vols. 1 and 2. J. Phys. Chem. Ref. Data 1996 , Monograph No. 6.

Acomprehensive collection of evaluated heat capacities of 1624 pure substances in the liquid state. This was updated in reference[19].

25. E. S. Domalski, E. D. Hearing. Heat Capacities and Entropies of Organic Compounds in the Condensed Phase , vol. 3. J. Phys. Chem. Ref. Data 1996 , 25 , 1.

This is a cumulative database, including values compiled in two earlier publications (1984 and 1990). It is superseded by the NIST Chemistry WebBook [1].

26. J. B. Pedley. Thermodynamic Data and Structures of Organic Compounds . Thermodynamics Research Center Data Series, vol. 1; Thermodynamics Research Center: College Station, 1994.

This database supersedes those in Cox and Pilcher [54], Pedley 77 [45], and Pedley 86 [38]. An empirical scheme, developed by the author, to estimate enthalpies of formation of organic compounds in gas and condensed phases, is also described.

27. S. S. Stein. NIST Structures and Properties. Version 2.0; NIST Standard Reference Database 25; National Institute of Standards and Technology: Gaithersburg, 1994.

This useful and simple-to-use software package relies on Benson' s group additivity scheme [47] to estimate thermochemical data for organic compounds in the gas phase. It also contains values from several NIST databases, including NIST Positive Ion Energetics [32] and JANAF Tables [22]. The first version of

NIST S&amp;P is from 1991. The database is superseded by the NIST Chemistry WebBook [1].

28. E. S. Domalsky, E. D. Hearing, V . J. Hearing Jr.. NIST Estimation of the Chemical Thermodynamic Properties for Organic Compounds at 298.15 K . NIST Standard Reference Database 18; National Institute of Standards and Technology: Gaithersburg, 1994.

Although the software is old-fashioned, this package is one of the best options to estimate thermochemical data for organic compounds in the gas and condensed phases. It relies on Benson' s group additivity scheme [47] and also contains selected experimental values for a large number of organic compounds.

29. L. V . Gurvich, I. V . Veyts, C. B. Alcock, Eds. Thermodynamic Properties of Individual Substances (4th ed.). Vols. 1 and 2. Hemisphere: New Y ork, 1989 and 1991. Vol. 3, CRC Press: Boca Raton, 1994.

This database offers an extensive discussion before the selection of each value. It is the English translation and update of the first three volumes of Glushko Tables [42].

30. M. Frenkel, G. J. Kabo, K. N. Marsh, G. N. Roganov, R. C. Wilhoit. Thermodynamics of Organic Compounds in the Gas State , vols. 1 and 2. Thermodynamics Research Center: College Station, 1994.

This database can be considered as an update of Stull, Westrum, and Sinke [57].

31. M. W. Chase Jr., C. A. Davies, J. R. Downey Jr., D. J. Frurip, R. A. McDonald, A. N. Syverud. NIST JANAF Thermochemical Tables 1985. Version 1.0; NIST Standard Reference Database 13; National Institute of Standards and Technology: Gaithersburg, 1993.

This is the electronic form of the third edition of the JANAF Tables [22]. As such, it is rather useful, but unfortunately the software is very primitive.

32. S. G. Lias, J. F. Liebman, R. D. Levin, S. A. Kafafi. NIST Positive Ion Energetics. Version 2.0; NIST Standard Reference Database 19A; National Institute of Standards and Technology: Gaithersburg, 1993.

This database, which is an update of the GIANT Tables [37], provides the same information as described for NIST Structures and Properties [27].

33. S. G. Lias, J. E. Bartmess, J. F . Liebman, J. L. Holmes, R. D. Levin, W . G. Mallard. NIST Negative Ion Energetics Database. Version 3.0; NIST Standard Reference Database 19B; National Institute of Standards and Technology: Gaithersburg, 1993.

This database, which is an update of the GIANTTables [37], was superseded by the NIST Chemistry WebBook [1-12].

34. D. D. Wagman, W. H. Evans, V . B. Parker, R. H. Schumm, I. Halow, S. M. Bailey, K. L. Churney, R. L. Nuttall. NIST Chemical Thermodynamics Database. Version 1.1;

NIST Standard Reference Database 2; National Institute of Standards and Technology: Gaithersburg, 1993.

This is the electronic form of NBS 82 Tables [40]. It is very difficult to use in a PC.

35. I. Barin. Thermochemical Data of Pure Substances (2nd ed.). VCH: Weinheim, 1993.

The first edition of this publication dates from 1973 (I. Barin, O. Knackle. Thermodynamic Properties of Inorganic Substances . Springer-Verlag: Berlin, 1973). A supplement, coauthored by O. Kubaschewski, was released in 1977.

36. J. D. Cox, D. D. Wagman, V . A. Medvedev, Eds. CODATA Key Values for Thermodynamics . Hemisphere: New York, 1989. The CODATA database is also posted at www.codata.org/resources/databases (November 2006).

This is, in our opinion, the primary source of thermochemical values and therefore it should be the starting point of all the other databases. The selections have been made by the Task Group on Key Values for Thermodynamics appointed in 1968 by the Committee on Data for Science and Technology (CODATA) of the International Council of Scientific Unions. Unfortunately, the number of species for which data are recommended in the final report is rather small ( ∼ 150).

37. S. G. Lias, J. E. Bartmess, J. F . Liebman, J. L. Holmes, R. D. Levin, W . G. Mallard. Gas Phase Ion and Neutral Thermochemistry . J. Phys. Chem. Ref. Data 1988 , 17 , Suppl. 1.

This database, which follows three earlier NBS publications [41,46,58], was superseded by the NIST Chemistry WebBook [1-12].

38. J. B. Pedley, R. D. Naylor, S. P . Kirby. Thermochemical Data of Organic Compounds . Chapman and Hall: London, 1986.

This database updated those in Cox and Pilcher [54] and Pedley 77 [45]. It was superseded by Pedley 94 [26].

39. V. Majer, V . Svoboda. Enthalpies of Vaporization of Organic Compounds. A Critical Review and Data Compilation . IUPAC Chemical Data Series No. 32; Blackwell: Oxford, 1985.
40. D. D. Wagman, W. H. Evans, V . B. Parker, R. H. Schumm, I. Halow, S. M. Bailey, K. L. Churney, R. L. Nuttall. The NBSTables of Chemical Thermodynamic Properties: Selected V alues for Inorganic and C 1 and C 2 Organic Substances in SI Units . J. Phys. Chem. Ref. Data 1982 , 11 , Suppl. 2.

The NBS 82 tables are still widely used, mainly because they contain data (e.g., solution enthalpies) not easily found in other databases.

41. R. D. Levin, S. G. Lias. Ionization Potential and Appearance Potential Measurements, 1971-1981 . National Standard Reference Data Series, National Bureau of Standards 71; U.S. Department of Commerce: Washington, D.C., 1982.

This database, for gaseous positive ions, follows two earlier NBS publications [46,58]. It has been superseded by the GIANT Tables [37] and by the NIST Chemistry WebBook [1-12].

42. V. P . Glushko, Ed. Thermodynamic Properties of Individual Substances (3rd ed.), vols. 1-4. Nauka: Moscow, 1978-1982.

This database offers an extensive discussion before the selection of each value. It is published in Russian, but the English translation and update of the first three volumes is available [29].

43. V. P . Glushko, Ed. Thermal Constants of Substances , vols. 1-9. Academy of Science, USSR: Moscow, 1965-1982.

This database may be considered the Russian equivalent of the NBS 82 Tables [40]. It is only available in Russian.

44. (a) D. D. Wagman, W. H. Evans, V . B. Parker, I. Halow, S. M. Bailey, R. H. Schumm. Selected V alues of Chemical Thermodynamic Properties . NBS Technical Note 270-3; Washington, D.C., 1968. (b) D. D. Wagman, W. H. Evans, V . B. Parker, I. Halow, S. M. Bailey, R. H. Schumm. Selected V alues of Chemical Thermodynamic Properties . NBSTechnical Note 270-4; Washington, D.C., 1969. (c) D. D. Wagman, W . H. Evans, V. B. Parker, I. Halow, S. M. Bailey, R. H. Schumm, K. L. Churney. Selected Values of Chemical Thermodynamic Properties . NBS Technical Note 270-5; Washington, D.C., 1971. (d) V . B. Parker, D. D. Wagman, W . H. Evans. Selected V alues of Chemical Thermodynamic Properties . NBS Technical Note 270-6; Washington, D.C., 1971. (e) R. H. Schumm, D. D. Wagman, S. Bailey, W . H. Evans, V . B. Parker. Selected V alues of Chemical Thermodynamic Properties . NBS Technical Note 270-7; Washington, D.C., 1973. (f) D. D. Wagman, W . H. Evans, V . B. Parker, R. H. Schumm, R. L. Nuttall. Selected V alues of Chemical Thermodynamic Properties . NBS Technical Note 270-8; Washington, D.C., 1981.

NBSTechnicalNote270replacedtheNBSCircular500[60]andwassuperseded by NBS 82 Tables [40].

45. J. B. Pedley, J. Rylance. Sussex-N. P . L. Computer Analysed Thermochemical Data: Organic and Organometallic Compounds . University of Sussex: Brigton, 1977.

This database updated the one in Cox and Pilcher [54]. It was superseded by Pedley 86 [38] and Pedley 94 [26].

46. H. M. Rosenstock, K. Draxl, B. W . Steiner, J. T. Herron. Energetics of Gaseous Ions . J. Phys. Chem. Ref. Data 1977 , 6 , Suppl. 1.

This database follows an earlier NBS publication [58]. It has been superseded by the GIANTTables [37] and the NIST Chemistry WebBook [1-12].

47. S. W. Benson. Thermochemical Kinetics (2nd ed.). Wiley: New Y ork, 1976.

This book contains a small database for organic and inorganic compounds. Its main value, however, is that it describes a group additivity scheme to estimate thermochemical data.An updated and extended list of group parameters is given in NIST Therm [28]. The first edition of this classic work is from 1968.

48. D. S. Barnes, J. B. Pedley, A. Kirk, E. Winser, L. G. Heath. ComputerAnalysis of Thermochemical Data (CATCH Tables), Cr, Mo and W Compounds . School of Molecular Sciences, University of Sussex: Brighton,1974.

49. R. Hultgren, P . D. Desai, D. T. Hawkins, M. Gleiser, K. K. Kelley, D. D. Wagman. Selected V alues of the Thermodynamic Properties of the Elements . American Society for Metals: Metals Park, 1973.
50. J. D. Cox, J. B. Pedley, A. Kirk, S. Seilman, L. G. Heath. ComputerAnalysis ofThermochemical Data (CATCH Tables), Halogen Compounds . School of Molecular Sciences, University of Sussex: Brighton,1972.
51. A. J. Head, J. B. Pedley, A. Kirk, S. Seilman, L. G. Heath. Computer Analysis of Thermochemical Data (CATCH Tables) , Phosphorous Compounds . School of Molecular Sciences, University of Sussex: Brighton,1972.
52. J. B. Pedley, B. S. Iseard, A. Kirk, S. Seilman, L. G. Heath. ComputerAnalysis of Thermochemical Data (CATCHTables), Silicon Compounds . School of Molecular Sciences, University of Sussex: Brighton,1972.
53. G. Pilcher, J. B. Pedley,A. Kirk, S. Seilman, L. G. Heath. ComputerAnalysis ofThermochemical Data (CATCHTables), Nitrogen Compounds . School of Molecular Sciences, University of Sussex: Brighton,1972.
54. J. D. Cox, G. Pilcher. Thermochemistry of Organic and Organometallic Compounds . Academic Press: London, 1970.

This has been, for many years, the main source of standard enthalpies of formation of neutral organic compounds. It is a classic work on thermochemistry and has set a standard for thermochemical databases. Superseded by Pedley' s 1994 compilation [26].

55. M. Kh. Karapet'yants, M. K. Karapet'yants. Handbook of Thermodynamic Constants of Inorganic and Organic Compounds . Ann Harbour-Humphrey Science Publishers: London, 1970.
56. B. D. Darwent. Bond Dissociation Energies in Simple Molecules . National Standard Reference Data Series, National Bureau of Standards 31; U.S. Department of Commerce: Washington, D.C., 1970.

Tables of bond dissociation energies at 0 K and 298.15 K.

57. D. R. Stull, E. F . Westrum Jr., G. C. Sinke. The Chemical Thermodynamics of Organic Compounds . Wiley: New Y ork, 1969.

Together with Cox and Pilcher [54] and Benson' s Thermochemical Kinetics [47], this book is a classic work on thermochemistry. It is still useful to review basic concepts and, as a database, to look for H o T -H o 298 values for many organic substances in the ideal gas state. See also [30].

58. J. L. Franklin, J. G. Dillard, H. M. Rosenstock, J. T. Herron, K. Draxl, F . H. Field. Ionization Potentials, Appearance Potentials, and Heats of Formation of Gaseous Positive Ions . National Standard Reference Data Series, National Bureau of Standards 26; U.S. Government Printing Office: Washington, D.C., 1969.

This database has been superseded by the GIANT Tables [37] and the NIST Chemistry WebBook [1-12].

59. A. G. Gaydon. Dissociation Energies and Spectra of Diatomic Molecules (3rd ed.). Chapman and Hall: London, 1968.

Table of bond dissociation energies at 0 K.

60. F. D. Rossini, D. D. Wagman, W . H. Evans, S. Levine, I. Jaffe. SelectedValues of Chemical Thermodynamic Properties . NBS Circular 500; U.S. Department of Commerce: Washington, D.C., 1952.

This database was superseded by the NBS Technical Note 270 [44].

61. F. R. Bichowsky, F. D. Rossini. The Thermochemistry of the Chemical Substances . Reinhold: New Y ork, 1936.

This is one of the first thermochemical databases ever available. The standard enthalpies of formation are tabulated at 18 ◦ C.

## Index

| absolute energy content, E = mc 2 , 10 accuracy                                                  | anthracene                                                                                                         |         |                                      |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------|--------------------------------------|
|                                                                                                  | combustion enthalpy, 16-17                                                                                         |         |                                      |
| reaction-solution calorimeters, 129-130                                                          | standard enthalpy of formation, 16                                                                                 |         |                                      |
| temperature measure in differential scanning                                                     | appearance energy                                                                                                  |         |                                      |
| calorimetry, 176-177                                                                             | calculation at any temperature, 52                                                                                 |         |                                      |
| acetic acid                                                                                      | complications, 53                                                                                                  |         |                                      |
| reaction enthalpy, 9                                                                             | energy profile for unimolecular decomposition, 53 f                                                                |         |                                      |
| standard enthalpy of formation, 17                                                               |                                                                                                                    |         |                                      |
| standard states, 18-19                                                                           | error source in experimental                                                                                       |         |                                      |
| stepwise construction of final reaction state, 11-12                                             | determination, 53 ethyl cation, 54-55                                                                              |         |                                      |
| thermochemical cycle, 11 f                                                                       | kinetic shift, 53                                                                                                  |         |                                      |
| thermochemical cycle relating                                                                    | standard enthalpy of formation, 52                                                                                 |         |                                      |
| enthalpies, 12 f                                                                                 | standard enthalpy of formation of ethyl                                                                            |         |                                      |
| acetonitrile. See phenol and acetonitrile                                                        | cation and ethane, 49 t 51 f                                                                                       |         |                                      |
| acidity, gas-phase energetics, 55-57                                                             | thermochemical cycle,                                                                                              |         |                                      |
| acoustic wave, amplitude S , 192, 193 f                                                          | Arrhenius activation energy, 219                                                                                   |         |                                      |
| activation enthalpy values, phosphine exchange                                                   | Arrhenius plot                                                                                                     |         |                                      |
| reaction, 225 f                                                                                  | benzoyl peroxide decomposition, 221 f                                                                              |         |                                      |
| activities                                                                                       | kinetic analysis, 40                                                                                               |         |                                      |
| equilibrium constants, 34, 207                                                                   | modified, 41                                                                                                       |         |                                      |
| Gibbs energy of reaction, 230                                                                    | solution reactions, 44                                                                                             |         |                                      |
| activity coefficient, dimensionless, 34                                                          | atomization, enthalpy of, 74                                                                                       |         |                                      |
| adiabatic                                                                                        | azobenzene, photochemical isomerization of                                                                         |         |                                      |
| calorimeter class, 83, 85 f                                                                      |                                                                                                                    |         |                                      |
| determination of, temperature rise /Delta1 T ad                                                  | trans - to cis -, 154-155                                                                                          |         |                                      |
| , 89-92 affinity,                                                                                | radical, basicity gas-phase energetics, 55-57 organometallic complexes, 165-166 calorimetry, second law advantage, | methoxy | term, 83 adiabatic electron 27, 28 f |
| adiabatic expansion coefficient, observed photon energy release, 196 adiabatic ionization energy | batch 33 beam splitter, photoacoustic measuring, 199                                                               |         |                                      |
|                                                                                                  | Bell' s photophone, 190, 191 f                                                                                     |         |                                      |
| molecule AB, 47 potential energy curves, 49, 50 f                                                | benzene valence isomers, energetics of interconversion by differential scanning                                    |         |                                      |
| adiabatic temperature rise, flame combustion                                                     | calorimetry, 186-187                                                                                               |         |                                      |
| calorimetry, 117 affinity, adiabatic electron, 49                                                | acid energy of combustion of,                                                                                      |         |                                      |
| amplitude S , acoustic wave, 192, 193 f , 200                                                    | benzoic standardizing laboratories, 94-96                                                                          |         |                                      |
| aneroid combustion calorimeter, micro                                                            | uncertainty interval of O-H bond                                                                                   |         |                                      |
| rotating-bomb, 111 f                                                                             | dissociation enthalpy, 222                                                                                         |         |                                      |
| anodic and cathodic parameters, cyclic                                                           | benzoyl peroxide                                                                                                   |         |                                      |
| voltammogram, 237                                                                                | Eyring and Arrhenius plots,                                                                                        |         |                                      |
|                                                                                                  | 221 f                                                                                                              |         |                                      |

| benzoyl peroxide ( continued ) rate constants of reaction, 221 t reverse of decomposition, 222 thermal decomposition, 220-222   | O-H bond lengths in phenol and ethanol, 69                                    | O-H bond lengths in phenol and ethanol, 69                                    | O-H bond lengths in phenol and ethanol, 69                                    | O-H bond lengths in phenol and ethanol, 69                                    | O-H bond lengths in phenol and ethanol, 69                                    | O-H bond lengths in phenol and ethanol, 69                                    | O-H bond lengths in phenol and ethanol, 69                                    | O-H bond lengths in phenol and ethanol, 69                                    | O-H bond lengths in phenol and ethanol, 69                                    | O-H bond lengths in phenol and ethanol, 69                                    | O-H bond lengths in phenol and ethanol, 69                                    | O-H bond lengths in phenol and ethanol, 69                                    | O-H bond lengths in phenol and ethanol, 69                                    |
|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
|                                                                                                                                 | PhO-H bond dissociation enthalpy in                                           | PhO-H bond dissociation enthalpy in                                           | PhO-H bond dissociation enthalpy in                                           | PhO-H bond dissociation enthalpy in                                           | PhO-H bond dissociation enthalpy in                                           | PhO-H bond dissociation enthalpy in                                           | PhO-H bond dissociation enthalpy in                                           | PhO-H bond dissociation enthalpy in                                           | PhO-H bond dissociation enthalpy in                                           | PhO-H bond dissociation enthalpy in                                           | PhO-H bond dissociation enthalpy in                                           | PhO-H bond dissociation enthalpy in                                           | PhO-H bond dissociation enthalpy in                                           |
|                                                                                                                                 | solution and gas phase, 62 f relation of solution and gas-phase bond          | solution and gas phase, 62 f relation of solution and gas-phase bond          | solution and gas phase, 62 f relation of solution and gas-phase bond          | solution and gas phase, 62 f relation of solution and gas-phase bond          | solution and gas phase, 62 f relation of solution and gas-phase bond          | solution and gas phase, 62 f relation of solution and gas-phase bond          | solution and gas phase, 62 f relation of solution and gas-phase bond          | solution and gas phase, 62 f relation of solution and gas-phase bond          | solution and gas phase, 62 f relation of solution and gas-phase bond          | solution and gas phase, 62 f relation of solution and gas-phase bond          | solution and gas phase, 62 f relation of solution and gas-phase bond          | solution and gas phase, 62 f relation of solution and gas-phase bond          | solution and gas phase, 62 f relation of solution and gas-phase bond          |
| bimolecular reactions                                                                                                           | dissociation enthalpies, 61 f                                                 | dissociation enthalpies, 61 f                                                 | dissociation enthalpies, 61 f                                                 | dissociation enthalpies, 61 f                                                 | dissociation enthalpies, 61 f                                                 | dissociation enthalpies, 61 f                                                 | dissociation enthalpies, 61 f                                                 | dissociation enthalpies, 61 f                                                 | dissociation enthalpies, 61 f                                                 | dissociation enthalpies, 61 f                                                 | dissociation enthalpies, 61 f                                                 | dissociation enthalpies, 61 f                                                 | dissociation enthalpies, 61 f                                                 |
| gas phase, 42                                                                                                                   | relaxation energies, 71                                                       | relaxation energies, 71                                                       | relaxation energies, 71                                                       | relaxation energies, 71                                                       | relaxation energies, 71                                                       | relaxation energies, 71                                                       | relaxation energies, 71                                                       | relaxation energies, 71                                                       | relaxation energies, 71                                                       | relaxation energies, 71                                                       | relaxation energies, 71                                                       | relaxation energies, 71                                                       | relaxation energies, 71                                                       |
| kinetics of gas-phase, 38-39                                                                                                    | reorganization energies, 69, 70-71                                            | reorganization energies, 69, 70-71                                            | reorganization energies, 69, 70-71                                            | reorganization energies, 69, 70-71                                            | reorganization energies, 69, 70-71                                            | reorganization energies, 69, 70-71                                            | reorganization energies, 69, 70-71                                            | reorganization energies, 69, 70-71                                            | reorganization energies, 69, 70-71                                            | reorganization energies, 69, 70-71                                            | reorganization energies, 69, 70-71                                            | reorganization energies, 69, 70-71                                            | reorganization energies, 69, 70-71                                            |
| bis (butadiene) iron carbonyl, thermal                                                                                          | solution phase bond dissociation                                              | solution phase bond dissociation                                              | solution phase bond dissociation                                              | solution phase bond dissociation                                              | solution phase bond dissociation                                              | solution phase bond dissociation                                              | solution phase bond dissociation                                              | solution phase bond dissociation                                              | solution phase bond dissociation                                              | solution phase bond dissociation                                              | solution phase bond dissociation                                              | solution phase bond dissociation                                              | solution phase bond dissociation                                              |
| decomposition by heat flow calorimetry,                                                                                         | enthalpy, 64                                                                  | enthalpy, 64                                                                  | enthalpy, 64                                                                  | enthalpy, 64                                                                  | enthalpy, 64                                                                  | enthalpy, 64                                                                  | enthalpy, 64                                                                  | enthalpy, 64                                                                  | enthalpy, 64                                                                  | enthalpy, 64                                                                  | enthalpy, 64                                                                  | enthalpy, 64                                                                  | enthalpy, 64                                                                  |
| 142-144                                                                                                                         | stepwise and mean bond dissociation                                           | stepwise and mean bond dissociation                                           | stepwise and mean bond dissociation                                           | stepwise and mean bond dissociation                                           | stepwise and mean bond dissociation                                           | stepwise and mean bond dissociation                                           | stepwise and mean bond dissociation                                           | stepwise and mean bond dissociation                                           | stepwise and mean bond dissociation                                           | stepwise and mean bond dissociation                                           | stepwise and mean bond dissociation                                           | stepwise and mean bond dissociation                                           | stepwise and mean bond dissociation                                           |
| Born-Haber cycle, lithium methoxide, 28 f                                                                                       | enthalpies, 64-68                                                             | enthalpies, 64-68                                                             | enthalpies, 64-68                                                             | enthalpies, 64-68                                                             | enthalpies, 64-68                                                             | enthalpies, 64-68                                                             | enthalpies, 64-68                                                             | enthalpies, 64-68                                                             | enthalpies, 64-68                                                             | enthalpies, 64-68                                                             | enthalpies, 64-68                                                             | enthalpies, 64-68                                                             | enthalpies, 64-68                                                             |
| bomb combustion calorimetry, reaction in                                                                                        | stepwise bond dissociation enthalpies in f                                    | stepwise bond dissociation enthalpies in f                                    | stepwise bond dissociation enthalpies in f                                    | stepwise bond dissociation enthalpies in f                                    | stepwise bond dissociation enthalpies in f                                    | stepwise bond dissociation enthalpies in f                                    | stepwise bond dissociation enthalpies in f                                    | stepwise bond dissociation enthalpies in f                                    | stepwise bond dissociation enthalpies in f                                    | stepwise bond dissociation enthalpies in f                                    | stepwise bond dissociation enthalpies in f                                    | stepwise bond dissociation enthalpies in f                                    | stepwise bond dissociation enthalpies in f                                    |
| closed vessel, 84                                                                                                               | first-row hydrides, 67                                                        | first-row hydrides, 67                                                        | first-row hydrides, 67                                                        | first-row hydrides, 67                                                        | first-row hydrides, 67                                                        | first-row hydrides, 67                                                        | first-row hydrides, 67                                                        | first-row hydrides, 67                                                        | first-row hydrides, 67                                                        | first-row hydrides, 67                                                        | first-row hydrides, 67                                                        | first-row hydrides, 67                                                        | first-row hydrides, 67                                                        |
| bond dissociation energy, upper limits for some                                                                                 | transferability of bond enthalpies, 69                                        | transferability of bond enthalpies, 69                                        | transferability of bond enthalpies, 69                                        | transferability of bond enthalpies, 69                                        | transferability of bond enthalpies, 69                                        | transferability of bond enthalpies, 69                                        | transferability of bond enthalpies, 69                                        | transferability of bond enthalpies, 69                                        | transferability of bond enthalpies, 69                                        | transferability of bond enthalpies, 69                                        | transferability of bond enthalpies, 69                                        | transferability of bond enthalpies, 69                                        | transferability of bond enthalpies, 69                                        |
| molecules, 60 t                                                                                                                 | bond energy, concept, 8                                                       | bond energy, concept, 8                                                       | bond energy, concept, 8                                                       | bond energy, concept, 8                                                       | bond energy, concept, 8                                                       | bond energy, concept, 8                                                       | bond energy, concept, 8                                                       | bond energy, concept, 8                                                       | bond energy, concept, 8                                                       | bond energy, concept, 8                                                       | bond energy, concept, 8                                                       | bond energy, concept, 8                                                       | bond energy, concept, 8                                                       |
| bond dissociation enthalpies                                                                                                    | bond enthalpy contribution                                                    | bond enthalpy contribution                                                    | bond enthalpy contribution                                                    | bond enthalpy contribution                                                    | bond enthalpy contribution                                                    | bond enthalpy contribution                                                    | bond enthalpy contribution                                                    | bond enthalpy contribution                                                    | bond enthalpy contribution                                                    | bond enthalpy contribution                                                    | bond enthalpy contribution                                                    | bond enthalpy contribution                                                    | bond enthalpy contribution                                                    |
| cyclic voltammetry methodology for organic compounds, 242-243                                                                   | estimating Cr-C 6 H 6 , in Cr(CO) 3 (C 6 H 6 ), 71, 72 f                      | estimating Cr-C 6 H 6 , in Cr(CO) 3 (C 6 H 6 ), 71, 72 f                      | estimating Cr-C 6 H 6 , in Cr(CO) 3 (C 6 H 6 ), 71, 72 f                      | estimating Cr-C 6 H 6 , in Cr(CO) 3 (C 6 H 6 ), 71, 72 f                      | estimating Cr-C 6 H 6 , in Cr(CO) 3 (C 6 H 6 ), 71, 72 f                      | estimating Cr-C 6 H 6 , in Cr(CO) 3 (C 6 H 6 ), 71, 72 f                      | estimating Cr-C 6 H 6 , in Cr(CO) 3 (C 6 H 6 ), 71, 72 f                      | estimating Cr-C 6 H 6 , in Cr(CO) 3 (C 6 H 6 ), 71, 72 f                      | estimating Cr-C 6 H 6 , in Cr(CO) 3 (C 6 H 6 ), 71, 72 f                      | estimating Cr-C 6 H 6 , in Cr(CO) 3 (C 6 H 6 ), 71, 72 f                      | estimating Cr-C 6 H 6 , in Cr(CO) 3 (C 6 H 6 ), 71, 72 f                      | estimating Cr-C 6 H 6 , in Cr(CO) 3 (C 6 H 6 ), 71, 72 f                      | estimating Cr-C 6 H 6 , in Cr(CO) 3 (C 6 H 6 ), 71, 72 f                      |
| or homolytic,                                                                                                                   |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |
| heterolytic 229                                                                                                                 | bond enthalpy contributions bonding energetics, 68-69                         | bond enthalpy contributions bonding energetics, 68-69                         | bond enthalpy contributions bonding energetics, 68-69                         | bond enthalpy contributions bonding energetics, 68-69                         | bond enthalpy contributions bonding energetics, 68-69                         | bond enthalpy contributions bonding energetics, 68-69                         | bond enthalpy contributions bonding energetics, 68-69                         | bond enthalpy contributions bonding energetics, 68-69                         | bond enthalpy contributions bonding energetics, 68-69                         | bond enthalpy contributions bonding energetics, 68-69                         | bond enthalpy contributions bonding energetics, 68-69                         | bond enthalpy contributions bonding energetics, 68-69                         | bond enthalpy contributions bonding energetics, 68-69                         |
| solution and gas-phase R-H, 240-241                                                                                             |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |
| solution phase, 64                                                                                                              | chromium-benzene, 68                                                          | chromium-benzene, 68                                                          | chromium-benzene, 68                                                          | chromium-benzene, 68                                                          | chromium-benzene, 68                                                          | chromium-benzene, 68                                                          | chromium-benzene, 68                                                          | chromium-benzene, 68                                                          | chromium-benzene, 68                                                          | chromium-benzene, 68                                                          | chromium-benzene, 68                                                          | chromium-benzene, 68                                                          | chromium-benzene, 68                                                          |
| transition metal-ligand, by differential                                                                                        |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |
| scanning calorimetry, 183-185                                                                                                   | transferability, 69                                                           | transferability, 69                                                           | transferability, 69                                                           | transferability, 69                                                           | transferability, 69                                                           | transferability, 69                                                           | transferability, 69                                                           | transferability, 69                                                           | transferability, 69                                                           | transferability, 69                                                           | transferability, 69                                                           | transferability, 69                                                           | transferability, 69                                                           |
| bond dissociation enthalpy                                                                                                      | bond lengths, estimating bond enthalpy contributions, 73-74                   | bond lengths, estimating bond enthalpy contributions, 73-74                   | bond lengths, estimating bond enthalpy contributions, 73-74                   | bond lengths, estimating bond enthalpy contributions, 73-74                   | bond lengths, estimating bond enthalpy contributions, 73-74                   | bond lengths, estimating bond enthalpy contributions, 73-74                   | bond lengths, estimating bond enthalpy contributions, 73-74                   | bond lengths, estimating bond enthalpy contributions, 73-74                   | bond lengths, estimating bond enthalpy contributions, 73-74                   | bond lengths, estimating bond enthalpy contributions, 73-74                   | bond lengths, estimating bond enthalpy contributions, 73-74                   | bond lengths, estimating bond enthalpy contributions, 73-74                   | bond lengths, estimating bond enthalpy contributions, 73-74                   |
| ArO-H, of p -monosubstituted phenols, 63 t                                                                                      | bond-snap enthalpies, 70                                                      | bond-snap enthalpies, 70                                                      | bond-snap enthalpies, 70                                                      | bond-snap enthalpies, 70                                                      | bond-snap enthalpies, 70                                                      | bond-snap enthalpies, 70                                                      | bond-snap enthalpies, 70                                                      | bond-snap enthalpies, 70                                                      | bond-snap enthalpies, 70                                                      | bond-snap enthalpies, 70                                                      | bond-snap enthalpies, 70                                                      | bond-snap enthalpies, 70                                                      | bond-snap enthalpies, 70                                                      |
| PhO-H, in solution and gas phase, 62 f                                                                                          | bond strength                                                                 | bond strength                                                                 | bond strength                                                                 | bond strength                                                                 | bond strength                                                                 | bond strength                                                                 | bond strength                                                                 | bond strength                                                                 | bond strength                                                                 | bond strength                                                                 | bond strength                                                                 | bond strength                                                                 | bond strength                                                                 |
| bond dissociation enthalpy balance,                                                                                             | idealized concept, 68                                                         | idealized concept, 68                                                         | idealized concept, 68                                                         | idealized concept, 68                                                         | idealized concept, 68                                                         | idealized concept, 68                                                         | idealized concept, 68                                                         | idealized concept, 68                                                         | idealized concept, 68                                                         | idealized concept, 68                                                         | idealized concept, 68                                                         | idealized concept, 68                                                         | idealized concept, 68                                                         |
| thermochemical cycle, 65 f                                                                                                      | intrinsic, 75                                                                 | intrinsic, 75                                                                 | intrinsic, 75                                                                 | intrinsic, 75                                                                 | intrinsic, 75                                                                 | intrinsic, 75                                                                 | intrinsic, 75                                                                 | intrinsic, 75                                                                 | intrinsic, 75                                                                 | intrinsic, 75                                                                 | intrinsic, 75                                                                 | intrinsic, 75                                                                 | intrinsic, 75                                                                 |
| bond energies adjusting bond enthalpy                                                                                           | burner vessel, flame combustion calorimetry, 116-117                          | burner vessel, flame combustion calorimetry, 116-117                          | burner vessel, flame combustion calorimetry, 116-117                          | burner vessel, flame combustion calorimetry, 116-117                          | burner vessel, flame combustion calorimetry, 116-117                          | burner vessel, flame combustion calorimetry, 116-117                          | burner vessel, flame combustion calorimetry, 116-117                          | burner vessel, flame combustion calorimetry, 116-117                          | burner vessel, flame combustion calorimetry, 116-117                          | burner vessel, flame combustion calorimetry, 116-117                          | burner vessel, flame combustion calorimetry, 116-117                          | burner vessel, flame combustion calorimetry, 116-117                          | burner vessel, flame combustion calorimetry, 116-117                          |
| contributions with                                                                                                              |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |
| bond lengths and angles, 73-74                                                                                                  |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |
| ArO-H bond dissociation enthalpies of                                                                                           | cage effects Koenig, Hay, and Finke's model, 45-46 reaction kinetics, 45      | cage effects Koenig, Hay, and Finke's model, 45-46 reaction kinetics, 45      | cage effects Koenig, Hay, and Finke's model, 45-46 reaction kinetics, 45      | cage effects Koenig, Hay, and Finke's model, 45-46 reaction kinetics, 45      | cage effects Koenig, Hay, and Finke's model, 45-46 reaction kinetics, 45      | cage effects Koenig, Hay, and Finke's model, 45-46 reaction kinetics, 45      | cage effects Koenig, Hay, and Finke's model, 45-46 reaction kinetics, 45      | cage effects Koenig, Hay, and Finke's model, 45-46 reaction kinetics, 45      | cage effects Koenig, Hay, and Finke's model, 45-46 reaction kinetics, 45      | cage effects Koenig, Hay, and Finke's model, 45-46 reaction kinetics, 45      | cage effects Koenig, Hay, and Finke's model, 45-46 reaction kinetics, 45      | cage effects Koenig, Hay, and Finke's model, 45-46 reaction kinetics, 45      | cage effects Koenig, Hay, and Finke's model, 45-46 reaction kinetics, 45      |
| benzene, 63 t bond dissociation enthalpies and energies, 58-64                                                                  | calorific value                                                               | calorific value                                                               | calorific value                                                               | calorific value                                                               | calorific value                                                               | calorific value                                                               | calorific value                                                               | calorific value                                                               | calorific value                                                               | calorific value                                                               | calorific value                                                               | calorific value                                                               | calorific value                                                               |
| bond dissociation enthalpy balance, 65 f                                                                                        | definition, 21                                                                | definition, 21                                                                | definition, 21                                                                | definition, 21                                                                | definition, 21                                                                | definition, 21                                                                | definition, 21                                                                | definition, 21                                                                | definition, 21                                                                | definition, 21                                                                | definition, 21                                                                | definition, 21                                                                | definition, 21                                                                |
| bond enthalpy contributions and bond strengths, 68-74                                                                           | inferior, 21 superior, 21                                                     | inferior, 21 superior, 21                                                     | inferior, 21 superior, 21                                                     | inferior, 21 superior, 21                                                     | inferior, 21 superior, 21                                                     | inferior, 21 superior, 21                                                     | inferior, 21 superior, 21                                                     | inferior, 21 superior, 21                                                     | inferior, 21 superior, 21                                                     | inferior, 21 superior, 21                                                     | inferior, 21 superior, 21                                                     | inferior, 21 superior, 21                                                     | inferior, 21 superior, 21                                                     |
| bond enthalpy terms, 68                                                                                                         | proper                                                                        | proper                                                                        | proper                                                                        | proper                                                                        | proper                                                                        | proper                                                                        | proper                                                                        | proper                                                                        | proper                                                                        | proper                                                                        | proper                                                                        | proper                                                                        | proper                                                                        |
| bond-snap enthalpies, 70                                                                                                        | heart of calorimeter, 83, 84                                                  | heart of calorimeter, 83, 84                                                  | heart of calorimeter, 83, 84                                                  | heart of calorimeter, 83, 84                                                  | heart of calorimeter, 83, 84                                                  | heart of calorimeter, 83, 84                                                  | heart of calorimeter, 83, 84                                                  | heart of calorimeter, 83, 84                                                  | heart of calorimeter, 83, 84                                                  | heart of calorimeter, 83, 84                                                  | heart of calorimeter, 83, 84                                                  | heart of calorimeter, 83, 84                                                  | heart of calorimeter, 83, 84                                                  |
| bond strength, 68                                                                                                               | f rate of temperature change of, for titration                                | f rate of temperature change of, for titration                                | f rate of temperature change of, for titration                                | f rate of temperature change of, for titration                                | f rate of temperature change of, for titration                                | f rate of temperature change of, for titration                                | f rate of temperature change of, for titration                                | f rate of temperature change of, for titration                                | f rate of temperature change of, for titration                                | f rate of temperature change of, for titration                                | f rate of temperature change of, for titration                                | f rate of temperature change of, for titration                                | f rate of temperature change of, for titration                                |
| chromium hexacarbonyl stepwise                                                                                                  | calorimetry, 161                                                              | calorimetry, 161                                                              | calorimetry, 161                                                              | calorimetry, 161                                                              | calorimetry, 161                                                              | calorimetry, 161                                                              | calorimetry, 161                                                              | calorimetry, 161                                                              | calorimetry, 161                                                              | calorimetry, 161                                                              | calorimetry, 161                                                              | calorimetry, 161                                                              | calorimetry, 161                                                              |
| bond dissociation enthalpies, 65-67                                                                                             | classes, 83, 85 f                                                             | classes, 83, 85 f                                                             | classes, 83, 85 f                                                             | classes, 83, 85 f                                                             | classes, 83, 85 f                                                             | classes, 83, 85 f                                                             | classes, 83, 85 f                                                             | classes, 83, 85 f                                                             | classes, 83, 85 f                                                             | classes, 83, 85 f                                                             | classes, 83, 85 f                                                             | classes, 83, 85 f                                                             | classes, 83, 85 f                                                             |
| Cr-C 6 H 6 bond enthalpy contribution Cr(CO) (C H ), 72 f                                                                       | Calvet, heat flow calorimeter design, carbenium ion, resonance-stabilized, by | Calvet, heat flow calorimeter design, carbenium ion, resonance-stabilized, by | Calvet, heat flow calorimeter design, carbenium ion, resonance-stabilized, by | Calvet, heat flow calorimeter design, carbenium ion, resonance-stabilized, by | Calvet, heat flow calorimeter design, carbenium ion, resonance-stabilized, by | Calvet, heat flow calorimeter design, carbenium ion, resonance-stabilized, by | Calvet, heat flow calorimeter design, carbenium ion, resonance-stabilized, by | Calvet, heat flow calorimeter design, carbenium ion, resonance-stabilized, by | Calvet, heat flow calorimeter design, carbenium ion, resonance-stabilized, by | Calvet, heat flow calorimeter design, carbenium ion, resonance-stabilized, by | Calvet, heat flow calorimeter design, carbenium ion, resonance-stabilized, by | Calvet, heat flow calorimeter design, carbenium ion, resonance-stabilized, by | Calvet, heat flow calorimeter design, carbenium ion, resonance-stabilized, by |
| in 3 6 6                                                                                                                        | 139-140                                                                       | 139-140                                                                       | 139-140                                                                       | 139-140                                                                       | 139-140                                                                       | 139-140                                                                       | 139-140                                                                       | 139-140                                                                       | 139-140                                                                       | 139-140                                                                       | 139-140                                                                       | 139-140                                                                       | 139-140                                                                       |
| density functional theory, 70 dissociation of O-H bonds in phenol ethanol, 69, 70 f                                             | titration calorimetry, 166 carbon, enthalpy of sublimation, 74                | titration calorimetry, 166 carbon, enthalpy of sublimation, 74                | titration calorimetry, 166 carbon, enthalpy of sublimation, 74                | titration calorimetry, 166 carbon, enthalpy of sublimation, 74                | titration calorimetry, 166 carbon, enthalpy of sublimation, 74                | titration calorimetry, 166 carbon, enthalpy of sublimation, 74                | titration calorimetry, 166 carbon, enthalpy of sublimation, 74                | titration calorimetry, 166 carbon, enthalpy of sublimation, 74                | titration calorimetry, 166 carbon, enthalpy of sublimation, 74                | titration calorimetry, 166 carbon, enthalpy of sublimation, 74                | titration calorimetry, 166 carbon, enthalpy of sublimation, 74                | titration calorimetry, 166 carbon, enthalpy of sublimation, 74                | titration calorimetry, 166 carbon, enthalpy of sublimation, 74                |
| and                                                                                                                             | monoxide, flame combustion calorimetry, 115                                   | monoxide, flame combustion calorimetry, 115                                   | monoxide, flame combustion calorimetry, 115                                   | monoxide, flame combustion calorimetry, 115                                   | monoxide, flame combustion calorimetry, 115                                   | monoxide, flame combustion calorimetry, 115                                   | monoxide, flame combustion calorimetry, 115                                   | monoxide, flame combustion calorimetry, 115                                   | monoxide, flame combustion calorimetry, 115                                   | monoxide, flame combustion calorimetry, 115                                   | monoxide, flame combustion calorimetry, 115                                   | monoxide, flame combustion calorimetry, 115                                   | monoxide, flame combustion calorimetry, 115                                   |
| energy to cleave chemical bonds, 58                                                                                             |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |
| E s as intrinsic bond strengths, 69, 71 estimating derivation for E s (Cr-C 6 H 6 ),                                            | cell potential, electrical potential difference between electrodes, 229       | cell potential, electrical potential difference between electrodes, 229       | cell potential, electrical potential difference between electrodes, 229       | cell potential, electrical potential difference between electrodes, 229       | cell potential, electrical potential difference between electrodes, 229       | cell potential, electrical potential difference between electrodes, 229       | cell potential, electrical potential difference between electrodes, 229       | cell potential, electrical potential difference between electrodes, 229       | cell potential, electrical potential difference between electrodes, 229       | cell potential, electrical potential difference between electrodes, 229       | cell potential, electrical potential difference between electrodes, 229       | cell potential, electrical potential difference between electrodes, 229       | cell potential, electrical potential difference between electrodes, 229       |
| Laidler terms, 74-75                                                                                                            | chemical bonds, bond energies, chemical calibration, iodine                   | chemical bonds, bond energies, chemical calibration, iodine                   | chemical bonds, bond energies, chemical calibration, iodine                   | chemical bonds, bond energies, chemical calibration, iodine                   | chemical bonds, bond energies, chemical calibration, iodine                   | chemical bonds, bond energies, chemical calibration, iodine                   | chemical bonds, bond energies, chemical calibration, iodine                   | chemical bonds, bond energies, chemical calibration, iodine                   | chemical bonds, bond energies, chemical calibration, iodine                   | chemical bonds, bond energies, chemical calibration, iodine                   | chemical bonds, bond energies, chemical calibration, iodine                   | chemical bonds, bond energies, chemical calibration, iodine                   | chemical bonds, bond energies, chemical calibration, iodine                   |
| mean bond disruption enthalpy, 66                                                                                               | 58                                                                            | 58                                                                            | 58                                                                            | 58                                                                            | 58                                                                            | 58                                                                            | 58                                                                            | 58                                                                            | 58                                                                            | 58                                                                            | 58                                                                            | 58                                                                            | 58                                                                            |
|                                                                                                                                 | sublimation                                                                   | sublimation                                                                   | sublimation                                                                   | sublimation                                                                   | sublimation                                                                   | sublimation                                                                   | sublimation                                                                   | sublimation                                                                   | sublimation                                                                   | sublimation                                                                   | sublimation                                                                   | sublimation                                                                   | sublimation                                                                   |
|                                                                                                                                 | thermogram, 143, 144 f                                                        | thermogram, 143, 144 f                                                        | thermogram, 143, 144 f                                                        | thermogram, 143, 144 f                                                        | thermogram, 143, 144 f                                                        | thermogram, 143, 144 f                                                        | thermogram, 143, 144 f                                                        | thermogram, 143, 144 f                                                        | thermogram, 143, 144 f                                                        | thermogram, 143, 144 f                                                        | thermogram, 143, 144 f                                                        | thermogram, 143, 144 f                                                        | thermogram, 143, 144 f                                                        |
| bond dissociation enthalpy,                                                                                                     |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |
| mean                                                                                                                            |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |
| 66                                                                                                                              |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |
|                                                                                                                                 | carbon                                                                        | carbon                                                                        | carbon                                                                        | carbon                                                                        | carbon                                                                        | carbon                                                                        | carbon                                                                        | carbon                                                                        | carbon                                                                        | carbon                                                                        | carbon                                                                        | carbon                                                                        | carbon                                                                        |
|                                                                                                                                 | calorimeters,                                                                 | calorimeters,                                                                 | calorimeters,                                                                 | calorimeters,                                                                 | calorimeters,                                                                 | calorimeters,                                                                 | calorimeters,                                                                 | calorimeters,                                                                 | calorimeters,                                                                 | calorimeters,                                                                 | calorimeters,                                                                 | calorimeters,                                                                 | calorimeters,                                                                 |
|                                                                                                                                 | calorimeter                                                                   | calorimeter                                                                   | calorimeter                                                                   | calorimeter                                                                   | calorimeter                                                                   | calorimeter                                                                   | calorimeter                                                                   | calorimeter                                                                   | calorimeter                                                                   | calorimeter                                                                   | calorimeter                                                                   | calorimeter                                                                   | calorimeter                                                                   |
|                                                                                                                                 | 73                                                                            | 73                                                                            | 73                                                                            | 73                                                                            | 73                                                                            | 73                                                                            | 73                                                                            | 73                                                                            | 73                                                                            | 73                                                                            | 73                                                                            | 73                                                                            | 73                                                                            |

## Index

| chromium hexacarbonyl stepwise bond dissociation enthalpies, 65-67 thermal decomposition by heat flow calorimetry, 144-146 chromium-ligand bonds, enthalpy of disruption, 68 Clausius-Clapeyron equation, enthalpy of vaporization, 23 cleavage reactions, R-X bond, 227-228 CODATA Key Values for Thermodynamics , 17 coefficient of thermal expansion, enthalpy of liquid ethanol, 24 combustion calorimeters conventional, 87 flame, in oxygen, 114-120 moving-bomb, in oxygen, 108-114 static-bomb, in oxygen, 87-108 combustion calorimetry fluorine, 120-124 reaction in closed vessel, 84 reduction to standard states, 97 f combustion enthalpy, anthracene, 16-17   | kinetic potential shift, 238 outer Helmholtz plane (OHP), 234 potential waveform, 231, 232 f qualitative understanding of voltammogram, 236-237 reference electrode, 232 relation of standard electrode potentials and p K a to bond dissociation Gibbs energy, 239 f reversibility criteria, 237 reversible oxidation of species R - to R, 233-235 R-H bond dissociation enthalpy in gas, 240, 241 R-H bond dissociation enthalpy in solution, 240, 241 Stern model of double layer, 234 supporting electrolyte, 235 switching potential, 231 three-electrode electrochemical cell, 232 f working electrode, 231, 232 cylinder-type heat flux, differential scanning   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| analysis, 238-240 concentrations equilibrium constants proportional to molalities, 207-208 rate constants for reaction in solution, 219 consistency, 16, 17 coordination compounds, photocalorimeter, 151 crucibles, differential scanning calorimetry, 174, 175 current intensity, cyclic voltammetry, 236 4-cyanopyridine N -oxide combustion, 98-99, 100 t , 101 t combustion data, 107 t mass balance of combustion, 100 t uncertainties, 105-106, 108 cyclic voltammetry (CV) anodic and cathodic parameters, 237 auxiliary electrode, 232                                                                                                                              | deconvolution algorithms, photoacoustic calorimetry, 204-206 density functional theory (B3LYP/cc-pVTZ) bond-snap enthalpies, 70 reorganization energy, 75 derivative cyclic voltammetry (DCV), 238-239 Dewar vessel isoperibol reaction-solution calorimetry, 125, 126 f isoperibol titration calorimetry apparatus, 157 f diethyl ether, flame combustion calorimetry, 115 differential ebulliometry vapor pressure, 22-23 vapor pressure of ethanol, 23 f                                                                                                                                                                                                             |

| differential scanning calorimetry (DSC)                                         | electromotive force (emf), cell, 229                                  |
|---------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| ( continued )                                                                   | electron affinity                                                     |
| interconversion of benzene valence isomer                                       | ionization energy and, 47-49                                          |
| derivatives, 186                                                                | potential energy curves, 49, 50 f                                     |
| interpolated baseline, 176                                                      | electron convention, 48, 49                                           |
| isothermal method, 175, 187-189                                                 | t electron FD (Fermi-Dirac) convention, 49,                           |
| operational temperature ranges, 174                                             | 52, 54                                                                |
| power compensation DSC, 172-173                                                 | endothermic process                                                   |
| programmed temperature line, 176                                                | differential scanning calorimetry (DSC) by                            |
| sample in sealed capsule, 85                                                    | isothermal method, 188 f                                              |
| scheme of disk-type heat flux DSC, 172 f                                        | ideal DSC curve, 176 f                                                |
| scheme of ideal DSC curve for endothermic                                       | temperature-time curve for isoperibol                                 |
| process, 176 f                                                                  | reaction-solution calorimetry                                         |
| scheme of temperature gradient along sample                                     | calibration, 128 f , 130 f                                            |
| cell, 177 f                                                                     | energetics of metal-ligand complexation                               |
| standard state corrections, 179                                                 | heat flow vs. isoperibol calorimetry, 169-170                         |
| temperature-modulated DSC                                                       | titration calorimetry study, 170 t                                    |
| (TMDSC), 174                                                                    | energy balance                                                        |
| term, 171                                                                       | photoacoustic calorimetry, 194                                        |
| thermochemistry of organic molecules,                                           | photocalorimetry, 147-148                                             |
| 186-187                                                                         | energy content, Einstein' s E = mc 2 , 10                             |
| transition metal-ligand bond dissociation                                       | energy equivalents                                                    |
| enthalpies, 183-185                                                             | isoperibol reaction-solution calorimetry,                             |
| true overall heat flow rate into sample cell,                                   | 127-128, 133                                                          |
| 179-181 user-friendly instruments, 171-172                                      | titration calorimetry, 159-160                                        |
| zero line, 176                                                                  | energy for ignition, /Delta1 U ign , 93 of combustion, benzoic for    |
|                                                                                 | energy acid                                                           |
| differential thermal analysis (DTA), 171 2,2-diphenyl-1-picrylhydrazyl radical, | standardizing laboratory, 94-96 enthalpies of reaction                |
| radical                                                                         |                                                                       |
| trap, 220 f                                                                     | activation parameters for forward and reverse                         |
| disk-type heat flux, differential scanning calorimetry, 172                     | reaction, 219 relative values from                                    |
| disruption enthalpy, chromium-ligand bonds, 68                                  | single-temperature equilibrium constants, 217                         |
| dissociation energy, symbols, 8                                                 | enthalpies of reactions                                               |
| drop calorimetry method                                                         | definition, 9                                                         |
| heat flow calorimetry, 146                                                      | isoperibol continuous titration calorimetry,                          |
| reaction vessel for drop technique, 142 f                                       | 163-166 in solution,                                                  |
| dynamic calorimeter, eliminating bomb rotation corrections, 111                 | titration calorimetry for, 156 enthalpy                               |
| dynamic method, 175. See also differential                                      | pressure correction, 15 standard bond dissociation symbol, 8          |
| scanning calorimetry (DSC)                                                      | state function, 10-11 symbol H , 8                                    |
| ebulliometry                                                                    | enthalpy change                                                       |
| vapor pressure, 22-23                                                           | calorimetric process under isothermal                                 |
| vapor pressure of ethanol, 23 f Einstein relationship, E mc 2 ,                 | conditions, 125-127, 129 isoperibol continuous titration calorimetry, |
| = 10 electrical calibration, combustion calorimeter,                            | 159-162                                                               |
|                                                                                 | of atomization,                                                       |
| 94, 95-97                                                                       |                                                                       |
| electrochemical                                                                 | enthalpy phenol, 74 enthalpy of formation, solid f                    |
| cell, cyclic voltammetry, 231, 232 f                                            | alkoxide, 27, 28 enthalpy of protonation, basicity of                 |
| electrochemistry, and thermodynamics,                                           | organometallic complexes, 165-166 in                                  |
| 229-231 radiation,                                                              | enthalpy of solution, lithium chloride water, 29-30                   |
| electromagnetic                                                                 | 74                                                                    |
|                                                                                 | of sublimation,                                                       |
| 147                                                                             |                                                                       |
| photocalorimetry,                                                               | enthalpy carbon,                                                      |

## Index

| enthalpy of vaporization                                                    |                                                                                                                                                       |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Clausius-Clapeyron equation, 23 correction, 24-25 standard, 22, 23-25       | ethanol calculation of compressibility factors, 24 flame combustion calorimetry, 115 hypothetical thermochemical cycle, 69, 70 f O-H bond lengths, 69 |
| enthalpy profile, unimolecular reaction in                                  |                                                                                                                                                       |
| solution, 45 f                                                              | pressure effect of liquid, on enthalpy, 24                                                                                                            |
| entropy, symbol S , 8                                                       | standard enthalpy of formation, 17                                                                                                                    |
| equilibrium constants                                                       | standard states, 18-19                                                                                                                                |
| activity based, 34, 207                                                     | vapor pressures by ebulliometry, 23 f                                                                                                                 |
| concentrations proportional to molalities,                                  | ethyl cation                                                                                                                                          |
| 207-208                                                                     | appearance energy, 54-55                                                                                                                              |
| isoperibol continuous titration calorimetry,                                | standard enthalpy of formation, 49 t                                                                                                                  |
| 163-166                                                                     | exergonic reactions, Gibbs energy, 31                                                                                                                 |
| molality K m , 35, 207                                                      | exothermic process                                                                                                                                    |
| relative reaction enthalpies from                                           | temperature-time curve for isoperibol                                                                                                                 |
| single-temperature, 217                                                     | continuous titration calorimetry, 158 f                                                                                                               |
| solute concentration K c , 34-35                                            | temperature-time curve for isoperibol                                                                                                                 |
| solution reactions K ‡ , 43, 44                                             | reaction-solution calorimetry                                                                                                                         |
|                                                                             | 130                                                                                                                                                   |
| standard redox potentials, 231                                              | calibration, 128 f , f                                                                                                                                |
| equilibrium in solution                                                     | experimental bomb process, internal energy                                                                                                            |
| complications in second law method,                                         | change calculation, 93 f                                                                                                                              |
| 212-213, 215-216                                                            | extrapolated onset temperature, differential                                                                                                          |
| determination of [H2] difficulties, 211-212                                 | scanning calorimetry, 176 f , 177 Eyring plot                                                                                                         |
| energetics of hydrogen bond between phenol and acetonitrile, 208-209, 210 f | benzoyl peroxide decomposition, 221 f                                                                                                                 |
| equilibrium concentrations of Rh 2 (CO) 8 and                               | equation, 219                                                                                                                                         |
| Rh 4 (CO) 12 , 213-215                                                      | kinetic analysis, 40, 44                                                                                                                              |
| equilibrium constants, 207-208                                              | titanium complexes, 224                                                                                                                               |
| fugacities as correction parameters,                                        | f                                                                                                                                                     |
| 213, 214-215                                                                |                                                                                                                                                       |
| Henry's law, 214                                                            | Fermi-Dirac (FD), electron FD convention, 49,                                                                                                         |
| Henry's law and H 2 in two phases, 211                                      | 52, 54                                                                                                                                                |
| hydrogen transfer between two substituted                                   | ferrocenium/ferrocene, reference couple,                                                                                                              |
| phenols, 216-217                                                            | 241, 242 f                                                                                                                                            |
| Lambert-Beer law, 209                                                       | first law method, Gibbs energy, 31                                                                                                                    |
| phenolic compounds for equilibrium                                          | first-row hydrides, stepwise bond dissociation                                                                                                        |
| studies, 216 f                                                              | enthalpies, 67 f                                                                                                                                      |
| reaction enthalpy reflecting Sc-H and dissociation enthalpies,              | flame combustion calorimetry rise, 117                                                                                                                |
| Sc-Ph bond 210-211                                                          | adiabatic temperature                                                                                                                                 |
| relative values of reaction enthalpies,                                     | burner vessel, 116-117 combustion of hydrogen in excess of                                                                                            |
| 217 Ru(Cp ∗ )(PMe 3 ) 2 X complexes, 217 f                                  | oxygen, 116                                                                                                                                           |
| σ bond metathesis reaction, 210-213                                         | enthalpies of combustion of gases and                                                                                                                 |
| scandium-hydrogen (Sc-H) bond to Sc-C                                       | vaporized liquids, 114 water,                                                                                                                         |
| bond, 210-213                                                               | enthalpy of formation of liquid                                                                                                                       |
| structure of                                                                | 115-120                                                                                                                                               |
| bis (pentamethylcyclopentadienyl)                                           | enthalpy of reaction at reference temperature,                                                                                                        |
| scandium complex, 211 f                                                     | 117-119                                                                                                                                               |
| van't Hoff plot for reaction enthalpy and                                   | ignition enthalpy, 118 combustion calorimeter                                                                                                         |
| entropy, 208 van't Hoff plot for bond metathesis reaction,                  | isoperibol flame by Rossini, 116 f                                                                                                                    |
| 213 f                                                                       | in oxygen, 114-120                                                                                                                                    |
| ethane                                                                      | quantitative analysis of products, 115                                                                                                                |
| standard enthalpy of formation, 49 t                                        | Rossini apparatus, 115, 116 f                                                                                                                         |
| energy, 60                                                                  | reaction, 119                                                                                                                                         |
| upper limits of bond dissociation                                           | standard enthalpy of                                                                                                                                  |

| fluorine combustion calorimetry auxiliary apparatus, 122-123 combustion chamber and primary vessel, 124 f differences from oxygen combustion calorimetry, 121 experimental method, 123-124 hypergolic substances, 122 modern bomb calorimetry, 120 sample isolation from fluorine prior to reaction, 121-122   | enthalpy and entropy, 32, 33 equilibrium constant based on concentration ( K c ) , 34-35   | enthalpy and entropy, 32, 33 equilibrium constant based on concentration ( K c ) , 34-35   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| solution                                                                                                                                                                                                                                                                                                       |                                                                                            |                                                                                            |
|                                                                                                                                                                                                                                                                                                                | equilibrium constant based on molality ( K m ) , 35                                        | equilibrium constant based on molality ( K m ) , 35                                        |
|                                                                                                                                                                                                                                                                                                                | equilibrium constant in terms of activities                                                | equilibrium constant in terms of activities                                                |
|                                                                                                                                                                                                                                                                                                                | ( K ) , 34                                                                                 | ( K ) , 34                                                                                 |
|                                                                                                                                                                                                                                                                                                                | error bar, 31, 32 f                                                                        | error bar, 31, 32 f                                                                        |
|                                                                                                                                                                                                                                                                                                                | exergonic reactions, 31                                                                    | exergonic reactions, 31                                                                    |
|                                                                                                                                                                                                                                                                                                                | first law method, 31                                                                       | first law method, 31                                                                       |
|                                                                                                                                                                                                                                                                                                                | fugacity concept, 34                                                                       | fugacity concept, 34                                                                       |
| scheme of two-chamber bomb for, 121 f                                                                                                                                                                                                                                                                          | fugacity of pure substance, 36                                                             | fugacity of pure substance, 36                                                             |
| similarity to oxygen bomb calorimetry,                                                                                                                                                                                                                                                                         | general relationship between K c and                                                       | general relationship between K c and                                                       |
| 120-121                                                                                                                                                                                                                                                                                                        | half-reactions, 229                                                                        | half-reactions, 229                                                                        |
| special handling of fluorine, 123                                                                                                                                                                                                                                                                              | heterolytic or homolytic bond                                                              | heterolytic or homolytic bond                                                              |
| sulfur use, 122                                                                                                                                                                                                                                                                                                | dissociation, 229                                                                          | dissociation, 229                                                                          |
| tungsten inducing complete combustion, 122                                                                                                                                                                                                                                                                     | reaction based on activities, 230                                                          | reaction based on activities, 230                                                          |
| formal potential, 235                                                                                                                                                                                                                                                                                          | redox couples, 230                                                                         | redox couples, 230                                                                         |
| free radical production                                                                                                                                                                                                                                                                                        | second law methods, 31                                                                     | second law methods, 31                                                                     |
| photoacoustic calorimetry (PAC), 203                                                                                                                                                                                                                                                                           | symbol G , 8                                                                               | symbol G , 8                                                                               |
|                                                                                                                                                                                                                                                                                                                | thermochemical                                                                             | thermochemical                                                                             |
| photomodulation voltammetry (PV), 244 fugacity                                                                                                                                                                                                                                                                 | third law method, 36-37                                                                    | third law method, 36-37                                                                    |
|                                                                                                                                                                                                                                                                                                                | cycle, 239, 240                                                                            | cycle, 239, 240                                                                            |
| carbon monoxide at experimental temperature and pressure, 214                                                                                                                                                                                                                                                  | uncertainty, 31, 32 f                                                                      | uncertainty, 31, 32 f                                                                      |
| 34                                                                                                                                                                                                                                                                                                             |                                                                                            |                                                                                            |
|                                                                                                                                                                                                                                                                                                                | van't Hoff equation,                                                                       | van't Hoff equation,                                                                       |
| concept,                                                                                                                                                                                                                                                                                                       | 32                                                                                         | 32                                                                                         |
| pure substance, 36 reactants and products, 36                                                                                                                                                                                                                                                                  | halogenated products, organohalogen combustion, 108 t combustion                           | halogenated products, organohalogen combustion, 108 t combustion                           |
|                                                                                                                                                                                                                                                                                                                | halogen atmospheres,                                                                       | halogen atmospheres,                                                                       |
| fusion, standard enthalpy, 22                                                                                                                                                                                                                                                                                  |                                                                                            |                                                                                            |
| gas-phase acidity, molecular energetics, 55-57 basicity, molecular energetics, 55-57                                                                                                                                                                                                                           | heat capacity differential scanning calorimetry, 182-183                                   | heat capacity differential scanning calorimetry, 182-183                                   |
| gas-phase 45                                                                                                                                                                                                                                                                                                   | 181, Kirchhoff equation for standard                                                       | 181, Kirchhoff equation for standard                                                       |
| gas-phase chemistry, solution chemistry vs., gas-phase energetics                                                                                                                                                                                                                                              | partial molar, 13                                                                          | partial molar, 13                                                                          |
| acidity, 55-57                                                                                                                                                                                                                                                                                                 | reaction, symbol C p , 8                                                                   | reaction, symbol C p , 8                                                                   |
| appearance energy,                                                                                                                                                                                                                                                                                             | temperature dependence, 13                                                                 | temperature dependence, 13                                                                 |
| 50-55 basicity, 55-57                                                                                                                                                                                                                                                                                          | conduction, calorimeter                                                                    | conduction, calorimeter                                                                    |
| electron affinity, 47-49                                                                                                                                                                                                                                                                                       | heat class, 83, 85 heat flow calorimetry. See also titration                               | heat class, 83, 85 heat flow calorimetry. See also titration                               |
| ionization energy, 47-49                                                                                                                                                                                                                                                                                       | calorimetry                                                                                | calorimetry                                                                                |
| proton affinity, 55-57                                                                                                                                                                                                                                                                                         | advantages of Calvet' s design, 140                                                        | advantages of Calvet' s design, 140                                                        |
| gas-phase reactions                                                                                                                                                                                                                                                                                            | block diagram of heat flux                                                                 | block diagram of heat flux                                                                 |
| A-B bond dissociation enthalpy, 58 experimental data for PhO-H                                                                                                                                                                                                                                                 | microcalorimeter, 141 f Calvet' s instrument, 139-140                                      | microcalorimeter, 141 f Calvet' s instrument, 139-140                                      |
| bond dissociation enthalpy, 62 f                                                                                                                                                                                                                                                                               | chemical calibration, 143 146                                                              | chemical calibration, 143 146                                                              |
|                                                                                                                                                                                                                                                                                                                | drop calorimetric method,                                                                  | drop calorimetric method,                                                                  |
| second law method, 35-36 function, reaction, 37                                                                                                                                                                                                                                                                | heat flow rate, 137                                                                        | heat flow rate, 137                                                                        |
| Giauque                                                                                                                                                                                                                                                                                                        | Joule effect, 138                                                                          | Joule effect, 138                                                                          |
| Gibbs energy activities of reactants and products,                                                                                                                                                                                                                                                             | measuring curve,                                                                           | measuring curve,                                                                           |
| 33-34 activity coefficient, 34                                                                                                                                                                                                                                                                                 | 137 microcalorimeter and sensitivity,                                                      | 137 microcalorimeter and sensitivity,                                                      |
| activity concept, 33-34 applying second law method to                                                                                                                                                                                                                                                          | 141-142 Peltier effect, 138 reaction vessel for drop technique, 142 f                      | 141-142 Peltier effect, 138 reaction vessel for drop technique, 142 f                      |
| reactions, 35-36                                                                                                                                                                                                                                                                                               | schematic of Calvet' s calorimeter, 139                                                    | schematic of Calvet' s calorimeter, 139                                                    |
|                                                                                                                                                                                                                                                                                                                | Seebeck effect, 137, 138                                                                   | Seebeck effect, 137, 138                                                                   |
| 'batch'                                                                                                                                                                                                                                                                                                        |                                                                                            |                                                                                            |
| calorimetry,                                                                                                                                                                                                                                                                                                   |                                                                                            |                                                                                            |
| 33                                                                                                                                                                                                                                                                                                             |                                                                                            |                                                                                            |
|                                                                                                                                                                                                                                                                                                                | f                                                                                          | f                                                                                          |
|                                                                                                                                                                                                                                                                                                                | gas-phase                                                                                  | gas-phase                                                                                  |

| sensitivity, 169                                                                                | correction to standard state, 97-105                                                    | correction to standard state, 97-105                                                    | correction to standard state, 97-105                                                    | correction to standard state, 97-105                                                    | correction to standard state, 97-105                                                    |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| standard enthalpy of sublimation of iodine,                                                     | static-bomb combustion, 89                                                              | static-bomb combustion, 89                                                              | static-bomb combustion, 89                                                              | static-bomb combustion, 89                                                              | static-bomb combustion, 89                                                              |
| 143, 144 f                                                                                      | Washburn corrections, 97-105                                                            | Washburn corrections, 97-105                                                            | Washburn corrections, 97-105                                                            | Washburn corrections, 97-105                                                            | Washburn corrections, 97-105                                                            |
| thermal decomposition of bis (butadiene) iron carbonyl, 142-144                                 | International Organization for Standardization (ISO), calorific value of methane, 21-22 | International Organization for Standardization (ISO), calorific value of methane, 21-22 | International Organization for Standardization (ISO), calorific value of methane, 21-22 | International Organization for Standardization (ISO), calorific value of methane, 21-22 | International Organization for Standardization (ISO), calorific value of methane, 21-22 |
| thermal decomposition of chromium                                                               | International System of Units (SI), 7, 267 t , 268 t                                    | International System of Units (SI), 7, 267 t , 268 t                                    | International System of Units (SI), 7, 267 t , 268 t                                    | International System of Units (SI), 7, 267 t , 268 t                                    | International System of Units (SI), 7, 267 t , 268 t                                    |
| hexacarbonyl, 144-146 138 f                                                                     | International Union of Pure and Applied                                                 | International Union of Pure and Applied                                                 | International Union of Pure and Applied                                                 | International Union of Pure and Applied                                                 | International Union of Pure and Applied                                                 |
| thermocouple, 137,                                                                              | Chemistry (IUPAC)                                                                       | Chemistry (IUPAC)                                                                       | Chemistry (IUPAC)                                                                       | Chemistry (IUPAC)                                                                       | Chemistry (IUPAC)                                                                       |
| thermogram, 137 thermopile, 137, 138                                                            | dissociation energy, 59                                                                 | dissociation energy, 59                                                                 | dissociation energy, 59                                                                 | dissociation energy, 59                                                                 | dissociation energy, 59                                                                 |
| f                                                                                               | International Systems of Units (SI), t                                                  | International Systems of Units (SI), t                                                  | International Systems of Units (SI), t                                                  | International Systems of Units (SI), t                                                  | International Systems of Units (SI), t                                                  |
| Tian's instrument, 138-139                                                                      | 267 t , 268                                                                             | 267 t , 268                                                                             | 267 t , 268                                                                             | 267 t , 268                                                                             | 267 t , 268                                                                             |
| titration, 167-170 heat flow rate, true, in                                                     | nomenclature, 7-8                                                                       | nomenclature, 7-8                                                                       | nomenclature, 7-8                                                                       | nomenclature, 7-8                                                                       | nomenclature, 7-8                                                                       |
| differential scanning calorimetry, 179-181                                                      | interpolated baseline, differential scanning calorimetry, 176                           | interpolated baseline, differential scanning calorimetry, 176                           | interpolated baseline, differential scanning calorimetry, 176                           | interpolated baseline, differential scanning calorimetry, 176                           | interpolated baseline, differential scanning calorimetry, 176                           |
| heat flux, differential scanning calorimetry,                                                   | intrinsic volume changes,                                                               | intrinsic volume changes,                                                               | intrinsic volume changes,                                                               | intrinsic volume changes,                                                               | intrinsic volume changes,                                                               |
| 172, 173 f                                                                                      | photoacoustic                                                                           | photoacoustic                                                                           | photoacoustic                                                                           | photoacoustic                                                                           | photoacoustic                                                                           |
| Henry's law, 211,                                                                               | calorimetry, 195                                                                        | calorimetry, 195                                                                        | calorimetry, 195                                                                        | calorimetry, 195                                                                        | calorimetry, 195                                                                        |
| 214                                                                                             | iodine sublimation, calibration thermogram,                                             | iodine sublimation, calibration thermogram,                                             | iodine sublimation, calibration thermogram,                                             | iodine sublimation, calibration thermogram,                                             | iodine sublimation, calibration thermogram,                                             |
| hermetically sealed crucibles, differential                                                     | 143, 144 f                                                                              | 143, 144 f                                                                              | 143, 144 f                                                                              | 143, 144 f                                                                              | 143, 144 f                                                                              |
| scanning calorimetry, 174, 175                                                                  | ion convention, 48, 49                                                                  | ion convention, 48, 49                                                                  | ion convention, 48, 49                                                                  | ion convention, 48, 49                                                                  | ion convention, 48, 49                                                                  |
| Hückel method, estimating bond enthalpy                                                         | t ionic character of solids, lattice energy, 26-27                                      | t ionic character of solids, lattice energy, 26-27                                      | t ionic character of solids, lattice energy, 26-27                                      | t ionic character of solids, lattice energy, 26-27                                      | t ionic character of solids, lattice energy, 26-27                                      |
| contributions, 73                                                                               | ionic solids, lattice enthalpies, 27, 29                                                | ionic solids, lattice enthalpies, 27, 29                                                | ionic solids, lattice enthalpies, 27, 29                                                | ionic solids, lattice enthalpies, 27, 29                                                | ionic solids, lattice enthalpies, 27, 29                                                |
| hydration enthalpy                                                                              | ionization energy                                                                       | ionization energy                                                                       | ionization energy                                                                       | ionization energy                                                                       | ionization energy                                                                       |
| formation of aqueous ions, 30                                                                   | adiabatic, 47                                                                           | adiabatic, 47                                                                           | adiabatic, 47                                                                           | adiabatic, 47                                                                           | adiabatic, 47                                                                           |
| lithium methoxide ions, phase transition, 26                                                    | and electron affinity,                                                                  | and electron affinity,                                                                  | 47-49                                                                                   | and electron affinity,                                                                  | and electron affinity,                                                                  |
| acid, flame                                                                                     | lithium, 27, 28 f                                                                       | lithium, 27, 28 f                                                                       | lithium, 27, 28 f                                                                       | lithium, 27, 28 f                                                                       | lithium, 27, 28 f                                                                       |
| hydrochloric combustion calorimetry, 115                                                        | potential energy curves, 49, 50 f                                                       | potential energy curves, 49, 50 f                                                       | potential energy curves, 49, 50 f                                                       | potential energy curves, 49, 50 f                                                       | potential energy curves, 49, 50 f                                                       |
| hydrogen bromide, upper                                                                         | iR drop, cyclic voltammogram, 237-238                                                   | iR drop, cyclic voltammogram, 237-238                                                   | iR drop, cyclic voltammogram, 237-238                                                   | iR drop, cyclic voltammogram, 237-238                                                   | iR drop, cyclic voltammogram, 237-238                                                   |
| limits of bond dissociation energy, 60 t                                                        | isomerization reaction 3                                                                | isomerization reaction 3                                                                | isomerization reaction 3                                                                | isomerization reaction 3                                                                | isomerization reaction 3                                                                |
| hydrogen peroxide, upper limits of dissociation energy, 60 t                                    | η -coordinated allyl ligand to trans -1-propenyl ligand                                 | η -coordinated allyl ligand to trans -1-propenyl ligand                                 | η -coordinated allyl ligand to trans -1-propenyl ligand                                 | η -coordinated allyl ligand to trans -1-propenyl ligand                                 | η -coordinated allyl ligand to trans -1-propenyl ligand                                 |
| bond                                                                                            | of titanium complexes, 223-224                                                          | of titanium complexes, 223-224                                                          | of titanium complexes, 223-224                                                          | of titanium complexes, 223-224                                                          | of titanium complexes, 223-224                                                          |
| hydrogen transfer, substituted phenols, 216-217 hydroxylic hydrogen abstraction in phenol,      | photochemical, of trans - to cis -azobenzene, 154-155                                   | photochemical, of trans - to cis -azobenzene, 154-155                                   | photochemical, of trans - to cis -azobenzene, 154-155                                   | photochemical, of trans - to cis -azobenzene, 154-155                                   | photochemical, of trans - to cis -azobenzene, 154-155                                   |
| photoacoustic calorimetry, 201, 202 f hypergolic substances, use in fluorine                    | See also titration calorimetry                                                          | See also titration calorimetry                                                          | See also titration calorimetry                                                          | See also titration calorimetry                                                          | See also titration calorimetry                                                          |
| combustions, 122                                                                                | isoperibol. calorimeter class, 83, 84, 85 f continuous titration calorimetry, 158-166   | isoperibol. calorimeter class, 83, 84, 85 f continuous titration calorimetry, 158-166   | isoperibol. calorimeter class, 83, 84, 85 f continuous titration calorimetry, 158-166   | isoperibol. calorimeter class, 83, 84, 85 f continuous titration calorimetry, 158-166   | isoperibol. calorimeter class, 83, 84, 85 f continuous titration calorimetry, 158-166   |
|                                                                                                 | macro rotating-bomb combustion calorimeter, 109 f                                       | macro rotating-bomb combustion calorimeter, 109 f                                       | macro rotating-bomb combustion calorimeter, 109 f                                       | macro rotating-bomb combustion calorimeter, 109 f                                       | macro rotating-bomb combustion calorimeter, 109 f                                       |
| ideal solution, standard chemical potential of solute i, 34 ignition enthalpy, flame combustion | micro rotating-bomb aneroid combustion calorimeter, 111 f                               | micro rotating-bomb aneroid combustion calorimeter, 111 f                               | micro rotating-bomb aneroid combustion calorimeter, 111 f                               | micro rotating-bomb aneroid combustion calorimeter, 111 f                               | micro rotating-bomb aneroid combustion calorimeter, 111 f                               |
| calorimetry, 118                                                                                | static-bomb calorimeters, term, 84                                                      | static-bomb calorimeters, term, 84                                                      | static-bomb calorimeters, term, 84                                                      | static-bomb calorimeters, term, 84                                                      | static-bomb calorimeters, term, 84                                                      |
| inferior calorific value, enthalpy of                                                           |                                                                                         |                                                                                         |                                                                                         |                                                                                         |                                                                                         |
|                                                                                                 | titration calorimetry                                                                   | titration calorimetry                                                                   | titration calorimetry                                                                   | titration calorimetry                                                                   | titration calorimetry                                                                   |
| vaporization, 21 filter effects, photocalorimeter,                                              | using heat flow instruments, 169                                                        | using heat flow instruments, 169                                                        | using heat flow instruments, 169                                                        | using heat flow instruments, 169                                                        | using heat flow instruments, 169                                                        |
| inner 151 insulin growth factor-I, interaction of IGF-I                                         | isoperibol reaction-solution                                                            | isoperibol reaction-solution                                                            | isoperibol reaction-solution                                                            | isoperibol reaction-solution                                                            | isoperibol reaction-solution                                                            |
| receptor with, 169                                                                              | calorimetry accuracy assessment by                                                      | calorimetry accuracy assessment by                                                      | calorimetry accuracy assessment by                                                      | calorimetry accuracy assessment by                                                      | calorimetry accuracy assessment by                                                      |
| internal energy lattice energy, 27                                                              | tris(hydroxymethyl)aminomethane (THAM) HCl reaction,                                    | tris(hydroxymethyl)aminomethane (THAM) HCl reaction,                                    | tris(hydroxymethyl)aminomethane (THAM) HCl reaction,                                    | tris(hydroxymethyl)aminomethane (THAM) HCl reaction,                                    | tris(hydroxymethyl)aminomethane (THAM) HCl reaction,                                    |
|                                                                                                 | + 129-130 calorimetry study of mordenite HF                                             | + 129-130 calorimetry study of mordenite HF                                             | + 129-130 calorimetry study of mordenite HF                                             | + 129-130 calorimetry study of mordenite HF                                             | + 129-130 calorimetry study of mordenite HF                                             |
| standard bond dissociation symbol,                                                              | + reaction, 134 t                                                                       | + reaction, 134 t                                                                       | + reaction, 134 t                                                                       | + reaction, 134 t                                                                       | + reaction, 134 t                                                                       |
| symbol U , 8                                                                                    | calorimetry study of reaction                                                           | calorimetry study of reaction                                                           | calorimetry study of reaction                                                           | calorimetry study of reaction                                                           | calorimetry study of reaction                                                           |
| energy change calculation at 298.15 K:                                                          | Mo( η 5 -C 5 H 5 ) 2 (C 2 H 4 ) + I 2 ,                                                 | Mo( η 5 -C 5 H 5 ) 2 (C 2 H 4 ) + I 2 ,                                                 | Mo( η 5 -C 5 H 5 ) 2 (C 2 H 4 ) + I 2 ,                                                 | Mo( η 5 -C 5 H 5 ) 2 (C 2 H 4 ) + I 2 ,                                                 | Mo( η 5 -C 5 H 5 ) 2 (C 2 H 4 ) + I 2 ,                                                 |
| calibration,                                                                                    | dehydrated form of mordenite, 136                                                       | dehydrated form of mordenite, 136                                                       | dehydrated form of mordenite, 136                                                       | dehydrated form of mordenite, 136                                                       | dehydrated form of mordenite, 136                                                       |
| computation steps for Washburn                                                                  | 133                                                                                     | 133                                                                                     | 133                                                                                     | 133                                                                                     | 133                                                                                     |
| 92-97                                                                                           |                                                                                         |                                                                                         |                                                                                         |                                                                                         |                                                                                         |
| 102-105                                                                                         |                                                                                         |                                                                                         |                                                                                         |                                                                                         |                                                                                         |
|                                                                                                 | Dewar vessel, 125, 126 f                                                                | Dewar vessel, 125, 126 f                                                                | Dewar vessel, 125, 126 f                                                                | Dewar vessel, 125, 126 f                                                                | Dewar vessel, 125, 126 f                                                                |
| internal                                                                                        |                                                                                         |                                                                                         |                                                                                         |                                                                                         |                                                                                         |
|                                                                                                 | 87-88                                                                                   | 87-88                                                                                   | 87-88                                                                                   | 87-88                                                                                   | 87-88                                                                                   |
|                                                                                                 | corrections,                                                                            | corrections,                                                                            | corrections,                                                                            | corrections,                                                                            | corrections,                                                                            |

| isoperibol reaction-solution calorimetry ( continued ) difference from photocalorimetric results, 154 energy equivalents ε i and ε f , 127 enthalpy change under isothermal conditions /Delta1 H ICP , 125-127, 129 enthalpy of formation of Mo( η 5 -C 5 H 5 ) 2 (C 2 H 4 ), 131, 132 f , 133 experiments, 125-126 LKB 8700 reaction-solution calorimeter, 129, 130 f mordenite, 131, 134-136 organotransition metal compounds, 131 reference calorimeter, ε o , 127 schematic, 126 f scheme of typical calibration circuit, 128 f technique, 125 temperature-time curves of calibration before exothermic and endothermic reaction, 130 f temperature-time curves of calibrations in   | ligand (phosphine) exchange reaction, 225-226 nitrogen-centered radicals with acyl radical, 220 rate constant in terms of concentrations, 219 rate constants of benzoyl peroxide decomposition, 221 t reliability of thermochemical kinetics and reaction mechanism, 223 reverse reaction assumption, 222 uncertainty interval for O-H bond dissociation enthalpy in benzoic acid, 222 uncertainty intervals, 224 kinetic studies gas phase reactions, 38-43 reactions in solution, 43-46 Kirchhoff equation, standard reaction heat capacity, 12 Koenig, Hay, and Finke's model, cage effects, 45-46   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Index

| metal-ligand complexation heat flow vs. isoperibol calorimetry, 169-170 titration calorimetry study, 170 t metathesis reaction, equilibrium in σ bond, 210-213 methane calorific value, 21-22 errors in thermochemistry, 21 flame combustion calorimetry, 115 upper limits of bond dissociation energy, 60 t methane pyrolysis, thermodynamic analysis, 13-14 methanol, upper limits of bond dissociation energy, 60 t microcalorimeter, heat flow calorimetry,   | organoiodine compound combustion, 113-114 organometallic compounds, 114 sulfur-containing compounds, 111-112 temperature corrections, 110-111 Washburn correction, 114 multiple reactions, gas phase, 42 Properties                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 141-142 mnemonic heterolytic and homolytic cleavages, 228 f thermochemical information on R-X bond, 227-229 modified Arrhenius plot, kinetic analysis, 41 molality equilibrium constants, calculating, 35, 207 molar enthalpy of reaction, photocalorimetry, 153 molecular thermochemistry, differential scanning calorimetry, 186-187 Mo( η 5 -C 5 H 5 ) 2 (C 2 H 4 )                                                                                            | National Bureau of Standards (NBS), calorific value, 21 NBSTables of Chemical Thermodynamic , 17 Nernst equation, 230 nitric oxide, titration calorimetry studying, 166 nomenclature dissociation energy, 59 thermodynamics, 7-8 non-International System of Units (non-SI), 7, 268 t normal hydrogen electrode, 231 ohmic drop, cyclic voltammogram, 237-238 onset temperature, true, in differential scanning calorimetry, 178 organic compounds, bond dissociation enthalpies using cyclic voltammetry, 242-243 |

oxygen, static-bomb calorimeters, 87-108 oxygen combustion calorimetry, comparison to fluorine combustions, 120-121

partial molar heat capacities, 13 Peltier effect, heat flow calorimetry, 138 perfect gas model, kinetics, 41-42 phase transitions, standard enthalpies, 22-26 phenol enthalpy of atomization, 74 experimental data for PhO-H bond dissociation enthalpy, 62 f hypothetical thermochemical cycle, 69, 70 f O-H bond lengths, 69 standard enthalpy of formation, 75 phenol and acetonitrile energetics of hydrogen bond between, 208-209, 210 f equilibrium constants, 209 t van't Hoff plot, 210 f phosphine exchange reaction activation enthalpy values, 225 f relative enthalpies for series of, 225-226 photoacoustic calorimetry (PAC) amplitude S of acoustic wave, 192, 193 f assuming microphone responds to process rate, 194-195 assuming photoacoustic wave by thermal expansion of irradiated region, 195-196 basic theory of photoacoustic effect, 190 beam splitter, 199 calibration constant K , 193 calibration importance, 204 calibration results, 202 f consecutive calibration and experiment, 200 deconvolution algorithms, 204-206 diagram of photoacoustic calorimeter, 198 f division into three subsets, 197-198 elementary design, 190, 192 f enthalpic information by energy balance, 194 error sources, 201-203 experimental procedure, 200-201 experiment results, 202 f intrinsic volume changes, 195 ligand exchange reactions, 206 observed fraction of photon energy released as heat, 196 photoacoustic measuring system, 198 photochemical cleavage of O-O bond in ditert -butylperoxide, 203 photophone by Bell, 190, 191 f pyroelectric probe, 199 reference cell, 199 sample flow line, 200

short-lived compounds, 86, 190 simplified diagram of photoacoustic calorimeter, 192 f simulated responses of 0.5 MHz transducer for process at different rates, 195 f spectrophotometer, 199 test reaction to assess instrument reliability, 203 time-resolved PAC, 206 volume increase by thermal expansion mechanism, 192-193 working equation for PAC, 193 photocalorimeters, 86, 147 photocalorimetry basic principles, 147-149 calculating molar enthalpy of reaction, 153 calibration of calorimetric unit, 153 constant of instrument, 153 conversion efficiency, 148 difference from reaction-solution results, 154 electromagnetic radiation, 147 energy balance within cell, 147-148 error sources and design, 151-152, 153 first photocalorimeter by Magee, 149 inner filter effects, 151 instrument by Adamson, 149-150 isomerization of trans - to cis -azobenzene, 154-155 Joule calibration, 150 radiant energy, 148 radiant power, 150 radiation-absorbing cell, 152, 153 reaction-solution isoperibol, by Adamson, 149 f reference cell, 152 studying coordination and organometallic complexes, 151 thermochemistry of ligand replacement reaction, 150 twin unit version of heat flow photocalorimeter, 152 f photochemical O-O bond cleavage, photoacoustic calorimetry, 203 photochemical reaction, 147 photomodulation voltammetry (PV) apparatus diagram, 244 f charge transfer coefficient, 246 free radical production, 244 limiting current, 246 linear sweep voltammetry, 246 source of problems, 244-245 voltammogram example, 245-246 photon, photoacoustic effect, 190, 192 f photon energy, release as heat, 196 photophone, Bell, 190, 191 f

| planar electrode, current, 236 potential energy curves, ionization energy and electron affinity, 49, 50 f potential waveform, cyclic voltammetry, 231, 232 f power compensation, differential scanning calorimetry, 172-173 pressure correction, enthalpy, 15 pressure effect enthalpy of gaseous ethanol, 24 enthalpy of liquid ethanol, 24 programmed temperature line, differential scanning calorimetry, 176   | reorganization energies, ER (PhO ∗ ) and ER (EtO ∗ ), 69-71 Republic of Easyprofit, calorific value, 21 Resonance-stabilized carbenium ion, calorimetry for enthalpies of, 166 reversible cyclic voltammogram, 232 f , 235 f reversible oxidation of R - to R, cyclic voltammetry, 233 rhodium complexes, equilibrium concentrations, 213-215 Rossini   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                                                                                                                                                                                                                                    | titration                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                    | waveform,                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                    | enthalpy of formation of liquid water,                                                                                                                                                                                                                                                                                                                  |
| proton affinity, gas-phase molecular energetics,                                                                                                                                                                                                                                                                                                                                                                   | 115-120                                                                                                                                                                                                                                                                                                                                                 |
| 55-57                                                                                                                                                                                                                                                                                                                                                                                                              | flame combustion apparatus, 115-116                                                                                                                                                                                                                                                                                                                     |
| pure substances, standard enthalpy                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                         |
| of                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                         |
| formation, 9-10                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                         |
| pyroelectric probe, measuring                                                                                                                                                                                                                                                                                                                                                                                      | sample cell, calorimeter proper, 83, 84 f                                                                                                                                                                                                                                                                                                               |
| transmittance, 199                                                                                                                                                                                                                                                                                                                                                                                                 | σ bond metathesis reaction                                                                                                                                                                                                                                                                                                                              |
| pyrolysis of methane, thermodynamic analysis,                                                                                                                                                                                                                                                                                                                                                                      | scandium-H bond in                                                                                                                                                                                                                                                                                                                                      |
| 13-14                                                                                                                                                                                                                                                                                                                                                                                                              | bis (pentamethylcyclopentadienyl) bond,                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                    | scandium hydride to Sc-C                                                                                                                                                                                                                                                                                                                                |
| radiant power, photocalorimetry, 150                                                                                                                                                                                                                                                                                                                                                                               | 210-213 van't Hoff plot, 213 f                                                                                                                                                                                                                                                                                                                          |
| radiation-absorbing cell, photocalorimetry,                                                                                                                                                                                                                                                                                                                                                                        | scandium-hydrogen bond to Sc-C bond                                                                                                                                                                                                                                                                                                                     |
| 152, 153                                                                                                                                                                                                                                                                                                                                                                                                           | σ bond metathesis reaction, 210-213                                                                                                                                                                                                                                                                                                                     |
| radical trap, 2,2-diphenyl-1-picrylhydrazyl                                                                                                                                                                                                                                                                                                                                                                        | structure of bis (pentamethylcyclopendienyl)                                                                                                                                                                                                                                                                                                            |
| radical, 220 f random errors, reaction enthalpy, 19                                                                                                                                                                                                                                                                                                                                                                | Sc complex, 211 f secondary thermal effects, heat of stirring,                                                                                                                                                                                                                                                                                          |
| rate of temperature change, isoperibol                                                                                                                                                                                                                                                                                                                                                                             | 90 second harmonic alternating current                                                                                                                                                                                                                                                                                                                  |
| calorimeters, 90, 91                                                                                                                                                                                                                                                                                                                                                                                               | voltammetry (SHACV), 243                                                                                                                                                                                                                                                                                                                                |
| reaction kinetics                                                                                                                                                                                                                                                                                                                                                                                                  | second law method                                                                                                                                                                                                                                                                                                                                       |
| cage effects, 45                                                                                                                                                                                                                                                                                                                                                                                                   | equilibrium complications, 212-213,                                                                                                                                                                                                                                                                                                                     |
| gas phase, 41-42                                                                                                                                                                                                                                                                                                                                                                                                   | 215-216                                                                                                                                                                                                                                                                                                                                                 |
| reaction profile, thermodynamic and kinetic                                                                                                                                                                                                                                                                                                                                                                        | evaluating reaction enthalpy and entropy, 33                                                                                                                                                                                                                                                                                                            |
| properties, 39 f                                                                                                                                                                                                                                                                                                                                                                                                   | gas-phase reactions, 35-36                                                                                                                                                                                                                                                                                                                              |
| reaction-solution calorimeters. See also                                                                                                                                                                                                                                                                                                                                                                           | Gibbs energy, 31                                                                                                                                                                                                                                                                                                                                        |
| isoperibol reaction-solution calorimetry                                                                                                                                                                                                                                                                                                                                                                           | second virial coefficient, enthalpy                                                                                                                                                                                                                                                                                                                     |
| difference from photocalorimetric results, 154                                                                                                                                                                                                                                                                                                                                                                     | corrections, 15 137,                                                                                                                                                                                                                                                                                                                                    |
| testing accuracy, 129-130                                                                                                                                                                                                                                                                                                                                                                                          | Seebeck effect, heat flow calorimetry, 138 sensitivity                                                                                                                                                                                                                                                                                                  |
| reaction vessel, calorimeter proper, 83, f                                                                                                                                                                                                                                                                                                                                                                         | heat flow instruments,                                                                                                                                                                                                                                                                                                                                  |
| 84                                                                                                                                                                                                                                                                                                                                                                                                                 | 169                                                                                                                                                                                                                                                                                                                                                     |
| redox couples, 230-231 reduction potentials, 229                                                                                                                                                                                                                                                                                                                                                                   | heat flow microcalorimeters, 141-142                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                    | short-lived compounds, photoacoustic                                                                                                                                                                                                                                                                                                                    |
| reference cell                                                                                                                                                                                                                                                                                                                                                                                                     | calorimetry, 86, 190 cyclic                                                                                                                                                                                                                                                                                                                             |
| photoacoustic calorimetry, 199                                                                                                                                                                                                                                                                                                                                                                                     | software, voltammogram analysis, 238-240                                                                                                                                                                                                                                                                                                                |
| photocalorimetry, 152 reference electrode                                                                                                                                                                                                                                                                                                                                                                          | solid 4-cyanopyridine N                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                    | -oxide, combustion,                                                                                                                                                                                                                                                                                                                                     |
| cyclic voltammetry, 232                                                                                                                                                                                                                                                                                                                                                                                            | 98-99, 100 t , 101 t solute concentration, equilibrium constants,                                                                                                                                                                                                                                                                                       |
| ferrocenium/ferrocene couple, 241, 242 f reference states, most stable physical states, 9                                                                                                                                                                                                                                                                                                                          | 34-35                                                                                                                                                                                                                                                                                                                                                   |
| reliability assessment, photoacoustic                                                                                                                                                                                                                                                                                                                                                                              | chemistry                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                    | solution                                                                                                                                                                                                                                                                                                                                                |
| calorimetry, 203                                                                                                                                                                                                                                                                                                                                                                                                   | gas-phase chemistry vs.,                                                                                                                                                                                                                                                                                                                                |
| reliability of kinetics, mechanism of                                                                                                                                                                                                                                                                                                                                                                              | 45 standard enthalpies, 22, 26                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                    | solution                                                                                                                                                                                                                                                                                                                                                |
| reaction, 223                                                                                                                                                                                                                                                                                                                                                                                                      | enthalpies, acetic acid formation, 11                                                                                                                                                                                                                                                                                                                   |

| solution phase bond dissociation enthalpy, concept, 64   | benzoic acid combustion for standardizing                                  |
|----------------------------------------------------------|----------------------------------------------------------------------------|
| solution reactions                                       | laboratories, 94-96 energy                                                 |
|                                                          | calculating change of internal                                             |
| Arrhenius plots, 44                                      | /Delta1 c U ◦ , 89 at                                                      |
| cage effect in reaction kinetics, 45                     | calibration by calculation of /Delta1 U IBP                                |
| cage pair, 45                                            | 298.15 K, 92-97                                                            |
| differences from gas-phase, 43                           | combustion of 4-cyanopyridine                                              |
| enthalpy profile, 45 f                                   | N -oxide, 107 t                                                            |
| equilibrium constant K ‡ , 43, 44                        | compounds with C, H, O, and N, 87, 97, 98 f ,                              |
| experimental data for PhO-H bond                         | 99 f , 101                                                                 |
| dissociation enthalpy, 62 f                              | computation steps for Washburn corrections,                                |
| Eyring plot, 44                                          | 102-105                                                                    |
| kinetics, 43-46                                          | correction of /Delta1 U IBP to standard state,                             |
| solvation enthalpy                                       | 97-105                                                                     |
| A-B, 61-62                                               | electrical calibration, 94, 95-97                                          |
| phase transition, 26                                     | energy equivalent of calorimeter, ε o , 94                                 |
| solvents, PhO-H bond dissociation                        | energy supplied for ignition /Delta1 U ign , 93                            |
| enthalpies, 63                                           | internal energy change with bomb process                                   |
| spectrophotometer, measuring                             | under isothermal bomb conditions, 89                                       |
| transmittance, 199                                       | observed temperature change, 90                                            |
| standard chemical potential, solute i, 34                | rate of temperature change during initial and                              |
| standard enthalpies, phase transition, 22-26             | final periods, g , 90, 91                                                  |
| standard enthalpies of atomization                       | reduction of combustion calorimetic results                                |
| experimental vs. calculated, 74-75                       | to standard states, 97 f                                                   |
| phenol, 74                                               | scheme of calculation of /Delta1 U , 93 f                                  |
| standard enthalpies of formation                         | IBP scheme of final-state Washburn                                         |
| anthracene, 16                                           | corrections, 99 f                                                          |
| databases, 18-19                                         | scheme of initial-state Washburn                                           |
| definition, 10                                           | corrections, 98 f                                                          |
| pure substances, 9-10                                    | scheme of macro, isoperibol combustion                                     |
| reactants and products, 17-18                            | calorimeter, 88 f                                                          |
| uncertainty, 20                                          | sum of secondary thermal effects due to heat                               |
| standard enthalpies of                                   | of stirring, 90                                                            |
| solvation, thermochemical cycle, 61 f                    | temperature-time curve from combustion                                     |
| standard hydrogen electrode (SHE), 231                   | reaction, 90 f                                                             |
| standardizing laboratory, energy of combustion           | temperature-time data, 91-92                                               |
| of benzoic acid, 94-96                                   | uncertainties, 105-106, 108                                                |
| standard massic energy of combustion,                    | Washburn corrections, 97-105                                               |
| 4-cyanopyridine N -oxide, 105-106                        | Washburn corrections for combustion of                                     |
| standard reaction heat capacity, Kirchhoff equation, 12  | 4-cyanopyridine N -oxide, 100 t , 101 t stationary electron convention, 48 |
| standard state combustion reaction, C, H,                | stepwise bond dissociation enthalpies                                      |
| O,                                                       |                                                                            |
| compounds, 101                                           | chromium hexacarbonyl, 65-67                                               |
| standard states                                          | first-row hydrides, 67 f                                                   |
| reduction of combustion calorimetry, 97 f                | Stern model of double layer, electrode, 234                                |
| thermochemical databases, 8-9                            | stirred-liquid, calorimeter, 84                                            |
| state function                                           | Student' s t -factors, reaction enthalpy, 19-20                            |
| enthalpy, 10-11                                          | sublimation                                                                |
| reaction profile, 39 f                                   | calibration thermogram for, of iodine,                                     |
| static-bomb combustion calorimetry                       | 143, 144 f                                                                 |
| adiabatic temperature rise /Delta1 T ad                  | enthalpy of lithium, 27, 28                                                |
| determination, 89-92                                     | f standard enthalpies, 22                                                  |
| average temperature T m of calorimeter                   | substituent effects, phenolic O-H bond                                     |
| proper, 91                                               | dissociation enthalpy, 63                                                  |

substituted phenols, hydrogen transfer between, 216-217

sulfur, use in fluorine combustions, 122 sulfur-containing compounds, combustion, 108, 111-112

superior calorific value, enthalpy of vaporization, 21 supporting electrolyte, 235 switching potentials, 231

temperature, dependence of heat capacities, 13 temperature gradient, differential scanning calorimetry, 177 f temperature-induced changes, differential scanning calorimetry, 171 temperature measurement, differential scanning calorimetry, 176-177 temperature-modulated differential scanning calorimetry, 174 temperature-time curve combustion reaction with isoperibol combustion calorimeter, 90 f isoperibol reaction-solution calorimetry, 130 f temperature-time data combustion reaction, 90 f isoperibol continuous titration calorimetry, 158 f isoperibol reaction-solution calorimetry calibration, 128 f , 130 f static-bomb calorimeter, 91-92 thermal decomposition, benzoyl peroxide, 220-222 thermal electron convention, 48 thermal expansion assumptions in photoacoustic calorimetry, 195-196 volume increase by, mechanism, 192-193 thermochemical cycle bond dissociation enthalpy balance, 65 f Cr-C6 H 6 bond enthalpy contribution in Cr(CO)3 (C 6 H 6 ), 71, 72 f enthalpies of methane pyrolysis, 14 f enthalpy of acetic acid formation, 11 f enthalpy of formation of Mo( η 5 -C 5 H 5 ) 2 (C2 H 4 ), 132 f relating enthalpies for acetic acid at 298.15 K and 310 K, 12 f solution and gas-phase bond dissociation enthalpies, 61 f Washburn corrections, 97 thermochemical cycles heterolytic and homolytic cleavages of R-X bond, 227, 228 f

- O-H bond enthalpy contributions in phenol and ethanol, 69, 70 f

thermochemical data, uncertainties, 19-22 thermochemical mnemonic, heterolytic and homolytic cleavages of R-X bond, 227, 228 f

Thermodynamic Data and Structures of Organic Compounds , Pedley's, 17 thermodynamic property, standard states, 8-9 thermodynamics electrochemistry and, 229-231 nomenclature, 7-8 units, 7

third law method, Gibbs energy, 36-37 third virial coefficient, enthalpy corrections, 15

Tian, heat flow calorimeter design, 138-139

time-resolved photoacoustic calorimetry, 206

titanium complexes, isomerization of

η 3 -coordinated allyl ligand to trans -1-propenyl ligand, 223-224 titration calorimetry accuracy, 157

basicity of organometallic complexes, 165-166

biological activity of NO, 166 calibration, 159, 168

continuous or incremental procedures, 156-157

curve for continuous, of exothermic reaction, 167 f determination of enthalpies of reaction and equilibrium constants, 163-166

determination of enthalpy of isothermal calorimetric process /Delta1 H ICP , 159-162

energetics of metal-ligand complexation, 169-170

energy equivalent of calorimetric system ε , 159-160

enthalpies of resonance-stabilized carbenium ion, 166

enthalpy of reaction under study in heat flow, 168-169

heat flow, 167-170

historical development, 156

hypothetical, study of reaction A(aq) + B(aq)

insulin growth factor-I (IGF-I), 169 isoperibol continuous, 158-166

- → AB(aq), 165 f

rate of temperature change of calorimeter proper, 161-162

reaction vessel for isoperibol, 157-158 scheme of isoperibol, apparatus, 157 f temperature-time curve for isoperibol continuous, experiment, 158 f use, 156

transferability, bond enthalpies, 69 transition metal-ligand bond dissociation enthalpies, differential scanning calorimetry, 183-185 transition-state theory (TST) gas phase reactions, 38-43 solution reactions, 43-46 tungsten, inducing complete combustions with fluorine, 122 twin unit version, heat flow photocalorimeter, 152 f

## uncertainty

combustion of 4-cyanopyridine N -oxide, 105-106, 108 Gibbs energy, 31, 32 f overall uncertainty interval, 19, 20 Student' s t -factors, 19-20 thermochemical data, 19-22 uncertainty interval O-H bond dissociation enthalpy of benzoic acid, 222 reaction kinetics, 224, 224-230 unimolecular reaction enthalpy profile of, in solution, 45 f gas phase, 42 kinetics of gas-phase, 39-40

van't Hoff equation, enthalpy and entropy, 32

van't Hoff plots basis for equilibrium constants, 215

phenol and acetonitrile reaction, 209, 210 f reaction enthalpy and entropy, 208 σ bond metathesis reaction, 210, 213 f vaporization, standard enthalpies, 22, 23-25 vapor pressure, ebulliometric method, 22-23 vertical ionization energy, 49, 50 f virial coefficients, second and third, 15 voltammetry. See cyclic voltammetry (CV);

photomodulation voltammetry (PV)

Washburn corrections auxiliary data, 100 t combustion of 4-cyanopyridine N -oxide, 101 t computation steps, 102-105 general scheme for final-state, 99 f general scheme for initial-state, 98 f internal energy change, 89, 97-105

thermochemical cycle, 97 water enthalpy of formation of liquid, 115-120 flame combustion calorimetry, 115 standard enthalpy of formation, 17 upper limits of bond dissociation energy, 60 t waveform, reversible cyclic voltammogram, 235 f working electrode, cyclic voltammetry, 231, 232

zero-current cell potential, 229 zero line, differential scanning calorimetry, 176