## SCHAUM'S OUTLINE OF

## THEORY AND PROBLEMS

of

## ENGINEERING ECONOMICS

by

## JOSE  A. SEPULVEDA, P ~ . D .

Associate Professor of Industrial Engineering University of Central Florida

## WILLIAM E. SOUDER, Ph.D.

Professor of Industrial Engineering University of Pittsburgh and

## BYRON S. GOTTFRIED, Ph.D.

Professor of Industrial Engineering Engineering Management and Operations Research University of Pittsburgh

## SCHAUM'S OUTLINE SERIES McGRAW-HILL

New York San Francisco Washington, D.C. Auckland Bogotb Caracas Lisbon London Madrid MexicoCity Milan Montreal NewDelhi SanJuan Singapore Sydney Tokyo Toronto

I

J O S ~ A.  SEPULVEDA  is  an Associate Professor of Industrial Engineering  at  the  University of  Central  Florida.  He holds  a  Ph.D.  in Industrial Engineering and an M.P.H.  from the University of  Pittsburgh. His research and teaching interests are in  health operations research and economic feasibility analysis.  He is a  Registered  Professional Engineer.

WILLIAM E. SOUDER is a Professor of  Industrial Engineering at the University of  Pittsburgh.  Since 1972,  he  has  been  at  the  University of Pittsburgh,  where  he  teaches  courses  in  Engineering  Management  and Behavioral  Systems  and  directs  the  Technology  Management  Studies Research  Group.  He is  the  author  of two  other  books  and  over  one hundred technical papers.

BYRON  S.  GOTTFRIED  is  a  Professor  of Industrial  Engineering, Engineering Management, and Operations Research at the University of Pittsburgh. He received his Ph.D. from Case-Western Resene University (1%2),  and has been a member of  the Pitt faculty since 1970. His primary interests  are  in the  development  of complex  technical  and  business applications  of computers.  Dr.  Gottfried  is  the  author  of  several  textbooks, as well as Introduction to Engineering Calculations in the Schaum's Outline Series.

Schaum's Outline of Theory and Problems of ENGINEERING ECONOMICS

Copyright O 1984 by The McGraw-Hill Companies, Inc. All Rights Reserved. Printed in the United States of America. Except as permitted under the Copyright Act of 1976, no part of this publication may be reproduced or distributed  in any form or by any means, or stored in a data base or retrieval system, without the prior written permission of the publisher.

16 17 18 VFM VFM 06 05 04

## ISBN 0-07-02383q-0

Sponsoring Editor, David Beckwith Editing Supervisor, Marthe Grice Production Manager, Nick Monti

## Library o f Congress Cataloging in Pubfiestion h t e

## Sepulveda, Josd A.

Schaum's outline of  theory and problems of  engineering economics.

(Schaum's outline series)

Includes index.

1.  Engineering economy. I.  Souder, William E.

11. Gottfried, Byron S.,  1934-

TAl77.4.S47

1 M

ISBN 0-07-023834-0

## McGraw  -Hill

111.  Title.

658.1'55

<!-- image -->

i z

114-778

## Preface

Despite remarkable technological  advances  during the past  several decades, most major engineering decisions are based on economic considerations-a situation  that  is  unlikely  to change  in  the  years  ahead.  Hence  the  importance  of economic principles to all undergraduate engineering students, regardless of  their particular disciplinary  interests.

This Schaum 7 s Outline contains a clear and concise review of  the principles of engineering economics,  together  with  a  large number of  solved  problems.  Most chapters  also  contain  a  list  of  supplementary  problems,  which  the readers may solve themselves. Thus, readers receive an exposure to the theory, as well as an opportunity to become actively involved in the application of  this theory to typical (though simple) problem situations.

The  book  is  designed  to  complement  a  standard  undergraduate  course  in engineering economics.  The  first  five  chapters  consider the  mathematics  of compound interest, emphasizing the time value of  money. Chapters 6 through 9 discuss  the application  of  this  material  in  various  decision-making  criteria,  and Chapter 10 deals with equipment  replacement and retirement decisions.  Chapter 11 considers  the important  topics of  depreciation and taxes, and their impact  on the decision-making  process.  Finally,  Chapter  12  presents  a  realistic  economic feasibility  study.

The four appendixes to the book contain  tables of  various compound interest factors. Such tables continue to be useful, even in an era of  electronic calculators and personal computers.

JosÉ A. SEPULVEDA WILLIAM E. SOUDER BYRON S. GOTTFRIED

## Contents

................................................

| Chapter   | 1 BASIC CONCEPTS                                                                                                      |   1 |
|-----------|-----------------------------------------------------------------------------------------------------------------------|-----|
|           | 1.1 Interest ...............................................................                                          |   1 |
|           | 1.2 Interest Rate ...........................................................                                         |   1 |
|           | 1.3 Simple Interest .........................................................                                         |   1 |
|           | 1.4 Compound Interest .....................................................                                           |   2 |
|           | 1.5 The Time Value of Money ..............................................                                            |   2 |
|           | 1.6 Inflation ...............................................................                                         |   3 |
|           | 1.7 Taxes .................................................................                                           |   4 |
|           | 1.8 Cash Flows ............................................................                                           |   5 |
| Chapter   | 2 ANNUAL COMPOUNDING .........................................                                                        |  12 |
|           | 2.1 Single.Payment. Compound-Amount Factor ...............................                                            |  12 |
|           | 2.2 Single.Payment. Present-Worth Factor ....................................                                         |  12 |
|           | 2.3 Uniform.Series. Compound-AmountFactor ............................... .....................................       |  12 |
|           | 2.4 Uniform.Series. Sinking-Fund Factor                                                                               |  13 |
|           | 2.5 Uniform.Series. Capital-Recovery Factor ..................................                                        |  14 |
|           | 2.6 Uniform.Series. Present-Worth Factor ....................................                                         |  15 |
|           | 2.7 Gradient Series Factor ..................................................                                         |  15 |
| Chapter   | 3 ALGEBRAICRELATIONSHIPS AND SOLUTION PROCEDURES ......                                                               |  23 |
|           | 3.1 Relationships Between Interest Factors ...................................                                        |  23 |
|           | 3.2 Linear Interpolation ....................................................                                         |  24 |
|           | 3.3 Unknown Number of Years . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |  24 |
|           | 3.4 Unknown Interest Rate .................................................                                           |  26 |
| Chapter   | 4 DISCRETE. PERIODIC COMPOUNDING ............................                                                         |  31 |
|           | 4.1. Nominal and Effective Interest Rates .....................................                                       |  31 |
|           | ...................... 4.2 When Interest Periods Coincide with Payment Periods                                        |  31 |
|           | ................... 4.3 When Interest Periods Are Smaller than Payment Periods                                        |  32 |
|           | .................... 4.4 When Interest Periods Are Larger than Payment Periods                                        |  33 |
| Chapter   | 5 CONTINUOUS COMPOUNDING ....................................                                                         |  40 |
|           | 5.1 Nominal and Effective Interest Rates .....................................                                        |  40 |
|           | 5.2 Discrete Payments ......................................................                                          |  40 |
|           | 5.3 Continuous Payments ...................................................                                           |  42 |

## CONTENTS

..................................................

| Chapter 6   | EQUIVALENCE                                                                                                                                                                                                                            | 48      |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
|             | 6.1 Economic Equivalence ..................................................                                                                                                                                                            | 48      |
|             | ..................................................... 6.2TheCostofCapital ........................................................                                                                                                     | 50      |
|             | 6.3 Stock Valuation                                                                                                                                                                                                                    | 50      |
|             | 6.4 Bond Valuation ........................................................                                                                                                                                                            | 51      |
|             | 6.5 Minimum Attractive Rate of Return ......................................                                                                                                                                                           | 51      |
|             | 6.6 Fair Market Value ......................................................                                                                                                                                                           | 52      |
| Chapter 7   | PW. FW. EUAS/EUAC ........................................                                                                                                                                                                             | 57      |
|             | 7.1 Present Worth .........................................................                                                                                                                                                            | 57      |
|             | 7.2 Future Worth ..........................................................                                                                                                                                                            | 58      |
|             | 7.3 Equivalent Uniform Annual Series .......................................                                                                                                                                                           | 59      |
|             | 7.4 Capital Recovery .......................................................                                                                                                                                                           | 60      |
|             | 7.5 Capitalized Equivalent ..................................................                                                                                                                                                          | 60      |
| Chapter 8   | NET PRESENT VALUE. RATEOF RETURN. PAYBACK PERIOD. .......................................... BENEFIT-COSTRATIO                                                                                                                         | 66      |
|             | 8.1 Net Present Value ......................................................                                                                                                                                                           | 66      |
|             | 8.2 Rate of Return .........................................................                                                                                                                                                           | 66      |
|             | 8.3 Payback Period ........................................................                                                                                                                                                            | 68      |
|             | 8.4 Benefit-Cost Ratio ......................................................                                                                                                                                                          | 69      |
| Chapter 9   | CHOOSING AMONG INVESTMENT ALTERNATIVES ................                                                                                                                                                                                | 77      |
|             | 9.1 SettingtheMARR                                                                                                                                                                                                                     | 77      |
|             | ..................................................... 9.2 Project Selection and Budget Allocation ..................................                                                                                                   | 78      |
|             | 9.3 The Reinvestment Fallacy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                             | 81      |
| Chapter 10  | EQUIPMENTREPLACEMENTAND RETIREMENT ..................                                                                                                                                                                                  | 92      |
|             | 10.1 Retirement and Replacement Decisions ..................................                                                                                                                                                           | 92      |
|             | 10.2 Economic Life of an Asset .............................................                                                                                                                                                           | 92      |
|             | 10.3 RetirementIReplacementEconomics .....................................                                                                                                                                                             | 94      |
|             | 10.4 Replacement Assumption for Unequal-Lived Assets .......................                                                                                                                                                           | 97      |
| Chapter 11  | DEPRECIATIONAND TAXES ......................................                                                                                                                                                                           | 105     |
|             | 11.1 Definitions ...........................................................                                                                                                                                                           | 105     |
|             | 11.2 Straight-Line Method .................................................                                                                                                                                                            | 105     |
|             | 11.3 Declining-BalanceMethod .............................................                                                                                                                                                             | 106     |
|             | 11.4 Sum-of-Years' -Digits Method ..........................................                                                                                                                                                           | 108     |
|             | 11.5 Sinking-Fund Method .................................................                                                                                                                                                             | 109     |
|             | 11.6 Group and Composite Depreciation ....................................                                                                                                                                                             | 110     |
|             | 11.7 Additional First-Year Depreciation; Investment Tax Credit ......................................................... 11.8 Comparison of Depreciation Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 111 112 |

## CONTENTS

|            | 11.9                                                                                                                         | ........................................ Business Net Income and Taxes 112                                         |     |
|------------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----|
|            | 11.10                                                                                                                        | Comparative Effects of Depreciation Methods on IncomeTaxes ...................................................     | 114 |
|            | 11.11                                                                                                                        | ................................. The Accelerated Cost Recovery System                                             | 116 |
|            | 11.12                                                                                                                        | ........................................ Choice of Depreciation Method ........................................... | 117 |
|            | 11.13                                                                                                                        | Depreciation and Cash Flow                                                                                         | 118 |
|            | 11.14                                                                                                                        | .............................. Before- and After-Tax Economic Analyses                                             | 118 |
| Chapter 12 | PREPARING AND PRESENTING AN ECONOMIC FEASIBILITYSTUDY ............................................                           | PREPARING AND PRESENTING AN ECONOMIC FEASIBILITYSTUDY ............................................                 | 127 |
|            | .......................................................... 12.1 Introduction                                                 | .......................................................... 12.1 Introduction                                       | 127 |
|            | ............................................... 12.2 Background Information                                                  | ............................................... 12.2 Background Information                                        | 127 |
|            | ......................................................... 12.3 Market Study                                                  | ......................................................... 12.3 Market Study                                        | 128 |
|            | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12.4 Project Engineering | . .                                                                                                                | 129 |
|            | ....................................................... 12.5 Cost Estimation                                                 | ....................................................... 12.5 Cost Estimation                                       | 130 |
|            | ................................................ 12.6 Estimation of Revenues                                                 | ................................................ 12.6 Estimation of Revenues                                       | 132 |
|            | ............................................................. 12.7 Financing                                                 | ............................................................. 12.7 Financing                                       | 132 |
| Appendix A | ..... COMPOUNDINTERESTFACTORS-ANNUAL COMPOUNDING                                                                             | ..... COMPOUNDINTERESTFACTORS-ANNUAL COMPOUNDING                                                                   | 135 |
| Appendix B | ................. NOMINAL VERSUS EFFECTIVEINTERESTRATES                                                                      | ................. NOMINAL VERSUS EFFECTIVEINTERESTRATES                                                            | 157 |
| Appendix C | COMPOUNDINTERESTFACTORS-CONTINUOUS COMPOUNDING ...............................................                               | COMPOUNDINTERESTFACTORS-CONTINUOUS COMPOUNDING ...............................................                     | 159 |
| Appendix D | ... CONTINUOUSVERSUS ANNUAL UNIFORM PAYMENTFACTORS                                                                           | ... CONTINUOUSVERSUS ANNUAL UNIFORM PAYMENTFACTORS                                                                 | 181 |
| INDEX      | ........................................................................                                                     | ........................................................................                                           | 183 |

183

## 1.1 INTEREST

Interest is  a  fee  that  is  charged  for  the  use  of  someone else's  money. The size  of  the fee  will depend upon the total amount of  money borrowed and the length of  time over which it is borrowed.

Example 1.1 An engineer wishes to borrow $20 000 in  order to start his own  business. A bank  will lend him the money provided  he agrees to repay $920 per month for two years. How much interest is he being charged? $22 080. Since the original loan is

The total amount of  money  that will be paid  to the bank  is 24 x $920 = only $20 000, the amount of  interest is $22 080 -$20 000 = $2080.

Whenever money is borrowed or invested, one party acts as the lender and another party as the borrower. The lender is the owner of  the money, and the borrower pays interest to the lender for the use of  the lender's  money.  For example, when money is deposited in a savings account, the depositor is  the  lender  and  the  bank  is  the  borrower.  The  bank  therefore  pays  interest  for  the  use  of  the depositor's  money. (The  bank  will  then  assume  the  role  of  the  lender,  by  loaning  this  money  to another borrower, at a higher interest  rate.)

## 1.2 INTEREST RATE

If  a  given  amount  of  money  is  borrowed  for  a  specified  period  of  time  (typically,  one year),  a certain percentage of  the money is charged as interest. This percentage is called the interest rate.

Example 1.2 (a) A student deposits $1000 in a savings account  that pays interest at the rate of  6% per year. How much money will the student have after one year? (b) An investor makes a loan of  $5000, to be repaid in one lump sum at the end of  one year. What annual interest rate corresponds to a lump-sum payment of  $5425?

- (a) The student will have his original $1000, plus an interest payment of  0.06 x $1000 = $60. Thus, the student will  have  accumulated  a  total  of $1060  after  one  year.  (Notice  that  the  interest  rate  is  expressed  as  a decimal when carrying out the calculation.)
- (b) The total amount of  interest paid is $5425 -$5000 = $425. Hence the annual interest rate is

<!-- formula-not-decoded -->

Interest rates are usually influenced by the prevailing economic conditions, as well as the degree of  risk  associated  with  each  particular loan.

## 1.3 SIMPLE INTEREST

Simple interest is defined as a fixed percentage of  the principal (the amount of  money borrowed), multiplied  by the life of  the loan. Thus,

<!-- formula-not-decoded -->

## Basic Concepts

where I =total  amount of  simple interest n =life of  the loan

i = interest rate (expressed as a decimal)

P = principal

It  is understood  that n and i refer  to the same unit of  time (e.g., the year).

<!-- image -->

I

Normally, when a simple interest loan is made, nothing is repaid until the end of  the loan period; then,  both  the  principal  and  the  accumulated  interest  are  repaid.  The  total  amount  due  can  be expressed as

<!-- formula-not-decoded -->

Example 1.3 A student borrows $3000 from his uncle in order to finish school. His uncle agrees to charge him simple interest at the rate of 5% per year. Suppose the student waits two years and then repays the entire loan. How much will he have to repay?

By  (1.2), F = $3000[1+ (2)(0.055)] = $3330.

## 1.4 COMPOUND INTEREST

When  interest  is  compounded,  the  total  time  period  is  subdivided  into several  interest periods (e.g., one year, three months, one month). Interest is credited at the end of  each interest period, and is allowed to accumulate from one interest period to the next.

During  a given  interest  period,  the current  interest  is  determined  as a  percentage  of  the  total amount owed (i.e.,  the principal  plus the previously accumulated interest).  Thus, for the first interest period, the interest is determined as

<!-- formula-not-decoded -->

and the total amount accumulated is

For the second interest period, the interest is determined as

<!-- formula-not-decoded -->

and the total amount accumulated is

<!-- formula-not-decoded -->

For the third interest  period,

<!-- formula-not-decoded -->

and so on. In general, if  there are n  interest  periods, we have (dropping the subscript):

<!-- formula-not-decoded -->

which  is  the  so-called law  of compound  interest.  Notice  that  F,  the  total  amount  of money accumulated, increases exponentially with  n, the time measured in interest  periods.

Example 1.4 A  student  deposits $1000 in  a savings account  that  pays interest  at  the  rate of  6%  per  year, compounded  annually.  If  all of  the  money is allowed to accumulate,  how  much will  the student  have after 12 years? Compare this with the amount that would have accumulated i f   simple interest  had been paid.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Thus, the student's original investment will have more than doubled over the 12-year period.

I f   simple interest had  been  paid, the total amount that would have accumulated is determined by  (1.2) as

<!-- formula-not-decoded -->

## 1.5 THE TIME VALUE OF MONEY

Since  money  has  the ability  to earn  interest,  its  value  increases with  time.  For instance,  $100 today is equivalent to

<!-- formula-not-decoded -->

five years from now if  the interest rate is 7% per year, compounded annually. We say that the future worth of $100 is $140.26 i f i = 7% (per  year) and n = 5 (years).

Since money increases in  value as we move from  the present to the future, it  must decrease in value as we move from the future to the present. Thus, the present worth of $140.26 is $100 i f i = 7% (per  year) and n = 5 (years).

Example 1.5 A student who will  inherit $5000 i n   three  years has a savings account  that pays 5% per  year, compounded annually. What is the present worth of  the student's inheritance?

Equation (1.3) may be solved for P, given the value o f   F:

<!-- formula-not-decoded -->

The present worth of $5000 is $4258.07 if  i = 5$%, compounded annually, and n = 3.

## 1.6 INFLATION

National  economies  frequently  experience inflation, in  which  the  cost  of goods  and  services increases  from  one  year  to  the  next.  Normally,  inflationary  increases  are  expressed  in  terms  of percentages which  are compounded  annually.  Thus,  if  the  present  cost  of  a  commodity  is  PC,  its future cost, FC, will be

<!-- formula-not-decoded -->

where A = annual inflation rate (expressed as a decimal)

n = number of  years

Example 1.6 An economy is experiencing inflation at the rate o f 6% per year. An item presently costs $100. If the 6% inflation rate continues, what will  be the price o f   this item in  five years?

By (1.4), FC = $100(1+ 0.06)' = $133.82.

In  an  inflationary  economy,  the  value  (buying  power)  of  money  decreases  as  costs  increase. Thus,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where F is the future worth, measured in  today's dollars, of  a  present  amount P.

Example 1.7 An  economy is experiencing inflation at an  annual rate o f 6%. I f   this continues, what will $100 be worth five years from now, in  terms o f   today's dollars? From (1.5),

<!-- formula-not-decoded -->

Thus $100 i n   five years will  be worth only $74.73 i n   terms o f   today's dollars.  Stated differently, in five years $100 will  be required to purchase the same commodity that can  now  be purchased for $74.73.

If  interest is being compounded at the same time that inflation is occurring, then the future worth can be determined by combining (1.3) and (1.5):

<!-- formula-not-decoded -->

or, defining the composite  interest rate,

we have

Observe that  0 may be negative.

Example 1.7 An engineer has received $10 000 from his employer for a patent disclosure. He has decided to invest the money in a 15-year savings certificate that pays 8% per year, compounded annually. What will be the final value of  his investment, in terms of  today's dollars, if  inflation continues at the rate of  6%  per year?

A composite interest rate can be determined from  (1.6):

<!-- formula-not-decoded -->

Substituting  this value into (1.7),  we obtain

<!-- formula-not-decoded -->

(If  more significant figures are included in  the value for 8, the future value $13 236.35 is obtained.)

## 1 . 7 TAXES

In  most  situations,  the interest  that is  received  from  an investment  will  be subject  to taxation. Suppose that the interest is taxed at a rate t, and that the period of  taxation is the same as the interest period  (e.g.,  one year).  Then  the tax for each  period  will  be  T = tip,  so that  the net return  to the investor (after taxes) will be

<!-- formula-not-decoded -->

If  the effects of  taxation and inflation  are both included in a compound interest calculation,  (1.7) may still be used to relate present and future values, provided the composite interest rate is redefined as

<!-- formula-not-decoded -->

Example 1.8 Refer to Example 1.7.  Suppose the engineer is in  the 32%  tax bracket,  and is likely to remain there throughout the lifetime of  the certificate. If  inflation continues at the rate of  6% per year, what will be the value of  his investment, in  terms of  today's dollars, when the certificate matures?

Let us assume that the engineer is able to invest the entire $10 000 in a savings certificate and that the 32% tax bracket includes all federal, state, and local taxes. By  (1.9),

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Because of  the combined effects of  inflation and taxation, I3 is negative,  and the engineer ends up with less real purchasingpower after  15 years than he has today. (To make matters worse, the engineer will most likely have to pay taxes on the original $10 000, substantially  reducing the amount of  money available for investment.)

The subject o f   taxation is considered in  much greater detail in Chapter 1 1 .

and (1.7) then gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 1.8 CASH FLOWS

A cash flow  is the difference  between  total cash  receipts (inflows) and total cash  disbursements (outjlows)  for  a  given period  of time  (typically,  one  year).  Cash  flows  are  very  important  in engineering economics  because they form  the  basis for evaluating projects, equipment, and  investment alternatives.

The easiest  way  to visualize  a cash  flow is through  a  cash flow diagram, in  which  the individual cash  flows are  represented as vertical  arrows along a  horizontal time scale.  Positive cash  flows (net inflows)  are  represented  by  upward-pointing  arrows,  and  negative  cash  flows  (net  outflows)  by downward-pointing  arrows;  the  length  of an  arrow  is  proportional  to  the  magnitude  of the  corresponding cash  flow.  Each cash flow is assumed to occur at the end of  the respective time period.

Example 1.9 A company plans to invest $500 000 to manufacture a new  product. The sale of this product is expected to provide a net income o f   $70 000 a year for 10 years, beginning at the end o f   the first year. Figure 1-1 is the cash flow diagram for this proposed project. Notice that the initial $500 000 investment is represented by  a downward-pointing arrow located at the end of   year 0 (i.e., at the beginning o f   year 1).  Each annual net income ($70  000) is indicated by  an  upward-pointing arrow located at the end o f   the corresponding year.

Fig. 1-1

<!-- image -->

In a lender-borrower situation, an inflow for the one is an outflow for the other. Hence, the cash flow diagram for the lender will be the mirror image in the time line of  the cash flow diagram for the borrower.

## Solved Problems

- 1.1 The ABC Company deposited $100 000 in  a bank account on June 15 and withdrew a total of $115 000 exactly one year later. Compute: ( a ) the interest which the ABC Company received from the $100 000 investment, and (b) the annual interest rate which  the ABC Company was paid.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 1.2 What is the annual rate of  simple interest if  $265 is earned in four months on an investment of $15 O O O ?

From (1.2),

F

=

P(1+  n i )

<!-- formula-not-decoded -->

- 1.3 Determine  the principal  that  would  have  to be  invested  to  provide  $200  of  simple  interest income at the end of  two years if  the annual interest rate is 9%

<!-- formula-not-decoded -->

- 1.4 Compare  the interest  earned  from  an  investment  of  $1000 for 15 years  at 10%  per  annum simple interest, with  the amount of  interest  that could  be earned if  these funds were invested for 15 years at 10°/o  per year, compounded annually.

The simple interest is given by (1.1) as I = (15)(0.10)($1000) = $1500. From (1.3),

<!-- formula-not-decoded -->

or more than double the amount earned using simple interest.

- 1.5 At what annual interest rate is $500 one year ago equivalent to $600 today?

From (1.3),

<!-- formula-not-decoded -->

- 1.6 Suppose that  the interest  rate is 10%  per year, compounded  annually.  What is the minimum amount of  money that would  have to be invested for a two-year  period in  order to earn $300 in  interest?

From ( 1 . 3 ) ,

<!-- formula-not-decoded -->

- 1.7 How  long  would  it  take  for  an  investor  to  double  his  money  at  10%  interest  per  year, compounded annually?

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Actually, since the interest is compounded only at  the end o f   each year, the investor would have to wait 8 years.

- 1.8 Suppose that a man lends $1000 for four years at 12%  per year simple interest. At the end of the four years, he invests the entire amount which he then has for 10 years at 8% interest per year, compounded annually. How much money will he have at the end of  the 14-year period?

From (1 . 2 ) and ( 1 . 3 ) ,

<!-- formula-not-decoded -->

- 1.9 Let the inflation  rate be 6% per year. I f   a person deposits $50 000 in a bank account at 9% per annum simple interest for 10  years,  will  this effectively  protect  the purchasing  power  of  the original  principal?

The answer is not obvious, for the inflation rate, though the smaller, is compounded. From (1.2), the principal will grow  to:

<!-- formula-not-decoded -->

- By ( 1 . 5 ) , the inflation will  reduce the "real" purchasing power o f   these funds to

<!-- formula-not-decoded -->

Thus, the purchasing power o f   the investment will  be protected, and a small amount o f   interest will  be earned.

- 1.10 Rework Problem 1.9, which is changed as follows: the individual is in  the 35% tax bracket and pays  taxes on  all  the interest  received; the $50 000 is  invested  at 9%  per year, compounded annually.

Now (1. 9 ) gives

<!-- formula-not-decoded -->

With f 3 negative, (1.7) implies F &lt; P: the investment is not ~rotected, and there will be a (small) loss.

- 1.11 An individual wants to have $2000 at the end of  three years. How much would the individual have to invest at a  10% per year interest  rate, compounded  annually, in  order to obtain  a net of  $2000 after paying a $250  early withdrawal fee  at  the end of  the third  year?  Draw a cash flow diagram for the individual.

<!-- formula-not-decoded -->

The cash flow diagram for the individual is given  in  Fig.  1-2.

Fig. 1-2

| End of Year   | Savings   | Withdrawals   | Cash Flows   |
|---------------|-----------|---------------|--------------|
|               | S600      | $ 0           | S60o         |
|               |           | 300           | +300         |
| 2             | 50o       | 300           | 200          |
|               |           | 300           | +300         |
|               |           |               | 500          |
| 5             |           | 350           | +350         |
|               | 400       |               | 400          |
|               | 400       | 350           | 50           |
| 8             | 400       |               | 400          |
|               | 400       | 350           | 50           |
| 10            | 400       |               | 400          |

Table 1-1

<!-- image -->

- 1.12 Suppose that you have a savings plan covering the next ten years, according to which  you  put aside $600  today, $500 at the end of  every other year for  the next five years, and $400 at  the end  of  each  year for  the  remaining five  years.  As part  of this  plan,  you  expect  to withdraw $300  at  the end  of  every  year for  the first 3 years,  and  $350  at  the end  of  every  other  year thereafter. (a)  Tabulate your cash flows. (b) Draw your cash flow diagram.
- (a) See Table 1-1.
- (b) See Fig. 1-3.

Fig. 1-3

<!-- image -->

- 1.13 Under your six-year savings plan, you deposit $1000 now, and $1000 at the end of  the fourth year, in a bank account that earns 8% per year, compounded annually. You withdraw all your accumulated interest at the end of  the second  year, and  the further interest  plus principal  at the end  of the sixth  year. ( a ) Tabulate  the cash  flows  and  the  balance  in  your  investment account. ( b ) Draw a cash flow diagram for the bank. ( c ) Compute the penalty (suffered by you) for the early  withdrawal  of  interest at the end of  the second year.
- ( a ) See Table 1-2.

Table 1-2

|             |          |             | Account Balance   | Account Balance   | Account Balance   |            |
|-------------|----------|-------------|-------------------|-------------------|-------------------|------------|
| End of Year | Deposits | Withdrawals | for First $1000   | for Second $1000  | Total             | Cash Flows |
| 0           | $1000    | $ 0         | $1000.00          | ---               | $1000.00          | -$lO00.00  |
| 1           | 0        | 0           | 1080.00           | ---               | 1080.00           | 0          |
| 2           | 0        | 166.40      | 1000.00           | - - -             | 1000.00           | + 166.40   |
| 3           | 0        | 0           | 1080.00           | - - -             | 1080.00           | 0          |
| 4           | 1000     | 0           | 1166.40           | $1000.00          | 2166.40           | - 1000.00  |
| 5           | 0        | 0           | 1259.71           | 1080.00           | 2339.71           | 0          |
| 6           | 0        | 2526.88     | 1360.48           | 1166.40           | 2526.88           | + 2526.88  |
|             |          |             |                   | NET               | CASH now          | +$693.28   |

Fig. 1-4

<!-- image -->

- (b) See Fig.  14.
- (c) I f   the accumulated interest had not been withdrawn at the end o f   year 2, the $1000 invested at the  start of   the plan would have grown to

<!-- formula-not-decoded -->

and the total available for withdrawal at the end o f   year 6 would have been

<!-- formula-not-decoded -->

Hence, the net cash flow would have been $753.27, or $59.99 more.

## Supplementary Problems

- 1.14 How much interest would be due at the end o f   one year on a loan  o f   $10000 i f   the interest is  12% per year? Ans. $1200
- 1.15 What is the annual interest rate on  a $1000 loan in  which all interest is paid at the end o f   the year, and a total o f   $1125 must be repaid at the end o f   the year? Ans. 12.5%
- 1.16 I f $300  is  earned  in three  months  on  an  investment  o f $12000,  what  is  the  annual  rate  of  simple interest? Ans. 10%
- 1.17 How long will  it  take for an  investment o f   $5000  to grow  to $7500, i f   it earns 10%  simple interest per year? Ans. 5 years
- 1.18 Find the principal o f   a loan in  which the interest rate is  1% per month, payable monthly, and in  which the borrower has  just made the first monthly interest payment o f   $50. Ans. $3333.33
- 1.19 Find the principal, i f   the principal plus interest at the end o f   one and one-half years is $3360 for a simple interest rate o f   8% per annum. Ans. $3000
- 1.20 Which is more desirable: investing $2000 at 6%  per year compound interest for three years, or investing $2000 at 7%  per year simple interest for three years? Ans. Simple interest is superior by $38.

- 1.21 At  what  rate o f   interest, compounded annually, will  an  investment triple itself  in ( a ) 8 years? ( b ) 10 years? ( c ) 12 years? Ans. ( a ) 14.7%; ( b ) 11.6%; ( c ) 9.6%
- 1.22 What rate of   interest, compounded annually, will result in  the receipt o f   $15 938.48 if  $10 000 is invested for  8 years? Ans. 6%
- 1.23 How much money will be required  four years  from today to repay a $2000 loan that is made today ( a ) at 8% interest,  compounded  annually? ( b ) at  8%  simple  interest? Ans. ( a ) $2720.97; ( b ) $2640.00
- 1.24 How many years will be required for an investment o f   $3000 to increase to $4081.47 at an interest rate o f 8% per year, compounded annually? Ans. 4 years
- 1.25 What is the present value of  $10 000 to be received 20 years from now, if  the principal is invested at 8% per year, compounded annually? Ans. $2145.48
- 1.26 How many years will it  take for an investment to double, if  the interest rate is 8%  per year, compounded annually? Ans. 9 years
- 1.27 A  person  lends $2000  for five  years at  10%  per  annum simple  interest;  then  the entire  proceeds are invested for 10  years at 9%  per year, compounded annually. How  much  money will  the person have at the end of   the entire 15-year period? Ans. $7102.09
- 1.28 Suppose that a person  invests $3000  at 10%  per year, compounded annually, for 8 years. ( a ) Will  this effectively protect the purchasing power o f   the original principal, given  an annual inflation rate o f   8%? ( b ) If so, by  how much? Ans. ( a ) yes; ( b ) $474.34
- 1.29 Let the person in Problem 1.28 be in  the 45%  tax bracket and pay taxes on all the interest received. (a) Will  the after-tax purchasing power o f   the original principal be protected? ( b ) Why? Ans. ( a ) no; ( b ) $512.57 in  purchasing power will  be lost
- 1.30 What amount of money is equivalent to receiving $5000 two years from today, if  interest is compounded quarterly at the rate o f 2? / 0 per quarter? Ans. $4103.73
- 1.31 On the first day o f   the year, a man deposits $1000 in  a bank at 8%  per year, compounded annually. He withdraws $80.00 at the end of   the first  year, $90.00  at  the end o f   the second year, and  the remaining balance at the end o f   the third year. ( a ) How much  does he withdraw at the end of  the third year? ( 6 ) What is his net  cash flow? ( c ) How much better off,  in terms  o f   net cash flow, would he have been i f   he  had not made the withdrawals at the ends o f   years one and two? Ans. ( a ) $1069.19; ( b ) $239.19; ( c ) $20.51

## Annual Compounding

## 2.1 SINGLE-PAYMENT, COMPOUND-AMOUNT FACTOR

Suppose that a given sum of  money, P, earns interest at a rate i, compounded annually. We have already seen  (Section 1.4)  that the total amount of  money, F, which  will  have accumulated from an investment of  P dollars after n  years is given  by F = P(1+ i)". The ratio

<!-- formula-not-decoded -->

is  called  the  single-payment,  compound-amount  factor. Numerical  values  of this  factor  may  be calculated from (2.1)  or obtained from compound interest tables such as those shown in Appendix A.

A  fuller  notation,  (FIP, i%, n), is  helpful  when  setting  up the solution  to a  compound interest problem.

Example 2.1 A student  deposits $1000 in  a  savings  account  that  pays  interest  at  the rate of  6%  per  year, compounded annually. If all of  the money is allowed to accumulate, how much money will the student have after 12 years?

We wish  to solve for F, given P, i,  and n. Thus,

<!-- formula-not-decoded -->

where the factor (FIP, 6%, 12) was evaluated from Appendix A.

## 2.2 SINGLE-PAYMENT, PRESENT-WORTH FACTOR

The single-payment,  present-worth  factor  is  the  reciprocal  of the  single-payment,  compoundamount factor:

<!-- formula-not-decoded -->

The expanded  notation  for  this  quantity  is  (PIF, i0/0, n).  Numerical  values  for  the single-payment, present-worth factor can be obtained directly from (2.2) or from a set of  tables such as those given in Appendix A.

Example 2.2 A certain sum of  money will  be deposited  in  a savings account that  pays interest at the rate of 6% per year, compounded annually.  If  all of  the money is allowed to accumulate, how much must be deposited initially  so that $5000 will have accumulated after 10 years?

We wish  to solve for P, given  F ,  i, and n. Thus,

<!-- formula-not-decoded -->

where Appendix A gives (FIP, 6%, lo)-' = (1.7908)-' = 0.5584.

## 2.3 UNIFORM-SERIES, COMPOUND-AMOUNT FACTOR

Let  equal  amounts of money,  A,  be deposited  in  a  savings  account  (or  placed  in  some  other interest-bearing  investment)  at  the  end  of  each  year,  as  indicated  in  Fig.  2-1.  If  the  money  earns interest at a rate i,  compounded annually,  how much  money will have accumulated after  n  years?

The ratio

Fig. 2-1

<!-- image -->

To answer this question, we note that after n years, the first year's deposit will have increased  in value to

<!-- formula-not-decoded -->

Similarly,  the second year's deposit will  have increased  in  value to

<!-- formula-not-decoded -->

and so on. The total amount accumulated will thus be the sum of  a geometric progression:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

is called the uniform-series, compound-amount factor. Numerical values of  this factor can  be obtained directly,  using (2.3) in  conjunction with  an  electronic calculator, or from a set  of  compound  interest tables  such  as  those  given  in  Appendix  A. The  extended  notation (FIA,  i0/o,  n ) is  helpful  when solving compound interest  problems involving a uniform series.

Example 2 . 3 A student plans to deposit $600 each year in  a savings account, over a period  of  10 years. If  the bank  pays  6%  per  year,  compounded  annually,  how  much  money  will  have  accumulated  at  the  end  of  the 10-year period?

<!-- formula-not-decoded -->

## 2.4 UNIFORM-SERIES, SINKING-FUND FACTOR

The uniform-series, sinking-fund  factor is the reciprocal of  the uniform-series, compound-amount factor:

<!-- formula-not-decoded -->

This quantity has the extended notation (AIF, i0/o, n).

Example 2.4 Suppose that a fixed sum of  money, A, will be deposited in a savings account at the end of  each year for 20 years. If  the bank pays 6% per year, compounded annually, find A such that a total of  $50 000 will be accumulated at the end of  the 20-year period.

<!-- formula-not-decoded -->

## 2.5 UNIFORM-SERIES, CAPITAL-RECOVERY FACTOR

Let us now consider a somewhat different situation involving uniform annual payments. Suppose that a given sum of  money, P, is deposited in  a savings account where it earns interest at a rate i per year, compounded annually. At the end of  each year a fixed amount, A, is withdrawn  (Fig. 2-2). How large should A be so that the bank account will  just be depleted at the end of  n years?

Fig. 2 2

<!-- image -->

We can  make use of  previously defined factors to solve this problem, since

<!-- formula-not-decoded -->

Substituting (2.4) and (2.1) into (2.5), we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

is called  the  uniform-series, capital-recovery  factor.  Numerical  values of  this factor can  be computed using  (2.6) and  an  electronic calculator,  or  they  can  be obtained  from  a  set  of  compound  interest tables such as those given in Appendix A. Symbolically, the uniform-series, capital-recovery factor is written as (AIP, i%, n).

Example 2.5 An engineer who is about to retire has accumulated $50 000 in a savings account that pays 6%  per year, compounded annually. Suppose that the engineer wishes to withdraw a fixed sum of  money at the end of each year for 10 years. What is the maximum amount that can be withdrawn?

<!-- formula-not-decoded -->

The ratio

## 2.6 UNIFORM-SERIES, PRESENT-WORTH FACTOR

The uniform-series,  present-worth factor is  the  reciprocal  of  the  uniform-series,  capital-recovery factor:

<!-- formula-not-decoded -->

The extended notation is (PIA, i%, n).

Example 2.6 An engineer who is planning his retirement has decided  that he will have to withdraw $10 000 from his savings account at the end of  each year. How much money must the engineer have in the bank at the start  o f his  retirement,  if  his  money earns 6% per  year,  compounded  annually, and  he is planning a  12-year retirement  (i.e.,  12 annual  withdrawals)?

<!-- formula-not-decoded -->

## 2.7 GRADIENT SERIES FACTOR

A  gradient  series is  a  series  of  annual  payments  in  which  each  payment  is  greater  than  the previous  one by  a  constant  amount,  G.  Let  us  develop  the future  worth  of  a  gradient  series  by visualizing it in terms of  its component parts, as in Fig. 2-3. Each level constitutes a uniform series, to which (2.3)  applies; thus,

<!-- formula-not-decoded -->

Fig. 2-3

<!-- image -->

The last n -1  terms on the right  may be rearranged to give

<!-- formula-not-decoded -->

and, summing the geometric progression, we obtain

<!-- formula-not-decoded -->

Now consider a series of n uniform annual payments, A. + A, where A. has the same value as in the above series of  gradients and where A is determined such  that the future worth of  this uniform series is the same as that given  by (2.8). Thus,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (2.9) permits  direct  calculation  of the gradient series factor,  (AIG, iO/o, n). Alternatively, since

<!-- formula-not-decoded -->

the factor can  be evaluated from a table of (AIF, iO/o, n).

Example 2.7 An engineer is planning for a 15-year retirement.  In  order to supplement his pension  and offset the anticipated effects of  inflation, he intends to withdraw $5000 at the end of  the first year, and to increase the withdrawal by $1000 at the end of  each successive year (Fig.  2-4). How much money must the engineer have in his savings account at the start of  his retirement, if  money earns 6%  per year, compounded annually?

<!-- image -->

from which

We want to obtain the value of P, given  the values of Ao,  G , i,  and n. We first obtain  a  series of  uniform withdrawals A' equivalent to the series of  gradients.

<!-- formula-not-decoded -->

We can now calculate P as follows:

<!-- formula-not-decoded -->

A  more concise, and the preferable, way to solve this problem is to write

<!-- formula-not-decoded -->

The gradient series factor can also be used with  a decreasing series of  gradients.

- Example 2.8 How  much  money  must  initially  be  deposited  in  a  savings  account  paying 5% per  year, compounded annually, to provide for ten annual withdrawals that start at $6000 and decrease by $500 each year? In  this case, A 0 = $6000 and G = -$500. Thus,

<!-- formula-not-decoded -->

## Solved Problems

- 2.1 A woman deposits $2000 in  a savings account that pays interest at 8% per year, compounded annually.  If  all the money is allowed to accumulate, how much will she have at the end of  (a) 10 years? ( b ) 15 years?
- (a) F = P x (F/P,  8%,  10) = $2000(2.1589) = $4317.80
- ( b )
- F = P x (FJP,  8%,  15) = $2000(3.1722) = $6344.40

<!-- formula-not-decoded -->

- 2.2 How much money must be deposited in  a savings account so that $5500 can  be withdrawn 12 years hence, if   the interest rate is 9%  per year, compounded annually, and if  all the interest is allowed to accumulate?

<!-- formula-not-decoded -->

- 2.3 Repeat Problem 2.2 for an interest  rate of  7i0/0  per year, compounded annually.

<!-- formula-not-decoded -->

Appendix A does not include tabular entries for i = 79/0 per year; therefore we will make direct use of (2.2).

<!-- formula-not-decoded -->

- 2.4 Suppose that a person deposits $500 in  a savings account at the end of  each year, starting now, for the next 12 years. If  the bank  pays 8%  per year, compounded annually, how much  money will  accumulate by  the end of  the 12-year period?

<!-- formula-not-decoded -->

Alternatively,

- 2.5 Repeat Problem 2.4 for an interest  rate of 6+% per year, compounded annually.

<!-- formula-not-decoded -->

- 2.6 How much  money  must  be deposited  at  the end of  each  year in  a savings account that  pays 9% per year, compounded annually, in order to have a total of  $10 000 at the end of  14 years?

<!-- formula-not-decoded -->

- 2.7 A man has deposited $50 000 in  a  retirement income plan  with  a local  bank. This bank  pays 9%  per year, compounded annually, on such deposits. What is the maximum amount the man can  withdraw at the end of  each year and still  have the funds last for 12 years?

From Appendix A,

<!-- formula-not-decoded -->

- 2.8 Repeat Problem 2.7 for an interest rate of 8:% per year, compounded annually.

This problem  must be solved by direct use o f   (2.6).

<!-- formula-not-decoded -->

- 2.9 Mr. Smith  is  planning  his retirement. He has decided  that he needs to withdraw $12000 per year from his bank account to supplement his other income from Social Security and a private pension  plan.  How  much  money  should  he  plan  to  have  in  the  bank  at  the  start  of his retirement, if  the  bank  pays 10%  per year, compounded annually,  and  if  he wants  money to last for a 12-year retirement period?

<!-- formula-not-decoded -->

- 2.10 Mr. Doe is trying  to decide whether to put  his money  in  the XYZ Bank  or the ABC Bank. The XYZ Bank pays 6% per annum interest, compounded annually; the ABC Bank pays 5% per annum interest, compounded quarterly. Mr. Doe expects to keep his money  in  the bank for 5 years. Which bank should  he select?

From Appendix A,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

He should choose XYZ, which offers the greater return  per dollar.

- 2.11 If, in  Problem 2.10, Mr. Doe plans to keep his money in  the bank for 10 years, is XYZ still the best choice?

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

It  is; in  fact, the advantage of  XYZ increases with  the longer time period.

- 2.12 Mr. Franklin wants to  save for a new sports car that he  expects will cost $38 000 four and one-half years from now. How much money will he have to  save each year and deposit in a savings account that pays 6% per year, compounded annually, to buy the car in four and one-half years?

Since the interest is compounded only once a year, Mr. Franklin will have to accumulate the entire $38  000 during the first four years. Therefore,

<!-- formula-not-decoded -->

- 2.13 In  Problem  2.12,  suppose  that  Mr. Franklin  makes a  deposit  at  the beginning of  each  year, rather than at the end. How much money must be deposited each year?

There will  now  be five deposits, each  o f   size A. At  the end of 4 years, the first deposit will  have accumulated to

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and the next four deposits to

Hence

Solving, A = $6707.38.

- 2.14 A father wants to set aside money for his 5-year-old son's future college education. Money can be deposited  in a bank  account  that  pays  8%  per  year, compounded  annually.  What  equal deposits should  be made by  the father, on  his son's 6th  through 17th  birthdays,  in  order to provide $5000 on the son's 18th, 19th, 20th, and 21st birthdays?

On the son's 17th birthday, the deposits must have accumulated to

<!-- formula-not-decoded -->

Thus, the deposit size, A, must satisfy

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 2.15 Dr. Anderson  plans to make a series of  gradient-type withdrawals from  her savings account over  a  10-year  period,  beginning  at  the  end  of the  second  year.  What  equal  annual  withdrawals would  be equivalent to a withdrawal of  $1000 at the end of  the second year, $2000 at the end of the third year,. .  .  , $9000 at the end of  the 10th year, if  the bank pays 9%  per year, compounded annually?

In  the notation o f   Section 2.7, A o = 0, G = $1000. Hence, from Appendix A,

<!-- formula-not-decoded -->

- 2.16 Mr. Jones is planning a 20-year retirement; he wants to withdraw $6000 at the end of  the first year, and  then  to increase  the withdrawals by $800 each  year to offset  inflation. How  much money should he have in his savings account at the start of  his retirement, if the bank pays 9% per year, compounded annually, on his savings?

Using an analog o f   (2.11) and the tables in  Appendix A,

<!-- formula-not-decoded -->

- 2.17 The ABD Company is building a new plant, whose equipment maintenance costs are expected to be $500 the first year, $150 the second year, $200 the third year, $250 the fourth year, etc., increasing by $50 per year through the 10th year. The plant is expected to have a 10-year life. Assuming the interest rate is 8O/0,  compounded annually,  how much should the company plan to set  aside now in  order to pay for the maintenance?

The cash flow diagram is given in  Fig. 2-5. First we compute the present worth at the end of  year 1 [see (2.1  I)] :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The present worth at the end o f   year 0 is thus

<!-- formula-not-decoded -->

<!-- image -->

- 2.18 Slick Oil Company is considering the purchase of  a new machine that will last 5 years and cost $50 000; maintenance will cost $6000 the first year, decreasing by $1000 each year to $2000 the fifth year. If  the interest  rate is 8%  per year, compounded annually, how much money should the company set aside for this machine?

Proceeding as in  Problem 2.16, and including the purchase price,

<!-- formula-not-decoded -->

- 2.19 Mr. Holzman estimates that the maintenance cost of  a new car will be $75 the first year, and will  increase by $50 each subsequent year.  H e  plans to keep the car for 6 years. H e  wants to know how much money to deposit in a bank account at the time he purchases the car, in order t o  cover  these  maintenance  costs.  His  bank  pays  5% per  year,  compounded  annually,  on savings deposits.

The P/A and A/G factors must be evaluated directly from (2.7) and (2.9). Thus, and

<!-- formula-not-decoded -->

## Supplementary Problems

- 2.20 An investment plan  pays 15%  per year,  compounded  annually. How  much would have to be invested every year so that $40000 will be accumulated  by  the end of  10 years? Ans. $1970.08
- 2.21 Repeat Problem 2.20 for an interest rate of  13% per year, compounded annually. Ans. $2119.48
- 2.22 Mr.  Doe borrowed  $1000 from  his bank  at  8%  per  year,  compounded  annually.  He can  (i) repay  the $1000 together with the interest at the end of  3 years, or (ii) pay the interest at the end of  each year and repay the $1000 at the end of  3 years. By  how much is (ii) better than (i)? Ans. $259.71 -$240.00 = $19.71
- 2.23 Suppose that $2000 is invested now, $2500 two years from now, and $1200 four years from now, all at 8% per year, compounded annually. What will be the total amount 10 years from now? Ans. $10 849.42
- 2.24 Repeat Problem 2.23 for an interest rate of  79/0 per year, compounded annually. Ans. $10 639.21
- 2.25 On  the day  his son  was  born,  a father  decided  to establish  a fund  for  his son's  college education. The father wants the son  to be able to withdraw $4000 from  the fund on his 18th birthday, again on his 19th birthday, again on his 20th birthday, and again on his 21st birthday. If  the fund earns interest at 9%  per year, compounded annually, how much should the father deposit at the end of  each year, up through the 17th year? Ans. $350.49
- 2.26 Repeat Problem 2.25 for an interest rate of  89/0 per year, compounded annually. Ans. $370.95
- 2.27 A new machine is expected to cost $6000 and have a life of  5 years. Maintenance costs will be $1500 the first year, $1700 the second year, $1900 the third year, $2100 the fourth year, and $2300 the fifth year. To pay for the machine, how much should be budgeted and deposited in a fund that earns (a) 9%  per year, compounded annually? (b) 1&amp;/0 per year, compounded annually? Ans. (a) $13 256.69; (6) $12 962.59
- 2.28 The ABC Company has contracted to make the following payments:  $10 000 immediately;  $1000 at the end of year 1; $1500 at the end of  year 2; $2000 at the end of  year 3; $2500 at the end of  year 4; $3000 at the end of year 5. What fixed amount of  money should  the company plan to set aside each year, at 8% interest per year, compounded annually, in order to make the above payments? Ans. $4427.82
- 2.29 Suppose that someone deposits $2500 in  a savings account  at the end of  each year for the next 15 years. How much money will the person have by the end of  the 15th year if  the bank pays (a) 8'10,  (b) 69/0, per year, compounded annually? Ans. (a) $67 880.28; (b) $61 626.00
- 2.30 Mr.  Jones has deposited  his life savings of  $70 000  in  a  retirement  income plan  with  a local bank. The bank  pays (a) 10°h, (b) l l h ,   per year, compounded  annually, on such deposits.  What is the maximum fixed amount Mr. Jones can withdraw at the end of each  year and still have the funds last for 15 years? Ans. (a) $9203.16; (b) $9869.27
- 2.31 Mr. White is planning to take early retirement. He has decided that he needs $15 000 per year to live on, for the first 5 years of  his retirement; after that, his Social Security and other pension plans will  provide him an  adequate retirement  income.  How  much  money  must  he have in  the bank  for his 5-year early retirement period,  i f the  bank  pays  (a)  10°h,  (b)  &amp;/o, per  year,  compounded  annually,  on  the funds? Ans. (a) $56 861.80; (b) $57 968.26
- 2.32 Ms. Frank is planning for a 25-year retirement  period and wishes to withdraw a portion of  her savings at the end of  each year. She plans to withdraw $10 000 at the end of  the first year, and then to increase the amount of  the withdrawal  by $1000 each year, to offset inflation. How  much money should  she have in her savings account at  the start  of  the retirement  period,  i f the  bank  pays (a) 9' 1 0 , (b) 7:%, per  year, compounded annually? Ans. (a) $175 152.28; (b) $205 435.72

- 2.33 How much  money would  have to be saved at (a) 8%, (b) 89h, per year, compounded annually, each year for the next 10 years if  $50 000 is needed at the end o f   the  10th year? Ans. (a) $3451.47;  (b) $3410.71
- 2.34 A freshman college student, who owns a car, plans to buy a motorcycle. The student expects to save an increasing amount of   money on travel every year he is in college, as he will make less use o f   his car each year. How much money should he plan to save and put in  the bank from his job this summer, in order to pay  his  travel  costs for  his  remaining 3  years o f college? Assume  that  the  bank  pays  8%  per  year, compounded annually, and that his travel costs will be $900 the first year, $700 the second year, and $500 the third year. Ans. $1830.39
- 2.35 A father wants to set aside money for his 8-year-old daughter's future education, by  making  monthly deposits to a bank account that pays 8%  per year, compounded annually. What equal monthly deposits must  the father  make- the  first  1  month  after her 9th  birthday and  the last  on  her 17th  birthday- in order for her to withdraw $4000 on each of her next four birthdays (the 18th through the 21st)? Am. $103.80
- 2.36 Suppose $5000 is deposited in  a savings account that pays interest at 8%  per year, compounded annually. I f   no withdrawals are made, how long will it  take to accumulate $12 000? Ans. 12 years (actually, the amount accumulated at the end o f   12 years will  be $12 590.85)
- 2.37 Repeat Problem 2.36 for an interest rate of  69/0  per year, compounded annually. Ans. 14 years
- 2.38 Suppose that $1000 is deposited in the bank at the end o f   each year. How long will it take to accumulate $20 000 i f   the interest rate is 6%  per year, compounded annually? Ans. 14 years (actually, $21 015.07 will have accumulated at the end of  14 years)
- 2.39 Repeat Problem 2.38 for an interest rate o f   5 : % per year, compounded annually. Ans. 15 years
- 2.40 Ms. Brown deposits $750 in a savings account at the beginning o f   each year, starting now, for the next 10 years.  I f   the  bank  pays  (a) 7%, (b) 5:%,  per  year, compounded annually, how  much  money  will  Ms. Brown have accumulated by  the end of  the 10th year? Ans. (a) $11  087.70; (b) $10 332.09

## Chapter 3

## Algebraic Relationships and Solution Procedures

## 3.1 RELATIONSHIPS BETWEEN INTEREST FACTORS

The following  relationships  are  sometimes  helpful  in  interest  calculations,  particularly  when interest tables are used.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Example 3.1 Determine the value of (FIP,  8%,  37), using the tables presented in Appendix A. The numerical value of (FIP,  8%,  37) is not included in  the tables; however, from (3.1),

<!-- formula-not-decoded -->

(3.1),

Example 3.2 Determine the value of (FIA,  8%,  37), using the tables presented in  Appendix A. The numerical value of (FIA,  8%,  37) is  not  included  in  the tables; however, from (3.3) and

<!-- formula-not-decoded -->

All of  the right-hand terms can  now be evaluated using the tables in  Appendix A. Thus,

<!-- formula-not-decoded -->

Example 3.3 Estimate the value of (AIP,  51%,  63).

From (3.6), (AIP,  5q%,  63) = 0.055. (The correct value, to four decimal places, is 0.0570.)

In  addition t o  the above relationships, there are a  number of  others that have been discussed in Chapter 2. Specifically,  the reader is reminded of  the reciprocal relationships

<!-- formula-not-decoded -->

and various product relationships such as

<!-- formula-not-decoded -->

## 3.2 LINEAR  INTERPOLATION

If  a  required compound interest factor falls between two tabulated values, it may be desirable or necessary  to use  linear  interpolation  to approximate that  factor.  Let ( x l ,   y l ) and ( ~ 2 , y2) be known tabulated  points.  We wish  to determine the value of y corresponding to some given value x, where xl &lt; x &lt; x2. Then, by direct proportionality, we can  write

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

or, as more commonly applied in  practice,

Solving for y,

<!-- formula-not-decoded -->

Example 3.4 Approximate (FIP,  8%,  37), using the tabulated values in  Appendix A and linear interpolation. From Appendix A, (FIP, 8%,  35) = 14.7853 and (FIP,  8%, 40) = 21.7245. Therefore,

<!-- formula-not-decoded -->

The correct answer, from (2.1), is 17.2456.

Example 3.5 Approximate (AIP,  8%,  37), using the tabulated values in  Appendix A and linear interpolation. From Appendix A, (AIP,  8%,  35) = 0.08580 and (AIP,  8%,  40) = 0.08386. Therefore,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The correct answer, from (2.6), is 0.08492.

Example 3.6 Approximate (FIA,  &amp;lo, 15) by  interpolating  linearly  between  the  tabulated values  given  in Appendix A.

From Appendix A, (FIA,  6%,  15) = 23.2760 and (F/A,  7 % ,   15) = 25.1290 (note that these values come from two different tables). Hence,

<!-- formula-not-decoded -->

The correct answer, from (2.3), is 24.6504.

## 3.3  UNKNOWN NUMBER OF YEARS

Sometimes we  require the number of  years,  n,  that  corresponds  to a  given  compound interest factor  and  a  given  annual  interest  rate, i. Solving  the  appropriate  formulas  from  Chapter  2  by logarithms, we obtain the results displayed in Table 3-1. Formula (2.9)  cannot be solved exactly for n, given AIG and i ; in  this case, a graphical solution or linear interpolation  is employed.

Table 31

| Factor     | Number of Years                                                   |
|------------|-------------------------------------------------------------------|
| F/P or PIF | n = log (FIP) - -log (PIF) log (1 + i ) log (1 + i)               |
| FIA or AIF | log [1+i(F1A)I = log I+- n = log (1 + i ) ( A f F ) log (1 + i)   |
| PIA or AIP | -log (1 - - &) n = -log [ I - i(P/A)] - log (1 + i ) log (1 + i ) |

Example 3.7 How many years will be required for a given sum of   money to triple, i f   it is deposited in  a bank account that pays 6% per year, compounded annually?

We require n, given FIP = 3 and i = 0.06. From Table 3-1,

<!-- formula-not-decoded -->

But, since the interest is compounded only at the end o f   each year, the calculated value for n  must be an integer. Hence n = 19 (corresponding to FIP = 3.0256) is the correct solution.

Example  3.8 Determine  the  value  o f n  corresponding  to AIF = 0.01, i f i = 7% per  year,  compounded annually.

From Table 3-1,

<!-- formula-not-decoded -->

The required number of  years is therefore 30.

Example 3.9 Determine the value of   n corresponding to AIG = 11.6 and i = 7%, compounded annually, using the following known points (n, AIG) (all at i = 7%): (35, 10.6687), (40, 11.4234), (45,12.0360).

From  the  graph  o f the  data,  Fig. 3-1, we  can  see  that  the  value  o f n  corresponding  to AIG = 11.6 is approximately 41.4.

Fig.  3-1

<!-- image -->

The value of n can also be approximated by  interpolating linearly between the second two data points:

<!-- formula-not-decoded -->

Since the interest is compounded annually, n can only take on integer values. Thus, n = 41 comes closest to satisfying the given condition that AIG = 11.6.

## 3.4 UNKNOWN INTEREST RATE

Another situation  that frequently  arises  is  the  need  to solve  for  the annual  interest  rate  that corresponds to  a given compound interest factor  and a specified number  of  years. If  the  given compound interest factor is either F/P or P/F, then  the value of  i can  be obtained explicitly  as

<!-- formula-not-decoded -->

When  one of  the  remaining  five  interest  factors  is  specified,  however,  it  is  necessary  to  utilize  a numerical or graphical solution procedure, or to interpolate linearly between tabulated  values. If  the given  interest  factor  is  not  tabulated  for  the  specified value  of n,  double  interpolation  will  be required.

Example 3.10 Determine the value of  i  corresponding  to FIA = 1000 and n = 38,  using  the  known  values displayed in Table 3-2.

Table 3-2

|     |          | FIA                          |
|-----|----------|------------------------------|
| 12% | 35 40 45 | 431.6635 767.0914 1358.2300  |
| 15% | 35 40 45 | 881.1702 1779.0904 3585.1286 |

We first obtain an  interpolated value o f F/A for i = 12% and n = 38:

<!-- formula-not-decoded -->

Then we obtain an interpolated value o f FIA for i = 15% and n = 38:

<!-- formula-not-decoded -->

We can now interpolate between these calculated values to obtain the desired interest rate:

<!-- formula-not-decoded -->

A  more  accurate result  can  be  obtained  i f the  factors (FIA, 12%, 38) and (FIA, 15%, 38) are  evaluated directly from (2.3).  Thus,

<!-- formula-not-decoded -->

and now linear interpolation gives:

## 3 1 ALGEBRAIC RELATIONSHIPS AND SOLUTION PROCEDURES

<!-- formula-not-decoded -->

This latter method is preferable, provided a calculator is available to carry out the exponentiation.

## Solved Problems

- 3.1 Evaluate (a) (FIP, l o%, 44), ( b )   (AIF, 10°/o, 37).

<!-- formula-not-decoded -->

- (b) By (3.3) and (3.1),

<!-- formula-not-decoded -->

Hence, (AIF,  lo%,  37) = 11330.039 = 0.00303.

- 3 . 2 Estimate (a) (AIP, 8%, loo),  ( b )   (PIA, 20°/0, 50).
- ( a ) By (3.6), (AIP,  8%, 100) = 0.08 (Appendix A gives the correct value as 0.08004).

<!-- formula-not-decoded -->

The correct value is 4.9995.

- 3.3 Find (AIF, i%, n) from (a) (FIP,  i%, n), (b)  (PIC i%, n), ( c ) (Alp, i%, n).

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 3.4 Derive (3.1) without reference to (2.1).

Investing $1 for nl years  at i % annual  compound interest,  and  then  investing  the  accumulated amount for a further nl years at the same rate, must be equivalent to investing $1 for nl+ n2 years at iOh.

- 3 . 5 Derive (3.3) without reference to (2.3) or (2.1).

As shown in  Fig. 3-2, a uniform series o f n payments of $1 may  be considered as composed of   two parts: the first n -nl payments, whose total future worth at  the end of year n i s

<!-- formula-not-decoded -->

and the uniform series o f   the remaining nl payments, whose future worth is

<!-- formula-not-decoded -->

The sum of ( 1 ) and (2) must be the future worth o f   the entire series, (FIA,  i %,  n).

as before.

- 3 . 7 Use linear interpolation and the tables given in  Appendix A to evaluate (a) (PIF, 6%, 52), (b) (PIA, 89h, lo), ( c ) (AIG, 13%,  48).
- (a) First interpolate for (FIP,  6 % ,   52), then take the reciprocal.

. .

52

-

50 (24.6503

-

18.4204)

(Fly,  6 %,  52)

:

18.4202

+  -

55

-

50

<!-- formula-not-decoded -->

- (b) First interpolate for (AIP, 8%0,  lo), then take the reciprocal.

=

(0.15582

-

=

20.9122

=

0.14903)

0.15073

( A l p ,   8%,  10)

0.14903

+

8'25

-

8'00

<!-- formula-not-decoded -->

- ( c ) First interpolate on n to obtain (AIG,  12%,  48) and (AIG,  15%,  48); then interpolate on i to obtain (AIG,  13%,  48).

<!-- formula-not-decoded -->

- 3.8 How many  years will  be required for a sum o f   money  to quadruple,  if  it  is deposited  in  a bank  account that pays 6p/n per year, compounded annually?

<!-- formula-not-decoded -->

or 22 years, if n must  be an  integer.

Fig. 3-2

<!-- image -->

It  is obvious from Fig. 3-2 that the sum (1)  above is equal to

<!-- formula-not-decoded -->

Hence we have the following, more compact version of (3.3):

<!-- formula-not-decoded -->

- 3.6 Rework Problem 3.l(b), using (3.10).

<!-- formula-not-decoded -->

- 3.9 Determine  the  value  of n  corresponding  to PIA = 12,  i f i = 8%  per  year,  compounded annually.

<!-- formula-not-decoded -->

or 42, i f n must be an integer.

- 3.10 Use linear interpolation to  determine the value of  n corresponding to AIG = 5.4000 and i = 8% per year, compounded annually.

From the tables in  Appendix A,

<!-- formula-not-decoded -->

Then

Therefore, for AIP = 0.15000,

<!-- formula-not-decoded -->

## Supplementary Problems

- 3.13 Evaluate,  using (3.1) and  Appendix  A, ( a )  (FIP, 10°h,41),  (b) (FIP,  12%,43),  (c) (FIP960/~,57). Am.  (a)  49.7852; (b)  130.7299; (c)  27.6971
- 3.14 Evaluate,  using (3.3) or (3.10) and the tables  in Appendix  A, ( a ) (FIA,  lo%,  41),  ( b ) (FIA,  12%,  4%  (c)  (FIA, 6%, 57). Ans. ( a ) 487.8518; (b)  1081.0826; ( c )   444.9517
- 3-15 Evaluate,  using (3.4) and  Appendix  A, ( a )   (PIA,  5%,  52),  ( b )  ( H A ,   9%,  3% ( c )  (PIA,  1 2 % ~ ~ 43)Am. ( a )   18.4181; ( b )   10.7255; ( c )   8.2696
- 3.16 Evaluate, using (3.5) and the tabular values of (AIP, i % , n ) given in Appendix A, ( a )   (AIF,  4%,  20), (b) (AIF,  15%,  8), (c)  (AIF,  12%,  40). Ans. ( a )   0.03358; (b)  0.07285; (c)  0.00130
- 3.17 Estimate the following factors, using (3.6), and compare with  the correct  values as given  by  (2.6): ( a ) (AIP,  8%,80), (b)  (AIP,  &amp;/o, 120). ( c )   (AIP,  19.08%, 100). Ans. ( a )  0.08 (correct  value, 0.0802); (b) 0.0475 (correct  value, 0.0477); (b) 0.1908 (correct  value, 0.1908)

<!-- formula-not-decoded -->

- 3.11 A bank will return $2345 on  a  10-year  certificate  of  deposit  that originally cost $1000. What interest rate, compounded annually, is the bank paying?

<!-- formula-not-decoded -->

- 3.12 By interpolation, determine the value of  i corresponding to AIP = 0.15000 and n = 12.

From the tables in  Appendix A, we find that for n = 12:

<!-- formula-not-decoded -->

- 3.18 From the interest tables in  Appendix A, determine the value o f   each o f   the following compound interest factors  using  linear  interpolation.  Compare  each  value  with the  exact  answer  obtained  from  the appropriate  formula  in Chapter  2. (a)  (FIP, 7210, 12),  (b) (FIP, 12%,  47), (c) (PIF, 5%,  20), (d) (FIA, 4%, 38), (e) (FIA, 42/0,38),  (f)  (AIF, 1 lt%  ,30), (g) (AIP, 5%, 57), (h) (AIP, 73/0,57),  (i) (PlA, 1@/0,30), (j) (AIG, 89/0,15), (k) (AIG, 13?/0,39).
- Ans. (a) 2.3852 (exact: 2.3818);  (b) 213.9934 (205.7061); (c) 0.3606 (0.3594); (d) 86.4762 (85.9703); (e) 92.0092 (101.7364); Cf) 0.004869 (0.00479); (g) 0.05333 (0.05330);  (h) 0.07391 (0.07387);  (i) 8.9125 (8.8675); (j) 5.5545 (5.5541); (k) 7.0591 (7.0146)
- 3.19 How many years (a whole number) will be required for a sum of.money to double i f   the interest rate is (a) 1O0/0, (b) 12%, ( c ) 13:%,  per year, compounded annually? Ans. (a) 8 years; (b) 7 years; (c) 6 years
- 3.20 How many years (a whole number) will be required to accumulate $10 000 i f   $500 is deposited at the end of   each year, and interest is payable at 6 ? / 0 per year, compounded annually? Ans. 14 years
- 3.21 A person has $80 000 in  a savings account that earns interest at 7% per year, compounded annually. I f the person withdraws $12000 at the end of each year, after how  many years (a whole number) will the savings be exhausted? Ans. 10 years
- 3.22 Use linear interpolation to determine the value of  n corresponding to AIG = 6.0000, i f i = 9% per year, compounded annually. Ans. 16.99
- 3.23 Repeat Problem 3.22 for an interest rate o f   11% per year, compounded annually. Am. 18.84
- 3.24 A man has entered into a contract in  which  he has agreed to lend $1000 to a friend, and the friend has agreed  to  repay  him  $1060.90  two  years  later.  What  annual  compound  rate  o f interest  is  the  man receiving on his $1000? Ans. 3%
- 3.25 The First  National Bank  advertises it  will  pay  $3869.70  in  cash  at  the end  o f   20  years to anyone who deposits  $1000.  Federal  Savings,  a  competitor,  advertises  that  it  pays  10%  per  year,  compounded annually, on all deposits left one year or more. Which bank is paying the higher interest rate, and by how much? Ans. Federal Savings, by  3%
- 3.26 A person who is about to retire has accumulated $100 000 in  a savings account. Suppose that the person withdraws $8195.23 from  the savings account at  the end o f   each  year for 20  years, at  which  time the account is totally depleted. What is the interest rate, based upon annual compounding? Ans. 5% per year
- 3.27 A person is considering entering into an  agreement with  an  investment company to deposit $1000 into a special account at the end o f   each year for 15 years. At  the end o f   the period, the person would be able to  withdraw  a lump sum  o f   $28 800.  At  what  rate  would  the  person  earn  interest, i f the interest was compounded annually? Ans. 8%  per year
- 3.28 A person is considering entering into an  agreement with an investment company to deposit $1000 into a special account at the end o f   the first year, $1100 at  the end o f   the second year, etc.,  increasing by  $100 each year. At the end o f   15 years the person would be able to withdraw a lump sum o f   $36 000. At what rate would the person earn interest, i f   the interest was compounded annually? Ans. 5.54%  per year

## Discrete,  Periodic  Compounding

## 4.1 NOMINAL AND EFFECTIVE INTEREST RATES

Many financial transactions  require  that  interest  be compounded  more often  than once a  year (e.g.,  quarterly,  monthly, daily, etc.).  In  such  situations,  there are  two  expressions for  the interest rate. The nominal  interest  rate,  r,  is expressed on  an  annual basis; this is  the  rate that  is  normally quoted when describing an  interest-bearing  transaction. The effective interest  rate, i, is the rate that corresponds  to  the  actual  interest  period.  The effective interest  rate  is  obtained  by  dividing  the nominal interest  rate by  m, the number of  interest  periods per year:

<!-- formula-not-decoded -->

Example 4.1 A bank claims to pay interest to its depositors at the rate of  6% per year, compounded quarterly. What are the nominal and effective interest rates?

The nominal interest rate is r = 6%. Since there are four interest periods per year, the effective interest rate is

<!-- formula-not-decoded -->

## 4.2 WHEN INTEREST PERIODS COINCIDE WITH PAYMENT PERIODS

When  the interest  periods  and  the payment  periods  coincide, it  is  possible to make  direct  use both  of  the compound  interest  formulas developed  in  Chapter 2 and the compound  interest tables presented  in  Appendix  A, provided  the interest  rate, i,  is  taken  to be the effective interest  rate for that  interest period.  Moreover,  the  number  of years,  n,  must  be  replaced  by  the  total  number  of interest  periods,  mn.

Example 4.2 An engineer  plans  to borrow  $3000 from his company  credit  union,  to be repaid in  24 equal monthly installments.  The credit  union  charges  interest  at  the rate of  1%  per  month  on  the  unpaid  balance. How much money must the engineer repay each month?

This  problem  can  be  solved  by  direct  application  of (2.6), since  the  interest  charges  and  the  uniform payments are both determined on a  monthly basis:

<!-- formula-not-decoded -->

We conclude that the engineer must repay $141.22 at the end of  every month for 24 months.

Alternatively, Appendix A gives (Alp, I%, 24) = 0.04707, whence

<!-- formula-not-decoded -->

If,  as  in  the  case  of  commercial  loans,  the  nominal  interest  rate  is  specified,  the  compound interest formulas of  Chapter 2 and/or Appendix A can still be used, with i replaced by  rlm, and n by mn.

EXAMPLE 4.3 An engineer  wishes to purchase an $80 000 home by making a down  payment of $20 000 and borrowing the remaining $60 000, which  he will  repay  on  a  monthly basis over the next 30 years.  If  the bank charges interest at the rate of @/o per year, compounded monthly, how much money must the engineer  repay each month?

Again applying (2.6),

<!-- formula-not-decoded -->

It  is interesting to note that the total amount of  money which  will be repaid to the bank is

<!-- formula-not-decoded -->

or three times the amount of  the original loan.

## 4.3 WHEN INTEREST PERIODS ARE SMALLER THAN PAYMENT PERIODS

If the  interest  periods  are  smaller  than  the  payment  periods,  then  the  interest  may  be  compounded several  times between  payments. One way to handle problems of  this type is to determine the effective  interest  rate for the given  interest  period, and then  treat each  payment separately.

Example 4.4 An engineer deposits $1000 in a savings account at the end of  each year. If  the bank pays interest at the rate of 6% per year, compounded quarterly, how much money will have accumulated in the account after 5 years?

The effective interest rate is i = 6%/4 = 1.5% per quarter; the first deposit accumulates for 16 quarters; etc.

<!-- formula-not-decoded -->

The FIP factors can be obtained from either (2.1) or Appendix A.

<!-- formula-not-decoded -->

Another procedure, which is usually more convenient, is to calculate an effective interest rate for the  given payment period,  and  then  to  proceed  as  though  the  interest  periods  and  the  payment periods coincided. This effective interest rate can  be determined as

<!-- formula-not-decoded -->

where a represents the number of  interest periods per payment period and r is the nominal interest rate for  that  payment  period.  If the  payment  period  is  one year,  then  a = m,  and  we  obtain  the following expression  for the effective annual interest  rate:

<!-- formula-not-decoded -->

Example 4.5 Rework Example 4.4 by  using an effective annual interest rate.

Here, r = 6% and a = m = 4, so that, by (4.3),

<!-- formula-not-decoded -->

We can now apply (2.3) t o  obtain

<!-- formula-not-decoded -->

which  agrees with Example 4.4 t o  within  roundoff  errors.

Appendix  B  contains  a  tabulation  of effective  annual  interest  rates  corresponding  to  various nominal interest  rates. This table may  be used in  place of (4.3), if  desired.

## 4.4 WHEN INTEREST PERIODS ARE LARGER THAN PAYMENT PERIODS

If  the interest  periods are larger  than  the payment periods, some of  the payments may not have been  deposited  for  an  entire interest  period.  Such  payments  do  not  earn  any  interest  during  that interest  period.  In other words, interest is earned only  by  those  payments that  have been deposited or invested for the entire interest  period.

Situations of  this type can  be treated in  the following manner:

- I. Consider all deposits that were made during the interest period to have been made at the end of  the interest  period (and therefore to have earned  no interest  during that interest  period).
2. Consider all withdrawals that were made during the interest period to have been made at the beginning of  the interest  period (again earning  no interest).
3. Then proceed as though the interest  periods and the payment periods coincided.

Example 4.6 A  person  has  $4000  in  a savings account  at  the  beginning o f a calendar  year; the  bank  pays interest at 6%  per year, compounded quarterly. Table 4-1 shows the transactions carried out during the calendar year; the second column gives the effective dates according to rules 1 and  2 above. To find  the balance in  the account at the end o f   the calendar year, we calculate the effective interest rate, 6%/4 = 1.5%  per quarter. Then, lumping the amounts at the effective dates and applying (2.1), we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Table 4-1

| Date                                                                                         | Effective Date                                                                           | Deposit                | Withdrawal                    |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|------------------------|-------------------------------|
| Jan. 10 Feb. 20 Apr. 12 May 5 May 13 May 24 June 21 Aug. 10 Sept. 12 Nov. 27 Dec. 17 Dec. 29 | Jan. 1 Mar. 31 Apr. 1 June 30 June 30 Apr. 1 Apr. 1 Sept. 30 July 1 Oct. 1 Dec. 31 Oct.1 | $1200 65 115 1600 2300 | $ 175 1500 50 250 800 350 750 |

## Solved Problems

- 4.1 A bank advertises that it pays interest at the rate of 10% per year, compounded quarterly. What effective interest rate is the bank  paying?

<!-- formula-not-decoded -->

- 4.2 An engineer has just borrowed $8000 from a local bank, at the rate of  1% per month on the unpaid  balance.  His  contract  states  that  he  must repay  the  loan  in 35 equal  monthly installments.  How much  money must he repay each month?

<!-- formula-not-decoded -->

- 4.3 A bank  pays interest  at the rate of  6%  per year, compounded monthly. If  a  person deposits $2500 in  a  savings account  at  the  bank,  how  much  money  will  accumulate  by  the end  of  2 years?

Equation (2.1), with the appropriate substitutions, gives

<!-- formula-not-decoded -->

Alternatively,  using the tables in Appendix A, we have

<!-- formula-not-decoded -->

- 4.4 A man plans to buy a $150 000 house. H e   wants to make a down payment of $30 000 and to take out a 30-year mortgage  for the remaining $120 000, at 10% per year, compounded monthly. How much  must he repay each month?

Equation (2.6), with the appropriate substitutions, gives

<!-- formula-not-decoded -->

The solution can also be approximated by use of (3.6):

<!-- formula-not-decoded -->

- 4.5 A  man  plans  to save  $1000 a  month  for the next  20  years,  at  10%  per  year,  compounded monthly. How much money will he have at the end of  20 years?

Equation (2.3), with the appropriate substitutions,  gives

<!-- formula-not-decoded -->

- 4.6 Repeat Problem 4.5 using quarterly compounding.

<!-- formula-not-decoded -->

Note that this is much less than the value obtained using monthly compounding.

- 4.7 What is the present value of  a stream of  monthly payments of  $500 each over 10 years, if  the interest  rate is  1O0/0  per annum, compounded monthly?

Equation (2.7), with the appropriate substitutions, gives

<!-- formula-not-decoded -->

- 4.8 Repeat Problem 4.7 using daily compounding. For computational simplicity, assume 30 days in each month (many banks do this).

Here,  r = 10%/12 = 0.00833333 and cu = 30; hence by (4.2), the effective monthly interest rate is

<!-- formula-not-decoded -->

Now use (2.77, as before.

<!-- formula-not-decoded -->

- 4.9 How much money must be deposited in  a savings account each month to accumulate $10 000 at  the end of 5 years,  if  the bank  pays interest  at  the rate of 6% per year, compounded (a) monthly? ( b ) semiannually? ( c ) quarterly? (d) daily?

In  each case use (2.4), with the appropriate substitutions.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

or $872.3016 = $145.38 per  month.

<!-- formula-not-decoded -->

or $432.4513 = $144.15

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 4.10 Using a suitable version of (2.9), evaluate AIG for r = 12%, compounded monthly, and n = 2 years. Compare the result with  the tabulated value in  Appendix A.

<!-- formula-not-decoded -->

Appendix A gives (AIG, I%, 24) = 11.0237.

- 4.11 Mrs. Carter deposits $100 in the bank at the end of  each month. If the bank pays (a) 6% per year, ( b ) 7%  per year, compounded monthly, how much  money will she have accumulated at the end of 5 years?

- ( a ) The effective monthly interest rate is 6%/12 = 0.5%. There will  be a total o f 5 X 12 = 60 monthly payments. Hence, using Appendix A,

<!-- formula-not-decoded -->

- ( b ) The effective monthly interest rate is 7%/12=0.583333%. As the tabulated value of (FIA,  0.583333%, 60) is  not  readily  available, we  interpolate linearly between (FIA,  0.5%, 60) and (FIA,  0.75%, 60).

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

Another (and more accurate) way  to solve this problem is to apply (2.3):

<!-- formula-not-decoded -->

- 4.12 In Problem 4.11, suppose that Mrs. Carter deposits $100 a month during the first year, $110 a month during the second year, $120 a  month during the third year, etc. How much will have accumulated  at the end of  5 years if  the interest rate is 6%  per year,  compounded  monthly?

Treating each year separately,

<!-- formula-not-decoded -->

The required numerical values can  be obtained from Appendix A (using interpolation in some cases), or from (2.1) and (2.3).

<!-- formula-not-decoded -->

## Supplementary Problems

- 4.13 What is the effective annual interest rate if  the nominal interest rate is 6%, compounded monthly? Ans. 6.1678% per year
- 4.14 How  many  years will  be  required  for  a sum  o f money  to  double, if  the  annual  interest  rate  is l o %, compounded quarterly? Ans. n = 5.86 years (6 years, i f n must be an integer)
- 4.15 Mr. Smith plans to deposit money in  a bank  that pays 10% interest per year, compounded daily. What effective rate o f   interest will  he receive ( a ) yearly? ( b ) semiannually? Ans. ( a )  10.515% ; ( b )   5.0625%
- 4.16 A bank pays interest at the rate of  12%  per year, compounded monthly. If  a man deposits $3000 in the bank and leaves it  for 5 years, how  much  money will accumulate, according to ( a ) (2.1)? (b) Appendix A? Ans. ( a )   $5450.09; (b)  $5450.10
- 4.17 A  person deposits $2000 i n   a savings account. If all of the money  is  allowed to accumulate, how  much will  the  person  have  at  the  end  of 5 years,  given  a  nominal  interest  rate  o f 6%, compounded ( a ) annually? ( b ) quarterly? ( c ) monthly? (d) daily? Use the tables in  Appendix A to obtain the answers whenever possible. Ans. ( a )   $2676.40; (b)  $2693.80; ( c )   $2697.80; ( d )   $2699.65

- 4.18 What amount of  money is equivalent to receiving $8000 three years from today, if  the interest rate is 8% per year, compounded semiannually? Ans. $6322.52
- 4.19 A bank pays 6%  interest per year, compounded quarterly. To what amount will a $5000 deposit grow i f left in  that bank for 10 years? Ans. $9070.09
- 4.20 Repeat Problem 4.19 for annual compounding. Ans. $8954.24
- 4.21 Calculate the amount of   money that you would have in  your savings account at the end o f   12 months i f you  made the following deposits:

| End of Month   |     |   3 |   6 |   7 |   8 |   11 |
|----------------|-----|-----|-----|-----|-----|------|
| Deposit, $     | 200 |  90 |  70 |  75 |  85 |   70 |

Assume  that  the  bank  pays 6%  interest per  year, compounded semiannually, and  that it  pays simple interest on  any interperiod deposits. Ans. $611.73

- Calculate the balance in  Mr. Warren's account at the end of the year, i f   he deposits $100 each at the ends of months 1 and  6,  and  $200  each  at  the  ends  o f months  7  and  9.  His  bank  pays  8%  per  year, compounded quarterly, and simple interest on the interperiod deposits. Ans. $622.30 4.22
- Mr. Smith plans to deposit $8000 in a savings account at the end o f   each year for 5 years. The bank pays interest at  the rate o f   12% per year, compounded quarterly, on such a plan. Calculate how much money Mr. Smith can expect to withdraw at the end o f   5 years, (a) by the method o f   Example 4.4, (b) by  use of (4.3). Ans. (a) $51 382.40; (b) $51 394.73 4.23
- Suppose that $2000 is invested now, $2500 two years from now, and $1200 four years from now, all at 8% per year, compounded quarterly. What will be the total amount 10 years from now? Ans. $11 057.33 4.24
- A savings bank offers $1000 certificates  o f   deposit.  Each certificate  can be redeemed for  $2000 after 8 4    ears. What is the nominal annual interest rate i f   the interest is compounded monthly? Ans. 8.182% 4.25
- What is the effective annual interest rate for the certificates o f   Problem 4.25? Ans. 8.496% 4.26
- Frank  is  trying  to determine whether or  not  he  can  afford  to  borrow  $10000 for  2 years. The  bank charges 1% per  month  on  the  unpaid  balance.  Frank  wants to  repay  the  loan  in  24  equal  monthly installments, but feels he cannot pay more than $450 per month. Can he afford the loan? Ans. No (he would have to repay $470.70 per month) 4.27
- What will be the monthly payment on a 30-year, $100 000 mortgage  loan, where the interest rate is 12% per year, (a) compounded monthly? (b) compounded daily? Ans. (a) $1028.61; ( b ) $1033.25 4.28
- What is the answer to Problem 4.28 under the approximation lim (AIP, i, n ) = i? Ans. $1000 n-'= 4.29
- Mrs. Jones plans to save $750 a month for the next 10  years, at 10%  per year, compounded monthly. How much money will she have at the end o f   10 years? Ans. $153 633.38 4.30
- What is the present value o f   a series o f   monthly payments o f   $300 each over 12 years, if  the interest rate is 9%  per year, compounded monthly? Ans. $26 361.29 4.31
- How much money must be deposited in  a savings account each month to accumulate $12 000 at the end of   5 years, if  the bank pays interest at  the rate o f   6%  per year, compounded monthly? Ans. $171.99 4.32

- 4.33 Compute the amount of  the monthly deposits Mr. Jones must make for the next 5 years in order for him to accumulate $10 000 at the end o f   5 years, at the nominal rate o f   6%  per year, compounded daily. Ans. $143.28
- 4.34 A series o f   quarterly payments of   $1000 for 25 years is economically equivalent to what present sum, i f the quarterly payments are invested at an  annual rate o f   8%, compounded quarterly? Ans. $43 103.45
- 4.35 Using  a  suitable form  o f (2.9), evaluate A/G for  r = 12%, compounded  monthly,  and n = 5  years. Compare the result to the tabulated value in  Appendix A. Ans. 26.5333 (same in  Appendix A)
- 4.36 An  investment plan  pays  15%  per  year, compounded monthly. How much  would  have to be  invested every year so that $40 000 would be accumulated by  the end o f   10 years? Ans. $1869.13
- 4.37 On the day of  his son's birth, a father decided  to establish a fund for the boy's college education. The father wants the son  to be able to withdraw $4000 from the fund on  his 18th birthday, again on  his 19th birthday, again on  his 20th  birthday, and  again on  his 21st birthday. I f   the fund earns interest at 9%  per year, compounded quarterly, how much should the father deposit at the end o f   each year, up through the 17th year? Compare with the result obtained for annual compounding (Problem 2.25). Ans. $338.41
- 4.38 Solve Problem 4.37 again, assuming now that the money is deposited in  the bank at the beginning, rather than the end, o f   each year. Ans. $309.59
- 4.39 A new machine is expected to cost $6000 and have a life o f   5 years. Maintenance costs will be $1500 the first  year, $1700 the second year, $1900  the third year, $2200  the fourth year, and $2300  the fifth year. How much should be deposited in  a fund that earns 9%  per year, compounded monthly, in order to pay for this machine? Ans. $13 180
- 4.40 Suppose that a person deposits  $2500 in a savings account at the end o f   each year for the next 15 years. I f the bank  pays (a) 8%  per year, (b)  8 : % per year, compounded daily, how  much  money will  the person have by  the end o f   the 15th  year? Ans. (a) $69 609; (b) $72 649
- 4.41 Jones has deposited his life  savings of $70 000 in a retirement income plan with a local bank.  The bank pays (a)  10% per year, (b)  11.25% per year,  compounded quarterly,  on such deposits. What is the maximum fixed amount Jones can withdraw at the end o f   each year and still have the funds last for 15 years? Ans. (a) $9404.33; (b) $10 132.00
- 4.42 Ann White is  planning to take early retirement. She has decided  that she needs $15000 a year for the first 5  years  o f retirement; after  that,  Social  Security  and  other  pension  plans  will  provide  her  with adequate retirement income.  How  much  money  will  she  need  to have in  the bank  at  the start  o f the 5-year period, i f   the bank pays (a)  10% per year, (b) 6.75% per year, compounded monthly? Compare the result in  (a) with Problem 2.31(a). Ans. ( a ) $56 184; (b) $61 565
- 4.43 Mr. Frank is planning for a 25-year retirement period, during which  he wants to withdraw a portion of his savings at the end of  each year. He plans to withdraw $10 000 at the end o f   the first year, and to then increase the amount o f   the withdrawal by  $1000 each year (to offset inflation). How much money should he have in  his savings account at the start o f   his retirement period in order to achieve these goals, if  the bank pays 9% per year, compounded quarterly? Compare with Problem 2.32(a). Ans. $169 740
- 4.44 Repeat Problem 4.43 for an  interest rate o f   8 1 %   per year, compounded quarterly. How significant is the 10 2 / O difference? Ans. $179 267 (the $% difference requires almost $10 000 additional)
- 4.45 The cost  to maintain a new  car  is estimated  to be $75 the first year, and to increase by  $12 each  year thereafter. How much money should be set aside for maintenance, i f   the car is to be kept 6 years and i f the money which is set aside earns interest at the rate o f   5%  per year, compounded monthly? Ans. $522.15

- 4.46 A father wants to set aside money for his 8-year-old son's college  education, by making annual deposits to a  bank  account  in  his  son's  name  that  pays 8%  per  annum,  compounded  quarterly.  What  equal deposits must the father make on the son's 9th through 17th birthdays, in order for the son to be able to withdraw $4000 on each of  his four birthdays from the 18th to the 21st? Ans. $1013.76
- 4.47 A savings account earns interest at the rate of  6% per year, compounded quarterly. How much money must  initially  be  placed  in the  account  to  provide  for  fifteen  end-of-year  withdrawls,  i f the  first withdrawal is $2000 and each subsequent withdrawal increases by  $350? Ans. $36 792
- 4.48 A bank offers its customers a Christmas Club  account in  which they deposit $25 a week for 39 weeks, starting  in  February.  At  the  end  of  the  period  (mid-November),  each  customer  can  withdraw  $1000. What is the nominal annual interest rate, assuming monthly compounding? (Hint: The 39 weeks compose nine interest periods, at the ends  of which the  lumped deposits are $100, $100, $125,. . . . ) Ans. 7.72%
- 4.49 Mr.  Williams  deposits $200  in  the  bank  at  the  end  of  each  quarter.  I f the  bank  pays 6%  per  year, compounded quarterly, how much money will Mr. Williams have accumulated at the end of  12 years? Ans. $13913
- 4.50 Repeat Problem 4.49 for a nominal interest  rate of  6f%  per year, compounded monthly. Ans. $14373
- 4.51 Repeat Problem 4.49 for the case where the money is deposited  at the beginning of  each quarter. Ans. $14 122
- 4.52 An engineering student borrows $4000 to pay tuition for his senior year. Payments are to be made in 36 equal  monthly  installments,  to  begin  the  first  month  after  graduation.  How  much  money  must  the student repay each month, if  he is graduated 9 months after taking out the loan and if the interest rate is 10%  per year, compounded  (a) monthly? (6) quarterly? (c) daily? Ans. (a) $139.08; (b) $139.98; (c) $138.64
- 4.53 A recent engineering graduate intends to purchase a new car. He plans to pay $2000 down and to finance the balance over a Cyear period. The maximum amount that he can repay each month is $200. What is the  most  expensive  car  that  he can  afford,  assuming  an  interest  rate of 1 2 O / 0   per  year,  compounded monthly? Ans. $9595
- 4.54 Suppose that the engineering graduate of  Problem 4.53 can afford to repay $200 a month during the first year, $225 a month during the second year, $250 a month during the third year, and $275 a month during the fourth year. What  is  the most  expensive car  he can afford, assuming he pays $2000 down  and  the interest rate is 12%  per year, compounded  monthly? Ans. $10 878
- 4.55 Repeat  Problem 4.54 for an interest rate of  1@/0 per year, compounded  daily. Ans. $11 094
- 4.56 A  young couple  are saving money  in  order  to make a  down  payment  on  a  house  6  years from  now. Suppose that they save $150 a month during the first year, $165 a month during the second year, and so on, the amount increasing by $15 a month in each successive year. What is the most expensive house that they will be able to purchase at the end of  the 6-year period, i f   they pay 25%  down? Assume that their savings earns 7% per year, compounded  quarterly. Ans. $65 327
- 4.57 An engineer plans to borrow $10 000 to open  his own consulting business. He must repay $215 a month for 5 years. What is the nominal annual interest rate, based on monthly compounding? Ans. 10.51%

## Continuous Compounding

## 5.1 NOMINAL AND EFFECTIVE INTEREST RATES

Continuous  compounding  can  be  thought  of  as  a  limiting  case  of  the  multiple-compounding situation of  Section 4.3.  Holding the nominal annual interest rate fixed at r and letting the number of interest  periods  become  infinite,  while  the  length  of  each  interest  period  becomes  infinitesimally small, we obtain from (4.3)

<!-- formula-not-decoded -->

as the expression for the effective annual interest  rate in continuous compounding.

Example 5.1 A savings bank is selling long-term savings certificates  that  pay  interest  at the rate of  7% per year,  compounded  continuously.  The bank  claims  that  the actual  annual  yield  of  these certificates  is  7.79%. What does this mean?

The  nominal  interest  rate  is  7%. Since  the  interest  is  compounded  continuously,  the effective  annual interest rate is given  by  (5.1)  as

Formula (5.1)  is  very  convenient,  provided  a  calculator  is  available  to carry  out  the exponentiation. Tabulated values of  the effective annual interest  rate may  be used instead; see Appendix B.

## 5.2 DISCRETE PAYMENTS

If  interest  is  compounded  continuously  but  payments  are  made  annually,  we can  still  use  the formulas of  Chapter 2 for the various compound interest factors,  provided  i is given by (5.1).  Thus:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where  n represents  the  number  of years,  as  before.  These  factors  are  denoted [FIP, roh7  n], [PIF, r0/0, n], etc.  (Notice  the use of square brackets rather than  parentheses,  and  reference to the nominal  interest  rate,  to  indicate  continuous  compounding.)  The  continuous  compound  interest factors can  be evaluated directly  from  the above formulas, or they can  be obtained from  the tables presented in Appendix C.

Example 5.2 A savings bank offers long-term savings certificates at 7910 per year, compounded continuously. If  a  10-year  certificate  costs $1000, what  will  be its value at  maturity?  Compare with  the value  that  would  be obtained if  the interest were compounded annually  rather than continuously.

From (5.2), and

<!-- formula-not-decoded -->

This problem can also be solved using Appendix C. Since a table is not available for a nominal interest rate of 7% per year, however, it will be necessary  to interpolate between  the 7%  and 8% values.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The future worth of  the savings certificate can  now be obtained as

<!-- formula-not-decoded -->

If  the interest were compounded annually rather than continuously, the future worth would be

<!-- formula-not-decoded -->

or $56 less than the amount that is obtained with continuous compounding.

Example 5.3 A  savings  account  earns interest  at the  rate of  6%  per year,  compounded continuously.  How much  money  must  initially  be placed  in  the account  to provide for twenty  end-of-year withdrawals,  if  the first withdrawal is $1000 and each subsequent  withdrawal  increases  by  $200?

The solution may be formulated after (2.11):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(these values can  also be obtained from Appendix C); hence,

<!-- formula-not-decoded -->

If  interest  is compounded continuously  but  payments are made  p  times  a  year,  formulas (5.2) through (5.8)  remain valid with r replaced by rlp and with  n  replaced by  np. [These substitutions do not, of  course, alter  the forms of (5.2) and (5.3).]

- Example 5.4 A person borrows  $5000  for  3 years, to  b e   repaid  in 36equal  monthly installments. The  interest rate  is 10%  per year, compounded continuously. How much money must be repaid at the end of  each month?

Calculating [AIP,  10°/0/12,  361 by  (5.6), we have

<!-- formula-not-decoded -->

Example 5.5 A bank offers its customers a Christmas Club account, in which they deposit $12.61 a week for 39 weeks, starting in mid-February. At the end of  39 weeks (mid-November), each customer will have accumulated $500, which  can  be withdrawn  to pay for gifts and other seasonal expenses. What is the nominal interest  rate, assuming continuous compounding?

We know  that FIA = $500/$12.61 = 39.6511.  Let  us attempt  to choose  an  interest  rate  that  will  yield  this value when substituted into (5.4), which in  this case takes the form

<!-- formula-not-decoded -->

with  n = 0.75  year and p = 52 payment  periods per year:

From (5.7) and (5.8),

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The desired  value, FIA = 39.6511, lies  somewhere  between  the 4% and  the 5% values.  Thus,  using  linear interpolation,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.3 CONTINUOUS PAYMENTS

For p payments of A per year and continuous compounding, we have, as in  Example 5.5,

<!-- formula-not-decoded -->

where A =Alp-' is  the  average  rate  of payment  over  a  payment  period.  With  A  held  fixed,  the denominator above approaches r as p + = m; and we obtain for continuous payments at rate A (dollars per unit time)

In  like manner, we find:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The notation [F/&amp; r%, n], etc., is used for these factors.

Example 5.6 At what  rate  must  funds  be continuously added  to a  savings  account  in  order  to accumulate $10 000 in 15 years, if  interest is paid at 5% per year, compounded continuously?

BY (5.10),

<!-- formula-not-decoded -->

that is, $447.63 must flow  uniformly into the account each year.

It  is  interesting  to  compare  this  result t o   a series  of uniform,  end-of-year  payments,  with  interest compounded continuously as above. The amount of  each such payment is given  by (5.5) as

<!-- formula-not-decoded -->

Thus,  an  additional $11.37 would  be  required  each  year  if the  payments  were  made  annually  rather  than continuously.

It  is  convenient  to determine the end-of-year  payment A equivalent  to continuous  payments at rate A, under continuous compounding. If  (5.4) and (5.9) are to give the same value of F, and so

<!-- formula-not-decoded -->

This factor, written symbolically  as [A/A,  r0/0], is tabulated in Appendix D.

- Example 5.7 Rework Example 5.6, using the concept of  the equivalent yearly payment. The solution can be formulated as

<!-- formula-not-decoded -->

From Appendixes C and D, [AIF,  so%,  151 = 0.0459 and [AIA, 5%] = 1.0254. Thus,

<!-- formula-not-decoded -->

## Solved Problems

- 5 . 1 What effective annual interest  rate corresponds  to a  nominal  interest  rate of  10%  per year, compounded continuously?

<!-- formula-not-decoded -->

(This  result could also have been obtained from Appendix B.)

- 5.2 Determine  the  nominal  interest  rate corresponding  to an  effective interest  rate of  10%  per year, compounded continuously.

Solving (5.1)  by natural logarithms, or 9.53%

- 5 . 3 How much money must be deposited in a savings account so that $5500 can be withdrawn 12 years  hence,  if the  interest  rate  is  9%  per  year,  compounded  continuously,  and  if all  the interest  is  allowed  to accumulate?  Compare  the  answer with  the result  obtained for  annual compounding, in Problem 2.2.

<!-- formula-not-decoded -->

Comparing with Problem 2.2, we see that a savings of $87.66 is realized by continuous compounding.

- 5.4 How much money must be deposited  at the end of  each year in  a savings account that pays 9%  per  year,  compounded continuously, to have  a  total of  $10 000 at  the end of  14 years? Compare the answer with the result obtained for annual compounding, in  Problem 2.6.

<!-- formula-not-decoded -->

If the interest  were compounded annually rather than continuously, the yearly deposit would have t o  be $11.43 greater.

- 5.5 Mr. Smith is planning his retirement. He has decided that he will need $12 000 per year to live on, in addition to his other retirement income from Social Security and a private pension plan. How much money should  he plan  to have in  the bank  at  the start  of  his retirement, if  the bank  pays  10%  per  year,  compounded  continuously,  and  if  Mr.  Smith  wants  to  make  12 annual withdrawals of  $12 000 each?

<!-- formula-not-decoded -->

In  Problem 2.9 we saw  that  the required  amount of  money  would  be $81  766.15 if  the interest  were compounded annually rather than continuously. Hence, the  continuous  compounding results in a savings of over $2000.

- 5 . 6 Ms.  Brown  deposits $1000  in  the bank  at  the end of  the first  year,  $1200 at the end of  the second year, etc., continuing to increase the amount by $200 a year, for 20 years. If the bank pays 7%  per year, compounded continuously,  how much money will have accumulated at the end of  20 years?

Writing A' = $1000 + A, we have, from Section 2.7,

Substituting  G = $200 and using Appendix C,

- 5 . 7 Calculate the factors [FIA, 7%, 201 and [AIG, 7%, 201 used in  Problem 5.6.

By (5.4), and, by (5.8),

<!-- formula-not-decoded -->

- 5.8 Mrs. Carter deposits $100 in the bank at the end of  each month. If  the bank  pays ( a ) 6%  per year, (b) 7% per year, compounded continuously, how much money will she have accumulated at the end of  5 years? (Compare Problem 4.11.)
- ( a ) The nominal  monthly  interest  rate is 6%/12 = 0.5%. There will  be a  total  of 5 X 12 = 60 monthly payments. Hence,

<!-- formula-not-decoded -->

From Appendix C, [FIA,  0.S0/0,  601 = 69.7970; therefore,

- (b) The nominal monthly interest rate is 7%/12=0.583333%. As a tabulated value of [ F/A,  0.583333%, 601 is not available, we interpolate linearly between [FIA,  O.SOh, 601 and [FIA,  0.7S0/o,  601:

<!-- formula-not-decoded -->

The desired solution  is then F = $100(71.6951) = $7169.51.

A more accurate procedure would be to use (5.4), with r replaced  by rl12:

<!-- formula-not-decoded -->

- 5.9 In Problem 5.8, suppose Mrs. Carter deposits $100 a month during the first year, $110 a month during  the  second  year,  $120  a  month  during  the  third  year,  etc.  How  much  will  have accumulated  at  the  end  of 5 years  if the  interest rate  is  6%  per  year,  compounded continuously? (Compare Problem 4.12.)

Proceeding as in  Problem 4.12, we have:

<!-- formula-not-decoded -->

The required numerical  values can  be obtained  from  Appendix C. Thus,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

A  neater solution procedure (which  might also have been applied  in  Problem 4.12) is to consider the deposits as constituting a five-year gradient series, with

<!-- formula-not-decoded -->

Thus, as in  Problem 5.6,

<!-- formula-not-decoded -->

- 5.10 Suppose that $2000 is deposited each year, o n  a continuous basis, into a savings account that pays 6% per year, compounded continuously.  H o w  much money will  have accumulated after 12 years?

With A = $2000 per year, (5.9) gives

<!-- formula-not-decoded -->

Alternatively, using the tabular values in  Appendixes C  and D,

<!-- formula-not-decoded -->

## Supplementary Problems

- 5.11 What effective annual interest rate corresponds to a  nominal interest rate of 15% per year, compounded continuously? Ans. 16.18%
- 5.12 What  nominal  interest  rate  corresponds  to an  effective  interest  rate  of 12% per  year,  compounded continuously? Ans. 11.33%
- 5.13 Determine the effective annual interest rate corresponding to a nominal interest rate of 8?% per year, if the interest is compounded ( a ) quarterly, ( b ) monthly, ( c ) daily, ( d ) continuously. Ans. ( a )   8.77%; (b)  8.84%; (c)  8.871%; ( d )   8.872%
- 5.14 An  investment  plan  pays 15% per  year,  compounded  continuously.  How  much  would  have  to  be invested  at the end of  each year so that $40 000 will  be accumulated  by  the end of 10 years? Compare with the result obtained for annual compounding (Problem 2.20). Ans. $1859.26
- 5.15 Suppose that $2000 is invested  now, $2500 is invested two years from now, and $1200 is invested four years from now, all at 8% per year, compounded continuously. What will be the total amount 10 years from now? Ans. $11 131.57

- 5.16 Repeat Problem 2.25 for continuous compounding. Ans. $334.23

- 5.17 Repeat Problem 2.27(a) for continuous compounding. Ans. $13 173.00

- 5.18 Repeat Problem 2.29(a) for continuous compounding. Ans. $69 642.25

- 5.19 Repeat Problem 2.30 for continuous compounding. Ans. ( a )   $9476.60; (b)  $10 226.83

- Repeat Problem 2.31(a) for continuous compounding. Ans. $56 118.82 5.20
- Repeat Problem 2.32(a) for continuous compounding. Ans. $167 884.49 5.21
- Repeat Problem 2.32 for continuous compounding at 89/0. How significant is the &amp; difference vis-a-vis Problem 5.21? Ans. $177 478.94 5.22
- The cost of  maintaining a  new car is estimated  to be $75 the first  year and to increase by $12 each year thereafter. How much money should be set aside for maintenance, if  the car is to be kept 6 years and if the money  which  is  set  aside  earns  interest  at  the  rate  of 5% per  year,  compounded  continuously? (Compare Problem 4.45.) Ans. $521.95 5.23
- Rework Problem 4.46 for continuous compounding. Ans. $1001.16 5.24
- Find the monthly payment on a 30-year, $100 000 mortgage loan, where the interest rate is 12% per year, compounded continuously. Ans. $1033.25 [cf.  Problem 4.28(b)] 5.25
- Repeat Problem 4.30 for continuous compounding. Ans. $154 001.91 5.26
- Repeat Problem 4.31 for continuous compounding. Ans. $26 317.24 5.27
- 5.28
- Repeat Problem 4.32 for continuous compounding. Ans. $171.93
- Mr. Smith plans to purchase a  new $10 000 automobile.  H e  wants to borrow all the money for the car, and repay it in  equal monthly  installments over a  4-year  period. The nominal interest  rate is 11% per year, compounded continuously.  What will be Mr. Smith's monthly payment? Ans. $258.70 5.29
- Repeat Problem 4.33 for continuous compounding. Ans. $143.27 5.30
- A savings bank offers $1000 certificates of  deposit.  Each certificate can  b e  redeemed for $2000 after 8: years.  What  are ( a ) the nominal, ( b ) the effective, annual  interest  rate, if  the interest  is  compounded continuously? Ans. ( a )   8.155%;  (b)  8.496% 5.31
- A  savings  account  earns interest  at  the  rate of 6?/0 per  year,  compounded  continuously.  How  much money  must  initially  be  placed  in  the  account  to  provide  for 15 end-of-year  withdrawals  if the  first withdrawal  is $2000 and each subsequent  withdrawal  increases  by $350? Ans. $36 620.17 5.32
- Repeat Problem 4.48 for continuous compounding. Ans. 6.90% 5.33
- Repeat Problem 4.49 for continuous compounding. Ans. $13 953.93 5.34
- Repeat Problem 4.50 for continuous compounding. Ans. $14 423.37 5.35
- Repeat Problem 4.51 for continuous compounding. Ans. $14 163.24 5.36
- A savings account pays 5 % per year, compounded continuously.  How much  money must be deposited at the end of  each month in order to accumulate $10 000 at the end of 7 years? Ans. $97.82 5.37
- Repeat Problem 4.52 for continuous compounding. Ans. $139.21 5.38
- Repeat Problem 4.53 for continuous compounding. Ans. $9586.27 5.39
- Repeat Problem 4.54 for continuous compounding. Ans. $10 867.03 5.40
- Repeat Problem 4.54 for continuous compounding at 1&amp;/0 per annum. Ans. $11 094.03 5.41
- Repeat Problem 4.57 for continuous compounding. Ans. $65 824.16 5.42

- 5.43 Repeat Problem 4.57 for continuous compounding at 6$% per year. Ans. $64 878.08
- 5.44 An engineer borrows $10 000 to buy a personal computer. He must repay $218.94 a month for 5 years. What is the nominal annual interest rate, based  upon continuous compounding? Ans. 11%
- 5.45 A consulting firm has a continuous cash inflow of  $5 million  a year. If  this money is accumulated  in  an account that earns (a) 15% per year, (b) 13.S0/~  per year, compounded continuously,  how  much  money will have accumulated  after 7 years? Ans. (a) $61 921 704; (b) $58 252 347
- 5.46 A company has set aside $10  million to promote a new product. The money is to be spent continuously over a 3-year period (during which it is assumed that the sales of  the product will offset expenses). If  the $10  million  is  placed  in  an  account  that  earns  (a) 12%  per  year,  (b)  10.75%  per  year,  compounded continuously,  what  is the maximum rate at which money can be withdrawn during the 3-year period? Ans. (a) $3 969 256 per year; (b) $3  899 674 per year
- 5.47 In  Problem  5.46,  how  much  money  must  be placed  in  the account  if $4  million  is  to be spent  on  a continuous basis each year, and the interest rate is  10% per year, compounded continuously? Ans. $10 367 271

## 6.1 ECONOMIC EQUIVALENCE

In economic analysis, "equivalence" means "the state o f being equal in  value." The concept is primarily applied in the comparison o f   different cash flows. As we know from earlier chapters, money changes  value  with  time;  therefore,  one o f t h e   main  factors  when  considering  equivalence  is  to determine  at  which  point(s)  in  time  the money  transactions occur.  A  second  factor  is  the specific amounts of  money involved in the transactions. Finally, the interest  rate at which  the equivalence is evaluated must also be considered.

Example 6.1 Bob, an  engineering student, has just received his salary for a summer  job. After living expenses and entertainment, he has left $1000, which he plans to save for a down payment on a new car. His father wants to borrow Bob's $1000, and promises to return $1060 one year from  now. According to his father, that is what Bob would receive if  he put the money in  his bank savings account, which  pays an effective annual interest rate of 6%. What should  Bob do?

I f   Bob's only alternatives are lending the money or depositing it in  his current savings account, both courses of  action  are indeed equivalent. That is, either would provide  Bob, one year from now, with $1060 in  return for his decision  to forego using his $1000 today.  Given  this equivalence,  Bob's  decision  would be based  on  factors external  to engineering  economics  (e.g., the degree  to which he trusts his father).

However,  i f Bob  had  a  different  savings option-say,  a  savings certificate  with  a  guaranteed 9% annual yield-the equivalent value of  his assets one year from now would be $1090. In this case, the lending and savings alternatives are no longer equivalent, and Bob has the problem of  explaining this to his father.

In Example 6.1, (FIP, 6%, 1) served as the equivalencing  factor. In  general,  all  t h e  compounding and discounting factors presented in  earlier chapters are equivalencing factors.

Equivalence is not always directly apparent. Cash flows that have very different structures (i.e., different amounts being transacted at different points in  time) may be equivalent at a certain interest rate.

Example 6.2 A company which produces and markets microcomputers has just introduced a new line which is expected  to  sell  for $10000 per  system.  Owing  to  market  conditions,  the  company  is  being  forced  to offer financial  incentives  to  potential  customers.  The  company  has  decided  to  charge  an  interest  rate  of l o % , compounded yearly, and to give customers three options.

Option 1: Pay in four equal yearly installments of

<!-- formula-not-decoded -->

Option 2: Pay  the interest  each  year, and  the principal  (and  interest) at the end of  the fourth  year.  This means paying $1000 ($10 000 x 0.10) at  the end of  years 1, 2, and 3, and $11 000 at the end of  year 4.

Option 3: Make a single payment of

<!-- formula-not-decoded -->

at the end of  year 4.

Which option is best for a customer? for the company?

As summarized  in Table 6-1, the three  payment  plans offered  a customer  are quite different  in  structure. However, if 10% is the "appropriate"  interest  rate for his economic evaluations, all  three plans are equivalent: each  provides  him with  a microcomputer worth $10 000 and gives him 4 years  to repay at a 10% interest  rate, compounded yearly. From the company's  point of  view, similar reasoning applies: at looh interest, all  plans are equivalent because all  result  in  the sale of  a $10 000 item, and the money is recovered over a Cyear period.

## Equivalence

## Chapter 6

Table 6-1

| End of   | Payment   | Payment   | Payment   |
|----------|-----------|-----------|-----------|
| Year     | Option 1  | Option 2  | Option 3  |
| 1        | $3155     | $1000     | $ 0       |
| 2        | 3155      | 1000      | 0         |
| 3        | 3155      | 1000      | 0         |
| 4        | 3155      | 11000     | 14641     |

Notice that different cash flows are equivalent if  they have the same value at some point in time.

Example 6.3 Are the financing plans of Example 6.2  still equivalent i f   the evaluation is made at the end of year 4?

Yes; at the end o f year 4,  all  plans have an  equivalent value o f   $14641 (up to roundoff  errors) when  the same interest rate (10%) is used to make the evaluations.

Option 1 (equal payments):

<!-- formula-not-decoded -->

Option 2 (amortization  of  interest):

<!-- formula-not-decoded -->

More generally, we  can  say  that options 1 and 3 must  be equivalent at  the end o f   year 4,  since  they  are obviously equivalent at the end of year 0; and  that options 2 and 3 are equivalent, on the basis o f   the relation

<!-- formula-not-decoded -->

derived in  Problem 3.3(a). Thus, all  three options are equivalent, to the customer and to the company, provided the two parties use the same interest rate.

Example 6.4 The company in  Example 6.2  still uses interest  rate i = lo%, and therefore still offers the same three payment plans. The customer, however, calculates interest at rate it, so that the values (costs) to him o f   the three options at the end o f   year 0 are as given in  Table 6-2; for instance, for i' = 12%, the value of  option 2 is

<!-- formula-not-decoded -->

Table 6-2

| Customer's Rate'   | Present Value   | Present Value   | Present Value   |
|--------------------|-----------------|-----------------|-----------------|
| Customer's Rate'   | Option 1        | Option 2        | Option 3        |
| 8%                 | $10450          | $10662          | $10760          |
| 10%                | 10000           | 10000           | 10000           |
| 12%                | 9583            | 9392            | 9304            |

Note  that  when i t # lo%, the  options are  no  longer  equivalent  to  the  customer,  and,  more  important, different interest rates may  lead  to different decisions. Consider, for example, a customer who has the money ($10000) on  hand, but who knows that he can  put  that money  in  a savings account which  pays 12%  effective interest, compounded yearly. The best strategy for this customer would be to take option 3 and pay $14 641 four years from now. Since this amount is equivalent to only $9304 at the rate he has saved his money, he would end up with a net saving of  $10 000 -$9304 = $696 (year 0 money). On the other hand, i f   a customer is used to paying only 8% for loans, his best alternative (assuming he cannot pay cash or borrow at that rate to buy the computer) is option 1, the least costly at the interest  rate he normally uses to make his economic evaluations.

## 6.2 THE  COST OF CAPITAL

From Example 6.4 it  is seen  that the relative evaluation  o f cash  flows depends critically on  the "appropriate" or "pertinent" interest  rate used in  the calculations.  Unfortunately, the interest rate that determines the time value of  money is not usually known, nor is it easy to determine. It stands to reason, though,  that i f   money is to be invested in  a  project, the project's cash flow equivalent  value should be calculated at an interest rate that exceeds the rate incurred in raising the initial capital. The extra  percentage  points are  justified  in  terms of  risks  associated  with  the specific  project  and  with long-term  commitment  of  funds,  and  in  terms  of  a  profit  margin  required  to get  involved  in  the economic  activity.  Thus,  a  mining  company  considering  diversification  into  plastics  would  use  a higher interest rate to evaluate such a project than it would use for a new mining project, because of the  risk  of  entering  a  new  venture  with  unknown  market  factors  and  for  which  no experience  is available.

There are several means for a company to raise money for a project. It may borrow from a bank at a specified interest  rate; it may reinvest profits from other projects instead of  distributing them to the  owners  or  shareholders;  it  may  sell  stock,  thereby  increasing  the  number  of owners  (and decreasing  the equity of  each stockholder); and it  may borrow from the public  through the issue of bonds.  Almost  always, a combination  of  methods is employed, and one way  to measure the cost  of capital is to calculate a weighted average of  the costs of  funds acquired from all sources.

## 6.3 STOCK  VALUATION

Stock  represents  a  share  of  ownership in  a  company.  Its equivalent-value  calculation  presents practical  difficulties  of  estimating  future dividends  and selling  price, which  are affected  not only  by the company's performance but also by the overall situation of  the economy and of  the stock market.

Example 6.5 ABC Corporation's  stock, which currently sells for $50 per share, has been  paying a $3 annual dividend per share and increasing in value at an average rate o f 5% per year, over the last 5 years. It is expected that the company's stock will maintain this performance over the next 5 years. (a) What is the company's cost o f the capital raised through the selling o f   this stock? (b) Is this stock a good buy for an investor who expects a 9% return on  his investments?

- (a) From the company's point of  view, it will receive $50 per share today and would have to pay

<!-- formula-not-decoded -->

to buy it back 5 years from now. In addition, it must pay a yearly dividend o f $3 per share. The equation o f value at time 0 for this cash flow is therefore

<!-- formula-not-decoded -->

where i % is  the  cost  o f capital  for  money  raised  through  the  sale  o f this stock, assuming the forecast dividends and selling price are accurate. The solution for i  must  be found by  a trial-and-error approach:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Thus, by  linear interpolation,

<!-- formula-not-decoded -->

- (b) For a customer who wants to make 9% on  his investments, the value o f   his expected  receipts from  this share is given by

<!-- formula-not-decoded -->

Since the expected value of  the share exceeds the asked price, it  is expedient for him to buy it; i f   he does so, he should not only recover his $50 investment and the 9% he expects yearly, but he should gain an extra $3.14 (year 0 money) in the transaction.

Alternatively,  since  we  infer  from ( a ) that  the  company  expects  the  stock  to  yield 10.49% to  an investor, the investor ought  to buy  it, i f   he  requires only 9% and if  he agrees with  the company as to the stock's future performance.

## 6.4 BOND VALUATION

A  bond is  an  economic  instrument  which  has  a face  value guaranteed  to  be  paid  to  the bondholder by  the issuing  company  when  the instrument  reaches  maturity.  In  addition,  the bondholder usually  receives  periodic dividends at a  specified interest  rate.  Bonds are transacted  on the market,  and  their  value  depends  on  the  size  and  timing  of the  dividends,  the  duration  before maturity,  and  the rate of  return  desired  by  the bond  purchaser. The company's cost  of  the capital raised through  bonds will depend on their acceptability  to the public.

Example 6.6 ABC Corporation has decided to sell $1000 bonds which will  pay semiannual dividends of $20 (2% per  period)  and  will  mature in 5 years. The  bonds are sold  at $830, but  after  brokers' fees  and  other expenses the company ends up receiving $760. (a) What is the company's cost of  the capital raised  through the sale o f   these bonds? (b) Is the bond a good  buy for an  investor who expects a 9% return  on  his investments?

- ( a ) From the company's point of  view, it will receive $760 per bond today and will have to pay $1000 (the face value) 5 years hence, plus a $20 semiannual dividend. The equation of   value at time 0 for this cash flow is

<!-- formula-not-decoded -->

where 10 periods are  used because dividends are paid  twice a year and the bond  matures in 5 years, and where i % is the cost o f   capital, effective per 6-month period. Solving by  trial and error:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and linear interpolation gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The company's cost of  capital for money raised through the sale o f   these bonds is, on  a yearly basis, given by  (4.3) as

<!-- formula-not-decoded -->

- (6) From the investor's point o f view, he will  pay $830 today to receive $20 every 6 months and $1000 i n   5 years. He expects an  effective rate o f 9% a year on  his investments, or

<!-- formula-not-decoded -->

per 6-month period. Hence the equivalent value at time 0 of   his expected receipts is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This value represents the maximum amount the investor can  bid for this bond, i f   he requires an  effective annual yield o f 9% on his investments. Since the market value today ($830) exceeds this maximum amount, he should look for another business opportunity which could give him  his required 9% return.

Notice  that  we  could not conclude from ( a ) that  the  investor could  realize 10.62%  (&gt;9%); for,  in effect,  part o f   that 10.62% goes to the brokers.

## 6.5 MINIMUM ATTRACTIVE RATE OF RETURN

If,  as is often  the case,  the interest  rate at which  a  project  should  be evaluated  is  not  known, a target rate, cut-off  rate, or valuation rate will  be used. This rate is also called the minimum attractive rate  of  return (abbreviated  MARR). While dependent  on general company  policy, the MARR may

also be project specific, and will normally increase with the risk attending the project. It will certainly be higher than  the cost o f   raising capital for the project, estimated as described in Section 6.2.

Example 6.7 In  order  to finance a $100 000  project, ABC Corporation has decided  to raise $20 000 through the sale  o f stock,  as  described  in  Example 6.5,  and  $30 000  through  the  issuance  o f bonds,  as  described  in Example 6.6. For the  balance, $10000 will  be  borrowed from a  bank  at  an  annual  interest  rate o f   12%  and $40 000 will  be  reinvested from  last  year's profits. (a) What  is the  project's cost  o f   capital?  (b)  What MARR should be used to evaluate this project?

- (a) For the four sources o f   capital, we have:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Note that the cost of  capital for reinvested profits  was assumed to be equal to the cost o f   common stock: this is a minimal value, based on the consideration that stockholders are being denied dividends from the retained earnings.

- (b) The MARR for this project must exceed 10.68%.

The MARR will be treated in further detail in Chapter 9.

## 6.6 FAIR MARKET VALUE

The concept o f   equivalence, as applied in the foregoing examples, may be used to determine the actual cost o f   a  loan,  the maximum amount a person or company can bid on a desired property or equipment, and, in general, in the determination o f   the "fair market value"  o f   an asset.

Example  6.8 An  engineering  firm  has  turned  to  Friendly  Shark,  Inc.,  to  borrow  $30000  needed  for  a short-term (2-year) project, attracted by an advertisement announcing an interest rate o f   12% per year. Friendly Shark's loan statement indicates the following:

$$Interest: ($30 000) (1%  per month)  (24 months) = $ 7 200 Loan 30 000 Total $37 200 Monthly installment = $37 200124 = $1550$$

What is the actual cost o f   borrowing money from Friendly Shark, Inc.?

The engineering firm  receives $30 000 immediately and must  pay  back $1550 per  month  over a 24-month period. The monthly interest rate i which makes these flows equivalent satisfies

<!-- formula-not-decoded -->

Now, (PIA, 1.5%,  24) = 20.030 and  (PIA, 2.0%, 24) = 18.914. Hence, by  interpolation,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

which is rather different from the advertised rate.

and so or, on an annual basis,

Example 6.9 A house is being advertised for sale by the owner. An investor estimates that the property could be rented out for $600 per month. Taxes and minor maintenance expenses are estimated at $1200 per year. The house has been  recently remodeled and the tenant should have to pay all utilities. The investor thinks he could sell the house for $85 000 after 5 years. What is the largest amount that the investor can offer for the property i f   his MARR is 12%, compounded monthly?

The equivalent value at year 0 of  the expected receipts and disbursements is given by

<!-- formula-not-decoded -->

where , i = 1% = effective monthly MARR

<!-- formula-not-decoded -->

Now, (PIA,  1%,  60) = 44.955 (from Appendix A), and

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The investor must buy the house for $69 511.62 (or less) to get an effective rate of 1% per month (or more) on his investment.

## Solved Problems

- 6.1 Is the receipt of  $4000 annually for 10 years equivalent  to the receipt of  $5000 annually for 8 years, i f   the interest  rate is 8%  per year, compounded  annually?

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The flows are not equivalent; the receipt'of $5000 for 8 years gives the larger  present value.

- 6 . 2 If the interest  rate is 8%  per year, compounded annually, what is the equivalent present value of  $10 000 (a) 1 year from today? (b) 5 years from  today?

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 6.3 What is the equivalent future value of  $1000 annually for the next 9 years, if  the interest rate is 8%  per year, compounded annually?

<!-- formula-not-decoded -->

- 6.4 A man can invest $150 000 for 12 years in  a business venture and expect to receive $6000 per year in  return. If his MARR is 7% per year, compounded annually, would this investment be satisfactory?

The yearly return A necessary to achieve this MARR is given by

<!-- formula-not-decoded -->

The investment would not be satisfactory.

Therefore,

- 6.5 What amount of  money is equivalent to receiving $8000 three years from today, if  the interest rate is 8% per year, compounded semiannually?

<!-- formula-not-decoded -->

- 6.6 A bank  pays 6% interest  per year, compounded ( a ) quarterly, ( b ) annually.  A $5000 deposit will grow to what amount if  left in  that bank for 2 years?
- (a) F = 85632.46
- (b)
- 6.7 What is the equivalent present value of  the following series of  payments:  $5000 the first year, $5500  the  second  year,  and  $6000  the  third  year?  The  interest  rate  is  8%,  compounded annually.

<!-- formula-not-decoded -->

- 6.8 What single  amount at the end of  the fourth  year is equivalent  to a  uniform  annual series of $3000 per year for 10 years, if  the interest  rate is  10% per year, compounded annually?

Find  the present value of  the series and then move it ahead 4 years:

<!-- formula-not-decoded -->

- 6.9 A series of  10 annual payments of $2000 is equivalent to two equal payments, one at the end of 15  years  and  the  other  at  the  end  of 20  years.  The  interest  rate  is 8%, compounded annually.  What is the amount of  the two equal payments?

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 6.10 A new corporate bond is being offered  in  the market for $930. The bond has a face value of $1000 and matures in 10 years. The issuing corporation  promises to pay $70 in  interest every year. (a) Should an investor requiring an 8% return on investment buy this bond? ( b ) What is the company's cost of  the capital raised  through this bond issue if  the stockbroker's fee is $15 per bond sold?
- ( a ) At the investor's rate, the present value of  the bond is

<!-- formula-not-decoded -->

The investor should buy the bond.

(b)

Interpolating,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The company's  cost of  capital from this bond issue is about 8.29%, compounded yearly.

- 6.11 Is it expedient for Thomas, who requires an 8% return on his investments, to buy an artificial Christmas tree? The tree costs $45 and is expected to  last eight years. The alternative is to keep purchasing natural trees, which now cost $8 (Christmas  of year 0) and are expected to  increase $1 in  price each coming year.

The present value at 8% of a stream o f   payments of  $9 one year from now, $10 in  two years, etc., up to $16 in  eight years, is:

<!-- formula-not-decoded -->

This amount, plus this  year's  natural tree cost  ($8), greatly exceeds the artificial  tree's price; Thomas should buy the artificial tree.

- 6.12 A  mine is for sale.  A  mining 'engineer estimates that, at current  production  levels,  the mine will  yield  an  annual  net  income  of $80000  for  15  years,  after  which  the  mineral  will  be exhausted.  If  an  investor's MARR is  15%, what  is the maximum  amount he can  bid  on  this property ?

<!-- formula-not-decoded -->

- 6.13 How long must a temporary warehouse last to be a desirable investment if  it costs $16 000 to build, has annual  maintenance  and operating costs of  $360, provides storage space valued  at $3600 per year, and if  the company MARR is 1O0/0?

The yearly  net  income  is  $3600-  $360 = $3240, and so  the warehouse must  last  at  least n years, where

<!-- formula-not-decoded -->

Solving by  Table 3-1, or by  scanning the table of  AIP in  Appendix A, we find that n = 8 years.

- 6.14 For what value of X are the following two cash flows equivalent at a 10%  interest  rate?

| End of Year   |
|---------------|
| Flow B, $     |

<!-- formula-not-decoded -->

Equating and

we obtain

## Supplementary Problems

- What series of  equal annual payments is economically equivalent to the investment o f   a present amount of   $5000 for 5 years at  12%, compounded annually? Ans. $1387.03 6.15 6.15
- What single amount at the end o f   the fifth year is equivalent to a uniform annual series of $2000 per year for 10 years, if  the interest rate is  10°h,  compounded annually? Ans. $19'791.09 6.16 6.16
- A series o f   12 annual payments of $2000 is equivalent to three equal payments, one each at the end o f   12 years, 15 years, and 20  years. The interest rate is  lo%, compound annually. What is the amount o f   the three equal payments? Ans. $19 284.55 6.17 6.17
- What is the equivalent present value o f   the following series o f   payments: $7000 the first year, $6500 the second year, $6000  the third year, $5500  the fourth  year, and $5000  the fifth  year? The interest rate is lo%, compounded annually. Ans. $23  104.44 6.18 6.18
- Is  a series o f   100  equal  quarterly payments of $800  equivalent  to  a  present  amount  o f $35000 if  the interest rate is 8%  per year, compounded quarterly? Ans. No; it is equivalent to exactly $34 482.76. 6.19 6.19
- Machine  X will  produce cost  savings of $5000  per  year  for  four  years;  machine  Y will  produce  cost savings of  $4000  per  year for five years. If the interest rate is  1O0h,  compound annually, are these two machines economically equivalent in  terms of the present value o f   their cost savings? Ans. No: PX = $15 849.37 and Pv = $15 163.00. 6.20 6.20
- Find  the  uniform  annual series of seven  payments that  would  be equivalent  to the following gradient series: $500 initially, with  a $50 increment per year, for a total o f   seven years. The interest rate is  12%, compound annually. Ans. $627.58 6.21 6.21
- A woman can invest $100 000 for 15 years in a bank and expect to receive a yearly return of  $10 000. The woman's objective is to earn 12%  per year, compounded annually, on her investments. Is this objective met by  the bank  plan? Ans. No; the woman  requires a return o f   $14 682 per year. 6.22 6.22
- Machine A will save $5000  per year for 6 years; machine B will save $6000  per year for 5 years. I f   the interest rate is  1 O 0 / 0 ,   compounded annually, do these two machines have equal future values at the end o f the sixth year? Ans. No: FA = $38 578 and FB = $36 630.60 x 1.10 = $40 293.66. 6.23 6.23
- The XYZ Bank advertises it  will  pay $3869.70 in  cash  at  the end o f   20  years to anyone who deposits $1000; the ABC Bank states that it pays  10% per year, compounded annually,  on all deposits  left one year  or more. Which bank is paying the higher interest rate, and by  how much? Ans. ABC; XYZ is paying only 7%  per year, compounded annually. 6.24 6.24
- A series o f   quarterly  payments o f   $1000 for 25 years is economically equivalent to what present sum, i f the quarterly payments are invested at an annual rate o f   8%, compounded quarterly? Ans. $43 103.45 6.25 6.25
- What series of  equal annual payments is economically equivalent to the investment o f   a present amount of   $5000 for 5 years at  12%, compounded annually? Ans. $1387.03 6.26 6.26
- A promissory note has outstanding  payments of $650  at  the end o f   each  o f the  next five  years.  What market  price would  be paid  for this note by  an  investor who requires a  12% yield  on  his investments, compounded quarterly? Ans. $2311.47 6.27 6.27
- A loan of   $750 is to be repaid in 18 equal monthly installments, computed as follows: 6.28 6.28

| Loan                                     | $750   |
|------------------------------------------|--------|
| Interest at l0/0 per month for 18 months | 144    |
| Credit check and processing fee          | - 60   |
|                                          | $954   |

Monthly payment: $954118 = $53

What (a) nominal and (b)  effective annual interest  rates are being charged? Ans. ( a ) 32.15% ; (b) 37.34%

-60 $954

## PW,  FW,  EUASIEUAC

This  chapter  treats  several  valuation  methods  which  are  useful  in  deciding  among  economic alternatives.  Its sequel, Chapter 8,  is  devoted  to techniques  that  are  primarily  used  for  analyzing proposed capital investments.

## 7.1 PRESENT WORTH

The present  worth  (PW)  or present value  (PV)  of  a  given  series of  cash  flows is  the equivalent value of the cash  flows at the end of  year 0 (i.e.,  at  the beginning of  year 1).  For the case of  annual compounding,

<!-- formula-not-decoded -->

Here, CFj is the (positive or negative) cash flow for the jth year, (PIF, i0/0, j) = (1 + i)-i, and n is the total  number of  years.

Example 7.1 Determine the present worth o f   the following series o f   cash flows, based  on  an  interest rate o f 12% per  year, compounded annually: $0 (end o f   year O), $1000  (I),  $2000  (2),  $3000  (3),  $4000  (4), $4000 (5), $4000 (6).

BY (7.11,

<!-- formula-not-decoded -->

Alternatively, since the cash flows compose a gradient series followed  by  a uniform series,

P W

=

- = [$lo00 + $1000(1.3589)](3.0374) + $4000(1.6901)(0.6355)

[$I000

+

$1000(A/G,  12%,  4 1 1  (PIA,  12%,  4)

- = $7164.92+ $4296.23 = $11 461.15

Figure 7-1 diagrams this latter solution (which agrees with  the former up to roundoff  errors).

<!-- image -->

Fig. 7-1

$4000(P/A,  12%,  2)  (PIF,  12%,  4)

+

Equation (7.1)  is often applied to problems involving  an initial cash outflow followed by a series of  cash  inflows;  i.e.,  CFo&lt;  0 and  CFj &gt;  0 ( j &gt; 0).  In  such cases, the PW is renamed the net present worth  (NPW) or the net present value (NPV). Clearly the NPW is a monotonically decreasing function of  the interest  rate i  (because,  as  i  increases,  the  positive  flows- and  only  these-are  increasingly discounted).  Applications of  the NPW will  be given in  Chapter 8.

## 7.2 FUTURE WORTH

Given a series of  cash flows as in Section 7.1, the future worth (FW) of  the series is its equivalent value at the end of  year n. Assuming annual compounding,

<!-- formula-not-decoded -->

From the theory of Chapter 2, the future worth is related  to the present worth via

<!-- formula-not-decoded -->

Example 7.2 Determine the future worth of  the cash flows given in  Example 7.1, based on an interest  rate of 12% per year, compounded annually,  using ( a )   (7.2), ( b ) (7.3).

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The variation  of FW with  i,  in  the  special  case  CFo  &lt; O   and  CFj &gt; 0 ( j &gt;O),  is  a  little  more complicated  than  the analogous variation  of  PW. If  (CFol  is very small in  comparison to the positive flows,  then  the  future value  of  the  positive  flows-and  along  with  it  the  FW- will increase  as i increases.  However, if  lCFol is sufficiently large (as it  will  be, in  practical applications),  FW will  be a monotonically decreasing function  of  i,  like PW.

Fig. 7-2

<!-- image -->

## Example 7.3 Given the series

| End of Year   |
|---------------|

y 1

determine the future worth o f   the series at annual interest rates 0%,  5%, lo%,  20%, 30%, and 50%. Graph your results.

Using the equation or, substituting (7.1),

<!-- formula-not-decoded -->

instead  of (7.2), we  calculate  the  following  points (I,  FW):  (O0/0,  $25 O O O ) ,   (5%,  $19 070),  (lo%,  $11 051), (20°/o,  -$12792),  (3O0/o,  -$49  998), (SO%, -$I81  870). These points are plotted to give the curve o f   Fig. 7-2. It is seen  that FW rapidly  decreases with i, becoming zero at  i = 15% (more precisely, at i = 15.26%). In  view  o f (7.3, PW must vanish at this same interest rate.

## 7.3 EQUIVALENT UNIFORM ANNUAL SERIES

The equivalent uniform annual series (EUAS) is obtained by converting the equivalent value (at a specified  time,  usually  the  present)  of a  given  set  of  cash  flows  into  a  series  of  uniform  annual payments. Thus, if  interest is compounded annually, we can write

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The EUAS is widely used for analyzing decision  alternatives.

Example 7.4 The EUAS is particularly convenient when studying a repeated cycle o f   cash flows, as exemplified i n   Fig. 7-3. Applying (7.5) to the first 3-year cycle, we  have, assuming i = 9%:

EUAS ='[-$600 + $400(P/F,  9%, 1) + $300(PIF,  9%,  2) + $500(P/F,  9%,  3)]  (AIP,  9%,3)

= [-$600 + $400(0.9174) + $300(0.8417) + $500(0.7722)](0.3951)

= $160.24 per year for 3 years

Fig. 7-3

<!-- image -->

| End of Year   | Disbursements (Cash Outflows)   | Receipts (Cash Inflows)   |
|---------------|---------------------------------|---------------------------|

Because each cycle has this same EUAS (relative to its starting year), the EUAS for the entire series is $160.24 per year for 12 years.

In  the  important  special  case  CFo &lt; 0  and  CFj &gt; 0 (j &gt; O),  it  can  be shown  that  the  EUAS decreases, in almost linear fashion, as i increases. Furthermore, as is shown by (7.4), it becomes zero at the same value of  i for which PW (and FW) becomes zero.

If  many or all of  the cash flows are negative  (i.e., are costs), it may be convenient to deal with the negative of  the EUAS; we call this quantity the equivalent uniform annual cost (EUAC). It is clear that, in calculating the EUAS or EUAC, we may neglect any constant yearly cash flow (e.g., a fixed annual maintenance charge), and simply add in  that constant amount at the end.

## 7.4 CAPITAL RECOVERY

Let us apply the notion of  EUASIEUAC to an asset whose series of  cash  flows consists of  just two terms: an original cost, P, and an (actual or estimated) salvage value, SV, at the end of  n  years. For this series,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

in  which (3.5)  was used in  the last step.  Because here the EUAC represents the difference  between the annualized  cost  of  the asset  and  the annualized salvage value, it  is  retitled  the capital recovery (cost)  and resymbolized CR.

Example 7.5 A machine which  costs $50 000  when  new  has a 10-year lifetime and a salvage value equal to 10%  of its  original  value.  Determine  the  capital  recovery,  based  upon  an  interest  rate  of 8 ' / 0 per  year, compounded annually.

From (7.6), and (7.4)  gives

<!-- formula-not-decoded -->

This value represents the annualized net cost o f   the machine.

Unlike the EUASIEUAC in general, the CR does not take into account operating or maintenance expenses associated with  the asset.

## 7.5 CAPITALIZED EQUIVALENT

Suppose  that  a  given  sum  of money,  P,  earns  interest  at  an  annual  rate  i.  I f the  interest  is withdrawn  at the end of each  year but the principal is left intact, then a perpetual series of  uniform annual payments will  be obtained, the amount of  each payment being

<!-- formula-not-decoded -->

[(7.7) also follows from  (3.6).]

Looking  at  matters  the  other  way  round,  we  call  P  the  capitalized  equivalent  (CE)  of the perpetual  annual payments A, and write

<!-- formula-not-decoded -->

## Solved Problems

- 7.1 Determine the present worth of  the following cash flows, based on an interest rate of ( a ) 10% per year, ( b ) 15% per year, compounded annually. Explain the results.

| End of Year   |
|---------------|

y 1

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The PW at i = 15% is smaller than the PW at i = 10%; at the higher interest rate, a smaller present sum can generate the given series of positive payments.

- 7.2 Compute  the  corresponding  future  worths  of the  cash  flows  in  Problem  7.1.  Explain  the results.

Since the present worths are known, it is simplest to use (7.3).

- (a) FW = (S20 397.OO)(FIP; 10% , 5) (S20 397.00)(1.6105) 532 849.37
- (b FW (S18 388.IO)(FIP. 15% , 5) (S18 388.10)(2.0114) = $36 985.82

At  the higher interest  rate, the positive payments accumulate to a higher future value.

- 7 . 3 Compute the present worth of  the following cash flows at ( a ) i = 6% per year, ( b ) i = 15% per year, compounded annually.  Explain  the results.

| End of Year   |
|---------------|

y 1

- ( a PW = -$40  000 + $12 000(PIA,  6Oh, 4) = -$40 000 + $12 000(0.28859)-' = +$1581.48
- ( b ) PW = -$40  000 + $12 000(PIA,  15%, 4) = -$40  000 + $12 OOO(0.35027)-' = -$5740.71

In accordance with  the discussion in Section 7.1, the PW declines as the interest rate increases.

- 7.4 Compute the future worth and the equivalent uniform annual series value for the cash flows in Problem 7.3.  Explain  the results.

Use (7.3) and (7.4).

- ( a ) FW = ($1581.38)(F/P, 6Oh, 4) = ($1581.48)(1.2625) = +$1996.62 EUAS = ($1581.48)(AIP,  6%, 4) = ($1581.48)(0.28859) = +$456.40

<!-- formula-not-decoded -->

The behavior discussed in Sections 7.2 and 7.3 is exhibited  here: both FW and EUAS decrease as i increases.

- 7 . 5 An engineer is thinking of  starting a part-time consulting business next September 5, on his 40th birthday.  He expects the business will require an initial cash outlay of  $5000, to come from his savings, and will cost $500 per year to operate; the business ought to generate $2000 per year in cash receipts. During the 20 years that he expects to operate the business, he plans to deposit the annual net proceeds in a bank each year, at an interest rate  of 8% per year, compounded annually. When he retires, on his 60th  birthday, the engineer expects to invest whatever proceeds plus interest  he  then  has from the business  in  a  long-term  savings  plan  that  pays 10%  per year, compounded annually. What is the maximum amount he could withdraw from the savings plan each year during his retirement and still  have the funds last 15 years?

The net proceeds from the business will be $2000 -$500 = $1500 per year. Therefore, at the end of 20 years, the engineer will have

```
FW = SISOO(FIA, 8% , 20) = SSOOO(FIP, 8% , 20) $1500(45.7620) S5000(4.6610) $45 338 FW = SISOO(FIA, 8% , 20) SSOOO(FIP, 8% , 20) S1500(45.7620) S5000(4.6610) = 845 338
```

The maximum annual amount he could withdraw is therefore

```
A = $45 338(AIP,  10°/o,  15) = $45 338(0.13147) = $5960.59
```

- 7 . 6 Let  i = 15%  per year, compounded annually. Determine  the present  worth of  the following cash flows:

| End of Year   |
|---------------|

Analyze the last two flows as $2000 + $4000. Then,

```
PW = -$I0  000 + $2000(P/A,  15%, 4) + $4000(P/A,  lSO/o, 2)  (PIF,  15%, 2) = -$lo 000 + $2000(0.35027)-' + $4000(0.61512)-'(1.3225)-' = $626.93
```

- 7 . 7 Determine the EUAS for the repeated cycle of  disbursements and receipts shown in Fig. 7-4, i f   the interest  rate is 10%  per year, compounded annually.
- 7.8 A  machine costs $40000  to purchase  and  $10000  per year to operate. The machine  has no salvage  value,  and  a  10-year  life.  I f i = 10%  per  year,  compounded  annually,  what  is  the equivalent uniform annual cost of  the machine?

```
EUAS = [-$SO0 + $200(P/F,  10°/o,  1 ) + $150(P/F,  lo%, 2) + $300(P/F, 10°/o, 3) + $4OO(PIF, lo%, 4 1 1   (Alp,  10° /o,  4) = [-$SO0 + $200(1.1000)-' + $150(1.2100)-' + $300(1.3310)-' + $400(1.4641)-'](0.31547) = $96.03 per year for 16 years
```

The EUAC is  given  by  (7.4)  or (74, with  costs  counted  as  positive,  together  with  the  fixed operating cost.

```
EUAC = $40 000(A/P,  10°/o,  10) + $10 000 = $40 OOO(0.16275) + $10 000 = $16 510
```

I

Fig. 7-4

| End of Year   | Disbursements   | Receipts   |
|---------------|-----------------|------------|

- 7.9 A new bridge with a 100-year life is expected to  have an initial cost of $20 million. This bridge must be resurfaced every five years, at a cost of  $1 million. The annual inspection and operating costs are estimated to be $50 000. Determine the present-worth cost of the bridge using the capitalized equivalent approach (i.e., take the life of  the bridge as infinite). The interest rate is 10% per year, compounded annually.

The present worth of the nonrecurring cost is simply PI = $20 million. The recurring $1  million cost is equivalent  to

A 1 = ($1  000 000)(AIF, 1O0/0,  5) = ($1 000 000)(6.1051)-I = $163 797 per year

Thus, there are two annual costs, A1 = $163  797 and A2 = $50 000; their combined capitalized equivalent is

<!-- formula-not-decoded -->

and the total  present-worth cost is

PI + CE = $20  000 000 + $2 137 970 = $22  137 970

- 7.10 Determine the approximate size of  the annual payment needed to retire $70 000 000 in  bonds issued by a city to build a dam. The bonds must be repaid over a 50-year period, and they earn interest at an annual rate of  6 ' 1 0 ,   compounded annually.

To the extent that 50 years may be taken as infinite,

<!-- formula-not-decoded -->

- 7.11 A machine that cost $30 000 new  has an  &amp;year life and a salvage  value equal to 10% of  its original cost.  The annual  maintenance  cost  of  this  machine  is  $1000  the first  year,  with  an increase of  $200 each  year hereafter;  the annual operating cost  is $800  per year. Determine the EUAC of  this machine if  the interest  rate is  10% per year, compounded annually.

The EUAC is the sum of  three terms: the CR given by (7.6); the EUAC for the $200 gradient; and the fixed annual cost, $1000 + $800 = $1800.

$1800

EUAC = ($30  000 -$3000)(AIP,  lo%,  8) + (0.10)($3000) + $200(AIG,  lo%,  8) + = $27 OOO(0.18744) + $300 + $200(3.0045) + $1800 = $7761.78

## Supplementary Problems

- 7.12 Find the present worth o f   the machine o f   Problem 7.8. Ans. PW = -$I01  443.93 (the negative value indicates a cash outflow or cost)
- 7.13 Rework  Problem 7.8, using  annual  interest  rates  o f ( a )  5%, ( b )  IS%, and ( c )  20%, compounded annually. ( d ) Comment on the results.
- Ans. ( a ) EUAC = $15 180; (b) EUAC = $17 790; (c) EUAC = $19 541; ( d ) the EUAC increases with i , since all costs are positive and since the value o f   (AIP, i0/0,  10) increases as i increases.
- 7.14 A machine costs $30 000 to purchase and $12 000 per year to operate. The machine has a 10-year life and no salvage value. Determine the EUAC of  this machine at annual interest rates o f ( a )   5%, (b)  15%, and ( c )   20°/0, compounded annually. Ans. ( a )   $15 885.00; (b)  $17 977.50; (c)  $19 155.60
- 7.15 A used machine costs $20 000 to purchase. It has an  annual maintenance  cost o f $20 000, a salvage value of $5000, and  a 10-year  life.  I f the  interest  rate  is 10% per  year,  compounded  annually, what  is  the present-worth cost of   the machine? Am. $140 960.12
- 7.16 Rework Problem 7.6 for i = 8% per year, compounded annually. Ans. $2739.71
- 7.17 Use (7.2) to  determine  the  future  worth  o f the  cash  flows  in  Problem 7.6, for i = 8% per  year, compounded annually. Ans. $3727.20
- 7.18 Calculate by (7.2) the future worth  o f the cash  flows  o f   Problem 7.6, using ( a ) i = 15% per  year, ( b ) i = 8% per year, compounded annually. Ans. ( a )   $1096.50; (b)  $3727.38
- 7.19 Compute the future-worth cost of   the machine o f   Problem 7.15. Ans. $365 608.25
- 7.20 Compute the EUAC of   the machine of  Problem 7.15, using the result o f   Problem 7.15. Ans. $22 941.26 per year
- 7.21 Compute the capital recovery for the machine o f   Problem, 7.15, using (7.6). Compare with the answer to Problem 7.20. Ans. $2941.25 = $22 941.26 -$20 000
- 7.22 Determine  the  present  worth  o f the  following  series  o f cash  flows,  given  i = 15%: CFo = -$I0  000, CF, = CF2 = CF3 = CF4 = $5000, CF5 = -$2000, CFs = $3000. Ans. $6566.15
- 7.23 Calculate the present worth o f   the following cash flows, when i = 10% per year, compounded annually.

| End of Year   |
|---------------|

y

l

Ans. $2679.49

- 7.24 Calculate the present worth of  the following cash flows, i f   the interest rate is 12% per year, compounded annually.

| End of Year   |
|---------------|

y 1

Ans. -$1786.86

- A machine which costs $100 000 when new has a lifetime of 15 years and a salvage value equal to 20% of its original  cost.  Determine the capital  recovery  for  this  machine,  i f the interest  rate is 10% per year, compounded annually. Ans. $12 517.60 per year 7.25
- Repeat Problem 7.25, using a salvage value equal to 5% of  the machine's  original cost. Ans. $12 989.56 per year 7.26
- Determine the capital  recovery  for  the  machine  in  Problem 7.25, i f the interest  rate is 15% per  year, compounded annually, and total operating and maintenance costs are $2000 per year. Ans. $16681.60 per year 7.27
- Determine the amount of  money required  to generate an  infinite number of  annual payments of $5000 each, if  the interest  rate is 1O0/ 0 per year, ( a ) compounded annually, ( b ) compounded continuously. Ans. ( a )   $50 000; ( b )   $47 528.52 7.28
- Mr. Diamond expects to invest $1000 per year for each of the next 20 years in  an investment plan  that pays 10% per  year,  compounded  annually.  At  the end  of  the 20th  year,  he expects  to withdraw  the balance in  his investment  plan  and deposit  it  in  a savings account.  This savings account  pays 6% per year, compounded monthly. Mr.  Diamond wants to withdraw a fixed amount from  this savings account each month, for a total of  five years.  How large may this fixed amount be? Ans. $1107.13 7.29
- Repeat Problem 7.7 for an interest  rate of 15% per year, compounded annually. Ans. $74.71 per year for 16 years 7.30
- Costs of $10 000, $20 000, and $23 000 are incurred at the ends of  three successive years. Find the EUAC for k repetitions of  the cycle, if ( a ) i = 10% per year, ( b ) i = 15% per year, compounded annually. Ans. ( a )   $17 250.55 per year for 3k years; ( b )   $21 322.10 per year for 3k years
- A flood-control dam with a 100-year life has an initial cost of $15 million. The gates in the dam must be replaced  every  five  years,  at  a  cost  of $2 million.  If the  interest  rate  is 8% per  year,  compounded annually, what is the capitalized  equivalent of  the annual cost of  the dam? Ans. $4 261 412 7.32
- What is the total present worth of  the dam described  in  Problem 7.32? Ans. $19 261 412 7.33
- Assuming that money earns 10% a year, which would be the better arrangement for leasing an electron microscope: (1) paying a deposit of $100 000, to be returned at the end of  the lease period; or (2) paying $10 000 a year for as long as the device is kept? Ans. For (I),  (7.6) gives EUAC = iP = (0.10)($100  000) = $10 000, and so the two plans are equivalent. 7.34

## Net Present Value, Rate of Return, Payback Period, Benefit-Cost Ratio

This chapter continues  the  ideas developed  in  Chapter  7,  particularly  as  they  are  applied  in deciding among alternative capital investments.

## 8.1 NET PRESENT VALUE

The definition,  (7.1), of  the NPV is repeated here:

<!-- formula-not-decoded -->

in  which the notation emphasizes our assumption that the initial cash flow, CFo,  is negative (a capital outlay). No assumption is made concerning the signs of  the remaining CFj, although often these terms will  all  be positive  (revenues).  In  the special case CFj = A (j  = 1,2, . .  .  , n),  (8.1)  becomes,  in  view of (3.4),

<!-- formula-not-decoded -->

as it  must. Another name for the NPV is the discounted cash pow, or DCF.

From (8.1)  it is seen that the NPV is positive when and only when the total value of  the returns CF,  (in  year  0 dollars) exceeds the amount  invested,  lCFol (year  0 dollars);  that is to say, when and only when the original amount, earning compound interest at rate i for n years, would be insufficient to generate the returns. For a proposed investment to be economically acceptable, the NPV must be positive  or,  at  worst,  zero  (in  which  case  the  investment  of lCFol would  just  suffice  to yield  the revenues CFj).

Example 8.1 The  cash flows associated with a milling machine are CFo= -$50000. CFj = $15000 0' = 1,. .  . ,5). Use (8.2) to  determine  the  economic  acceptability  of  this  machine  at  interest  rates  of  (a) 10°/o, ( b )   15%, and (c) 20% per year, all compounded annually.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The  machine  is  seen  to  be  an  economically  acceptable  investment  when  the  interest  rate  is 1O0/0, and (barely) when the interest rate is 15%. It is not economically  justifiable to buy the machine if  the interest rate is 20%.

## 8.2 RATE OF RETURN

The rate of  return  (ROR) for a series of  cash flows is that particular value, i*, of  the interest rate for  which  the NPV vanishes. Thus, if  we  plot  the  NPV  as a function  of  i,  using  (8.1)  or (8.2),  the curve will  cross  the  i-axis  at  i*. Alternatively,  we  could  find,  by  trial  and error,  i-values for which the NPV is slightly  positive and slightly  negative, and interpolate linearly  between  them for i*. If  a more accurate  approximation  for  i* is required, the Newton-Raphson  iteration  method or another numerical  technique can be used to solve (8.1) or (8.2) for i, with the left side replaced by zero.

## Example 8.2 Find the ROR for the machine of  Example

By  linear interpolation between the results o f   Example 8.l(b)

8.1. and (c):

<!-- formula-not-decoded -->

## Case of  a Single Sign-Reversal

From Section 7.1,  we  know  that when  CFo &lt; 0 and  CFj &gt; 0 (j &gt; 0)-that  is, when  there is  just one reversal of   sign  in  the sequence CFo, CF1, CF2, .  .  . , CF,-the NPV is a monotone decreasing function  o f i,   and  so  i*  is  uniquely  determined.  Moreover,  at  this  unique  ROR,  the FW and EUAS are zero. (Compare Example 8.2 with Example 7.3 and Fig. 7-2.)

## Case o f   Multiple Sign-Reversals

When the sequence CFo,  CF,, CF2,. .  .  , CF,  shows more than one reversal of  sign, it is possible that NPV = 0 for several values o f   the interest rate; there could thus be several rates o f   return.

Example 8.3 For the series of  cash flows

| End of Year      |   0 |   1 |   2 |   3 |   4 | 5    |
|------------------|-----|-----|-----|-----|-----|------|
| Cash Flow, $1000 |  -3 |   0 |   6 |   6 |   0 | - 10 |

determine the NPV  at  annual interest rates OOh, 5%, lo%,  20%, 30%, SO%, and 70%. From a graph of  the results, find the rate(s) o f   return.

For the given flows,

<!-- formula-not-decoded -->

and evaluation at the specified interest rates gives the points

| i,%    |   5 |   10 |   20 |   30 | 50   |   70 |
|--------|-----|------|------|------|------|------|
| NPV, $ | 210 |  257 |  620 |  588 |      |  407 |

which are plotted in  Fig. 8-1. It  is seen that there are two rates o f   return in  this case, i* -7% and i* = 54%.

An  upper bound on  the number of  (positive) rates o f   return may  be obtained by  deriving from (8.1) the polynomial equation

<!-- formula-not-decoded -->

for x = 1 + i*. According to Descartes' rule o f   signs, the number o f   positive real roots x cannot exceed the  number o f   sign changes in  the series o f coefficients CFo,  CFl, .  . .  , CF,.  Now,  a positive x  might correspond to a negative i*; therefore, the number o f   sign changes is a fortiori an upper limit on the number of  i*-values. In  particular, i f   there are no sign changes, there is no ROR for the given flows.

Example 8.4 There are two sign reversals in  the cash flows o f   Example 8.3, and two values of i * were found. In  this case, the upper bound is actually attained.

I f multiple  i*-values exist,  it  is  usually  better  to  abandon  the  ROR  method  and  instead  to. investigate the sign o f   the NPV for various assumed values o f   the interest rate.

<!-- formula-not-decoded -->

<!-- image -->

## 8.3 PAYBACK PERIOD

The payback  period  (PBP)  is  the  time  required  for  an  initial  investment  to  be  recovered, neglecting the time value of  money. Thus, if  lCFol represents the initial investment and CFj is the net cash inflow for the jth year (j = 1,2,.  .  .  , n), the payback period satisfies

<!-- formula-not-decoded -->

If  the yearly cash  inflows are equal, or if  an average value is used, then (8.4) simplifies to

<!-- formula-not-decoded -->

where YCF represents the (average) yearly cash inflow.

Example 8.5 Determine the payback period for a proposed investment as follows:

| End of Year      |   0 |   1 |   2 |   3 |   4 |   5 |
|------------------|-----|-----|-----|-----|-----|-----|
| Cash Flow, $1000 | -50 |  10 |  12 |  15 |  18 |  20 |

The sum of  the first three yearly cash  inflows, $37 000, is less than the initial investment, $50 000; but the sum o f   the first four yearly cash inflows,  $55 000, exceeds the initial investment. Hence the payback period will be somewhere between 3 and 4 years. Linear interpolation yields

<!-- formula-not-decoded -->

Because it ignores the time value of  money, the payback  method should not be used in place of the  other  methods  discussed  above.  On  the  other  hand,  the  payback  method  is  valuable  for  a secondary  analysis,  when  the  NPV  or  ROR  is  used  as  the  primary  method.  As  will  be  further discussed  in  Chapter 9, there are many practical examples where an investment  is sought with a high rate of  return and a sufficiently short payback  period.

Fig. 8-1

Example 8.6 Determine the payback period and the net present value for each proposal in Table 8-1, using an interest rate o f 10°/ o   per year, compounded annually. Which proposal is best?

Table 8-1

|             | Cash Flows   | Cash Flows   | Cash Flows   |
|-------------|--------------|--------------|--------------|
| End of Year | Proposal A   | Proposal B   | Proposal C   |
| 0           | -$75 000     | -$75 000     | -$75 000     |
| 1           | 25000        | 20 000       | 0            |
| 2           | 25000        | 25000        | 0            |
| 3           | 25000        | 30 000       | 0            |
| 4           | 25000        | 35000        | $130000      |

Proposals A and B each have a Iyear payback period; however, proposal A has an NPV o f   $4248, while proposal B has an NPV of $10 289. Proposal C has an  NPV of  $13 792, but it  has a 3.58-year  payback period (assuming the $130 000 to be evenly spread over the fourth year). In summary:

| Proposal   | NPV, $   |   PBP, years |
|------------|----------|--------------|
| A          | 4248     |         3    |
| B          | 10 289   |         3    |
| C          | 13792    |         3.58 |

Since proposal A is inferior to proposal B, it  can be eliminated from further consideration. Proposal C is economically superior to proposal B, but its longer payback period might constrain the decision maker to choose proposal B instead (e.g., i f   the f i r m were cash-poor and could not afford to wait until the end of  the third year to receive any cash inflows). Thus, the choice o f   the best investment alternative may involve a trade-off  among two or more objectives, with  the PBP providing important secondary information.

## 8.4 BENEFIT-COST RATIO

The benefit-cost ratio (BCR) is often used to assess the value of  a municipal  project in  relation  to its cost; it  is defined as

<!-- formula-not-decoded -->

where B represents the equivalent value of  the benefits associated with the project, D represents the equivalent  value of  the disbenefits, and C represents the project's net cost. Similarly,  the net benefit value (NBV) is defined as

<!-- formula-not-decoded -->

For a  project  to  be  desirable, BCR &gt; 1 or NBV&gt;O. This  rule  must  be  applied  with  caution, however,  since  benefit  quantification  is  usually  not  very  precise  and since  the distinction  between disbenefits  and  costs  is  somewhat  conjectural.  The BCR may  vary  considerably  depending  on whether the disbenefits are included in  the numerator, or are classified as a cost and included in  the denominator.  If  questions arise  about  the classification  of  disbenefits,  it  is  better  to  use  the  NBV approach, because (8. 7 ) gives the same value irrespective of  how the disbenefits are classified.

Either present worth (the NPV), future worth, or the EUAS approach may be used  to evaluate B, D, and C, provided the same method be used for all three terms.

Example 8.7 A large city is located close to a major seaport.  It has been proposed that a new superhighway be built  between  the city  and the seaport, running parallel  to the present congested, two-lane highway. A  group of consulting engineers has estimated that the new highway will provide the following direct benefits: (1) additional commerce between the city and the seaport, having a value of $50 million  per year; (2) future economic growth within  the region  over a  10-year  period,  resulting  in  an  increase of $5 million  per year in  commercial activity, beginning in  the second year; (3) a  reduction in  highway accidents,  resulting in a direct savings of  approximately $0.8 million  per year. On the other hand, the following disadvantages or disbenefits are associated  with the new highway:  (i) the destruction o f   valuable farmland  that currently contributes $1.3 million  per year to the regional economy; (ii) a decrease in commercial activity along the present highway,  resulting in a loss of $0.7 million  per year.  Assess  the desirability  o f the proposed superhighway, based on a construction cost of $280 million  and a yearly maintenance cost o f $1.5 million.  Assume a lifetime of 30 years and an interest rate of 7%, compounded annually.

Over the entire 30-year period, the yearly net benefits, B -D, are given  by  the EUAS method as

<!-- formula-not-decoded -->

Similarly, the yearly costs are given  by

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Since BCR &gt;.I, the proposed  highway  is considered  to be desirable.

## Solved Problems

- 8.1 Compute the net present value (NPV) of  the following cash flows:

| End of Year      | 0   |   1 |   2 | 3   |   4 |   5 |
|------------------|-----|-----|-----|-----|-----|-----|
| Cash Flow, $1000 | - 6 |   4 |   2 | - 3 |  -2 |   3 |

The interest  rate is 15O/0 per year, compounded annually.

BY  (8.1 ), and the benefit-cost ratio is

<!-- formula-not-decoded -->

- 8.2 A new plant to produce steel tubing requires an initial investment of  $10 million. It is expected that after three years of  operation an additional investment of  $5 million will  be required; and after six  years of  operation, another investment of  $3 million.  Annual operating costs will  be $3  million  and  annual  revenues  will  be  $8  million.  The life  of the  plant  is  10  years.  If  the interest  rate is 15%  per year, compounded annually,  what is the NPV of  this plant?

The data imply a level cash flow of

<!-- formula-not-decoded -->

per year in  years 1 through 10, plus flows of -$5 000 000 and -$3 000 000 in  years 3 and 6, respectively. Hence, in  units of  $1 million,

<!-- formula-not-decoded -->

= 10.5096

or $10 509 600.

- 8.3 The XYZ Company is contemplating the purchase of  a  new  milling  machine. The purchase price of  the new  machine is $60 000 and its annual operating cost is $2 675.40. The machine has a life of  seven years, and it is expected to generate $15 000 in revenues in each year of  its life,  What is the net  present value of  the investment in  this machine i f   the interest  rate is (a) 8% per  year,  (b) 10%  per  year,  (c) 12%  per  year,  compounded  annually?  Interpret  your results.

In years 1 through 7, the net annual cash flow is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

When the interest rate is less than lo%, the present worth of  the annual cash flows of $12 324.60 for 7 years is greater than the $60 000 investment; hence, the NPV is a  positive number. When the interest rate is  lo%, the present  worth  of  the annual  cash  flows  is  just  equal  to the $60000 investment,  and NPV = 0. When the interest rate is greater than  lo%, the present  worth of  the annual cash flows is less than the investment, and the NPV is negative. Thus, when the interest rate is above 1O0h,  it would not be economical to purchase the milling machine.

- 8.4 Determine the rate of return (ROR) for the machine of  Problem 8.3.

By definition, the R O R  is the interest rate at which  NPV = 0; thus, by Problem 8.3(b), ROR = 10%. (For the given cash flows,  we know that the R O R  is unique.)

- 8.5 Find the ROR for cash flows of  -$50  000 in year 0 and +$I6  719 each year in years 1- 5.

From (8.2),

<!-- formula-not-decoded -->

Locating the combination  n = 5, AIP = 0.33438 in Appendix A, we see that i * = 20%.

- 8.6 Solve Problem 8.5 by trial and error, using (8.2).

T r y  i = 15%

<!-- formula-not-decoded -->

The given  cash  flows  are such  as to make the NPV monotonically decreasing in i ; hence i * , the value at which the NPV vanishes, must be greater than 15%.

Try i = 25%

<!-- formula-not-decoded -->

Since the NPV now is negative, it must be that 15% &lt; i * &lt; 25%. Try a  rate that is halfway between these two rates:

Try i = 20%

<!-- formula-not-decoded -->

Hence, i * = 20%.

8.7 Solve Problem 8.5 by  linear interpolation between  i = 15% and i = 25%.

Using the NPV-values calculated  in Problem 8.6,

<!-- formula-not-decoded -->

The value 20.45% is slightly  in  error  because  we  have  used l i n e a r interpolation  over a  relatively wide range of  values (from 15% t o 25%), whereas (8.2) is a  nonlinear equation.

## 8.8 Compute the ROR for the following cash flows:

| End of Year   |
|---------------|

y 1

Descartes'  rule tells us to expect no more than three positive values for i * . Adding and subtracting $31 000 from CF2, we obtain

<!-- formula-not-decoded -->

As a first approximation,  neglect the last term on the right:

<!-- formula-not-decoded -->

From the tables in  Appendix  A, we see that:

|     |   (AlP; i% ,3) |
|-----|----------------|
| 30% |        0.55063 |
| 40% |        0.62936 |

Hence,  for  the  approximate equation, 30% &lt; i *   &lt;40%. Restoring  the  neglected  term  should  pull i* closer  to 30% ; hence, try i = 30% :

<!-- formula-not-decoded -->

Under  the  previous  approximation,  NPV = -$31000(P/F, i*%,  2)-$18000, and  under  the  present approximation,  NPV = -$I3  860.15; we conclude that i * &lt; 30%. Try i = 8%:

<!-- formula-not-decoded -->

Hence, i *  &gt; 8 %. Try i = 10%:

Hence, 8% &lt; i * &lt; 10%. Try i = 9%:

<!-- formula-not-decoded -->

Hence, 8% &lt; i* &lt; 9%. By  linear interpolation,

<!-- formula-not-decoded -->

It is not difficult to show that there are no other positive values- in  fact, no other real values--of i* besides i * = 8.83%.

- 8.9 Determine the payback period  (PBP) for the cash flows of (a) Problem 8.5,  (b)  Problem 8.8. (c) Comment on the results in the light of  the corresponding ROR-values.

<!-- formula-not-decoded -->

- (b) We have CFl + CF2 = $29 000, CFl+ CF2 + CF3 = $59 000; hence,

<!-- formula-not-decoded -->

- ( c ) The cash flows o f   Problem 8.5 have a longer payback period, but a higher rate o f   return, than those of Problem 8.8. We  might  say  that  the  PBP  and  the  ROR  give  opposite  rankings o f the  two investments. However, we must always bear in  mind  that the PBP takes no account o f   interest.
- 8.10 In  Example 8.7, assume  that  the affected  farmers  are lobbying  for relocation  payments and subsidies to compensate them for the lost farmland. Estimates of  "equitable" payments vary widely, but one number being considered is an annual payment of  $3.25 million per year to the farmers over the 30-year period. Would the project still be desirable, with this new disbenefit?

<!-- formula-not-decoded -->

Since BCR &gt; 1, the project is still desirable.

- 8.11 A  public  works  project  is  proposed  that  has total  present-worth  benefits of  $75  million  and total  present-worth  costs of  $55 million.  In  deliberating this proposal, some members of  the town  council  have  suggested  that  the  project  has  a  total  present-worth  disbenefit  of  $15 million;  other  members  feel  the  $15  million  should  be  treated  as  a  cost.  How  should  the proposal  be evaluated?

In  this  particular case,  it  makes  very  little  difference whether  the $15 million  is  classified  as  a disbenefit or as a cost. I f   the $15 million is treated as a disbenefit,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

However, to eliminate any confusion, (8.7) should be used:

<!-- formula-not-decoded -->

Since NBV &gt; 0, the project is economically acceptable.

- 8.12 The ABC Company is considering the purchase of  a new sanding machine; machine models A and  B  are available.  Both  models  have a  five-year  life,  and  their cash  flows are as given  in Table 8-2. The interest rate is 10% per year, compounded annually. Which model should ABC buy?

I f   it is treated as a cost,

## NPV, ROR, PBP, BCR

Table 8-2

|             | Cash Flows   | Cash Flows   |
|-------------|--------------|--------------|
| End of Year | Model A      | Model B      |
| 0           | -$30 000     | -$30 000     |
| 1           | 10 000       | 30000        |
| 2           | 10 000       | 5000         |
| 3           | 10 000       | 3000         |
| 4           | 10 000       | 2000         |

By  the net present value method:

<!-- formula-not-decoded -->

By  the payback  period  method:

<!-- formula-not-decoded -->

By  the rate o f   return  method:

<!-- formula-not-decoded -->

and by  linear interpolation in Appendix A,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By  trial and error:

and by linear interpolation,

<!-- formula-not-decoded -->

It is seen that all three methods rate model B above model A; ABC should purchase model B.

<!-- formula-not-decoded -->

## Supplementary Problems

- 8.13 A new plant to produce tractor gears requires an  initial investment o f   $10 million. It is expected that a supplemental investment of  $4  million  will  be  needed  every  3 years to  update the  plant. The  plant  is expected to start  producing gears 2 years after the initial investment is made (at the start o f   the third year).  Revenues o f $5  million  per  year  are  expected  to  begin  to  flow  at  the start  o f the fourth  year. Annual operating and maintenance costs are expected to be $2 million per year. The plant has a 15-year life. List  the annual cash flows.
- Am. CFo = -$I0  000 000,  CFI = CF2 = 0,  CF3 = -$6 000 000,  CF4 = CF5 = CF7 = CFs = CFlo = CFll= CF13 = CF14 = $3 000 000, CF6 = CF9 = CF12 = CFIS = -$I000  000
- 8.14 What  is  the  NPV  of  the  plant  in Problem  8.13  i f the  interest  rate  is  10%  per  year,  compounded annually? Ans. -$5 336 645.33
- 8.15 Is the plant described in  Problems 8.13 and 8.14 an  economically acceptable investment? Ans. No, because the NPV is negative.
- 8.16 A different plant from  the one described in  Problem 8.13 can  be  built for an  initial investment o f   $13 million  and no supplemental investments. All other data are the same as in  Problems 8.13 and 8.14.  (a) Compute the net present value. (b) Is this plant an  economically acceptable investment? Ans. (a) +$855  708.47;  (b) yes
- 8.17 Is the investment described in  Problem 8.16 still economically acceptable i f   the interest rate is 15%  per year, compounded annually? Use the net present value method. Ans. No: NPV = -$3 624 238.52 &lt; 0.
- 8.18 Compute  the  NPV  of  an  investment  with  CFo = - $ S O   000  and  CFj = +$I2  000 0' = 1,. .  . ,6) i f the annual interest rate,  compounded  annually, is  (a) 8%, (b)  lo%, (c)  12%, (d) 15%.  (e) Interpret  the results.
- Ans. (a) $5473.37;  (b) $2262.53;  (c) -$663.98; (d) -$4586.74.  (e) The investment is not economically acceptable  when the  interest rate  is  12% or  greater,  in which case  the  present  worth o f   the  cash flows  is less than the (present worth of  the) investment.
- 8.19 Is  the  conclusion  of Problem  8.15  changed  i f the  interest  rate  is  5%  per  year,  compounded  annually? Ans. No:  NPV = -$I928 607.02.
- 8.20 What  is  the  NPV  of the  investment  described  in  Problem  8.13  i f the  interest  rate  is  3%  per  year, compounded annually? Ans. $48 465.06
- 8.21 What can be said about the ROR of  the plant of   Problem 8.13, in  view  o f   the results o f   Problems 8.19 and 8.20? Ans. There is at least one value o f i * between 3%  and 5%.
- 8.22 Approximate the ROR for Problem 8.18  by  interpolation between  the results o f   Problem 8.18(b) and (c). Ans. i * . = 10.454%
- 8.23 Compute the  payback  period  for  the  investment o f (a) Problem 8.3,  (b) Problem  8.16, ( c ) Problem 8.18. Ans. (a) PBP = 11 years; (b) PBP = 8 years; (c) PBP = 4.17 years
- 8.24 What  is  the  NPV  o f the  plant  described  in Problem  8.16,  if the  interest  rate  is  12% per  year, compounded annually? Ans. -$1 195 881.54
- 8.25 What is the ROR of  the plant described in  Problem 8.16? Solve by  interpolation, using the NPV data from Problems 8.16 and 8.24. Ans. 10.834%
- 8.26 What can be said about the ROR for a set of  positive cash flows? Ans. Since the NPV is positive for every positive i, no ROR exists.

- 8.27 Rework Problem 8.12 if  the interest rate is (a) 15% per year, (b) 25% per year, compounded annually. Am. (a) NPVA = -$1450.60, NPVs = $2983.17  (buy  model  B).  (b)  Neither  model  is  economically acceptable;  both have negative net present  values.
- 8.28 A  new  highway has been  proposed  to join  two cities, at  a  total construction  cost of  $700000000.  The new highway has a 20-year life. It would render obsolete the current railroad system connecting the two cities, which would be dismantled at a cost of  $100 000 000. This would put the 4000 railroad employees out of  work; they would each  be paid $6000 per year  in  damages, for a total of  20 years. The railroad would  require  a  $1  000000  annual  maintenance  program  i f it  is  kept.  The  railroad  property  has  an assessed valuation  of  $30000000;  the property  would  be purchased  at  that figure and  used as the new roadbed. The highway is estimated to yield, in taxes on the trucks using it, $0.005 per ton-mile more than the railroad; a total of  500 million annual ton-miles of  use is expected. It is also estimated that the general tax revenues would increase by $10 000 each year because of  the new highway. On theother  hand, it is estimated that the new highway would cost $2 000 000 per year to maintain. What is the BCR for the new highway, relative to the current railroad, assuming the project would be financed by 7% per year interest-bearing bonds, with the interest compounded annually? What is the NBV? [Hint: The annual cost for 20 years is given by

and the corresponding annual benefit is (500 000 000)($0.005) + $10 000(A/G, 7%, 20).] Am. BCR = 0.0249,  NBV = -$I00  770 537.00

- 8.29 Should the highway in Problem 8.28 be built? Why? Ans.

No, because the BCR is less than 1.0 and the NBV is negative, relative to keeping the railroad.

- 8.30 A state agency is contemplating giving a total of  $5 000 000 in grants to various universities. These grants would be paid out in  installments of  $500 000  per  year over  a 10-year period. The grants would enable low-skilled persons to be retrained for new  jobs, with a resulting benefit of  $5000 per year in  increased income for each of  1000 persons in  the regional labor force, over  the next 10 years. These state grants would  enable  the  universities  to  obtain  a  total  of $1 000000  in  matching  federal  funds  for  their operations,  thereby  reducing  by  $1  000000  the  total  amount  of  state funds which  would  normally  be required by the universities. However, the grants would require 10 persons to be added to the university staffs at an  average  annual salary of  $20 000 each, which  would have to be paid out of  state funds. The current  annual  interest  rate  is  10%  on  funds  of this  type.  Is  the  retraining  program  an  economical investment  for  the  state,  on  a  present-worth  basis?  Compute  both  the  present-worth  BCR  and  the present-worth NBV. Ans. BCR = 8.33,  NBV = +$27 035 330.26; yes, it is economical.
- 8.31 Does the answer  to Problem 8.30  change if  the BCR  and  NBV are computed in  terms of  annualized costs? Ans. BCR = 8.33,  NBV = +$4 400 000; again the investment is economical.
- A state agency is contemplating  building a new 5630-acre industrial park. The property can be acquired at a cost of  $1000 per acre. Roadways and other improvements are estimated  to cost a total of  $1000 per acre, with these costs spread evenly over the next 10 years. The few residents currently on the property will be moved out over the next three years; the displacement costs are estimated at $1  000 000 this year, $500 000 next year, and $200 000 the year after. The park is expected  to provide the state with new tax revenues of  $5 000 000  per  year,  starting five  years from  now,  with  an  increase  of  $2 000 000  per  year thereafter. The state has decided to evaluate this project on the basis of  a 10-year lifetime. The funds for the project will  be borrowed  at an interest rate of  7%  per year, compounded  annually. (a) What is the present-worth  NBV of  the project? (b) What is the present-worth BCR? (c) Is the project economically justifiable? Am. (a) $14 401 566; (6) 2.30; (c) yes 8.32

## Choosing  Among  lnvestmen  t  Alternatives

## 9.1 SETTING THE MARR

In Chapter 6 we introduced the MARR as the smallest yield rate at which a proposed investment would be acceptable.  How is this cut-off  rate arrived at?

1. The MARR may be set equal to the interest rate that is available at a local savings bank or other  institution.  The MARR  then  becomes  the "opportunity  cost  of money," in  that  it measures the opportunity lost from not placing money in  the bank.
2. For most businesses, the savings bank  rate would  be lower than  their usual overall  rate of return on investment. Thus, the MARR is sometimes set equal to the firm's current average return on total investment.
3. The MARR may be purposely set higher than either the bank rate on savings or the firm's current return on investment. It may be set according to the firm's long-range profit goals, so as to achieve  a  desired  future growth  rate; it  may  be set  at a  high ,level to encourage  the search for more profitable new ventures; it may be chosen large to offset the high degree of risk  attached to the investment.

Under option 1  and (within the law of  averages) under option 2, the MARR is an attainable rate; i.e.,  there are investment  alternatives that actually  achieve that rate.  However, under option 3,  the MARR is a target rate, with no guaranteed means of  realization.

Example 9.1 The  ABC  Company  is  currently  earning  an  average  before-tax  return  of  25%  on  its  total investment. The board of   directors o f   ABC is considering three proposals as given in  Table 9-1.

Table 9-1

|               | Cash Flows   | Cash Flows   | Cash Flows   |
|---------------|--------------|--------------|--------------|
| End of Year I | Proposal A   | Proposal B   | Proposal C   |

Proposal A is for a new machine that will replace  one of  their older, worn-out pieces o f   equipment; this machine is vital to ABC's  production. Proposal B is for a plant expansion. Proposal Cis  for an addition to ABC's  product line. There is a high probability that this product could fail in the marketplace,  resulting  in the loss of  most o f   the $50 000 initial  investment.  The board feel that they  would need at least a  40% rate  of  return on this  project  to  compensate  for its additional riskiness. Which o f   these three proposals are acceptable?

Compute net  present values,  using  the attainable MARR of 25% for proposals A and  B,  and  the target MARR of  40% for proposal C:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Only proposal A is acceptable (NPVA &gt; 0).

The ROR method leads to the same conclusion: linear interpolation in  Appendix A gives

<!-- formula-not-decoded -->

and only i : exceeds the associated MARR.

Because NPVs  and NPVc, though negative, are small in  magnitude (causing i : and i; to be just under their associated MARRs), the ultimate decisions concerning proposals B and C may have to be made on the basis o f other considerations, such  as ABC's long-term product strategies and  the company's ability to raise capital. If capital is scarce, proposal A must be given the highest priority, since ABC's  continued profits appear to depend on that piece o f   machinery.

Example 9.2 The  XYZ Company has $50  million  which  can  be  invested  in  proposal  A  ( i : = 17%) or  in proposal  B  (iz = 29%);  or  else  it  can exercise  the  do-nothing  alternative  and  invest  the  $50  million  in modernizing current operations. A target MARR of  35%  has been established by XYZ's management to achieve their long-range  plans and strategies. The XYZ Company currently earns an average o f   25% on its total investment in  plant and equipment, some of  which is very old. Which alternative should XYZ pursue?

For  the  do-nothing  alternative,  i* = 25%;  thus,  none  o f the  three  alternatives meets  the  desired  35% MARR.  If the  company  is  serious  about  the  35%  MARR,  then  additional  alternatives should  be  sought. Proposal B, which has an ROR slightly better than the current average rate o f   return on total investment, would clearly enhance the company's average rate o f   return. In  addition, given that some of  the company's plant and equipment is "very old," using the available $50 million for refurbishing this old plant and equipment might also improve  the company's  average rate o f return.  One  reasonable strategy  would  be  to spend  part  of  the $50 million on  new  plant and equipment, and then to search for higher-profit proposals (e.g., a 35%  ROR) on which to spend the balance.

## 9.2 PROJECT SELECTION AND BUDGET ALLOCATION

Determining  the  best  way  to allocate  a  given  budget  among  several  competing  projects  is  a commonly  encountered  problem,  because often  there  are  more  worthwhile  project  proposals and ideas than can be funded with the available monies. The solution principle is to evaluate each project in  terms of  present worth  or some similar measure, and to choose  that set o f   projects for which  the sum of  the measures is a maximum, subject to the budget constraint.

## Independent Projects

Two or more proposals or projects are independent when the acceptance or rejection of any one of them  does  not  entail  the  acceptance  or  rejection  of any  other.  For  instance,  a  proposal  to air-condition  the company  offices and  a  proposal  to undertake an  advertising campaign  for a  new product would  usually be considered  independent.

For independent  projects,  the following  selection  algorithm  will  always  maximize the financial return on the available monies.

- Step 1 Compute i* for each project.
- Step 2 Eliminate any project whose i*-value is less than the MARR (if  no MARR exists, omit this step).
- Step 3 Arrange the surviving proposals from step 2 in descending order of  i*-value.
- Step 4 Select  proposals  from  the  top  of this  list  downward,  until  an  additional  selection  would exceed the available funds or the budget.

If, as often will be the case, some funds remain at the end of step 4, there are three options: (i) if  one or more of  the remaining projects is divisible into subprojects, then these subprojects may be funded, using the above algorithm,  until the available funds are exhausted; (ii) the remaining funds may be invested in  the do-nothing alternative,  at the MARR (for an attainable MARR) or at some rate less than the MARR (for a target MARR); (iii) the remaining funds are simply "left over."

Example 9.3 The BK Company is considering five  proposals for  new  equipment, as indicated in  Table 9-2. Each  piece of equipment has a life of  100  years. Treating that  period as infinite, the ROR will  be the interest rate at which I is  the capitalized equivalent o f   the perpetual series o f   payments R ; hence, (7.8) gives the third row  of Table 9-2.  The BK  Company has established a MARR o f   11%  and  has a budget o f   $325 000.  Which proposal(s)  should the company select?

Table 9-2

|                   | Proposal 1   | Proposal 2   | Proposal 3   | Proposal 4   | Proposal 5   |
|-------------------|--------------|--------------|--------------|--------------|--------------|
| Annual Revenue, R | $5000        | $6000        | $25000       | $16000       | $20000       |
| Investment, I     | $60000       | $50000       | $100000      | $100000      | $100 000     |
| i* - RII          | 8f%          | 12%          | 25%          | 16%          | 20%          |

Using the selection algorithm, we  obtain the following list:

Proposal  2  is  acceptable from  the standpoint o f the  MARR criterion,  but  insufficient funds are  available  to include it. Thus, proposals 3, 5, and 4 are selected, and $25 000 is left unspent from  the $325 000 budget.

|                                   | i*   | Investment   | Budget cut-off   |
|-----------------------------------|------|--------------|------------------|
| Proposal 3                        | 25%  | $100000      |                  |
| Proposal 5                        | 2OoA | $100 000     |                  |
| Proposal 4 ...................... | 16%  | $100000      |                  |
| Proposal 2 ...................... | 12%  | $50000       | MARR cut-off     |
| Proposal 1                        | 89h  | $60000       |                  |

## Mutually Exclusive Projects

A  set  of  projects  are  mutually exclusive  if  at  most  one of  them  may  be accepted.  It  is  thus a question of  picking the single economically best project (or of  rejecting them all).

For  mutually  exclusive  projects,  the  selection algorithm  given  below  will  always  yield  the maximum  total  return  on  the  total  amount  invested. First,  we  shall  need  some terminology.  Let I denote the investment cost of  a project, and R the measure of  revenues @resent worth, EUAS, etc.) from  the project.  We shall say  that  project 1 dominates  project 2 if Il 5 I 2 and Rl r Rz. Clearly, a dominated project can never be the best of  a mutually exclusive set. Further, for any two projects-a standard  and a  challengeraefine the incremental rate o f   return  of  the challenger as

<!-- formula-not-decoded -->

- Step 1 Eliminate any project whose investment exceeds the budget.
- Step 2 Arrange the surviving projects in  ascending order of  investment (break  any investment-ties arbitrarily).  Now eliminate any project  that is dominated by another project; the candidates that  remain  will  be  in  ascending  order  both  of  investment  and  of  return.  Compute  i* for each candidate.
- Step 3 Eliminate from further consideration any candidate having i* &lt; MARR.
- Step 4 From the surviving candidates, select  as the standard that candidate which  has the smallest investment.
- Step 5 Compute the incremental  rate  of  return  of  the challenger  that  immediately  succeeds  the standard in  the list of  candidates.

- Step 6 If hi* I MARR, eliminate this challenger from further consideration  and repeat step 5 for the next challenger; if  Ai* &gt; MARR, eliminate the old standard from further consideration, replace it with this challenger  as the new standard, and repeat step 5.
- Step 7 Select the one surviving candidate: it is the best alternative.

Example 9.4 The KLN Company is attempting to determine the economically best size of  processor  machine for their facilities. The six alternative  machine sizes which are feasible  are as given in  Table 9-3. Each  machine has a life of  100 years and no salvage value, so that i * = RII, as in  Example 9.3.  The company has a total capital budget of  $350 000 and a MARR of  15%. Which machine should they buy?

Table 9-3

| Size of Machine   | Annual Revenue, R   | Investment, I   | i*     |
|-------------------|---------------------|-----------------|--------|
| Economy           | $ 7200              | $60000          | 12%    |
| Regular           | 25000               | 100 000         | 25%    |
| Super             | 36000               | 200000          | 18%    |
| Delux             | 45000               | 220000          | 20.45% |
| Bulk              | 50000               | 300000          | 16.67% |
| Extended          | 52000               | 385000          | 20.5%  |

The Extended machine is  unacceptable according  to step 1 of  the selection  algorithm,  and  the Economy machine is unacceptable according to step 3. The application  of  steps 5 and 6 to the four surviving candidates is shown in Table 9-4; step 7 gives Delux as the winner.

Table 9-4

| Comparisons       | i *               | Steps 5 and 6                                                                                                                                                    |
|-------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Regular VS. Super | 25% VS. 1 8 OI o  | Standard #1 A R $36000 - $25000 $11000 - 11% < MARR VS. Ai* =-= Challenger #l A $200000-$100000=$100- Decision: reject challenger #1 and repeat step 5           |
| Regular VS. Delux | 25% VS. 20.45%    | Standard 81 VS. 1 Ai* = ------. $20 - - 16.7% > MARR Challenger #2 $120 000 Decision: replace standard #1 (Regular) with challenger #2 (Delux) and repeat step 5 |
| Delux VS. Bulk    | 20.45% VS. 16.67% | Standard #2 VS. ~ i * = - - $5OoO - 6.25% < MARR Challenger #3 $80000 Decision: reject challenger #3                                                             |

Let us examine the logic of  the selection  algorithm, on the  assumption  that the company can  realize 15% (the  MARR) by  implementing the do-nothing  alternative.  Consider  the first  comparison  in  Table 9-4.  Super costs AI = $100 000 more than Regular, and yields A R = $11 000 more per year. If  the company chose Super, it

would,  in  effect,  be  making  $11  000  a  year  on  a  $100000  investment;  that  is,  it  would  be  investing  at  rate Ai* = 11%, whereas it could be earning MARR = 15%. Choosing Super would thus entail an opportunity loss of

<!-- formula-not-decoded -->

Or, looked at in  a slightly different way, if  the Regular machine is purchased,  at a saving of  $100 000, the company  will  earn  $25 000  a  year  on  the  machine,  plus  15% x $100 000 = $15 000  a  year  on  the  do-nothing alternative.  This is a total annual return of  $40 000 on a total investment of  $200 000. The same total investment in the Super machine will earn only $36 000 a year.

In this first comparison, it so happens that the economically superior machine has the larger  i*-value. Note however, that the eventual winner, Delux, has a smaller i*-value than Regular. As we have seen, when purchase prices differ, a mere comparison of  i*-values is not decisive; one must also consider what will be done with any funds left over from the purchase of  the cheaper machine.

## Other Interrelationships Between Projects

A  project  may  be  contingent  upon  some  other  project,  in  the  sense  that  the  acceptance  or rejection of  one may result in  the corresponding acceptance or rejection of  the other. For example, the purchase of  a new computer storage disk may be contingent on the purchase of  a new computer.

Some projects may be joint, in  that either both are accepted or both are rejected. For instance, though they may be purchased separately, the tractor and trailer of  a rig for highway hauling of  steel are normally  joint items.

Some projects  may  be financially  interdependent;  i.e.,  approval  of  one exhausts  the available funds and thus precludes approval of  the other.

Joint  projects  should  be  treated  as  a  single,  total  project  or  investment.  Contingent  projects should be evaluated both jointly and separately. The basic investment should first be evaluated alone. The contingent items should then be brought in  and their effect on  the total investment  evaluated. Financial interdependences are usually resolved by considering the irreducibles, those factors to which a dollar value cannot be attached.

Example 9.5 Which project(s) in Table 9-5 should  be approved, if  the budget  is $150 000 and the MARR is IS%?

Table 9-5

| Project   | Investment                       | i *                 |
|-----------|----------------------------------|---------------------|
| A B C D E | $100000 50000 50000 50000 150000 | 20% 20% 20% 20% 20% |

This is an  instance  of  financial interdependence.  Because of  the $150 000 budget, selecting  project  A and either B, C, or D precludes selecting any others; selecting E precludes selecting any others; and selecting B and C  and  D  precludes  selecting  any  others.  Thus,  there  are  five  alternatives  (investment  portfolios),  each representing a  total investment  of  $150 000 and each  with  an  ROR of  20%. The choice among  them must  be made on the basis of  the intrinsic characteristics of  the projects, the need for a diversified portfolio,  and other irreducible factors.

## 9.3 THE REINVESTMENT FALLACY

It  is  implicitly  assumed  in  the  NPV,  EUASIEUAC,  and  ROR  methods  that  any  cash  inflows generated by an investment are reinvested, at the rates MARR, MARR, and i*, respectively. If such an assumption does not hold, and if  the assets being compared have unequal service lives, fallacious results may be obtained.

Here, C is the initial investment, A is the annual net cash inflow, and n is the service life o f   the asset. The ROR method yields:

<!-- image -->

Example 9.6 Consider two competing projects, for which MARR = 16%:

|                                         |                 | A A           |
|-----------------------------------------|-----------------|---------------|
| Project A Project B Project A Project B |                 | 523 000       |
|                                         | 100 000 100 000 | 35 000 35 000 |

<!-- formula-not-decoded -->

Hence, according to the MARR, project A is acceptable and project B is not.

However, suppose that the cash flows can be reinvested at 25%, compounded annually. Thus, the $23  000 annual cash inflows from project A are actually equivalent to a future value

<!-- formula-not-decoded -->

nine years hence, and the annual cash inflows from project B are actually equivalent to a future value

<!-- formula-not-decoded -->

nine years hence. Thus (the initial investments being equal) project B is actually the preferred alternative.

The reinvestment fallacy  can  be avoided  if  the MARR is set  at  the reinvestment  rate (whose value,  however,  may  be very  difficult  to  predict)  and  if  future  values  based  on  this  MARR  are compared, as in  Example 9.6.  As for the matter of  unequal lives, it can sometimes be ignored, and the  NPV,  EUAC, or ROR method  applied  notwithstanding.  For  other situations,  a  replacement method  which  assumes  that  each  asset,  at  the end  of  its  useful  life,  is  replaced  with  a  new  asset identical in  kind, may be more appropriate. This method will be employed in Chapter 10.

## Solved Problems

- 9.1 The  management  of  the  Conway  Corporation  is  considering  five  alternative  new-product proposals that their employees have submitted to them:

| Pr0P-l        | Rate of Return   |
|---------------|------------------|
| Fryer         | 49%              |
| Box Loader    | 26%              |
| Conveyor      | 19.5%            |
| Planer        | 23%              |
| Cutter-Loader | 26.5%            |

Conway currently enjoys an  average return of 260h on total investment. Which proposal(s) is (are) acceptable?

Using the current average return on total investment as the MARR, only Fryer and Cutter-Loader are strictly acceptable. If   the rule is: ROR r MARR, then Box Loader is also acceptable.

- 9.2 Rework Problem 9.1 i f   Conway desire a future average return of 31%.

Only Fryer is acceptable under the target MARR.

- 9.3 The  Wyandot  Company  currently  earns  an  average  rate  of return  of 30°h on  its  total investment. The board of  directors of  Wyandot is considering the three proposals whose cash flows are specified in Table 9-6. Which proposal(s) is (are) acceptable, if  the board of directors has set a target MARR of 25%? Make an NPV calculation.

Table 9-6

|   End of Year | Proposal A   | Proposal B   | Proposal C   |
|---------------|--------------|--------------|--------------|
|             0 | -$SO 000     | -$75 000     | -$loo 000    |
|             1 | 15000        | 30 000       | 35000        |
|             2 | 15000        | 30 000       | 35000        |
|             3 | 15000        | 30000        | 35000        |
|             4 | 15000        | 30000        | 35000        |

<!-- formula-not-decoded -->

Since all  three net present values are negative, none o f   the projects is acceptable.

- 9.4 Solve Problem 9.3 by an ROR calculation.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

All  three  ratesof  return  are  smaller  than  the  target  MARR  (2S0/0),  and  so  none  o f the  projects is acceptable.

- 9.5 With reference to Problems 9.3 and 9.4, how would Wyandot's average return on investment be affected  by the acceptance of  proposal  B?

The effect would depend on the amount of   Wyandot's  total invested capital.  Suppose Wyandot to be a very small f i r m , whose total investment before accepting proposal B is $225 000. Since i i ,  the rate o f return o f   proposal B, is 21.85%  (by linear interpolation in  Appendix A), the average rate o f   return after acceptance of   proposal B would be

<!-- formula-not-decoded -->

or a decrease of about 2%. However, i f   Wyandot were a larger company, with, say, $925 000 in invested capital, then the new average rate would be

<!-- formula-not-decoded -->

a decrease o f   only $/ o .

- 9.6 Refer  to Problem  9.3.  Suppose  that  if  proposal B were  rejected,  the competition  would  be likely  to introduce a  new  product that would  cut Wyandot's  market share in  half, and hence cause them  to suffer  a  50%  reduction  in  current  profits.  Should  proposal B  be accepted  or rejected under these circumstances?

We have seen that acceptance of  proposal B is  unprofitable per se. However, rejection could only prove more unprofitable (unless Wyandot's profits  are minuscule to begin with). Thus, proposal B should be accepted, as "the lesser o f   two evils."

- 9.7 The  Clearwater  Company  has  a  budget  of  $500000  which  can  be  spent  on  the  five  independent projects of  Table 9-7. If  MARR = 20°/0,  how should the budget be allocated?

Table 9-7

|   Project Number | j *   | Total Project Cost   |
|------------------|-------|----------------------|
|                1 | 29.1% | $150000              |
|                2 | 10.5% | 50000                |
|                3 | 21.5% | 200000               |
|                4 | 19.5% | 75000                |
|                5 | 23.2% | 25000                |

The selection algorithm for independent projects gives:

| Step 2   | Eliminate projects 2 and 4.   |         |
|----------|-------------------------------|---------|
| Step 3   | Select Project1               | $150000 |
|          | Project 5                     | 25000   |
|          | Project 3                     | 200000  |
|          |                               | $375000 |

with $500 000 -  $375 000 = $125 000 unspent.

- 9.8 Rework Problem 9.7 if  (a) MARR = 25' 1 0 , (6) MARR = 19%, (c) MARR = 18% and capital is rationed at $400 000.
- (a) Only project 1 can be funded; $350 000 remains unspent.
- (b) Only project 2 is unacceptable, and $450 000 is spent as follows:

| Project 1   | $150000   |
|-------------|-----------|
| Project 3   | 200000    |
| Project 4   | 75000     |
| Project 5   | 25000     |
| TOTAL       | $450 000  |

## CHAP.  91 CHOOSING AMONG INVESTMENT ALTERNATIVES

- (c) The MARR eliminates project 2, and the ranking becomes:

|           | Project Cost   | Cumulative Amount Spent   |
|-----------|----------------|---------------------------|
| Project 1 | $150000        | $150000                   |
| Project 5 | 25000          | 175000                    |
| Project 3 | 200000         | 375000                    |
| Project 4 | 75 000         |                           |

Unless it is divisible,  project 4 cannot  be funded:  its inclusion would exceed  the $400000 budget constraint.

- 9.9 Grampian Manufacturing Company is attempting to determine the "best 7 ' -sized  milling machine for their production shop. Five alternative sizes are  available, as  given in Table  9-8. Grampian has a budget of  $250 000, and MARR = 15%. Which size machine should they purchase? Assume that  n = 100 years and that the ultimate salvage value is zero for each machine.

Table 9-8

| Size        | Annual Revenue   | Initial Cost   | i*     |
|-------------|------------------|----------------|--------|
| Economy     | $5000            | '$50000        | 10%    |
| Regular     | 25000            | 100000         | 25%    |
| Super       | 36000            | 200000         | 18%    |
| Delux       | 45000            | 220000         | 20.45% |
| Super Delux | 50000            | 300000         | 16.67% |

This situation involves mutually exclusive projects. The selection  algorithm  (Section 9.2) gives:

Step 1 Eliminate Super Delux.'

Step 2 See Table 9-8.

Step 3 Eliminate Economy.

Steps 4 through 6 Compare Super against Regular:

<!-- formula-not-decoded -->

hence, eliminate Super. Compare Delux against Regular:

<!-- formula-not-decoded -->

hence, Delux becomes the new standard.

Step 7 Select  Delux.

In this case, $30 000 will be left over from  the original $250 000 budget.

- 9.10 Rework Problem 9.9 for MARR = 20%.

Now  only  Regular  and  Delux  survive  step 1 of  the  algorithm.  From  step 5, with  Delux  as  the challenger,

<!-- formula-not-decoded -->

Hence, Regular is selected, and $100 000 is spent.

- 9.11 Rework Problem 9.9 for a budget o f   $200 000.

In  this case, Delux and Super Delux are eliminated in step 1  o f   the algorithm,  and Economy in step 3. Then, only Regular and Super remain; from Problem 9.9, Regular wins.

- 9.12 The  CCC  Corporation  is  weighing  the  purchase  of a  computer.  The  basic  machine  costs $200 000; the costs of  various peripheral equipment are:

| Slow Printer                  |
|-------------------------------|
| Fast Printer                  |
| Low-Resolution Video Display  |
| High-Resolution Video Display |
| Disk Drives (each)            |
| Remote-User Ports (each)      |
| Software                      |
| Special Disks                 |

The job that the  computer would perform is now being done  by hand, by five persons, at an annual salary and overhead cost of $100 000. Though these people would all be  replaced by the  computer, the purchase o f   the computer would necessitate the hiring o f   two programmer-operators  and one mathematician, at a total salary and overhead cost o f   $80 000. Classify the investment decisions and proposals involved in this situation.

The  peripheral  equipment  are  all  contingent  projects-contingent  on  the  purchase of the  basic computer. The slow and fast printers are mutually exclusive, as are the high- and low-resolution videos. Some type of  printer and/or video, some software, some disks, and one or more disk drives would seem to  be  mandatory:  they  are  joint  proposals with  the computer. The do-nothing alternative (continuing with  the  handicraft  technology  o f five persons) and  the  computer  purchase alternative are  mutually exclusive projects.

- 9.13 If,  in  Problem 9.12,  CCC has only $210 000 available  for the computer system, exclusive  of software, does this introduce any financial interdependences?

Yes. If  $10 000 is spent on the slow printer, then no other peripherals can be purchased. If  $10 000 is spent on some combination  of  peripherals (e.g., special disks plus one remote-user port plus one disk drive plus one high-resolution video), then  no other items can  be purchased beyond the basic computer.

- 9.14 For the data o f   Problem 9.12 and Table 9-9, and for MARR = 15%, should the computer be purchased? What peripherals should be purchased?

Table 9-9

| Comparison                                  | hi*   |
|---------------------------------------------|-------|
| Do-Nothing vs. Basic Computer plus Software |       |
| Slow vs. Fast Printer                       |       |
| Low- vs. High-Resolution Video Computer     |       |
| Computer with One Disk Drive                |       |
| vs. Computer with Two Disk Drives           |       |
| Zero vs. Two Remote Ports                   |       |

The basic computer plus software, one slow  printer, one disk  drive, one low-resolution video, and two remote ports should  be  purchased, since hi* &gt; MARR for these items. The high-resolution video may  be justifiable on the basis o f   irreducibles, such as operator eye-fatigue, since its hi* is  not that far away from the established MARR.

- 9.15 ABC Company have decided to automate certain of  their procedures by installing a computer system. The cash flows for two competing systems are given in Table 9-10; both systems have a five-year life and zero salvage value. If  the MARR is 15%,  which system should ABC purchase?

Table 9-10

|   End of Year | System 1   | System 2   |
|---------------|------------|------------|
|             0 | -$SO 000   | -$75 000   |
|             1 | 22000      | 24000      |
|             2 | 22000      | 24 000     |
|             3 | 22000      | 24000      |
|             4 | 22000      | 24000      |
|             5 | 22000      | 24000      |

In  the case of equal lifetimes, the NPV (or the EUAS) is a linear function of  initial cost and annual revenue; hence we compute

<!-- formula-not-decoded -->

As ANPV &lt; 0, system 2 is economically inferior to system 1; system 1 should be purchased.

- 9.16 In a situation like that of  Problem 9.12,  the directors of  a f i r m are trying to decide whether to buy  computer  system  A,  to  buy  computer  system  B,  or  to stay  with  the  current  manual technology. Advise them, given a MARR of 15% a planning horizon of  4 years, and costs as in Table 9-11.

Table 9-11

|                 | Manual   | System A      | System B      |
|-----------------|----------|---------------|---------------|
| Equipment       |          |               |               |
| Computer        |          | $200000       | $200000       |
| Printer         |          | 20000         | 10 000        |
| Video           |          | 5000          | 2000          |
| Disk Drives     |          | 4000          | 4000          |
| Remote Ports    |          | 2000          | 0             |
| Disks           |          | 5000          | 2000          |
|                 |          | TOTAL $236000 | TOTAL $218000 |
| Software        |          | 100 000       | 50000         |
| Annual Manpower | $100000  | 80 000        | 40 000        |
| Annual Overhead | 50 000   | 20 000        | 40 000        |

We compare either computer system to the manual technology by the difference method of  Problem 9.15, choosing present-worth  cost as economic parameter. For system B versus manual,

<!-- formula-not-decoded -->

and for system A versus manual,

<!-- formula-not-decoded -->

The  strict  conclusion  is  that  the  current  manual  technology  should  be  retained.  However,  a consideration of the irreducibles (e.g., improved output quality when the job is done by computer) might make system B more attractive.

- 9.17 Illustrate  the  reinvestment  fallacy  by  supposing  that,  in  Problem  9.15,  the  revenues  from system 2 could  be reinvested  at 40%  in years 3 through 5.

At the end of   five years, the net future worth of  system 1 is:

<!-- formula-not-decoded -->

and the net future worth o f   system 2 is (draw a time diagram):

<!-- formula-not-decoded -->

The effect o f   the reinvestment is to reverse the conclusion of  Problem 9.15: now, system 2 is the better.

## Supplementary Problems

- 9.18 The executives of   the XYZ Company are considering the three independent proposals whose cash flows are given in  Table 9-12, The MARR is 10%. Evaluate these three proposals by the NPV method.
- Ans. NPVA = $2180.87, NPVB = $8824.93, NPVc = -$7355.69; proposal C is unacceptable.
- 9.19 Rework Problem 9.18 for MARR = 15%.
- Ans. NPVA = -$3003.40, NPVB = 0, NPVc = -$21527.68; proposals A and  C are  unacceptable and proposal B is barely acceptable.
- 9.20 Evaluate the three proposals in  Problem 9.18 using the ROR method and linear interpolation. Ans. iT\ = 12%, ig = IS%, iz = 7.71%; since i g &lt; MARR, proposal C is unacceptable.

Table 9-12

|   End of | Proposal A   | Proposal B   | Proposal C   |
|----------|--------------|--------------|--------------|
|        4 |              |              |              |

- 9.21 The capital budgeting committee of   the ABC Company is contemplating five independent proposals for projects to be included in  the forthcoming year's budget; their cash flows are given in Table 9-13. The ABC Company has established a MARR of  20%. Assuming that capital is not rationed, which projects should the company select and what is the total investment required? Use the ROR method.
- Ans. i : = 15%, iz = 20°h, i T = 25%, iz = 21.85% (by interpolation), i 3 = 12%. Projects2,3, and4 should be selected. at a total investment o f   $430 000.
- 9.22 Would  the  results  o f Problem 9.21  change  if  (a) MARR = lo%? (b)  MARR = 13%  and  capital  is rationed at $430 000? Ans. (a) no; (b) no
- 9.23 How would the results of  Problem 9.21 change i f   the MARR is 13%, the budget constraint is $480 000, and all the projects are divisible into smaller projects? Ans. Select projects 2, 3, and 4, and spend $50 000 on project 1.
- 9.24 How would  the  results  o f Problem 9.23  change i f the  MARR is 16%  and  none of  the  projects are divisible? Am. Select projects 2, 3, and 4, and leave $50 000 unspent.
- 9.25 Would the results of  Problem 9.24 change i f   all the projects were divisible? Ans. no
- 9.26 The executives of  the XYZ Company are attempting to determine the economically best process-control computer to purchase for one o f   their production lines. The choice has been narrowed to the five mutually exclusive  alternatives  whose cash flows are presented in Table  9-14. I f   capital is not rationed and the MARR is 7%, which computer should the company purchase? Ans. C or D
- 9.27 Will the result o f   Problem 9.26 change i f   the MARR is (a) 1O0/0? (b) llO/o?  (c) 13%? Ans. (a) no; (b) no; (c) yes (none o f   the alternatives is acceptable)
- 9.28 Rework Problem 9.26 i f   capital is rationed at (a) $30 000, (b) $28 000, (c) $25 000. Am. (a) C; (b) C; (c) E

Table 9-13

|   End of Year | Project1   | Project 2   | Project 3   | Project 4   | Project 5   |
|---------------|------------|-------------|-------------|-------------|-------------|
|             0 | -$lo0 000  | -$200 000   | -$I50 000   | -$80 000    | -$300 000   |
|             1 | 35027      | 77258       | 63516       | 32000       | 98769       |
|             2 | 35027      | 77258       | 63516       | 32000       | 98769       |
|             3 | 35027      | 77 258      | 63516       | 32000       | 98769       |
|             4 | 35027      | 77 258      | 63516       | 32000       | 98769       |

Table 9-14

|   End of Year | Computer A   | Computer B   | Computer C   | Computer D   | Computer E   |
|---------------|--------------|--------------|--------------|--------------|--------------|
|             0 | -$20 000     | - $30000     | - $28000     | -$35 000     | - $25000     |
|             1 | 6309.40      | 9057.60      | 9218.44      | 1 1523.05    | 7886.75      |
|             2 | 6309.40      | 9057.60      | 9218.44      | 11523.05     | 7886.75      |
|             3 | 6309.40      | 9057.60      | 9218.44      | 1 1523.05    | 7886.75      |
|             4 | 6309.40      | 9057.60      | 9218.44      | li 523.05    | 7886.75      |

- 9 . 2 9 For what combinations of  capital  rationing and  MARR values  in  Problem 9.26 would computer B be preferred  to computer C? Ans. None: C dominates B (Section 9.2).
- 9 . 3 0 The executives  of  the ABC Company  are trying  to select  the most  economical  feeder machine.  Cash flows for the six available models are shown in Table 9-15. The MARR is 8%. ( a ) Compute the ROR for each alternative model. ( b ) Determine which model should be purchased. Ans. ( a ) i i = l o % , ig = 25'10, ic = 18%, i&amp; = 20.5%, ig = 19.S0h, : i = 20.5%; (b) F
- 9 . 3 1 Which model should be purchased in  Problem 9.30, i f   there is a budget constraint of ( a )   $280 000? ( b ) $230 000? ( c )   $210 000? Ans. ( a )   E ;   ( b ) D; ( c ) C
- 9 . 3 2 How would the result of  Problem 9.30(b) change if  the MARR is ( a )   9%? ( b )   l o % ? ( c )   12%? ( d ) 15%? ( e )   20%? Ans. (a)-(e) no change
- 9 . 3 3 How  would  the result  of  Problem 9.30(b) change  if  MARR= 15% and  the budget  constraint  is ( a ) $210 000? ( b )   $280 000? Ans. ( a ) B (the only choice); ( b ) D
- 9 . 3 4 The KJL Company  is contemplating five  independent  projects,  with  cash flows as in  Table 9-16. The MARR is 12% and the budget constraint is $200000. ( a ) Compute the rate of  return for each project. ( b ) What is the optimum  portfolio, if the minimum desired payback  period  (Section 8.3) is  two years? Ans. ( a ) iX = ig = i E = i s = ig = 15O/0. ( b ) PBPA = PBPe = PBPc = 2.28 years,  PBPo = 2.055 years PBPE = 2.0 years;  the only acceptable choice is project E.
- 9 . 3 5 How would the result of  Problem 9.34(b) change if ( a ) the minimum desired payback period is 2.2 years? ( b ) the minimum desired payback period is 2.2 years and the budget constraint is $150 000? Ans. ( a ) D, or E, or D and E; ( b ) D or E

Table 9-15

|   End of Year | A        | B         | C         | D         | E         | F          |
|---------------|----------|-----------|-----------|-----------|-----------|------------|
|             0 | -$50 000 | -$lo0 000 | -$200 000 | -$220 000 | -$250 000 | -$380 000  |
|             1 | 13 190   | 37185     | 63991.20  | 74 386.40 | 82693.50  | 128485.60  |
|             2 | 13 190   | 37185     | 63991.20  | 74 386.40 | 82 693.50 | 128 485.60 |
|             3 | 13 190   | 37 185    | 63 991.20 | 74 386.40 | 82693.50  | 128 485.60 |
|             4 | 13 190   | 37 185    | 63 991.20 | 74 386.40 | 82693.50  | 128 485.60 |
|             5 | 13 190   | 37 185    | 63 991.20 | 74 386.40 | 82 693.50 | 128485.60  |

Table 9-16

|   End of Year | Project A   | Project B   | Project C   | Project D   | Project E   |
|---------------|-------------|-------------|-------------|-------------|-------------|
|             0 | -$100000    | -$50000     | -$75 000    | -$60 000    | -$95 000    |
|             1 | 43798       | 21 899      | 38 848.50   | 30000       | 50 000      |
|             2 | 43798       | 21 899      | 38 848.50   | 29000       | 45000       |
|             3 | 43798       | 21 899      | 38 848.50   | 18228       | 26 609      |

- 9 . 3 6 Two alternative cleaning machines are being considered as replacements  for an older, worn-out cleaner. The cash flows for the two mutually exclusive alternatives are presented in Table 9-17; the MARR is 10%. ( a ) Compute  the  present-worth  difference  of  value  (APW)  between  the  two  machines. ( b ) Compute  the incremental rate of  return (Ai*)  on the investment difference between the two machines. (c) Which machine should be purchased? Ans. ( a ) $816.33; (b) 37.9% ; ( c ) machine #2

Table 9-17

|   End of Year | Machine #1   | Machine #2   |
|---------------|--------------|--------------|
|             0 | -$20 000     | -$28 000     |
|             1 | 4 864.60     | 8419.88      |
|             2 | 4 864.60     | 8 419.88     |
|             3 | 4 864.60     | 8419.88      |
|             4 | 4 864.60     | 8419.88      |
|             5 | 4 864.60     | 8 419.88     |
|             6 | 4 864.60     | 8419.88      |

## Equipment Replacement and Retirement

## 10.1 RETIREMENT AND REPLACEMENT DECISIONS

The decision to replace equipment or to retire it (to take the equipment  out of  service without replacing  it)  can  be motivated  by  the physical  impairment  of  the equipment,  its obsolescence,  or external  economic  conditions.  Retirement  and  replacement  decisions  should  always  be  based  on economics rather than on whether or not the equipment  has reached the end of  its physical service life.  A  piece of  equipment may have many years of  service life remaining beyond the point at which it  has become uneconomical to operate it.

All past  investments and expenses connected  with  the equipment  are sunk  costs, which do not enter  into  a  retirement/replacement  decision. Only  current  and  future  costs  and  investments  are relevant.

## 10.2 ECONOMIC LIFE OF AN ASSET

As operating  equipment  ages,  the  usual  pattern  is  for  its  capital  costs  to  decline  while  its operating costs rise.  When summed,  these two cost  functions often  result  in  a  cost function  that is generally  U-shaped. Ideally,  the equipment  should be retired  at the lowest point on this total cost function.

Example 10.1 A machine has an initial cost o f   $10 000. Being a special-purpose custom-built unit, it can only be resold as scrap at $500, no matter what its age. The machine has a 10-year service life. The annual operating costs are $2000 for each o f   the first two years, with an increase o f   $600 per year thereafter. The MARR is 10%. When is the optimum time to retire the machine?

The cost curve for this type o f   problem is the net EUAC, evaluated at the MARR, as a function o f   time. From Section 7.4, we  know that the net EUAC will be made up of   two components: the capital recovery cost,

<!-- formula-not-decoded -->

and the equivalent annualized operating cost,

In  deriving ( I ) , the constancy o f   the salvage value was used; in  deriving (2), the gradient series was extended backwards by  writing the first year's cost as $1400+  $600. In  both expressions, j is the time, in years; thus, to keep the machine for 4 years would cost the company CR(4) + A(4) per year.

Substituting j = 1,2, .  . .  , 10 in  (1)  and (2), we generate Table 10-1; the points are plotted in Fig. 10-1. The data show that the machine should be retired at the end o f 7 years.

The time  interval  for  which  the  EUAC of  an  asset  is smallest  (7  years,  for  the  machine  of Example 10.1)  is called  the economic  life of  the asset.  As we have seen,  the economic life is given analytically  as that value j*  at which

is minimized.

The concept of  economic life may also furnish  the basis for a replacement decision, particularly when service lives are not precisely known, when salvage values in each year are not known, or when the equipment obsolesces rapidly.

Table  1 0 -1

|   Years of Service Life, j | CR(J')    | A(j)     | EUAC(j) = CR(I')+A(j)   |
|----------------------------|-----------|----------|-------------------------|
|                          1 | $10500.00 | $2000.00 | $12500.00               |
|                          2 | 5523.81   | 2000.00  | 7523.81                 |
|                          3 | 3870.05   | 2181.24  | 6051.29                 |
|                          4 | 3046.97   | 2400.77  | 5447.74                 |
|                          5 | 2556.10   | 2629.99  | 5186.09                 |
|                          6 | 2231.30   | 2859.40  | 5090.70                 |
|                          7 | 2001.40   | 3085.07  | 5086.47 = min.          |
|                          8 | 1830.68   | 3304.85  | 5135.53                 |
|                          9 | 1699.58   | 3518.12  | 5217.70                 |
|                         10 | 15%.13    | 3724.16  | 5320.29                 |

F i g .   1 0 - 1

<!-- image -->

Example 10.2 The XYZ Company purchased a very specialized machine three years ago for $25000. This machine is not  readily salable and is assumed to have a zero salvage value. Operating costs are expected to be $10 000 next year, and to increase by $800  per year thereafter. The company has an opportunity to replace the existing machine with another specialized one that will cost $12 000. This machine has no salvage value, a useful life o f   10 years, and operating costs o f   $5000 in the first year, with an annual increase o f   $1200 thereafter. I f   the MARR is IS%, should the company replace the old machine with the new one?

For the new machine:

| Year, j   | EUACG) = $12 000(AIP, 15%, j ) + $5000 + $12OO(AIG,IS%, j)   |
|-----------|--------------------------------------------------------------|
| 1         | $18800.00                                                    |
| 2         | 12940.52                                                     |
| 3         | 11344.16                                                     |
| 4         | 10793.96                                                     |
| 5= j*     | 10 647.20                                                    |
| 6         | 10687.52                                                     |
| . . .     | (increases)                                                  |

The economic life of  the new machine is thus 5 years, with a corresponding EUAC of $10  647.20. For the old machine,

<!-- formula-not-decoded -->

which is a strictly increasing function of  j .  Hence,  j* = 1 year, with a corresponding EUAC of $10 000.

The old machine should be kept for its economic life of  one more year, since its EUAC of $10 000 is less than the EUAC of $10 647.20 for the new machine. At the end of  that year, the analysis should be repeated and updated to take any new information into account. If  there is no new information, and the above data are still valid, then at the end of  next year the old machine should be replaced by the new one, because, at that time, the EUAC for the old machine will be

## 10.3 RETIREMENT/REPLACEMENT ECONOMICS

The decision  to retire a  piece of  equipment  is seldom  taken  without  replacing that equipment. Thus, in most cases,  a  joint  retirernentlreplacement decision  is made.

The optimum  retirementlreplacement  point  is  that  point  where  the  EUAC curve  of  the old machine  and  the  EUAC curve  of the  new  machine  intersect.  Thus,  if in  Example 1 0 . 1 a  new replacement  machine were  available  whose  EUAC was $5500 at five  years and $4000 at  all  years beyond the fifth,  then  the old  machine should  be retired  at the end of  the fifth  year, and replaced with the cheaper new machine.

Example 10.3 The XYZ Company owns a Cyear-old pump that originally cost $3000. For the past four years the operating and maintenance costs of  this pump have been:

C k

|   Year of Service, 1 |   Operating and Maintenance Costs, C k $ 90 |
|----------------------|---------------------------------------------|
|                    2 |                                         180 |
|                    3 |                                         560 |
|                    4 |                                         950 |

The  company  originally  planned  to keep  this  pump 8 years.  If the  pump  is  retained,  the expected  future operating and maintenance costs will be:

C k

|   Year of Service, k 5 |   Operating and Maintenance Costs, C k $1125 |
|------------------------|----------------------------------------------|
|                      6 |                                         1500 |
|                      7 |                                         1700 |
|                      8 |                                         2000 |

The pump could be sold today as a used pump for SVo = $1200. It is expected that the pump could be sold a year from  now for $900; two years from  now for $800; and afterwards for $500. A new, energy-saving pump, with expected service life of 8 years, has just become available for P = $4000. Its costs are as follows:

| Year of   |   Service, j | Operating and Maintenance Costs, Cj   |
|-----------|--------------|---------------------------------------|
|           |            1 | $ 40                                  |
|           |            2 | 80                                    |
|           |            3 | 260                                   |
|           |            4 | 450                                   |
|           |            5 | 625                                   |
|           |            6 | 1000                                  |
|           |            7 | 1200                                  |
|           |            8 | 1500                                  |

It is estimated that if this new  pump is purchased it could be sold one year later for $3100, two years later for $2000, three years later for $1500, four years later for $1000, and thereafter for $900. Given a MARR of 15%, should the XYZ Company replace the old machine now, or at some later time?

In computing the EUAC curve of  the old pump, the sunk costs o f   years 1 through 4 are disregarded.  Thus, k = 5 becomes j = 1, and we have:

where

<!-- formula-not-decoded -->

Similarly, for the new pump, where

<!-- formula-not-decoded -->

Evaluating  (1) for j = 1,. .  . , 4 and  (2) for  j = 1, .  .  . ,8, we  generate Table 10-2. It  is  seen  that  all  the EUAC-values for the new  pump are below  the lowest EUAC-value for the old pump. Hence, the old  pump should immediately be replaced by the new one. Even in  the worst case, where the new  pump is kept for only two years, its EUAC would still be lower  than  that for  keeping the old  pump for even one more year. The reader should note the oscillation o f   the EUAC curve for the new  pump; the curve is not  o f   the simple form shown in Fig. 10-1.

Table 10-2

| Years From Now, j   | EUAC(j)                          | EUAC'(j)                                                         |
|---------------------|----------------------------------|------------------------------------------------------------------|
| 1 2 3 4 5 6 7 8     | $1605.00 1663.90 1796.30 1852.18 | $1540.00 1588.84 1436.55 1384.18 1402.41 1371.86 1368.52 1387.94 |

The question  of  how  long  the  new  pump should  be  kept  is  readily  answered from  its  EUAC data:  its economic life is 7 years. Of  course, the unexpected advent o f   some new technology could alter these plans,  just as the availability o f   the new  pump altered the XYZ Company's original plans.

## Comparative Use Value

It is sometimes useful  to compare EUAC's via the comparative use value (CUV) of  the current equipment relative to the replacement equipment. Let subscripts 1 and 2 pertain to the current and replacement machines, respectively; after nl and n2 years of  service, their annualized  operating and

<!-- formula-not-decoded -->

maintenance costs are Al(nl) and A;(n2), and their salvage values are SVI and SV2. Then, the CUV is given  by

<!-- formula-not-decoded -->

where P 2   is the initial cost of machine 2. By (10.1), the CUV is the putative market price of  machine 1 that makes EUACl(n1) = EUAC2(n2).  If  the actual market or current salvage value, PI, is known, (10.1)  can be solved algebraically to yield

<!-- formula-not-decoded -->

That is, the C W   of  the current machine with respect to a replacement  machine is the market value of  the current  machine  plus  the present  value  of  all  annual  cost  savings realized  over  the service period of  the current machine.

It is evident from (10.2) that CUV &gt; P1  if  and only if  EUAC2(n2) &gt; EUACl(nl); in this case, and only then, the current machine should be kept.

Example 10.4 Compute the CUV for keeping the old  pump of  Example 10.3 another four years, as against buying the new pump and keeping it seven years.

Substituting the numerical values from Example 10.3 and Appendix A into (10.2), we find

<!-- formula-not-decoded -->

The CUV is less than the current salvage value by  $1381, which amount represents the present-worth loss that would be incurred in keeping the old  pump four more years.

## Present-Worth Method for Equal Service Periods

If machines 1  and 2 have present-worth costs PWl and PW2, and service periods nl = n2 = n,  then

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and so

Thus, a comparison of  EUAC's may be replaced by a comparison of  PW's (although  usually there is no computational advantage in so doing).

## Short-Study-Period Method for Unequal Service Periods

In the case nl # n2, we might compare the costs of  a series of  machines 1 and a series of  machines 2 over  the least  common  multiple  of  nl and  n2; this  approach  will  be illustrated  in  Section 10.4. However, if  we do not want to assume a continual substitution of  machines in  kind, we may restrict the study  period  to the smallest  of  nl,  n2, and  the forecasting horizon.  Thus,  only known  data are included  and  tenuous  estimates  are  ruled  out.  In  this short-study-period  approach,  any  "unused" values or costs are distributed back over the study period.

Example 10.5 The ABC Company is contemplating replacing its current  milling  machine with  an  improved machine. Data are as shown in Table 10-3. The executives at the ABC Company do not feel that any estimates beyond 10 years are accurate for decision making purposes. If  the MARR is 1S0/0,  should the company replace the current machine with the new improved one?

The length of  the study period is the minimum o f   15, 10, and 10 years; i.e., 10 years. The present-worth cost of   15 more years o f   service from the current machine is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Tab

|                  | II Salvage Value   | II Salvage Value   |               |             |              |
|------------------|--------------------|--------------------|---------------|-------------|--------------|
|                  |                    | End of Life        | Original Cost | Annual Cost | Service Life |
| Current Machine  | $500               | $100               | $5000         | $1000       | 15more years |
| Improved Machine | -                  | 500                | 7000          | 375         | 10 years     |

Annualizing this over the 10-year study period gives

<!-- formula-not-decoded -->

For the improved machine:

<!-- formula-not-decoded -->

Thus,  keeping  the  current  machine  is  $1745.13-  $1262.25 = $482.88 cheaper  (per  year  for  10  years)  than replacing it with the improved machine.

Example 10.6 Suppose  that  in  Example  10.5  the  company  executives  feel  they  cannot  accurately  forecast annual costs beyond five years into the future. All other data remain the same.  Using a five-year study period, we obtain for the current machine:

<!-- formula-not-decoded -->

and for the improved machine:

<!-- formula-not-decoded -->

The numbers are different, but the decision is the same as before: it is cheaper to keep the current machine. The difference between  the alternatives in  the 5-year study is $2389.08 -$1889.85 = $499.23,  which is slightly larger than  the $482.88 difference found  in  the 10-year study  of  Example 10.5.  In  this case,  using  the shorter study period did not reduce the amount of  discrimination between  the alternatives.

## 10.4 REPLACEMENT ASSUMPTION FOR UNEQUAL-LIVED ASSETS

Equipment investment decisions frequently involve the comparison  of  assets with unequal lives. In most businesses, a piece of  equipment will be replaced with a like one at the end of  its useful life, in order for the f i r m to continue operating. When this is the case, the cash flows of  the unequal-lived assets should be estimated into the future until the least common multiple of  their individual useful lives has been reached. The EUAS method can then be readily applied.

Example 10.7 A  company  can  purchase either of  two  alternative  machines,  A  and  B,  with  the following characteristics:

| Machine B   |
|-------------|

Here, P is the initial outlay, A is the annual net cash flow, and n is the useful life of  the machine. It is assumed that  when  either  machine  is  at  the  end  of  its  life,  a  similar  replacement  machine  will  be  purchased.  Which machine should be purchased, under a MARR of  lo%?

1

I

Machines A and B will first reach  a common multiple of  their individual useful lives at the end of  fifteen years. The cash flows for this fifteen-year period are displayed in Table 10-4. Note the replacements of  machine A by exact replicas at the end of  five and ten years; and of  machine B, at the end of  three, six, nine, and twelve years.  (Both  machines  are also  replaced  at  the end of  fifteen  years,  but  those costs  belong  to the  next  study period.)

Table 10-4

|   End of Year | Machine A   | Machine B   |
|---------------|-------------|-------------|
|             0 | -$I5 000    | -$9000      |
|             1 | 6000        | 3000        |
|             2 | 6000        | 3000        |
|             3 | 6000        | 3000 - 9000 |
|             4 | 6000        | 3000        |
|             5 | 6000-15000  | 3000        |
|             6 | 6000        | 3000 - 9000 |
|             7 | 6000        | 3000        |
|             8 | 6000        | 3000        |
|             9 | 6000        | 3000 - 9000 |
|            10 | 6000-15000  | 3000        |
|            11 | 6000        | 3000        |
|            12 | 6000        | 3000 - 9000 |
|            13 | 6000        | 3000        |
|            14 | 6000        | 3000        |
|            15 | 6000        | 3000        |

Proceeding as in Example 7.4, we compute:

<!-- formula-not-decoded -->

= -$619  for fifteen years

The conclusion is that machine B is unacceptable,  and that machine A should be purchased.

## Solved Problems

- 10.1 Mr. Jones bought a new car in September 1981 for $7800. He paid $2400 down, and financed the balance with  a loan  at 18%  nominal interest  to be repaid  in  35 monthly installments of $199.42  each.  It  is  understood  that  i f Mr.  Jones  fails  to  make  a  payment,  the  car  will  be repossessed by  the loan  company  and, though  Mr.  Jones will  owe  nothing,  he  will  lose all money already paid. He can also pay the outstanding balance of  the loan at any time. Twelve months after the transaction, Mr. Jones's  balance is  $3855. Thanks to a good deal, Mr. Jones has this amount and is going to pay off  the loan. At this point, Mr. Jones's brother offers him an  essentially  identical  car  (they  bought  the  same  model  the  same  day,  and  the  use  and maintenance of  both cars have been very similar) for $3500. Mrs. Jones would prefer to keep their  current  car "because we  have already spent  almost $4800 on it." What  is  the sensible decision to make?

This is a clear and very common instance of a sunk cost:  Mrs. Jones is wrong in her analysis. While it is true that they have invested a large amount of  money so far, it is also true that this money will not be recovered, no matter what decision is taken. The sole question is whether Mr. Jones should acquire a car for $3855 or acquire a car for $3500. Provided  the.two cars are physically equivalent,  the answer is obvious.

- 10.2 A machine can be sold now for $15 000; if  kept for another year, its salvage value will decline to $13  000. The operating expenses for this year are expected to be $30 000. A new machine is available for $50 000, with expected operating expenses of  $18 000 for the first year, increasing by  $1000  a  year  because  o f deterioration.  It  is  believed  that  after  5  years  new  technology would make replacement necessary; the new machine's salvage value at that time is estimated to be $20 000. The MARR is 20%. Should the new machine be acquired?

<!-- formula-not-decoded -->

whence CUV = $13 893.25.  Since the comparative  use  value of  the old  machine  is smaller  than  its net market value ($15 O O O ) ,   the machine should be replaced.

- 10.3 A contractor can  purchase  a  used  machine for  $1000.  The  market  value of  the machine is expected to decrease $70 the first year and $60 per year, the second and third years. Operating disbursement is estimated  at $8000 the first year and  is expected to increase by  $175 a  year thereafter.  An  alternative  is  to  buy  a  new  machine costing  $10 000.  It  is  believed  that  the salvage value of  this machine will decrease by 15% each year over a maximum service life of 20  years.  The operating expenses are estimated  at  $6050  the first  year  and are expected  to increase by $135 a year after that. If  the MARR is 1O0/0,  which machine should be bought, and when should that  machine be replaced?  (Assume that  the used machine is  unique, but  that new machines are always available.)

For the used machine:

```
EUACl(1) = ($1000 -$930) (AIP, 10%.  1) + (0.10) ($930) + $8000 = $8170.00 EUACl(2) = ($1000 -$870) (AIP, lo%,  2) + (0.10) ($870) + $8000 + $175(A/G, lo%,  2) = $8245.24 EUACl(3) = ($1000 -$810) (AIP, lo%, 3) + (0.10) ($810) + $8000 + $175(A/G, lo%, 3) = $8321.30 For the new machine: EUACz(1) = [$I0  000 -(0.85) ($10 O O O ) ]   (AIP, lo%, 1) + (0.10) (0.85) ($10 000) + $6050 = $8550.00 EUACz(2) = [$I0  000 -(0.85)2($10  000)] (AIP, lo%, 2) + (0.10) (0.85)2($10  000) + $6050 + $135(A/G, lo%, 2) = $8435.71 EUACz(3) = $8342.20 EUACz(4) = $8206.37 EUACz(5) = $8435.11
```

The used  machine should  be bought  and  kept for one year (its economic life). At that time,  the  new machine should be bought and kept for four years (its economic life).

- 10.4 A machine costs $10 000 and is expected to have scrap value $1500 whenever it is retired. The operating disbursements for the first year are expected to be $1500 and they will then increase $400  per  year,  as a  result  of  deterioration.  I f the MARR is  15%, determine the  machine's economic life.

For j = 1, 2 For j = 1, 2

<!-- formula-not-decoded -->

The evaluations, Table 10-5, give an economic life of 8 years.

Table 10-5

| Years of Service, j   | CR(I')   | AO')   | EUACG)   |
|-----------------------|----------|--------|----------|

- 10.5 A  plant  is  considering  buying  a  second-hand  machine  to  use  as  stand-by  equipment.  The machine costs $3000 and has an economic life of 10 years, at which  time its salvage value is $600; expected annual operating costs are $100. Without a stand-by machine, the plant would have to shut down an average of seven  days a year at a cost of $50 per day. If  the MARR is 10°/o, is it  expedient  to buy the stand-by machine?

<!-- formula-not-decoded -->

The stand-by machine should not be purchased.

- 10.6 XYZ Company  is  considering  replacing  a  machine.  The  new  improved  machine  will  cost $16000 installed; it will have an estimated service life of  8 years and $3000 salvage value. It is estimated  that  operating  expenses  will  average $1000 a  year.  The  present  machine  was purchased for $20 000 four years ago and is ,estimated to have 8 more years of  service life, at the  end  of which  its  salvage  value  will  be $2000. Operating  costs  are $1800 per  year.  If replaced  now,  it  can  presumably  be  sold  for $5000. Using  a MARR of 15%, determine whether to replace the existing machine.

Compare present-worth costs over the next 8 years.

<!-- formula-not-decoded -->

Do not replace the machine.

- 10.7 Consider the replacement situation  indicated  in  Table 10-6. I f   estimates beyond 8 years are unreliable  and if  the MARR is 15%, decide whether  it is expedient to replace  the current equipment.

The study period is limited by the current equipment and the forecast horizon to 8 years.

<!-- formula-not-decoded -->

Table 10-6

|                       | Salvage Value   | Salvage Value   | Original Cost   | Annual Cost   | Service Life   |
|-----------------------|-----------------|-----------------|-----------------|---------------|----------------|
|                       | Now             | End of Life     |                 |               |                |
| Current Equipment     | $8000           | $1000           | $17000          | $3600         | 8 more years   |
| Replacement Candidate |                 | 6000            | 19000           | 800           | 15 years       |

For the replacement candidate, the present-worth cost is given by

Annualizing over the 8-year period,

<!-- formula-not-decoded -->

Replace the current equipment.

- 10.8 To keep an existing machine going for a number of  years, an extensive (and expensive: $4000) overhaul is needed. Maintenance is expected to be $2000 annually for the next 2 years and to increase by $1000 per year after that. The machine has no present or future salvage value. An alternative  machine costs $8000  and, owing to its specialized  nature, it has no salvage value after it is installed. Maintenance expenses are expected to be $1000 the first year, increasing by $500 per year in subsequent  years. If  the MARR is  15%, determine the best course of  action.

For the defender, writing the first year's maintenance as $1000 + $1000,

<!-- formula-not-decoded -->

and for the challenger,

From the evaluations in  Table 10-7, we  see that  the economic lives are j'i' = 4 years and j Z = 7 years. It follows that  the best  course o f   action  is  to overhaul  the current equipment and  keep it  for four years. Then (provided an  analysis indicates that things remain as expected), buy the new equipment and keep it for seven years.

Table 10-7

| EUAC (j)   |       |
|------------|-------|
| 4460       | 6 154 |
| 4040       | 4 957 |
| 4032       | 4 465 |
| 4175       | 4 248 |
|            | 4 163 |
|            | 4 148 |
|            | 4 173 |

- 10.9 It  is  necessary  to pump twice as much  water  as can  be handled  by  the existing small  pump, which is now 5 years old. This pump can be sold now for $1200 or kept for 5 years, after which it  will  have zero salvage value.  Operating expenses are $3000 per year. If  the pump is kept, a similar  one must  be purchased  for $3500, with  operating costs of  $2500 per year; its salvage values after 5 and 10  years are the same as for  the original  pump.  A large  pump, equal in capacity to the two small  pumps, costs $6000, with operating expenses of  $4500 per year. New

i

machines have economic lives of  10 years, and zero salvage values at that date. Analyze the situation, i f   the MARR is 10.Y0.

There are 3 possible alternatives: (1) t o  replace the present pump by a new, large pump; (2) t o  buy a new small pump now and every fifth year hereafter; (3) t o  buy a  new small pump now, and after 5 years t o  sell  it and install a single large pump. We calculate the present-worth costs for a 10-year study period.

<!-- formula-not-decoded -->

Note, in  the calculations for plans 2 and 3, how certain costs are spread out over ten years and then are partially brought back into the study  period.

The conclusion is that plan 1 is best, with  plan 3 being slightly superior to plan 2.

- 10.10 A  company  decides  to automate  a  process  by  installing a  machine  that  costs $8000  and  is expected  to save $2500  per  year.  Discuss the wisdom  o f   this decision, if  the economic life of the machine is 10 years, at which time it  has a $2000 salvage value, and i f   the MARR is 15%.

The present worth of  the decision is (costs counted negative):

<!-- formula-not-decoded -->

that is, the company can expect net savings of $5041.38 (today's dollars) over the next 10 years.

## Supplementary Problems

- 10.11 Solve Problem 10.10 for an economic life of 3 years. Ans. PW = -$976.94 (the company should not automate)
- 10.12 Table 10-8 shows the expected annual operating costs and salvage values for a machine whose initial cost is $20 000. Find the economic life of  the machine,  if  the MARR is 20%. Ans. 6 years

Table 10-8

|   Year of Service | Salvage Value at End of Year   | Operating Cost for Year   |
|-------------------|--------------------------------|---------------------------|
|                 1 | $10 000                        | $ 2000                    |
|                 2 | 9000                           | 3000                      |
|                 3 | 8000                           | 4 000                     |
|                 4 | 7 000                          | 5000                      |
|                 5 | 6000                           | 6 000                     |
|                 6 | 5000                           | 7 000                     |
|                 7 | 4000                           | 8000                      |
|                 8 | 3000                           | 9000                      |
|                 9 | 2000                           | 10 000                    |
|                10 | 1000                           | 11000                     |

d

- 10.13 For a MARR of  15%, find the economic life of   the new  machine in  Problem 10.3. Ans. 15 years
- 10.14 Repeat Problem 10.7 for a forecast horizon o f   5 years. Ans. EUACmmnt(5) = $5838, EUAC,,l.,,nt(5) = $5843; therefore, keep the current equipment. (Note that  this  is  a  conservative criterion, since  it  tends  to  preserve  the existing situation when  the challenger's edge  consists in savings  in the distant  future, the  estimation o f   which must be unreliable.)
- 10.15 For the situation  described in  Problem  10.5,  determine the  number o f   down-days per  year  that would justify the acquisition o f   the stand-by machine. Ans. 12.01 (thus, 13)
- 10.16 A word-processor was bought two years ago for $22 000.  ~ t ' the time, the machine was expected to last six years and to have operating costs o f   $7200 the first year, increasing by  $300 per year thereafter. The salvage value at the end o f   the sixth  year is assumed to be zero. Another company is presently offering a competitive machine for $16 000; they will give $10 000 for the one in  use as trade-in value. Although the book value of   the old  machine is $14 167,  this offer o f   $10000 is thought  to be fair, since the technical obsolescence of   the current system would make it very difficult to get a better offer. For this reason, it is believed that the salvage value o f   the current machine will decrease by $2500 per year over the next four years. The new machine is expected to last four years and to have operating expenses o f   $6500 per year. After four years, its salvage value will be zero. I f   the MARR is 15%, should the machine be changed? If so, when?
- Ans. The old machine's  current market  value (salvage  value)  is  $10 000; its  economic  life is  found  as 4  more years, with EUACAa(4) = $11  700.59. The new machine also has an economic life o f   4 years, with EUAC,(4) = $12 104.32. Thus, the old machine should be kept for four more years.
- 10.17 Refer to Table 10-9. I f   the MARR is  15%, should the current machine be replaced? Ans. No (based on  a 10-year study period)
- 10.18 A  pump  costing  $18000  is  expected  to  have  operating  disbursements  o f $6500  the  first  year.  The machine's resale value is expected to decline by  15% a year, while its operating expenses are expected to increase by $500 a year. If   the MARR is 20°h,  determine the economic life and the corresponding annual equivalent cost. Ans. 8 years, EUAC(8) = $12 181.50
- 10.19 In  a replacement analysis, data for the challenger are as follows:
- 10.20 Is it expedient to replace the current machine o f   Table 10-11, i f   the MARR for this type o f   study is 15%? Ans. No: CUV = $1088 &gt; $1000

Table 10-9

|                  | Salvage Value   | Salvage Value   | Original Cost   | Annual Cost   | Service Life           |
|------------------|-----------------|-----------------|-----------------|---------------|------------------------|
|                  | Now             | End of Life     |                 |               |                        |
| Current Machine  | $14000          | $1000 5000      | $50 000         | $10000        | 10 more years 15 years |
| Improved Machine |                 |                 | 45000           | 3750          |                        |

Initial cost (installed):

$12 000

Maximum service life:

8 years

Operating expenses:

none, the first  three years; $2000  the fourth  and fifth  years; increasing by  $2500 per year after the fifth  year

Salvage value:

zero at all  times

The MARR is 10%. Tabulate the EUAC of  the challenger and infer its economic life. Ans. See Table 10-10.

Table 10-10

| 1 2 3 5 7 8   | S13 200 6914 4 825 4 390 4071 3 706 3843 4 162   |
|---------------|--------------------------------------------------|

Table 10-11

|               | Current Machine               | Challenger   |
|---------------|-------------------------------|--------------|
| Service Life  | 3 more years                  | 7 years      |
| Original Cost |                               | $5500        |
| Salvage Value | $1000 now, $200 after 3 years | after y ears |
| Annual Cost   | $1300                         | $600         |

- 10.21 Compute the CUV of   the new machine in  Problem 10.13,  i f   the old  machine is kept two  years and the new one is kept ten years. Am. CUV = $9448 (&lt;$lo 000).
- 10.22 The data  in  Table 10-12  pertain  to  the  average standard-size 1979-model automobile, purchased for $6263. Assuming that 1 2 O / 0  is a good estimate o f   the pertinent interest rate, determine the economic life of   such an automobile. Am. 10 years
- 10.23 A Cyear-old die-casting machine, o f   market value $3500, is 50%  too small for future production needs. A new machine with identical production capacity costs $5000 installed. Both machines are expected to have economic lives o f   6 years from this date. Salvage values at that date will be $1000 for the new, and $700 for the old, machine. Annual operating expenses for the new and old machines are expected to be $3500 and $4000,  respectively. A double-capacity machine is also available; its installed cost is $12000, with  a salvage value o f   $2000 at the end o f   its 6-year economic life. Operating costs are expected to be $6000 per year. If  the MARR is lo%, which machine should be purchased? Ans. EUACneW,,,,~~ = $9231, EUACI.,, = $8496; buy  the large machine.
- 10.24 A certain 5-year-old machine has a salvage value of $1200 i f   sold today, and o f   $400 i f   sold 5 years from now.  Its  operating expenses are $800  per  year.  A  new  improved machine is  available for $2400,  has expected operating expenses of   $500 per year, and has a salvage value o f   $1000 at the end o f   its 5-year economic life. There is also the possibility o f   overhauling the old machine at a cost o f   $600, which would increase the salvage value in 5 years by $200 and reduce the operating expenses by $200 per year. If  the MARR is lo%, which course of  action should be taken?

Table 10-12

|   Years of Service | Operating Cost   | Salvage Value   |
|--------------------|------------------|-----------------|
|                  1 | $2178            | $4503           |
|                  2 | 1880             | 3582            |
|                  3 | 2080             | 2881            |
|                  4 | 1554             | 2255            |
|                  5 | 2166             | 1723            |
|                  6 | 1923             | 1285            |
|                  7 | 2379             | 890             |
|                  8 | 1476             | 564             |
|                  9 | 1604             | 251             |
|                 10 | 1078             | 0               |

Ans. EUAC,la = $1051, EUAC,, = $969, EUACover~..l = $977; buy the new machine.

## 11.1 DEFINITIONS

Depreciation is a  way of  accounting for the cost  of  an asset when income is determined  for tax purposes.  The cost,  including  any  delivery  or installation  charges,  is  treated  as  a  prepayment  for future services; and depreciation consists in  amortizing this prepayment over the period of  use of  the asset.

The annual depreciation is the amount of  the asset's cost that is charged off  in  a given year; the total of the annual depreciations to date is the accumulated depreciation. The salvage value or scrap value of  an asset is the estimated proceeds that will be realized from its sale or disposition when it is retired.  Under federal tax law, the net  salvage  value is either zero or the salvage value minus the cost of  removing the asset from the premises, whichever is greater. The adjusted cost of  an asset is its original cost less its net salvage value.

The useful life, over which an asset is depreciated, may not be the same as its service life, physical life,  economic life,  market life,  etc. The U.S.  government  publishes guidelines for most equipment, showing the ranges of  useful lives allowed in tax computations.

## Depreciable And Nondepreciable Assets

The  current  tax  laws  permit  only  assets  with  a  useful  life  or  more  than  one  year  to  be depreciated.  Depreciation is allowed only for assets used in a  business, trade or profession, or held for the production of  income. Personal property, such as a family residence or automobile used for pleasure, is not depreciable; however, that portion of  an automobile or other property which is used in  business may be depreciable. Depreciation is not permitted on land (or on its upkeep), even when it  is  used  for  business  purposes  or  income  generation.  However,  buildings  and  equipment  which occupy that land are depreciable if  used in a business or to generate income. Inventories of  goods used in a business, other stock in trade, and short-term assets that will be consumed during a normal year's operation of  the business are not depreciable.

## Computation Methods

The four traditional methods of  computing  an asset's depreciation from its cost, useful life, and salvage value will be presented in Sections 11.2-11.5.  A  newer method is treated in Section  1 1 . 1 1 .

## 11.2 STRAIGHT-LINE METHOD

For an asset with useful life n years, the annual depreciation in  year j is

<!-- formula-not-decoded -->

a constant independent of j ; this corresponds to the constant annual depreciation rate  r, = 100%ln. The accumulated depreciation at the end of  year j is simply

<!-- formula-not-decoded -->

and the book value of  the asset at the end of  year j is defined as

## Depreciation and Taxes

In  particular, for  j = n, (11.3) gives

SB, = (original cost) -(adjusted cost) = net salvage value

Example 11.1 A new machine costs $160 000, has a useful life o f 10 years, and can be sold for $15 000 at the end of   its useful life. It is expected that $5000 will  be spent to dismantle and remove the machine at the end o f its useful life. Determine the straight-line depreciation schedule for this machine.

Here, the adjusted cost is $160 000 -  ($15 000  $5000) = $150  000, and the rate o f   depreciation is 10% per year. Applying (11.1), (11.2), and (11.3), we generate Table 11- 1 . At the end of   year 10, the sale o f   the asset for $15 000 will remove the $10 000 book value from the firm's accounting records.

Table 11-1

|   Year, j | Depreciation Charge (10%) for Year, SD   | Accumulated Depreciation, ASDj   | Book Value at End of Year, SBi   |
|-----------|------------------------------------------|----------------------------------|----------------------------------|
|         1 | $15 000                                  | $ 15000                          | $145 000                         |
|         2 | 15000                                    | 30000                            | 130000                           |
|         3 | 15000                                    | 45 000                           | 115000                           |
|         4 | 15000                                    | 60000                            | 100000                           |
|         5 | 15000                                    | 75 000                           | 85 000                           |
|         6 | 15000                                    | 90000                            | 70000                            |
|         7 | 15000                                    | 105000                           | 55000                            |
|         8 | 15000                                    | 120000                           | 40000                            |
|         9 | 15 000                                   | 135000                           | 25000                            |
|        10 | 15000                                    | 150000                           | 10000                            |

## 11.3 DECLINING-BALANCE METHOD

In  this method, the annual depreciation  in  year  j is computed  as a fixed fraction  of  the asset's book value at the end of  year  j -1:

<!-- formula-not-decoded -->

where rd is  the declining-balance  annual depreciation  rate, in  percent, and  DBo = original cost. The accumulated depreciation at the end of  year  j is

<!-- formula-not-decoded -->

and the book value at the end of  year j is

<!-- formula-not-decoded -->

Equations (11.4),  (11.5), and (11.6)  imply the recursion formula

<!-- formula-not-decoded -->

which may be solved to give the following  explicit  expressions (k = 1,2, .  . .  , n):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We see that the depreciation amount (and also the book value) decreases geometrically with time. Thus, the declining-balance  method  results in  a  larger share of  the depreciation being charged during the earlier years of  the asset's life. In contrast to the straight-line method, it is an accelerated depreciation method.

Also unlike the straight-line  method,  the declining-balance method does not automatically take account of  the net salvage value of  the asset. Thus, according to the  first equation (11.7), the book value steadily decreases through positive values, and could very  well become smaller than the net salvage value. Salvage value is included in the method by fiat: Federal tax law forbids the application of  the method past the point at which ADDk becomes greater than the adjusted cost of  the asset-which is precisely  the point  at which DBk becomes smaller than the net salvage value.

Example 11.2 Apply  the  double-declining-balance  method  (i.e., r d = 2rs = 20O0/0/n) to (a)  the  machine  of Example 11.1; (b) the machine of  Example 11.1, with the net salvage value changed to $30 000.

In  either case,  construct the depreciation  schedule by applying  (11.4), with r d = 20°h and DBo = $160 000, for as long as is permitted.

- ( a ) See  Table 11-2. Here,  the  accumulated  depreciation  never  reaches $150000, the  adjusted  cost  of the machine. The excess of  the final book value over the net salvage value,

<!-- formula-not-decoded -->

will presumably  be deducted from the firm's income as a capital loss, upon sale of  the machine.

Table 11-2

| Year, i              | Depreciation Charge (20%) for Year, DDj                                            | Accumulated Depreciation, ADDi                                                                 | Book Value at End of Year, DBi                                                            |
|----------------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| 1 2 3 4 5 6 7 8 9 10 | $32000 25 600 20 480 16 384 13 107.20 10 485.76 8 388.61 6710.88 5 368.71 4 294.96 | $ 32000 57 600 78 080 94 464 107 571.20 118 056.96 126 445.57 133 156.45 138 525.16 142 820.12 | $128000 102 400 81 920 65 536 52 428.80 41 943.04 33 554.43 26 843.55 21 474.84 17 179.87 |

- (b) See Table 11-3. Entries for years 1 through 7 are computed in normal fashion. The depreciation charge for the 8th year becomes $3554.43; any larger amount would cause the accumulated depreciation to  exceed the legal maximum of

<!-- formula-not-decoded -->

No depreciation can be taken in years 9 and 10. A total of $30 000 in book value, equal to the machine's net salvage value, remains undepreciated. The sale of  the machine for its salvage value will remove this $30 000 from the firm's accounting records.

Table 11-3

| Year              | Depreciation Charge for Year   | Accumulated Depreciation   | Book Value at End of Year   |
|-------------------|--------------------------------|----------------------------|-----------------------------|
| 1 2 3 4 5 6 7 8 9 | $ 32000                        | $ 32000                    | $128000                     |
|                   | 25 600                         | 57600                      | 102400                      |
|                   | 20 480                         | 78080                      | 81920                       |
|                   | 16384                          | 94464                      | 65 536                      |
|                   | 13107.20                       | 107571.20                  | 52428.80                    |
|                   | 10 485.76                      | 118056.96                  | 41943.04                    |
|                   | 8388.61                        | 126445.57                  | 33 554.43                   |
|                   | 3554.43                        | 130000                     | 30000                       |
|                   | 0                              | 130000                     | 30000                       |
| 10                | 0                              | 130000                     | 30000                       |

## 11.4 SUM-0FYEARS'-DIGITS METHOD

The sum of  years, SY, for an asset  with useful life  n  years is

<!-- formula-not-decoded -->

In  the sum-of-years' -digits  method, the annual depreciation  in  year j is given  by

<!-- formula-not-decoded -->

whence the accumulated depreciation  at the end of  year  j is given by

<!-- formula-not-decoded -->

The book value at the end of  year  j is defined in  the usual way:

<!-- formula-not-decoded -->

Because ASYD, = adjusted cost, SYB. = net salvage value, as in  the straight-line  method.

Table 11-4

|   Year, I | Depreciation Charge for Year, SYDj   | Accumulated Depreciation, ASYDj   | Book Value at End of Year, SYBj   |
|-----------|--------------------------------------|-----------------------------------|-----------------------------------|
|         1 | $27272.73                            | $ 27 272,73                       | $132727.27                        |
|         2 | 24545.45                             | 51818.18                          | 108181.82                         |
|         3 | 21818.18                             | 73 636.36                         | 86363.64                          |
|         4 | 19090.91                             | 92727.27                          | 67272.73                          |
|         5 | 16363.64                             | 109090.91                         | 50909.09                          |
|         6 | 13 636.36                            | 122727.27                         | 37272.73                          |
|         7 | 10909.09                             | 133 636.36                        | 26363.64                          |
|         8 | 8181.82                              | 141818.18                         | 18181.82                          |
|         9 | 5454.55                              | 147 272.73                        | 12727.27                          |
|        10 | 2727.27                              | 150000.00                         | 10000.00                          |

According to (11.8),  a different  fraction  is applied each year to the adjusted  cost of the asset  to obtain the annual depreciation. The denominator of  this fraction is the total of  the digits representing the years of  the estimated useful life of  the asset; the numerator changes each year, so as to represent the number of  years of  useful  asset  life  remaining at the start  of  that year.  Currently,  the tax laws prohibit  the sum-of-years' -digits method  from  being  used  on  any  property  for  which  the  doubledeclining-balance  method is prohibited.

Example 11.3 Apply the sum-of-years' -digits method to the machine o f   Example 11.1.

By (11.8), SY = (10)(11)/2  =  55, and the adjusted cost o f   the machine is $150 000. Repeated application of (11.9) generates Table 11-4.

## 11.5 SINKING-FUND METHOD

This method depreciates an asset as if  the f i r m were to make a series of  equal annual deposits (a sinking fund)  whose value at the end of  the asset's useful life  just  equaled the cost of  replacing the asset.  Writing

A' = sinking-fund deposit

C=  (purchase price of  replacement  asset) -(net salvage value of  current asset)

n = useful life of  current asset i = annual interest  rate

we have: A' = C (AIF, i%, n). The amount in the sinking fund at the end of  year j ( j = 1,2, .  .  .  , n) is identified with  the accumulated depreciation  to date; thus,

<!-- formula-not-decoded -->

and the depreciation amount in year j is

<!-- formula-not-decoded -->

As usual, the book value is defined as

<!-- formula-not-decoded -->

Table 11-5

|   Year, i | Depreciation Charge for Year, SFDj   | Accumulated Depreciation, ASFDj   | Book Value at End of Year, SFBj   |
|-----------|--------------------------------------|-----------------------------------|-----------------------------------|
|         1 | $ 7387.81                            | $ 7387.81                         | $152612.19                        |
|         2 | 8495.98                              | 15883.79                          | 144116.21                         |
|         3 | 9770.38                              | 25654.17                          | 134345.83                         |
|         4 | 11235.93                             | 36890.10                          | 123109.90                         |
|         5 | 12921.32                             | 49811.43                          | 110188.57                         |
|         6 | 14859.52                             | 64670.95                          | 95 329.05                         |
|         7 | 17088.45                             | 81759.40                          | 78 240.60                         |
|         8 | 19651.72                             | 101411.12                         | 58588.88                          |
|         9 | 22599.48                             | 124010.60                         | 35 989.40                         |
|        10 | 25989.40                             | 150000.00                         | 10000.00                          |

It  is  seen  from  (11.13) that  the  annual  depreciation  amount increases geometrically  with time-just  the opposite of  the declining-balance  method. As a  matter  of  tax  law,  the sinking-fund method may be used only when the replacement asset will have the same original cost as the current asset,  in  which  case C = adjusted  cost  of current  asset.  (Otherwise,  the  firm  could  take  a  total depreciation allowance in excess of  the current asset's adjusted cost, and this is not allowed.)

Example 11.4 Apply the sinking-fund method to the machine of  Example 11 . 1 , given i = 15%.

By  repeated application o f (11.13), starting with

<!-- formula-not-decoded -->

Table 11-5 is generated.

## 11.6 GROUP AND COMPOSITE DEPRECIATION

The methods discussed in Sections 11.2-11.5 are all unit depreciation methods in  that they apply t o   a  single  item,  asset,  or  unit.  When  there  are  many  like  items,  a group  depreciation becomes convenient, whereby a single annual depreciation figure is computed for the ensemble, using the sum of  the items'  original costs and the sum of  their salvage values. The group's  useful life is the average of  the lives of  all the items. Any of  the unit depreciation  methods can be used to compute the group depreciation.

Example 11.5 The  ABC Company purchased five cutters with  useful  lives of 5, 6, 7, 8, and 10 years;  the cutters cost $10000,  $12000,  $13 000,  $14000, and $16000, respectively. The salvage value o f each  cutter  is estimated to be $500. Compute the annual group depreciation charge, using the straight-line method.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

When  a  mixed  collection  of  assets  is  subdivided  into groups  according  to useful  life,  one can perform  a composite  depreciation. First,  an  annual  depreciation  charge  is  calculated  for  each  life group by use of  a  group depreciation  method. The sum of  these charges then  gives  the composite annual depreciation. A composite life, n, can now be defined as the total of  all adjusted costs, divided by the composite depreciation  amount. The corresponding composite depreciation  rate is defined as 100% In.

Example 11.6 Rework Example 11.5 by  composite depreciation.

Applying the straight-line method to each life group, which in  this case consists o f   a single item, we obtain:

Then,

<!-- formula-not-decoded -->

Comparing with  Example 11.5, we see that, under composite depreciation, a little more is charged off  each year for a slightly smaller number o f   years.

The composite depreciation  rate  (or  useful  life)  is  restricted  by  guidelines  issued  by  the  U.S. Treasury  Department.  Variations  from  these  guidelines  must  be  individually  approved  by  the Internal  Revenue Service.

## 11.7 ADDITIONAL FIRST-YEAR DEPRECIATION; INVESTMENT TAX CREDIT

The U.S. government from time to time seeks to encourage new capital investments by business, to stimulate the economy. Two incentives have been  used, either of  which may be enacted into law when  the federal government feels stimuli  are needed,  and withdrawn when it feels stimuli are not needed.

The additional first-year  depreciation provision  allows  an  additional  percentage  depreciation deduction during the year in which the asset was purchased. The percentage is based on the original cost  of  the asset,  and is in  addition  to any  regular  depreciation.  The investment tax credit provision allows a  business to reduce its annual income tax by some stated percentage of  the original cost  of any assets purchased during that year.

Example 11.7 The  SSG  Company  spent  $1000000  for  new  equipment  on  January 1 of  this  year.  The equipment  has a  useful  life  o f   10  years,  zero salvage value,  and  is  depreciated by  the straight-line method. Additional first-year depreciation o f   2 0 ° / 0   and an investment tax credit of   7% apply. Compute the total first-year depreciation, depreciation for other years, and the first-year investment tax credit for the SSG Company.

Fig. 11-1

<!-- image -->

<!-- formula-not-decoded -->

This year, the depreciation charge will be

<!-- formula-not-decoded -->

Since 3 SD is charged off  in  year 1 , the annual depreciation will be SD in  years 2 through 8, and zero in  years 9 and 10. In  addition, the SSG Company can reduce this year's tax bill by

## 11.8 COMPARISON OF DEPRECIATION METHODS

Figures 11-1 and 11-2 are plots of  the annual depreciation charges and book values from Tables 11-1, 11-2, 11-4, and 11-5. Figure 11-1 makes manifest what we have said about the four traditional depreciation  schemes:  the sum-of-years' -digits  method  and  the declining-balance  methods  are accelerated (heaviest  depreciation  in  earlier  years);  the sinking-fund  method  is decelerated (heaviest depreciation  in  later  years);  and  the straight-line  method  is  neither  accelerated  nor  decelerated. Notice,  in  Fig.  11-2,  that  the  book  values  generated  by  the straight-line  method  are intermediate between  those for the accelerated  and the decelerated  methods. This holds true in general.

Fig. 11-2

<!-- image -->

## 11.9 BUSINESS NET INCOME AND TAXES

In  the U.S.,  most corporations are subject to a two-step income tax, characterized by a base tax rate and a surtax rate. The base tax rate, r , is currently  22% of  net taxable income, I ,  where

I = (gross receipts and sales) -@ad debts) -

<!-- formula-not-decoded -->

The surtax rate, s,, is presently 26%; it applies only  to income in  excess of  $25 000. Total corporate income tax is thus given by

<!-- formula-not-decoded -->

where it is assumed that I 2 $25 000. For most corporations, I 9 $25 000, so that

<!-- formula-not-decoded -->

where tr = r, + s, = 48%.

Unincorporated  businesses are generally taxed at the individual tax rate(s) of  the owner(s).

Example 11.8 The KJL Corporation received $10 000 000 from the sales of   their products during the current year.  A  total of  $1000  of  these sales was  never actually collected and  was  accounted for as  bad  debts. The company spent $3 000 000 in  the production and warehousing o f   their products during the current year. A total of   $1 000 000 was spent for wages and salaries, $500 000 was paid out in interest on long-term loans, $700 000 was spent  for  rental  of space  and  equipment,  and  $600000  depreciation  was  charged  off.  Compute  the KJL Corporation's  income tax bill for the current year, i f   the base tax rate is 22%  and the surtax rate is 26%.

From (11.15):

| Gross Receipts and Sales   |
|----------------------------|
| Less: Bad Debts            |
| Gross Income               |
| Period Costs:              |
| Cost of Goods Sold         |
| Wages and Salaries         |
| Interest                   |
| Rent                       |
| Less: Total Period Costs   |
| Net Income                 |
| Less: Depreciation         |
| Net Taxable Income         |

Capital gains  (losses)  occur  when  an  asset  is  sold  for  more  (less)  than  its  book  value.  Under current  U.S.  tax  laws,  if an  asset  has  been  held  more  than  six  months,  it  is  a  long-term  asset; otherwise, it is a short-term  asset. Long-term capital gains and losses are aggregated separately from short-term capital gains and losses. If  the long-term aggregate is positive (a capital gain), it is taxed at only 30%  (not at  tr = 48%). If  the long-term  aggregate is negative (a  capital loss),  this loss  may  be carried forward and spread arbitrarily over the next five years, as an offset to any capital gains during those years. If  the short-term aggregate is positive (a capital gain), it is taxed as regular income, at tr; if it  is negative (a  capital loss), it is treated like a long-term capital loss.

Example 11.9 Assume that in  the current year the KJL Corporation sells a machine, which  it  has  used  for several  years,  for  $600000.  The  machine  originally  cost  $500000  and  has  been  depreciated  under  the double-declining-balance method;  the  current  book  value  is  $300 000.  The  corporation also  had  short-term capital losses o f   $50 000 and short-term capital gains o f   $20 000. Compute the KJL Corporation's  income tax bill, using the other information in Example 11.8.

Sale o f   the machine results in  a long-term capital  gain of

plus ordinary income i n   the amount

In  addition, there is an aggregate short-term capital loss of $30 000. KJL will therefore have to pay taxes of

<!-- formula-not-decoded -->

+ + $2 135 020

but may claim a credit of $30 000 against future capital gains.

## 11.10 COMPARATIVE EFFECTS OF DEPRECIATION METHODS ON INCOME TAXES

Depreciation  is  deducted  as  an  expense  of doing  business.  Thus,  by  lowering  net  income, depreciation  lowers income  taxes.  Specifically,  i f   the normal  tax rate is t,, then  the depreciation tax shield in  year j, or amount of  taxes saved in  that year because depreciation is taken, is

<!-- formula-not-decoded -->

where Dj is the depreciation charge for that year.

Over the life of  an asset, the total amount of  depreciation  tax shield will  be the same under the straight-line, sum-of-years' -digits, and sinking-fund methods (since each of  these methods charges off the entire adjusted cost of the asset). The declining-balance  method will often yield a slightly smaller depreciation  tax shield over the life of  the asset, which, however, will  be more or less compensated for by the capital loss suffered when the asset is sold at a salvage value below its book value. Thus, all four  methods  will  give  approximately  the  same total tax  shield  over  the  useful  life  of the  asset. However, because of  the time value of  money, accelerated depreciation  methods (declining-balance and sum-of-years'-digits) will  yield a larger present-worth  net income after taxes. This is because the accelerated methods provide a larger tax shield in  the earlier years of  the asset's life; and the earlier the savings, the less they are discounted in  calculating the present worth.

Example 11.10 Assume that the tax rate is 52% and the (before-tax)  net income is $100 000 per year, before depreciation. Compare the effects of  the four depreciation methods from ( a ) Example 11.1, (b) Example 11.2(a), (c) Example 11.3, (d) Example 11.4. Assume MARR = 15%.

- ( a ) annual taxes = (0.52)($100  000 -$15 000) = $44 200 total taxes for 10 years = $442 000 present worth of 10 years' taxes = $44 200(P/A,  15%,  10) = $221 831.87
- ( b ) The tax shield from the capital loss (at maximum rate) is $7179.87  (0.30) = $2153.96.

Table 11-6

| Year   | Net Taxable Income, 1   | Net Taxable Income, 1   | Taxes, 0.521   | Present Worth o f Taxes   |
|--------|-------------------------|-------------------------|----------------|---------------------------|
|        | $100000 -               | $32000 = $68000.00      | $35 360.00     | $30747.83                 |
|        | 100 000 -               | 25 600 = 74 400.00      | 38688.00       | 29 253.69                 |
|        | 100 000 -               | 20 480 = 79 520.00      | 41 350.40      | 27 188.56                 |
|        | 100000 -                | 16 384 = 83616.00       | 43480.32       | 24 860.01                 |
|        | 100000 -                | 13 107.20 = 86 892.80   | 45 184.26      | 22464.56                  |
|        | 100 000 -               | 10 485.76 = 89 514.24   | 46 547.41      | 20 123.73                 |
|        | 100 000 -               | 8388.61 = 91611.39      | 47 637.92      | 17 908.86                 |
|        | 100 000 -               | 6710.88 = 93 289.12     | 48 510.34      | 15 858.12                 |
|        | 100000 -                | 5368.71 = 94 631.29     | 49 208.27      | 13988.06                  |
|        | 100000 -                | 4294.96 = 95705.04      | 49766.62       | 12301.55                  |
|        |                         | TOTALS                  | $445735.54     | $214694.97                |

Then, from Table 11-6, adjusted total taxes for 10 years = $445 735.54-  $2153.96 = $443 581.58

present worth of   10 years' taxes = $214 694.97

adjusted present worth o f   10 years' taxes = $214 694.97 -$2153.96(PIF, 15%,  10) = $214 162.54

- (c) The 10 years' taxes and their present worth are given by the totals in  Table 11-7.
- (d) The 10 years' taxes and their present worth are given  by  the totals in  Table 11-8.

Table 11-7

| Year   | Net Taxable Income,1            | Taxes, 0.521   | Present Worth of Taxes   |
|--------|---------------------------------|----------------|--------------------------|
| 1      | $100000 - $27272.73 = $72727.27 | $ 37818.18     | $ 32885.37               |
| 2      | 100000 - 24545.45 = 75454.55    | 39236.37       | 29668.33                 |
| 3      | 100000 - 21818.18 = 78181.82    | 40654.55       | 26731.02                 |
| 4      | 100000- 19090.91 = 80909.09     | 42072.73       | 24055.31                 |
| 5      | 100000 - 16363.64 = 83636.36    | 43490.91       | 21622.67                 |
| 6      | 100 000 - 13636.36 = 86363.64   | 44909.09       | 19415.44                 |
| 7      | 100000 - 10 909.09 = 89090.91   | 46327.27       | 17416.14                 |
| 8      | 100000 - 8181.82 = 91818.18     | 47745.45       | 15608.07                 |
| 9      | 100000 - 5454.55 = 94545.45     | 49163.63       | 13975.37                 |
| 10     | 100000 - 2727.27 = 97272.73     | 50 581.82      | 12503.05                 |
| TOTALS | TOTALS                          | $442000.00     | $213880.77               |

Table 11-8

| Year   | Net Taxable Income,1   | Taxes, 0.521   | Worth of Taxes   |
|--------|------------------------|----------------|------------------|

Comparing the above results, we see that the total taxes for 10 years are $442  000 under each depreciation method (with a deviation of  $1581.58 for the double-declining-balance method). However, on a present-worth basis we have:

## Method

Present-  Worth T a r Advantage (+) or Disadvantage (-) Relative to Straight-Line Method

Double-Declining-Balance Sum-of-Years 1 -Digits Sinking-Fund

## 11.11 THE ACCELERATED COST RECOVERY SYSTEM

The Accelerated Cost Recovery System (ACRS) is a depreciation  method recently  instituted by the  Internal  Revenue  Service.  It  is  mandatory  for  most  tangible  assets  placed  in  service  after December 31, 1980. Its main features are that salvage value is not relevant and that the useful life of the asset is limited  to 3, 5, 10, or 15 years. The IRS publishes depreciation scales for each class life. Thus, the percentages for three-year property placed in service during 1982 are 25% for the first year, 38% for the second year, and 37% for the third year. This class life includes assets with a useful life of  4 years or less, such  as automobiles, small  trucks,  and some manufacturing tools.  Items used  in research and experimentation  are also included  in  this category.

Five-year property includes office furniture, some storage facilities, and, in  general,  all  property that  is  not  three-,  ten-,  or fifteen-year.  The  percentages  are  15%  for  the  first  year;  22%  for  the second year; and 21% for the third, fourth, and fifth year.

Ten-year property  includes  assets with  a  useful  life of  less than 12.5  years.  The percentages are 8% for the first  year,  140h  for the second year, 12%  for the third  year,  10% for each of  years four through six, and 9% for each of  years seven  through ten.

Assets with a  useful life of  more than 12.5 years are designated as fifteen-year property. There is one rate structure for low-income housing and another for all other fifteen-year  property.  Percentages for the fifteen-year asset also depend on the month the property was placed in service; e.g.,  for an asset (not low-income housing) placed in service in  April, the percentages are:

Example 11.1  1 Apply the ACRS to the asset of  Example 11.1.

<!-- image -->

The calculations for this ten-year asset are given in  Table 11-9.

Table 11-9

|   Year | Depreciation Rate for Year   | Depreciation Charge for Year   | Accumulated Depreciation   | Book.Value at End of Year   |
|--------|------------------------------|--------------------------------|----------------------------|-----------------------------|
|      1 | 8%                           | $12800                         | $ 12800                    | $147200                     |
|      2 | 14                           | 22400                          | 35 200                     | 124800                      |
|      3 | 12                           | 19200                          | 54400                      | 105 600                     |
|      4 | 10                           | 16000                          | 70400                      | 89 600                      |
|      5 | 10                           | 16000                          | 86400                      | 73 600                      |
|      6 | 10                           | 16000                          | 102400                     | 57 600                      |
|      7 | 9                            | 14400                          | 116800                     | 43 200                      |
|      8 | 9                            | 14400                          | 131200                     | 28800                       |
|      9 | 9                            | 14400                          | 145600                     | 14400                       |
|     10 | 9                            | 14400                          | 160000                     | 0                           |

+57669.33 +57669.33

+57951.18 +87951.18

55738.36

Example 11.12 Assume again, as in  Example 11 . 1 0 , and  tax rate o f 52% and  an  annual income o f $100  0 0 0 before  depreciation  and  taxes.  Compare  the  effect o f the  ACRS  (using  Table 11-9) with  those  o f the four traditional methods, as found in  Example 11-1 0 .

Table 11-10

| Year                  | Net TaxableIncome, I                                                                                                                                                                                                                         | Taxes, 0.521                                                 | Present Worth of Taxes ( i = 15%)                                                                 |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| 1 2 3 4 5 6 7 8 9 1 0 | $100000 - $12800 = $87200 100000 - 22400 = 77600 100000 - 1 9200 = 80800 100000 - 1 6000 = 84000 100000 - 16000 = 84000 100000 - 1 6000 = 84000 100000 - 1 4400 = 85600 100000 - 14400 = 85600 100000 - 14400 = 85600 100000 - 14400 = 85600 | $45344 40352 42016 43680 43680 43680 44512 44512 44512 44512 | $39429 .57 30511.91 27626.20 24974.18 2 1716.68 1 8884.07 1 6733.71 1 4551 .05 12653 .09 11002.09 |
|                       | TOTALS                                                                                                                                                                                                                                       | $436800                                                      | $2180 82 .55                                                                                      |

See Table 11-1 0 . The comparison made in  Example 1 1 . 1 0 may now be extended as follows:

| Method                   | Present-Worth Tax Advantage (+) or Disadvantage (-) Relative to Straight-Line Method   |
|--------------------------|----------------------------------------------------------------------------------------|
| Double-Declining-Balance |                                                                                        |
| Sum-of-Years 1 -Digits   |                                                                                        |
| Sinking-Fund             |                                                                                        |
| ACRS                     |                                                                                        |

It  is  seen  that,  in  this  case,  the  ACRS is  better  than  straight-line depreciation  but  not  as  good  as  the  two traditional accelerated methods. However, had the useful life o f   the asset been 12 years, the ACRS would have been best (the asset would still be ten-year property, but the traditional methods would have to be applied over the whole 12 years).

## 11.12 CHOICE OF  DEPRECIA'TION METHOD

As  indicated,  a  taxpayer  would  have  to  present  excellent  arguments  (based on  facts,  not opinions) to be allowed  to use a  method other than  ACRS for tangible  assets. For intangible assets (franchises,  designs,  drawings,  copyrights, patterns,  subscription lists, customer  lists,  etc.), the traditional  methods can  still  be applied,  singly  or in  combination,  provided  the  useful  life  can  be projected  with reasonable accuracy.

As can be seen from Fig. 11-2, the use of  the double-declining-balance during the early years, combined with  a switch  to the sum-of-years'-digits in  later years, may provide the greatest  possible tax shield, for this combination gives the largest  possible accumulated depreciation  charge (smallest possible  book  value)  over  the  life  of the  asset.  However,  this  combination  may  result  in an accumulated depreciation at the end of  the useful life of the asset which exceeds the asset's adjusted cost- a violation  of tax  regulations.  Moreover,  the  current  tax  laws  specifically  prohibit  certain switches in  depreciation  method without the prior approval of  the Internal Revenue Service.

## 11.13  DEPRECIATION AND CASH now

Depreciation, as an accounting charge against income, is not itself  a cash flow. However, it does influence  the amount of  income tax paid, which is a (negative) cash flow. For year j ,  let us write:

BTCFj 5 before-tax net cash flow

ATCFj = after-tax net cash flow

4 = net taxable income

ATIj after-tax net income

Ti = income tax

Dj = depreciation charge

Then, ATCFj = BTCFj -  ? ; . . But, by (11.15),

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

that is to say, the after-tax cash flow for the year is the sum of  the after-tax net income for the year and the depreciation charge for the year.

## 1 1 . 1 4 BEFORE AND AFTER-TAX ECONOMIC ANALYSES

Economic analyses should  generally  be  made  on  an  after-tax  basis,  unless  it  is  clear  that  tax considerations are irrelevant. We have seen  that depreciation can cause the before-tax and after-tax pictures to differ.  Deduction of  interest paid on borrowed money will have a similar effect.  Perhaps most significant is the fact that businesses are judged  (by analysts and investors) on the basis of  their after-tax  performance.

Example 11.13 The ABC Company is  planning to buy  a  new  pump.  The pump costs $50000, and  has  a 10-year life and zero salvage value. The pump will increase the company's net income before taxes by $12 000 in each of   the 10 years. The company's tax rate is 51%. What is the ROR on the pump?

We make three different analyses, which give three different results.

BeforeTax

<!-- formula-not-decoded -->

AfterTax, No Depreciation

With Dj = 0, (1  1.19) gives ATCFj = (0.49)($12  000) = $5880; thus,

<!-- formula-not-decoded -->

AfterTax, Straight-Line Depreciation

With D, = $50 000/10 = $5000, (11.19) gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Example 11.14 The ABC Company (Example 11.13) can  purchase an  alternative "Superpump" that  costs $100 000 and generates an annual increase in  the company's net income before taxes o f $23 852. This pump also has a 10-year life and zero salvage value; however, a special provision in the tax laws permits  depreciation o f   this pump over a 5-year period. Which pump should the company buy?

For the Superpump, we make two analyses:

Consequently, and so

Before-Tax

<!-- formula-not-decoded -->

After-  Tax, Straight-Line Depreciation

Forj= 1,2, ..., 5:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

while for j = 6,7, .  .  . , l o :

<!-- formula-not-decoded -->

which yields i * = 12.8%.

Comparing the above results with  those o f   Example 11.3,  we  conclude that  the Superpump is  not  to be preferred on a before-tax basis, but is definitely to be preferred on an after-tax basis. In such cases, the after-tax picture is always the correct one.

## Solved Problems

- 11.1 A company's tax rate is 52%. To improve labor relations, the company has decided  to donate $1  000 000  to its labor  union  to build  a  sports arena  for  the  use  of  union  members  and  the general public. (a) If  the gift  is ruled  tax deductible,  what is the actual cost  to the company? (b) If  the gift  is ruled  nondeductible, what is the actual cost to the company,  and how does it account for the gift? ( c ) If  the labor union is a  tax-exempt corporation, to what extent is the general public (through  the government) subsidizing the arena?
- (a) tax savings = (0.52)($1000  000) = $520 000 actual cost to the company = $480 000
- (b) $1 000 000; nondeductible expense.
- ( c ) If  the  donation  is  ruled  tax  deductible,  the  general  public  would  be  footing  the  company's tax savings, $520 000. (If  the labor union were not tax-exempt, it would have to pay taxes on the gift, in which case the public's subsidy would amount to $520 000 minus the union's taxes.)
- 1 1 . 2 A computer system can be purchased for $18 000. The operating costs will be $10 000 per year, and the useful life is expected to be 5 years, with $5000 salvage value at that time. The present annual sales volume should  increase by $16000 as a  result of  acquiring the computer system. The company's  tax rate is  50%.  (a) Depreciate the  asset  by  the straight-line  method.  (b) Compute annual taxes, annual cash flows after taxes, and after-tax ROR for the investment.
- (a) SD = ($18  000 -$5000)/5 = $2600; see Table 11-11.

Table 11-11

|   Year | Depreciation Charge for Year   | Accumulated Depreciation   | Book Value at End of Year   |
|--------|--------------------------------|----------------------------|-----------------------------|
|      1 | $2600                          | $2600                      | $15400                      |
|      2 | 2600                           | 5200                       | 12800                       |
|      3 | 2600                           | 7800                       | 10200                       |
|      4 | 2600                           | 10400                      | 7600                        |
|      5 | 2600                           | 13000                      | 5000                        |

<!-- formula-not-decoded -->

- (b) The annual net cash flow before taxes is $16 000 -$10 000 = $6000; see Table 11-12.

Table 11-12

|                    | Year 1   | Year 2   | Year 3   | Year 4   | Year 5   |
|--------------------|----------|----------|----------|----------|----------|
| BTCF               | $6000    | $6000    | $6000    | $6000    | $6000    |
| Depreciation       | 2600     | 2600     | 2600     | 2600     | 2600     |
| Net Taxable Income | 3400     | 3400     | 3400     | 3400     | 3400     |
| Tax (@ 50%)        | 1700     | 1700     | 1700     | 1700     | 1700     |
| ATCF               | 4300     | 4300     | 4300     | 4300     | 4300     |

The after-tax ROR may be found by equating the after-tax PW to zero (see Chapter 7): 0 = -$I8  000 + $4300(P/A, i*%, 5) + $5000(P/F, i*%, 5)

<!-- formula-not-decoded -->

- 11.3 Rework Problem 11.2 if  the IRS rules that the equipment's tax life  is eight years, with  $2000 salvage value at that date.
- (a)  SD = ($18 000 -$2000)/8 = $2000; see Table 11-13.

Table 11-13

|   Year | Depreciation Charge for Year   | Accumulated Depreciation   | Book Value at End of Year   |
|--------|--------------------------------|----------------------------|-----------------------------|
|      1 | $2000                          | $ 2000                     | $16000                      |
|      2 | 2000                           | 4000                       | 14000                       |
|      3 | 2000                           | 6000                       | 12000                       |
|      4 | 2000                           | 8000                       | 10000                       |
|      5 | 2000                           | 10 000                     | 8000                        |

The useful life, or depreciation period, remains 5 years. At that time the computer system would presumably be sold- for $3000 less than its book value. Thus the company would take a long-term capital loss o f   $3000 and carry it  forward to offset long-term capital gains over the next five years.

- (b) See Table 11-14.

Table 11-14

|                    | Year 1   | Year 2   | Year 3   | Year 4   | Year5   |
|--------------------|----------|----------|----------|----------|---------|
| BTCF               |          |          |          |          |         |
| Depreciation       |          |          |          |          |         |
| Net Taxable Income |          |          |          |          |         |
| Tax (@ 50%)        |          |          |          |          |         |
| ATCF               |          |          |          |          |         |

Assuming that the company takes its tax credit [see (a)] in  year 6, it will save (0.30)($3000) = $900 in long-term capital gains taxes in  that year. Hence, the after-tax ROR is given by

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 11.4 Rework Problem 11.2 using the double-declining-balance depreciation  method.
- ( a ) With rd = 2rs =-200%/5 = 40%, we generate Table 11-15.

Table 11-15

|   Year | Depreciation Charge for Year   | Accumulated Depreciation   | Book Value at End of Year   |
|--------|--------------------------------|----------------------------|-----------------------------|
|      1 | $7200                          | $ 7 200                    | $10 800                     |
|      2 | 4320                           | 11 520                     | 6 480                       |
|      3 | 1480                           | 13000                      | 5000                        |
|      4 | 0                              | 13000                      | 5000                        |
|      5 | 0                              | 13000                      | 5000                        |

Observe that  the  third-year values  had  to  be  adjusted  so  that  the accumulated depreciation would not exceed the maximum set by  the IRS (the adjusted cost). No depreciation can be taken in years 4 and 5, and the book value of $5000 remains undepreciated.

- (b) See Table 11-16.

|                    | Year 1   | Year 2   | Year 3   | Year 4   | Year 5   |
|--------------------|----------|----------|----------|----------|----------|
| BTCF               | $6000    | $6000    | $6000    | $6000    | $6000    |
| Depreciation       | 7200     | 4320 -   | 1480 -   | 0 -      | 0 -      |
| Net Taxable Income | - 1200   | 1680     | 4520     | 6000     | 6000     |
| Tax (@ 50%)        | - 600    | 840      | 2260     | 3000     | 3000     |
| ATCF               | 6600     | 5160     | 3740     | 3000     | 3000     |

For the after-tax ROR:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 11.5 Rework Problem 11.2 using the sum-of-years'-digits  method of  depreciation.

<!-- formula-not-decoded -->

Table 11-16

-

and we have:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

1 1 . 6 Rework Problem 11.2(a) using the  sinking-fund method of depreciation and a before-tax MARR of 12%.

From (11.13), with  C = adjusted cost = $13 000,

<!-- formula-not-decoded -->

and we obtain Table 11-19.

Table 11-17

|   Year | Depreciation Charge for Year   | Accumulated Depreciation   | Book Value at End of Year   |
|--------|--------------------------------|----------------------------|-----------------------------|
|      1 | (&)($13000) = $4333.33         | $ 4333.33                  | $13666.67                   |
|      2 | (&)( 13000) = 3466.67          | 7800.00                    | 10200.00                    |
|      3 | (&)( 13000) = 2600.00          | 10400.00                   | 7600.00                     |
|      4 | (&)( 13000) = 1733.33          | 12133.33                   | 5866.67                     |
|      5 | (&)( 13000) = 866.67           | 13000.00                   | 5000.00                     |

Table 11-18

|                    | Year 1   | Year 2   | Year 3   | Year 4   | Year 5   |
|--------------------|----------|----------|----------|----------|----------|
| BTCF               | $6000.00 | $6000.00 | $6000    | $6000.00 | $6000.00 |
| Depreciation       | 4333.33  | 3466.67  | - 2600   | 1733.33  | 866.67   |
| Net Taxable Income | 1666.67  | 2533.33  | 3400     | 4266.67  | 5133.33  |
| Tax (@ 50%)        | 833.33   | 1266.67  | 1700     | 2133.33  | 2566.67  |
| ATCF               | 5166.67  | 4733.33  | 4300     | 3866.67  | 3433.33  |

## (b) See Table 11-18.

In  writing the equation for  the after-tax ROR, we  note that the depreciation charges form a gradient series, with

<!-- formula-not-decoded -->

Hence, the ATCFj also form a gradient series, with

<!-- formula-not-decoded -->

Table 11-19

|   Year | Depreciation Charge for Year   | Accumulated Depreciation   | Book Value at End of Year   |
|--------|--------------------------------|----------------------------|-----------------------------|
|      1 | $2046.33                       | $ 2046.33                  | $15953.67                   |
|      2 | 2291.89                        | 4338.21                    | 13661.79                    |
|      3 | 2566.91                        | 6905.12                    | 11094.88                    |
|      4 | 2874.94                        | 9780.07                    | 8219.93                     |
|      5 | 3219.93                        | 13000.00                   | 5000.00                     |

- 1 1 . 7 Refer to Problems 11.2  and 11.6. Is the computer system a viable proposition i f   the company's after-tax MARR is 12%?

Table 11-20

|                    | Year 1   | Year 2   | Year 3   | Year 4   | Year 5   |
|--------------------|----------|----------|----------|----------|----------|
| BTCF               | $6000.00 | $6000.00 | $6000.00 | $6000.00 | $6000.00 |
| Depreciation       | 2046.33  | 2291.89  | 2566.91  | 2874.94  | 3219.93  |
| Net Taxable Income | 3953.67  | 3708.11  | 3433.09  | 3125.06  | 2780.07  |
| Tax (@ 50%)        | 1976.84  | 1854.06  | 1716.55  | 1562.53  | 1390.04  |
| ATCF               | 4023.16  | 4145.95  | 4283.45  | 4437.47  | 4609.96  |

The after-tax cash flows are computed in Table 11-20. Then, at  MARR = 12%,

$4283.45(P/F, 12%,  3)

<!-- formula-not-decoded -->

=

<!-- formula-not-decoded -->

From  this, we  conclude that  the investment meets the after-tax MARR and  pays an  extra $219.18 (in today's  money)  over the five-year useful life.

- 11.8 Rework Problem 11.2  using the ACRS. Assume that the IRS classifies the asset as five-year property.
- (a) See Table 11-21.
- (b) See Table 11-22.

Table 11-21

|   Year | Depreciation Rate for Year   | Depreciation Charge for Year   | Accumulated Depreciation   | Book Value at End of Year   |
|--------|------------------------------|--------------------------------|----------------------------|-----------------------------|
|      1 | 15%                          | $2700                          | $ 2700                     | $15300                      |
|      2 | 22                           | 3960                           | 6660                       | 11340                       |
|      3 | 21                           | 3780                           | 10 440                     | 7560                        |
|      4 | 21                           | 3780                           | 14 220                     | 3780                        |
|      5 | 21                           | 3780                           | 18000                      | 0                           |

Table 11-22

|                    | Year 1   | Year 2   | Year 3   | Year 4   | Year 5   |
|--------------------|----------|----------|----------|----------|----------|
| BTCF               | $6000    | $6000    | $6000    | $6000    | $6000    |
| Depreciation       | 2700     | 3960     | - 3780   | - 3780   | - 3780   |
| Net Taxable Income | 3300     | 2040     | 2220     | 2220     | 2220     |
| Tax (@ 50%)        | 1650     | 1020     | 1110     | 1110     | 1110     |
| ATCF               | 4350     | 4980     | 4890     | 4890     | 4890     |

-

Sale of   the equipment for its salvage value at the end o f   year 5 produces a long-term capital gain, o f   which the value after taxes is

<!-- formula-not-decoded -->

Hence, the equation for the after-tax ROR is

<!-- formula-not-decoded -->

giving i* = 14.45%.

- 11.9 Rework Problem 11.8 on  the assumption that the asset is reclassified as three-year property.
- ( a ) See Table 11-23.
- ( b ) See Table 11-24.

Table 11-23

|   Year | Depreciation Rate for Year   | Depreciation Charge for Year   | Accumulated Depreciation   | Book Value at End of Year   |
|--------|------------------------------|--------------------------------|----------------------------|-----------------------------|
|      1 | 25%                          | $4500                          | $ 4 500                    | $13500                      |
|      2 | 38                           | 6840                           | 11340                      | 6 660                       |
|      3 | 37                           | 6660                           | 18000                      | 0                           |
|      4 | 0                            | 0                              | 18000                      | 0                           |
|      5 | 0                            | 0                              | 18000                      | 0                           |

Table 11-24

|                    | a r 1   | Year 2   | Year 3   | Year 4   | Y e a r   |
|--------------------|---------|----------|----------|----------|-----------|
| BTCF               | $6000   | $6000    | $6000    |          |           |
| Depreciation       | - 4500  | 6840 -   | 6660 -   |          |           |
| Net Taxable Income | 1500    | - 840    | -660     |          |           |
| Tax (@ 50%)        | 750     | -420     | -330     |          |           |
| ATCF               | 5250    | 6420     | 6330     |          |           |

<!-- formula-not-decoded -->

whence i* = 16.27%. Note the benefit to the taxpayer when the asset's  cost is depreciated  over a period shorter than the useful life.

## Supplementary Problems

- 11.10 For the asset o f   Problem 11.2, ( a ) determine the ROR of  the project before taxes and (b) recommend a depreciation method on the basis o f   Problems 11.2(b), 11.4(b), 11.5(b), 11.7, and 11.8(b). Ans. ( a )   24.4%; (b) sum-of-years' -digits (if  allowed by  the IRS, which is doubtful)

- 11.11 A car rental agency has bought three economy-size, four medium-size, and two full-size cars; see Table 11-25.  Using  composite  depreciation, compute  the  annual  straight-line  depreciation charge  and  the (composite) life for this collection o f   cars. Ans. $12 100, 3241121 = 2.678  years
- 11.12 Rework Problem 11.11 using group depreciation. Ans. $12 150, 813 = 2.667  years
- 11.13 Rework Problem 10.16, assuming a Cyear tax life remaining for the current machine and a Cyear tax life for the new one. Straight-line depreciation is used, and an after-tax MARR o f   15% is applicable. The tax rate is 50%. Ans. after-tax EUACOu = $6565, after-tax EUAC.,, = $7640; keep old machine.
- 11.14 Would the decision made in Problem 10.5 change i f   the second-hand machine could be depreciated in 10 years by  the sum-of-years' -digits  method and  the company's tax rate is 52%? The after-tax MARR is 10%. Ans. after-tax EUAC*,,,dwn = $168, after-tax EUAC,,~-L,, = $407; decision unchanged.
- 11.15 Rework Problem 10.15, using an after-tax MARR of  10% and straight-line depreciation. The company's tax rate is 52%. Ans. 18 days
- 11.16 Would the economic life of  the challenger in  Problem 10.19 change i f   the sum-of-years' -digits  depreciation  method is used, the tax life is 8 years, the tax rate is 52%, and the after-tax MARR is  lo%? Ans. no [after-tax EUAC(6) = $23211
- 11.17 Perform an after-tax analysis for the situation described in  Problem 10.20. Assume that the service life and the tax life are identical, that straight-line depreciation is used, that the after-tax MARR is 10%. and that the company's tax rate is 50%. Ans. after-tax CUV &gt; $1000; keep current machine.
- 11.18 A machine's current book value is $600. The machine cost $1300 three years ago. Operating expenses have been $380 per year, and the machine could last for three more years. Because of  a breakthrough in design,  a  replacement  machine which  would  save $300  per  year  sells for  $1000  and  has  an  expected service life o f   eight years. The scrap value of  either machine at any time after installation is $100. If the IRS allows straight-line depreciation over a six-year period for this type o f   machinery and i f   an after-tax MARR of  12%  is acceptable, should the current machine be changed? The company's  tax rate is 52%. Ans. after-tax EUACCumnt = $90, after-tax EUAC,l,-ent = $167; keep current machine.
- 11.19 An  income-producing asset costs $60 000, has an  estimated useful  life o f   7 years, has no salvage value after installation, and  is expected to produce annual  net savings o f   $15 000.  The company's tax  rate is 52%. Compute (a) the before-tax ROR, and (b) the after-tax ROR under straight-line depreciation. Ans. (a) 16.3%;  (6) 8.6%
- 11.20 For  the  situation  described  in  Problem  11.19,  compute  the  after-tax  ROR  when  sum-of-years 1 -digits depreciation is charged. Ans. 9.7%
- 11.21 Fifty  percent o f   the asset  described in  Problem 11.19 was financed from capital borrowed at 7%. This loan is to be repaid at the end of the seventh year, but interest is due on the principal at the end o f   each year. Rework Problem 11.20.
- Ans. 26.0%  (notice the big difference made by  tax-deductible interest and the delay o f   seven years in half  o f   the investment)

Table 11-25

| Initial Cost (each)   | $6200   |       |
|-----------------------|---------|-------|
| Service Life          |         |       |
| Salvage Value (each)  |         | $7300 |

- 11.22 Would the result o f   Problem 10.23  change  under  straight-line  depreciation,  a 35% tax rate, and an after-tax MARR of  lo%? Assume that the current machine is fully depreciated. Ans. no
- 11.23 Rework Problem 10.24  using straight-line depreciation, a 50% tax rate, and an after-tax MARR o f   10%. Assume that salvage values are book values and that overhaul expenditures are depreciable. Ans. Now the best action is to overhaul the old machine.
- 11.24 An underwater camera is purchased for $1000; it has an expected life of  12 years, at the end o f   which the estimated salvage value is $730. Using straight-line depreciation,  find the book value o f   the camera at the end of   8 years. Ans. $420
- 11.25 An  engineer is  being  transferred to another state  and  must  vacate her  house. The house,  bought for $40 000 eight years ago, can be sold now for $60 000; the property is free of  debt. I f   the house is sold, she will have to pay a 15% capital gains tax. The engineer is also considering leasing the house for five years, receiving $7200 annual rental. In  this case, she estimates an  annual  disbursement o f $1800  for  taxes, insurance, and maintenance.  She would also be allowed $1200 per year depreciation on her tax return (in addition to her cash disbursements); her rental income would be taxed at 30%. (Note that houses cannot be depreciated during the years used as the owner's personal residence.)  Determine her after-tax ROR i f she  decides  to  lease  the  property  and  i f the  property  shall  be  worth  $64000  at  the  end  of the lease. Ans. 8%
- 11.26 A truck was bought 10 years ago for $70 000; its current salvage value is $14 000. It is believed that it can last 5 more years, at which time its salvage value will be $8000. Its operating expenses amount to $14 000 per year and they are expected to remain at that level for the next 5 years. The truck is currently being depreciated by  the straight-line method, using a 15-year life and estimated salvage value of  $10 000.  A new  truck can  be purchased for $65 000. It will  have yearly operating costs of  $9000 and would last 20 years; salvage value after 20  years is estimated at  $15 000.  Again, straight-line depreciation would  be used.  Supposing  that  tax  rates are 50%  on  income  and 15%  on  capital gains (or losses), and  that  the company's after-tax MARR is lo%, should it buy the new truck?

Ans. No: after-tax EUAC0jd = $7967, after-tax EUAC., = $10 623

- 11.27 A $60 000 asset will  be depreciated by  the straight-line method over a six-year period. NO salvage value is expected. If   the company's tax  rate is 50°h, what would be  the present-worth advantage o f   using the sum-of-years 7 -digits method, given a 10%  after-tax MARR? Ans. $1184
- 11.28 Rework Problem 11.26 using the ACRS for the new truck, classified as a 10-year asset. The current truck is still depreciated by  the straight-line method. Ans. No: after-tax EUAC,ld = $7967, after-tax EUAC,,, = $9481
- 11.29 Rework Problem 11.27 using the ACRS, with a five-year life, instead o f   the sum-of-years' -digits method. Am. -$3217  (i.e., straight-line depreciation is better in  this case)

<!-- image -->

## Preparing and Presenting an Economic Feasibility Study

## 12.1 INTRODUCTION

This chapter  attempts  to  bridge  the gap  between  the specific  analytic  techniques-equivalent uniform annual series,  rate o f return,  etc.-and the "wide-angle" considerations that determine (or should  determine)  investment  decisions  in  the  real  world.  Our  frame  of reference  will  be  the presentation o f   a feasibility analysis to a lending institution.

Example 12.1 It will  be assumed throughout this chapter that the project under study can be characterized as "marginal"  with respect to the overall economic environment. Discuss the need for such an assumption and give examples of  marginal projects.

A project is "marginal" if  it  will  not significantly alter the economic environment. A dry-cleaner outlet in a major shopping center, a small die-casting factory in  an  industrial park, a new  boutique in  a fashion  mall, are typical  examples.  Although  undeniably  important  to  their  promoters,  these  ventures  will  not  effect  major changes in  the economic patterns o f   the communities where they are  to be implemented. For such  ventures, clear-cut decisions may  be derived from an engineering economic analysis.

By  contrast, projects which represent a structural investment for the community (which would, for example, significantly alter  the  unemployment level  or  the gross regional product) would  need  in-depth study in  every aspect and a thorough sensitivity analysis o f   each assumption underlying the feasibility study. Most likely, final decisions would be largely political in  nature. Two such  nonmarginal projects were Walt Disney World, which changed central Florida from a depressed rural area to a tourist capital, and the Trans-Alaska Oil Pipeline.

The sections that follow will discuss, one at a time, the main components of  the feasibility study.

## 12.2 BACKGROUND INFORMATION

This section o f   the report should consist of:

1. A brief  summary o f the project, covering the nature o f   the venture, location, expected site, life, overall capital costs, financing, and return on investment
2. A description o f   the promoting individuals or institution:  name(s), addresses (both legal and of proposed  facility  location),  and  institution  characteristics  (capital,  number  of  shares  of stock,  principal shareholders, etc.)

Example 12.2 Why do most lending institutions require background information o f   the above type?

The lender  will  charge  interest;  nevertheless,  he  is  risking  his  money,  and  before  committing  himself, understandably  wants  to  gauge  the  risk  as  accurately  as  possible.  Complete  details  about  the  board  and executive officers o f   the  promoting company, any  partnerships or relationships to other companies, insurance available,  and- most important-a  history  o f past  and  current  projects,  are  all  commonly  required.  For industries currently in operation, data about their capacity, production level, productivity indicators, sales, labor force, salary structure, overhead, inventory turnover ratio, and other items (which  may include some seemingly unrelated to the project itself) may be in order. Sometimes the lender requires an organizational chart, as well as details  about  production  planning and  control, quality control, labor  relations, and financial situation  (end of year balances for the last few  years).

## 1 2 . 3 MARKET STUDY

In this section the report describes what is to be produced, and where and to whom it is going to be sold. An  analysis should  be made of:

1. The product-description,  brand or name, quality standards to be met, characteristics,  and utilization. Subproducts (if  any)-description, utilization (if  it is not going to be marketed).
2. The  market--estimated  demand  for  the  final  product.  If the  product  can  serve  as  raw material or intermediate product for some other article  (e.g.,  a microprocessor to be used in an electronic toy), an estimate of  potential uses and corresponding demands is in  order. An analysis  of  complementary and competitive  products, as well  as their current  and expected availabilities, should also be included.

Example 12.3 Discuss the importance of a thorough, realistic market study. What should be included in it, and what should  be its ultimate objective? Show a typical summary output of  this phase of  the analysis.

A  number  of  otherwise  carefully  planned  ventures  have  failed  because  of an  unjustified  belief  that  the market will  buy  whatever  can  be  produced.  An  excessive capacity  is  then  built  to exploit  the good  idea- so good, in  fact, that it attracts immediate competition, and the long-term  market share turns out to be lower than predicted. (Case in  point: some fast-food retailers.)

A marketing study should  provide information about:  volume of  similar  products sold in the target  region over the last, say, five years; local production; imports from, and exports to, other areas; consumption. It should give  a  quantification  (and  causes)  of  any  unmet  demand.  An  analysis of  main  producers  is  a  must:  location, market  share,  other  areas  served  by  them.  Also,  an  analysis  of main  consumers:  where  they  are  located, historical consumption, uses of  our product.

The goal  of  the market study  is to provide  the basis for  a forecast  of  demand  for  the product  in  the first (say) five years after the operations start up. Not  just a single number, but a range of  values should be sought. A pessimistic, an optimistic, and a most  probable value would  be invaluable in  a sensitivity analysis,  provided  the technical  bases of  the forecast are sound.  A description  of the techniques used in forecasting,  as well as of  the assumptions and data bases used in the analysis, should  be included  in  an appendix to the report.

Figure 12-1 suggests the summary format.

Year 1 (units)

Year 2

Year 3 (units)

(units)

1.  Estimate of  Regional Production

2.  Imports

3.  Exports

4.  Estimated  Demand (1 + 2 - 3)

## With respect to the company

5.  Estimated  Production

6.  Imports

7.  Exports

8.  Regional Demand Met (5 + 6 - 7)

Fig. 12-1

3. Raw materials analysis. [Too often this phase of  the study is replaced by an assumption  that whatever is required will be there when (and in the amount) needed.]

Example 12.4 Discuss  the  potential  dangers  of omitting  a  raw  materials  analysis.  Describe  what  such  an analysis would yield. Give an example of  obvious need for this type of  study.

Unreliable providers may  cause shortages, or  they  may  force operators  to  keep  excessive raw  materials inventories lest they expose themselves to production stoppages. A raw materials analysis should include a study of prices (in  the  national and  international markets), with  considerations of  transportation, insurance,  tariffs, quality and delivery reliability of  provider included for the latter and normal commercialization channels. I f   the project size is large, its potential effect on  the raw  materials market should  be also considered. The availability of   alternative providers, or even o f   alternative materials, may also turn out to be an important factor.

An extreme instance of  the necessity for raw materials analysis was provided by  the oil crisis o f   the 1970s.

## 12.4 PROJECT ENGINEERING

This  section makes  an  analysis  of available technologies for the process. A  brief technical/economic  comparison should  be made and a  justification  of  the selected technology  provided. A  statement  of the  potential  consequences  of this  selection,  a  comparison  with  the  "normal" competitor,  as well as with  the "state of  the art" competitor,  are desirable.  Opinions from outside consultants, if  available,  regarding the selection of  technology are also recommended.

Example 12.5 Describe the contents o f   the typical project engineering  segment o f   the report. Comment on the effect o f   technology,  size, start-up, and major equipment. Illustrate a typical summary output o f   this phase o f   the analysis.

The project engineering section o f   the economic feasibility report should include a thorough description of:

Fabrication process. No detail plans are needed; a flow  diagram  with  durations o f   the stages, capacities, yields, and material and energy balances is normally sufficient for most manufacturing industries.

Project size. The planned production capacities must be forecast, indicating expected dates to attain them. Operating conditions  (shifts  per  day,  days  per  year)  must  be  indicated.  The  relationship  between  this production plan and the market and raw  materials studies should be included. An analysis of the marketshare  penetration  must  be  provided.  A  justification  o f size  from  the  point  o f view  of  the  selected technology, financing limitations, plant location, seasonality factors, market restrictions, etc.,  is important. Analyses of   size versus production costs, break-even point, resources needed to compensate for operating deficits over the start-up period, and impact o f   unforeseen slumps in  sales are also required. A note should be made if future expansions to adapt to enlarged market share and product acceptance are envisioned.

Location. This extremely important factor is frequently lost in  the shuffle. It is evident that remoteness o f   a location influences the pool of  manpower available for the project, as well as the level o f   investment needed to  provide housing, transportation, energy, water, sewage and  tailings treatment, etc. These same factors should be considered for any location. Special consideration should be given to potential benefits related to the  project's location,  such as tax breaks,  availability  o f cheap  transportation,  surrounding  market, population, local regulations controlling noise and  pollution, etc. The main factors influencing the selection of   the project site should be discussed in  detail, and an  analysis o f   potential alternative sites, i f   any, should also be included.

Physical means of production. The plant site must be specified (total and build surfaces). Buildings required must  also  be  detailed. Areas should  be  classified as  direct  production,  ancillary  facilities, administrative, warehouses, etc. If some o f   the buildings are already available and require little renovation, that should  be noted. It is also very important to specify any earth moving, roads, docks, railroad connections, fences, etc., which should be needed as part o f   the site preparation. Note that electric substations,  water treatment plant, and the like, are normally considered auxiliary facilities (see below).

Major equipment. Separate lists are  usually  made  o f domestic and  imported  equipment. The  units are listed  in  order o f   decreasing value,  until  the total value o f   the two  lists represents 60  to 70  percent of  the entire capital investment. Numbers of  the various units, their technical characteristics, theoretical capacities, prices (FOB; for imported equipment, extra charges such as transportation, in-transit insurance, tariffs, etc., must be detailed), and manufacturers  are all indicated. Prices quoted should reflect actual market values, i f at all  possible. Pro forma invoices are o f   great help in  documenting this phase of the analysis.

Auxiliary facilities (for direct production)-electric energy, gas, fuel, compressed air, water treatment plant, internal communications, internal transportation, sewage, tailings treatment  plant, etc.  If  applicable, flow diagrams and material and/or energy balances  must be provided. A global estimate  o f   capital expenditures  (as a function o f   plant size, i f   applicable) should also be included.

Service facilities. These include plant security, medical facilities, dining room, and other personnel-related facilities. A global estimate of  capital expenditures (as a function o f   plant size, i f   applicable) is required.

Raw  materials  and  supplies. For each  production  level,  an  estimate must  be  made of  quantity, quality requirements, annual  consumption,  availability, unit  price,  and  consumption  per  unit  o f product.  For electric energy, it  is customary to indicate installed power, processes at constant and at variable load, and maximum illumination-related load. An estimate of  size and value must be given for all raw materials and for in-production or finished-product inventories expected for the process.

Transportation  expenses-for raw materials,  fuels,  and intermediate  and  finished products. If contracts  are to be awarded to third parties, their availability and maximum requirements (at start-up and in  the long run), as well as prices, must be included.

Manpower requirements. Estimate  o f   personnel required  at  different  levels  in each unit, including  labor,  direct supervisory  personnel,  indirect  supervisory  personnel,  service  people  (labs,  maintenance, security),  administration,  marketing,  and  management.  Detail  wage  and  salary  structures,  as  well  as  fringe  benefit charges. Any contractual obligations should also be included. Any  need  for specially  trained personnel, training facilities, start-up consultants, etc.,  should also be reported.

The project engineering phase of  the  analysis should  produce a summary bar diagram  describing target completion date for all major project components, as well as a plan for project implementation until "normal" operation is achieved. Such  a bar chart is illustrated in  Fig. 12-2.

Fig. 12-2

<!-- image -->

Operations Start-up

## 12.5 COST ESTIMATION

This section of the economic feasibility report falls into two main parts: the analysis of investment costs (or first costs) and the analysis of operating costs.

Example 12.6 Itemize the components of  the investment costs for a typical industrial project.

The  investment  costs  include  all  expenditures  related  to  the  implementation  o f the  project,  from  its conception  until  start-up.  A  distinction  is  usually  made  between depreciable and nondepreciable investment costs.

Fued capital costs. (Depreciable, except for land purchasing). These include costs of: residential buildings (offices, cafeteria, etc.); industrial buildings (including warehouses); roads, energy lines, railroads, and other infrastructure; hauling, loading, and unloading equipment; industrial machinery and equipment; spare parts (includes maintenance,  repair,  and  standby  equipment); ancillary  facilities (electrical substation, laboratories,  transformers, fire  extinguishers, etc.);  office  furniture. Usually only  buildings and  main  equipment and facilities are estimated accurately. Spare parts, furniture, etc.,  are often  estimated as a percentage o f those items.

Operating capital costs. This is theamount o f   money required to start up the project and keep it working. The operating  capital  costs  usually  increase until the project reaches the level  of   normal  operation; then they stay on a plateau throughout the project's lifetime,  and are recovered in  the final year o f   operation. They cannot be depreciated. They include: cash (to pay salaries, to cover emergencies, and- sometimes- to  help in operating process); circulating capital (accounts receivable minus accounts payable); stocks and inventories (general merchandise, finished or intermediate or secondary products, raw  materials, in-transit material, packages, consumption materials, etc.);  material handling (loading and transportation and unloading from and  to the warehouses, cost o f   inventory control and insurance, protection o f   inventories, etc.).

The analysis of first  cost  should  produce a  table  such  as  Table 12-1  (for each  alternative size o f project considered).

## Table  121

| Item                                                                 |
|----------------------------------------------------------------------|
| Feasibility studies                                                  |
| Land                                                                 |
| Land preparation                                                     |
| Construction & installation (buildings)                              |
| Equipment (incl. insurance, transportation, installation & start-up) |
| For the main plant                                                   |
| For ancillary facilities                                             |
| For construction                                                     |
| Patents and royalties                                                |
| Supervision .                                                        |
| Consultantships (legal and engineering)                              |
| Start-up costs                                                       |
| Subtotal                                                             |
| Contingency costs (% of subtotal)                                    |
| Operating capital                                                    |

Typical  errors  in  the  analysis  of investment  costs  are:  (i)  underestimation  of  transportation, installation,  and  start-up  costs;  (ii)  underestimation  of  time  needed  to construct  the  project;  (iii) underestimation  of the  operating  capital;  (iv)  underestimation  of the  time  needed  to  test-run equipment  and  to  reach  the  level  of normal  operation;  and  (most  common)  (v)  omission  of a sensitivity  study  of project  size.  Keep  in  mind  that  first  costs,  being  incurred  in  year  0,  are  not discounted.  Thus,  too-large estimates  of  investment  costs can  kill  a  project's feasibility  a  lot faster than any overestimation of  operating expenses.

Example 12.7 Itemize the components of  the operating costs for a typical industrial project.

Direct costs: raw material (includes cost of  handling); direct materials (explosives, catalysts, grinding balls, packages, etc.);  direct labor (including direct supervision)-salaries, fringe benefits, overtime, etc.; directproduction utilities (energy, fuel, lubricants, steam, water, etc.).

Indirect costs: indirect labor (salaries, fringe benefits,  overtime, etc., for general supervision, maintenance, general engineering, security, plant  protection, quality control, laboratories); indirect  materials  (e.g.,  lab reagents); other  indirect  costs  (health clinic,  recreation  and  eating facilities, transportation o f personnel, communications, lights, cleaning, etc.);  employee benefits (child-care center, gymnasium, etc.).

Overhead costs: administrative costs (salaries o f   managerial personnel, secretaries, legal and engineering staff;  rent,  office  cleaning,  office  materials,  reproduction, etc.);  fixed  charges  (taxes,  insurance);  selling expenses (salesmen,  commissions, travel, market surveys, entertainment o f   clients, displays, sales space, etc.); research and development; financing charges (interest and loan payments); bad debts; contributions (not in excess of S0/0 of   taxable income); losses by fire, theft, etc.,  not covered by  insurance.

The analysis of  the operating costs should  produce a table such as Table 12-2 (for each alternative size o f project considered).

## Table 122

| Item                        | Year 1   | Year2 -.. Yearn   |
|-----------------------------|----------|-------------------|
| Direct costs Labor Material |          |                   |
| Indirect costs              |          |                   |
| Labor                       |          |                   |
| Material                    |          |                   |
| Other                       |          |                   |
| Overhead costs              |          |                   |
| Administrativecosts         |          |                   |
| Selling costs               |          |                   |
| Other                       |          |                   |

The  most  common  error  in  the  analysis  of  operating  costs  is  the  wrong  estimation  of plant utilization  (i.e.,  designing with  overcapacity),  which strongly affects direct  costs.

## 12.6 ESTIMATION OF REVENUES

A  projection  of  annual  income  has  to  be  made,  with  consideration  of:  (i)  sales  of  main  and secondary  products;  (ii) services  provided; (iii) recuperation  of  operating capital  (typically  occurs at the  end  of year n, when  stocks  and  inventories  are  depleted,  circulating  capital  is  settled,  and material handling stops).

The most common error in  this phase of  the analysis is to assume that all the production will be sold.  Sometimes  market  conditions  will  not  permit  this  to  happen;  or  the  product  quality  may fluctuate, and sizable quantities may have to be recycled or scrapped.

Another common error, from a company point of  view, is to forget that revenue consists only in actual incremental receipts.  For  example,  if an  ice  cream  distributor  is  evaluating  a  new  line  of products, actual net receipts attributable to this product is given by the expected sales less the loss in sales of  current products  because of  customers' shifting preferences. In  the extreme case, the public may  not  be  spending  more  money  for  the  company's  products  (although the  new  product  is experiencing brisk sales); rather, they have ceased buying some of  the old products and are using that money to buy the new one!

## 12.7 FINANCING

Once  the cost  and  revenue analyses  are  ready,  (11.15)  and  (11.19)  may  be  used  to prepare a summary table of  yearly cash  flows (see Table 12-3). Then a specific performance indicator, such as after-tax  PW  or  after-tax  ROR,  can  be  computed.  In  fact,  it  is  recommended  that  both  these indicators be calculated.  For, on the one hand, if  the company has a good estimate of  its (after-tax) MARR, then the PW corresponding to that MARR will represent to the company its net increase in assets  as  a  result  of the  project  once  the  initial  investment  (and  all  operating  costs)  have  been recovered and the MARR realized. On the other hand, financial institutions prefer the ROR, since it is independent of  the company's MARR and is useful in choosing among independent projects that are similar in  size  and duration (see Section 9.2).

- (1) Sales
- (2) Services provided
- (3) Recovered operating capital
- (4) TOTAL RECEIPTS
- (5) Less:  Direct labor
- (6) Less:  Direct material
- (7) Less: Maintenance
- (8) Less: Indirect material
- (9) Less: Indirect labor
- (10) Less: Overhead
- (11) Less: Other expenses
- (12) Net income before taxes
- (13) Less: Depreciation
- (14) Net taxable income
- (15) Less: Taxes [rate X (14)]
- (16) After-tax net income
- (17) Depreciation
- (18) After-tax net cash flow

It should be noted that, generally,  not one but two economic evaluations must be presented to a lending institution. One of  them analyzes the project as if  it were going to be completely financed by the  owner.  The results  of this  analysis  reflect  the  project's  potential of  success  (and  its  ability  to generate enough revenue to pay the loan). The second analysis takes account of  the size of  the loan and  of  the  corresponding  schedule  of  payments.  This  analysis  furnishes  the  owner  with  a  better representation  of  the economic potential of  the project as it is actually intended to be financed. Both sorts of  evaluation  are carried out using the techniques of  Chapter 11--see, in  particular, Problems 11.19  and  11.21. (That  Chapter  11  dealt  with  level  series  of before-tax  cash  flows  is  obviously inessential.)

## Table 12-3

<!-- image -->

## Compound Interest FactorsAnnual Compounding

COMPOUND  INTEREST  FACTORS  -  ANNUAL  COMPOUNDING

I N T E R E S T   RATE  = 0 . 2 5 PERCENT

|    | SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|----|-----------------------------------------|------------------------------------------|-------------------------------------------|--------------------------|
| N  | ( F / P)                                | ( F/ A)                                  | ( A l p )                                 | (A/G)                    |

## COMPOUND INTEREST FACTORS-ANNUAL COMPOUNDING

## COMPOUND  INTEREST  FACTORS  -  ANNUAL  COMPOUNDING

## I N T E R E S T   RATE  = 0 . 5 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|------------------------------------------|------------------------------------------|--------------------------|
| ( F / P)                                | ( F/ A)                                  | ( A l p )                                | (A/G)                    |

## APP.  A] COMPOUND INTEREST FACTORS-ANNUAL COMPOUNDING

## COMPOUND  INTEREST  FACTORS -  ANNUAL  COMPOUNDING

## I N T E R E S T   RATE  = 0 . 7 5   PERCENT

|    | SINGLE- PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|----|------------------------------------------|------------------------------------------|-------------------------------------------|--------------------------|
| N  | ( F / P )                                | ( F / A )                                | ( A l p )                                 | ( A I G)                 |

## COMPOUND  INTEREST FACTORS-ANNUAL  COMPOUNDING

## COMPOUND  INTEREST  FACTORS  -  ANNUAL  COMPOUNDING

## I N T E R E S T   RATE  = 1 . 0 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|-----------------------------------------|-------------------------------------------|--------------------------|
| ( F / P)                                | ( F/ A)                                 | ( A l p )                                 | (A/G)                    |

## APP.  A] COMPOUND INTEREST FACTORS-ANNUAL COMPOUNDING

## COMPOUND  INTEREST  FACTORS  -  ANNUAL  COMPOUNDING

## I N T E R E S T   RATE  = 1.25 PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|------------------------------------------|------------------------------------------|--------------------------|
| ( F / P)                                | ( F/ A)                                  | ( A l p )                                | (A/G)                    |

139

## COMPOUND INTEREST FACTORSANNUAL COMPOUNDING

## COMPOUND  INTEREST  FACTORS -ANNUAL  COMPOUNDING I N T E R E S T   RATE = 1 . 5 0   PERCENT

100

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------|
| ( F / P)                                | ( F / A)                                | ( A l p )                                | (A/G)                    |

## APP.  A] COMPOUND INTEREST FACTORS-ANNUAL COMPOUNDING

## COMPOUND  INTEREST  FACTORS -ANNUAL  COMPOUNDING I N T E R E S T   RATE = 2. 0 0 PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------|
| (F/P)                                   | (F/A)                                   | ( Al p )                                 | (A/G)                    |

## COMPOUND  INTEREST  FACTORS -ANNUAL  COMPOUNDING I N T E R E S T   RATE = 3 . 0 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------|
| (F/P)                                   | ( F / A)                                | ( A l p )                                | (AIG)                    |

## APP.  A] COMPOUND INTEREST FACTORS-ANNUAL COMPOUNDING

## COMPOUND  INTEREST  FACTORS  -  ANNUAL  COMPOUNDING I N T E R E S T   RATE  = 4 . 0 0 PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|------------------------------------------|-------------------------------------------|--------------------------|
| ( F / P)                                | ( F / A)                                 | ( A l p )                                 | (AIG)                    |

## COMPOUND  INTEREST  FACTORS -ANNUAL  COMPOUNDING

## I N T EREST  RATE = 5 . 0 0   PERCENT

| N   | SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR (F/A)   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----|-----------------------------------------|-----------------------------------------------|------------------------------------------|--------------------------|
|     | ( F / P)                                |                                               | ( Al p )                                 | (A/G)                    |

## APP. A] COMPOUND INTEREST FACTORS-ANNUAL COMPOUNDING

## COMPOUND  INTEREST  FACTORS -  ANNUAL  COMPOUNDING I N T E R E S T   RATE  = 6 . 0 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|------------------------------------------|-------------------------------------------|--------------------------|
| ( F / P )                               | ( F / A )                                | ( A l p )                                 | ( A I G)                 |

## COMPOUND  INTEREST  FACTORS -ANNUAL  COMPOUNDING I N T E R E S T   RATE = 7 . 0 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------|
| ( F / P)                                | ( F / A)                                | ( A l p )                                | (A/G)                    |

## APP.  A] COMPOUND INTEREST FACTORS-ANNUAL COMPOUNDING

## COMPOUND  INTEREST  FACTORS  -  ANNUAL  COMPOUNDING I N T E R E S T   RATE  = 8 . 0 0 PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|-----------------------------------------|-------------------------------------------|--------------------------|
| ( F / P)                                | ( F / A )                               | ( A l p )                                 | (A l G)                  |

## COMPOUND INTEREST FACTORS-ANNUAL COMPOUNDING [APP.  A

## COMPOUND  INTEREST  FACTORS -ANNUAL  COMPOUNDING I N T E R E S T   RATE = 9.00 PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|------------------------------------------|-------------------------------------------|--------------------------|
| ( F / P )                               | ( F /A)                                  | ( A l p )                                 | (A/G)                    |

## APP.  A] COMPOUND INTEREST FACTORS-ANNUAL COMPOUNDING

## COMPOUND  INTEREST  FACTORS -ANNUAL  COMPOUNDING

## I N T E R E S T   RATE = 1 0 . 0 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------|
| (F/P)                                   | (F/A)                                   | ( Al p )                                 | (A/G)                    |

## COMPOUND  INTEREST  FACTORS -ANNUAL  COMPOUNDING I N T E R E S T   RATE = 1 2 . 0 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR ( F / P)   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR ( F / A)   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR ( Al p )   | GRADIENT SERIES FACTOR (A/G)   |
|--------------------------------------------------|--------------------------------------------------|---------------------------------------------------|--------------------------------|

## APP.  A] COMPOUND INTEREST FACTORS-ANNUAL COMPOUNDING

## COMPOUND  INTEREST  FACTORS -ANNUAL  COMPOUNDING I N T E R E S T   RATE = 1 5 . 0 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR ( F l P )   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR ( A l p )   | GRADIENT SERIES FACTOR (A/G)   |
|---------------------------------------------------|----------------------------------------------------|--------------------------------|

## COMPOUND  INTEREST  FACTORS  -  ANNUAL  COMPOUNDING I N T E R E S T   RATE  =  2 0 . 0 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR ( F / P)   | UNIFORM- SERIES COMPOUND-AMOUNT FACTOR ( F / A)   | UNIFORM- SERIES CAPITAL-RECOVERY FACTOR ( A l p )   | GRADIENT SERIES FACTOR (A/G)   |
|--------------------------------------------------|---------------------------------------------------|-----------------------------------------------------|--------------------------------|

## APP.  A] COMPOUND INTEREST FACTORS-ANNUAL COMPOUNDING

## COMPOUND  INTEREST  FACTORS -ANNUAL  COMPOUNDING I N T E R E S T   RATE = 2 5 . 0 0   PERCENT,

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR (F/P)   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR (F/A)   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR ( Al p )   | GRADIENT SERIES FACTOR (A/G)   |
|-----------------------------------------------|-----------------------------------------------|---------------------------------------------------|--------------------------------|

## COMPOUND  INTEREST  FACTORS -ANNUAL  COMPOUNDING I N T E R E S T   RATE = 3 0 . 0 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR ( F / P)   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR (F/A)   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR ( A l p )   | GRADIENT SERIES FACTOR (AIG)   |
|--------------------------------------------------|-----------------------------------------------|----------------------------------------------------|--------------------------------|

## APP.  A] COMPOUND INTEREST FACTORS-ANNUAL COMPOUNDING

## COMPOUND  INTEREST  FACTORS  -  ANNUAL  COMPOUNDING

## I N T E R E S T   RATE  =  4 0 . 0 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR ( F / P)   | UNIFORM- SERIES CAPITAL-RECOVERY FACTOR ( A l p )   | GRADIENT SERIES FACTOR (A/G)   |
|--------------------------------------------------|-----------------------------------------------------|--------------------------------|

## COMPOUND  INTEREST  FACTORS -ANNUAL  COMPOUNDING I N T E R E S T   RATE = 50.00 PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR (F/P)   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR ( F / A)   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR (A/P)   | GRADIENT SERIES FACTOR (A/G)   |
|-----------------------------------------------|--------------------------------------------------|------------------------------------------------|--------------------------------|

## Appendix  B

## Nominal versus Effective Interest Rates

EFFECTIVE  INTEREST  RATES

| NOMINAL INTEREST   | F R E Q U E N C Y O F C O M P O U N D I N G   | F R E Q U E N C Y O F C O M P O U N D I N G   | F R E Q U E N C Y O F C O M P O U N D I N G   | F R E Q U E N C Y O F C O M P O U N D I N G   | F R E Q U E N C Y O F C O M P O U N D I N G   | F R E Q U E N C Y O F C O M P O U N D I N G   |
|--------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| RATE               | SEMIANNUALLY                                  | QUARTERLY                                     | MONTHLY                                       | WEEKLY                                        | DAILY                                         | CONTINUOUSLY                                  |

## Appendix  C

## Compound Interest FactorsContinuous Compounding

COMPOUND  INTEREST  FACTORS -CONTINUOUS  COMPOUNDING

NOMINAL  INTEREST  RATE = 0 . 2 5   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------|
| (F/P)                                   | (F/A)                                   | ( Al p )                                 | (AIG)                    |

159

## COMPOUND  INTEREST  FACTORS -CONTINUOUS  COMPOUNDING

## NOMINAL  INTEREST  RATE = 0.50 PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------|
| (F/P)                                   | (F/A                                    | ( A l p )                                | (A/G)                    |

## APP.  C] COMPOUND INTEREST FACTORS-CONTINUOUS COMPOUNDING

## COMPOUND  INTEREST  FACTORS  -  CONTINUOUS  COMPOUNDING

## NOMINAL  INTEREST  RATE  = 0 . 7 5   PERCENT

|    | SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|----|-----------------------------------------|------------------------------------------|-------------------------------------------|--------------------------|
| N  | ( F/ P)                                 | ( F / A)                                 | ( A l p )                                 | (A/G)                    |

161

## COMPOUND  INTEREST  FACTORS -CONTINUOUS  COMPOUNDING NOMINAL  INTEREST  RATE = 1 . 0 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------|
| (F/P)                                   | (F/A)                                   | ( A l p )                                | (A/G)                    |

## APP.  C] COMPOUND INTEREST FACTORS-CONTINUOUS COMPOUNDING

## COMPOUND  INTEREST  FACTORS -CONTINUOUS  COMPOUNDING NOMINAL  INTEREST  RATE = 1 . 2 5   PERCENT

|    | SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERV FACTOR   | GRADIENT SERIES FACTOR   |
|----|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------|
| N  | ( F / P)                                | (F/A)                                   | ( A l p )                                | (AIG)                    |

## COMPOUND  INTEREST  FACTORS -CONTINUOUS  COMPOUNDING NOMINAL  INTEREST  RATE = 1 . 5 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------|
| ( F / P)                                | (F/A)                                   | ( A l p )                                | (A/G)                    |

## APP.  C] COMPOUND INTEREST FACTORS-CONTINUOUS COMPOUNDING

## COMPOUND  INTEREST  FACTORS -CONTINUOUS  COMPOUNDING

## NOMINAL  INTEREST  RATE = 2 . 0 0   PERCENT

|    | SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|----|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------|
| N  | ( F / P)                                | (F/A)                                   | ( Al p )                                 | (A/G)                    |

## COMPOUND  INTEREST  FACTORS -CONTINUOUS  COMPOUNDING NOMINAL  INTEREST  RATE = 3.00 PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------|
| ( F / P)                                | (F/A)                                   | ( A l p )                                | (AIG)                    |

## APP. C] COMPOUND INTEREST FACTORS-CONTINUOUS  COMPOUNDING

## COMPOUND  INTEREST  FACTORS -CONTINUOUS  COMPOUNDING NOMINAL  INTEREST  RATE = 4.00 PERCENT

|    | SINGLE-PAVMENT COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|----|-----------------------------------------|------------------------------------------|-------------------------------------------|--------------------------|
| N  | ( F / P )                               | (F/A 1                                   | ( A l p )                                 | (A/G)                    |

## COMPOUND INTEREST FACTORS-CONTINUOUS  COMPOUNDING

## COMPOUND  INTEREST  FACTORS  -  CONTINUOUS  COMPOUNDING

## NOMINAL  INTEREST  RATE  = 5.00 PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----------------------------------------|------------------------------------------|-------------------------------------------|--------------------------|
| ( F/ P)                                 | (F/A                                     | ( A l p )                                 | (A/G)                    |

## APP.  C] COMPOUND INTEREST FACTORS--CONTINUOUS  COMPOUNDING

## COMPOUND  INTEREST  FACTORS -CONTINUOUS  COMPOUNDING NOMINAL  INTEREST  RATE = 6 . 0 0   PERCENT

| N   | SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------|
|     | ( F / P)                                | ( F I A )                               | (A/P)                                    | (AIG)                    |

## COMPOUND  INTEREST  FACTORS -CONTINUOUS  COMPOUNDING NOMINAL  INTEREST  RATE = 7 . 0 0   PERCENT

|    | SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|----|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------|
| N  | ( F I P )                               | (F/A)                                   | ( A l p )                                | (AlG)                    |

## APP.  C] COMPOUND INTEREST FACTORS-CONTINUOUS COMPOUNDING

## COMPOUND  INTEREST  FACTORS -CONTINUOUS  COMPOUNDING NOMINAL  INTEREST  RATE = 8 . 0 0   PERCENT

| N   | SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|-----|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------|
|     | ( F l P )                               | (F/A)                                   | ( Al p )                                 | (A/G)                    |

## COMPOUND  INTEREST  FACTORS -CONTINUOUS  COMPOUNDING NOMINAL  INTEREST  RATE = 9 . 0 0   PERCENT

|    | SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|----|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------|
| N  | ( F I P )                               | (F/A)                                   | ( A l p )                                | (AIG)                    |

## APP. C] COMPOUND INTEREST FACTORS-CONTINUOUS COMPOUNDING

## COMPOUND  INTEREST  FACTORS -  CONTINUOUS  COMPOUNDING

## NOMINAL  INTEREST  RATE  = 1 0 . 0 0 PERCENT

|    | SINGLE- PAYMENT COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES COMPOUND-AMOUNT FACTOR   | UNIFORM- SERIES CAPITAL-RECOVERY FACTOR   | GRADIENT SERIES FACTOR   |
|----|------------------------------------------|------------------------------------------|-------------------------------------------|--------------------------|
| N  | ( F / P )                                | ( F / A )                                | ( A l p )                                 | (A/G)                    |

## COMPOUND  INTEREST  FACTORS -CONTINUOUS  COMPOUNDING NOMINAL  INTEREST  RATE = 1 2 . 0 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR (F/P)   | UNIFORM-SERIES COMPOUNO-AMOUNT FACTOR (F/A   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR ( A l p )   | GRADIENT SERIES FACTOR (A/G)   |
|-----------------------------------------------|----------------------------------------------|----------------------------------------------------|--------------------------------|

## APP.  C] COMPOUND INTEREST FACTORS--CONTINUOUS COMPOUNDING

## COMPOUND  INTEREST  FACTORS -CONTINUOUS  COMPOUNDING NOMINAL  INTEREST  RATE = 1 5 . 0 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR ( F / P)   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR (F/A)   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR ( Al p )   | GRADIENT SERIES FACTOR (AIG)   |
|--------------------------------------------------|-----------------------------------------------|---------------------------------------------------|--------------------------------|

## COMPOUND  INTEREST  FACTORS -CONTINUOUS  COMPOUNDING NOMINAL  INTEREST  RATE = 20.00 PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR (F/P)   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR (F/A)   | UNIFORM-SERIES CAPITAL-RECOVERV FACTOR ( A l p )   | GRADIENT SERIES FACTOR (A/G)   |
|-----------------------------------------------|-----------------------------------------------|----------------------------------------------------|--------------------------------|

## APP. C] COMPOUND INTEREST FACTORS-CONTINUOUS COMPOUNDING

## COMPOUND  INTEREST  FACTORS  -  CONTINUOUS  COMPOUNDING NOMINAL  INTEREST  RATE  =  2 5 . 0 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR ( F / P)   | UNIFORM- SERIES CAPITAL-RECOVERY FACTOR ( A l p )   | GRADIENT SERIES FACTOR (A/G)   |
|--------------------------------------------------|-----------------------------------------------------|--------------------------------|

## COMPOUND  INTEREST  FACTORS -CONTINUOUS  COMPOUNDING NOMINAL  INTEREST  RATE = 3 0 . 0 0   PERCENT

| N   | SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR (F/P)   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR ( F / A)   | UNIFORM-SERIES CAPITAL-RECOVERY FACTOR ( A l p )   | GRADIENT SERIES FACTOR (A/G)   |
|-----|-----------------------------------------------|--------------------------------------------------|----------------------------------------------------|--------------------------------|

## APP.  C] COMPOUND INTEREST FACTORS-CONTINUOUS COMPOUNDING

## COMPOUND  INTEREST  FACTORS  -  CONTINUOUS  COMPOUNDING

## NOMINAL  INTEREST  RATE  =  4 0 . 0 0 PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR ( F / P)   | UNIFORM- SERIES COMPOUND-AMOUNT FACTOR ( F I A )   | UNIFORM- SERIES CAPITAL-RECOVERY FACTOR (A / P   | GRADIENT SERIES FACTOR (A/G)   |
|--------------------------------------------------|----------------------------------------------------|--------------------------------------------------|--------------------------------|

## COMPOUND  INTEREST  FACTORS  -  CONTINUOUS  COMPOUNDING

## NOMINAL  INTEREST  RATE  =  5 0 . 0 0   PERCENT

| SINGLE-PAYMENT COMPOUND-AMOUNT FACTOR ( F / P)   | UNIFORM-SERIES COMPOUND-AMOUNT FACTOR ( F / A)   | GRADIENT SERIES FACTOR ( A / G)   |
|--------------------------------------------------|--------------------------------------------------|-----------------------------------|

## Appendix  D

## Annual versus Continuous Uniform Payment Factors

| NOMINAL INTEREST RATE, O h   | RATIOOF ANNUALTO CONTINUOUSUNIFORMPAYMENTS (A/&)   |
|------------------------------|----------------------------------------------------|

Accelerated cost-recovery system (ACRS), 116

Accelerated depreciation, 107, 112

Accumulated depreciation, 105

Adjusted cost, 105

Annual compounding, 12

Annual depreciation, 105

Assets, long-term, 113

short-term, 113

Attainable rate, 77

Base tax rate, 112

Before- and after-tax economic analysis, 118

Benefit-cost ratio (BCR), 69

Bonds, 51

Book value, 105

Budget allocation, 78

Capital, cost of, 50

Capital gains (losses), 113

Capital recovery (CR), 60

Capitalized equivalent (CE), 60

Cash flow, 5

diagram, 5

discounted (DCF), 66

Challenger versus standard, 79

Comparative use value (CUV), 95

Composite depreciation, 110

Composite interest rate, 3

Compound interest, 2

factors for annual compounding (tables), 135

factors for continuous compounding (tables), 161

Compounding, annual, 12

continuous, 40

discrete, 31

periodic, 31

Contingent projects, 81

Continuous compounding, 40

with continuous payments, 40

with discrete payments, 40

uniform payment factors (table), 185

Cost, adjusted, 105

Cost of   capital, 50

Cost recovery system, accelerated, 116

CR (see Capital recovery)

CUV (see Comparative use value)

DCF (see Cash flow, discounted)

Decelerated depreciation, 112

Declining-balance depreciation, 106

Depreciable assets, 105

## Index

Depreciation, 105

accelerated, 107, 112

accumulated, 105

additional first-year,  1 1 1

annual, 105

choice o f   method, 117

comparison of  methods, 112

composite, 110

decelerated, 112

declining-balance,  106

double-declining-balance,  107

group, 110

and income taxes, 114

sinking-fund,  109

straight-line,  105

sum-of-years' -digits, 108

unit, 110

Descartes' rule  of  signs, 67

Discounted cash flow (DCF), 66

Discrete, periodic compounding, 31

Do-nothing alternative, 78

Double-declining-balance  depreciation, 107

Economic analysis, before- and after-tax, 118

Economic equivalence, 48

Economic feasibility study, 127

background, 127

cost estimation, 130

estimation o f   revenues, 132

financing, 132

market study, 128

project engineering, 129

Economic life of   an asset, 92

Effective interest rate, 31, 40

annual, 32

Equal service periods, 96

Equivalence, 48

Equivalencing factor, 48

Equivalent uniform annual cost (EUAC), 60

Equivalent uniform annual series (EUAS), 59

Fair market value, 52

First-year depreciation, additional,  111

Future worth, 3, 58

Gradient series factor, 15

Group depreciation, 110

Incremental rate of  return, 79

Independent projects, 78

## INDEX

Inflation, 3

Interest, 1

Interest factors, relations among, 23

Interest period, 2

Interest rate,  1

composite, 3

effective, 40

effective annual, 32

nominal, 40

nominal versus effective, 31

as unknown, 26

Interpolation, linear, 24

Investment tax credit, 1 1 1

Joint projects, 81

Linear interpolation, 24

Long-term assets, 113

Minimum attractive rate of  return (MARR), 51, 77

Money, time value of, 2

Mutually exclusive projects, 78

Net present value (NPV), 58, 66

Net present worth (NPW), 58

Nominal versus effective interest rate (table), 159

Nominal and effective interest rates,

continuous compounding, 40

Nominal interest rate, 31, 40

Nondepreciable assets, 105

NPV (see Net present value)

NPW (see Net present worth)

Number of  years as unknown, 24

Payback period, 68

Present value, 57

Present worth, 3, 57

Principal, 1

Project selection, 78

Projects, contingent, 81

financially interdependent, 81

independent, 78

joint, 81

mutually exclusive, 78

Rate, attainable, 77

target, 77

Rate of   return (ROR), 66

incremental, 79

uniqueness and sign-reversals, 67

Reinvestment fallacy, 81

Relationships  among interest factors, 23

Replacement assumption

for unequal-lived assets, 97

Replacement decisions, 92

Retirement decisions, 92

Retirement/replacement decisions, 94

ROR (see Rate of  return)

Salvage value (scrap value), 60, 105

Secondary analysis, 68

Short-study-period method, 96

Short-term assets, 113

Sign-reversal, multiple, 67

single, 67

Simple interest, 1

Single-payment, compound-amount factor, 12

Single-payment, present-worth factor, 12

Sinking-fund depreciation, 109

Standard versus challenger, 79

Stock, 50

Straight-line depreciation, 105

Sum-of-years' -digits depreciation, 108

Sunk cost, 92

Surtax rate, 112

Target rate, 77

Tax credit, 111

Tax rate, base, 112

Tax shield, 114

Taxes, 4

Time value of  money, 2

Unequal-lived assets, replacement assumption for, 97 Unequal service periods, 96 Uniform-series, capital-recovery factor, 14 compound-amount factor, 12 present-worth factor, 15 sinking-fund factor, 13 Unit depreciation,  110 Unknown interest rate, 26 Unknown number of  years, 24

Useful life, 105

## SCHAUM' $ SOLVED PROBLEMS SERIES

- H Learn the best strategies for solving tough problems in step-by-step detail
- H Prepare effectively for exams and save time in doing homework problems
- H Use the indexes to  quickly locate  the  types  of problems  you need the most help solving
- H Save these books for reference in other courses  and even for your professional  library

I

I

I

I

I

I

I

I

I

I

I

1

I

To order, please check the appropriate box(es) and complete the following coupon.

a 3000 SOLVED PROBLEMS IN BIOLOGY ORDER CODE 005022-81$16.95 406 pp.

a 3000 SOLVED PROBLEMS IN CALCULUS ORDER CODE 041  523-41$19.95  442 pp.

a 3000 SOLVED PROBLEMS IN CHEMISTRY ORDER CODE  023684-4/$20.95  624 pp.

a 2500 SOLVED PROBLEMS IN COLLEGE ALGEBRA &amp; TRIGONOMETRY ORDER CODE  055373-4/$14.95  608 pp.

0 2500 SOLVED PROBLEMS IN DIFFERENTIAL EQUATIONS ORDER CODE  007979-d$19.95 448 pp.

0 2000 SOLVED PROBLEMS IN DISCRETE MATHEMATICS ORDER CODE  03803 1-7616.95  412 pp.

I

a 3000 SOLVED PROBLEMS IN ELECTRIC CIRCUITS ORDER CODE  045936-3/$21.95  746 pp.

a 2000 SOLVED PROBLEMS IN ELECTROMAGNETICS ORDtR CODE  045902-9/$18.95  480 pp.

a 2000 SOLVED PROBLEMS IN ELECTRONICS ORDER CODE  010284-81519.95  640 pp.

a 2500 SOLVED PROBLEMS IN FLUID MECHANICS &amp; HYDRAULICS ORDER CODE  019784-9/$21.95  800 pp.

a 1000 SOLVED PROBLEMS IN HEAT TRANSFER ORDER CODE  050204-8/$19.95  750 pp.

a 3000 SOLVED PROBLEMS IN LINEAR ALGEBRA ORDER CODE 038023-6/$19.95  750 pp.

2000 SOLVED PROBLEMS IN ORDER  CODE 037863-0/$19.95  406 pp. Mechanical Engineering THERMODYNAMICS

a 2000 SOLVED PROBLEMS IN NUMERICAL ANALYSIS ORDER CODE  055233-9/$20.95  704 pp.

I

a 3000 SOLVED PROBLEMS IN ORGANIC CHEMISTRY ORDER CODE  056424-81$22.95  688 pp.

a 2000 SOLVED PROBLEMS IN PHYSICAL CHEMISTRY ORDtR CODE  041 7 16-4/$21.95  448 pp.

I

a 3000 SOLVED PROBLEMS IN PHYSICS ORDER CODE 025734-51$20.95  752 pp.

I

a 3000 SOLVED PROBLEMS IN PRECALCULUS ORDER CODE  055365-31$16.95 385 pp.

a

800 SOLVED PROBLEMS IN VECTOR MECHANICS FOR ENGINEERS Vol I:  STATICS ORDER CODE  056582-11$20.95  800 PP.

700 SOLVED PROBLEMS IN VECTOR MECHANICS FOR ENGINEERS Vol 1 1 :   DYNAMICS ORDER CODE 056687-91$20.95  672 pp.

## ASK FOR THE SCHAUM'S SOLVED PROBLEMS  SERIES AT YOUR LOCAL BOOKSTORE OR  CHECK THE APPROPRIATE BOX(ES) ON THE PRECEDING PAGE AND MAIL WITH THIS COUPON TO:

MCGRAW-HILL, INC. ORDER PROCESSING S-1 PRINCETON ROAD HIGHTSTOWN, NJ 08520

OR CALL 1-800-338-3987

NAME  (PLEASE PRINT LEGIBLY OR TYPE)

ADDRESS  (NO P.O.  BOXES)

CITY

STATE

ZIP

ENCLOSED IS

0 A CHECK

0 MASTERCARD

0 VISA

0 AMEX

(J ONE)

ACCOUNT #

EXP.  DATE

SIGNATURE

MAKE CHECKS PAYABLE TO MCGRAW-HILL, INC.  PLEASE INCLUDE LOCAL SALES TAX AND $1.25 SHIPPING~HANDLING PRICES SUBJECT TO CHANGE WITHOUT NOTICE AND MAY VARY OUTSIDE THE U.S. FOR THIS INFORMATION, WRITE TO THE ADDRESS ABOVE OR CALL THE 800 NUMBER.