## PREFACE

## General Character and Purpose of the Instructor's Manual

- Detailed solutions of the even-numbered problems.

This Manual contains:

(ID General comments on the purpose of each section and its classroom use; with mathematical and didactic information on teaching practice and pedagogical aspects. Some of the comments refer to whole chapters (and are indicated accordingly).

## Changes in Problem Sets

The major changes in this edition of the text are listed and explained in the Preface of the booka They include global improvements by updating and steamlining chapters as wel these changes on the problem sets are as follows.

() Balancing by extending problem sets that seemed too short and contracting others that were too adjusting the length to the relative importance of the material in section; s0 that important issues are reflected sufficiently well not only in the text but also in the problems. Thus;, the danger of overemphasizing minor and ideas is avoided as much as possible. long, techniques

The problems have been changed:. The large total number of over 4000 problems has been retained; increasing their overall usefulness by the following;

(D Simplification by omitting a small number of very difficult problems that appeared in the previous edition; retaining the wide spectrum ranging from simple routine lems to more sophisticated engineering applications; and into account the "algorithmic thinking" that is developing with computers. prob taking along

This has again been achieved by the làrge number of over 600 worked-out examples in the text and by inproblems closely related to those examples. cluding

These changes in the problem sets will help students in problems as well as in gaining a better understanding of practical aspects in the text: It will also enable instucn tors to explain ideas and methods in terms of examples supplementing and illustrating theoretical discussions Or even replacing some of them if s0 desired. solving

(Y) Addition of TEAM PROJECTS, CAS PROJECTS, and WRITING PROJECTSse hose cole is explained in the Preface 0f the book under Big Changes:

## "Show the details of your work.:

This request repeatedly stated in the book applies to all the problem sets. Of course, it is intended to prevent the student from simply producing answers by a CAS instead of trys to understand the underlying mathematics. ing

## Orientation on Computers

Comments on computer use are included in the Preface of the book: Software systems are listed in the book subsequent to Contents and at the beginning of 17 on numerical methods. Chap.

ERWIN KREYSZIG

## Part A. ORDINARY DIFFERENTIAL EQUATIONS

## CHAPTER 1 First-Order Differential Equations

Direction fields are now discussed much earlier; in Sec. 1.2. This~ 'geometrical" itative" approach to differential equations and "qualof may provide a better conceptual understanding equations and solutions. The graphical power of a CAS will be helpful in this contexg

## Major Changes

The second major concerns the combination of related solution methods. Solution by separation and solution by reduction to separable form now in tion (Sec. 1.3) Similarly, exact appear a single secequations and integrating factors are both discussed in the same section (Sec. 1.5). change

Team Projects and CAS Projects are included in most problem sets.

## SECTION 1.1. Basic Concepts and Ideas; page 2

Background Material For the whole chapter we need integration formulas and tech niques; which the student should review.

Purpose. To give the student first impression of what a differential what we mean by solving it. equation is and

## General Comments

This section should be covered relatively rapidly to get quickly to the actual solution meth ods in the next sections.

If an example of a partial differential equation is wanted in passing, tion Laplace' s equa-

<!-- formula-not-decoded -->

Problem Set 1.1 is supposed t0 help the student with the tasks of y f(x) by calculus; particular solutions from given general solutions; Setting up a differential equation for a given function as solution, Gaining a first experience in modeling, by one OI two problems, Solving Finding doing Gaining without wasting time on matters that can be done much faster, once systematic are available. methods

first impression of the importance of differential equations;

## Comment on &lt;General Solution? and sSingular Solution"

of the term 'general solution is not uniform in the literature. Some books term to mean a solution that includes all solutions; use the that is, both the particular and the sinfrequently quite Usage

difficult to prove that a formula includes all solutions; hence this definition of a general solution is rather useless in practice. Second;, linear differential equations (satisfying rather general conditions on the coefficients) have no singular solutions (as mentioned in the text), s0 that for these equations a general solution as defined does include all solutions. For the latter reason; some books use the term *general solution' for linear equations only; but this seems very unfortunate.

## Comment on Example 2

This also illustrates that open intervals generally are the appropriate domains of definition of solutions.

Theoretically inclined students may show (a) by differentiation; (b) directly from the differential   equation;  that   the solution cannot be continued to the closed interval ~l2x = 1, where the function is still continuous; but no longer differentiable.

## SOLUTIONS TO PROBLEM SET 1.1, page 8

10. yy' =0 by implicit differentiation and division by 2

<!-- formula-not-decoded -->

12. From the solution and the initial condition; 0 + 1 = c. Answer: + y4 = 1 (y &gt; 0) The figure shows the portion of this curve in the first quadrant; together  with a quarter-circle for comparison. 49

Section 1.1. Problem 12

<!-- image -->

<!-- formula-not-decoded -->

- 1.
20. = 1/2, k = 0.192 541, e -k 0.825 after 1 3.012 after 365 10-31 days. e-3.6k day,
- 1/2, k = In (1/2)/18000 ~0.000038 508. Answer: 0.26y Since the decay is exponential, 36000 2 18000 would give (yo/2)/2 0.25y
22. y" = g. By two integrations y' = 0 because the stone starts from rest, =y = gt2/2 + c2 with C2 = 0 because s(0) = 0, the stone starts at = 0.
26. y = 0.08; y(l) equals

1080.00, and equals

1469.33,

1082.43 ,

1485.95,

1083.28,

1491.76,

1083.29

1491.82.

The last two numbers in each line differ only slightly from each other, as claimed.

## SECTION 1.2. Geometrical Meaning of y' = f(x; y) Direction Fields, page 10

Purpose  To give the student a feel for the nature of differential equations and the eral behavior of fields of solutions: This amounts to a genclarification before restricted to relatively small albeit important classes of equations. This approach is becoming increasingly important; especially because of the graphical power 0f computer softwage .It is the analog of conceptual studies of the derivative and integral in calculus as to formal techniques of differentiation and integration. opposed being

These could be omitted since students sometimes confuse them with solutions. In the computer approach to direction fields no longer play a role. they

## Comment on Isoclines

## Comment on Order of Sections

This section could equally well be presented later in 1, perhaps after one or two formal methods of solution have been studied. Chap.

## SOLUTIONS TO PROBLEM SET 1.2, page 12

<!-- formula-not-decoded -->

14. The exact solution is y 1). This is not part of the problem because the solution is obtained by separating variables (which is discussed in the next section), dyly? y = = ~1 from the initial condition. ~dx,
12. y = c = 1,a bell-shaped curve ce-r212
16. s'(t) lls(t). Exact solution = problem; it is obtained by separating variables; s ds = dt, s2/2 =t+ ã,s2 = 2t + c, and s(0) = 1 gives c = 1. Now take square roots
18. The main points of this problem are to realize that a direction field can give clusions. We can write it

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We now see that y =4 is a solution. For x = 0 Eq. (A) gives

<!-- formula-not-decoded -->

For 0 y(o) 4 both factors on the right are positive; 80 that y' (0) is positive. Similarly, as as 0 &lt; we get y' (x) &gt; 0, that is, an increasing curve. When y(x) &gt; 4, then y (x) 0 and the curve decreases . long

- (b) y ce-2æ is monotone; and the simple direction field may help the student y const, property that should also become visible if the field is produced by computer; without reference to isoclines.
20. CAS PROJECT: (a) The point is that enlargement of subregions may give a more accurate impression.
- (c) The impression of circles should come out very nicely.
- (d) y' = ~xldy

## SECTION 1.3. Separable Differential Equations, page 14

Purpose. To familiarize the student with the first "big" method by solving simple equations as well as some that require more skill, with initial value problems (which are simple to solve; once the general solution has been found) . Applications of separable equations follow in the next section: along

## Comment on Example 1

From the implicit solution we can get two solutions explicit

<!-- formula-not-decoded -->

representing semi-ellipses in the upper half-plane; and

<!-- formula-not-decoded -->

representing semi-ellipses in the lower half-plane. [Similarly , we can two explicit solutions x(y) representing semi-ellipses in the left and right half-planes, respectively:] larly for x' (y) on the y-axis. get

## Comment on Separability

An analytic function f(x, y) in a domain D of the xy-plane can be factored in D, f(x;y) = g(x)h(y); if and only if in D,

[D. Scott; American Math. Monthly 92 (1985), 422-23]. Simple cases are easy to decide; but this may save time in cases of more complicated equations, some of which may perhaps be of practical interest.

## SOLUTIONS TO PROBLEM SET 1.3, page 18

<!-- formula-not-decoded -->

- 10; u2 + 4. We may set v/2 = 4(w? + 1). By integration; arc tan w = 2x + c, W tan (2x + c) = vl2 = yl2 + 2x. Answer: y ~4x + 2tan (2x + c) y +
8. x(u + xu') = xu + X, u' x = 1, u = = In |x| + c = ylx. Answer: y x(ln |x| + c)
12. yy' = =X, y?/2 = = c. From this and the initial condition; 12 + (V)? = 4 = C. Answer: x2 + y? = 4, a circle; of radius 2

49

16. By separation of variables; dyl(l + 4y2) = dx. We may set 2y By substitution;
14. By integration; y4/4 + x4/4 = c. From this and the initial condition; 1/4 + 0 = c. Answer:

<!-- formula-not-decoded -->

hence y zI2 2 tan (2x + c). From this and the initial condition; 0 = 0. Answer: y 2 tan 2x.

18. By separation; integration; and exponentiation;

<!-- formula-not-decoded -->

From this and the initial condition; r(O) = c = 2.5. Answer: r = 2.5e-t?

20. Substitute ylx and simplify to get

<!-- formula-not-decoded -->

By separation and integration;

<!-- formula-not-decoded -->

Hence by taking roots,y = =x + xIVc ~ x2 . From this and the initial condi-= 1 +

<!-- formula-not-decoded -->

22. We substitute ylx = u,y = xu,y' = u + xu" and simplify , obtaining

<!-- formula-not-decoded -->

From this and the initial condition y(l) = T we have u(1) = TT, 0 = sin T = 1 + c; c = ~1. Answer: y

24. = x + y - 2,y' =u = v2 + 1 can be separated, dv = dx, =
2. is undefined at the origin.

- (c) y Here the student should learn that c must not appear in the differential equation. ylx = c,y'Ix = 0, y = ylx. ylx?
- = ~ylx
- (d) The right sides ~xly and ylx are the y of the curves. Orthogonality is important and will be discussed further in Sec. 1.8. slopes

## SECTION 1.4. Modeling: Separable\_Equations, page 19

Purpose; This section contains some typical applications to choose from; depending on students' interests and background. serve to convince the student of the practical importance of differential  equations: Similarly, Problem Set 1.4 contains much more material than one would ordinarily wish to discuss. They

## Comment on Example 4

often possible to stay within first-order equations; as in this case.

## Comment on Footnote 4

Newton conceived his method of fluxions (calculus) in 1665-1666, Philosophiae Naturalis Principia Mathematica was his most influential work.

Leibniz invented calculus independently in 1675 and introduced notations that were culus appeared in 1684.

## SOLUTIONS TO PROBLEM SET 1.4, page 23

2. y" =k (constant acceleration). By two integrations; y we used the given initial After 50 sec we have y(5o) = 1250k + 500 2000. This gives k = 1.2. By differentiation and substitution, y' (50) = 5Ok + 10 = 70 meterslsec 252 kmhhour. speed.
4. Acceleration y" = 7t. Hence y = = = 350 (initial speed of further flight end 7000/6 = 1167 (height reached after the 10 sec) At the peak, v 0, s = 0, say; thus for the further flight = = 4.9t2, v(t) 9.8t = 350 (see before). This gives the further flight time to the peak t = t1 = 350/9.8 35.7 and the fur ther height s(t1) = 4.9t12 6245. Answer: 1167 + 6245 7412 [m] speed (gI2)t2
6. e-k.10 = 0.069315, e-kto 0.01 (1% is the remaining moisture). 1 Answer: to In 100 = 66.4 min; practically 1 hour . k
8. The acceleration is a = 9 106 meterslsec? , and the distance traveled is 5.5 meters. This is obtained as follows. Since s(0) = 0 (ie, count time from the instant the particle enters the accelerator), we have for a motion of constant acceleration we

<!-- formula-not-decoded -->

and the velocity is

From the given data thus obtain v(0) = b = 103 and we

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

so that

Finally, with this a and that b, from (A) get we

<!-- formula-not-decoded -->

10. At the earth' s surface the minimum velocity for escape is vo2, and from (11) and (12) in Example 4 we see that then the square of the velocity at any distance r from the center of the earth is

<!-- formula-not-decoded -->

so that at the of separation ro = R + 1000 (i.e. 1000 km above the earth' $ surface) the projectile has the velocity point

<!-- formula-not-decoded -->

This is the minimum velocity of escape at the separation point.

- 12 AA ~kAAx (A amount of incident light; AA = absorbed light, Ax thickness; constant of   proportionality). Let Ax 0. Then A ~kA. Hence A(x) Aoe-kæ is the amount of light in a thick layer at depth x from the surface of incidence.
14. Let y(t) be the amount of salt in the tank at time t. Then each contains gallon

= 2At (y/400) ~yi2oo, y ~0.OO5y, Y(t) = 1OOe-0.3 = 74 [Ib]

16. Let V = V(t) be the volume and r = r(t) the radius. Then the area is A = 4ur2. The rate of change dVIdt is proportional to A; thus by the chain denoting the constant of proportionality by k, rule,

<!-- formula-not-decoded -->

At t = 0 the radius is 1 and after 2 months, it is ž. Now dividing the previous equation by 4ur2 and integrating; we obtain

<!-- formula-not-decoded -->

and that condition can be used to find k and c,

<!-- formula-not-decoded -->

Hence k = ~ 1/4, and from this and the condition that the ball have radius 0.05 cm; we obtain

<!-- formula-not-decoded -->

The answer is 3.8 months .

18. W = mg in Fig. 12 is the weight (the force of attraction on the body). Its component parallel to the surface is mg sin œ, and N mg cos œ Hence the friction is cos œ, and it acts against the direction of motion. From this and Newton' s second law, noting that the acceleration is dvldt (v the velocity), we obtain acting 0.2mg

<!-- formula-not-decoded -->

The mass m drops out; and two integrations give

<!-- formula-not-decoded -->

Since the slide is 10 meters the last equation with s long,

<!-- formula-not-decoded -->

From this we obtain the answer

<!-- formula-not-decoded -->

- = t(h) into v(t); thus

<!-- formula-not-decoded -->

- (b) This is a typical exercise in modeling: It is remarkable that A and B(h) in (14) are unspecified, 80 that (14) could serve as a model for various types of tanks

decreases by Ah during a short time\_At; and this must equal AvAt, which, by Torricelli' s law equals A 0.600V2ghAt. By equating the two expressions; and

<!-- formula-not-decoded -->

Dividing by At and letting At 0 gives (14)

- This is the simplest case because B is constant (independent of h), and we can easily solve (14) by separation of variables and integration,

<!-- formula-not-decoded -->

- (d) A/B (1/100)2, Vh(o) V1so = 12.25 = c, and the tank will be empty at t satisfying

<!-- formula-not-decoded -->

## SECTION 1.5. Exact Differential Equations. Integrating Factors; page 25

Purpose.  This is the second "big" method in this chapter, after separation of variables; and also applies to equations that are not separable.  The criterion (5) is basic. Simpler cases are solved by inspection; more involved cases by integration, as explained in the text.

## Comment on Footnote 12

Condition (5) is equivalent t0 (6") in Sec. 9.2, which is equivalent to (6) in the case of two variables x, y. Simple connectedness of D follows from our assumptions in Sec. 1.5. Hence the differential form is exact by Theorem 3, Sec. 9.2, part () and part (a), in that order

## Method of Integràting Factors

This greatly increases the usefulness of solving exact equations. It is important in itself as well as in connection with linear equations in the next section. Problem Set 1.5 will help the student skill needed in finding integrating factors. Inasmuch, the method has somewhat the flavor of tricks, but on the other hand, Theorems 1 and 2 show that at least in some cases one can proceed systematically\_and one of them is precisely the case needed in the next section. gain

## Comment on Notation in Exàmple 5

The standard notation for (sin y)? is sin? y, hence sin y? clearly means sin (y2); the parentheses are superfluous; but we wanted to help students . poorer

## SOLUTIONS TO PROBLEM SET 1.5, page 31

- ~(2x dx + 2y dy)l(x? + y2)2 = 0, concentric circles
6. cosh y dx + sinx sinh y dy 0. The curves u = const g0 vertically to infinity as sin x - 0, as x - 0, +T, see the figure. upward

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 20.

Now y(O) = = c. Hence c = 1. Answer: e2x sin @y = 1. )y = )r shows exactness. By integration; (2xyer?)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

22. Equation (9) becomes s4 + +4 = const; see the figure in the solution to Prob. 12 of Sec. 1.1 in this Manual.
24. (xy)-1 dy x2 dx = 0 has the integrating factor F = y, giving

<!-- formula-not-decoded -->

which is exact because

Now (A) implies so that

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

as claimed, but y = 0 is not a solution of the original equation.

26. y cos (x + y) dx + [ycos (x + y) + sin (x + y)] dy = 0 is exact because

<!-- formula-not-decoded -->

By inspection or systematically,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

28. The new equation is

It is exact,

The general solution is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

2 cos 2x cos y dx sin 2x sin y dy = 0

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

It is exact;

general solution is

32. F y2 gives the new equation

<!-- formula-not-decoded -->

which is exact and has the general solution x2y3 const.

34. F = e22 gives the new equation

This equation is exact;

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The general solution is cos y = c. e2

36. F

is exact! We now obtain

<!-- formula-not-decoded -->

The general solution is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

etc\_ can be solved by inspection; separation; Or as exact equations.

40. CAS PROJECT. () Theorem 1 does not apply. Theorem 2 gives

<!-- formula-not-decoded -->

The exact equation is

as one could have seen by inspectionany equation of the form

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) The vertical asymptotes that some CAS programs draw disturb the graph. From the solution in (b) the student should conclude that for each initial condition y(xo) = yo with y # 0 there is a unique particular solution because from (b)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SECTION 1.6. Linear Differential Equations. Bernoulli Equation; page 33

Purpose. Linear equations are of great practical importance; as Problem Set 1.6 illustrates (and even more s0 are higher order linear equations in 2). We show that the homogeneous equation is easily separated and the nonhomogeneous equation is solved, once and for all, in the form of an integral (4) by the method of integrating factors: Of course, in simpler cases one does not need (4), as our examples illustrate. Chap.

## Comment on Notation

We write

<!-- formula-not-decoded -->

p(x) seems standard. r(x) suggests "right side. The notation

<!-- formula-not-decoded -->

used in are not concerned with higher order equations) would be short-sighted here because few weeks later in 2 order equations Chap.

<!-- formula-not-decoded -->

where 'we need q(x) on the left;, thus in a quite different role (and on the right we would have to choose another letter different from that used in the first-order case).

## Comment on Content

Bernoulli?s equation appears occasionally in practice; s0 the student should remember how to handle it.

Input and output have become common terms in various contexts, s0 we thought it a good place to mention them here.

Riccati and Clairaut equations are less important than Bernoulli' s, so we have them in the problem set; will not be needed in our further work. put they

Problems 23-30 express the properties that make linearity important; and their counterparts will, of course, reappear in Chap. 2

## Comment on Footnote 14

Eight members of the Bemnoulli family became known as mathematicians; for more details, see p. 220 in Ref. [2] listed in Appendix 1.

## SOLUTIONS TO PROBLEM SET 1.6, page 38

4. y = + 1.25
6. y = + 4 Separation of variables seems simplest here, y ~(y 4)x; then divide by y 4, etc.
8. y = ce-4r + 17cos x + 17 sin x The particular solution can be obtained by substiy = a cos x + b sin x, which leads to a 4b and 17b 1 by comparing with cos x on the right of the given equation: This avoids the integration. tuting
12. y =
14. x2y 4 = (x2y)' = sinh 5x; now integrate to get 2xy

<!-- formula-not-decoded -->

These problems illustrate that the integral solution formula (4) can be avoided in many cases.

16. y = x is the general solution: The initial condition gives c =1
18. This homogeneous linear equation has the general solution y c sec x; and c = from the initial condition.
20. y = e-22 '(c llx) is the general solution; c 1 from the initial condition.
22. y = cx-4 + is the general solution. The initial condition gives c = 1.
24.  Problems 23-30 require proofs by substitution; so they are basically very similar. By working these problems the student should become aware of the difference between homogeneous and nonhomogeneous equations. This will also serve as a preparation for the corresponding theorems for higher order equations; some of which are important in constructing general solutions of nonhomogeneous equations from those of homogeneous equations.
30. y' + Poy ~Poly rolpo), y Ily rolpo) Po, In (y rolpo) = ~Pox + ã,y = rolpo + ce-Por
32. u = y2, yy' + 2u = ~2x; hence

<!-- formula-not-decoded -->

34. This differential equation can simply be solved by separating variables,

<!-- formula-not-decoded -->

As an alternative, we can regard it as a differential equation for the unknown function x = x(y) and solve it by formula (4) with x and y interchanged.

36. Take x as the dependent variable to get

<!-- formula-not-decoded -->

and by (4) with x and y interchanged,

<!-- formula-not-decoded -->

38. the given transformation y2 = z we obtain the linear differential equation Using

<!-- formula-not-decoded -->

which we can solve by (4) with z instead of y,

<!-- formula-not-decoded -->

From this we obtain y = Vz

40. y + y = 1 (atl12). Solution:

<!-- formula-not-decoded -->

where y(0) = 2 gives 1.936, s0 that we get the answer

<!-- formula-not-decoded -->

42. From and the initial condition v(0) 0 we obtain

<!-- formula-not-decoded -->

By integration; using y(O) = 0,

<!-- formula-not-decoded -->

From v(t) we calculate that v Ucrit when

<!-- formula-not-decoded -->

This gives y(tcrit) = 105 meters, approximately .

44. The given equation y x3(y x)? + x-ly shows immediately that y x is a sOlution. It is a Riccati equation; its standard form is

<!-- formula-not-decoded -->

as follows by direct calculation.

From w =y - x we have y = w + x, and from the given equation we get

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

tution

Answer:

<!-- formula-not-decoded -->

This linear equation can now be solved by (4),

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- Ily'2) Now (A) y' =0 gives y = cx + a and a = Ilc by substitution; a family of straight lines: (B) x = Ily' 2 gives by integration y = +ã and ã = 0 by substituting y and y' into the given equation, hence y 2Vx; the singular solution; to which the straight lines in (A) are tangent. 2x1/2 .
48. y = ax + b intersects the axes at (~bla, 0) and (0, b). Length 1 implies that b = y and we the equation given in the problem. We write y = s. Then the singular solution results from x ~g'(s) = (1 + ,2)-3/2. From this and the differential equation; by simplification; get

The result is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

parametric representation of the astroid (see the figure). Adding these two expres sions, each raised to the power 2/3, we the formula in the problem. get

Section 1.6. Astroid in Problem 48

<!-- image -->

## SECTION 1.7. Modeling: Electric Circuits; page 41

order equation and to discuss the currents for the simplest inputs (constant and sinusoidal) . This is a major standard application of linear equations and will help all students not just electrical engineers ~to further experience in modeling. (RLC-circuits; leading to second-order equations, follow in Sec. 2.12) gain

Shorter Courses. Sections 1.7-1.9 may be omitted without interrupting continuity.

## SOLUTIONS TO PROBLEM SET 1.7, page 47

- ô increases with L, studied further in Sec. 2.12, where we show the analogy between mechanical and electrical quantities).
4. Solve (4) algebraically for I' = [Eo RIJIL, and I' &gt; 0 as as Eo/R &gt; I(t), so that I(t) begins to increase when I(0) Eo/R. Similarly, I(0) Eo/R implies that I(t) begins to decrease. long
- 6 For t = 1 and I 0.99Eo/R we have from (5**) with L = 10

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 8. We obtain

and from this,

<!-- formula-not-decoded -->

By (14), Appendix A3.1,

<!-- formula-not-decoded -->

as in (6), and tan ô =

10. TEAM PROJECT. (a) I(t) is continuous. A jump JIL of I' gives a jump J of LI' to the jump of E(t) on the right side of (4) equal
2. (b) I = I1 =1 = (this is better than writing C2e-t which, however; would also work). Now by continuity of I, I2(4) = I1(4) = 1 0.99. cze-(t-4)
3. (c) Here we proceed as in () with letters instead of numbers.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Again; t in the exponent is practical, but we could use t instead. C2 follows from

<!-- formula-not-decoded -->

12. From the first line in (11),

<!-- formula-not-decoded -->

this gives c. Inserting it into the first line, we have

<!-- formula-not-decoded -->

14. Differentiation of (7) gives

<!-- formula-not-decoded -->

Hence I = c(t 200)3 and I(0) = 1 gives c = -1/(8 108), thus

<!-- formula-not-decoded -->

16. We want the time such that Q = Qe-tIRC = 0.01Qo. Hence t = RC In 100 = 4.605RC [sec]
18. 20Q' + 10Q = 30e-3t is the new equation. For the initial condition Q(0) = 0 we obtain the particular solution

<!-- formula-not-decoded -->

Q'(t) = 0.6(-0.5e-tl2 + 3e =0 gives = 6, tm (In 6)/2.5 = 0.717 [sec] and Qm 0.349 [coulomb]. The larger R has caused a smaller Qm at a later time tm: See the figure, where the upper curve corresponds to Prob. 17. e2.5t ~3t)

<!-- image -->

20. TEAM PROJECT. (a) Use (3*), (3). Then from (7)

<!-- formula-not-decoded -->

- (b) This follows from (7). The on the capacitor cannot change abruptly . Hence RI on the left must have a jump of magnitude J, so that I must have a jump JIR. charge

Divide by R and set t = 0

- (c) I(0) = 0 by (a) I' + I = t,I = t - 1 + I(2) = 1 + dEldt bas a jump ~2 at t = 2 Hence the current I2 for t = 2 satisfies

<!-- formula-not-decoded -->

$$Solution: I2 =$$

## SECTION 1.8. Orthogonal Trajectories of Curves. Optional, page 48

Purpose. To show that families of curves F(x, y; c) = 0 can be described by differential equations y~ = l/f(x; y) produces as general solution the orthogonal trajectories. This is a nice application; which may also help the student more self-confidence; skill; and a deeper understanding of the nature of differential equations. We leave this section optional, for reasons of time. This will cause no gap. gain

## SOLUTIONS TO PROBLEM SET 1.8, page 51

2. (x c)? + (y - c32 \_ 4 =0 gives a circle of radius 2 with center (xo, Yo) (c, c3), and we see that the coordinates of the center satisfy y Xo3 as required.
6. From the given formula we arc tan y = X + Differentiating and applying the chain rule, we obtain get
4. y 1/2. This is the of these parallel straight lines. slope

<!-- formula-not-decoded -->

8. x-4y = c. By differentiation; ~4x-5y + x-4y' = 0. Algebraic solution for y gives the answer

<!-- formula-not-decoded -->

10. From the given representation we get

<!-- formula-not-decoded -->

This is the differential equation of the given family of curves. From this we have the differential equation of the orthogonal trajectories

<!-- formula-not-decoded -->

Separation of variables and integration gives

<!-- formula-not-decoded -->

Taking exponentials and solving for x as a function of y, we obtain

<!-- formula-not-decoded -->

These are bell-shaped curves\_note that in Sec. 1.3 the roles of x and y are inter changed.

12. y llx gives for the orthogonal trajectories y

<!-- formula-not-decoded -->

Note that here we have congruent curves as well as congruent orthogonal trajectories.

- we obtain

<!-- formula-not-decoded -->

This is the differential equation of the given curves. Hence the differential equation of the orthogonal trajectories is

<!-- formula-not-decoded -->

By separation of variables and integration obtain we

Exponentiation gives the answer

<!-- formula-not-decoded -->

16. Differentiating the given formula; we obtain

<!-- formula-not-decoded -->

This is the differential equation of the given hyperbolas. Hence the differential equation of the orthogonal trajectories is

<!-- formula-not-decoded -->

Separation of variables and integration gives

<!-- formula-not-decoded -->

Answer: The hyperbolas x2 = y? are the orthogonal trajectories of the given hyperbolas.

18. = 2c by algebra. By differentiation;

<!-- formula-not-decoded -->

Hence the equation of the trajectories is

<!-- formula-not-decoded -->

To solve it for x x(y), set v xly and separate.

<!-- formula-not-decoded -->

which gives

<!-- formula-not-decoded -->

20. I)ly = 2c by algebra; 2xly = 0. Now replace and multiply by [(r2 (x2 y?Ix?:

<!-- formula-not-decoded -->

Integration now gives

<!-- formula-not-decoded -->

Multiply by x to get the desired final formula

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

= 0 gives dyldx and this must equal uyluz (see Prob. 23)

Differentiating UI = we obtain Uy'

and by taking exponentials;

<!-- formula-not-decoded -->

By integration with respect to y,

<!-- formula-not-decoded -->

where the 'constant" of integration k = k(x) depends on x because we are dealing with partial derivatives. From this and the second Cauchy-Riemann equation;

<!-- formula-not-decoded -->

Hence we must have k(x) = 0, and k = ã = const. Answer: e" sin y C*

26. TEAM PROJECT. (a) The is that the student should learn to summarize the essential facts in a given more detailed presentation. point
2. braically for y' we obtain the differential equation of the given curves

<!-- formula-not-decoded -->

This involves the constant k 2 b2/a2; hence we are dealing with infinitely many families; each corresponding to some value of k. The differential equation of the orthogonal trajectories is

<!-- formula-not-decoded -->

By separation of variables and integration,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We see that a2/b2 has substantial influence on the form of the trajectories. For = b2 we have circles and obtain straight lines as trajectories. a2/b2 2 gives quadratic parabolas. For larger integer values of a2/b2 we obtain parabolas of higher order. Intuitively, the 'flatter" the ellipses are, the more rapidly must the trajectories increase to have orthogonality .

- (c) For hyperbolas we have a minus sign in the given formula. This produces a plus sign in the differential equation for the curves (instead of the minus we had) and minus sign in the differential equation of the trajectories;

<!-- formula-not-decoded -->

By separation of variables and integration we obtain

= 1 we get hyperbolas and for higher values less familiar curves.

- (d) The problem set contains various cases that lead to other families of curves that can be handled easily.

## SECTION 1.9. Existence and Uniqueness of Solutions. Picard Iteration; page 52

Purpose. To give the student at least some impression of the theory that would occupy central position in a more theoretical course on higher level.

Short Courses. This section can be omitted.

## Comment on Iteration Methods

Iteration methods were used rather early in history, but it was Picard who made them pop ular. They are well suited for the computer because of their modest storage demands and usually short programs in which the same Or loops are used many times, with different data. Since integration is generally no difficulty for a CAS, Picards method has gained popularity during the past two decades. loop

## SOLUTIONS TO PROBLEM SET 1.9, page 58

2. General solution y so that 0 does not specify c and we have infinitely many solutions, f(x, y) = Aylx is not defined when x 0 Note that in Prob. 1 we had no solutions; hence both cases, nonexistence or nonuniqueness; may occur. y(o)
2. 4 Separating variables and integrating, we get

<!-- formula-not-decoded -->

and by taking exponentials

<!-- formula-not-decoded -->

From this we can see the answers:

- (a) No solution if y(O) = k # 0 or =k # 0 y(2)
- tradictions to Theorems 1 and 2 because (c)
- (b) Infinitely many solutions if y(O) 0 or y(2) = 0.

<!-- formula-not-decoded -->

is not defined when x = 0 or 2

- are y' = xy ify 2 0 and y ~xy if y = 0. Cex?/2 they
10. PROJECT.  (a) The student should get an understanding of the "intermediate' position of a Lipschitz condition between continuity and (partial) differentiability .
8. The smallest Kis K = (b + 1)2, and bl(b + 1)2 is maximum when b = 1, the value is 1/4. Hence œ 1/4. The solution is y = 1/(2 x).
- (b) It suffices to consider the sine term. The validity of a Lipschitz condition follows from (12) in Appendix A3.1 and the calculation

<!-- formula-not-decoded -->

cusp at O; formally, if x = 0, then

<!-- formula-not-decoded -->

- Here the student should realize that the linear equation is basically simpler than the nonlinear one. The calculation is straightforward because we have

<!-- formula-not-decoded -->

and this implies that

<!-- formula-not-decoded -->

This becomes a Lipschitz condition if we note that the continuity of p(x) for Ix absolute values on both sides of (A) now gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

18. The solution is y = x3 . The Picard iterates are linear combinations of powers of In x,
2. 16 y = (x ~ 1)2,y = 0. The general solution is y = (x + c)?. Picard iterations for this equation other initial values are not suitable either. The student may give it a try for y(l) = 1, etc. and

<!-- formula-not-decoded -->

etc.

20. CAS PROJECT. (b) The Maclaurin series is

<!-- formula-not-decoded -->

Picard' s method gives the terms one after another; undisturbed by any error terms that change from to step. The initial value problem is step

<!-- formula-not-decoded -->

This linear differential equation is solved as explained in Sec. 1.6.

- y' candidate to begin with. It is perhaps a good idea to assume the initial choice in the form y + a; then a = 0 corresponds to the choice in the text, and we see how the expressions in a are involved in the various approximations. The conjecture is true for any choice of a constant (or even of continuous function of x). good

## SOLUTIONS TO CHAPTER 1 REVIEW, page 59

16. This Bernoulli equation (a Verhulst equation if b 0) can be reduced to linear form; as shown in Example 5 of Sec. 1.6 (except for the notations). The general solution is (see (9) in Sec. 1.6)

<!-- formula-not-decoded -->

18. We separate variables and integrate;

<!-- formula-not-decoded -->

We now take the tangent on both sides and use the addition formula for the tangent (formula (16) in Appendix A3.1). This gives the answer.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

20. Exact equation; solvable almost by inspection;

<!-- formula-not-decoded -->

22. ylx = = Xu + u substituted gives

<!-- formula-not-decoded -->

Xu out on both sides. Dividing by x2, we get drops

<!-- formula-not-decoded -->

Answer: y = = X arc sin (x + c)

24. The equation is not exact. Theorem 1 in Sec. 1.5 gives an integrating factor F = Multiplying the equation by this factor; we see that it can be written e2?

<!-- formula-not-decoded -->

26. By separating variables; integrating, and simplifying we get

<!-- formula-not-decoded -->

we obtain the answer y = sin (x +

28.  The general solution of this linear differential equation is obtained as explained in Sec. 1.6,

<!-- formula-not-decoded -->

From this and the initial condition y(O) ~4 we have c = Answer:

<!-- formula-not-decoded -->

30. The exactness test gives ey = ey s0 that the differential equation is exact; We have Uy xe" from the equation. By integration;

<!-- formula-not-decoded -->

By differentiation with respect to x and comparing with the coefficient function of dx in the equation; we get

<!-- formula-not-decoded -->

This gives the general solution

<!-- formula-not-decoded -->

The initial condition = 0 gives 2 . 1 y(2)

<!-- formula-not-decoded -->

32. Theorem 1 in Sec. 1.5 gives the integrating factor F = llx?. We thus obtain the exact equation

<!-- formula-not-decoded -->

By inspection or systematically by integration (as explained in Sec. 1.5), we obtain

<!-- formula-not-decoded -->

From this and the initial condition we get ! 1 = c. Answer:

<!-- formula-not-decoded -->

34. To solve this Bernoulli equation we set u = Then y = y = Substitution into the given differential equation gives y~2

<!-- formula-not-decoded -->

We now multiply by ~2u3/2, obtaining

<!-- formula-not-decoded -->

Hence

<!-- formula-not-decoded -->

From this and the initial condition y(O) = 1 we =1 Answer: get

<!-- formula-not-decoded -->

36. The student should confidence in the method by working simple equations that region to be plotted, trial and error. Solution: y = ce-*2 (bell-shaped curves) . gain using
38. y 2x). See the figure, which shows the tangent directions of these hyper bolas

Chapter Review. Problem 38

<!-- image -->

40. The given curves can be written x3y = C. By differentiation and simplification we the differential equation of the given curves, get

<!-- formula-not-decoded -->

Hence the differential equation of the orthogonal trajectories is

<!-- formula-not-decoded -->

By separating variables we get as the general solution the family of orthogonal trajectories

<!-- formula-not-decoded -->

42. We square the given representation and differentiate the result;

<!-- formula-not-decoded -->

Hence the differential equation of the orthogonal trajectories is y =xy We separate variables; integrate; and then take exponentials;

<!-- formula-not-decoded -->

These are the orthogonal trajectories. This agrees with Prob. where we went in the opposite direction. 41,

44. Exact: y = 1 4 Iterates: e~z

<!-- formula-not-decoded -->

46. By Newton's law of cooling, since the surrounding temperature is 10OPC and the initial temperature of the metal is T(O) 20, we first obtain

<!-- formula-not-decoded -->

k can be determined from the condition that T(I) 51.5; that is,

<!-- formula-not-decoded -->

so that k = In (48.5/80) = .-0.500. With this value of k we can now find the time at which the metal has the temperature 99.99C,

<!-- formula-not-decoded -->

Answer: The temperature of the metal has practically reached that of the boiling wa after 13.4 min. ter

48. We get 10 amperes from the 48-volt battery by choosing R = 48/10 = 4.8 [ohms]. Then L = 0.007 henry follows from the condition

<!-- formula-not-decoded -->

Here we have used the initial condition I(0) =0

50. We proceed as in Sec. 1.4. The time rate of change y = dyldt equals the inflow of salt minus the outflow per minute,

<!-- formula-not-decoded -->

= 80. This gives the particular solution

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

from which we can determine

<!-- formula-not-decoded -->

so it will take little over an hour .

52. This is Example 1 in Sec. 1.8 with the given curves and the trajectories interchanged. It also shows how these kinds of curves and orthogonal trajectories may occur in. physics. From x2 + 2y2 c we obtain the differential equation y ~xl2y. Hence the differential equation of the orthogonal trajectories is

<!-- formula-not-decoded -->

54. The equation is separable;

<!-- formula-not-decoded -->

We now use partial fractions;

By integration and multiplication by b - a,

Taking exponentials now gives

<!-- formula-not-decoded -->

We can solve this algebraically for y Denoting the function on the right by f, we obtain

<!-- formula-not-decoded -->

## CHAPTER 2: Linear Differential Equations of Second and Higher Order

## Major Changes

The old 3 on bigher order linear differential equations has been absorbed into Chap. 2 (Secs. 2.13-2.15). The main emphasis is on second-order differential equations: sentation has become more streamlined. Chap.

## SECTION 2.1. Homogeneous Linear Equations of Second Order, page 64

Purpose; To extend the basic concepts from first-order to second-order equations and to present the basic properties of linear equations:

## Comment on the Standard Form (1)

The form (1) with 1 as the coefficient of y is practical, because if one starts from

<!-- formula-not-decoded -->

one usually considers the equation in an interval I in which f(x) is nowhere zero, s0 that in I one can divide by f(x) and obtain an equation of the form (1) Points at which f(x) 0 require special study, which we present in Chap. 4

## Main Content, Important Concepts

Linear and nonlinear equations

Homogeneous linear equations (Secs: 2.1-2.7)

Nonhomogeneous linear equations (follow in Secs. 2.8-2.12, 2.15)

Superposition principle for homogeneous equations

General solution, basis, linear independence

Particular solution; initial value problem (2), (5)

Reduction to first order (Probs. 1-16)

## Comment on the Four Equations Near the Beginning

These are for illustration, not for solution; but should a student ask, answers are that the first will be solved by methods in Secs. 2.9 and 2.10, the second is a Legendre equation (Sec. 4.3), the third has y = as a solution, and the fourth is solved in Prob. 16.

## Comment on Footnote 4

In 1760, Lagrange gave the first methodical treatment of the calculus of variations. The book mentioned in the footnote includes all major contributions of others in the field and made him the founder of analytical mechanics.

## SOLUTIONS TO PROBLEM SET 2.1, page 71

<!-- formula-not-decoded -->

- 4 y , 2xz' 3z. Separation of variables and integration gives

<!-- formula-not-decoded -->

Integrating once more, we have

<!-- formula-not-decoded -->

6. p = 2Ix (divide the equation by x to it in standard form, with 1 as the coefficient of y"). Hence in (9), get

This gives from (9)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Tbe integral of this is ~cot x, and thus

<!-- formula-not-decoded -->

8 xz' + z = 0, d2 = \_ so that we obtain the answer x

10. dy 22 = 0, divide by z, separate variables; and integrate:

<!-- formula-not-decoded -->

Take exponentials; separate again; and integrate:

<!-- formula-not-decoded -->

Evaluation of the integral gives the answer (y I)ey = C1x + C2

<!-- formula-not-decoded -->

## 12. The standard form is

Hence in (9) we have

<!-- formula-not-decoded -->

This gives; in terms of partial fractions;

<!-- formula-not-decoded -->

By integration we get the answer

<!-- formula-not-decoded -->

The equation is Legendre's equation with parameter n = 1 (which, of course, need not be mentioned to the student), and the solution is essentially a Legendre function. Similarly, the equation in Prob. 11 is Bessels equation with parameter 3 (a case in which Bessel functions of the first kind reduce to sine and cosine (divided by x))

<!-- formula-not-decoded -->

Hence C1 0 and then C2 ~cosh 1 . The answer is (see the figure) y cosh x cosh 1.

Section 2.1. Problem 16

<!-- image -->

<!-- formula-not-decoded -->

Doing more such problems before the discussion of the (rather simple) solution method in the next section may scare students rather than really help them.

## SECTION 2.2. Second-Order Homogeneous Equations with Constant Coefficients, page 72

Purpose. To show that constant-coefficient equations can be solved by algebra; namely, by solving the quadratic characteristic equation (3) which may have:

- (Case I) Real distinct roots
- (Case II) A real double root ('critical case")
- (Case III) Complex conjugate roots (see Sec. 2.3 for details)

## SOLUTIONS TO PROBLEM SET 2.2, page 75

- 14

<!-- formula-not-decoded -->

18. Linearly independent 20. Linearly independent 22. Linearly independent
26.  Linearly dependent because sin 2x 2 sin x cos x
24. Linearly dependent because x/x/ = x2 for nonnegative x
28.  Proportionality on implies proportionality on J. proportionality on J does not imply proportionality on I. Probs. 24 and 25 illustrate this. No,
5. À2 (A1 + 2) + + b. Comparing coefficients gives a = =

- (b) y" + ay' 4 = C1e-ax C2. (ii) z' + az = 0 where y z = ce and the second term comes in by integration, y = J zdx = C1e-ax
- (d) e(k+m)r and ekæ satisfy y (2k + m)y' + k(k + m)y = 0, by the coefficient formulas in part (a) By the superposition principle, another solution is

<!-- formula-not-decoded -->

We now let m 0. This becomes 0/O, and by 1Hôpital s rule (differentiation of numerator and denominator separately with respect to m; not xl) we obtain

<!-- formula-not-decoded -->

The differential equation becomes y 2ky' + k2y = 0. The characteristic equation is

<!-- formula-not-decoded -->

and has a double root. Since a = ~2k, we get k = -al2, as expected.

## SECTION 2.3. Case of Complex Roots. Complex Exponential Function; page 76

Purpose. To discuss the remaining complex Case which gives undamped (harmonic) oscillations (if c 0) or damped oscillations; first obtained in complex form, but convertible to the real form (9) by the superposition principle. III,

## Main Content, Important Concepts

Real general solution (10) in Case III (a damped oscillation)

Euler formula (5) [resulting from the definition (7) of e?]

## Comment on How to Avoid Working in Complex

The average engineering student will profit from working a little with complex numbers. But if one has reasons for avoiding complex numbers here, one may apply the method of eliminating the first derivative from the equation; that is; substitute y = uu and determine U so that the equation for u does not contain u For v this gives

<!-- formula-not-decoded -->

With this v, the equation for u takes the form

<!-- formula-not-decoded -->

and can be solved by remembering from calculus that cos ãx and sin ãx reproduce under two differentiations; multiplied by ~52. This gives (10), where

Of course; the present approach can be used to handle all three cases. In particular;, =0 in Case I gives u

## Comment on Boundary Value Problems and Initial Value Problems

In usual courses on differential equations; initial value problems are generally given more space and weight than boundary value problems. Some reasons are that initial value lems have the following advantages: prob -

1. do not have the somewhat awkward nonuniqueness explained in Example 4. They
2. first-order system; as is usually done in existence and uniqueness theory.

For a first-order equation the two concepts formally coincide, but it seems a bit ical to speak of a boundary value problem because a single (at which the condition is given) does not bound any interval; it is not the 'boundary" of anything; s0 the situation that suggested the name 'boundary value problem" is not given in this case\_ illogpoint

## SOLUTIONS TO PROBLEM SET 2.3, page 80

- 2.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

20. y = cosh 5x by inspection: Systematically, we first get

<!-- formula-not-decoded -->

From the boundary conditions;

<!-- formula-not-decoded -->

spection.

22. y

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (a) minus e2 times (b) gives c2 = 0 Then c1 = Ile from (a) Answer: y
24. PROJECT. The purpose is twofold: (i) Students should learn to look at results carefully before rushing on to the next project or problem; and (ii) graphs may show var ious interesting facts not obvious from formulas. They may also give quantitative impressions (e.g+, in this case, how rapidly the exponential function decreases) . Since the tangent at the extrema is horizontal,  whereas at the points of contact the tangent has a negative (for positive y) or a positive (for negative y) it is clear without calculation that these cannot coincide with extrema, but must come after them (at larger x s) For the harmonic motion the inflection lie on the axis, for reasons of symmetry. For a damped oscillation; one might guess that are alternatingly at positive and negative y-values, shifted from the intersection points slope slope points points they

slightly to smaller x-values. Some calculations are as follows.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

thus x = ~0.049 958

26. CAS PROJECT. (a) 02 = b = 1 + 02 because a = 1.
2. (b) The approach is rapid. The figure shows the solutions for 5, 0.5, 0.1, 0.01, 0.000 001 .

<!-- formula-not-decoded -->

(differentiating numerator and denominator separately with respect to @, not x), we get the limit

<!-- formula-not-decoded -->

as it should be.

- Change y' (0) to 0 or to a positive value.

Section 2.3. CAS Project 26

<!-- image -->

## SECTION 2.4. Differential Operators. Optional, page 81

Purpose. To take a short look at the operational calculus of second-order differential operators with constant coefficients, which parallels and confirms our discussion of differ ential equations with constant coefficients.

## SOLUTIONS TO PROBLEM SET 2.4, page 83

<!-- formula-not-decoded -->

## SECTION 2.5. Modeling: Free Oscillations (Mass-Spring System) page 83

Purpose. To present a main application of second-order constant-coefficient equations

<!-- formula-not-decoded -->

resulting as models of motions of a mass m on an elastic spring of modulus k 0) under linear damping (2 0) by applying Newton's second law and Hooke' s law. These are free motions (no driving force). Forced motions follow in Sec. 2.11.

## Main Content, Important Concepts

Restoring force ky, damping force cy" force of inertia my'

No damping, harmonic oscillations (4), natural frequency 0/2m

Overdamping, critical damping, nonoscillatory motions (7), (8)

Underdamping, damped oscillations (10)

## SOLUTIONS TO PROBLEM SET 2.5, page 90

2. W = 20 and S0 2 gives k = 10 by Hooke's law. Thus Wlso

<!-- formula-not-decoded -->

From this we get the period IIf 0.284 [sec]

4. because the frequency is independent of initial conditions; it only depends on klm. No,
2. 6 By Hooke' s law, F1 = k1 =8 stretches spring S1 by 8, and F2 = k2 = 12 stretches spring S2 by 12. Hence the unknown k of the combination of the springs stretches S1 by klk1 kI8 'and S2 by klkz = k/12. And k is such that the sum of these stretches equals 1, because k is the force that corresponds to the stretch 1 of the combination Thus

<!-- formula-not-decoded -->

8. = =T 0.32yY, where n - 0.32y is the volume of water displaced when the is depressed y meters from its equilibrium position, and y 9800 nt is the weight of water per cubic meter. Thus y + @ 2y = 0, where 0 T 0.32ylm and the period is = 2; hence my" buoy

<!-- formula-not-decoded -->

10. TEAM PROJECT. (a) mLe" ~mg sin 0 ~ mg0 (the tangential component of W = mg), 0" + 020 = 0, 02 gIL. Answer: gILI2T
2. (b) By (a), the frequency is

<!-- formula-not-decoded -->

s0 it takes about 2 sec to complete 1 cycle. Answer: It ticks about 30 times per minute.

- W = kso = 8. Now S0 1 because the system has its equilibrium position 1 cm below the horizontal line. Also; m = that Wlg,

<!-- formula-not-decoded -->

and we get the general solution

<!-- formula-not-decoded -->

The initial conditions give y(O) = A = 0 and y(0) 31.3B = 10. Hence B = 0.319 and the answer is

<!-- formula-not-decoded -->

- (d) 0(t) = 0.5235 cos 3.7t + 0.0943 sin 3.7t [rad]
12. y = 0 gives C1 ~c2e-2ßt , which has at most one solution because the exponential function is monotone.
14. Equating the derivative of (8) to zero; we get

<!-- formula-not-decoded -->

and from this the solution

<!-- formula-not-decoded -->

16. From (10) and y 0 we obtain tan (@*t = 8) const and consecutive solutions of this equation have the constant distance Tlø*
18. If a maximum is at to, the next is at t1 to (10) have period 2u/ø*, the ratio is

= 2T; tan t =

- no matter what klm is or y(o), etc.
- (b) The first step is to see that Case II corresponds to c = 2. Then one can choose other values by experimentation. In 51 the values of c (omitted on purpose; the student should choose') are 0 and 0.1 for the oscillating curves and 1, 15,2, 3 for the others (from below to above)
- (c) This addresses a general issue that also arises in problems involving heating and cooling, mixing, electrical vibrations; etc. One is generally surprised how quickly certain states are reached practically when the theoretical time is infinite.
- (e) Tbe main difference is that Case I gives y(t) = (1 t)e -t which is negative for t &gt; 1 The experiments with the curves are as before.
- 4V4 c2. From the initial condi tions, A 0 gives as the smallest positive solution t2 = c2 Tlw*\_ There Y(t) has a horizontal tangent and touches y ~0.01 when y(t2) ~0.01 and stays within the limits in (11) because it oscillates between +e-ct2l2 Thus we get c from y(t2) = =e ~ct2/2 ~0.01 as c = 1.65, approximately . @*

<!-- formula-not-decoded -->

## SECTION 2.6. Euler-Cauchy Equation; page 93

Purpose. Algebraic solution of the Euler-Cauchy equation; which appears in certain applications (see our Example 4) and which we shall need in Sec. 4.4 as the simplest equation to which the Frobenius method We have three cases; this is similar to the situation for constant-coefficient equations; to which the Euler-Cauchy equation can be transformed (Prob. 20); however, this fact is of theoretical rather than of practical interest. again applies.

## Comment on Footnote 9

Euler worked in St. Petersburg 1727-1741 and 1766-1783 and in Berlin 1741-1766. He 12.7) since 1740, introduced integrating factors (Sec. 1.5) in 1764, and studied conformal mappings (Sec. 12.5) since 1770. His main influence on the development of mathematics and mathematical physics resulted from his textbooks; in particular from his famous Introductio in analysin infinitorum (1748), in which he also introduced many of the modern notations (for trigonometric functions; etc.). Euler was the central figure of the math ematical activity of the 18th century. His collected works are still incomplete, although some seventy volumes have already been published.

Cauchy worked in Paris; except during 1830-1838 when he was in Turin and Prague. à VÉcole royale polytechnique (vol. 1, 1823), he introduced more rigorous methods in calculus, based on an exactly defined limit concept; this also includes his convergence principle (Sec. 14.1). He also was the first to give existence proofs in differential equations. He initiated complex analysis; we discuss his main contributions to this field in Secs. 12.4, 13.2-13.4, and 14.2. His famous integral theorem (Sec. 13.2) was published in 1825, his paper on complex series and their radius of convergence (Sec. 14.2) in 1831. power

## SOLUTIONS TO'PROBLEM SET 2.6, page 96

2. I, + c2x3
2. ables.
8. I, c1 + c2 In x Also solvable by reduction and separation
4. In x)r0.6
10. I, c1x-0.2 +
14. General solution: c1x + Answer: 2x
16. General solution: A cos (3 In x) + B sin (3 In x). Answer: 2 cos (3 In x)
18. General solution: (c1 + c2 In x)lx. Answer: (3 In x)lx
20. x et In x. The chain rule gives

<!-- formula-not-decoded -->

where the dots denote derivatives   with respect to t. By substitution into (1) we obtain

<!-- formula-not-decoded -->

The characteristic equation of the new equation is

<!-- formula-not-decoded -->

It is of the form (3). Its roots are in Case I

<!-- formula-not-decoded -->

etc., sO that we can obtain the solution of the Euler-Cauchy equation from those of the new equation. Also; in Case III the transformation into real form in Sec. 2.3 car ries over into that in this section.

## SECTION 2.7. Existence and Uniqueness Theory. Wronskian; page 97

Purpose. To explain the theory of existence of solutions of equations with variable coefficients in standard form (that is, with y" as the first term; not; say, f(x)y")

<!-- formula-not-decoded -->

and of their uniqueness if initial conditions

<!-- formula-not-decoded -->

are imposed. Of course, no such theory was needed in the last sections on equations for which we were able to write down all solutions explicitly .

## Main Content

Continuity of coefficients suffices for existence and uniqueness.

Linear independence if and only if the Wronskian is not zero.

General solution exists and includes all solutions.

## Comment on Wronskian

For n 2, where linear independence and dependence can be seen immediately, the Wronskian serves primarily as a tool in our proofs; the practical value of the independence criterion will appear for higher n in Sec. 2.13.

## SOLUTIONS TO PROBLEM SET 2.7, page 100

<!-- formula-not-decoded -->

8. We use the abbreviations = sin Wx. Then

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where c cos (In x), s = sin (In x)

18. TEAM PROJECT: (a) Suppose that y1 and y2 are zero at some Xo in I. Then the first row of their Wronskian is zero at xo: This implies linear dependence of y1 and y2 by Theorem 2 point \_
2. () At a maximum or minimum the first derivative is zero; if this happens for two so W = 0 at that This implies linear dependence by Theorem 2 point:.
3. (c) By direct calculation;

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Multiplying out; we see that four of the eight terms cancel in pairs (the terms in Y1yí and The remaining terms can be written

<!-- formula-not-decoded -->

From this the conclusion follows. Note that in this calculation we need not refer to the familiar rule for multiplying determinants (which some students may not know).

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SECTION 2.8. Nonhomogeneous Equations, page 101

Purpose. We show that for getting a general solution y of a nonhomogeneous linear equation we must find a general solution yn of the corresponding homogeneous equation and thenthis is our new task\_any particular solution yp of the nonhomogeneous equation;

<!-- formula-not-decoded -->

## Main Content, Important Concepts

General solution; particular solution

Continuity of p, 9 r suffices for existence and uniqueness.

General solution exists and includes all solutions.

(Solution methods follow in Secs. 2.9,2.10)

## SOLUTIONS TO PROBLEM SET 28, page 103

2. The general solution of the homogeneous equation is c1e Hence as the s0Jution of the nonhomogeneous equation we first obtain

<!-- formula-not-decoded -->

We see that the last term is a solution of the homogeneous equation; and we can absorb it into the general solution of the latter; so that we simply have

<!-- formula-not-decoded -->

the same answer as in Prob. 1, except for the notation. Of course; the point of the problem is that two particular solutions of the nonhomogeneous equation can differ at most by a solution of the homogeneous equation; in the present case, this is ~3e" y = e"(Acos 2x + B sin 2x) + x3 . Whereas in Prob. 3 we have just one term on the rght side of the equation but many terms in yp here we have the opposite situation where the right side of the equation has many terms but yp is simple.

4.

<!-- formula-not-decoded -->

+ 4 + e*. Perhaps the student should express yp in terms of cosh x and sinh x, to see the analogy to the expression A cos x + B sin x in other equations. C1erl4
10. y cos x. From this form of the answer we recognize the form of the general solution yh + c2e-* (which may not always be the case). It is important for the student to understand that yp will satisfy the initial conditions only in very rare cases practically never\_and that further work is necessary for solving the initial value problem.
12. y = 1.8 cos 2x + sin 2x + 3x cos 2x. The right side of the equation is a solution of the homogeneous equation and produces the form of yp involving the factor x This will be discussed systematically in the next section
16. TEAM PROJECT. (a) 1.' Find a general solution of the homogeneous equation:
- 2x2 + 3e". The first two terms result from the general solution of the homogeneous equation c1x +
- 2 Find any particular solution Yp of (1). (It is quite unlikely that yp automatically satisfies the initial conditions.
- 3 Determine values of the arbitrary constants in (3) from the initial conditions.
- 0) The difference of the two solutions must be a solution of the homogeneous equation.
- (c) As in ()
- (d) Of course, because Yp does not depend on the choice of that general solution yn
- (e) The usual  method for the Euler-Cauchy equation gives the general   solution C1x + of the homogeneous equation; hence y = C1x + + 3e* for the nonhomogeneous equation. From this, y(O) = 3 (note that any other y(0) would result in no solutiont). Now y = C1 4 + 3e*,y'(0) = c1 + 3 = 7, hence C1 4, wbereas c2 remains arbitrary . The reason is that the coefficients of the equation in standard form 2c2x

<!-- formula-not-decoded -->

become infinite as x ~ 0.

## SECTION 2.9. Solution by Undetermined Coefficients, page 104

Purpose: To discuss a special method for particular solutions of constant-coefficient equations with right side r(x). This method is simpler than that in Sec. 2.10 and should be used whenever it applies. Rules (A), (B), and (C) tell us what to do in practice. special

## Comment on Table 2.1

It is clear that the table could be extended by the inclusion of products of polynomials times cosine or sine and other cases of limited practical value. Also, œ 0 in the last pair practical importance.

## SOLUTIONS TO PROBLEM SET 2.9, page 107

The request to show each step should prevent students from simply letting the CAS produce the final answer\_

- 2x 2. y = 4 4 + 2e An important point is that the Modification Rule applies only to one of the two exponential terms. The Sum Rule is also used. xer
4. y = C1e + an application of the Modification Rule for a simple root =2-
6. y = + C2e-rl3 + 3x 10 + g sin x; an application of the Sum Rule. Note that 9x causes an x-term and a constant term in the solution:. The cosine term would usually cause a cosine and a sine term; so here we get less than expected. ce-32
- the lines in Table 2.1, which does not contain products of trigonometric times exponential functions. However; the method is the same in principle and should encour age students to attempt more independent work. On the other hand, we did not include other such problems; whose practical value is not very great.
12. y = e3æ is 'hidden" in sinh 3x on the right, whereas the other term in sinh 3x does not call for the Modifi C1e3æ
10. y C2e3xl2 Students should perhaps be asked to express the solutions (the last two terms) in terms of cosh 2x sinh 2x, to see the analogy to expressions a cos x + b sin x in other differential equations. and
14. y e2æ(A cos 4x + Bsin 4x) + 4 cos x + 19 sin x
16. y e 2x sin 2x) + e32 Be sure students do not get confused: the Modifi cation Rule is not needed.
18. y cos 3x + x sin 3x. The first term results from the general solution c1 cos 3x + C2 sin 3x of the homogeneous equation. Initial conditions versely) appear in various theoretical considerations. y(o)
20. y = This is an application of the Modification Rule in the case of the dou1.4. A general solution of the   nonhomogeneous   equation is (c1 4 One should emphasize that the initial conditions y(O) 0 y (0) = 0 would imply y = 0 only in the homogeneous case. Also; C1 = 0, C2 is an = 0, yp(0) = 0, where yp = x2e1.42 .
22. 2e-0.52 cos 3x + + 4 The general solution e homogeneous equation contributes the first term of the solution. ~0.52(A

- (a + bx)e" , etc. Applications may occur occasionally  For instance, e-kæ cos @x (with = time) could represent a time-decreasing driving force.

## SECTION 2.10. Solution by Variation of Parameters; page 108

Purpose: To discuss the general method for particular solutions; which applies in any case, but may often lead to difficulties in integration (which we by and large have avoided in our problems, as the subsequent answers show).

## Comments

The equation must be in standard form, with 1 as the coefficient of y ~students tend to forget that.

Here we do need the Wronskian; in contrast to Sec. 2.7 where we could get away with out it.

## SOLUTIONS TO PROBLEM SET 2.10, page 111

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Answer:

4. Y1 = cos 3x, Yz sin 3x, W = 3,r = csc 3x. Hence in (2),

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Answer:

<!-- formula-not-decoded -->

Answer:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Answer:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

10. Y1 = sin X, W = e-22 Hence in (2) 2 1 dx = e COS cos x)4e-rIcos3 x

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Hence in (2),

<!-- formula-not-decoded -->

out and the answer is drop

<!-- formula-not-decoded -->

14. Y1 = x3 y2 = x2, W = -x4. From the standard form we get

Hence in (2),

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This gives the particular solution

Answer:

<!-- formula-not-decoded -->

This gives the particular solution

<!-- formula-not-decoded -->

Answer:

<!-- formula-not-decoded -->

12. Y1 = 1, Y2 = x2, W = 2x. Divide the given equation by x to get it in standard form and from it,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

18. TEAM PROJECT. (a) Y1 = = W = 2e 65 cos 2x. From (2),

<!-- formula-not-decoded -->

~cos 2x + 8 sin 2x.

Answer:

<!-- formula-not-decoded -->

This was much more work than that for undetermined coefficients.

- b) We can treat x? on the right by undetermined coefficients; obtaining the contribution x2 + 4x + 6 to the solution. We could treat it by the other method, but we would have to evaluate additional integrals of an exponential function times a power of x We treat the other part; 35x3/2e* , by the method of this section; = W = e22 . From this and (2),

<!-- formula-not-decoded -->

Complete answer:

- If the right side is a power of x, say, r = then substitution of yp Cxk gives (c) roxk,

<!-- formula-not-decoded -->

This can be solved for C. To explore further possibilities, one may work "backwards' that is, assume a solution; substitute it on the left, and see what form one as a right side. gets

## SECTION 2.11. Modeling: Forced Oscillations. Resonance; page 111

Purpose. To extend Sec. 2.5 from free to forced vibrations by adding an input (a driving force, here assumed to be sinusoidal) . Mathematically, we go from a homogeneous to a nonhomogeneous equation; which we solve by undetermined coefficients.

## New Features

Resonance (11) y At sin øt in the undamped case

Beats (12) y = B(cos @t COS wt) if input frequency close to natural

<!-- formula-not-decoded -->

Phase between input and output lag

## SOLUTIONS TO PROBLEM SET 2.11, page 117

2. Yp = 1.5 cos 3t + sin 3t
4. Yp = 1 cos t \_
8. y = Acos VBt + B sin VBt + 4 cos 0.5t. We have no sine term in yp because of the absence of y' in the equation. This is typical.
10. y = (c1 + + 2 sin t = gcos t C2t)e~3t
12. y = the equation causes the unbounded term in the solution.
14. y = e-t(cos t + 2 sin t) + 0.2cos t + 0.4 sin t. For t = 5 the exponential term has decreased to less than 19 of its original value; this practically marks the end of the transition.
16. y = 6.4 cos 0.5t. At t = 1.2 the exponential term has decreased to less than 1% of original value. This marks the end of the transition from practical point of view. t = 1.8 is the time when that term has become less than 1/10 of a percent in absolute value. its
18. WRITING PROJECT. Brevity should force the student to recognize what is important and what is marginal. It is useful to learn this in connection with short reports, articles, talks; etc.
20. CAS PROJECT. The choice of @ needs experimentation; inspecting the curves obtained and then making changes on a trial-and-error basis. It is interesting to see how in the case of beats the period longer and longer and the maximum amplitudes get and as @ approaches the resonance frequency. gets larger larger

## SECTION 2.12. Modeling of Electric Circuits, page 118

ATTENTION! The right side in (1) is Eowcos @t, because of differentiation:

## Main Content

Modeling by a simple extension of Sec. 1.7

Electrical-mechanical strictly quantitative analogy (Table 2.2)

Transient tending to harmonic steady-state current

## SOLUTIONS TO PROBLEM SET 2.12, page 122

2. Q = RIZL &gt; 0. If ß is real, ß = RI2L since R2 4LIC = R?; hence 41 ~Q + B &lt; 0 (and À2 damped oscillation.

- 4 10 cos t 4 20 sin t because the general solution of the homogeneous equation approaches zero as t -&gt; %

6. 0

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

10. The equation is

undetermined coefficients; we obtain the general solution Using

<!-- formula-not-decoded -->

Hence y(0) =A = g 2 0, A g From Eq: (1") for the charge we see that Q(0) 0 in the present case implies I' (0) = 0. By differentiating I and substituting A g we obtain from I' (0) 0 the value B Answer:

<!-- formula-not-decoded -->

12. The equation is

<!-- formula-not-decoded -->

It has the general solution

<!-- formula-not-decoded -->

From (1") for Q we obtain (similar to Example 1) I' (0) = Q"(0) = 24. From this and I(0) 0 we obtain the answer

<!-- formula-not-decoded -->

14. The equation is

general solution is

<!-- formula-not-decoded -->

I(0) = 0 gives A =0. Equation (1") for the charge is

It implies that because Q(0) =

<!-- formula-not-decoded -->

Answer:

16. (a) By integration;

<!-- formula-not-decoded -->

- (b) 20" + 2 . 10Q = 110; a general solution is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

From this and the first initial condition; Q(0) = A + 0.0055 = 0. Hence A = ~0.0055. The second initial condition I(0) = Q'(0) = 0 gives B =0 because

<!-- formula-not-decoded -->

Together we have as in (a)

<!-- formula-not-decoded -->

18. TEAM PROJECT. (a) The complex division trick is performed to make the denominator real,

<!-- formula-not-decoded -->

Before we multiply out and take the real part, the expression for Ip is

<!-- formula-not-decoded -->

- c) Substitution of (11) and its derivatives into the present equation gives

<!-- formula-not-decoded -->

Solving for K; we obtain K = 2 \_ i. Hence the complex solution is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The student should verify that it satisfies the given real differential equation.

## SECTION 2.13. Higher Order Linear Equations, page 124

Purpose. Extension of the basic concepts and theory in Secs. 2.1 and 2.7 to homogeneous linear differential equations of any order n. This shows that all the essential facts carry over practically now more involved than for n = 2, causes the Wronskian to become indispensable (whereas for n =2it played a mar ginal role)

## Main Content, Important Concepts

Superposition principle for the homogeneous equation (2)

General solution; basis; particular solution

General solution of (2) with continuous coefficients exists.

Existence and uniqueness of solution of initial value problem (2) (5)

Linear independence of solutions; Wronskian

General solution includes all solutions of (2)

## SOLUTIONS TO PROBLEM SET 2.13, page 131

2. W = y = er ~ ~6e2r
4. W = = 12 + 3 cos x 1,y =
6. W = = Note that another basis is er COS x, sin x e2
8. W = 18,y = cos x +
10. Linearly independent. Point out that sin 2x 2 sin xcos x is not a linear combination of cos x and sin x
12. Linearly dependent. This is an example where the use of a functional relation helps

The real is part

<!-- formula-not-decoded -->

14. Linearly dependent. The essential is that the exponential functions have the right exponent occurring in the definition of sinh 3x. point
16. Linearly independent
20. TEAM PROJECT (a) (1) If y1 = 0, then (4) holds with any k1 * 0 and the other k; all zero.
18. Linearly dependent. This serves as reminder that any set containing the zero func tion as an element is linearly dependent.
- (2) If $ were linearly dependent on I, then (4) would hold with a k; # 0 on I, hence also on J, contradicting the assumption: This also shows that linear de pendence on I implies linear dependence on J. Linear independence on implies no conclusion for J. Example: xx| and x2 are linearly independent on &lt;x &lt; 1 but linearly dependent on 0 &lt; x &lt; 1.
- (3) By assumption; k1V1 + kpYp 0 with k1 kp not all zero. This implies (4) with k1, kp as before and kp+1 kn 0. In the other case T may be linearly dependent (or not). Example: Take any linearly independent $ and let Tbe $ and the zero function:
7. If your functions are solutions of a homogeneous linear differential equation continuous coefficients; then you can use the Wronskian. For other means, see the problems (for instance; the use of functional relations; evaluating (4) at several xs in the interval, etc) with

## SECTION 2.14. Higher Order Homogeneous Equations, page 132

Purpose. Extension of the algebraic solution method for constant-coefficient equations from n 2 (Secs. 2.2, 2.3) to any n, and discussion of the increased number of possible cases:

Real different roots

Complex simple roots

Real multiple roots

Complex multiple roots

Combinations of the preceding four basic cases

Explanation of these cases in terms of typical examples.

## Comment on Numerical Work

In practical cases, one may have to use Newton' s method or another method for computing (approximate values of) roots in Sec. 17.2

## SOLUTIONS TO PROBLEM SET 2.14, page 137

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

With this, and

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

With c2 0, another differentiation gives and

Answer:

<!-- formula-not-decoded -->

14. The characteristic equation has the roots +1 and +i. Hence a general solution; its derivatives, and their values at x = 0, equated to the corresponding initial conditions; are as follows.
2. y = ~ ~ C1 = C2 + B = 7 Cer
3. (a) = + A cos x + Bsin x, C1 + A = \_1 Cer + C2
4. y = + C2e B sin x, C1 .+ C2 = A = =1 Ces
5. (d) y' = + A sin x

We obtain A =0 from (a) (c); then B = 0 from (), (d); then C1 and finally c2 ~4 from (a) Answer:

<!-- formula-not-decoded -->

- derivatives; and their values at x = 0, equated to the corresponding initial conditions; are as follows.
- (b) y = ~A1 sin x + B1 cOS x sin 3x + 3B2 cos 3x, B1 + 3B2 = 0 3A2
- (a) y = A1 cos x + B1 sinx + A2 cos 3x + B2 sin 3x, A1 + Az = 0
- (c) y = ~A1 COS X B1 sin x = cos 3x 9B2 sin 3x, ~A1 = 32 9Az 9Az

From (a) and (c) we obtain Az ~4, A1 =4. From (b) and (d) we obtain B2 0, B1 0. Answer:

- (d) y" A1 sin x - B1 cOS x + sin 3x 27B2 cos 3x, ~B1 27B2 = 0. 27A2

<!-- formula-not-decoded -->

18. Tbe characteristic equation has a triple root ~2 Hence a general solution; its derivatives, and their values at x = as follows.
2. (a) y = (c1 + c2x +

Answer:

<!-- formula-not-decoded -->

- 2c3r2)e-2, y"(0) =4 + = 6, C3 =1 2c; Ac3x

20. PROJECT. (a) Divide the characteristic equation by ^ = A1 if y1 =
2. (b) The idea is the same as in Sec. 21.
3. (c) Here, as always; the first step is to produce the standard form; as the form under which the equation for z was derived. Division by x3 gives

<!-- formula-not-decoded -->

With y1 yí = I,y" = 0, and the coefficients p1 and p2 from the standard equation, we obtain

<!-- formula-not-decoded -->

Simplification gives

<!-- formula-not-decoded -->

Hence

<!-- formula-not-decoded -->

By integration we get the answer

<!-- formula-not-decoded -->

## SECTION 2.15. Higher Order Nonhomogeneous Equations, page 138

Purpose. To show that the transition from n = 2 (Sec. 2.8) to general n introduces no new ideas, but generalizes all results and practical aspects in a straightforward fashion; this refers to existence; uniqueness; and the need for a particular solution yp to get a general solution in the form

<!-- formula-not-decoded -->

## SOLUTIONS TO PROBLEM SET 2.15, page 141

2. Y1 Yz = = 2x-1 . Further more, r = In x because we have to divide the equation by x3 to get it in standard form. From (7) we now obtain =x-1

<!-- formula-not-decoded -->

Answer:

The derivatives are

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

4. yp is conveniently obtained by undetermined coefficients. Answer:

<!-- formula-not-decoded -->

642 + 124 = 8 = (À - 2)3. Hence a basis is

<!-- formula-not-decoded -->

The second derivatives are

<!-- formula-not-decoded -->

From the Wronskian we can factor out e2r from each of the three columns. Then

<!-- formula-not-decoded -->

In (7) we further need

<!-- formula-not-decoded -->

With these values and the integrals in (7) become

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

explained in the text; we lose a factor e2æ . Furthermore;

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

From this and (7),

<!-- formula-not-decoded -->

Answer:

<!-- formula-not-decoded -->

8. = = (divide by 4x3). From (7) we thus obtain xl/2

<!-- formula-not-decoded -->

Answer:

<!-- formula-not-decoded -->

- = = ~2x In x, W3 = x2, = llx. Answer: y = x2 + x In x

12. y = sin x + sin 3x + 2 sinh x

14. CAS PROJECT. The first equation has as general solution

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

However; the equation alone does not show much; s0 another idea is needed. One could modify the right side systematically and see how the solution changes. The solution of the second suggested equation shows that the equation is not accessible by undetermined coefficients; its solution is (see Prob. 2)

<!-- formula-not-decoded -->

And one could perhaps modify this equation; too; in an attempt to obtain a form of solution that might be suitable for undetermined coefficients.

## SOLUTIONS TO CHAPTER 2 REVIEW, page 142

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

20. yp is obtained by the method of undetermined coefficients. Answer:

<!-- formula-not-decoded -->

22. The particular solution yp = ficients. Answer:

<!-- formula-not-decoded -->

24. The particular solution yp ~In x e-22 is obtained by the method of variation of parameters. Answer:

<!-- formula-not-decoded -->

26. The particular solution yp = = gcosh x is obtained by the method of undetermined coefficients. Answer:

<!-- formula-not-decoded -->

28. Applying the method of undetermined coefficients; we obtain as a general solution

30. By variation of parameters obtain the answer we

<!-- formula-not-decoded -->

32. The particular solution yp = 3 cos x + sin x is obtained by the method of undetermined coefficients. Answer:

<!-- formula-not-decoded -->

34. y = e + sin @x) 22(cos
36.  The initial conditions are such that the general solution of the homogeneous equation does not contribute to the answer
38. y = (2 x)er
4. tion is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By the method of undetermined coefficients and from the initial conditions get the answer we

<!-- formula-not-decoded -->

+ c2e-0.125008t

<!-- formula-not-decoded -->

44. I(t) = 0.0833e-160t 0.3333e 4Ot

Note that since E(t) is continuous at t = 0.01, and Q is always continuous (cannot change abruptly), I and I' are continuous at t = 0.01, whereas I" has a jump -1600 since IOE' has this jump at t = 0.01.

<!-- formula-not-decoded -->

1Oit Substituting I = and its derivatives and dropping the factor e we obtain Keloit

<!-- formula-not-decoded -->

Solving algebraically for K; we get

<!-- formula-not-decoded -->

Answer:

<!-- formula-not-decoded -->

46. The complex equation is

48. The equation is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The solution satisfying the initial conditions is

<!-- formula-not-decoded -->

as obtained by the method of undetermined coefficients.

The last two terms result from the driving force. In the first two terms, 0 Vklm = 3 This shows that resonance would occur if the driving force had the fre-= 3/2T.

50. C*() is given by (14), Sec. 2.11. The maximum is obtained by equating the deriv ative to zero; this gives (15) in Sec. 2.11, which for our numerical values becomes

<!-- formula-not-decoded -->

so that 0 = 4. Eq. (16) in Sec. 2.11 then gives the maximum amplitude

<!-- formula-not-decoded -->

To check this result; we determine the general solution; using the method of undetermined coefficients, finding

<!-- formula-not-decoded -->

and confirm the result by calculating the amplitude

<!-- formula-not-decoded -->

## CHAPTER 3 Systems of Differential Equations. Phase Plane Qualitative Methods

## Major Changes

This chapter has been completely rewritten; on the basis of suggestions by instructors who have taught from it and of my own recent experience of (once morel) teaching systems of differential equations. The main reason is that due to the increasing emphasis on linear algebra in our standard curricula; we can now expect that when students take a course on differential equations that includes material from Chap. 3, almost all of them have at least some working knowledge of 2 X 2 matrices.

To be completely on the safe side, Sec. 3.0 is included for reference, s0 that the student will have no need to search through Chap. 6 or 7 for concept or fact needed in Chap. 3.

Accordingly, Chap. 3 makes modest use of 2 x 2 matrices. n X n matrices are mentioned only in passing and are immediately followed by illustrative examples of systems of two differential equations in two unknowns; involving 2 X 2 matrices only. Section 3.2 and the beginning of Sec. 3.3 are intended to give the student the impression that for first-order systems, one can develop a theory that is conceptually and structurally similar to that in 2 for a single differential equation. Hence if the instructor feels that the class might be disturbed by n X n matrices, omission of the latter and explanation of the material in terms of two differential equations in two unknowns will entail no disadvan tage and will leave no gaps of understanding OF skill. Chap.

Basic throughout Chap. 3 is the eigenvalue problem (for 2 X 2 matrices), consisting first of the determination of the eigenvalues À2 (not necessarily numerically distinct) as solutions of the characteristic equation; that is, the quadratic equation

<!-- formula-not-decoded -->

and then an eigenvector corresponding to À1 with components X1, x2 from

<!-- formula-not-decoded -->

and an eigenvector corresponding to À2 from

<!-- formula-not-decoded -->

It may be useful to emphasize early that eigenvectors are determined only up to a nonzero factor and that in the present context; normalization (in order to obtain unit vectors) is hardly of any advantage.

If there are students in the class who have not seen eigenvalues before (although the elementary theory of these problems does occur in every up-to-date introductory text on linear algebra), should not have difficulties in readily grasping the meaning of these problems and their role in this chapter, simply because of the numerous examples and applications in Sec. 3.3 and in later sections. they

Section 3.5 includes three famous applications; namely, the pendulum and van der Pol equations and the Lotka-Volterra predator-prey population model

## SECTION 3.0. Introduction: Vectors, Matrices, Eigenvalues, page 146

Purpose. This section is for reference and review only, the material being restricted to what is actually needed in this chapter, to make it self-contained.

## Main Content

Matrices, vectors

Algebraic matrix operations

Differentiation of vectors

Eigenvalue problems for 2 2 matrices

## Important Concepts and Facts

Matrix, column and row vector, multiplication

Linear independence

Eigenvalue, eigenvector, characteristic equation

## Some Details on Content

Most of the material is explained in terms of 2 X 2 matrices, which play the major role in 3; indeed, n X n matrices for general n occur only briefly in Sec. 3.2 and at the beginning in Sec. 3.3. Hence the demand on the student in Chap. 3 will be very modest; and Sec. 3.0 is written accordingly . Chap.

Example 1. Although the later sections include many eigenvalue problems, the complete solution of such a problem (the determination of the eigenvalues and corresponding eigenvectors) is given here.

In particular, eigenvalue problems presently lead to quadratic equations only, so that nothing needs to be said about difficulties encountered with 3 X 3 or larger matrices.

## SECTION 3.1. Introductory Examples, page 152

Purpose. In this section the student is supposed to first impression of the tance of systems of differential equations in physics and engineering and why OCCUI, and why lead to eigenvalue problems. gain impor they they

## Main Content

Mixing problem

Electrical network

Conversion of single equations to systems [see (8)-(10)]

Short Courses. Take a look at Sec. 3.1, skip Sec. 3.2 and the beginning of Sec. 3.3, proceeding directly t0 solution methods in terms of the examples in Sec. 3.3. quick

## Some Details on Content

Example 1 extends the physical in Sec. 1.4, consisting of a single tank; to a system of two tanks. The principle of modeling remains the same. The problem leads to typical eigenvalue problem; and the solutions show typical exponential increases and decreases. system

Example 2 leads to a nonhomogeneous first-order system (a kind of system to be considered in Sec. 3.6). The vector g on the right in (5) causes a term + 3 in I1, but has no effect on I2, which is interesting to observe. If time permits; one could add a little discussion of particular solutions corresponding to different initial conditions.

Reduction of single equations to systems [formula (10)] is of great importance and should be emphasized. Example 3 illustrates it; and further applications follow in Sec. 3.5. It helps to create ''uniform' theory centered around first-order systems; along with the possibility of reducing higher order systems to first order.

## SOLUTIONS TO PROBLEM SET 3.1, page 158

2. The system is

As a single vector equation;

<!-- formula-not-decoded -->

has the eigenvalues À1 = ~0.03 and corresponding eigenvectors

<!-- formula-not-decoded -->

respectively. The corresponding general solution is

From the initial values;'

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In components this is c1 + c2 = 0, 0.5c1 C2 150. Hence c1 = 100, C2 = =100. This gives the solution

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In components;

4. In (6) we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where 0.01 appears because we divide by the content of the tank T1, which is twice the old value. In proper order, the system becomes

<!-- formula-not-decoded -->

From this and the initial conditions in vector form we get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

in components,

Subtract ž(a) from (b) to get

<!-- formula-not-decoded -->

Then from (a)

Thus in components,

<!-- formula-not-decoded -->

6. The first differential equation remains as before. The second equation is obviously changed to

<!-- formula-not-decoded -->

Substitution of the first equation into the new second one, as in the text; gives

<!-- formula-not-decoded -->

Hence the matrix of the new system is

<!-- formula-not-decoded -->

Its   eigenvalues are and Corresponding eigenvectors are x(l) [1 = [1 0.64] , respectively. The corresponding general solution is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The matrix has the eigenvalues ~1 and \_2 and corresponding eigenvectors [1 and [1 2] , respectively. From this

<!-- formula-not-decoded -->

and the second equation gives the derivative y2 = y'

10. The system is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

8. The system is

<!-- formula-not-decoded -->

The matrix has the eigenvalues 4 and 1/4 and eigenvectors [1 4]T and [1 respectively. The corresponding general solution is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The   eigenvalues of  its matrix are 1, Eigenvectors are [1 1 [1 4]T, respectively . The corresponding general solution is

<!-- formula-not-decoded -->

14. TEAM PROJECT. (a) From Sec. 2.5 we know that the undamped motions of a mass on an elastic spring are governed by my + ky = 0 or

<!-- formula-not-decoded -->

where y = y(t) is the displacement of the mass. By the same arguments, for the two masses on the two springs in Fig. 77 we obtain the linear homogeneous system

<!-- formula-not-decoded -->

for the unknown displacements y1 = Y1(t) of the first mass m1 and y2 = Y2(t) of the second mass m2: The forces on the first mass give the first equation; and the forces on the second mass give the second equation. Now m1 = 1, k1 = 3, and kz = 2 in 77 so that by ordering (11) we obtain acting acting Fig

<!-- formula-not-decoded -->

Or, written as a single vector equation,

<!-- formula-not-decoded -->

- () As for a single equation; we try an exponential function of t;,

<!-- formula-not-decoded -->

ev

Then; writing 0? = dividing by we get

<!-- formula-not-decoded -->

12. The system is

Eigenvalues and eigenvectors are

<!-- formula-not-decoded -->

Since 0 = VA and V-1 = +i and V-6 = +iVo, we get

<!-- formula-not-decoded -->

or, by (7) in Sec. 2.3,

<!-- formula-not-decoded -->

c4). These four arbitrary constants can be specified by four initial conditions. In components; this solution is i(c;

<!-- formula-not-decoded -->

- (c) The conversion is done by the formulas

<!-- formula-not-decoded -->

This gives the matrix

<!-- formula-not-decoded -->

Eigenvalues and eigenvectors are

<!-- formula-not-decoded -->

Denoting these complex vectors by z1), have as a general solution we

<!-- formula-not-decoded -->

The first and third components are

<!-- formula-not-decoded -->

Converting this to real form by means of the Euler formula (Sec. 2.3) we obtain the same result as in (), except for notations.

## SECTION 3.2. Basic Concepts and Theory, page 159

Purpose. This survey of some basic concepts and facts on nonlinear and linear systems is intended to give the student an impression of the conceptual and structural similarity of the theory of systems to that of single differential equations.

## Content, Important Concepts

Standard form of first-order systems

Form of corresponding initial value problems

Existence of solutions

Basis, general solution; Wronskian

Background Material. Sec. 2.7 contains the analogous theory for single equations. See also Sec. 1.9.

Short Courses. This section may be skipped, as mentioned before.

## SECTION 3.3. Homogeneous Linear Systems with Constant Coefficients. Phase Plane, Critical Points, page 162

Purpose. Typical examples are intended to show the student the rich variety of pattern of solution curves (trajectories) near critical points in the phase plane; with the process of actually solving homogeneous linear systems. This will also prepare the student for a good understanding of the systematic discussion of critical points in the phase plane in Sec. 3.4. along

## Main Content

Solution method for homogeneous linear systems

Examples illustrating types of critical points

Solution when no basis of eigenvectors is available

## Important Concepts and Facts

Trajectories as solution curves in the phase plane

Phase plane as a means for the simultaneous (qualitative) discussion of a number of solutions

Basis of solutions obtained from basis of eigenvectors

Background MateriaL. Short review of eigenvalue problems from Sec. 3.0, if needed.

Short Courses. Omit Example 6

## Some Details on Content

In addition to developing skill in solving homogeneous linear systems; the student is supposed to become aware that it is the kind of eigenvalues that determine the type of critical point. The examples show important cases. (A systematic discussion of all cases follows in the next section )

Example 2 A real double eigenvalue gives a node.

Example 1. Two negative eigenvalues give a node.

Example 3. Real eigenvalues of opposite sign give a saddle point.

Example 5. Genuinely complex eigenvalues give a spiral point. Some work in complex can be avoided, if desired, by differentiation and elimination: The first equation is

Example 4 Pure imaginary eigenvalues give a center, and working in complex is avoided by a standard trick, which can also be useful in other contexts .

<!-- formula-not-decoded -->

differentiation and from the second equation as well as (a) By

Complex solutions e(-1+t give the real solution

<!-- formula-not-decoded -->

From this and (a) follows the expression for y2 given in the text.

Example 6 shows that the present method can be extended to include cases when A does not provide a basis of eigenvectors; but then becomes substantially more involved. In this way the student will recognize the importance of bases of eigenvectors, which also play a role in many other contexts.

<!-- formula-not-decoded -->

## SOLUTIONS TO PROBLEM SET 3.3, page 169

2. The eigenvalues are -~3 and 4. Eigenvectors are [2 ~5]T and [1 The corresponding general solution ïs

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 4 The eigenvalues are 3 and 9. Eigenvectors are [3 ~I]T and [3 1]T , respectively. The corresponding general solution is

<!-- formula-not-decoded -->

6. The matrix has the double eigenvalue -6. An eigenvector is [1 vector u needed is obtained from

<!-- formula-not-decoded -->

We can take u = ~2] With this we obtain as a general solution

<!-- formula-not-decoded -->

8. The eigenvalue ~3 has two linearly independent eigenvectors, which we can choose as [1 0 0]T and [0 1]7. The second eigenvalue is ~6. A corresponding eigen vector is [1 1 ~1]T. This gives the solution

<!-- formula-not-decoded -->

16. The restriction of the inflow from outside to pure water is necessary to obtain a homogeneous system: The principle involved in setting up the model is

Time rate of Inflow Outflow . change

For Tank T1 this is (see 84) Fig;

For Tank T2 it is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Performing the divisions and ordering terms; we have

<!-- formula-not-decoded -->

The eigenvalues of the matrix of this system are ~0.04 and ~0.12. Eigenvectors are

- [1 2]T and [1 ~2]7, respectively . The corresponding general solution is

<!-- formula-not-decoded -->

The initial condition is y1(0) = 200. This gives c1 100, C2 = 0. In components the answer is

<!-- formula-not-decoded -->

Both functions approach zero as t ~&gt; %, a reasonable result because pure water flows in and mixture flows out.

18. Differentiate the first given equation;

Solve algebraically for Ií, substituting I2 from the second given equation. Solve the second equation algebraically for I2. Then we have the system in the usual form given

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This gives the characteristic equation

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Hence the eigenvalues are real if and only if

<!-- formula-not-decoded -->

20. TEAM PROJECT. From the complex solution in Example 4 we can obtain real basis and a real general solution by the Euler formula (Sec. 2.3), which we need in the form

<!-- formula-not-decoded -->

Collecting the real and imaginary parts; we thus obtain in the complex solution (12*)

<!-- formula-not-decoded -->

and similarly

Thus the matrix is and the eigenvalues

<!-- formula-not-decoded -->

Substitution into (12) shows that the real part and the imaginary part in (A),

<!-- formula-not-decoded -->

are solutions. These real solutions form a basis because their Wronskian is not zero,

<!-- formula-not-decoded -->

Hence a real general solution of (12) is

<!-- formula-not-decoded -->

This represents the same ellipses as before because by calculation and simplification we find

<!-- formula-not-decoded -->

We turn to Example (5). The complex solution is

<!-- formula-not-decoded -->

We derive from this a real general solution: In (B) we have

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

and v\_as can be seen by substitution. They form a basis because their Wronskian is not zero.

<!-- formula-not-decoded -->

The corresponding real general solution is

<!-- formula-not-decoded -->

in components;

<!-- formula-not-decoded -->

It represents spirals (see 82). To see this, we introduce the usual coordinates r, 0 in the y1yz-plane defined by Fig; polar

<!-- formula-not-decoded -->

Then by straightforward calculation   and simplification of the result we obtain from (C)

<!-- formula-not-decoded -->

where = VA? + B2 and 0 = ~t. For each co this represents a spiral, as claimed. The origin is a spiral of the system (13) Co point

## SECTION 3.4. Criteria for Critical Points. Stability, page 170

Purpose. Systematic discussion of critical in the plane from the standpoints of both the geometrical shapes of trajectories and stability. points phase

## Main Content

Formula (9) for the types of critical points

Formula (10) for the stability behavior

Stability chart, giving (9) and (10) graphically

## Important Concepts

Node, saddle point; center, spiral point

Stable and attractive, stable, unstable

Background Material. Sec. 2.5 (needed in Example 2)

Short Courses. Since all those types of critical points already occurred in the previous section; one may perhaps present just a short discussion of stability .

## Some Details on Content

The types of critical points in Sec. 3.3 now recur, and the discussion shows that haust all possibilities. With the examples of Sec. 3.3 fresh in mind, the student will acquire a deeper understanding by discussing the stability chart and by reconsidering those examples from the viewpoint of stability. This gives the instructor an opportunity to emphasize that the general importance of stability in engineering can hardly be overesti mated. they

Example 2, relating to the familiar free vibrations in Sec. 2.5, gives a good illustration of stability behavior; namely, depending on c; attractive stability, stability (and instability if one includes 'negative damping; with c &lt; 0, as it will recur in the next section in connection with the famous van der Pol equation).

## SOLUTIONS TO PROBLEM SET 3.4, page 174

2. p = 0, 9 = ~9, saddle point; always unstable. A general solution is

<!-- formula-not-decoded -->

4. p = ~12, 9 = 27, A = 144 108 &gt; 0, stable and attractive node. A general solution is

<!-- formula-not-decoded -->

- 6 ~36, center; always stable. A complex general solution; as ob tained directly from the characteristic equation, is

<!-- formula-not-decoded -->

The conversion to real form takes patience:

1. Take the simpler of the two components and multiply everything out. Then collect the cosine and the sine terms and choose a notation for their coefficients, say, A and B.
2. Express c1 and c2 in terms of A and B.
3. Substitute the result just obtained into the first component and simplify .

In the present case the second component; Y2; is simpler:

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

In the second step we solve this for C1 and c2, obtaining

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In the third step we turn to the first component;

<!-- formula-not-decoded -->

Expressing c1 and c2 in terms of A and B and simplifying (in this operation; imagi nary terms must drop out by cancellation) we obtain

<!-- formula-not-decoded -->

8. p = ~10, saddle point, always unstable. A general solution is

<!-- formula-not-decoded -->

10. We could solve the first equation; Y1 C1e-t and insert this into the second equagle independent eigenvector, say, [0 1]T, s0 that we have no eigenbasis and have to determine u from

<!-- formula-not-decoded -->

This gives 1, W1 = ~1/5, u2 = 0. A general solution is ~5u1

<!-- formula-not-decoded -->

The critical is a degenerate node, which is stable and attractive. point

- 12 y = A cos

<!-- formula-not-decoded -->

This is obtained as in Example 4 in Sec. 3.3.

14. y = e-t(A cos t + B sin t). The trajectories are stable and attractive spirals.
18. At a center, p + a22 = 0, 9 = det A &gt; 0, hence 4 &lt; 0. Under the change p changes into a11 + k + + k = 2k # 0; 9 remains positive because
16. yí = form; we have to multiply the transformed system by -1, which amounts to multiplying the matrix by ~1, changing p into ~p, but leaving 9 and 4 unchanged. In the example, we get an unstable node.

<!-- formula-not-decoded -->

Finally remains unchanged because

<!-- formula-not-decoded -->

Hence we obtain a spiral point, which is unstable if k &gt; 0 and stable and attractive if k &lt; 0

We can reason more simply as follows. For a center the eigenvalues are pure imag + k of A, causing a damped oscillation (when k &lt; 0) or an increasing one (when k &gt; 0), thus a spiral.

## SECTION 3.5. Qualitative Methods for Nonlinear Systems, page 175

Purpose. As a most important step, in this section we extend phase plane methods to nonlinear systems and nonlinear equations.

## Main Content

Critical of nonlinear systems points

- Their discussion by linearization

Transformation of single autonomous equations

Applications of linearization and transformation techniques

## Important Concepts and Facts

Linearized system (3), condition for applicability

Linearization of pendulum equations

Self-sustained oscillations, van der Pol equation

Short Courses. Linearization at different critical points seems the main issue that the stu dent is supposed to understand and handle practically . Examples 1 and 2 may help students skill in that technique. The other material could be skipped without loss of continuity . gain

## Some Details on Content

This section is very important, because from it the student should learn not only techniques (linearization; etc) but also the fact that phase plane methods are particularly pow erful and important in application to systems or single equations that cannot be solved ex plicitly. The student should also recognize that it is quite surprising how much information these methods can give. This is demonstrated by the pendulum equation (Examples 1 and 2) for a relatively simple system; and by the famous van der Pol equation for a single equation; which has become prototype for self-sustained oscillations of electrical systems of various kinds.

For the Rayleigh and Duffing equations; see the problem set.

We also discuss the famous Lotka-Volterra predator-prey modeL.

## SOLUTIONS TO PROBLEM SET 3.5, page 183

4. (nm, 0) saddle points for even n and centers for odd n
6. At (0, 0) Yí = y2 Y2 = ~Y1 P = 0, 9 = 1, 4 = ~4, center. The other critical + = = point point.

<!-- formula-not-decoded -->

Now ~Y1 = Y1(-1 + y1?) = 0 shows that there are three critical points; at Y2) = (0, 0), (~1, 0), and (1, 0).

The linearized system at (0, 0) is

<!-- formula-not-decoded -->

From the matrix we see that p = 1. Hence (0, 0) is a center (see Sec. 3.4)

For the next critical we have to linearize at (~1, 0) by setting point

Then

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Hence the linearized system is

<!-- formula-not-decoded -->

Hence 9 = det A = ~2 &lt; 0, that is, the critical Similarly, to linearize at (1, 0), set point point.

Then

<!-- formula-not-decoded -->

and we obtain another saddle point; as just before.

## 10. The equation gives the system

Now

<!-- formula-not-decoded -->

involves quadratic equation in y1 with solutions y12 = 1, 4. Hence the zeros of f(y1) are 42, +1, 0 and give the five critical points 0) with y1 = ~2, -1, 0, 1, 2 (y1

Linearization leads to the result that (0, 0), (~2, 0), and (2, 0) are centers   and (~1, 0), (1, 0) are saddle points.

For instance, at (0, 0), linearize to

<!-- formula-not-decoded -->

At the other points some work may be saved by setting

<!-- formula-not-decoded -->

and substituting y1 = ~2 + ñ1 at (~2, 0) (etc. for the others) and finding

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

More savings follow by noting that every linearized system is of the form

<!-- formula-not-decoded -->

Now

<!-- formula-not-decoded -->

is positive at 0 and +2, thus giving centers; and negative at +1, giving saddle points, as asserted.

y22 4y12 \_ + or (see the figure on the next page) C*

<!-- formula-not-decoded -->

14. Critical points at (0, 0), (2, 0), (~2, 0). Linearization leads to the following:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

which gives stable and attractive spiral (instead of centers) . points

Note the similarity to the situation in the case of the undamped and damped pendulum equations.

16. TEAM PROJECT. (a) Unstable node if 2 2, unstable spiral = 0, stable and attractive spiral point if 0 &gt; J &gt; ~2, stable and attractive node if u = -2 point

<!-- formula-not-decoded -->

giving the linearized system

<!-- formula-not-decoded -->

Section 3.5. Problem 12

<!-- image -->

By integration on both sides,

<!-- formula-not-decoded -->

## SECTION 3.6. Nonhomogeneous Linear Systems, page 184

Purpose.  We now turn from homogeneous linear systems considered so far to solution methods for nonhomogeneous systems.

## Main Content

Method of undetermined coefficients

Modification for special right sides

Method of variation of parameters

Method of diagonalization

Short Courses. Select just one or two of the preceding methods.

## Some Details on Content

In addition to understanding the solution methods as such, the student should observe the conceptual and technical similarities to the handling of nonhomogeneous linear differen tial equations in Secs. 2.8-2.12 and 2.15 and understand the reason for this, namely, that systems can be converted to single equations and conversely. For instance, in connection with Example 2 in this section; one may point to the Modification Rule in Sec. 2.9, or, if time permits; establish an even more definite relation by differentiation and elimination of y2,

<!-- formula-not-decoded -->

solving this for y1 and then getting y2 from the solution

## SOLUTIONS TO PROBLEM SET 3.6, page 189

2. The eigenvalues are ~2 and 2. Eigenvectors are [1 ~I]T and [1 1]T, respectively. A particular solution can be obtained by the method of undetermined coefficients. Answer:

<!-- formula-not-decoded -->

4. The eigenvalues are ~1 and 2, with eigenvectors [1 1]T and [1 4]7, respectively. By the method of undetermined coefficients have to assume, say, Y1 = A1 cos t + B1 sin t; similarly for y2: Answer: we

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

6. The eigenvalues are 2 and 5, with eigenvectors [1 ~2]T and [1 1]7, respectively. Answer:

<!-- formula-not-decoded -->

8. From the characteristic equation obtain we

<!-- formula-not-decoded -->

By the method of undetermined coefficients, we set

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We now compare componentwise the constant terms, linear terms, and quadratic terms:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The corresponding general solution is in components;

<!-- formula-not-decoded -->

From this and the initial conditions Y1(0) = 3, Y2(0) = 1 we obtain c1 = 2, C2 = 1

By substitution,

<!-- formula-not-decoded -->

Answer:

<!-- formula-not-decoded -->

10. From the characteristic equation,

<!-- formula-not-decoded -->

can be obtained by the method of undetermined coefficients, starting from

Substitution gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Comparing sinh terms and cosh terms (componentwise), we get from this

<!-- formula-not-decoded -->

To solve this, one can substitute the first two equations into the last two, solve for b1 = 2, b2 = 1, and then get from the first two equations a1 a2 = 0 This gives the general solution

<!-- formula-not-decoded -->

From the initial conditions we see that c1 = 0, c2 = 0, s0 that the general solution does not contribute to the answer\_ This is not automatically the case when we have Y1(0) = 0, y2(0) = 0, but is a consequence of the fact that y(p) at t 0 is the zero vector. Answer: Y1 = 2 sinh t, Y2 sinh t.

<!-- formula-not-decoded -->

lution of the homogeneous system. Hence, to find y(p) we have to proceed as in Ex ample 2, setting

Substitution gives

<!-- formula-not-decoded -->

Equating the terms in e (componentwise) gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and the terms in tet give

Hence u1 = 1, u2 = = 1, 02 = 0. This gives the general solution

<!-- formula-not-decoded -->

From the initial conditions we obtain c1 = ~2, C2 = 5. Answer:

<!-- formula-not-decoded -->

- 14 A general solution of the homogeneous system is

<!-- formula-not-decoded -->

Answer:

<!-- formula-not-decoded -->

16. The formula for shows that these various choices differ by multiples of the eigenvector for à = ~2, which can be absorbed into, or taken out of, c1 in the general s0(h) lution y
18. The equations are

<!-- formula-not-decoded -->

and

Thus

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

which, upon differentiation and insertion of I1 from (a) and simplification; gives

<!-- formula-not-decoded -->

The general solution of the homogeneous system is as in Prob. 17, and the method of undetermined coefficients gives as a particular solution

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SOLUTIONS TO CHAPTER 3 REVIEW, page 190

16. Eigenvalues =1, 6. Eigenvectors [1 [4 lution is

<!-- formula-not-decoded -->

The critical at (0, 0) is a saddle point, which is always unstable. point

<!-- formula-not-decoded -->

The critical point at (0, 0) is a center; which is always stable.

20. Y1 = Y2 = ~t 3c2e ~2t stable and attractive node C1e-t cze-2t ~2c1e

<!-- formula-not-decoded -->

- = Y2 = gc1e3t ~t. saddle point

<!-- formula-not-decoded -->

- A? has the eigen values p1 = and J2 =

<!-- formula-not-decoded -->

30. The matrix of the system is
2. A cos 2t + B sin 2t. From this and the first equation,

<!-- formula-not-decoded -->

where A = RIL and B = IIRC. A general solution is

<!-- formula-not-decoded -->

and the initial conditions give C1 ~1/3 and C2 1/3.

- = tion. This gives the system

<!-- formula-not-decoded -->

Eigenvalues À = ~0.1127, ~0.8873; corresponding eigenvectors:

<!-- formula-not-decoded -->

Answer:

<!-- formula-not-decoded -->

with c1 ~101.6 and c2 = 1.64 from the initial conditions.

## 34. A general solution is

<!-- formula-not-decoded -->

- Undetermined coefficients: This is much simpler than the other two methods. Y1 At + B, Y2 = Ct + D. By substitution; A =Ct + D + t, C = -At B; thus C =

- (II) Variation of parameters: We write c =

<!-- formula-not-decoded -->

where the last term is a solution of the homogeneous system.

(II) Diagonalization can be done in complex. À1 = ~i, and

<!-- formula-not-decoded -->

as expected. Also,

<!-- formula-not-decoded -->

Thus

Particular solutions are

<!-- formula-not-decoded -->

and thus

<!-- formula-not-decoded -->

36. (nu, 0) centers (n integer)

38. Critical points at (0, 0) and (0, ~1). The linearized systems are

<!-- formula-not-decoded -->

where Y1 = ñ1 and y2 = a saddle point.

## Series Solutions of Differential Equations Special Functions

## Changes

This chapter has been streamlined and shortened by presenting the material on Bessel functions in a more condensed form and several minor changes to make it more teachable; without the opportunity to familiarize the student with an overview of some of the techniques used in connection with higher special functions. losing

## SECTION 4.1. Power Series Method, page 194

Purpose. A simple introduction to the technique of the power series method in terms of simple examples whose solution the student knows very well.

## SECTION 4.2. Theory of the Power Series Method; page 198

Purpose. Review of power series and a statement of the basic existence theorem for power series solutions (without proof, which would exceed the level of our presentation)

## Main Content, Important Concepts

Radius of convergence (7)

Differentiation; multiplication of power series

Technique of index shift

Real analytic function (needed again in Sec. 4.4)

## Comment

Depending on the preparation of the class; skip the section or discuss just a few less known facts.

## SOLUTIONS TO PROBLEM SET 4.2, page 204

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

8. y = a1x + ao(1 ') [This is a particular case of Legendre' s equation (n I), which we consider in Sec. 4.3.]

<!-- formula-not-decoded -->

where A = ao cosh 1 a1 sinh 1, B = a1 cosh 1 ao sinh 1.

- of x, because of In x. The reason is that the coefficient llx of the equation is not analytic at x = 0. If we substitute a power series in powers of x into xy' = y + x, we = 0, a1 = a1 + 1, a contradiction.

<!-- formula-not-decoded -->

22. TEAM PROJECT. The student should see that power series reveal many basic properties of the functions that represent. The familiarity with the functions considered should help students understand the basic idea without being iritated by unfamiliar notions or notations and more involved formulas. Some of the tasks in (d) illustrate that not all properties become immediately visible; although all of them are determined by the sequence of the coefficients . they
24. (m4 2)(m + I)xm, 1 m=0
26. CAS PROJECT. (a) It is instructive to see how polynomials of increasing degree follow more and more the cosine curve and then at a distinctly noticeable begin to go their own way (see the figure). Some calculus books also show this, but students may have forgotten; s0 this reminder serves a purpose. Those 'qualitative" break-away points are very roughly at 1, 2, 3 Of course, for quantitative information; one would need more exact analytical estimates of remainders. point good
4. (b) The plot in the figure suggests that all the partial sums are even functions and that convergence seems to take place for =1 &lt;x &lt; l; of course, this does not prove that the convergence radius is 1. Divide the equation by the coefficient of y to see that we cannot expect convergence in a larger interval because 1 x2 is zero at x 4l. The series solution is

<!-- image -->

<!-- formula-not-decoded -->

CAS Project 26(b)

<!-- image -->

## SECTION 4.3. Legendre's Equation. Legendre Polynomials Pn(x) page 205

Purpose; This section on Legendre' s equation; one of the most important equations; and its solutions is more than just an exercise on the power series method: It should give the student a feeling for the usefulness of power series in exploring properties of special functions and for the wealth of relations between functions of a one-parameter family (with parameter n)

## Comment on Literature and History

Legendre's equation occurs again in Secs. 4.7,4.8, and 11.11.

For literature on Legendre' s equation and its solutions; see Refs. [1], [6], [11].

Legendre's work on the subject appeared in 1785 and Rodrigues' contribution (see Prob. 6) in 1816.

## SOLUTIONS TO PROBLEM SET 4.3, page 209

## 6. We have

<!-- formula-not-decoded -->

Differentiating times, we can express the   product of occurring factors (2n 2m)(2n 2m 1) as the quotient of factorials and get

<!-- formula-not-decoded -->

with M Then the left side equals the right side in Rodrigues' s formula and the right side equals the right side of (11)

10. TEAM PROJECT. (a) Following the hint; we obtain

<!-- formula-not-decoded -->

and for the general term on the right

<!-- formula-not-decoded -->

Now u" occurs in the first term of the expansion (B) of (2xu u2)", in the second term of the expansion (B) of (2xu u2)"-1, and s0 on. From (A) and (B) we see that the coefficients of u" in those terms are

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and so on. This proves the assertion.

- (b) Set u r1lr2 and x cos 0
- Use the formula for the sum of the geometric series and set x =1 Then set x 0 and use

<!-- formula-not-decoded -->

- (d) Abbreviate 1 2xu + u2 U. Differentiation of (13) gives

<!-- formula-not-decoded -->

Multiply this equation by U and represent by (13): U-1/2

<!-- formula-not-decoded -->

In this equation; has the coefficients

<!-- formula-not-decoded -->

Simplifying gives the asserted Bonnet recursion.

<!-- formula-not-decoded -->

## SECTION 4.4. Frobenius Method, page 211

Purpose. To introduce the student to the Frobenius method (an extension of the power series method) , which is important for equations with coefficients that have singularities; notably Bessel' s equation; so that the power series method can no longer handle them. This extended method requires more patience and care\_

## Main Content, Important Concepts

Regular and singular points

Indicial equation;, three cases of roots (one unexpected)

Frobenius theorem; forms of bases in those cases

Short Courses. Take a look at those bases in Frobenius' s theorem, say how it fits with the Euler-Cauchy equation; and omit everything else. quick

These terms are used in some books and papers; but there is hardly any need for confusthe student by using them; simply because we cannot do (and don'tdo) anything about 'iregular singular points. complex analysis, where holomorphic functions are also known as 'regular analytic functions") may thus be the best terminology. ing

## Comment on Footnote 11

Gauss was born in Braunschweig (Brunswick) in 1777. At the age of 16, in 1793 he discovered the method of least squares (Secs. 18.5, 23.9) From 1795 t0 1798 he studied at Göttingen. In 1799 he obtained his doctor' s degree at Helmstedt. In 1801 he published

his first masterpiece; Disquisitiones arithmeticae (Arithmetical Investigations; begun in 1795), thereby initiating modern number In 1801 he became generally known when his calculations enabled astronomers (Zach; Olbers) to rediscover the planet Ceres; which had been discovered in 1801 but had been visible only very briefly. He became the director of the Göttingen observatory in 1807 and remained there until his death. In 1809 he published his famous Theoria motus corporum coelestium in sectionibus conicis solem ambientium (Theory of the Heavenly Bodies Moving About the Sun in Conic Sections; Dover Publications; 1963), resulting from his further work in astronomy. In 1814 he developed his method of numerical integration (Sec. 17.5). His Disquisitiones generales circa superficies curvas (General Investigations Regarding Curved Surfaces; 1828) represents the foundation of the differential geometry of surfaces and contributes to confor mal mapping (Sec. 12.5). His clear conception of the complex plane dates back to his the sis, whereas his first publication on this topic was not before 1831. This is typical: Gauss left many of his most outstanding results (non-Euclidean geometry, elliptic functions; etc.) unpublished.  His paper on the hypergeometric series published in 1812 is the first systematic investigation into the convergence of a series; it allows a study of special functions from a single of view theory . many point

## SOLUTIONS TO PROBLEM SET 4.4, page 216

2. Y1 = x + 1, Y2 = Il(x + 1). Check: Set x + 1 = z to get an Euler-Cauchy equation.
4. Substitution of (2) and the derivatives (2*) gives

<!-- formula-not-decoded -->

this out, we have Writing

<!-- formula-not-decoded -->

By equating the sum of the coefficients of to zero we obtain the indicial equation rr-1

<!-- formula-not-decoded -->

The roots are r1 = 2 and r2 = 0. This is Case 1.

By equating the sum of the coefficients of in (A) to zero we obtain (take = s + 1 in the first two series and m = s in the last series)

<!-- formula-not-decoded -->

By simplification we find that this can be written

<!-- formula-not-decoded -->

We solve this for as+1 in terms of as:

<!-- formula-not-decoded -->

First solution. We determine first solution y1(x) corresponding to r1 = For r1 formula (B) becomes

<!-- formula-not-decoded -->

From this we get successively

<!-- formula-not-decoded -->

In many practical situations an explicit formula for am will be rather complicated Here it is simple: by successive substitution we get

<!-- formula-not-decoded -->

and in general, taking % 1,

<!-- formula-not-decoded -->

Hence the first solution is

<!-- formula-not-decoded -->

Second solution. If you recognize y1 as a familiar function; apply reduction of order (see Sec. 2.1). If not, start from (6) with r2 0. For r Y2 0, formula (B) [with As+1 and As instead of as+1 and as becomes

<!-- formula-not-decoded -->

From this we get successively

<!-- formula-not-decoded -->

and by successive substitution we have

<!-- formula-not-decoded -->

and in general, taking Ao 1,

<!-- formula-not-decoded -->

Hence the second solution, of the form (6) with r2 = 0, is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

16. TEAM PROJECT. (b) In (7b), Sec. 4.2,

<!-- formula-not-decoded -->

hence R = 1.

- In the second line;

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) The roots can be read from (15), brought to the form (1' ) by multiplying it by x and dividing by 1 \_ x; then bo = c in (4) and co

<!-- formula-not-decoded -->

## SECTION 4.5. Bessels Equation. Bessel Functions J,(x), page 218

Purpose; To derive the Bessel functions of the first kind J, and J\_v by the Frobenius method. (This is a major application of that method:) To show that these functions constitute a basis if vis not an integer; but are linearly dependent for integer v = n (so that we must look later; in Sec. 4.6, for a second linearly independent solution). To show that various differential equations can be reduced to Bessel's equation (see Problem Set 4.5).

## Main Content; Important Concepts

Derivation just mentioned

Linear independence of Jv and if vis not an integer J\_v

Linear dependence of Jv and if v = n = 1,2, J\_v

Gamma function as a tool

Short Courses. No derivation of any of the series. Discussion of Jo and J (which are similar to cosine and sine) . Mention Theorem 2.

## Comment on Special Functions

Since various institutions no longer find time to offer a course in functions; Bessel functions may give another opportunity (together with Sec. 4.3) for getting at least some feeling for the flavor of the theory of special functions; which will continue to be of some significance to the engineer and physicist: For this reason we have added some material on basic relations for Bessel functions in this section. special

## SOLUTIONS TO PROBLEM SET 4.5, page 226

From a practical point of view, this is probably the most frequently occurring case. Problems 1-10 are for gaining skill and making the student aware of the fact that Bessel' s equation; just as the hypergeometric equation in Problem Set 4.4, is a member of a large family of equations that can be solved in terms of Bessel functions, a fact that adds to the great importance of these functions.

<!-- formula-not-decoded -->

6. Jo(Vz)

10. and we do not get a general solution; by Theorem 2\_ x3Js(x)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where m = 1.

- 2m+2 2m X x fixed).
16. We obtain the following values. Note that the relative error of this very crude approximation is rather small.
18. Let x &gt; 0 We have Jo(x) = + Rq(x), S2(x) Jo(x) S4(x), S2(xo) 0 &lt; S4(xo); hence *1 &lt; Xo &lt; X2, where X1 = 2 and x2 = V8 are defined by s2(x1) = 0, S4(x2) = 0
- (25) with v = 0 is

|     |   Approximation |   Exact (4D) | Relative Error (9   |
|-----|-----------------|--------------|---------------------|
| 0   |          1      |       1      |                     |
| 0.1 |          0.9975 |       0.9975 |                     |
| 0.2 |          0.99   |       0.99   |                     |
| 0.3 |          0.9775 |       0.9776 | 0.01                |
| 0.4 |          0.96   |       0.9604 | 0.04                |
| 0.5 |          0.9375 |       0.9385 | 0.1                 |
| 0.6 |          0.91   |       0.912  | 0.2                 |
| 0.7 |          0.8775 |       0.8812 | 0.4                 |
| 0.8 |          0.84   |       0.8463 | 0                   |
| 0.9 |          0.7975 |       0.8075 | 1.2                 |
| 1   |          0.75   |       0.7652 | 2.0                 |

<!-- formula-not-decoded -->

- Together; J1 has at least one zero between two consecutive zeros of Jo Furthermore, (xJ)' =0 at least once between two consecutive zeros of xJ1, hence

of J1 (also at x = 0 since J1(0) = 0), by Rolle' s theorem. Now (24) with v = 1 is

Together, Jo has at least one zero between two consecutive zeros of J1

22.  Integrate (24).

24.  Integrate (27).

26.  Integrate (24) with v = 2 to get

<!-- formula-not-decoded -->

Integrate (24) with v = 1 to get

Integrating by parts, (b); and again; using (a), we get using

<!-- formula-not-decoded -->

28. TEAM PROJECT. Assuming small angles Q in the displacement; we can regard W() to be approximately equal to the tension acting: tangentially in the moving cable. The restoring force is the horizontal component of the tension. For the difference in force we use the mean value theorem of differential calculus. By Newton S second law this equals the mass pAx times the acceleration utt of this portion of the cable. The substitution of u first gives

<!-- formula-not-decoded -->

Now the cosine factor; perform the differentiation; and order the terms 0) dx = ~dz and by the chain rule, drop

<!-- formula-not-decoded -->

In the next transformation the chain rule gives

<!-- formula-not-decoded -->

Substitution gives

<!-- formula-not-decoded -->

24z1/2.

- This follows from the fact that the upper end (x = 0) is fixed. The second pormal mode looks similar to the portion of Jo between the second positive zero and the origin Similarly for the third normal mode. The first positive zero is about 2.405. For the cable of 2 meters this gives the frequency

<!-- formula-not-decoded -->

Similarly, we obtain 11.4 cycleslmin for the cable. long

30. CAS PROJECT. (b) X = 1, X1 = 2.5, = 20,  approximately .  It increases with n.
2. (c) (14) is exact.

- It oscillates.
- (e) Formula (25) with v = 0

## SECTION 4.6. Bessel Functions of the Second Kind, page 228

Purpose. Derivation of a second independent solution; which is still missing in the case of v = = 0, 1,

## Main Content

Detailed derivation of Yo(x)

Cursory derivation of Yn(x) for any n

General solution (9) valid for all v integer or not

Short Courses. Omit this section.

## Comment on Hankel Functions and Modified Bessel Functions

These are included for completeness; but will not be needed in our further work.

## SOLUTIONS TO PROBLEM SET 4.6, page 232

- 4 Substitute y and its derivatives into the given equation and multiply the resulting equation by x3/2 to get ux1/2

<!-- formula-not-decoded -->

Now introduce z as given in the problem statement to the answer get

<!-- formula-not-decoded -->

- x [AJus(gkr3/2) + equation. Its solutions ("Airy functions' have been extensively investigated; for some formulas and see M. Abramowitz and I. A. Stegun [1], pp. 446-52, listed in Appendix 1. graphs,
8. Vx 4
14. Use (20) in Sec. 4.5.
16. Since Iv is a solution of (12), so is I\_v because (12) involves and is linear and homogeneous. Hence Kv is a solution of (12)

The problem illustrates that for different purposes different special functions were introduced and investigated. It would lead us too far to show applications where those Kv are of practical advantage. See Watson' s standard treatise [A7] in Appendix 1.

## SECTION 4.7. Sturm-Liouville Problems. Orthogonal Functions; page 233

Purpose. Discussion of eigenvalue problems for ordinary second-order differential equations (1) under boundary conditions (2)

- = = = 7.07

## Main Content, Important Concepts

Sturm-Liouville equations; Sturm-Liouville problem

Reality of eigenvalues

Orthogonality of eigenfunctions

Orthogonality of Legendre polynomials and Bessel functions

Short Courses. Omit this section.

## Comment on Importance

This theory owes its significance to two factors: On the one hand; boundary value lems involving practically important equations (Legendre' s, Bessel' s, etc.) can be cast into Sturm-Liouville form s0 that here we have a general theory with several important par tral theory of those problems. prob -

## Comment on Existence of Eigenvalues

This theory is difficult. Quite generally, in problems where we can have infinitely many eigenvalues; the existence problem becomes nontrivial; in contrast to matrix eigenvalue problems (Chap: 7), where existence is trivial; a consequence of the fact that a polynomial equation f(x) 0 (f not constant) has at least one solution and at most n numerically different ones (n the degree of the polynomial).

## SOLUTIONS TO PROBLEM SET 4.7, page 238

- because (1) is linear and homogeneous; here, = the eigenvalue corresponding to ym: Also; multiplying (2) with y = Ym by C, see that zm also satisfies the boundary conditions. This proves the assertion. Zm Ams we
- Yn(x) = sin (nuxlL)
- Yo(x) 1, Yn(x)
- Yn(x) = sin nx

12. The kn as intersections of 2 = tan k and z = see the figure. ko ~ 2.029, k1 4.913, approximately .
10. y" + Ay = 0, y0) = 0,

Section 4.7. Problem 12

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SECTION 4.8. Orthogonal Eigenfunction Expansions, page 240

Purpose. To show how families (sequences) of orthogonal functions; as arise in eigenvalue problems and elsewhere, are used in series for representing other functions; and to show how orthogonality becomes crucial in simplifying the determination of the coefficients of such a series by integration. they

## Main Content, Important Concepts

Standard notation Yn

Orthogonal expansion (3), eigenfunction expansion

Fourier constants (4)

Fourier series (5), Euler formulas (6

Short Courses. Omit this section.

## Comment on Flexibility on Fourier Series

Since Sec. 4.8, with the definition of orthogonality taken from Sec. 4.7 and Examples 2 and 3 omitted, is independent of other sections in this chapter, it could also be after Chap. 10 on Fourier series. We did not put it there for reasons of time and because Chap: 10 is intimately related to the main applications of Fourier series (to partial differential equations) in Chap. 11. used

## Comment on Notation

yn) is not a must; but has become standard; perhaps if it is written out a few times; it will stop irritating poorer students.

## SOLUTIONS TO PROBLEM SET 4.8, page 246

2. By (7), where f(x) is the given polynomial; or by undetermined coefficients; starting from

<!-- formula-not-decoded -->

and equating coefficients of like powers on both sides; we get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Answer:

<!-- formula-not-decoded -->

8. From (7) we obtain

<!-- formula-not-decoded -->

10. TEAM PROJECT. (b) A Maclaurin series f(t) has the coefficients @n antn

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) = tG = 2 Hen-1lr)t"I(n
- and use (21). By integrations by parts, for n &gt; m, etc.,

<!-- formula-not-decoded -->

- e nxHen-1 from (22) with n 1 instead of n. In this equation; the first term on the right equals by (21). The last term equals as follows by differentiation of (21). nHen nHen-1 xHen ~Hen,

We write y Ew, where E = Then y = y" e22/4

<!-- formula-not-decoded -->

Substitute this into the differential equation (23) and divide by E to get the result. The is that the new equation does not contain a first derivative; hence our transformation is precisely that for eliminating the first derivative from (23). point

## SOLUTIONS TO CHAPTER REVIEW, page 247

16. (x 2)2, (x This is an Euler Cauchy equation with independent variable t = x ~

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

## CHAPTER 5 Laplace Transforms

## Major Changes

The first shifting theorem has been moved ahead to Sec. 5.1, where it fits much better and helps to simplify the presentation: Further streamlining has been achieved by placing the unit step function and Dirac' s delta in the same section (Sec. 5.3). The impractical theoretical formulas for the Laplace transforms of partial fractions have been replaced by more practical approach in terms of examples related to (Sec. 5.6). The application of the Laplace transform to systems of differential equations is discussed in the new Sec. 5.7. key

## SECTION 5.1. Laplace Transform. Inverse Transform. Linearity. Shifting; page 251

Purpose. To explain the basic concepts; to present a short list of basic transforms, and to show how these are derived from the definition.

## Main Content, Important Concepts

Transform; inverse, linearity

First theorem shifting

Table 5.1

Existence and its practical significance

## Comment on Table 5.1

After working for a while in this chapter, the student should be able to memorize these transforms. Further transforms in Sec. 5.9 are derived as we go many of them from Table 5.1. along;

## SOLUTIONS TO PROBLEM SET 5.1, page 257

<!-- formula-not-decoded -->

6. et cosh 3t {(eat + e-2t); transform

<!-- formula-not-decoded -->

8. sin 2t cos 2t = 2 sin 4t; tansform 2/(s2 + 16)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

18. 5 cosh 5t

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

36. 2t3e3t

<!-- formula-not-decoded -->

= œ-1(G) Since the transform is linear, we obtain

Now apply Y-1 on both sides to the desired result, get

<!-- formula-not-decoded -->

Note that we have proved much more than just the claim; namely the theorem: If a linear transformation has an inverse; the inverse is linear.

Thus,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The application is straightforward; with c

## SECTION 5.2. Transforms of Derivatives and Integrals. Differential Equations; page 258

Purpose. To a first impression of how the Laplace transform solves ordinary differential equations and initial value problems; the task for which it is designed. get

## Main Content, Important Concepts

<!-- formula-not-decoded -->

Extension of (1) to higher derivatives [(2)-(4)]

Solution of a differential equation; subsidiary equation

Transfer function

Transform of the integral of a function

Shifted data problems

## Comment on Differential Equations

The last of the three steps of solution is the hardest; but we shall derive many general properties of the Laplace transform (collected in Sec. 5.8) that will help, with for mulas in Table 5.1 and those in Sec. 5.9, 80 that we can proceed to equations for which the present method is superior to the classical one. along

## SOLUTIONS TO PROBLEM SET 5.2, page 264

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

10. PROJECT. () Theorems 1 and 2 are more important because are crucial in solving differential equations; whereas Theorem 3 serves as a tool for obtaining new transforms. they
2. (c) In the integration by parts shown in the proof of Theorem 1 we now have to integrate from 0 to a and then from a to % thus obtaining f(a O)e ~as from the ~as from the lower limit of integration of the second integral.
3. (d) For the given function; f(2 + 0) = f(2 \_ 0) = = 0, so that (1* and = (1 = e-s)ls give

<!-- formula-not-decoded -->

12. PROJECT. We derive (a) We have f(O) = 0 and

By (2)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Collecting Y(f)-terms; we obtain

<!-- formula-not-decoded -->

Division by s2 + 02 both sides gives (a) on

- In () on the right we get from (a)

<!-- formula-not-decoded -->

Taking the common denominator and simplifying the numerator, gives ()

<!-- formula-not-decoded -->

- (c) is shown in Example 4.
- (d) is derived the same way as (b), with + instead of so that the numerator is

<!-- formula-not-decoded -->

which gives (d)

- (e) is similar to (a). We have f(O) = 0 and obtain

<!-- formula-not-decoded -->

By (2) we obtain

<!-- formula-not-decoded -->

Hence

Division by s2 a2 gives (e)

<!-- formula-not-decoded -->

- (f) follows similarly. We have f(O) = 0 and, furthermore,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Division by s2 \_ a2 gives formula (f)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SECTION 5.3. Unit Step Function. Second Shifting Theorem. Dirac's Delta Function, page 265

## Purpose

1. Tointroduce the unit step function u(t a) which together with Dirac' s delta greatly increases the usefulness of the Laplace transform.
2. To find the transform of

<!-- formula-not-decoded -->

if that of f(t) is known ("t-shifting") ("s-shifting" was considered in Sec. 5.1.)

- a)

## Main Content, Important Concepts

Second shifting theorem (Theorem 1)

Dirac' s delta, its transform (8)

## Comment on the Unit Step Function

Problem Set 5.3 shows that u(t a) is the basic function for representing discontinuous functions.

## SOLUTIONS TO PROBLEM SET 5.3, page 273

2. The representation needed for applying the second shifting theorem is

<!-- formula-not-decoded -->

and gives the transform

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

12. The given function is

<!-- formula-not-decoded -->

so that we get the answer

14. 4u(t 2) = 8u(t - 5)
18. s2 + 2s + 2 = (s + 1)2 + 1. Hence the reciprocal of this has the inverse e-t sin t, and the second shifting theorem gives the answer e-(-27 (sin t)u(t

16. has the inverse +2/2, hence (s has the inverse e*t2/2 (first shifting), and e 1)3 has the inverse \_et-3(t 3)2u(t 3) (second shifting) 1) ~3 ~3s|(s

20. y = 3etl2(cos 3t + sin 3t)
22. In terms of unit step functions the function on the right is

<!-- formula-not-decoded -->

Answer:

<!-- formula-not-decoded -->

u(t 2)] 4et 4e2e-2) u(t 2) Hence

<!-- formula-not-decoded -->

Take ~s + 7 to the right, divide by s2 \_ 5s + 6 = (s = 2)(s = 3) to get

<!-- formula-not-decoded -->

The sum of the first two terms on the rght has the partial fraction expansion

<!-- formula-not-decoded -->

plus the inverse of

<!-- formula-not-decoded -->

this inverse is

<!-- formula-not-decoded -->

The sum of this and the previous solution is

<!-- formula-not-decoded -->

this is the solution if t &gt; 2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Answer:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

40. CAS PROJECT. Students should become aware of the fact that careful observation of plots may lead to discoveries or to more information about conjectures that may want to prove Or disprove. The curves branch from the solution of the homogeneous equation at the instant at which the impulse is applied; which by choosing; say, 1, 2, 3, gives an interesting joint plot. they

Purpose. To show that, roughly; differentiation and integration of transforms (not of functions; as beforel) corresponds to multiplication and division; respectively; of functions by t, with application to the derivation of further transforms and to the solution of Laguerre' $ differential equation:

## Comment on Application to Variable-Coefficient Equations

This possibility is rather limited; our Example 4 is perhaps the best elementary example of practical interest.

Very Short Courses. This section and the two subsequent sections can be omitted.

Answer:

## SOLUTIONS TO PROBLEM SET 5.4, page 278

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The inverse transform of the integral is sin t. Answer: e-3t

<!-- formula-not-decoded -->

14. [In (s + a) - In (s + b)]' = has the inverse transform e at e-bt\_ s + a

so that (1) gives the answer

<!-- formula-not-decoded -->

16. We have

<!-- formula-not-decoded -->

The inverse transform of the integrand is sin Tt. From (6) we thus obtain the answer

<!-- formula-not-decoded -->

18. nII(s a)n+1

20. CAS PROJECT. Students should become aware of the fact that usually there are various possibilities for calculations; and should not rush into numerical work before making a careful selection of formulas. they
2. (b) The formula follows by the usual rule of differentiating a product n times. Some of the polynomials are

<!-- formula-not-decoded -->

## SECTION 5.5. Convolution: Integral Equations; page 279

Purpose. To find the inverse h(t) of a product H(s) = F(s)G(s) of transforms whose inverses are known

## Main Content; Important Concepts

Convolution f * g, its properties

Convolution theorem

Application to differential and integral equations

## Comment on Occurrence

In a differential equation; the transform R(s) of the right side r(t) is known from 1 By the subsidiary equation algebraically for Y(s) the transform R(s) multi plied by the reciprocal of the factor of Y(s) on the left (the transfer function Q(s); see Sec. 5.2). This calls for the convolution theorem unless one sees some other way Or shortcut. Step solving gets

Very Short Courses. This section can be omitted.

## SOLUTIONS TO PROBLEM SET 5.5, page 283

<!-- formula-not-decoded -->

4. This is similar to Example 1. We obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

20. Subsidiary equation s?Y + Y = s-2, Y = + s4), solution y sin t 1/(s2

22. The subsidiary equation is

<!-- formula-not-decoded -->

Answer:

<!-- formula-not-decoded -->

24. We use the notation of the text,

<!-- formula-not-decoded -->

Then

From this,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For t &gt; 1 we have

<!-- formula-not-decoded -->

28. Y = 4s-2Y, Y = 2/(s2 + 4)y = sin 2t 2s -2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

34. TEAM PROJECT. (a) Setting t = ~dp; and p runs from t to O; thus

<!-- formula-not-decoded -->

- () Interchanging the order of integration and noting that we integrate over the shaded triangle in the figure obtain we

<!-- formula-not-decoded -->

Section 5.5. Team Project 34(b)

<!-- image -->

- (c) This is a simple consequence of the additivity of the integral.
- = =
- (e) Let t &gt; k. Then (fk * follows.

<!-- formula-not-decoded -->

## SECTION 5.6. Partial Fractions. Differential Equations, page 284

cally in terms of examples, along with their inverse transforms.

Very Short Courses. Omit this section:

## SOLUTIONS TO PROBLEM SET 5.6, page 289

<!-- formula-not-decoded -->

14. The subsidiary equation is

Its solution is

<!-- formula-not-decoded -->

factors; and s0 is s2 + p?. Accordingly, the partial fraction representation is

<!-- formula-not-decoded -->

Multiplication by the common denominator gives

<!-- formula-not-decoded -->

Equating the coefficients of each power of $ on both sides gives the four equations

- (a) [s3] 0 = A + M, thus M =
- () [s2]: 0 = B + N, thus N = -B
- (d) [s%]: 02)B by (b); hence B = Kpl(p? 2) 0o
- (c) [s]: 0 = p?A + 0 (p? by (a); hence A M = 0 2M =

From this, with N = -B, we have

<!-- formula-not-decoded -->

The inverse is (see Table 5.1 in Sec. 5.1)

<!-- formula-not-decoded -->

This is a superposition of two harmonic oscillations; as expected.

16. TEAM PROJECT. (a) If f(t) is piecewise continuous on an interval of length P; then its Laplace transform exists, and we can write the integral from zero to infinity as the series of integrals over successive periods:

<!-- formula-not-decoded -->

If we substitute t = T + p in the second integral, t = T + 2p in the third integral, t = T + (n in the nth integral, then the new limits in every integral are and p. Since 1)p etc., we thus obtain

<!-- formula-not-decoded -->

The factors that do not depend on T can be taken out from under the integral signs; this gives

The series in brackets ['] is a geometric series whose sum is 1/(1 e-ps). The theorem now follows .

- (b) From (10) we obtain

<!-- formula-not-decoded -->

Using 1 e-2nslw = (1 e-Tslø and integrating by parts or noting that the integral is the imaginary part of the integral

<!-- formula-not-decoded -->

we obtain the result.

- (c) From (10) we obtain the following equation by using sin @t from 0 to mlw and

<!-- formula-not-decoded -->

This gives the result.

- The saw-tooth wave has the representation

<!-- formula-not-decoded -->

Integration by parts gives

<!-- formula-not-decoded -->

and thus from (10) we obtain the result

<!-- formula-not-decoded -->

- (e) Since kt/p has the transform from (d) we have the result klps?,

<!-- formula-not-decoded -->

## SECTION 5.7. Systems of Differential Equations; page 291

Purpose. This new section explains the application of the Laplace transform to systems of differential equations in terms of three typical examples: mixing problem; an electrical network, and a system of masses on elastic springs.

## SOLUTIONS TO PROBLEM SET 5.7, page 294

2. The subsidiary equations

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

6. Y1 = sint + cos 2t, Y2 = sin t cos 2t

8. The subsidiary equations are

<!-- formula-not-decoded -->

have the solutions They

<!-- formula-not-decoded -->

Answer:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

10. Y1 = t2,y2 = t2 + 2t, y3 = +2 \_ 2t

12. The subsidiary equations are

<!-- formula-not-decoded -->

Solving algebraically gives

Answer:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 14. The subsidiary equations are

<!-- formula-not-decoded -->

Solving algebraically gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Taking the inverse Laplace transform gives the answer

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Setting 2t gives the old solution; except for notation:

<!-- formula-not-decoded -->

20. For 0 = t = 2T the solution is as in Prob. 19,

<!-- formula-not-decoded -->

For t 2m one has to add to this further terms whose form is determined by this solution and the second shifting theorem;

<!-- formula-not-decoded -->

The cosine and sine terms cancel, so that

<!-- formula-not-decoded -->

## SOLUTIONS TO CHAPTER 5 REVIEW, page 299

<!-- formula-not-decoded -->

## PART B. LINEAR ALGEBRA, VECTOR CALCULUS

## Major Change

Part B consists of

6 Linear Algebra: Matrices; Vectors, Determinants. Linear Systems of Equations Chap.

Chap. 7 Linear Algebra: Matrix Eigenvalue Problems

8 Vector Differential Calculus. Grad, Div, Curl Chap.

9 Vector Integral Calculus. Integral Theorems Chap.

Following several requests, we now present eigenvalue problems in a separate chapter. However; this does not change the flow of the material in Part B as a whole.

Chapter 8 is self-contained and completely independent of Chaps. 6 and 7. Thus, Part B consists of two large independent units; namely Linear Algebra (Chaps. 6, 7) and tor Calculus (Chaps. 8, 9) Chapter 9 depends on Chap. 8, mainly because of the occurrence of div and curl (defined in 8) in the and Stokes theorems in 9 VecChap. Gauss Chap.

## CHAPTER 6 Linear Algebra: Matrices, Vectors,

## Determinants. Linear Systems of Équations

## Major Changes

Various local changes have been made in order to increase the usefulness of this chapter portant in practice, the total amount of material has been reduced slightly; resulting in a smoother and better motivated flow of ideas and methods and a corresponding valuable in teaching time. More specifically; there are essentially three major changes; as follows. imgain

- 1 The beginning, which had been somewhat slow by modern standards, has been streamlined, so that the student will see applications to linear systems of equations much earlier .
2. The reference section on second-order and third-order determinants, which had become somewhat dated, has been omitted and replaced by a shorter portion on that material at the beginning of the section on determinants (Sec. 6.6), from which the essential information on those lower order determinants can now be obtained more easily and quickly.
3. The two sections on determinants and Cramer' s rule have been combined into a single section (Sec. 6.6), which precedes the discussion of the inverse in Sec. 6.7 \_ thus this portion of the chapter more compact:. making

## SECTION 6.1. Basic Concepts. Matrix Addition; Scalar Multiplication; page 305

Purpose. Explanation of the basic concepts and the two basic matrix operations .

## Main Content, Important Concepts

Matrix, square matrix, main diagonal

Double subscript notation

Row vector, column vector, transposition

Equality of matrices

Matrix addition

Scalar multiplication (multiplication of a matrix by a scalar)

## Comment on Notation

but will be needed to indicate differentiation in Chap. 8\_

## Comments on Important Facts

One should emphasize that vectors are always included as cases of matrices and that those two operations have properties [formulas (4), (5)] similar to those of operations for numbers; which is a great practical advantage. special

## Comment on Vector Spaces

Since vector spaces are defined in terms of matrix addition and scalar multiplication; more familiar with the matrix concept. they

## SOLUTIONS TO PROBLEM SET 6.1, page 309

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

6. Undefined, undefined, the 2 X 2 zero matrix 0
2. 108 8. the same matrix because of (5), (6), and (AT) = A. ~48 72 132
10. [~6 ~3], [6 5
12. [11 =1 3], [~36 120 48]
14. Undefined, [6 5 3]T, undefined (not of the same size)
16. 0 by (7), undefined, [7 0 26]
20. TEAM PROJECT. (b) The nodal incidence matrices are

<!-- formula-not-decoded -->

The networks with these incidence matrices are (c)

<!-- image -->

## SECTION 6.2. Matrix Multiplication; page 311

Purpose. Matrix multiplication; the third and last algebraic operation; is defined and dis cussed, with emphasis on its 'unusual?" properties; this also includes its representation by inner products of row and column vectors.

## Main Content, Important Facts

Definition of matrix multiplication

Properties of matrix multiplication

Matrix products in terms of inner products of vectors

Linear transformations motivating the definition of multiplication

AB + BA in general, so the order of factors is important:

AB 0 does not imply A =0 or B = 0 or BA = 0

<!-- formula-not-decoded -->

Short Courses: Products in terms of row and column vectors and the discussion of linear transformations could be omitted.

## Comments on Content

Most important for the next sections on systems of equations will be the multiplication of a matrix times a vector.

Formula (5) for the transposition of a product should be memorized.

~Unusual properties" (i.e,, having no counterpart in the multiplication of numbers) are exhibited in Examples 4 and 5, and it may be good to invite the student to invent further examples. The student should also get used to cases in which products are not defined, in order to recognize the limitation of the definition.

In motivating matrix multiplication by linear transformations, one may also illustrate the geometric significance of noncommutativity by combining a rotation with a stretch in x-direction in both orders and show that a circle transforms into an ellipse with main axes in the direction of the coordinate axes or rotated; respectively.

## SOLUTIONS TO PROBLEM SET 6.2, page 319

<!-- formula-not-decoded -->

4. [34 15 11]7, undefined, [34 24 17]

<!-- formula-not-decoded -->

8. pose

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- and the kth column of AT which is the kth row of A because of the transposition. Thus;

<!-- formula-not-decoded -->

To prove the second statement in (a) use (5). If AB = BA, then

<!-- formula-not-decoded -->

because AT = AB, then AB = (AB)T = BTAT = BA, s0 that A and B commute\_

<!-- formula-not-decoded -->

etc., and A2 = I is true for

<!-- formula-not-decoded -->

where a, b, and c # 0 are arbitrary .

- (d) The Ckj of (AB)T is c;k of AB, which is row j of A times column k of B hence column k of B, times column j of A, hence row j of A. entry
- c) Triangular are U1 + U2, UjU2, hence Uj? and the corresponding expressions for is lower triangular.
12. The transition probabilities can be given in a matrix

<!-- formula-not-decoded -->

The first row gives the state after one day if initially there was N, and the second row if initially there was T. From this we see that there will be N after 2 days with ability prob -

<!-- formula-not-decoded -->

because N will remain with P = 0.8 and T will return to N with P = 0.5. Similarly for the other possibilities. We see that this is just the law of matrix multiplication: Accordingly; \_ gives the probabilities after 2 and A3 after 3 here, by calculation; days days;

<!-- formula-not-decoded -->

Answer: 0.26, 0.278.

14. The matrix of the transition probabilities is

<!-- formula-not-decoded -->

The starting vector is Xo [1200 98800] and gives (rounded)

<!-- formula-not-decoded -->

indicating that a substantial increase is likely.

18. TEAM PROJECT. () Use induction on n. True if n = 1. Take the formula in the problem as the induction hypothesis; multiply by A, and simplify the entries in the product by the addition formulas for the cosine and sine t0 get An+1
16. We then proceed by time intervals of 10 years .
3. (c) Those formulas follow directly from the definition of matrix multiplication.
4. (d) A scalar matrix would correspond to a stretch or contraction by the same factor in all directions.
5. (e

## SECTION 6.3. Linear Systems of Equations. Gauss Elimination; page 321

Purpose; This simple section centers around the Gauss elimination for solving linear systems of msequations in n unknowns X1, Xn, its practical use as well as its mathematical justification (leaving the ~more demanding general existence theory to the next sections) .

## Main Content; Important Concepts

Nonhomogeneous; homogeneous; coefficient matrix; augmented matrix

Gauss elimination in the case of the existence of

- unique solution (Examples 2, 4)
- infinitely many solutions (Example 3)

no solutions (Example 5).

Pivoting

Elementary row operations, echelon form

Background Material. All one needs here is the multiplication of a matrix and a vector.

## Comments on Content

The student should become aware of the following facts:

2. The Gauss elimination (with pivoting) gives sensible results in each of the Cases I-I
1. Linear systems of equations provide a major application of matrix algebra and justification of the definitions of its concepts.
3. This method is a systematic elimination that does not look for unsystematic 'shortcuts" (depending on the size of the numbers involved and still advocated in some older pre-computer-age books)

Algorithms for programs of Gauss's and related methods are discussed in Sec. 18.1, which is independent of the rest of Chap. 18, and can thus be taken up along with the present section in case of time and interest.

## SOLUTIONS TO PROBLEM SET 6.3, page 329

6. No solution

10. x = 7y 9z

<!-- formula-not-decoded -->

18. Currents at the lower node:

The solution is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

12. No solution

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(minus because I1 flows out). Voltage in the left circuit:

and in the right circuit

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(minus because I3 flows against the arrow of E2). Hence the augmented matrix of the system is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

24. PROJECT. (a) B and C are different. For instance; it makes a difference whether first multiply a row and then interchange; and then do these operations in reverse order. we

<!-- formula-not-decoded -->

- (b) Premultiplying A by E makes E operate on rows of A. The assertions then follow almost immediately from the definition of matrix multiplication

- These matrices; applied in the order E1 E2, E3, are (c)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## page 331

Purpose. This section introduces some theory centered around linear independence and rank, in preparation for the discussion of the existence and uniqueness problem for linear systems of equations (Sec. 6.5).

## Main Content, Important Concepts

Linear independence

Real vector space Rn, dimension, basis

Rank defined in terms of row vectors

Rank in terms of column vectors

Invariance of rank under elementary row operations

Short Courses. For the further discussion in the next sections, it suffices to define linear independence and rank.

## Comments on Rank and Vector Spaces

Of the three possible equivalent definitions of rank,

- By row vectors (our definition)
- (ii) By column vectors (our Theorem 1),
- (iii)   By submatrices with nonzero determinant (Sec. 6.6),

the first seems to be most practical in our context:.

Introducing vector spaces here, rather than in Sec: 6.1, we have the advantage that the student immediately sees an application (row and column spaces) . Vector spaces in full generality follow in Sec. 6.8.

## SOLUTIONS TO PROBLEM SET 6.4, page 336

2. Linearly dependent
2. 4 Linearly dependent (four vectors in R3!)

6. Linearly dependent (one is the zero vector!)
8. Linearly dependent

<!-- formula-not-decoded -->

18. Yes when k = 0, dimension 2, basis [1 0 0], [0 1 4] No for any other value of k
20. No, because of the inequality
22.  Yes, dimension 2, basis e(-1) and (the last two vectors of the standard basis) e(n)
26. TEAM PROJECT. (b) BTAT = (AB)T and rank is invariant under transposition. The other two statements follow from the definition of rank and Theorem 1.
24.  Yes, dimension 1, basis [5 ~23], as follows by first considering the second equation and then the first

Parts (c) and (d) are proved in Ref. [B2] listed in Appendix 1. Equality in (d) oc-= =

curs for A B I, for instance.

<!-- formula-not-decoded -->

## SECTION 6.5. Solutions of Linear Systems: Existence, Uniqueness; General Form, page 338

Purpose. The student should see that the totality of solutions (including the existence and uniqueness) can be characterized in terms of the ranks of the coefficient matrix and the augmented matrix.

## Main Content, Important Concepts

Augmented matrix

Necessary and sufficient conditions for the existence of solutions

Implications for homogeneous systems

<!-- formula-not-decoded -->

Background Material. Rank (Sec. 6.4)

Short Courses. Brief discussion of the first two theorems; illustrated by some simple examples.

## Comments on Content

This section should make the student aware of the great importance of rank. It may be to have students memorize the condition good

<!-- formula-not-decoded -->

Students familiar with differential equations may be reminded of the analog of Theorem 4 (see Sec. 2.8).

for the existence of solutions.

This section may also provide a opportunity to to the roles of existence and uniqueness problems throughout mathematics (and to the distinction between the two) good point

## SECTION 6.6. Determinants. Cramer's Rule, page 341

Purpose. The first part of this section (on second- and third-order determinants) is mainly for reference in other chapters. The main body of the section concerns those properties. of nth-order determinants that are needed in practical work, and Cramer' s rule.

so that we obtain

<!-- formula-not-decoded -->

(e) For a general conic section the equation is s0 that we get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SECTION 6.7. Inverse of a Matrix Gauss-Jordan Elimination; page 350

Main Content; Important Concepts

Purpose. To familiarize the student with the concept of the inverse of a square matrix A, its conditions for existence; and its computation. A-1

<!-- formula-not-decoded -->

Nonsingular and singular matrices

Existence of A-1 and rank

Gauss-Jordan elimination

<!-- formula-not-decoded -->

Cancellation law

<!-- formula-not-decoded -->

Short   Courses.   Theorem 1 without proof, Gauss-Jordan   elimination; formulas (4*) and (7)

## Comments on Content

Although in this chapter we are not concerned with operations count (Chap. 18), it would make no sense to first blindfold the student by Gauss-Jordan for solving Ax = b and then later in numerical analysis correct the false impression by explaining why Gauss celimination is better because back substitution needs fewer operations than the diagonalization of a triangular matrix. Thus Gauss-Jordan should be applied only when A-1 is needed. using

The "unusual" properties of matrix multiplication; briefly mentioned in Sec. 6.2 can now be explored systematically by the use of rank and inverse.

Formula (4* is worth memorizing.

## Main Content, Important Concepts

Second - and third-order determinants nth-order determinants

General properties of determinants

Rank in terms of determinants (Theorem 3)

Cramer' s rule for solving linear systems by determinants (Theorem 4)

Our definition of a determinant seems more practical than that in terms of permutations (because it immediately gives those general properties), at the expense of the that our definition is unambiguous (see the in Appendix 4). proof proof

General  properties   are given for order n, from which can be easily seen for 'n = 3 when needed. they

The importance of determinants has decreased with time; but will remain basic in eigenvalue problems (characteristic determinants) , differential equations (Wronskians!), integration and transformations (Jacobians!), and other areas of practical interest.

## SOLUTIONS TO PROBLEM SET 6.6, page 349

<!-- formula-not-decoded -->

18. x = 2,y = -3, z = 8

20. TEAM PROJECT. (b) For a plane the equation is ax + by + cz + d . 1 = 0, 80 that we get the determinantal equation

<!-- formula-not-decoded -->

The plane is 3x + 4y = 2z = 5.

- (c) For a circle the equation is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The circle is x2 + y? \_ Ax = 2y = 20.

- (d) For a the equation is sphere

<!-- formula-not-decoded -->

so that we get

## SOLUTIONS TO PROBLEM SET 6.7, page 357

<!-- formula-not-decoded -->

4. Note that due to the special form of the given matrix, the 2 X 2 minor in the right lower corner of the inverse has the form of the inverse of a 2 X 2 matrix; the inverse is

<!-- formula-not-decoded -->

6. The entries of the inverse are the same as for a diagonal matrix, but their position on the other diagonal is different. The inverse is

<!-- formula-not-decoded -->

8. The given matrix is singular. It is interesting that this is not the case for the 2 x 2 matrix

<!-- formula-not-decoded -->

10. Multiply I = (A2)-1A? by from the right; (A2)-1A, and this result =1 by Afrom the right. A-1 A-1 again
12. We obtain

<!-- formula-not-decoded -->

This shows that the inverse of AT must be (A-1)T as we wanted to prove. 14. Use (1), with A replaced by C, and set C A-1

<!-- formula-not-decoded -->

## SECTION 6.8. Vector Spaces. Inner Product Spaces. Linear Transformations. Optional, page 358

Purpose. In this optional section we extend our earlier discussion of vector spaces Rn and define inner product spaces; and explain the role of matrices in linear transformations of Rn into Cn Rm\_

## Main Content, Important Concepts

Real vector space; complex vector space

Linear independence; dimension; basis

Inner product space

Linear transformation of Rn into Rm

Background MateriaL.  Vector spaces Rn and Cn (Sec. 6.4) inner product (Sec. 6.2)

## Comments on Content

The student is supposed to see and comprehend how concrete models (Rn and the inner product for vectors) lead to abstract concepts; defined by axioms resulting from basic properties of those models. Because of the level and general objective of this chapter; we have to restrict our discussion to the illustration and explanation of the abstract concepts in terms of some simple typical examples.

Most essential from the viewpoint of matrices is our discussion of linear transformations; which in a more theoretically oriented course of a higher level would occupy a more prominent position.

## Comment on Footnote 12

worked on number theory 1893-1898, foundations of geometry 1898-1902, integral equations 1902-1912, physics   1910-1922, and logic and foundations of mathematics 1922-1930. Closest to our interests here is the development in integral equations; as follows. In 1870 Carl Neumann (Sec. 4.6) had the idea of solving the Dirichlet problem for the Laplace equation (Sec. 9.8) by converting it to an integral equation: This created general interest in integral equations. In 1896 Vito Volterra (1860-1940) developed a general theory of these equations, followed by Ivar Fredholm (1866-1927) in 1900-1903, whose papers caused great excitement; and Hilbert since 1902. This gave the impetus to the development of inner product and Hilbert spaces and operators defined on them. These spaces and operators and their spectral theory have found basic applications in quantum mechanics since 1927. Hilbert' s great interest in mathematical physics is documented by Ref. [4], a classic full of ideas that are of interest to the mathematical work of the engineer. For more details; see G. Birkhoff and E. Kreyszig. The establishment of functional analysis. Historia Mathematica 11 (1984), Pp. 258-321.

## SOLUTIONS TO PROBLEM SET 6.8, page 364

2. nonnegativity is not preserved under scalar multiplication. No;
6. Dimension 6, basis
4. Dimension 2 Basis [cos x sin x]. Further examples from differential equations can easily be presented to students familiar with these equations. We did not mention this explicitly, to keep chapters independent.

<!-- formula-not-decoded -->

## 8. Dimension 4, basis

<!-- formula-not-decoded -->

12. If another such representation with coefficients k; would also hold, subtraction would give k;)a; = 0, hence C; ~ kj = 0, because of the linear independence. This shows the uniqueness.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SOLUTIONS TO CHAPTER 6 REVIEW, page 365

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- OI BT is singular; by the theorem on the determinants of products of matrices (Sec. 6.7, Theorem 4)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- Kirchhoff s voltage and Ohm' s law, this, law,

<!-- formula-not-decoded -->

This gives the indicated matrix .

## CHAPTER 7 Linear Algebra: Matrix Eigenvalue Problems

This chapter is new. Prerequisite is some familiarity with the notion of a matrix and with the two algebraic operations for matrices. Otherwise the chapter is independent of 6, s0 that it can be used for teaching eigenvalue problems and their applications; without first going through the material in 6 Chap. Chap:

## SECTION 7.1. Eigenvalues, Eigenvectors, page 371

Purpose. To familiarize the student with the determination of eigenvalues and eigenvectors of real matrices and to give a first impression of what one can expect (multiple eigenvalues, complex eigenvalues, etc.).

## Main Content; Important Concepts

Eigenvalue; eigenvector

Determination of eigenvalues from the characteristic equation

Determination of eigenvectors

Algebraic and geometric multiplicity, defect

## Comments on Content

To maintain undivided attention on the basic concepts and techniques; all the examples in this section are formal, and typical applications  are into a separate section (Sec. 7.2) put

The distinction between the algebraic and geometric multiplicity is mentioned in this early section; and the idea of a basis of eigenvectors could perhaps be mentioned briefly in class, whereas a thorough discussion of this in a later section (Sec. 7.5) will profit from the increased experience with eigenvalue problems; which the student will have gained at that later time.

In our present work we find eigenvalues first and are then left with the much simpler task of determining corresponding eigenvectors: Numerical work (Secs. 18.6-18.9) may proceed in the opposite order, but to mention this here would perhaps just confuse the student.

The possibility of normalizing any eigenvector is mentioned in Theorem 2, but this will be of greater interest to us only in connection with orthonormal or unitary systems (Sec. 7.4)

## SOLUTIONS TO PROBLEM SET 7.1, page 375

2. 0, any nonzero vector

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We discuss this in Sec. 7.3.

<!-- formula-not-decoded -->

namely, the matrix is orthogonal, its eigenvalues have absolute value 1, and its determinant has value 1

<!-- formula-not-decoded -->

(just as À = 3 in Prob. 13), so that we have no basis of eigenvectors.

<!-- formula-not-decoded -->

indicating that there is no direction that is preserved under a rotation.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

that every point in the is mapped onto itself. The other eigenvalue is 1, with eigenvector [0 0 1]7, indicating that every Z1 on the z-axis is mapped onto its negative ~Z1. ting xy-plane point

<!-- formula-not-decoded -->

every point in the plane y = X is mapped onto itself. The other eigenvalue 0 with eigenvector [1 1 0] T indicates that any point on the line y = 0 (which is perpendicular to the plane y = x) is mapped onto the origin The student should perhaps make a sketch to see what is going on geometrically.

## SECTION 7.2. Some Applications of Eigenvalue Problems, page 376

Purpose; Matrix eigenvalue problems are of greatest importance in physics; engineering, geometry, etc , and the applications in this section and in the problem set are supposed t0 give the student at least some impression of this fact.

## Main Content

Applications of eigenvalue problems in

Elasticity theory (Example 1),

Biology (Example 3),

Probability theory (Example 2),

Mechanical vibrations (Example 4).

Short Courses. Of course; this section can be omitted; for reasons of time, or one or two of the examples can be considered quite briefly.

## Comments on Content

The examples in this section have been selected from the viewpoint of modest prerequi sites, so that not too much time will be needed to set the scene

Example 4 illustrates why real matrices can have complex eigenvalues (as mentioned before; in Sec. 7.1) and why these eigenvalues are physically meaningful. (For students familiar with systems of differential equations; one can easily pick further examples from Chap.

## SOLUTIONS TO PROBLEM SET 7.2, page 379

2. Eigenvalues and eigenvectors are 1.6, [1 ~1]T and 2.4, [1 1] T . These vectors are orthogonal, as is typical of a symmetric matrix. Directions are respectively.
6. 2, [1 Directions 450 ~459, respectively and
4. 0.5, [1 1] T; 15, [1 1]7. Orthogonality as in Prob. 2 Directions ~45" and 459 respectively.
8. [1 1 umn sums equal to 1, which is not the case in general.
12. Growth rate 3 The other eigenvalues   are ~0.247004 and ~2.753. These are not needed.
10. The growth rate is 2. The other two eigenvalues are not needed; could be determined by dividing the characteristic polynomial by ^ 2; are =1 + V0.6. they they
7. 14 A has the same eigenvalues as A and A has row sums 1, so that it has the eigenvalue 1 with eigenvector x = [1
16. TEAM PROJECT. (a) Because a polynomial with real coefficients (in our case, the characteristic polynomial) has real or complex conjugate zeros.

Leontief is a leader in the development and application of quantitative methods in empirical economical research; genuine data from the economy of the United States to provide; in addition to the "closed model' of Prob. 13 (where the producers consume the whole production) models" of various situations of production and consumption; including import; export; taxes;, capital and losses, etc. See W. W.Leontief, The Structure of the American Economy 1919-1939 (Oxford: Oxford University Press, 1951), H. B. Cheney P.G. Clark, Interindustry Economics (New York: Wiley, 1959) using "open gains and

- (b) A exists if and only if det A # 0, but det A = as follows from the product representation ~1

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

namely,

- This follows by comparing the coefficient of in the expansion of D(A) with that obtained from the product representation. An-1
- (d) = (A = AjX; = (Aj = kI)Xj kxj k)Xj
- (e) The first statement follows from

<!-- formula-not-decoded -->

the second by induction and multiplication of = Akx;

- (f)   From = = Axj
- g) det (L 0. Hence ^ + 0. If all three eigen values are real, at least one is positive since trace L =0 The only other possi -= a

<!-- formula-not-decoded -->

## SECTION 7.3. Symmetric, Skew-Symmetric; and Orthogonal Matrices; page 381

Purpose To introduce the student to the three most important classes of real square matrices and their general properties and eigenvalue theory.

## Main Content; Important Concepts

The eigenvalues of a symmetric matrix are real.

The eigenvalues of a skew-symmetric matrix are pure imaginary or zero.

The eigenvalues of an orthogonal matrix have absolute value 1.

Further properties of orthogonal matrices

## Comments on Content

The student should memorize the preceding three statements on the locations of eigenvalues as well as the basic properties of orthogonal matrices (orthonormality of IOW vectors and of column vectors, invariance of inner product; determinant equal to 1 or ~1)

Furthermore; it may be good to emphasize that; since the eigenvalues of an orthogonal matrix may be complex; s0 may be the eigenvectors. Similarly for skew-symmetric matrices. Both cases are simultaneously illustrated by

<!-- formula-not-decoded -->

corresponding to the eigenvalues i and ~i, respectively.

## SOLUTIONS TO PROBLEM SET 7.3, page 384

2. Skew-symmetric if a 0, symmetric if b = 0, orthogonal if a2 + b2 = 1. Eigenvalues a + ib
2. 4 Orthogonal (a rotation about the x-axis through an angle  0) Eigenvalues 1 and cos 0 + i sin 0
3. 6 Symmetric (for real a and k). Eigenvalues a k (of algebraic and geometric multiplicities 2 when k # 0) and a + 2k
4. 8 Let Ax = Àx (x # 0) Ay = jy (y # 0). Then (Ax)T = xTAT = xTA = Ax T . Thus Axy = 'y. Hence,if À # J, then x y = 0, which proves orthogo nality.

10. Yes, for instance

where -1 =a= 1.

12. No for 3 X 3, yes for 4 X 4, no for 5 X 5. For 3 X 3,

<!-- formula-not-decoded -->

det A = det(AT) = det(~A) (~I)ndet A = 0 if n = 3,5, 14. (a) AT BT = (AB)T = = (AB) -1. (AT)-1 = (A-1)-1. In terms of rotations it means that the composite of rotations and A-1 B-1,

- the inverse of a rotation are rotations .
- (b) The inverse is

<!-- formula-not-decoded -->

- To a rotation of 16.269. No limit. For a student unfamiliar with complex numbers this may require some thought.
- (e) The matrix is obtained by familiar values of cosine and sine, using
- Limit 0, approach along some spiral.

<!-- formula-not-decoded -->

## SECTION 7.4. Complex Matrices: Hermitian, Skew-Hermitian, Unitary, page 385

Purpose. This section is devoted to the three most important classes of complex matrices and corresponding forms and eigenvalue theory .

## Main Content, Important Concepts

Hermitian and skew-Hermitian matrices

Unitary matrices, unitary systems

Location of eigenvalues (Fig. 146)

Quadratic forms, their symmetric coefficient matrix

Hermitian and skew-Hermitian forms

Background Material. Section 7.3, which the present section generalizes. The prerequisites on complex numbers are very modest; s0 that students will hardly need any extra help in that respect.

Short Courses: This section can be omitted.

## Comments on Content

This is the first time in this chapter that the student meets with complex matrices; The material is arranged so that the analogy of properties and proofs to those in Sec. 7.3 will be apparent.

<!-- formula-not-decoded -->

The importance of these matrices results from quantum mechanics as well as from mathematics itself from unitary transformations, product representations of nonsingular matrices A = UH, U unitary, H Hermitian; etc.). (e.g-,

The determinant of a unitary matrix (see Theorem 4) may be complex: For example; the matrix

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SOLUTIONS TO PROBLEM SET 7.4, page 390

2. [1 3i 3i ~2]T
4. [1 1] T, [1
6. Skew-Hermitian; ~i, [~1 + i 2]; 2i, [1 \_ i
4. ~1 =i 0 1] T; 2, [i 1 + i
8. Skew-Hermitian; i, [0 1 0] T; 3i, [~1 0 1]T; 5i, [1 0
6. = (AB)' We prove the statement about the inverse. Let A be unitary. Set A-1 = B. Then BT ~1 = (A-1) = = B Thus =B B-1
7. (c) AA = A? if A is Hermitian; ~A? if A is skew-Hermitian; AA-1 = Iif A is unitary . Commutability is now obvious.
8. (d) = =

Also

These two expressions are equal if and only if

<!-- formula-not-decoded -->

This implies that HS = SH, as claimed.

- (e) For instance,

is not normal: A normal matrix that is not Hermitian; skew-Hermitian; or unitary is obtained if we take a unitary matrix and multiply it by 2 or some other real factor different from +1.

<!-- formula-not-decoded -->

20. Skew-Hermitian; 6i
24.  Hermitian; 4

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

is unitary and has

## SECTION 7.5. Similarity of Matrices. Basis of Eigenvectors. Diagonalization; page 392

Purpose. This section exhibits the role of bases of eigenvectors in connection with linear transformations and contains theorems of great practical importance in connection with eigenvalue problems; notably Theorems 1, 4, 5.

## Main Content, Important Concepts

Similar matrices have the same spectrum (Theorem I).

Bases of eigenvectors (Theorems 3, 4)

Diagonalization of matrices (Theorem 5)

Principal axes transformation of forms

Short Courses. Complete omission of this section or restriction to a short look at Theorems 1 and 5

## Comments on Content

Theorem 1 on similar matrices has various applications in the design of numerical methods (Chap: 18), which often use subsequent similarity transformations to tridiagonalize or (nearly) diagonalize matrices on the way to approximations of eigenvalues and eigenvectors: The matrix X of eigenvectors [see (5)] also occurs frequently in that context quite

Theorem 4 is another result of fundamental importance in many applications; for instance; in those methods for numerically determining eigenvalues and eigenvectors. Its is substantially more difficult than the other proofs given in this chapter. proof

## SOLUTIONS TO PROBLEM SET 7.5, page 397

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

16. Hyperbola 39y2 = 156, hence 4y12 ~ 3y22 12; *1 = 3y2)/V13, Xz (3y1 2y2)/V13 52y1 (2y1

<!-- formula-not-decoded -->

18. Orthogonal straight lines 25y12 4 = 0, that is; the coordinate axes of the Y-system; X1 0.6y1 0.8y2, X2 = 0.8y1 + 0.6y2 50y2
2. 22 PROJECT: (a) This follows immediately from the product representation of the characteristic polynomial of A
3. (b) C = AB, C1l = a1bul C22 Now take the sum of these n 1=1

sums. Furthermore; trace BA is the sum of

<!-- formula-not-decoded -->

- (c) By multiplications from the right and from the left we readily obtain

involving the same terms as those in the double sum of trace AB.

<!-- formula-not-decoded -->

- (d) Interchange the corresponding eigenvectors (columns) in the matrix X in (5).

## SOLUTIONS TO CHAPTER 7 REVIEW, page 398

<!-- formula-not-decoded -->

22. Straight lines Y2 O; X1 = (2y1 + 3y2)/Vi3, x2 (~3y1 + 2y2)/Vis
24.  Eigenvalues and eigenvectors are

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## CHAPTER 8 Vector Differential Calculus: Grad,

## Changes

more concrete fashion. The section on grad, and curl in curvilinear coordinates has been omitted; this material can now be found in Appendix A3.4, since it is mainly for reference. div,

## SECTION 8.1. Vector Algebra in 2-Space and 3-Space; page 401

## Main Content, Important Concepts

Purpose; We introduce vectors in 3-space given geometrically by (families of parallel) directed segments or algebraically by ordered triples of real numbers; and we define addition of vectors and scalar multiplication (multiplication of vectors by numbers).

Vector; norm (length) unit vector; components

Addition of vectors, scalar multiplication

## Comments on Content

Our discussions in the whole chapter will be independent of 6, and there will be no more need for writing vectors as columns and for distinguishing between row and column vectors. Our notation a = [a1, a2, a3] is compatible with that in 6. Engineers seem to like both notations Chap. Chap.

preferring the first for "short'" components and the second in the case of longer expressions .

The student is supposed to understand that the whole vector algebra (and vector calculus) has resulted from applications; with concepts that are practical, that is, are "made to measure for standard needs and situations; thus; in this section; the two algebraic operations resulted from forces (forming resultants and changing magnitudes of forces); similarly in the next sections:. The restrictions to three dimensions (as opposed to n dimensions in the previous two chapters) allows us to "visualize" concepts; relations; and results and to give geometrical explanations and interpretations . they

On higher level, the equivalence of the geometric and the algebraic approach (Theorem 1) would require a consideration of how the various triples of numbers for the varichoices of coordinate systems must be related (in terms of coordinate transformations) for a vector to have a norm and direction independent of the choice of coordinate systems.

## SOLUTIONS TO PROBLEM SET 8.1, page 407

<!-- formula-not-decoded -->

## Curl Div,

<!-- formula-not-decoded -->

30. 3q| = 36. Nothing about the direction.

<!-- formula-not-decoded -->

34. TEAM PROJECT. (a) The idea is to write the position vector of P in the figure in two ways and then to compare,

<!-- formula-not-decoded -->

pressing bisection.

- (b) The idea is similar to that in part (a) It gives

= 4 thus a ratio 3:1.

- (c) Partition the parallelogram into four congruent parallelograms. Part (a) gives 1:1 for a small parallelogram; hence 1:(1 + 2) for the parallelogram. large
- (d) In the figure, a + b + c + d = 0, hence c + d = shows that one of sides is parallel and of the same length. Similarly for the other pair pair.
- (e) Let be the vectors. Their angle is œ = 2uIn. The interior angle at = T the terminal of etc\_ Then the figure thus obtained is an n-sided polygon; because the angle between two sides   equals T œ = B. Hence Y1 + V2 + + Vn =0 (Of course, for even n the truth of the statement is immediately' obvious) . V1 regular point 42,
- f) (see the figure). Then the four (space) diagonals have the midpoints point

<!-- formula-not-decoded -->

and these four position vectors are equal.

Section 8.1. Parallelepiped in Team Project 34(f)

<!-- image -->

## SECTION 8.2. Inner Product (Dot Product), page 408

Purpose.  We define; explain; and apply a first kind of product of vectors; the dot uct a b, whose value is a scalar . prod -

## Main Content, Important Concepts

Definition (1)

Dot product in terms of components

Orthogonality

Length and angle between vectors in terms of dot products

Schwarz and triangle inequalities

## Comment on Dot Product

This product is motivated by work done by a force (Example 2), by the calculation of components of forces (Example 3), and by geometric applications such as those given in Examples 5 and 6.

and is also used in more general settings (see Sec. 6.8). 'Inner

## SOLUTIONS TO PROBLEM SET 8.2, page 413

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) a such that = with 012 + a22 = 1 501 2a2
- (d) 3/4
- (c) b such that 2b1 + b2 = 0 and b3 arbitrary . Yes
- (e) C =
- (f) a = [0, 0, 1] is a unit vector orthogonal to b and c, and 91 92 = 1/5 gives unit vectors b and c, which are orthogonal.
- (g) If a and b correspond to adjacent sides; to the diagonals there correspond a + b and a b Orthogonality implies that

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SECTION 8.3. Vector Product (Cross Product), page 414

Purpose We define and explain a second kind of product of vectors, the cross product a x b, which is a vector perpendicular.to both given vectors (or the zero vector in some cases)

## Main Content, Important Concepts

Definition of cross product; its components (2), (2**)

Right- and left-handed coordinate systems

Properties (anticommutative, not associative)

Scalar triple product

Prerequisites. Elementary use of second- and third-order determinants (see the beginning of Sec. 6.6).

## Comment on Motivations

Cross products were suggested by the observation that in certain applications; one associates with two given vectors a third vector perpendicular to the given vectors (illustrations in Examples 46). Scalar triple products can be motivated by volumes (Example 7) and linear independence (Theorem 1)

## SOLUTIONS TO PROBLEM SET 8.3, page 421

6. 0, 0, 13

10.

<!-- formula-not-decoded -->

18. 1776

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

26. The area is obtained as the length of the cross product of two edge vectors;

<!-- formula-not-decoded -->

Answer: 30.

28. [4 ~ 0] x [6 \_ 2, 3 \_ 1, 0] = [0, 0, 12]. Answer: 6
30. [2 1, 0 ~ 3, 8 = 0] x [0 = 1, 2 2 = 0] = [2, -10, ~4]. Hence 2x 1Oy 4z = with c ~28 obtained by inserting one of the three points.

32.10

34. Edge vectors are [3 1, 7 3, 12 6], [8 1, 8 3, 9 6], [2 1, 2 = 3, 8 6]. The mixed triple product of these vectors is ~90 (or +90) Answer: 15.
36. Their determinant is 220. Answer: Yes.
38. TEAM PROJECT. (a) |a X bl2 Y) cos?
4. (b) We choose a right-handed Cartesian coordinate system such that the x-axis has the direction of d and the xy-plane contains c. Then the vectors in (b) are of the
4. [8, 12, 18]

<!-- formula-not-decoded -->

12. [=16, ~24, 0], 0

16. 32, 32

form

<!-- formula-not-decoded -->

Hence by (2**),

<!-- formula-not-decoded -->

The determinant on the right equals [~b2c2di 0] Also;

<!-- formula-not-decoded -->

This proves () for our special coordinate system: Now the length and direction of a vector and a vector product; and the value of an inner product; are independent of the choice of the coordinates. Furthermore; the representation of b x (c * d) in terms of i, j, k will be the same for right-banded and left-handed sian coordinate system; and the proof is complete:

- (d) a [b * (c * d)] equals (a b = (a * b) (c * d) by the definition of the triple product; as well as (a c)(b-d) (a'd)(b c) by (b) (take the dot product by a)
- (c) This follows from () with b replaced by a * b.

## SECTION 8.4. Vector and Scalar Functions and Fields. Derivatives, page 423

Purpose; To get started on vector differential calculus; we discuss vector functions and their continuity and differentiability .

## Main Content, Important Concepts

Vector and scalar functions and fields

Continuity, derivative of vector functions (9), (10)

Differentiation of dot; cross; and triple products, (11) (13)

Partial derivatives

## Comment on Content

This parallels calculus of functions of one variable and, if known to students, can be sur veyed quickly .

## SOLUTIONS TO PROBLEM SET 8.4, page 427

2. Ellipses
4. Circles

<!-- formula-not-decoded -->

10. CAS PROJECT. Note that all these functions ocçur in connection with solutions of Laplace' s equation; so are real or imaginary parts of complex analytic functions. they
6. Hyperbolas

For example, (f) occurs in connection with In cos z. A CAS can graphically handle these more complicated functions; whereas the paper and pencil method is relatively limited . This is the of the project. point

12. Elliptic cylinders
14. Paraboloids of revolution
16. Congruent cylinders whose cross section in the yz-plane is a quadratic parabola
20. Note that each field vector is orthogonal to the position vector of the corresponding point; as for the velocity field of a rotation.
18. Note that each field vector equals the position vector of the corresponding point.
26. ~yz sin xyz (i + j), =Xz sin xyz (i + j), ~xy sin xyz (i + j)
28. [e" cos y, er 0], [~e" sin y, 0] sin y,

<!-- formula-not-decoded -->

## SECTION 8.5. Curves. Tangents. Arc Length, page 428

Purpose. Discussion of space curves as an application of vector functions of one variable

## Main Content, Important Concepts

Parametric representation of curves (1)

Tangent vector, tangent; (7)-(9)

Arc length s

## Comment on Problems 27-32

These involve only integrals that are simple (which is usually not the case in connection with lengths of curves)-

## SOLUTIONS TO PROBLEM SET 8.5, page 433

2. r(t) = [=1 + 3t, 3 + t, 8]

<!-- formula-not-decoded -->

6. r(t) = [4t, 4t, t]

<!-- formula-not-decoded -->

10. Helix on an elliptical cylinder
12. Circle in the with center at (a, b, 0) xy-plane
14. Ellipse in the plane z = 4
16. Only the portion corresponding to x = 0
5. 2 sinh t, 1]
20. Helix [3 cos t, 3 sin t, 5t]
22. (a) r'(t) = [~2 sin t, 2 cos t, 0], u =
8. Vzw; 0]

<!-- formula-not-decoded -->

24. (a) r(t) = [~2 sin t, 2 cos t, (I/VS)r' (t)
2. (b) r'(P) = [0, 2, 1], u(P) = [0, 2/V5, I/VS]
3. (c) q(w) = [2, w] 2w,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This gives as the length in the first quadrant

Answer: 6a.

<!-- formula-not-decoded -->

32. From the given representation we get dp = a sin 0 d0. Hence

<!-- formula-not-decoded -->

where 1 cos 0 = 2 sin? '40, s0 that the total length is

<!-- formula-not-decoded -->

## SECTION 8.6. Velocity and Acceleration; page 435

Purpose; To show the role of parametric representations and of derivatives in connection with motions in mechanics.

## Main Content; Important Concepts

Velocity vector

Acceleration vector; its tangent and normal components

Angular speed

Centripetal acceleration

Coriolis acceleration

Short Courses. This section (and the next two sections) can be omitted.

## SOLUTIONS TO PROBLEM SET 8.6, page 439

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The looks like an infinity sign, with a double at the origin; corresponding to t = path point

8. CAS PROJECT. (a) [~2sin t ~ 2 sin 2t, 2 cos t 2 cos 2t]. From this we obtain |v/? V'V = (~2sint ~ 2 sin 2t)2 + (2 cos t 2 cos 2t)2. Performing the squares and simplifying gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Hence

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We use (4*). straightforward simplification; By

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) v = [~sin t ~ 2 sin 2t, COS t 2 cos 2t]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) Y = [~sin t, 2 cos 2t, ~2 sin 2t]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) [c cos t ct sin t, sin t + ct cos t, c]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This is a spiral on a cone.

Hence (4*) gives

10. 2 cos t]; lvl? 4 cos? t + sin? t is minimum at +T/2 and maximum at 0 and T. = ~2 sin t], and |a| is minimum at =0 and T (on the x-axis) and maximum at +"/2 (on the y-axis). Finally,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

12. r = v = 2tb + t2b' , 9 = v 2b + Atb' + t2b". Answer: 4tb t2b,
14. R = 3.85 108 m, 106) = = R, 10-4 g, where g is the acceleration due to gravity at the earth's surface.
16. R = 3960 + 450 = 4410 [mi], 2TR = = 277.1 milmin; g = = 17.41 [milmin?] = 25.53 [ftlsec?] = 7.78 [metersIsec2]- Here we used |vl

## SECTION 8.7. Curvature and Torsion of a Curve. Optional, page 440

Purpose. To complete the discussion of the foundations of differential geometric curve theory. We leave this section optional because we shall not refer to curvature or torsion in our further work.

## Main Content, Important Concepts

Curvature

Torsion

Frenet formulas

Short Courses. Omit this section.

## SOLUTIONS TO PROBLEM SET 8.7, page 443

2. We denote derivatives with respect to t by primes. In (1)

<!-- formula-not-decoded -->

Thus in (1)

where

Hence

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Taking square roots, we get (1')

<!-- formula-not-decoded -->

8. Hyperbola x2 \_ y2 = 1, (cosh? t + sinh? t)-3/2
6. Hyperbola; K

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where the dots denote terms that vanish by applying familiar rules for simplifying determinants; thus

<!-- formula-not-decoded -->

Now use (1') and formula (12) in Sec. 8.5.

14. + c2) clla?

<!-- formula-not-decoded -->

## SECTION 8.8. Review from Calculus in Several Variables. Optional, page 443

Purpose. To give the student a handy reference and some help on material known from calculus; if needed.

## SOLUTIONS TO PROBLEM SET 8.8, page 446

2. 8 Ih

<!-- formula-not-decoded -->

## SECTION 8.9. Gradient of a Scalar Field. Directional Derivative; page 446

Purpose. To discuss gradients and their role in connection with directional derivatives; surface normals; and the generation of vector fields from scalar fields (potentials)

## Main Content, Important Concepts

Gradient, nabla operator

Directional derivative; maximum increase, surface normal

Vector fields as gradients of potentials

Laplace's equation

## Comments on Content

This is probably the first section in which one should no longer rely on knowledge from calculus; although relatively elementary calculus books usually include a passage on gradients .

Potentials are important; will occur at a number of places in our further work. they

## SOLUTIONS TO PROBLEM SET 8.9, page 452

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

22. xyz

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The first formula follows from

<!-- formula-not-decoded -->

The second formula follows by the chain rule; and the third follows by applying the terms The last formula follows by two applications of the product rule to each of the three terms of V2 .

30. 1/V5

34. 2V3

## SECTION 8.10. Divergence of a Vector Field, page 453

Purpose: To explain the divergence (the second of the three concepts grad, div, curl) and its physical meaning in fluid flows.

## Main Content, Important Concepts

Divergence of a vector field

Continuity equations (5), (6)

Incompressibility condition

## Comment on Content

The interpretation of the divergence in Example 2 depends essentially on our assumption that there are no sources or sinks in the box. From our calculations it becomes plausible that in the case of sources or sinks the divergence may be related to the net flow across the boundary surfaces of the box. To confirm this and to make it precise we need integrals; we shall do this in Sec. 9.8 (in connection with Gauss' s divergence theorem) .

## Moving div and curl to Chap. 9?

Experimentation has shown that this would perhaps not be a good idea; simply because understanding div and curl themselves; and that of understanding the nature and role of the two basic integral theorems by Gauss and Stokes; in which div and curl play the key role.

## SOLUTIONS TO PROBLEM SET 8.10, page 456

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

10. = (w2z W1z)j + (w1y w2x)k shows immediately that div v = 0 because the first; second, and third components do not depend on x, y, 2, respectively.

<!-- formula-not-decoded -->

By integration; x = y = C2, z = C3, and r = xi + yj + zk. Hence

<!-- formula-not-decoded -->

This shows that the cube in Prob. 1l is transformed into the rectangular parallelepiped bounded by x = = 1, whose volume is e.

<!-- formula-not-decoded -->

16. 0

18. 2 cosh 2x 2 cosh 2y

20. ~I/Vx? + y2. Equation (3) is simpler than differentiation.

## SECTION 8.11. Curl of a Vector Field, page 457

## Purpose, Content

We introduce the curl of a vector field (the last of the three concepts grad, div, curl) and interpret it in connection with rotations [Example 2 and the remarks on (3) and (4)]. A main application of the curl follows in Sec. 9.9 in Stokes' s integral theorem:

## SOLUTIONS TO PROBLEM SET 8.11, page 459

<!-- formula-not-decoded -->

6. [sin z 0 ~cos y]
8. curl v = = 0, imcompressible, = [2y?, = 0, y = C2, z' = 2y2 = 2c22, x = 2c22t + C1
10. curl v = x = dt, sin x = t + C1 X = = cosec x
12. curl v (17/4)k, incompressible, = x'i + yj + zk = ~4yi 4 hence (a) x = ~éy, () y' = = From this and (a) we obtain Axj;

16.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Solutions to Chapter 8 Review, page 461

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

= 104.49, 0 (orthogonal vectors)

<!-- formula-not-decoded -->

32. = ~ 14k. The minus sign indicates that the tendency of rotation is in the clockwise sense.
34. 2/3

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

46. 0

48. 0, 0
50. 0 because this is a scalar triple product corresponding to a determinant with two equal
3. ~y?132 + const, x2 + (yl4)2 const. The streamlines are ellipses.
14. PROJECT. Parts (b) and (d) are basic. They follow from the definitions by direct calculation. Part (a) follows by decomposing each component accordingly.
5. (d) For twice continuously differentiable f , for which the mixed second derivatives are equal, this follows from Vf = fri + fyj + fzk and (1), which gives
- c) In the first component in (1) we now have fvs instead of etc. Product differ entiation gives (fus)y and the other six terms f(us)y etc. give f curl v

<!-- formula-not-decoded -->

- (e) Write out and compare the twelve terms on either side.

## CHAPTER 9 Vector Integral Calculus. Integral Theorems

## SECTION 9.1. Line Integrals, page 464

Purpose. To explain line integrals in space and in the conceptually and technically with regard to their evaluation by the representation of the of integration. plane using path

## Main Content, Important Concepts

Line integral (3), (3'), its evaluation

Its motivation by work done by force

General properties (8)

Dependence on (Example 3) path

Background Material. Parametric representation of curves (Sec. 8.5); a couple of review problems may be useful.

## Comments on Content

The integral (3) is more practical than (7) (more direct in view of subsequent material) , and work done by a force motivates it sufficiently well.

Independence of is settled in the next section. path

## SOLUTIONS TO PROBLEM SET 9.1, page 470

2. 6/5
6. For instance, r =
8. F(C) = [2 cos t - t, t = 2 sin t, 2 sin t 2 cos t]. Answer: 272 ~8T
12. PROJECT. (a) For t = p2 we obtain r = [~2p sin p? , 2p cos p?], F(C) = [~cos? p?, p? sin p2] so that the integrand is 4p cos? p? sin p? . Integration gives ~(2/3) cos3 p?, hence 4/3, in agreement with the result for the given representation.
10. F(C) = [cosh t; sinh (t2), cosh t + 2t sinh (t2) + 3t2 exp (t3) Answer: sinh 2 + cosh 4 + 2 ~ 3010 e8

<!-- formula-not-decoded -->

- (c) gives the same; where the two summands correspond to the horizontal and the

<!-- formula-not-decoded -->

- [2 2t, 2t], 0 = t = 1. Answer: ~4/15

<!-- formula-not-decoded -->

## SECTION 9.2. Line Integrals Independent of Path, page 471

Purpose. Independence of path is a basic issue on line integrals; and we discuss it here in full.

## Main Content, Important Concepts

Definition of independence of path

Relation to gradient (Theorem 1), potential theory

Integration around closed curves

Work; conservative systems

Relation to exactness of differential forms

## Comment on Content

We see that our text pursues three ideas by relating independence to (i) gradients (potentials) , (ii) closed paths; and (iii) exactness of the form under the integral sign. The complete proof of the latter needs Stokes's theorem; so here we leave a small gap to be easily filled in Sec. 9.9. path

## SOLUTIONS TO PROBLEM SET 9.2, page 477

2. f = cos y. Answer: 1
4. f = sin x cos 2y. Answer: IIV2 - 1

<!-- formula-not-decoded -->

10. PROJECT. (a) 2y? # x2 from (6").
2. (b) r = [t, bt], 0 = t = 1, represents the first part of the By integration; bl4 b3)/3. Equating the derivative of the sum of the two expressions to zero gives b = 1/V2. 0.78452. path.
3. The first part is y = xlc or r = [t, tlc];, 0 =t = c. The integral over this por tion is c814 + c/2. For the second portion r = [t, 1], c =t= 1 the integral is (1 c3)/3. For c = 1 we get I = 0.75, the same as in (b) for b = 1 This is the maximum value of I for the present paths through (c, 1) because the derivative of I with respect to c is positive for 0 = c = 1.
12. Dependent on path
16. Dependent on path
18. Dependent on path
20.  Independent of path, f = z cosh y x2, c cosh b a2

<!-- formula-not-decoded -->

## SECTION 9.3. From Calculus: Double Integrals. Optional, page 478

Purpose.  We need double integrals (and line integrals) in the next section and review them here for completeness; suggesting that the student go on to the next section.

## Comment

Definition; evaluation; and properties of double integrals

Some standard applications

Change of variables; Jacobians

## SOLUTIONS TO PROBLEM SET 9.3, page 484

2. Integrate over y to get

as before.

4. This order of integration is less practical because we have to split the integral into parts, two

<!-- formula-not-decoded -->

By integration over y we from the first part get

<!-- formula-not-decoded -->

The other part gives 27, too. Answer: 54.

6. After the integration over y we have

<!-- formula-not-decoded -->

8. We now have

<!-- formula-not-decoded -->

10. After the integration over x have we

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

14. 2b/3, hl3

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SECTION 9.4. Green's Theorem in the Plane, page 485

Purpose. To state, prove, and apply Green's theorem in the plane; relating line and double integrals.

## Comment on the Role of Green's Theorem in the Plane

This theorem is a special case of each of the two "big" integral theorems in this chapter, Gauss's and Stokes's theorems (Secs. 9.7,9.9), but we need it as the essential tool in the of Stokes' s theorem. proof

The present theorem must not be confused with Green's first and second theorems in Sec. 9.8

## SOLUTIONS TO PROBLEM SET 9.4, page 490

2. 4

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Here, the minus sign was needed because the sense of integration was such that the region was to the right of the curve.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

20. PROJECT. We obtain div F in (11) if we take F = ~F1] n = [y ~x' ] as in Example 4, we get from (1) the right side in (11), Taking

<!-- formula-not-decoded -->

Formula (12) follows from the explanation of (1').

= 4 times the area of the disk of radius 2 gives l67. For the line integral in (11) we need

<!-- formula-not-decoded -->

This gives

<!-- formula-not-decoded -->

In (12) we have curl F = and

<!-- formula-not-decoded -->

which gives zero upon integration from 0 to

## SECTION 9.5. Surfaces for Surface Integrals, page 491

Purpose. The section heading indicates that we are with a tool in surface integrals, and we concentrate our discussion accordingly. dealing

## Main Content, Important Concepts

Parametric surface representation (2) (see also Fig. 221)

Surface normal vector N, unit surface normal vector n

Short Courses. Discuss (2) and (4) and a simple example.

## Comments on Text and Problems

The student should realize and understand that the present parametric representations are the two-dimensional analog of parametric curve representations.

Problems 1-10 concern some standard surfaces of interest in applications. We shall need only a few of these surfaces; but these problems should help students grasp the idea of a parametric representation and see the relation to representations (1) Moreover, it may be to collect surfaces of practical interest in one place for possible reference. good

## SOLUTIONS TO PROBLEM SET 9.5, page 495

2. uk; note that this normal vector becomes the zero vector at the origin, where (4) is violated.
2. u] ~2u2
3. = 1, ellipses,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

10. = arc tan (ylx), helices; horizontal straight lines, [sin v, u]
12. [u, v, u], [~1, 0, 1]
14. [2 cos u, 3 sin u, v], [3 cos u, 2 sin u, 0]
16. [2 cos v cos u, 1 + 2 cos v sin u, ~2 + 2 sin v]; [4 cos u cos? v, 4 sin u 4 sin v cos v] cos?
18. [2u cos 0, 2u], [~2u cos v, 2u]
20. At the origin; in Prob. 3 because of the apex of the cone, in the other problems because of the representation.

22. Because Fu and rv are tangent to the coordinate curves v const and u = const; respectively.

28. (x2 + y? + z2)-12 [x, ~y, z]
2. the scalar triple product implies that r* r(P) lies in the tangent plane T(P).
3. () Geometrically, the vanishing of the dot product means that r* r(P) must be perpendicular to Vg, which is a normal vector of $ at P.
4. (x*, y* z* = X, = y gives z* = 2, so that T(P) passes through P, as it should. point x*

## SECTION 9.6. Surface Integrals; page 496

Purpose.  We define and discuss surface integrals with and without into account surface orientations. taking

## Main Content

Surface integrals (3) = (4) = (6)

Change of orientation (Theorem 1)

Integrals (7) without regard to orientation; also (11)

## Comments on Content

The right side of (3) shows that we need only N but not the corresponding unit vector n. An orientation results automatically from the choice of a surface representation, which determines ru and rv and thus N.

The existence of nonorientable surfaces is interesting; but is not needed in our further work

## SOLUTIONS TO PROBLEM SET 9.6, page 503

2. r = [u, 1 1] N = [1, 1, 1] (which is obvious without calculation) F(r)  N = u2 + e + 1. Answer: e 17/12 ~ 1.30
4. F(r) [sinh (cos v sin v), 0 cos4 v], N = [0, ~Cos U, ~sin v], F(r) * N = 16/5
6. r = [cos u, sin u, 0],
8. N = [cosh u, ~sinh u, = 2 cosh? u sinh u. Answer: 4 cosh? 2 -4
10. F(r) = [u? cos? v, u2 sin? v, 9v2], N = [3 sin v, u], F(r) * N = 9uv? + 3u?(cos? v sin v cos v sin? v) The integral of 9uv? is 1273 . The integral of the other term is zero. Answer: 1273

<!-- formula-not-decoded -->

Answer: (2 sin

14. N = [5 cos u, 5 sin u, 0], [Nl = 5, G(r)[NI = 5 . 625(cos4 u + sin4 u). Integration OveI u
2. = V5(us 4u3). Answer:

<!-- formula-not-decoded -->

22. hT(l + h216)
24. Proof for lamina $ of density 0. Choose coordinates so that A is the z-axis and B is the line x = k in the xz-plane. Then

<!-- formula-not-decoded -->

the second integral being zero because it is the first moment of the mass about an axis through the center of gravity.

26. TEAM PROJECT. (a) Use dr = Fu du dv. This gives (13) and (14) because 4 Iv

For a mass distributed in a region in space the idea of proof is the same

<!-- formula-not-decoded -->

- @) E, F, G appear if you express everything in terms of dot products. In the numerator,

<!-- formula-not-decoded -->

and similarly in the denominator.

- This follows by Lagrange' s identity (Problem Set 8.3),

<!-- formula-not-decoded -->

- (d) r = [u cos v, sin v] Fu = [cos v, = cos? v + sin? v = 1, etc\_
- (e) By straightforward calculation E = (a + b cos v)2, F = 0 (the coordinate curves on the torus are orthogonal!), and G = b2. Hence, as expected,

<!-- formula-not-decoded -->

## SECTION 9.7. Triple Integrals. Divergence Theorem of Gauss, page 505

## Purpose; Content

Proof and application of the first &lt;big" integral theorem in this chapter, Gauss' s theorem; preceded by a short discussion of triple integrals (probably known to most students from calculus) .

## Comment on Proof

The proof is simple:

- Cut (2) into three components. Take the third, (6).
2. On the left; integrate dz
- (9) Jf[Fs(upper surface) F3(lower surface)] dx dy integrated over the projection R of the region in the xy-plane (Fig: 231).
3. Show that the right side of (6) equals (9). Since the third component of n is cos Y, the right side is

<!-- formula-not-decoded -->

where minus comes from cos Y &lt; 0 in 231, lower surface. This is the Everything else is (necessary) accessory. Fig; proof.

## SOLUTIONS TO PROBLEM SET 9.7, page 509

2. Integration over gives   successively ~e-1-2 + ~2e-1-2 4 2e-1 + 1. e-2 2e-3
4. In coordinates, 0 r4/3. The integral is polar

<!-- formula-not-decoded -->

6. We may integrate in the order 0 = z = x, 0 =y=1 - x2,0 =x = 1. This gives 2r2, then 2x2(1 x2), and finally the answer 4/15.
14. div F = e" + eu + e?. Integration over x gives 2sinh 1 + 2ey + 2e2. Integration over y then gives 4 sinh 1 4 4 sinh 1 + 4e? . Integration over z gives the answer 24 sinh 1-

<!-- formula-not-decoded -->

16. div F ~sin z Integration over gives cos 2 1. Multiplication by the cross1) ~ ~40.04.
18. div F = + T sin "z. Integration over from 0 to 1 y gives 1 + (1 \_ x - y)(4x + y) cOS [T(1 Then integration over y from 0 to 1 x gives 4 y y)]

<!-- formula-not-decoded -->

Integration over x from 0 to 1 now gives the answer 17/24

## SECTION 9.8. Further Applications of the Divergence Theorem, page 510

Purpose: To represent the divergence free of coordinates (Example 1), t0 show that it measures the source intensity (Example 2), to use Gauss' s theorem for deriving the

heat equation governing heat flow in a region; and to obtain basic properties of harmonic functions.

## Main Content, Important Concepts

Divergence as the limit of a surface integral; see (3)

Total flow (4) out of a region

Heat equation (7) (to be discussed further in Chap. 11)

Properties of harmonic functions (Theorems 1-3)

Green' s formulas (10), (11)

Short Courses. This section can be omitted.

## Comments on (3)

Equation (3) is sometimes used as a definition of the divergence; giving independence of the choice of coordinates immediately. Also; Gauss' s theorem follows more readily, but since its proof is simple (see Sec. 9.7. in this Manual) , that savings is marginal. it seems that to the student our Example 2 in Sec. 8.10 motivates the divergence at least as well (and without integrals) as (3) does for a beginner. Also;

## SOLUTIONS TO PROBLEM SET 9.8, page 514

2. = [2 cos 0, = n = [cos 0, sin 0], f = 4 cos2 0 = = 4 4 sin? 0 = 4 cos 20 gives the integral zero. The inteover the disks (z 0 and z = 1) are zero, too, since Vf has no component in z-direction (the normal direction of those disks) . cos? grals
2. 4 div F 10. Answer: 10 times the volume Tr2hl3 of a cone of base radius and
6. div F = 10 + 322. Hence

<!-- formula-not-decoded -->

8. div F = x + y. (a) In polar coordinates (cylindrical coordinates)

<!-- formula-not-decoded -->

- (b) In Cartesian coordinates,

<!-- formula-not-decoded -->

10.

12. TEAM PROJECT. (a) Put f = g in (10)
2. (b) Use (a)
3. (c) Use (11).

- (e) Use div grad f = V2f .
- 0 on $. Thus h const in Tby (b)

## SECTION 9.9. Stokes's Theorem; page 515

Purpose. To prove, explain; and apply Stokes' s theorem; relating line and surface integrals.

## Main Content

Formula (2) = (3)

Further interpretation of the curl (see also Sec. 8.11)

Path independence of line integrals (leftover from Sec. 9.2)

## Comment on Orientation

Since the choice of right-handed or left-handed coordinates is essential to the curl (Sec. 8.11) surface orientation becomes essential here (Fig. 232).

## Comment on Proof

The proof is simple:

- 2.
3. Transform the right side of (4) by Green's theorem into a double integral and show equality with the integral obtained on the left.

## SOLUTIONS TO PROBLEM SET 9.9, page 520

<!-- formula-not-decoded -->

Line integral: Over the x-axis from -2 to 2 we obtain

<!-- formula-not-decoded -->

and over the semicircle r = [2 cos t, 2 sin t, 0], thus r = [~2sin t, 2 cos t, 0], we obtain

<!-- formula-not-decoded -->

The verifications in Probs . 1-6 are supposed to familiarize the student more thor oughly with the nature and significance of Stokes' s theorem.

<!-- formula-not-decoded -->

Line integral: The two circular arcs contribute nothing; = as can be seen from F, whose first two components are zero. From (~1, 0, 0) straight up to (~1, 0, "l4) we get

<!-- formula-not-decoded -->

Similarly, ~2 is obtained for the straight-line segment from (1, 0, "/4) to (1, 0, 0). 6.

- curl F [~2z, ~2x, ~2y] r [cos v cos u, COs U sin u, 1 4 sin v], cos? v sin u,

<!-- formula-not-decoded -->

(~cos3 v sin 2u 2 cos u cos2 v (1 + sin v) 2v) du dv

<!-- formula-not-decoded -->

Verification: The line integral over the horizontal semicircle equals +4/3, as in Prob. 5. Over the vertical   semicircle it is zerO because r = [t, 0 V1 = +2] r = [1, 0, [0, t2, t2], so that the

8. curl F = (1 x2, we have

<!-- formula-not-decoded -->

10. curl F = [1, 0, ~1], N = [-1, 0, 1], (curl F)n = ~V2 Multiplication by the area 9a V2 gives the answer
12. curl F 0. Answer: 0
3. 14 r = [cos 0, sin 8, 0]- Hence

<!-- formula-not-decoded -->

## SOLUTIONS TO CHAPTER 9 REVIEW, page 521

- 16 ~ 325/3 by exactness from f 2y3)/3, OI by integration from r = [4 7t, 2 + 3t], r [-7, 3],

<!-- formula-not-decoded -->

18. Not exact, C: r = [x, 2x2, x], r [1, 1]. F(r) = [2x3, 0] Hence Ax,

<!-- formula-not-decoded -->

20. Not exact. By Green's theorem in the plane, using coordinates, we obtain polar

<!-- formula-not-decoded -->

22. curl F = [~1, =1, 5], N = +[-1, 1], (curl F) 'n Answer: +241 ~ 75.4
24. Exact, e = 2 sinh 1 from f = + cosh 2y ex2

26. By Green's theorem in the plane,
30. Not exact, r [~sin t, COS t, 3], F(r) [cos? t, sin? t, sin? t cos t], ~cos? t sin t + 4 sin? t cos t. Answer: 1

Answer: +(3e2

2 In 2 = 3).

<!-- formula-not-decoded -->

34. M = Ta2/2, 7 = 0 (symmetry) 4a M

<!-- formula-not-decoded -->

38. r = [v, 2 cos u, 2 sin u], F(r) = [sin v, 2 sin u, 2 cos u], N = [0, 2 cos u, 2 sin u], F(r)  N = 8 cos u sin u. Answer: 4

+ y? + 22). Hence in Cartesian coordinates, 3(+2

<!-- formula-not-decoded -->

In spherical coordinates; with dx dy dz = r2 sin ø dr dø de,

<!-- formula-not-decoded -->

42. N = [2, =1, 0], F(r) = [e2u, 0, veu] F(r) N = 2e2u . Answer: 6 sinh 2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## PART C. FOURIER ANALYSIS AND PARTIAL DIFFERENTIAL EQUATIONS

## CHAPTER 10 Fourier Series, Integrals, and Transforms

## Change

The presentation was streamlined by moving half-range expansions into the section on even and odd functions.

## SECTION 10.1. Periodic Functions. Trigonometric Series, page 527

Purpose. To show what a Fourier series will look like; in Problem Set 10.1, to give a first impression of what kind of functions will occur in this chapter.

## Basic Concepts

Periodic function

Trigonometric system

Trigonometric series

## Comment on Footnote 1

Fourier series were used in special problems much earlier by Daniel Bernoulli (1700 1782) in 1748 (vibrating string, Sec. 11.3) and Euler (Sec. 2.6) in 1754 (Euler formulas; Sec. 10.2). Fourier' s book of 1822 became the source of many mathematical methods in classical mathematical physics. Furthermore; the surprising fact that Fourier series, whose terms are continuous functions, may represent discontinuous functions led to a reflection on, and generalization of, the concept of a function in general. Hence the book is a landmark in both pure and applied mathematics. [That surprising fact also led to a controversy between Euler and D. Bernoulli over the question of whether the two types of solution of the vibrating problem (Secs. 11.3 and 11.4) are identical; for details, see E. T. Bell, The Development of Mathematics, New York: McGraw-Hill, 1940, p. 482] A mathe matical theory of Fourier series was started by Peter Gustav Lejeune Dirichlet (1805 1859) of Berlin in 1829. The concept of the Riemann integral also resulted from work on Fourier series. Later on, these series became the model case in the theory of orthogonal functions (Sec. 4.7). An English translation of Fourier's book was published by Dover Publications in 1955. string

## SOLUTIONS TO PROBLEM SET 10.1, page 528

- 2uln, k, kIn;
4. True when n = f(x) Now set x + np = Z. Then f(x + (n + I)p) = f(z + p) = f(z) = f(x)
6. f(x + p) = f(x) implies f(ax + p) = f(a[x + (pla)]) = f(ax) Or g[x + (pla)] g(x), where g(x) f(ax) Thus g(x) has period This proves the first statement; and the other statement follows by setting a = pla.
8. A common source of errors here and throughout this chapter results from the fact that the student often does not pay attention to the interval on which the function is

Note that the first of these is preferable because it shows more immediately whether function is odd or even (or neither).

20. CAS PROJECT.  This 'experimental approach" to trigonometric and Fourier series should help the student obtain a and for the kind and quality of convergence; depending on continuity properties of the sum of the series feeling

Convergence is best for the first of the three series because its sum is continu ous-note that the coefficients are proportional to whereas for the other two se ries are only proportional to IIn. The second series has the square wave in Prob . 15 as its sum. The third series has the sum f(x) = X. Hopefully it will puzzle the stu dent by its poor convergence behavior (and the Gibbs phenomenon) near the discon tinuity points at x = hand limits, which is typical (see Sec. 10.2). +? they

## SECTION 10.2. Fourier Series, page 529

Purpose; To derive the Euler formulas (6) for the coefficients of a Fourier series (7) of a given function of period 2m, using the property of the orthogonality of the trigonometric system. key

## Main Content, Important Concepts

Euler formulas (6) for Fourier coefficients (period

Orthogonality of the trigonometric system

Convergence and sum of a Fourier series (Theorem 1)

## Comment on Notation

If we write instead of % in (1), we must do the same in (6a) and see that (6a) then becomes (6b) with n =0 This is merely a small notational convenience (but may be a source of confusion to poorer students)

## Comment on Fourier Series

Whereas their theory is involved, practical applications are simple, once the student has become used t0 evaluating integrals in (6) that depend on n. quite

Figure 238 should help students understand why and how a series of continuous terms can have a discontinuous sum

## SOLUTIONS TO PROBLEM SET 10.2, page 536

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

18. The student should be encouraged to choose any other integrals of products of cosines and sines. The is to realize the importance of the interval in connection with orthogonality. The integral suggested in the problem has the value sin a 4 sin 7a. The figure suggests orthogonality for a expected. point

Section 10.2. Integral in Problem 18

<!-- image -->

## SECTION 10.3. Functions of Period p 2L, page 537 Any

Purpose. Transition from period 2m to period 2L (a notation practical later), simply by a

## SOLUTIONS TO PROBLEM SET 10.3, page 540

2. 1 times the answer to Prob. 1 6.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

16. In Prob. 7, Sec. 10.2, write t for x and

<!-- formula-not-decoded -->

Now set t ax to get = 72x2, which shows that the series should be multiplied that of get

<!-- formula-not-decoded -->

## 20. CAS PROJECT. The figure shows s2o(x)

Section 10.3. Gibbs phenomenon in CAS Project 20

<!-- image -->

## SECTION 10.4. Even and Odd Functions. Half-Range Expansions, page 541

Purpose; 1. To show that a Fourier series of an even function (an odd function) has only cosine terms (only sine terms) so that unnecessary work (and sources of errors!) is avoided.

2. To represent a function f(x) by a Fourier cosine series or by a Fourier sine series (of period 2L) if fx) is given on an interval 0 = x = L only, which is half the interval of periodicity\_hence the name 'half-range:'

## Comment

shown in 11. Chap.

## SOLUTIONS TO PROBLEM SET 10.4, page 546

4. Neither even nor odd. The problem shows that the student must always pay careful attention to the interval on which the function is given because for different functions, different intervals are practical.
6. Even
3. 8 Neither even nor odd
10. PROJECT. (a) Sums and products of even functions are even. Sums of odd functions are odd. Products of odd functions are odd (even) if the number of their factors is odd (even). Products of an even times and odd function are odd. This is important in connection with the integrands in the Euler formulas for the Fourier coefficients. Absolute values of odd functions are even. f(x) + f(-x) is even; f(x) f(-x) is odd.
+ furthermore, ~x2

<!-- formula-not-decoded -->

- (c) f(-x) = -f(x) and f(-x) = f(x) together imply f = 0.
- (d) cos3 x is even, sin? x is odd. The Fourier series are the familiar identities

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

18. Set x T to get

<!-- formula-not-decoded -->

The result was first obtained by Euler.

20. The even periodic extension has the Fourier series f(r) = 1. For the odd half-range expansion we obtain

<!-- formula-not-decoded -->

22. The cosine series is

<!-- formula-not-decoded -->

Its Fourier coefficients are proportional to IIn?, reflecting the fact that its sum is continuous. The sine series is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Its coefficients are only proportional to reflecting the fact that its sum is discontinuous .

24. The cosine series is

<!-- formula-not-decoded -->

Its sum is continuous. Its coefficients go to zero faster than those of the sine series

<!-- formula-not-decoded -->

whose sum is discontinuous .

## SECTION 10.5. Complex Fourier Series. Optional, page 547

Purpose; To show that the formula for ei0 or direct derivation leads to the complex Fourier is

Short Courses. Sections 10.5-10.11 can be omitted.

## SOLUTIONS TO PROBLEM SET 10.5, page 549

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

10. PROJECT. When n =m; the integrand of the integral on the right is e0 = 1, s0 that the integral equals 2u. This gives

<!-- formula-not-decoded -->

provided the other integrals are zero, which is true by (5),

<!-- formula-not-decoded -->

Now writing n for m in (A) gives the coefficient formula in (8).

## SECTION 10.6. Forced Oscillations, page 550

Purpose. To show that mechanical or electrical systems with periodic but nonsinusoidal input may respond predominantly to one of the infinitely many terms in the Fourier series of the input, giving an unexpected output; see 252, where the output frequency is essentially five times that of the input. Fig;

Short Courses. Sections 10.5-10.11 can be omitted.

## SOLUTIONS TO PROBLEM SET 10.6, page 552

2. r(t) is given by the sine series in Example 1, Sec. 10.2, with k = ~1. The new Cn is n times the old, so that C5 is so that the output is practically a cosine vibration having five times the input frequency. Replacement of the right side by its inte(with r(O) = 0) also produces an increase of C5' large gral

<!-- formula-not-decoded -->

|               | 0.5          | 0.9    | 1.1    | 2.0    | 2.9    | 3.1    | 4.0    | 4.9   |   5.1 |   6.0 |   8.0 |
|---------------|--------------|--------|--------|--------|--------|--------|--------|-------|-------|-------|-------|
| B1            |              | ~5.3   | 4,8    | 0.33   | 0.13   | 0.12   | 0.07   | 0.04  |  0.04 | 0.03  | 0.02  |
| B3 = 1/9(? 9) | ~0.013       | ~0.014 | ~0.014 | ~0.02  | ~0.19  | 0.18   | 0.02   | 0.01  |  0.01 | 0.004 | 0.002 |
| Bs 1/25(2     | 25) / ~0.002 | ~0.002 | ~0.002 | ~0.002 | ~0.002 | ~0.003 | ~0.004 | ~0.04 |  0.04 | 0.004 | 0.001 |

the terms of the input r(t), then the output corresponding to that term becomes comparatively if w is near 5. The effect would even be stronger had we chosen all coefficients on the right equal to 1, instead of lIn? as in the partial sum of a Fourier series. large

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

10. The situation is the same as that in Fig. 57 in Sec. 2.11.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SECTION 10.7. Approximation by Trigonometric Polynomials, page 553

## Important Concepts

Purpose; We show how to find "best" approximations of a given function by trigonometric polynomials of a given degree N.

Trigonometric polynomial

Square error

Parseval' s identity

Short Courses. Sections 10.5-10.11 can be omitted.

## Comment on Quality of Approximation

This quality can be measured in many ways. Particularly important are (i) the absolute value of the maximum deviation over a given interval; and (ii) the mean square error considered here. See Ref. [9] in Appendix 1.

## SOLUTIONS TO PROBLEM SET 10.7, page 556

<!-- formula-not-decoded -->

The integral is 3020/945 3.196; E* = 0.054, 0.0054, 0.0011, 0.00032, 0.00012.

10. CAS PROJECT. (a) In part because of the Gibbs phenomenon (see Problem Set 10.3).
2. () For the continuous function (Prob. 4), E* equals (rounded)

0.0068, 0.0055, 0.0045, 0.0037,

For the discontinuous function (Example 1 in the text), E* equals

<!-- formula-not-decoded -->

It is typical that in the discontinuous case, the Fourier coefficients are only proportional to lln; whereas in continuous cases are etc. they

In Prob. 5 the initial error E* is very large (863), and E* decreases very slowly; it is still 1.53 for 800 terms and 0.408 for 3000 terms.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SECTION 10.8. Fourier Integrals, page 557

Purpose. Beginning in this section; we show how ideas from Fourier series can be extended to nonperiodic functions defined on the real line; leading to integrals instead of series .

## Main Content, Important Concepts

Fourier integral (5)

Existence Theorem 1

Fourier cosine integral, Fourier sine integral, (10)-(13)

Application to integration

Short Courses. Sections 10.5-10.11 can be omitted.

## SOLUTIONS TO PROBLEM SET 10.8, page 563

- T 2. The result suggests to consider f(x) = if 0 &lt; x &lt; 1 and f(x) = 0 if x &gt; 1. 2

sin w From (10) we obtain A(w) and by inserting this into (11) the result follows. W

<!-- formula-not-decoded -->

6. Taking f(x) (x &gt; 0), we obtain from (12)

<!-- formula-not-decoded -->

Here we used (11) in Appendix A3.1. Integration by parts yields

<!-- formula-not-decoded -->

From this and (13) the result follows.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 2 2 14. B(w) = = (sin aw aw cos aw), s0 that the answer is T Tw2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

20. PROJECT. (a) Formula (al): Setting wa p, we have from (11)

<!-- formula-not-decoded -->

If we again write w instead of p, we obtain (al)

Formula (a2): From (12) with f(v) replaced by vf(v) we have

<!-- formula-not-decoded -->

where the last equality follows from (10).

Formula (a3) follows by differentiating (10) twice with respect to w;

<!-- formula-not-decoded -->

- (b) In Prob. we have

<!-- formula-not-decoded -->

Hence by differentiating twice;

<!-- formula-not-decoded -->

By (a3) we now the result, as before, get

<!-- formula-not-decoded -->

- (c) A(w) = (2 sin aw)lTw; see Prob. 7. By differentiation,

<!-- formula-not-decoded -->

This agrees with the answer to Prob. 14.

- (d) The derivation of the following formulas is similar to that of (al)-(a3).

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d2) xf(x) = C*(w) cos xw dw, C*(w) = B as in (12) dw

<!-- formula-not-decoded -->

- (d3) x2f(x) = D*(w) sin xw dw, D*(w) = dw2

## SECTION 10.9. Fourier Cosine and Sine Transforms; page 564

Purpose. Fourier cosine and sine transforms are obtained immediately from Fourier cosine and sine integrals, respectively, and we investigate some of their properties.

## Content

Fourier cosine and sine transforms

Transforms of derivatives (8), (9)

## Comment on Purpose of Transforms

Just as the Laplace transform (Chap. 5), these transforms are designed for solving differential equations. We show this for differential equations in Sec. 11.6. partial

## SOLUTIONS TO PROBLEM SET 10.9, page 568

2. From (3) and the answer to Prob. 1 we obtain

<!-- formula-not-decoded -->

Problem 2 in Problem Set 10.8 shows that the first term is 2 if 0 &lt; x &lt; 1 and 0 if x &gt; 1Set 2w = u in the second term and conclude that the second term is \_1 if 0 &lt; xl2 &lt; 1 or 0 &lt; x &lt; 2 This agrees with Prob. 1.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

20. WRITING PROJECT. Methods include integration; the use of the operational formulas (8) and (9) (independently or together with the use of the tables in Sec. 10.11), and the use of integrals from Sec. 10.8. By presenting this in a systematic fashion; the student should better for these transform methods. gain feeling

Purpose: Derivation of the Fourier transform from the complex form of the Fourier integral; explanation of its physical meaning and its basic properties .

## Main Content, Important Concepts

Complex Fourier integral (4)

Fourier transform (6), its inverse (7)

Spectral representation;, spectral density

Transforms of derivatives

Convolution f * g

## Comments on Content

Note that convolution f * g differs from that in Chapter 5, and so does the formula (12) in the convolution theorem (we now have a factor V27).

The complex Fourier integral is relatively easily obtained from the real Fourier integral in Sec. 10.8, and the definition of the Fourier transform is then immediate.

## SOLUTIONS TO PROBLEM SET 10.10, page 575

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- ~0 ~t. Then

<!-- formula-not-decoded -->

Divide by 1 + iw to get the result.

Together,

30. For instance, use Prob. 23.

32. For instance, use Prob. 17.

36. y = C1 cOS @t + C2 sin @t

<!-- formula-not-decoded -->

38. 2w cos

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 16 TEAM PROJECT. (a) Use t = x a as a new variable of integration.
- () Use c = 3b.
- (c) Replace w by w a. This gives a new factor e

## SOLUTIONS TO CHAPTER 10 REVIEW, page 579

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## CHAPTER 1l Partial Differential Equations

## Change

The Fourier transform method has been included in the section on Fourier integrals for heat problems (Sec. 11.6).

## SECTION 11.1 Basic Concepts, page 583

Purpose: To familiarize the student with the following:

Concept of solution, verification of solutions

Superposition principle for homogeneous linear equations

Equations solvable by methods for ordinary differential equations

## SOLUTIONS TO PROBLEM SET 11.1, page 584

<!-- formula-not-decoded -->

## SECTION 11.2. Modeling: Vibrating String; Wave Equation; page 585

Purpose; A careful derivation of the one-dimensional wave equation (more careful than in most other texts; where some of the essential physical assumptions are usually missing) Short Courses; One may perhaps omit the derivation and just state the wave equation and mention of what c2 is composed.

## SECTION 11.3. Separation of Variables. Use of Fourier Series, page 587

- 1 To familiarize the student with the wave equation and with the typical initial and boundary conditions that physically meaningful solutions must satisfy.

Purpose  This first section in which we solve a "big" problem has several purposes:

- 2 To explain and apply the important method of separation of variables; by which the partial differential equation is reduced to ordinary differential equations.
4. To discuss the eigenfunctions of the problem; the basic building blocks of the soluwhich lead to a deeper understanding of the whole problem. tion,
3. To show how Fourier series help to get the final answer; thus seeing the reward of our great and effort in 10. long Chap.

## Steps of Solution

1. Setting u = F(x)G(t) gives two ordinary differential equations for F and G.
2. The boundary conditions lead to sine and cosine solutions of the latter.
3. A series of those solutions with coefficients determined from the Fourier series of the initial conditions gives the final answer

## SOLUTIONS TO PROBLEM SET 11.3, page 594

2. 0.01 cos 3t sin 3x

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Taking the separation constant negative; we obtain a similar result. Taking it zero, we have

<!-- formula-not-decoded -->

20. TEAM PROJECT. (c) From the given initial conditions we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SECTION 11.4. D'Alembert's Solution of the Wave Equation; page 595

Purpose: To show a simpler method of solving the wave equation; which, unfortunately , is not s0 universal as separation of variables.

## Comment on Order of Sections

Section 11.12on the solution of the wave equation by the Laplace transform may be studcause some students may not have studied Chap. 5 on the Laplace transform; which is not a prerequisite for 11. Chap.

## Comment on Footnote 2

D'Alembert' s Traité de dynamique appeared in 1743 and his solution of the vibrating string problem in 1747; the latter makes him; together with Daniel Bernoulli (1700 1782), the founder of the of partial differential equations. In 1754 d Alembert be came of science in France. theory

## SOLUTIONS TO PROBLEM SET 11.4, page 597

2. T = 200 nt, p = 0.8/(2 9.80) nt sec?Imeter?, c2 = Answer: 70 meters/sec
4. u(o, t) =

hence which proves the periodicity .

14. Hyperbolic; y'2 \_ y' \_ 2 = (y' + I)ly' = Uuz

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

20. TEAM PROJECT. (b) Fn = sin (nmxlL), Gn = an COS The solution satisfying the initial conditions is

<!-- formula-not-decoded -->

For the the frequency of the nth normal mode is proportional to n; whereas for the beam it is proportional to n2. string

<!-- formula-not-decoded -->

- (c) u(o, t) =

With this we further obtain

<!-- formula-not-decoded -->

This homogeneous system has a nontrivial solution if and only if its determinant is zero. Thus   (cos ßL cosh 4 sinh? ßL 0 OI 2 ~ 2 cos BL cosh ßL = 0. BL)? sin?

From this we have (17), which can be written

<!-- formula-not-decoded -->

because cosh ßL is very large. This gives approximate solutions

<!-- formula-not-decoded -->

BL sinh? ßL of this system must be zero, and from this the result follows. sin?

From (18) have we

<!-- formula-not-decoded -->

because cosh ßL is very large. This gives the approximate solutions

<!-- formula-not-decoded -->

## SECTION 11.5. Heat Equation: Solution by Fourier Series, page 600

1. To solve a typical heat problem by steps similar to those for the wave equation; pointing to the two main differences: only one initial condition (instead of two) and uz (instead of utt), resulting in exponential functions in t (instead of cosine and sine in the wave equation)
2. Solution of Laplace' s equation (which can be interpreted as a time-independent heat equation in two dimensions).

## Comments on Content

Additional points to emphasize are

More decay with increasing n, rapid

Difference in time evolution in 267 and 263, Figs.

Zero can be an eigenvalue (see Example 4)

Three standard types of boundary value problems;

Analogy of electrostatic and (steady-state) heat problems.

Problem Set 11.5 includes additional heat problems and types of boundary conditions.

## SOLUTIONS TO PROBLEM SET 11.5, page 608

2. A12 (In 2)/20, c2 = 0.003512

4. u = k sin 0.2ax e-1.75272t/25

<!-- formula-not-decoded -->

8. u(x; t) = with u1 as in Prob. 7 and where

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

12. u(x; t) = cos 2x e-4t

14. w" = = w(L) = 0 to get the function

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

18. CAS PROJECT. (a) u = sin Tx sinh Tylsinh 27.

20.

(b) uy(x; 0, t) =

=

F(x)G(y),

F

=

A cos px

=

0,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Hence p must satisfy tan ap = which has infinitely many positive real solutions p as you can illustrate by a simple sketch. Answer: hlp,

<!-- formula-not-decoded -->

where Y = = h.

To determine coefficients of series of un s from a boundary condition at the lower side is difficult because that would not be a Fourier series, the Yn's only approximately regularly spaced. See [C1], pp. 114-119, 167. being

## SECTION 11.6. Heat Equation: Solution by Fourier Integrals and Transforms, page 610

Purpose; Whereas we solved the problem of a finite bar in the last section by Fourier series, we show that for an infinite bar (practically; a long insulated wire) we can use the Fourier integral for the same purpose: Figure 271 shows the time evolution for a "rectangular" initial temperature (10O C between x ~1 and +1, zero elsewhere), giving bell-shaped curves as for the density of the normal distribution. using

B

= 0,

We also show typical applications of the Fourier transform and the Fourier sine transform to the heat equation.

Short Courses. This section can be omitted.

## SOLUTIONS TO PROBLEM SET 11.6, page 615

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

10. CAS PROJECT. (a) Set w = ~vin (21) to get erf(~x) = ~erf x

- () See (36) in Appendix A3.1.

<!-- formula-not-decoded -->

- (f)

## SECTION 11.7. Modeling: Membrane, Two-Dimensional Wave Equation; page 616

Purpose. A careful derivation of the two-dimensional wave equation governing the motions of a drumhead, from physical assumptions (the analog of the modeling in Sec. 11.2)

## SECTION 11.8. Rectangular Membrane. Use of Double Fourier Series, page 619

Purpose. To solve the two-dimensional wave equation in a rectangle 0 = 0 = y = b ("rectangular membrane") by separation of variables and double Fourier series.

## Comment on Content

New features as compared to the one-dimensional case (Sec. 11.3) are as follows:

1. We have to separate twice, first by u = F(x; y)G(t) , then the Helmholtz equation for Fby F =
2. We get a double sequence of infinitely many eigenvalues and eigenfunctions umn; see (12), (13). Amn
3. We need double Fourier series (easily obtainable from the usual Fourier series) to get a solution that also satisfies the initial conditions.

## SOLUTIONS TO PROBLEM SET 11.8, page 626

6. otherwise Bmn

10. CAS PROJECT. (b) The figure shows the first partial sum (a single term) and the partial sum of the terms up to that with coefficient b55 (9 terms).
8. = Bmn

12. u =

<!-- formula-not-decoded -->

16. A = ab, b s0 that from (12) with m = n = 1 by differentiating to a and equating the derivative to zero, we obtain with respect Ala,

<!-- formula-not-decoded -->

hence a4 = A2, a2 = A, b = Ala = a.

<!-- formula-not-decoded -->

18. CT '260 (corresponding eigenfunctions F '16,14), etc. F4,16,

## SECTION 11.9. Laplacian in Polar Coordinates; page 626

Purpose; A detailed discussion of the transformation of the Laplacian into polar coordinates as a typical case of a task often required in applications: The result (4) will be needed in the next section.

Short Courses. This section can be omitted:

## SOLUTIONS TO PROBLEM SET 11.9, page 628

- 0) = x2 \_ y2, r2 sin 20 = etc\_ 2xy, (c) sin?

<!-- formula-not-decoded -->

Section 11.8. CAS Project 10(b). Two partial sums

<!-- image -->

- (d) The form of the series results as in () and the formulas for the coefficients fol-

<!-- formula-not-decoded -->

8. u(0) = cos 20 Sr2

<!-- formula-not-decoded -->

12. sin 30. Note that this also follows from Prob. 7 because of the skew symmetry of the boundary condition as a function of 0. 25r3

<!-- formula-not-decoded -->

## SECTION 11.10. Circular Membrane: Use of Fourier-Bessel Series; page 629

Purpose. To derive the function that gives the vibrations of a circular membrane, by solvthe wave equation in coordinates. polar ing

## Comment on Content

We concentrate on the simpler case of radially symmetric vibrations; that is, vibrations independent of the angle (For eigenfunctions depending on the angle; see Probs. 11-18.) We do three steps:

1. = W(r)G(t)  gives  for W Bessel's   equation with 0, hence solutions W(r) Jo(kr)
2. We satisfy the boundary condition W(R) = 0 by choosing suitable values of k.
3. A Fourier-Bessel series (13) helps to get the solution (12) of the entire problem.

Short Courses. This section can be omitted.

## SOLUTIONS TO PROBLEM SET 11.10, page 634

2. f1 = ck1l27 = 0.3827cIR = 0.3827VTlpR?
2. 4 In coordinates the boundary has the simple representation R const. polar
3. CAS PROJECT () Error 0.04864 (m 0.00690, 0.00589, 0.00512, 0.00454, 0.00408 (m 10)
8. From (24), Sec. 4.5, we have (rJ (r)) rJo(r). By integration

<!-- formula-not-decoded -->

0 because the initial deflection is zero. From (15) and (A), with g(r) = 1 and Qmr s, we obtain @m

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Hence the series is

<!-- formula-not-decoded -->

- is already correct to 3 significant digits.

18. 0.6099 (see Table Al in Appendix 5)

## SECTION 11.11. Laplace's Equation in Cylindrical and Spherical Coordinates. Potential, page 636

- Purpose: 1. Transformation of the Laplacian into cylindrical coordinates (which is trivial because of Sec: 11.9) and spherical coordinates; some remarks on areas in which Laplace's equation is basic.
- 2 Separation of the Laplace equation in spherical coordinates and application to a typical boundary value problem:. For simplicity we consider a boundary value problem for a
- 1 G(r)H(%) and separation gives for H Legendre' s equation.
3. A Fourier\_Legendre series (17) helps to get the solution (16) of the interior problem. Similarly for the exterior problem; whose solution is (19).
2. Continuity requirements restrict H to Legendre polynomials.

Short Courses. Omit the derivation of the Laplacian in cylindrical and spherical coordinates

## SOLUTIONS TO PROBLEM SET 11.11, page 641

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

= 1,An = 0 (n &gt; 1) Answer: u =rcos % Of course; this is at once seen by inspection:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

20. Set P and consider u(p; 0, %) = rv(r, 0, %) By differentiation;

Thus

<!-- formula-not-decoded -->

By substituting this and uøø by we obtain the result. ru ø4' ing

24. TEAM PROJECT. (a) The two drops over a portion of the cable of length Ax are Ur' Divide by Ax and let Ax = 0.
22. = cos 0 sin 0 = + y2)2 r2
3. (c) To get the first equation; differentiate the first transmission line equation with respect to x and use the second equation to replace iz and izt:

<!-- formula-not-decoded -->

Now collect terms. Similarly for the second equation.

- (d) Set 2 Then ut RC

<!-- formula-not-decoded -->

- (e)

## SECTION 11.12. Solution by Laplace Transforms, page 643

Purpose. For students familiar with Chap. 5 we show that the Laplace transform also applies to certain partial differential equations; where the subsidiary equation must be exto be an ordinary differential equation. pected

Short Courses. This section can be omitted.

## SOLUTIONS TO PROBLEM SET 11.12, page 646

2. Use c = Tlp.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(where u(t x2) is the unit step fuction) as obtained from

<!-- formula-not-decoded -->

with c(s) = -Ils2 as obtained from u(0, t) = 1, U(O, s) =

6. u = f(x)g(t) xf' g + fg = xt, hence

<!-- formula-not-decoded -->

To complete the separation; we take f(x) obtaining

<!-- formula-not-decoded -->

hence

<!-- formula-not-decoded -->

= 0. Also, u(x; 0) = x(c 1). Thus c 1 and the answer is, as before;

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

From this and formula 39 in Sec. 5.9 we get, as asserted,

<!-- formula-not-decoded -->

Ils, and since w(x; 0) = 0,

W(x, s)

=

F(s)sWo(x, s)

F(s)[sWo(x, s)

Now apply the convolution theorem.

<!-- formula-not-decoded -->

## SOLUTIONS TO CHAPTER 11 REVIEW, page 647

<!-- formula-not-decoded -->

w(x; 0)]

8. From W =

Chapter 11 Review. Equipotential lines in Prob. 42

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## PART D. COMPLEX ANALYSIS

## CHAPTER 12 Complex Numbers and Functions. Conformal Mapping

## Major Changes

The old chapter on conformal mapping has been absorbed into 12, beginning with a general introduction to conformality in Sec. 12.5, continuing with the conformal special section on linear fractional transformations (Sec. 12.9). This: gives a better understanding of those functions because we now discuss their geometric properties (their mapping properties) simultaneously with their analytic formulas, as we do it all the time in calculus . Chap.

## SECTION 12.1. Complex Numbers. Complex Plane, page 652

Purpose. To discuss the algebraic operations for complex numbers and the representa tion of complex numbers as in the plane. points

## Main Content; Important Concepts

Complex number, real part, imaginary part, imaginary unit

The four algebraic operations in complex

Complex plane, real axis, imaginary axis

Complex conjugates

## Two Suggestions on Content

1. Of course; at the expense of a small conceptual concession, one can also start immediately from (4), (5),

<!-- formula-not-decoded -->

2. If students have some knowledge of complex numbers, the practical division rule (7) and perhaps (8) and (9) may be the only items to be recalled in this section. (But I personally would do ten minutes more in any case.)

and go on from there.

## SOLUTIONS TO PROBLEM SET 12.1, page 656

<!-- formula-not-decoded -->

173

20. Z1z2 0 if and only if

24. +(1 + i)
26. 4(2 + i) +(1 = 2i) is obtained by taking the square root of each of the two solutions in Prob. 25.
28. (18) in Team Project 20, we obtain Using

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

system of equations in the 'unknowns X1 and y1, which therefore must be zero; hence Z1 = 0

## SECTION 12.2 Polar Form of Complex Numbers. Powers and Roots, page 657

Purpose. To give the student a firm grasp of the polar form; including the principal value z, and its application in multiplication and division. Arg

## Main Content, Important Concepts

Absolute value |z/, argument 0, principal value 0 Arg

Triangle inequality

Multiplication and division in polar form nth root; nth roots of unity (16)

## SOLUTIONS TO PROBLEM SET 12.2, page 662

2. V8(cos :" + i sin 6. ~isin 10. V37/8 (cos 2.19105 ~ i sin 2.19105) 12. T, -3.0419 14. 3714 16. 18. 3 + V27i

20. TEAM PROJECT. (a) Use (15).
2. () Use those formulas (10) in the form

<!-- formula-not-decoded -->

use finally choose the sign of Im Vz in such a way that sign [(Re Vz)(m Vz] = sign y.

- i sin

30. Quadratic equation in z2 with solutions

<!-- formula-not-decoded -->

with the roots evaluated by (18). From this; by (18), we get the four solutions

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The name results from the fact that the equality relates the lengths of the sides and the diagonals of a parallelogram with sides determined by the vectors corresponding listed in Appendix 1.

## SECTION 12.3. Derivative. Analytic Function; page 663

Purpose. To define (complex) analytic functions the class of functions complex analy sis is concerned with and the concepts needed for that definition; in particular, derivatives.

This is preceded by a collection of a few standard concepts on sets in the complex plane that we shall need from time to time in the chapters on complex analysis:

## Main Content, Important Concepts

Unit circle; unit disk, open and closed disks

Domain; region

Complex function

Limit; continuity

Derivative

Analytic function

## Comment on Content

The most important concept in this section is that of an analytic function. The other con cepts resemble those of real calculus. The most important new idea is connected with the limit: the approach in infinitely many possible directions: This yields the negative result in Example 4 and\_much more importantly\_the Cauchy-Riemann equations in the next section.

## SOLUTIONS TO PROBLEM SET 12.3, page 668

2. Annulus with center 4 2i bounded by the circles of radius &lt; and 2
6. We obtain
3. 4 Disk without its center 1 + i, radius V2. Such domains will be crucial in connection with residue integration in 15. Chap.

<!-- formula-not-decoded -->

the exterior of the circle of radius \_ with center at 2

8. Angular region ~4T arg z &lt; 4"

<!-- formula-not-decoded -->

16. (rcos 0 = (cos 0

<!-- formula-not-decoded -->

24. TEAM PROJECT. (a) Use Re f(z) = [f(z) + f@]/2, Im f(z) = [f(z) f@]/2i.
2. = 0 such that

<!-- formula-not-decoded -->

- &lt; ô for all sufficiently n since lim zn = 4. Thus e for these n. large
- The is as in calculus. We write proof

<!-- formula-not-decoded -->

Then from the definition of a limit it follows that for any given € there is a 8 &gt; 0 such that |nl € when |z Zol ô. From this and the triangle inequality,

<!-- formula-not-decoded -->

which approaches 0 as |z = zl ~ 0.

- (e) no limit as Az -&gt; 0.

<!-- formula-not-decoded -->

When 2 0 the   expression on the   right   approaches zero as Az 0 When z # 0 and Az = Ax; then Az Ax and that expression approaches z + 7. When z # 0 and Az = iAy, then Az ~iAy and that expression approaches + Z. This proves the statement.

## SECTION 12.4. Cauchy-Riemann Equations. Laplace's Equation; page 669

To derive and explain the most important   equations in Cauchy\_Riemann equations; which constitute the basic criterion for analyticity.

## Main Content, Important Concepts

Cauchy-Riemann equations (1)

These equations as criterion for analyticity (Theorems 1 and 2)

Derivative in terms of partial derivatives; (4), (5)

Relation of analytic functions to Laplace's equation

Harmonic function; conjugate harmonic

## Comment on Content

(4), (5), and Example 3 will be needed occasionally .

The relation to Laplace's equation is basic; as mentioned in the text

## SOLUTIONS TO PROBLEM SET 12.4, page 673

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- () Same idea as in (a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

28. a = 2, ~sin 2x sinh 2y

<!-- formula-not-decoded -->

30. Students should observe the orthogonality of the two families, which will be discussed in the next section; as a consequence of conformality .

## SECTION 12.5. Geometry of Analytic Functions: Conformal Mapping, page 674

Purpose. To show conformality (preservation of angles in size and sense) of the mapping by an analytic function w = f(z); exceptional are Z at which f' (z) = 0 points

## Main Content, Important Concepts

Concept of mapping

Complex functions as mappings

Definition of conformality

Critical point

Conformality (Theorem 1)

## Comment on the Proof

The crucial point is to show that w f(z) rotates all straight lines (hence all tangents) passing through a point z through the same angle œ arg f' (zo), but this follows from (3) by taking arguments. This in a nutshell is the proof, once the stage has been set.

## Comment on Purpose of Section

Apart from applications, this discussion of geometric aspects of analytic functions should help the student a better understanding of complex functions. In a sense it is a counterpart of discussions of functions in terms of curves in calculus . gain

## SOLUTIONS TO PROBLEM SET 12.5, page 678

<!-- formula-not-decoded -->

6. The half-plane v &lt;0 lower
8. From the last formula in Example 1 with k = 1 we have for y = k = 1 the image

<!-- formula-not-decoded -->

parabola opening to the right. For the boundary y =0 we get v2 = 0. The x-axis is 'folded up' at 0, where angles are doubled, and is mapped onto the nonnegative ray of the u-axis\_

<!-- formula-not-decoded -->

This implies (u circle.

12. w = 2(z3 \_ a) - 322 = 0 gives z =
16. Ellipse z(t) = 3 cos t + i sint Advise students that other solutions are possible.
14. = 1)? after simplification. Hence z = 0.
18. z(t) =t+ ikt2

<!-- formula-not-decoded -->

20. CAS PROJECT. Orthogonality is a consequence of conformality because in the wplane; const and const are orthogonal.   (a) 6x2y2 + y4, = 4x3y = + (c) u ~ylr?

## SECTION 12.6. Exponential Function; page 679

Purpose. Sections 12.6-12.8 are devoted to the most important elementary functions in complex, which generalize the corresponding real functions, and we emphasize proper ties that are not apparent in real.

We also discuss the basic mapping properties of these functions. This is important for practical reasons (in connection with potential theoretic applications) as well as for crea better understanding of the nature of these complex special functions. It is the anaof what we do all the time in calculus when we discuss real functions in terms of their graphs in the xy-plane. ating log

## Basic Properties of the Exponential Function

Derivative and functional relation as in real

Euler formula, form of z polar

Periodicity with 2mi, fundamental region

# 0 for all z

Conformality of the mapping w = e? for all z

## SOLUTIONS TO PROBLEM SET 12.6, page 682

2. e(cos 1 + i sin 1) ~ 1.47 + 2.29i,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

14. z = In5 + (arc tan : + 2nn)i
2. the negative real axis along
18. Whole w-plane except w = 0
4. = 0, sin y = 0. Answer: On the horizontal lines y n = 0, 1, (ii) ~ isin y) e'(cos y + i siny) sin y
20. TEAM PROJECT: (a) el/z is analytic for all z # 0. e7 is not analytic for any z The last function is analytic if and only if k
6. (d) f' = By integration;

<!-- formula-not-decoded -->

By the first Cauchy-Riemann equation;

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Differentiating the last equation with respect to y, we get

<!-- formula-not-decoded -->

Now for y = 0 we must have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Also; b = c{(0) = ~C2(0) = 0. Together c1(y) = cos y. From this,

<!-- formula-not-decoded -->

This gives f(z) = e (cos y + i sin y)

Purpose. Discussion of basic properties (including mapping properties) of trigonometric and hyperbolic functions; with emphasis on the relations between these two classes of functions as well as between them and the exponential function; here we see on an elementary level that investigation of special functions in complex can add substantially to their understanding.

## SOLUTIONS TO PROBLEM SET 12.7, page 686

2. The right side is

cosh Z1 cosh Z2 + sinh z1 sinh z2

<!-- formula-not-decoded -->

If we multiply out, then because of the minus signs the products ez1e cancel in pairs. There remains, as asserted, 712

<!-- formula-not-decoded -->

Similarly for the other formula.

4. cos 1 cosh 1 ~isin 1 sinh 1 = 0.8337 0.9889i
6. isinh " ~ 11.5487i (same as Prob. 5)
8. cos 5 sinh 4 + i cosh 4 sin 5 = 7.7411 26.1865i
10. cosh z = 0, cosh x cos y = 0 = 0, y = #(2n 4 = 0, sin y # 0 for those y, hence sinh x = 0, x 0. Answer: sin y

<!-- formula-not-decoded -->

12. sinxcoshy = 100O, cos x sinh y = ey/2 (y large), ey 2000, y ~ 7.600 902 (which agrees with the 6D value of the solution of cosh y = 1000). Answer: z
14. The region in the U-axis and the   hyperbola 4u2 = 1 because for x = 0 formula (6b) reduces to

<!-- formula-not-decoded -->

Thus u = 0 (the v-axis) is the left boundary of that region. For x Tl6 we obtain thus

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and we obtain the right boundary curve of that region from as asserted.

<!-- formula-not-decoded -->

16. The region in the upper half-plane bounded by portions of the u-axis; the ellipse u?lcosh? 3 + v2Isinh? 3 = 1 and the hyperbola u2

<!-- formula-not-decoded -->

Indeed, for x =

and from this

<!-- formula-not-decoded -->

For y = 0 we = 0 (the u-axis). get

For y = 3 we get hence

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

18. The upper boundary maps onto the ellipse

<!-- formula-not-decoded -->

and the lower boundary onto the ellipse

<!-- formula-not-decoded -->

Since 0 2m, we get the entire ellipses as boundaries of the image of the given domain; which therefore is an elliptical &lt;x ring

Now the vertical boundaries x 0 and x 2m map onto the same segment

of the u-axis because for x = 0 and x 27 we have

<!-- formula-not-decoded -->

Answer: Elliptical annulus between those two ellipses and cut along that segment. See the figure.

Section 12.7. Problem 18

<!-- image -->

20. CAS PROJECT. This is an impressive demonstration of the relationships between the four functions. (a) and (b) reflect that are translations of one another by an odd multiple of ul2. More about the actual formula cos z = sin (z + 2") cannot be discovered from the plot. Similarly for (c) and (d), which are translates by multiples of in/2 (thus in the y-direction). (a) and (c) are rotations of one another through 909 . Similarly for (b) and (d). Hence (a) and are related by translations and rotations, and so are (b) and (c) they

## SECTION 12.8. Logarithm. General Power, page 687

Purpose. Discussion of the complex logarithm; which extends the real logarithm In x (defined for positive x) to an infinitely many-valued relation (3) defined for all z # 0; definition of general powers z ; mapping properties.

## Comment on Notation

In z is also denoted by x of base 10, the notation In is more practical; this notation is widely in mathematics. log used

Section 12.7. CAS Project 20

<!-- image -->

## SOLUTIONS TO PROBLEM SET 12.8, page 691

```
= Izleie = 2, In e? = In |ezl + =z + 2nni 6. In 20 _ i arc tan (4/3) = 2.9957 2.2143i = 2.302 635 + 3.131593 10. 1 + 2nai, n = 0, 1, 12. In4 + (2n + I)ai, n = 0, I, 14. In5 + (arc tan (3/4) + 2nu)i, n = 0, 1, 16. = e-2(cos g ~ ising) = 0.010 0.135i 15.154 2 e-"(cos (In 4) + i sin (In 4)) = 0.0079 + 0.0425i 22. In (1+i) exp [(1 = V2 e"l4(cos (4T 2.808 + 1.318i 24. ei In (1+3i) = e-arc tan 3 (cos (In V1o) + i sin (In V1o)) 0.1168 + 0.2619i e-2-3i/2 e?i(ln e(l-i)
```

<!-- formula-not-decoded -->

30. TEAM PROJECT. (a) W = g(eiw + e Multiply by 2eiw to a quadratic equation in eiw ~iw) get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) Similarly,

Now take logarithms, etc\_

- (c) cosh w = 2zew + 1 = 0, =z + Vz2 1. Take logarithms. ew
- (d). z sinh w = e-w), 2zew = 1, ew = z + Vz2 + 1. Take e2w loga -

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- This is similar to (e)

## SECTION 12.9. Linear Fractional Transformations. Optional, page 692

Purpose. Introduction to this large class of conformal mappings; also called Möbius transformations. These transformations form a group, have various general properties in commore important role in advanced complex analysis than it does in our investigations.

## Main Content, Important Concepts

Linear fractional transformations; special cases

Extended complex plane, at infinity point

Fixed points

Construction of linear fractional transformations

Mappings

Short Courses. This section may be omitted.

the given formula get

## SOLUTIONS TO PROBLEM SET 12.9, page 698

2. The inverse is

<!-- formula-not-decoded -->

numerator is 2u. This gives Re z = x in the form

<!-- formula-not-decoded -->

This yields the circles as claimed.

- = (2w I)/(-w + 1) The equation for the fixed points of w = f(z) is

with solutions

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

From the inverse we get the same equation with w instead of z. Of course; this is not surprising; a fixed of the mapping must be a fixed of the inverse. point point

6. TEAM PROJECT. (a) This follows by direct calculation and simplification.
2. (b) One can combine the cases of a straight line and a circle by writing (A =0 a straight line, A # 0 a circle)

<!-- formula-not-decoded -->

One can simplify the further work by writing this in terms of z and 7, a device that has other applications; too:

<!-- formula-not-decoded -->

W = lz gives z = llw. Substitution of this and multiplication by ww gives

<!-- formula-not-decoded -->

Or, in terms of u and v,

<!-- formula-not-decoded -->

- (c) This follows by direct calculation.
- If set we

<!-- formula-not-decoded -->

then we have w = W4 + alc from (c)

<!-- formula-not-decoded -->

The statement to be proved is tivial for a translation or a rotation; fairly obvious for a uniform expansion or contraction; and true for an inversion; as proved in () Hence the statement is true for any LFT (1) because of (c)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

must come out real for all real x Hence the four coefficients must be real, except possibly for a common complex factor.

18. cz2 0 (c # 0) has those fixed points as solutions; and by comparing this with (5) we see that we must have

and get the answer

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SECTION 12.10. Riemann Surfaces. Optional, page 699

Purpose: To introduce the idea and some of the simplest examples of Riemann surfaces, on which multivalued relations become single-valued, that is, functions in the usual sense.

Short Courses. This section may be omitted.

## SOLUTIONS TO PROBLEM SET 12.10, page 700

4. For w = Vz the Riemann surface has 4 sheets. To them correspond in the the four angular regions of angle 90' each and bounded by the two bisecting lines of the four quadrants; z = 0 is a branch point. If z moves 4 times around the origin and back to its original position; then w completes motion once around the origin. w-plane
2. 6.

Similarly for w where we need 5 sheets and z 0 is a branch vz, point.

<!-- formula-not-decoded -->

If we move from A in the first sheet (see the figure) we get into the second sheet at B (dashed curve) and get back to A after two loops around the branch point 1

Similarly for a around 2 (without encircling I); this curve is not shown in the figure. loop

Section 12.10. Problem 6

<!-- image -->

16. The requirement is that

10.

## SOLUTIONS TO CHAPTER 12 REVIEW, page 701

<!-- formula-not-decoded -->

44. e &lt; |wl &lt; e2 in the second quadrant

<!-- formula-not-decoded -->

50. c2z = (a - d)z = b = c(z + i)(z = i) = c(z? + 1) by the equation for the fixed points. comparing powers of z we have a - d = 0, b = ~c. Hence By

<!-- formula-not-decoded -->

If we move from C and back to C as shown, we do not cross the cut, we in the same sheet; and we increase 01 and 02 by 2m each. Hence (01 + 02)/2 is increased by and we have completed one in the w-plane. This makes it plausible that two sheets will be sufficient for the present w and that the cut along which the two sheets are joined crosswise is properly chosen: stay 27, loop

- 8 pass a single cut, we into the other sheet. If a crosses two cuts, it is back in the sheet in which it started. The figure shows one (A) that encircles two branch points and stays entirely in one sheet. The from B and back to B also encloses two branch points, and since it crosses two cuts; part of it is in one sheet and part of it is in the other. get path path path

A discussion in terms of coordinates as in Prob. 6 would be similar to the ous one. Various other can be drawn and discussed in the figure. previ paths

Section 12.10. Problem 8

<!-- image -->

## CHAPTER 13 Complex Integration

## Change

We now discuss the two main integration methods (indefinite integration and integration by the use of the representation of the path) directly after the definition of the integral, postponing the proof of the first of these methods until Cauchy' s integral formula is available in Sec. 13.2. This compactification of the material seems desirable from a practical of view. point

## Comment

The introduction to the chapter mentions two reasons for the importance of complex integration: Another practical reason is the extensive use of complex integral representa tions in the higher theory of special functions; see Ref:. [11] listed in Appendix 1.

## SECTION 13.1. Line Integral in the Complex Plane, page 704

Purpose; To discuss the definition; existence; and general properties of complex line integrals. Complex integration is rich in methods; some of them very elegant. In this section we discuss the first two methods, integration by the use of and (under suitable assumptions given in Theorem 1!) by indefinite integration. path

## Main Content, Important Concepts

Definition of the complex line integral

Existence

Basic properties

Indefinite integration (Theorem 1)

Integration by the use of (Theorem 2) path

Integral of Ilz around the unit circle (basicl)

ML-inequality (13) (needed often in our work)

## Comment on Content

tegral theorem. We discuss this method here for two reasons: (i) to get going a little faster and, more importantly, (ii) to answer the students" natural question suggested by calcuthat is, whether the method works and under what condition that it does not work unconditionally can be seen from Example 7! lus,

## SOLUTIONS TO PROBLEM SET 13.1, page 711

<!-- formula-not-decoded -->

4. 3 cos t + 2i sin t (0 = t = 2m). Here (and elsewhere) one should emphasize the vantage of parametric representations, that one the entire curve, whereas y = y(x) would give only the upper half (or the lower half), and y' (x) ~ adgets

8. 2 cosh t +
10. semicircle (radius V3, center 5i) Upper

14. Hyperbola xy = 4 from 1 4 4i to 4 + i

<!-- formula-not-decoded -->

26.

28. L = bound is much larger than the actual value.
2. (c) 2ai. The integral of z equals 372. The inteof Re z2 equals 7313 Ta2/2 gral
30. TEAM PROJECT. (b) (i) 128i, (ii) {(e2+4i 1)
4. (d) The integrals of the four functions in (c) have for tbe present the values 2)i/3, and ~2i/3, respectively . paths

Parts (c) and (d) may also help to motivate our further discussions on independence and the principle of deformation of path. path

## SECTION 13.2. Cauchy's Integral Theorem, page 713

integral  theorem, which is basic by itself and has various  basic consequences to be discussed in the remaining sections of the chapter.

<!-- formula-not-decoded -->

20. Re z2 = 42

<!-- formula-not-decoded -->

- (3) Down; z(t) = 1 + it; t goes from 1 to 0, 2(t) + 3)
2. Answer:
22. By Theorem 1, the integral gives

<!-- formula-not-decoded -->

24. By Theorem 1 the integral gives

<!-- formula-not-decoded -->

because of (7) in Sec. 12.6.

## Main Content; Important Concepts

Simply connected domain

Cauchy' s integral theorem; Cauchy' s proof

(Goursat' s proof in Appendix 4)

Independence of path

Principle of deformation of path

Existence of indefinite integral

Extension of Cauchy' s theorem to multiply connected domains

## SOLUTIONS TO PROBLEM SET 13.2, page 720

- Yes. (b) since we would have to move the contour across +2i where I/(z? + 4) is not analytic. No,
4. (a) z = 0 outside C, () z =0
6. No; because of the principle of deformation of path.
8. 0, yes
- 1 10. TZ 1 Answer: 2mi = 2i by the deformation principle and (6). No T

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- 2z + 3i 2 16. TEAM PROJECT. (b) (i) From this, the 2 il2 z + i/2 ple of deformation of path, and (6) obtain the answer princi we

<!-- formula-not-decoded -->

Now z = ~2 lies outside the unit circle. Hence the answer is g Ti.

- (c) The integral of z Im z z2, Re z2, Im z2 equals 1/2, al6, 1/3, 1/3 a2/30 ial6, al6 ia?/30, respectively: Note that the integral of Re 22 plus i times the inteof Im 2? must equal 1/3. Of course; the student should feel free to experiment with any functions whatsoever. gral
18. 0 by Cauchy' s theorem because = 1 and the portion x &gt; 1 of the real axis lie outside the contour .

<!-- formula-not-decoded -->

- (ii) Similarly,

- 2z = 1 22. = 4 Z(z = 1) 2 1 lie inside C.
24. 0 because the points +4nmi, at which sinh z = 0, lie all outside the contour of inte gration; s0 that Cauchy' s integral theorem applies.

## SECTION 13.3. Cauchy's Integral Formula, page 721

Purpose. To prove, discuss, and apply Cauchy' s integral formula; the second major consequence of Cauchy' s integral theorem (the first being the justification of indefinite integration).

## Comment on Examples

The student has to find out how to write the integrand as a product f(z) times 1/(z Zo), and the examples (particularly Example 3) and problems are designed to give help in that technique.

## SOLUTIONS TO PROBLEM SET 13.3, page 724

- il4 =
- 4 The ellipse 4x2 + y?/4 = 1 includes the singularities at ~1 and 1 in the interior; whereas ti lie outside. If we write the integrand

<!-- formula-not-decoded -->

we can apply Cauchy' s integral formula to each of the two terms on the right and get 4 4 =0

6. The integrand is

By Cauchy' s formula,

<!-- formula-not-decoded -->

8. The integrand is

<!-- formula-not-decoded -->

Hence Cauchy's formula gives

<!-- formula-not-decoded -->

10. TEAM PROJECT. (a) Eq. (2) is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

because the last integral is zero by Cauchy' s integral theorem. The result agrees with that in Example 2, except for a factor 2

- (b) (12) in Appendix A3.1, we obtain (2) in the form Using

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- As p in Fig. 343 approaches 0, the integrand approaches 0\_ 12. z = 2 lies outside the contour, s0 that we the solution get

<!-- formula-not-decoded -->

14. z = 0 lies inside the contour; the solutions of ez 2i = 0 lie outside because ez

<!-- formula-not-decoded -->

16. 4z2 8iz 2i) = 0 at z = 2i in the 'ring' in the figure and at z 0 not in the Hence

<!-- formula-not-decoded -->

Section 13.3. Problem 16

<!-- image -->

- = i lies inside the large circle; ~i and ~1 lie outside: The integral over |zl = 0.2 is zero by Cauchy' s theorem. Hence

<!-- formula-not-decoded -->

20. By Cauchy's integral theorem we can replace Cby two small circles C1 and C2 around 1 and ~1 and then apply (1)tó get

<!-- formula-not-decoded -->

## SECTION 13.4. Derivatives of Analytic Functions; page 725

Purpose. To discuss and apply the third major consequence of Cauchy' s integral formula; the theorem on the existence and form of the derivatives of an analytic function.

## Main Content

Formulas for the derivatives of an analytic function

Cauchy's inequality

Liouville' s theorem

Morera' s theorem (inverse of Cauchy's theorem)

## Comments òn Content

Technically the application of the formulas for derivatives in integration is practically the same as that in the last section.

The basic importance of (1) in giving the existence of all derivatives of an analytic function is emphasized in the text.

## SOLUTIONS TO PROBLEM SET 13.4, page 729

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

6. Differentiating three times, we obtain the answer

<!-- formula-not-decoded -->

8. The answer is obtained by 2n differentiations, which reproduces cos z times a factor (~1)n. Since cos 0 1, we obtain (~1)n2ail(2n)!
10. From (1) we obtain

<!-- formula-not-decoded -->

12. We have to differentiate twice, so that (1) gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

18. = 2 lies outside the contour, and (1) with n = 1 gives

<!-- formula-not-decoded -->

16. From (1) we obtain
2. theorem.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

From this the result follows. large

- (d) If f(z) # 0 for all z, then g = Ilf would be analytic for all z Hence by (a) there would be values of z exterior to every circle |z/ = R at which, say, Ig(z)l &gt; 1 and thus |f(z)l 1. This contradicts (b). Hence f(z) # 0 for all z cannot hold.
- (c) lezl &gt; M for real z = x with x &gt; R = In M. On the other hand, Jez| = 1 for any pure imaginary z = = 1 for any real y (Sec. 12.6)

## SOLUTIONS TO CHAPTER 13 REVIEW , page 730

- 16 64/35
18. The four   integrals   along the four   edges of   the   rectangle have the value =1 + cosh 1, + cosh 1. The sum is 0
20. 2 = 0 and z 2 both lie inside the contour. Hence we obtain ~2ri = ~4ti (clockwise integration!)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

28. z(t) =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## CHAPTER 14 Power Series Taylor Series

## Major Change

Laurent series have been moved to 15,a better place because of their use in residue integration. Chap.

## SECTION 14.1. Sequences, Series; Convergence Tests, page 732

Purpose. Since not too much changes in the transition from real to complex sequences and series, this section can almost be regarded as a review from calculus plus a presen tation of convergence tests for later use.

## Main Content; Important Concepts

Sequences, series; convergence; divergence

Comparison test (Theorem 5)

Ratio test (Theorem 8)

Root test (Theorem 10)

## SOLUTIONS TO PROBLEM SET 14.1, page 740

6. No, because Zn (cosh nu)In
2. 4 no, +l, +i Yes,
3. 8 Yes, yes; 0
10. Choose € &gt; 0 arbitrary; By the definition of convergence there exists N(e) such that * \_

<!-- formula-not-decoded -->

This proves the assertion.

12. Convergent; the sum e20+30i being
2. 1 14. Convergent since and converges\_ In? + i| n2 n2
16. This series converges by the ratio test because

<!-- formula-not-decoded -->

- ') and the harmonic series diverges
20. TEAMPROJECT. (a) By the generalized triangle inequality (6), Sec. 12.2, we have

<!-- formula-not-decoded -->

converges by assumption; the sum on the right becomes less than any given € &gt; 0 for every n greater than sufficiently N and p 1, 2, by Cauchy' s convergence principle. Hence the same is true for the left side, which proves convergence of z1 + z2 + by the same theorem. large

- (c) The form of the estimate of Rn suggests we use the fact that the ratio test is comparison test based on the geometric series. This gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) For this series we obtain the test ratio

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

from this with 9 = 1/2 we have

<!-- formula-not-decoded -->

Hence n = 5 (by computation), and

<!-- formula-not-decoded -->

Exact to 6 digits is 1 + 0.693147i.

## SECTION 14.2. Power Series, page 741

Purpose; To discuss the convergence behavior of power series; which is basic to our further work (and which is simpler than that of series arbitrary complex functions as terms) . having

## Proof of the Assertions in Example 6

<!-- formula-not-decoded -->

and divergence for every z # z by Theorem 9, Sec. 14.1.

Now, by the definition of a limit point, for a given we have for infinitely many n

hence for all z # zo and those n,

R = take K zol to get

<!-- formula-not-decoded -->

The right inequality holds even for all n &gt; N (N sufficiently large), by the definition of a greatest limit point:.

Let ñ 0 Since 2 0, we then have convergence to 0. Fix any z = Z1 # Zo: Then for € 1/(2/z1 zol) &gt; 0 there is an N such that € for all n &gt; N, hence

<!-- formula-not-decoded -->

and convergence for all z1 follows by the comparison test.

We establish lÎx as the radius of convergence of (1) by proving

Let Iz zol Then, say, Iz = b &lt; 1. With this and € = bl2/z Zol &gt; 0 in (*), for all n &gt; N,

<!-- formula-not-decoded -->

Convergence now follows from Theorem 9, Sec. 14.1.

Let Iz zolñ =1+ c &gt; 1. With this and € = cI(2/z = zol) &gt; 0 in (*) for infinitely many n,

<!-- formula-not-decoded -->

and divergence follows.

## SOLUTIONS TO PROBLEM SET 14.2, page 745

<!-- formula-not-decoded -->

10. ~1,4 (the reciprocal of R in Example 5 of the text)

12. The quotient in (6) is

<!-- formula-not-decoded -->

Hence the answer is 3i, Ile.

14. 0, 0

16. 0, V2 (not 2; see Team Project 20)

18. 0, 1/6
2. compared to Janl, and the larger |anlan+1l R becomes.
3. (b) (i) Nothing: (ii) This multiplies R by llk. (iii) The new series has radius of con-
4. In Example 6 we took the first term of one series; then the first term of the other, etc. We could have taken; for instance the first three terms of one series; then the first five terms of the other, then three terms and five terms, etc Or we could have mixed three or more series term by term. again

<!-- formula-not-decoded -->

## SECTION 14.3. Functions Given by Power Series, page 746

## Main Content

Purpose; To show what operations on power series are mathematically justified and to prove the basic fact that power series represent analytic functions.

Termwise addition; subtraction; and multiplication of power series

Termwise differentiation and integration (Theorems 3, 4)

Analytic functions and derivatives (Theorem 5)

## Comment on Content

That a power series is the Taylor series of its sum will be shown in the next section.

## SOLUTIONS TO PROBLEM SET 14.3, page 750

2. Set f =

4. 1

- 6 consists of the fixed k'; which has no effect on k! R, and factors n(n

<!-- formula-not-decoded -->

- n(n -

1) = T, the answer is T.

8. VsI3. The root appears because of z2n = (z2".
10. 0 Tbis is (36) in Appendix A3.1, except for a constant factor;, and with z instead of x
3. 12 1/4 because Il(n + 1) results from integration; and for the series without this factor in the coefficients we have in (6), Sec. 14.2,

<!-- formula-not-decoded -->

14. 0 because 3n(3n 1) results from differentiation; and for the coefficients without these factors we have in (6), Sec. 14.2,

<!-- formula-not-decoded -->

16. Tbis is a useful formula for binomial coefficients. It follows from.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

by equating the coefficients of z" on both sides. To get z"zm = z" on the left; we must have n m =r thus m =r n;, and this gives the formula in the problem.

18. The even-numbered coefficients are zero because f(-z) = ~f(z) implies

<!-- formula-not-decoded -->

## 20. TEAM PROJECT. (a) The list is

<!-- formula-not-decoded -->

In the recursion; an is the number of pairs of rabbits present and an-1 is the number of pairs of offspring from the of rabbits present at the end of the preceding month. pairs

- (b) the hint; we calculate Using

<!-- formula-not-decoded -->

where = 0, and Theorem 2 gives = 1, a1 = 0, an-2 = 0for n = 2,3, The converse follows from the unique ness of a power series representation (see Theorem 2) @n

## SECTION 14.4. Taylor Series and Maclaurin Series, page 751

Purpose. To derive and Taylor series, which include those for real functions known from calculus as cases. explain special

## Main Content

Taylor series (1), integral formula (2) for the coefficients

Singularity, radius of convergence

Maclaurin series for e2

Theorem 2 connecting Taylor series to the last section

## Comment

The series just mentioned, with z = x; are familiar from calculus .

## SOLUTIONS TO PROBLEM SET 14.4, page 757

<!-- formula-not-decoded -->

## The series is

<!-- formula-not-decoded -->

It can be obtained in several ways: (a) Integrate the Maclaurin series of the integrand termwise and form the Cauchy product with the series of (b) f satisfies the differential equation f = 2zf + 1 Use this, its derivatives f = 2(f + zf' ), f(O) = 0, f' (0) = 1, etc., and the coefficient formulas in (1). (c) Substitute etc.,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

14. First of all, since sin (w + 2m) = sin w and sin (a w) = sin w, we obtain all values of sin w by w vary in a suitable vertical strip of width n, for in example; letting

and

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

we have to exclude a part of the boundary of that strip, 80 we exclude the boundary in the lower half-plane. To solve our problem we have to show that the value of the series lies in that strip. This follows from |zl 1 and

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

26. We obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) For y # 0 the series

<!-- formula-not-decoded -->

has positive terms; hence its sum cannot be 0.

## SECTION 14.5. Uniform Convergence. Optional, page 759

Purpose. To explain uniform convergence and its application to power series (Theorem 1) To explain the two main reasons for the importance of uniform convergence (Theorems 2 and 3).

## SOLUTIONS TO PROBLEM SET 14.5, page 766

4. = and 2 converges. Use the Weierstrass M-test. Izl?n + 2-n
10. R = %; uniform convergence on any bounded set.
14. TEAM PROJECT. (a) Convergence follows from the comparison test (Sec. 14.1) Let Rn(z) and Rn be the remainders of (1) and (5), respectively . Since (5) converges, for given € &gt; 0 we can find an N(e) such that Rn* &lt; for all n &gt; N(e). Since Ifm(z)l = Mm for all z in the region G, we also have JRn(z) &lt; Rn* and therefore e for all n &gt; N(e) and all z in the region G. This proves that the conver gence of (1) in G is uniform
12. |tanh n2| = 1. Convergence for 1/6. Uniform convergence for Iz = 1/V6
5. (b) Since fo + fí + converges uniformly, we may integrate term by term, and the resulting series has the sum F(z)  the integral of the sum of that series. Therefore; the latter sum must be F' (z).
6. (c) The converse is not true.
7. (d) Noting that this is a geometric series in powers of 9 = (1 + 22-1, we have lemniscate. The series converges also at z = 0
8. (e) We obtain

<!-- formula-not-decoded -->

- = 1 + z

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

nTx because sin = 1 and the exponential function decreases in a monotone fashL ion as t increases. From this,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Weierstrass test it follows that converges uniformly and, by Theorem 4, has the sum 9u etc. dt dun

## SOLUTIONS TO CHAPTER 14 REVIEW, page 767

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

the distance of 3 + 4i from z = 0: R = 3

<!-- formula-not-decoded -->

32. 1 = ily obtainable from Taylor' s theorem.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- V1ooo &gt; |31 numbers serving the same purpose are 5 + 4i and 6 + 2i; then |5 + 4i/ = V41 &gt; J6 + 2i| = V40.
40. R = 0, the series converges only at the center z ~1,s0 that uniformity of conver gence loses its meaning.

## CHAPTER 15 Laurent Series; Residue Integration

## Major Change

Laurent series, formerly in the previous chapter, have now been placed into this because of their main application; which is residue integration chapter,

Applications to real integrals has been' shortened because their practical importance seems to have decreased.

## SECTION 15.1. Laurent Series, page 770

Purpose; Next in importance after power series are Laurent series, converging in an annulus; and we explain here their theory and technique of application.

## Comment on Content

The Laurent series of a given function in a given annulus is unique; this is essential in view of our various methods and tricks of derivation: Because of our later work (residue integration!) two facts should be emphasized: (i) a function may have different Laurent series in different annuli with the same center; and (ii) the series converging in an immediate neighborhood of a singularity (except at the singularity itself) is of particular interest because it will give the residue (defined as the coefficient of the term of the power llz)

## SOLUTIONS TO PROBLEM SET 15.1, page 775

<!-- formula-not-decoded -->

- 4 the sum formula for the geometric series, we obtain the answer Using

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

8. the sum formula for the geometric series, we obtain Using

<!-- formula-not-decoded -->

10. The function is the same as in Prob. 8, but we now have the center z0 1. (In Prob. 8 the center was 0.) We obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

14. sin z cos (z \_ 4")) This gives the answer

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

18. The answer is the Laurent series, which is the sum of the two series

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

20. The answer is the Taylor series that is the sum of the two series

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

(z and integrate along a circle with center at zo in the interior of the annulus. Since the series converge uniformly, we may integrate term by term. This yields = Ck for all k = 0, +l,

- hence at z = which accumulate at 0.-
- (c) These series are obtained by termwise integration of the integrand. The second function is Si(z)/z3 , where Si(z) is the sine integral [see (40) in Appendix A3.1]. Answer:

<!-- formula-not-decoded -->

## SECTION 15.2. Singularities and Zeros. Infinity, page 776

Purpose. Singularities just appeared in connection with the convergence of Taylor and Laurent series in the last sections; and since we now have the instrument for their classi fication and discussion (i.e , Laurent series) this seems the right time for s0. We also consider zeros, whose discussion is somewhat related. doing

## Main Content, Important Concepts

Principal part of a Laurent series convergent near a singularity

Pole; behavior (Theorem 1)

Isolated essential singularity, behavior (Theorem 2)

Zeros are isolated (Theorem 3)

Relation between and zeros (Theorem 4) poles

Point % extended complex plane; behavior at %

Riemann number sphere

## SOLUTIONS TO PROBLEM SET 15.2, page 780

2. +l, +i; fourth order

<!-- formula-not-decoded -->

- 6 = 0, 1, tenth order
- 8 TEAM PROJECT. (a) f(z) = (z - Zo)"g(z) gives

<!-- formula-not-decoded -->

which implies the assertion because g(zo) # 0.

- = (z z0) ~"h(z), where h(z) = I/g(z) is analytic at z0 because g(zo) # 0.
- (c) f(z) ~ k = 0 at those points. Apply Theorem 3
10. +l, +3, 45, (simple poles); % (essential singularity)
- (d) f1(z) = f2(z) is analytic in D and zero at each Hence its zeros are not isolated because that sequence converges. Thus it must be constant since otherwise it would contradict Theorem 3. And that constant must be zero because it is zero at those points. Thus f1(z) and f2(z) are identical in D.
12. 0 (essential singularity)
16. ~i (essential singularity)
- 14 cosh [w2/(1 + is analytic at w 0. Hence the given function is analytic at %
18. Tl4 + nT (simple poles). These are the points where the sine and cosine curves intersect. They have a different tangent there, hence their difference cos z not have a zero derivative at those points; accordingly, those zeros are simple and give simple poles of the given function. To make sure that no further zeros of sin z exist; one must calculate

<!-- formula-not-decoded -->

and by simplification;

<!-- formula-not-decoded -->

so that we get no further solutions beyond those found by inspecting those two curves.

<!-- formula-not-decoded -->

This motivates the proof.

To prove the theorem; let f(z) have a of mth order at some z = Zo. Then point\_ pole

<!-- formula-not-decoded -->

For given M &gt; 0, no matter how we can find a  &gt; 0 so small that large,

<!-- formula-not-decoded -->

for all |z

<!-- formula-not-decoded -->

Hence |f(z)l ~

## SECTION 15.3. Residue Integration Method, page 781

Purpose. To explain and apply this most elegant integration method.

## Main Content, Important Concepts

Formulas for the residues at poles

Residue theorem (several singularities inside the contour)

## Comment

The extension from the case of a single singularity to several singularities (residue theorem) is immediate.

## SOLUTIONS TO PROBLEM SET 15.3, page 786

2. 0 (at 0)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

14. Simple at +4. By (4) the residues are poles

<!-- formula-not-decoded -->

This gives the answer

16. Simple at ~1, 0, 1. Equation (4) gives (ez + z)/(322 1), hence 1)/2, ~1, (e + 1)/2, respectively. Answer: 2ui(cosh 1 1) poles (e-1
18. Simple at z = i/2 with residue pole

<!-- formula-not-decoded -->

Answer: T sin = -1.506.

20. sin 4z = 0 at 0, (outside C) This gives three simple poles at

<!-- formula-not-decoded -->

respectively, and by the residue theorem the answer

<!-- formula-not-decoded -->

## SECTION 15.4. Evaluation of Real Integrals, page 787

Purpose 1 To show that certain classes of real integrals over finite or infinite intervals of integration can also be evaluated by residue integration

Since residue integration requires a closed path, one must have methods for producing preceded by a translation and of scale if another interval is given (This is not shown in the text.) In the case of an infinite interval; we start from a finite one, close it by some curve in complex (here; a semicircle; Fig. 360), blow it up; and make assumptions on the integrand such that we can prove (once and for all) that the value of the integral over the complex curve added goes to zero change

## Comment on Content

- Purpose 2 Extension of the second of the two methods just mentioned to integrals of practical interest in connection with Fourier integral representations (Sec. 10.8) and to discuss the case of singularities on the real axis.

## SOLUTIONS TO PROBLEM SET 15.4, page 793

2. The denominator is

<!-- formula-not-decoded -->

Two simple poles; at z = 4/3 (outside the contour) and at z = 3/4 (inside). From this and d0 = dzliz we obtain the answer

<!-- formula-not-decoded -->

- 4 (2), we obtain for the integral Using

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The residue at the simple = 0 is I/(-1) = ~1 The\_two other poles are at Z1 = (~3 + V8)i inside the unit circle and z2 = (~3 V8)i outside the unit circle. From (3), Sec. 15.3, we obtain at z1 the residue pole

<!-- formula-not-decoded -->

Answer: 0

from \_" to T (set 0 gral

6. Using (2), we obtain for the integral

<!-- formula-not-decoded -->

The residue at the at i/3 is pole

8. The integral equals

<!-- formula-not-decoded -->

where Z1 = 1/4 (inside the unit circle) and z2 = 4 (outside) give simple The residue at z = 0 is = 2, and at z = 1l4 it is poles. 2/z122

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

10. Simple poles at z1 = (2 + = (-2 + 2i)/VZ in the upper half-plane (and at (+2 2i)/V2 in the lower half-plane)  From (4) in Sec. 15.3 we obtain the residues

<!-- formula-not-decoded -->

Answer: TI(8V2)

This gives the answer

<!-- formula-not-decoded -->

12. Third-order at z = i (and at z = ~iin the lower half-plane) with residue pole

<!-- formula-not-decoded -->

Answer: 2ui 6/(2i)5

14. Second-order at z1 =1 + 2i in the upper half-plane (and at z2 = 1 2i in the lower) with residue pole

<!-- formula-not-decoded -->

16. Simple poles at i and 3i in the upper half-plane (and at ~i and ~3i in the lower) with residues

Answer: 2"i(1/32i) = T/16.

<!-- formula-not-decoded -->

1/48i)

<!-- formula-not-decoded -->

20. Second-order poles at z1 = i and z2 = ~i (in the lower half-plane) . By (5), Sec. 15.3, we get the residue

<!-- formula-not-decoded -->

Multiplying the imaginary part ~3e-2/4 by ~2m gives the answer

<!-- formula-not-decoded -->

- 2iz = z(z 2i) shows that we have simple poles at 0 and 2i with residues [by (3), Sec. 15.3]

<!-- formula-not-decoded -->

The answer is

- residue

<!-- formula-not-decoded -->

24. z3 \_ 1 =0 has the solutions Z1 = 1, Z2 =-1 on the real axis, 73 = in the upper these four simple are poles

<!-- formula-not-decoded -->

s0 that (14) gives the answer

<!-- formula-not-decoded -->

26. TEAM PROJECT. () The integral of along C is zero. Writing it as the sum of four integrals over the four segments of C we have

<!-- formula-not-decoded -->

Let a ~&gt; œ. Then the terms having the factor e~a? approach zero. Taking the real part of the third integral, we thus obtain

<!-- formula-not-decoded -->

Answer:

- (c) Use the fact that the integrands are odd.

## SOLUTIONS TO CHAPTER 15 REVIEW, page 794

22. 6ui because C contains only the at z = 3 in its interior. pole
24. 9z = z(z + 3)(z 3) = 0 at z = ~3,0, 3 gives simple poles; all three inside c: |z =4 From (4), Sec. 15.3, we get the residues

<!-- formula-not-decoded -->

and similarly, at 0 the value 9/(-9) = ~1and at 3 the residue 54/18 3. Since all three poles lie inside C, by the residue theorem we have to take the sum of all three residues, which is zero. Answer: 0

26. Simple at z ~1/2, 1/2 with residues [by (4), Sec. 15.3] poles

<!-- formula-not-decoded -->

Answer: 2Ti 2

- = (4 exp z4)' so that indefinite integration (because of independence of path) gives, with (1 + i)4 = \_4,

<!-- formula-not-decoded -->

Answer: (e e-4)/4 0.6750. No:

30. From the Maclaurin series of sin z see that the residue is 0 for odd n and (~1)6n+2/2/(n 1)! for.n = 2, 4 Multiplication by 2ui gives the answer. we
32. Simple at 0, residue [by (4), Sec. 15.3] pole

<!-- formula-not-decoded -->

34. The integral equals

<!-- formula-not-decoded -->

36.

40. Poles at z1 = = -4 - iV3/2 (both simple) We need; (3) in Sec. 15.3, using

At the simple at z = 0 the residue is\_~1 (not counting the minus in front of the integral). At the simple at -3 + V8 (inside the unit circle) the residue is pole pole

Answer: 0.

<!-- formula-not-decoded -->

- at Z1 =il2 in the upper half-plane (and at ~il2 in the lower) with residue 1/(8z1) ~il4. Answer: 2ui(-il4) Tl2. pole

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where c answer

## CHAPTER 16 Complex Analysis Applied to Potential Theory

This seems perhaps the most important justification for teaching complex analysis to engineers, and it also provides for nice applications of conformal mapping:

## SECTION 16.1. Electrostatic Fields, page 799

Purpose. To show how complex analysis can be used to discuss and solve two-dimen sional electrostatic problems and to demonstrate the usefulness of complex potential; major concept in this chapter.

## SOLUTIONS TO PROBLEM SET 16.1, page 802

2. F(z) = 20z + 300
6. 1lO(ln r) /In 2 = 159 In r (with measured in cm)
8. @(r) = 20(In r) /ln 2 10, 4(3) 21.70 &gt; 20
10. because near a source line its effect is much stronger than that of the other source and for a single source line, the equipotential lines are exactly concentric circles. Yes, line,
12. $ = 110 5Oxy
16. CAS PROJECT. (a) x2 \_ y? = c,xy = k
14. Compare the formulas for cos-1 and cosh-1 in Team Project 30, Sec. 12.8, and note that v const in u + iv = represents ellipses.
8. (b) xy = c, x2 \_ y2 = k; the rotation caused by the multiplication by i leads to the interchange of the roles of the two families of curves
9. (d) Another interchange of the families; compared to (c), (y 1/2c)2 + x2 = 1l4c2, (x
10. 1/2c)2 + y? + y?) = k gives origin.

## SECTION 16.2. Use of Conformal Mapping, page 804

Purpose. To show how conformal mapping helps in solving potential problems by mapping given domains onto simpler ones or onto domains for which the solution of the lem (subject to the transformed boundary conditions) is known. prob -

## SOLUTIONS TO PROBLEM SET 16.2, page 807

2. Figure 315, Sec. 12.6, shows D (a semi-infinite horizontal strip) and D* (the upper half of the unit circular disk); and $ = 2e" cos sin y = 0 and y T, and sin 2y on the vertical boundary x = 0 of D. e22
4. @ = 2 sin x cos x cosh y sinh y = u sin 2x sinh 2y = and é sin 2x sinh 2 if y = 1

- obtaining from (2) with b = zo the conditions

hence

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

ro is real for positive c = u. Note that with increasing c the image (an annulus) becomes slimmer and slimmer .

<!-- formula-not-decoded -->

- this the assertion follows. (It also follows by setting x 0 and calculating |wl)
14. The function z = 22 maps the first quarter of |Zl = 1 onto the upper half of the unit mapped into the x-axis, where the potential is zero (Fig. 372a) From this the result follows. being

## SECTION 16.3. Heat Problems, page 808

Purpose. To show that previous examples and new ones can be interpreted as potential problems in time-independent heat flow.

## Comment on Interpretation Change

Boundary conditions of importance in one interpretation may be of no interest in another; this is about the only handicap in change of interpretation:

## SOLUTIONS TO PROBLEM SET 16.3, page 811

2. By inspection,

the real part of

4. 105(Arg z) /m

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

A systematic derivation is as follows. The boundary and boundary values suggest that T(x; y) is linear in x and y

<!-- formula-not-decoded -->

From the boundary conditions;

- (1) T(x; x 4) = ax + b(x 4) + c = -20,
- (2) T(x, x + 4) = ax + b(x + 4) + c = 40.

By addition;

<!-- formula-not-decoded -->

Since this is an identity in x, we must have a ~b and c 10. From this and (1),

<!-- formula-not-decoded -->

Hence b 7.5. This agrees with our result obtained by inspection:

6. The lines of heat flow are perpendicular to the isotherms; and heat flows from higher t0 lower temperatures; Accordingly, heat flows from the portion of higher temperature of the unit circle |zl = 1 to that kept at a lower temperature, the circular arcs that intersect the isotherms at right angles. along

Of course; as temperatures on the boundary we must choose values that are phys-

8. TEAMPROJECT. (a) wis a basic building block when we have jumps in the boundary values. To get it as the real part of an analytic function (a logarithm) we have to multiply the logarithm by ~i. Otherwise we just incorporate the real constants that appear in T(x, y) Answer: Arg

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

T = 0 if u &lt; -1

- (c) W = a = z2 . Hence Arg (w - a) Arg z2 = 2 z. Thus (a) gives Arg =

<!-- formula-not-decoded -->

and we see that T = T1 on the x-axis and T = T2 on the y-axis are the boundary data.

- z. This is quite similar to Example 3 because the smaller circular boundArg

Geometrically, the a in w = a + z2 is a translation; and z2 opens the quadrant up onto the upper half-plane, so that the result of (a) becomes applicable and gives the potential in the quadrant.

12. The answer is

<!-- formula-not-decoded -->

because w = z2 maps the first quadrant onto the upper half-plane with 1 1 and shows the transformed boundary conditions. The temperature is figure

<!-- formula-not-decoded -->

in agreement with Team Project 8(b) with To = 10.

14. (200 Arg

Section 16.3. Problem 12

<!-- image -->

## SECTION 16.4. Fluid Flow, page 812

Purpose. To give an introduction to complex analysis in potential problems of fluid flow. Important Concepts

= const

Velocity potential ÿ, equipotential lines @ const

Complex potential F = $ + iv

Velocity V = F'(z)

Circulation (6), vorticity; rotation (9)

Irrotational, incompressible

Flow around a cylinder (Example 2, Team Project 14)

## SOLUTIONS TO PROBLEM SET 16.4, page 817

2. F(z) = (1

The equipotential lines are

The velocity vector is

See the figure.

- gives the streamlines 2xy

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Sectlon 16.4. Problem 4

<!-- image -->

- 3xy? iy?) = ~3x2y + y? + ~ 3xy2) gives the streamlines i(x3

<!-- formula-not-decoded -->

This includes the three straight-line asymptotes x = 0 and y = +x/V3 (which make 609 angles with one another, dividing the plane into six angular regions of angle 60 each), and we could interpret the flow as a flow in such a This is similar to the case F(z) = z2, where we had four angular regions of 909 opening each (the four quadrants of the plane) and the streamlines were hyperbolas. In the present case the streamlines look similar but are "squeezed" a little so that each stays within its region; whose two boundary lines it has for asymptotes. region: they

The velocity vector is

<!-- formula-not-decoded -->

s0 that V2 = 0 on y =x and y = ~x. See the figure.

Section 16.4. Problem 6

<!-- image -->

8. This rotates the whole flow pattern about the origin through the angle œ.
12. W cosh-1 z implies
3. Ilr?) sin 20 = 0 if r = 1 (the cylinder wall) or 0 = 0, lar to that in Example 1. For smaller |z/ it is a flow in the first quadrant around a ter of |zl 1. Similarly in the other quadrants . quar -

<!-- formula-not-decoded -->

Along with an interchange of the roles of the z- and w-planes; this reduces the sent problem to the consideration of the sine function in Sec. 12.7 (compare with 316). Instead of (16), Sec. 12.7; we now have the hyperbolas Fig;

<!-- formula-not-decoded -->

where c is different from the zeros of sine and cosine; and as limiting cases; the y-axis and the two portions of the aperture.

14. TEAM PROJECT. () We have

<!-- formula-not-decoded -->

Hence the streamlines are circles

<!-- formula-not-decoded -->

The formula also shows the asserted increase of the potential

<!-- formula-not-decoded -->

if arg z is increased by 2T.

<!-- formula-not-decoded -->

has the consequence that the flow is directed radially inward toward the sink because the velocity vector Vis

<!-- formula-not-decoded -->

For instance; at z = a + i (above the sink),

<!-- formula-not-decoded -->

which is directed vertically downward, that is; in the direction of the sink at a. (e) The addition gives

<!-- formula-not-decoded -->

Hence the streamlines are

<!-- formula-not-decoded -->

In both flows that we have added, |zl = 1 is a streamline, hence the same is true for the flow obtained by the addition.

Depending on the magnitude of K, we may distinguish between three types of flow having either two or one or no stagnation points on the cylinder wall The speed is

<!-- formula-not-decoded -->

great distance from the cylinder the flow is nearly parallel and uniform: The stagnation points are the solutions of the equation V 0, that is,

<!-- formula-not-decoded -->

We obtain

<!-- formula-not-decoded -->

If K = 0 (no circulation), then z = +1, as in Example 2 As K increases from 0 to the stagnation points move from z = +1 up on the unit circle until unite at z i The value K = 4m corresponds to a double root of equation (A) If K&gt; the roots of (A) become imaginary, so that one of the stagnation lies on the imaginary axis in the field of flow while the other one lies inside the cylinder; thus losing its physical meaning. they 41, points

## SECTION 16.5. Poisson's Integral Formula, page 819

(5) over the boundary values; to derive from (5) a series that gives the potential and = Ris the Fourier series of the boundary values.

## Comment on Footnote 6

Poisson' s discovery (1812) that Laplace's equation holds only outside the masses (or charges) resulted in the Poisson equation (Sec. 11.1). The publication on the Poisson distribution (Sec. 22.7) appeared in 1837.

## SOLUTIONS TO PROBLEM SET 16.5, page 822

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Note that 0) is neither even nor odd, but @(1, 0) T is odd, so that we get sine series plus the constant term T. @(1,

<!-- formula-not-decoded -->

14. TEAM PROJECT. (a) r = 0 in (5) gives @(0) = @(R; œ) dœ. Note that
2. () V?u = 0, u + = 0, hence by separating 72 variables gh"

<!-- formula-not-decoded -->

Also,

<!-- formula-not-decoded -->

- By the Cauchy-Riemann equations,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) From the series for and % we obtain by addition

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

reie we have the power series Using

<!-- formula-not-decoded -->

## SECTION 16.6. General Properties of Harmonic Functions; page 822

Purpose. We derive general properties of analytic functions and from them correspond properties of harmonic functions. ing

## Main Content, Important Properties

Mean value of analytic functions over circles (Theorem 1)

Mean value of harmonic functions over circles, over disks (Theorem 2)

Maximum modulus theorem for analytic functions (Theorem 3)

Maximum principle for harmonic functions (Theorem 4)

Uniqueness theorem for the Dirichlet problem (Theorem 5)

## Comment on Notation

Recall that we introduced F to reserve f for conformal mappings (beginning in Sec. 16.2), and we continue to use F also in this last section of 16. Chap.

## SOLUTIONS TO PROBLEM SET 16.6, page 825

2. From (2) obtain we

as expected.

6. z = 1 + ei0, x = 1 + cos 0, y sin 0 gives

<!-- formula-not-decoded -->

8. x = 1 + cos grate over 0 from 0 to 2m, divide by 2m. This gives 2 = @(l, 1)

<!-- formula-not-decoded -->

10. TEAMPROJECT. (a) Polar coordinates show that |F(z)| = |zl?2 assumes its max imum at the boundary point 4 + 7i, namely, 65,but at no interior (ii) Use the fact that |ezl =e" is monotone. point.
2. (b) F(z) is not analytic.

<!-- formula-not-decoded -->

This shows that the maximum of |sin z/ is taken on the boundary of the disk at 1 + ir, r the radius of the disk, and equals

<!-- formula-not-decoded -->

- (d) The extension is simple. Since the interior D of C is simply connected, Theorem 3 applies. The maximum of |F(z)| is assumed on C, by Theorem 3, and if F(z) have its minimum on C, so that F(z) would be constant, contrary to our as -

The fact that |F(z)| = const implies F(z) const for any analytic function F(z) was shown in Example 3, Sec. 12.4

<!-- formula-not-decoded -->

- = = 1 only at y = 0, 2m, and (b, 0) and (b, 2") lie on the boundary .
14. $ = exp (x2 y?) cos image of (x1, Y1) = (1, 0); this is typical. (u1, U1) is found by noting that on the boundary (semicircle), @* = e" cos (V1 u2) increases monotone with u. Similarly for D. 2xy,

## SOLUTIONS TO CHAPTER 16 REVIEW, page 826

+ i)z

<!-- formula-not-decoded -->

center on y = x

20. $ exp (x2 y2) sin 2xy
22. Isotherms are the rays const. Heat flows along circular arcs from the higher to the lower temperature.
3. 24.43.22 C, which is obtained as follows. We have

and at the outer cylinder;

<!-- formula-not-decoded -->

- T(10)

<!-- formula-not-decoded -->

and from the condition to be achieved

<!-- formula-not-decoded -->

- 1) subtracted from (2) gives

<!-- formula-not-decoded -->

From this and (1)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Hence on the inner cylinder we should have

<!-- formula-not-decoded -->

i, flow between parallel plates sloping downward (459)

## PART E. NUMERICAL METHODS

The subdivision into three chapters has been retained . All three chapters have been updated in the light of computer requirements and developments. A list of suppliers (with addresses etc.) has been included on p. 829 of the book.

## CHAPTER 17 Numerical Methods in General

## Major Changes

Updating of this chapter consists of the inclusion of ideas; such as error estimation by halfing, changes in Sec. 17.4 on splines, the presentation of adaptive integration and Romberg integration; and further error estimation techniques in integration.

## SECTION 17.1. Introduction, page 831

Purpose. To familiarize the student with some facts of numerical work in general, regardless of the kind of problem or the choice of method.

## Main Content, Important Concepts

Floating-point representation of numbers, overflow, underflow,

Rounding

Stability

Sources of errors

Error, relative error, error propagation

Short Courses. Mention the round-off iule and the definitions of error and relative error.

## SOLUTIONS TO PROBLEM SET 17.1, page 836

2. ~0.89217 X 102, 0.50000 X 108, ~0.22137 X 10-2

6. 29.9666, 0.0334; 29.9666, 0.0333705

- 8 ~99.980, -0.020; 99.980, ~0.020004
12. ~0.126 X 10-2, ~0.402 X 10-3; -0.267 X 10-6; -0.849 X 10-7
10. Use the last formula in (12) Appendix A3.1. Avoiding differences of large numbers or expressions that may become nearly 0/0 is an important task in the design of algorithms. The problem illustrates that often a simple change in a formula may help. small

14. 65.425 + 17.05905 = 82.48405 = $ = 65.435 + 17.05915 82.49415

16. 2 (9.5 19.5 + 19.5 29.5 + 29.5 . 9.5) = 2081.5 = A = 2321.5 [cm?]

18. The is practically the same as that in the text. With the same notation we get proof

<!-- formula-not-decoded -->

20. Since x2 to 4S, we have |e(x1)/ = 0.005, hence 2/x1

This implies

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Exact: ~8.336016

## SECTION 17.2. Solution of Equations by Iteration; page 838

Purpose: Discussion of the most important methods for solving equations f() = 0, a very important task in practice.

## Main Content; Important Concepts

Solution of f(x) 0 by iteration (3) Xn+1 g(xn)

Condition sufficient for convergence (Theorem 1)

Newton (~Raphson) method (5)

Speed of convergence; order

Secant; bisection; false position methods

## Comments on Content

Fixed-point iteration gives the opportunity to discuss the idea of a fixed point, which is also of basic significance in modern theoretical work (existence and uniqueness of solutions of differential, integral; and other functional equations)

The less important method of bisection and method of false position are included in the problem set.

## SOLUTIONS TO PROBLEM SET 17.2, page 847

- Xo = 0.5, X1 = 0.875, X2 0.330, Xo = 2, X1 = -7, X2 = 344, X3
4. x 1.01 + 1.88/x); 1, 0.778, 0.806347, 0.798340, 0.800447, 0.799881, 0.800032, 0.79999i, 0.800002, 0.799999, 0.800000 (exact)
6. X = llcosh x; 1, 0.64805, 0.82140, 0.73706, approaches 0.76501 (5S exact;, 16 steps) in a nonmonotone fashion.
8. = xl(e' sin x); 0.5, 0.63256, 0.56838, converges to 0.58853 (5S exact) in 14 steps .
- 10
- CAS PROJECT. (a) This follows from the intermediate value theorem of calculus. () Roots r1
- = 1.56155 (6S-value), Y2 ~1 (exact), Y3 ~2.56155 (6S-value). (1)

Y1, about 12 vergent to 0, divergent; (5) r3, about 7 steps; (6) r2, divergent; (7) r1, 4 steps; this is Newton. steps,

<!-- formula-not-decoded -->

case, X4 is 1.414 214, 1.259 1.189 207, 1.148 698. 921,

<!-- formula-not-decoded -->

14. 0.906180 (6S exact; 4 steps; Xo = 1), also obtainable exactly by solving a quadratic equation in x2.
16. 2, 2.452, 2.473; temperature 39.029C
18. 21,21.20870, 21.20575, 21.20575. A Xo is essential. Xo 20 would give a zero near 2.36, which has no meaning for Bessel functions since such an x is too small for the asymptotic formula considered. good
22. 0.7, 0.577094, 0.534162, 0.531426, 0.531391
20. f(x) = f1lx) f2(x) 0; 3, 2.498, 2.472, 2.473
24. TEAM PROJECT. (a)

## ALGORITHM REGULA FALSI (f, a bo, € N). Method of False Position

This   algorithm computes an interval [an bn] containing a solution of f(x) (f continuous) or a solution Cn:

INPUT: Initial interval [ao bo] tolerance €, maximum number of iterations N. OUTPUT:

of failure

<!-- formula-not-decoded -->

If f(cn) = 0 then OUTPUT [Successful completion] Else continue. Stop. Cn;

<!-- formula-not-decoded -->

Else continue.

End

[Unsuccessful completion; N iterations did not give an interval of length not exceeding the tolerance.] Stop.

## SECTION 17.3. Interpolation; page 848

Purpose. To discuss methods for interpolating (or extrapolating)   given data fo) fn), all xj different; arbitrarily or equally spaced, by polynomials of degree not exceeding n. (xo (xn

## Main Content, Important Concepts

Lagrange interpolation (4) (arbitrary spacing)

Error estimate (5)

Newton' s divided difference formula (10) (arbitrary spacing)

Newton's difference formulas (14), (18) (equal spacing)

Short Courses. Lagrange' s formula briefly, Newton' s forward difference formula (14)

## Comment on Content

For given data; the interpolation polynomial p (x) is unique; regardless of the method by which it is derived. Hence the error estimate (5) is generally valid (provided f is n + 1 times continuously differentiable).

## SOLUTIONS TO PROBLEM SET 17.3, page 860

2. This parallels Example 3. From (5) we get

<!-- formula-not-decoded -->

where 9 =t= 9.5. Now the right side is a monotone function of t, hence its extrema Occur at 9.0 and 9.5. We thus obtain

This gives the answer

2.2300 is exact to 4D.

4. From (5) we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The right side is monotone in t, hence its extreme values occur at the ends of the interval 9 = t = 11. This gives

<!-- formula-not-decoded -->

and by adding ã = 2.2192

<!-- formula-not-decoded -->

6. From

<!-- formula-not-decoded -->

and the 5S-values of the logarithm in the text we obtain

<!-- formula-not-decoded -->

This gives the values and errors

2.2407, error 0

2.3028, error -0.0002

2.3517, eIror 0.0003

2.4416, error 0.0007

2.4826, error 0.0023.

It illustrates that in extrapolation one may usually get less accurate values. p2(x) would change if we took more accurate values of the logarithm.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and p3(O.5) = 0.943654 (6S exact 0.938470),P,(1.5) = 0.510116 (6S exact 0.511828), p3(2.5) ~0.047993 (6S exact ~0.048384); see Ref. [1], p. 390, in Appendix 1.

## 10. From (5) we obtain

<!-- formula-not-decoded -->

where, by differentiation;

<!-- formula-not-decoded -->

Another differentiation shows that f" is monotone on the interval 0.25 = t = 1 because

<!-- formula-not-decoded -->

on that interval. Hence the extrema of f" occur at the ends of the interval, so that we obtain

<!-- formula-not-decoded -->

and by adding ã 0.70929

Exact: 0.71116 (SD).

## 12. The difference table is

|       | f(x;)           |                 | 2nd Diff.   | 3rd Diff.   |
|-------|-----------------|-----------------|-------------|-------------|
| 10 15 | 0.94608 1.32468 | 0.37860         | 0.09787     | ~0.01002    |
| 2.0   | 1.60541         | 0.28073 0.17284 | 0.10789     | ~0.01002    |
| 2.5   | 1.77825         |                 |             |             |

The interpolating polynomials and errors are

<!-- formula-not-decoded -->

0.70496 = a = 0.71896.

<!-- formula-not-decoded -->

Note the decrease of the error.

## 14. The divided difference table is

|   Xj |   f(x;) |         |
|------|---------|---------|
|  9   |  2.1972 |         |
|  9.5 |  2.2513 | ~0.0053 |
| 11   |  2.3979 |         |

This gives by (10)

<!-- formula-not-decoded -->

the discrepancies being due to round-off, as can be seen by one Or two additional digits in the computations. using

## 16. With the in j the difference table is change

|    |   Xj | cosh X;   |                               |                     |           |
|----|------|-----------|-------------------------------|---------------------|-----------|
| =3 |  0.5 | 1.127 626 | 0.057 839 0.069 704 0.082 266 | 0.011 865 0.012 562 | 0.000 697 |
|    |  0.6 | 1.185 465 | 0.057 839 0.069 704 0.082 266 | 0.011 865 0.012 562 | 0.000 697 |
|    |  0.7 | 1.255 169 | 0.057 839 0.069 704 0.082 266 | 0.011 865 0.012 562 | 0.000 697 |
|    |  0.8 | 1.337 435 | 0.057 839 0.069 704 0.082 266 | 0.011 865 0.012 562 | 0.000 697 |

From this and (18) we obtain

<!-- formula-not-decoded -->

and with x 0.56 this becomes

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This agrees with Example 5. The correct last digit is 1 (instead of 5 here or 4 in Ex ample 5).

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 18. The difference table is

| Xj   | J1(x;)   |      |      |     |    |    |
|------|----------|------|------|-----|----|----|
| 0.0  | 0.0000o  |      |      |     |    |    |
|      |          | 9950 |      |     |    |    |
| 0.2  | 0.09950  |      | 297  |     |    |    |
|      |          | 9653 |      | 289 |    |    |
| 0.4  | 0.19603  |      | 586  |     | 22 |    |
|      |          | 9067 |      | 267 |    | 5  |
| 0.6  | 0.28670  |      | 853  |     | 27 |    |
|      |          | 8214 |      | 240 |    |    |
| 0.8  | 0.36884  |      | 1093 |     |    |    |
|      |          | 7121 |      |     |    |    |
| 1.0  | 0.44005  |      |      |     |    |    |

From this and (14) we by straightforward calculation get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

the errors being 1, 0, 0, 1, 0 unit of the last given digit.

## 20. TEAM PROJECT. (a) For p1(x) we need

<!-- formula-not-decoded -->

p1(x) 2.19722(19 2x) 4 2.25129(-18 + 2x) = 1.22396 0.10814x, P1(9.2) 2.21885.

<!-- formula-not-decoded -->

This gives (with 1OS- values for the logarithm)

<!-- formula-not-decoded -->

hence 2) 2.21916, error 0.00004. The error estimate is P2(9.

<!-- formula-not-decoded -->

- (b) Extrapolation gives a much error. The difference table is larger

|   0.2 |   0.9980 |        |        |
|-------|----------|--------|--------|
|   0.4 |   0.9686 |        | 0.0949 |
|   0.6 |   0.8443 | 0.1243 | 0.1842 |
|   0.8 |   0.5358 | 0.3085 | 0.2273 |
|  10   |   0      | 0.5358 |        |

The differences not shown are not needed. x = 0.6,0.8, 1.0 gives the best result. Newton's formula (14) with = 0.1/0.2 = 0.5 gives Taking

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Similarly, by taking x 0.4, 0.6,0.8 we obtain

<!-- formula-not-decoded -->

Taking x = 0.2, 0.4, 0.6, we extrapolate and get a much poorer result:

<!-- formula-not-decoded -->

- (e 0.386 4185, exact to 7S.

## SECTION 17.4. Splines; page 861

Purpose Interpolation of data fo), fn) by a (cubic) spline, that is, a twice is given by a polynomial of third degree at most. (xo, (Xn

Short Courses. This section may be omitted.

## Comments on Content

Higher order polynomials tend to oscillate between nodes\_Pe(r) in 402 is typical and splines were introduced to avoid that phenomenon: This motivates their application. Fig

If we impose the additional condition (3) with given ko and kn, then for given data the cubic spline is unique.

## SOLUTIONS TO PROBLEM SET 17.4, page 867

- 2.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This verifies (4). By differentiation;

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

There remains

<!-- formula-not-decoded -->

Similarly, if x Xj+1, then G 0 and

<!-- formula-not-decoded -->

because [' ' '] =0. This verifies (5)

4. This is simple and straightforward.
6. aj2 can be seen from (7), and a;8 follows directly as indicated in the text after (14).
3. p2(x)]' = 4x3 2x = 0 gives the points of maximum deviation

<!-- formula-not-decoded -->

For the spline g(x) we get; taking x = 0

<!-- formula-not-decoded -->

solution is x = 1/2. The corresponding maximum deviation is

which is merely 259 of the previous value.

10. Since the third derivative of a cubic polynomial is constant and g(x) consists of cubic polynomials; g"(x) is always piecewise constant: Since 8 (x) is assumed to be continuous, g" '(x) = M = const throughout the entire interval.  By integration = Mx + Aj  Since g"(x) is always continuous, Aj = A =const for all j. This idea and two more integrations show that g(x) is just one cubic polynomial throughout the whole interval. P;(x)"
12. Po(x) ~ 4x3 6x2

<!-- formula-not-decoded -->

16. Po

P1

<!-- formula-not-decoded -->

=

1

The interpolation polynomial is (Fig: 405)

- 5 5 (instead of 1) was chosen to avoid fractions } throughout:. Equation (12) gives k1 = ~1, k2 = 4, k3 = 0, k4 = ~4, k5 = 1. From this and (13)-(14) we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Note that this is an even function; and so is the interpolation polynomial

<!-- formula-not-decoded -->

Section 17.4. Cubic spline versus polynomial of 6th degree in Problem 18

<!-- image -->

## 20. TEAM PROJECT.

<!-- formula-not-decoded -->

## SECTION 17.5. Numerical Integration and Differentiation, page 869

Purpose; Evaluation of integrals of empirical functions; functions not integrable by ele mentary methods; etc.

## Main Content, Important Concepts

rule (7) (most important) , error (8), (10)

Trapezoidal rule (2), error (4), (5)

Gaussian integration

Adaptive integration with Simpson' s rule (Example 6)

Numerical differentiation

Short Courses. Discuss and apply Simpson's rule.

## Comments on Content

The range of numerical integration includes empirical functions; as measured or recorded in experiments, functions that cannot be integrated by the usual methods, or functions that can be integrated by those methods but lead to expressions whose computational evaluation would be more complicated than direct numerical integration of the integral itself:

Numerical  differentiation can sometimes be avoided by changing the mathematical model of the problem.

Simpson's rule approximates the integrand by quadratic parabolas. Approximations by higher   order  polynomials are possible, but lead to formulas   that are   generally   less practical.

## SOLUTIONS TO PROBLEM SET 17.5, page 880

- 2 A = J= B,A = Aj and B; being lower and upper bounds for f in the jth subinterval. 0.681 = J = 0.808.
6. + €n-1 + genl = [(b a)In]nu (b a)u. This is similar to the corresponding for Simpson' s rule given in the text. proof
4. h = 1,J1 0.5; h 0.5,Jo.s = 0.28125, €.5 3(0.28125 0.5) = ~0.07292 (actual error -0.08125); h = 0.25, Jo.25 = 0.22070, €0.25 4(0.22070 0.28125) ~0.02018 (actual error ~0.02070). The agreement is very good. The same is true in Prob. 5, where we integrate a trigonometric function (instead of a single power of x)
8. 0.693150. Exact to 6D: In 2 = 0.693147
10. 0.07392 8162. Exact to 9D: 0.07392 8106
12. 0.78539 8153. Exact to 9D: 0.78539 8163
- 14 C = ~0.54/90 in (9), ~0.000695 = ~0.000094 (actual ~0.000292). In (10),

<!-- formula-not-decoded -->

Note that the absolute value of this is less than that of the actual error, and we must carefully distinguish between bounds and approximate values.

18. 0.4716. Exact to 4D: 0.4615. For tables, see Ref. [1]
16. 0.946146,0.946083. Exact to 6D: 0.946083. A modest table is included in Appendix 5. See Ref. [1] for larger tables.
3. Bessel functions.
22. (a) Mz = 2, M2* = 1/4, hence by (4) and the accuracy requirement;

<!-- formula-not-decoded -->

- () From (9) with fiv = = 24, and the accuracy requirement;

<!-- formula-not-decoded -->

24. TEAM PROJECT. The factor 24 = 16 comes in because we have replaced h by !h, has the factor 1/(26

which gives n 183.

which gives 2m 14.

J1 = 0

<!-- formula-not-decoded -->

J44 is exact to SD.

28. Differentiating (14) in Sec. 17.3 with respect to r and dr = dxlh we get using
26. 0.240,which is not exact: It can be shown that the error term of the present formula h &lt; $ &lt; x2 + h. In 0.256 and 0.256 + 0 = 0.256, respectively .

<!-- formula-not-decoded -->

Now x Xo gives r = (x = = 0 and the desired formula follows . xo)/h

## SOLUTIONS TO CHAPTER 17 REVIEW, page 882

22. 0.14910 102, ~0.91842 X 10-1, 0.30303 104, ~0.81818 X 10-1, 0.97656 X 10-3
24.  8.2586, 8.258, 9.90, impossible
28. In multiplication; relative errors add (see the proof of Theorem 1 in Sec. 17.1).
32. Because |g' (x)l is small (0.038) near the solution 0.739085.
30. Multiply numerator and denominator by V2 + 16 + 4, s0 that the given expression takes the form x2I(VR + 16 + 4)
34. 0.641714
7. 36.0.450184
38. 0.4, 0.085

40. 2.969

<!-- formula-not-decoded -->

44. Jo.s 0.90266, = 0.90450, 0.00012 Jo.25 €0.25

<!-- formula-not-decoded -->

J33 is exact to 4D.

## CHAPTER 18 Numerical Methods in Linear Algebra

## SECTION 18.1. Linear Systems: Gauss Elimination; page 886

Purpose. To explain the Gauss elimination; which is a solution method for linear systems of algebraic equations by systematic elimination (reduction to triangular form)

## Main Content; Important Concepts

Gauss elimination, back substitution

Pivot equation; pivot; choice of pivot

Operations count; order [e.g. O(n?)]

## Comments on Content

This section is independent of Chap. 6 on matrices (in particular; Sec. 6.3, where the Gauss elimination is also considered) .

Gauss' s method and its variants (Sec. 18.2) are the most important solution methods for those systems (with matrices that do not have too many zeros).

The Gauss-Jordan method (Sec. 18.2) is less practical because it requires more operations than the Gauss elimination.

Cramer' $ rule (Sec. 6.6) would be totally impractical in numerical work, even for systems of modest size.

## SOLUTIONS TO PROBLEM SET 18.1, page 893

2 X2 (25/42)x1 *1 arbitrary

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

10. X1 =2

12. No solution; the matrix obtained at the end is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

20. TEAM PROJECT. (a) (i) a # 1 to make D = a = 1 # O; (ii) a = 1, b = 3;
2. = 4(3x3 tem. The second system has no solution.
3. (c) det A = 0 can change to det A # 0 because of round-off.
4. (d) (1 = 2 lle eventually becomes x2le ~ Ile, X2 = 1, X1 = (1 x2)le ~ 0. The exact solution is X1 = 1/(1 e) X2 (1 20)/(1 e) We obtain it if we take X1 + x2 = 2 as the pivot equation.

- (e The exact solution is x1 = 1, X2 ~4. The 3-digit calculation gives X2 ~4.5, X1 = 1.27 without pivoting and x2 = ~6, X1 = 2.08 with pivoting. This shows that 3S is simply not enough. The 4-digit calculations give x2 = ~4.095, = 1.051 without pivoting and the exact result x2 1 with

## SECTION 18.2 Linear Systems: LU-Factorization; Matrix Inversion; page 894

Purpose: To discuss Doolittle' s, Crout's, and Cholesky' s methods, three methods for solv linear systems that are based on the idea of writing the coefficient matrix as a uct of two triangular matrices ('LU-factorization") . Furthermore; we discuss matrix inversion by the Gauss-Jordan elimination. ing prod -

## Main Content, Important Concepts

Doolittle's and Crout' s methods for arbitrary square matrices

Numerical matrix inversion

Cholesky' method for positive definite symmetric matrices

Short Courses. Doolittle's method and the Gauss-Jordan elimination.

## Comment on Content

L suggests 'lower triangular' and U triangular. For Doolittle' s method, these are the same as the matrix of the multipliers and of the triangular system in the Gauss elimination.

The point is that in the present methods; one solves one equation at a time; no systems .

## SOLUTIONS TO PROBLEM SET 18.2, page 899

<!-- formula-not-decoded -->

12. x(-A)x = ~xTAx &lt; 0, no; xAx = (xTA Tx)T because this is a scalar; this gives xTATTxTT = xTAx &gt; 0, yes: A + B is positive definite; A B is not.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- = [ujk] are

<!-- formula-not-decoded -->

- To get the Doolittle factorization; take the transpose of Crout's factorization. The Cholesky factorization is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

20. det A =0 as given; but rounding makes det A # 0 and may completely change tbe situation with respect to existence of solutions of linear systems; a to be watched for when using a CAS. In the present case we get (a) ~0.00000035, (b) ~0.00001998, (c) ~0.00028189, (d) 0.002012, (e) 0.0002. point

## SECTION 18.3. Linear Systems: Solution by Iteration, page 900

Purpose: To familiarize the student with the idea of solving linear systems by iteration; to explain in what situations that is practical; and to discuss the most important method (Gauss-Seidel iteration) and its convergence

## Main Content, Important Concepts

Distinction between direct and indirect methods

Gauss-Seidel iteration; its convergence; its range of applicability

Matrix norms Jacobi iteration

Short Courses. Gauss-Seidel iteration only.

## Comments on Content

A word on the frequently occurring sparse matrices may be good. For instance; we have about  99.59 zeros in solving the Laplace equation in two dimensions by 1000 X 1000 and the usual five-point pattern (Sec. 19.4) using grid

The Jacobi iteration appeals by its simplicity but is of no practical value.

## SOLUTIONS TO PROBLEM SET 18.3, page 905

2. The exact solution 3, ~9,6 is reached at 8, rather quickly due to the fact that the spectral radius of C is 0.125, hence rather small. Step
6. The exact solution is 2, 0, 1. 10 gives [2.00144 ~0.00221311 The spectral radius (3)3/2 0.544331 of C is relatively Step large.
4. Interchange the first equation and the last equation: Then the exact solution ~2.5,2, 4.5 is reached at 11, the spectral radius of C = 0.258199. (The eigenvalues are complex conjugates; and the third eigenvalue is 0, as for the present C.) Step being always
4. 8 In (a) we obtain

<!-- formula-not-decoded -->

and   Ilcl 0.2 &lt; 1 by (11), which implies convergence by (8). In (b) we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

From this we compute

Developing the characteristic determinant by its first column, we obtain

<!-- formula-not-decoded -->

which shows that one of the eigenvalues is greater than 1 in absolute value; so that we have divergence.

<!-- formula-not-decoded -->

Step 5 of the Gauss-Seidel iteration gives the better result

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

5 of the Gauss-Seidel iteration gives the more accurate result Step

<!-- formula-not-decoded -->

14. The eigenvalues of I A are 0.5,0.5, -1. Here, A is 2 times the coefficient matrix of the given system.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SECTION 18.4. Linear Systems: Ill-Conditioning, Norms, page 906

Purpose. To discuss ill-conditioning quantitatively in terms of norms; leading to the condition number and its role in judging the effect of inaccuracies on solutions.

## Main Content, Important Concepts

Ill-conditioning, well-conditioning

Symptoms of ill-conditioning

Residual

Vector norms

Matrix norms

Condition number

Effect of inaccuracies of coefficients on solutions

## Comment on Content

Reference [E8] in Appendix 1 gives some help when A-1, needed in K(A), is unknown (as is usual in practice).

## SOLUTIONS TO PROBLEM SET 18.4, page 912

2. 12, V5O ~ 7.07, 5, [0.6 0.8 4 5, V5 ~ 2.24, 1, [1 1 1 1 1] 6. 1, 1, 1, [0 0 0 1

8. 2, 2; 2 . 2 = 4, 2 . 2 =4. Inverse

<!-- formula-not-decoded -->

10. 5.5, 5.5; 5.5 136 = 748,5.5 136 = 748, ill-conditioned. Inverse

<!-- formula-not-decoded -->

- 13 = 247,21 13 = 273. Inverse

<!-- formula-not-decoded -->

- = 0.845455, X2 = 1.27273 (6S); K(A) = 4.7 . 42.7273 200.8
18. By\_ (12), 1 K(A) norm, n = Illl = K(A)
16. The residual is [0.145 0.120]7, whereas the approximate solution deviates from the true solution by a factor 5 (the first component) and 34: This is a consequence of the fact that the system is very ill-conditioned.
20. TEAM PROJECT. (a) Formula (18a) is obtained from

<!-- formula-not-decoded -->

Equation (18) follows from (18a) by division by n.

To get (19b), divide (19a) by Vn.

- (d) These &lt;axioms of a norm" follow from (3), which are the axioms of vector norm
- (b) To get the first inequality in (19a) consider the square of both sides and then take square roots on both sides. The second inequality in (19a) follows by means of the Cauchy-Schwarz inequality and a little trick worth remembering;

<!-- formula-not-decoded -->

- (c) Let # 0. Set X = 1. Also; Ax A(llxlly) of = 1 we only take the maxi mum over all y of norm 1 Write x for y to get (10) from this. taking

## SECTION 18.5. Method of Least Squares, page 914

## Main Content; Important Concepts

Purpose; To explain Gauss's least squares method of "best fit" of straight lines to given data Yo), yn) and its extension to best fit of quadratic polynomials; etc (xo,

Least squares method

Normal equations (4) for straight lines

Normal equations (8) for quadratic polynomials

Short Courses. Discuss the linear case only.

Comment. Normal equations are often ill-conditioned,  so that results may be sensitive to round-off. For another (theoretically much more complicated) method, see Ref. [E3], p. 201.

## SOLUTIONS TO PROBLEM SET 18.5, page 916

2. 3.68 1.22x. Note the considerable change of the slope.
6. 2950, 2 1 822 500, 7010, 4 490 OOO; this gives the normal equations Sx; Sx; SxjY;
4. 95.26 0.574t, where t 0 [min] corresponds to 12:00. This is a cooling process following Newton's law of cooling, an exponential decrease of temperature; this explains the better fit in Prob. 5.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The solution is bo ~1145.79, b1 = 4.32. Answer:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

12. 1660 + 656x 32x2

10. 0.955 1.159x + 0.932x2

14. 5.9 0.O5x; 5.9 0.95x + 0.23x2

<!-- formula-not-decoded -->

20. TEAMPROJECT. (a) We substitute Fm(x) into the integral and perform the square.
18. ~0.15 + 0.35x; 0.09 + 0.35x 0. ~0.03 1.S4x O.1lx2 + 0.57x3. Note the large x3-term, which had to be expected from the position of the given points.

<!-- formula-not-decoded -->

This is a quadratic function in the coefficients. We take the partial derivative with respect to any one of them; call it av and equate this derivative to zero. This gives

<!-- formula-not-decoded -->

Dividing by 2 and taking the first integral to the right gives the of normal = 0 m. system

- (b) In the case of a polynomial we have

<!-- formula-not-decoded -->

- which can be readily integrated:. In particular; if a = 0 and b 1, integration from 0 to 1 gives 1/(j + 1), and we obtain the Hilbert matrix the coefas ficient matrix.
- In the case of an orthogonal system we see from (4), Sec. 4.8, with p(r) 1 (as

## SECTION 18.6. Matrix Eigenvalue Problems: Introduction; page 917

The section frees both the instructor and the student from the task of locating these matters in 6 and 7, which contain much more material and should be consulted only if problems on one or the other matters are wanted (depending on the of the student) or if a proof might be of interest. background Chaps.

Purpose. This section is a collection of concepts and handful of theorems on matrix eigenvalues and eigenvectors that are frequently needed in numerical methods; some of them will be discussed in the remaining sections of the chapter and others can be found in more advanced or more specialized books listed in part E of Appendix 1.

## SECTION 18.7. Inclusion of Matrix Eigenvalues;, page 920

Purposef To discuss theorems that give approximate values and error bounds of eigenvalues of general (square) matrices (Theorems 1, 2, 4, Example 2) and of special matrices (Theorem 6).

## Main Content; Important Concepts

Gerschgorin's theorem (Theorem 1)

Sharpened Gerschgorin' s theorem (Theorem 2)

Strict diagonal dominance (Theorem 3)

Gerschgorin's theorem improved by similarity (Example 2)

Schur' s inequality (Theorem 4), normal matrices

Perron' s Theorem (Theorem 5)

Collatz' s theorem (Theorem

## Short Courses. Discuss Theorems 1 and 6.

## Comments on Content

It is important to emphasize that one must make sure whether or not a thoerem whatsoever, whereas others are restricted to certain classes of matrices . always

The exciting Gerschgorin's theorem was one of the early theorems on numerical meth ods for eigenvalues; it appeared in Bull: Acad: Sciences d 7URSS (Classe mathém; 7-e wandte Mathematik und Mechanik

## SOLUTIONS TO PROBLEM SET 18.7, page 924

2. Symmetric   matrix;  hence we intervals on the  real  axis, 9.7 1 The eigenvalues (6S-values) are 10.0082, 5.9 2.99429. 99751, get

- Spectrum (6S-values) ~0.0933282 + 1.O6li, ~0.403385

0.72446i,3.49671 + 4.66346i

- 0.5, 1.8, and we can take the smaller of the two in each case. Spectrum 0.108609 + 0.742484i (absolute value 0.750386), 1.182781.
- 8 T with t11 = t22 = 1,t 34 gives

<!-- formula-not-decoded -->

Note that the disk with center 3 is still disjoint from that with center 10.

## 10. An example is

<!-- formula-not-decoded -->

The eigenvalues   are =1 and 1, s0 that the entire spectrum lies on the circle. A similar-looking 3 X 3 matrix or 4 X 4 matrix, can be constructed with some or all of its eigenvalues on the circle. etc.,

12. This is a 'continuity proof: Let $ = D1 U D2 U . U Dp without restriction; where We write A = B 4 C, where B consider diag

<!-- formula-not-decoded -->

Then Ao = B and A1 A. Now by algebra, the roots of the characteristic polynomial f.(A) of At (that is, the eigenvalues of At) depend continuously on the coeffi cients of fz(A), which in tumn depend continuously on t. For t = 0, the eigenvalues are If we let t increase continuously from 0 to 1, the eigenvalues move continuously and, by Theorem 1, for each t lie in the Gerschgorin disks with centers ajj and radii 011' @nn;

<!-- formula-not-decoded -->

Since at the end, $ is disjoint from the other disks, the assertion follows.

14. These proofs follow readily from the definition of these classes of matrices.
16. A?(A?)T = AAATAT = ATA (AB)(AB) (AB)(AB) if and only if BTA = ABT; no, in general. CCT CTC is symmetric, hence normal. TAA; yes.
3. The third gives 31.66 = ^ = 33.00.
20. CAS PROJECT. (a) The midpoint is an approximation for which the endpoints give error bounds.

In practice, one would compute several steps and use the last two vectors for determining an interval that contains an eigenvalue. See Example 4 in the text.

- (b) Nonmonotone behavior may occur if by chance you pick an initial vector close to an eigenvector corresponding to an eigenvalue that is not largest in absolute value.

## SECTION 18.8. Eigenvalues by Iteration (Power Method), page 925

bounds for eigenvalues of real symmetric matrices.

## Main Content; Important Concepts

The iteration process of the power method

Rayleigh quotient (the approximate value)

(for eigenvectors) Scaling

Improvement of convergence by a spectral shift

Short Courses. Omit spectral shift.

## Comments on Content

The method is simple but converges slowly, in general:

Symmetry of the matrix is essential to the validity of the error bound (1). The method as such can be applied to more general matrices.

## SOLUTIONS TO PROBLEM SET 18.8, page 928

<!-- formula-not-decoded -->

This illustrates that the error bounds € need not be a monotone function of the are present case) They large.

4. 9 = 11.3333, 11.9802, 11.9994; lel = 2.4944, 0.4446, 0.0742. The rapid convergence to the absolutely largest eigenvalue; 12, results from the fact that the other eigenvalues; 2 and ~2, are much smaller in absolute value.
8. We get the vectors
6. 9 10.5000, 1l. 1303, 11.1831; lel = 2.95804, 1.36886, 0.96374

<!-- formula-not-decoded -->

and from them the following. From the first Collatz gives 8 = ^ = 14, thus; if one wishes, the approximation 11 and error bound 3. Our Theorem 1 gives 11.33 9 (a bit closer to the exact &gt; nitude as Collatz' s bound. mag two;

ap proximation 11.643 and error bound 0.643. Theorem 1 gives 9 = 11.98, which is much closer to 12, and |e| = 0.45, about of the same quality as the bound by Collatz.

Remember that Collatz assumes positivity of the matrix entries; whereas in Theowe require symmetry of the matrix; in that sense the two theorems are not com parable. Theorem 1 uses all components of the vectors involved; and that tends to give better results than those from methods that use only one Or two components.

Note further that Theorem 1 requires more operations (not excessively many, however).

10. The eigenvalues are ^ = 45. Corresponding eigenvectors are

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and I have chosen Xo as so that

etc. From this , and for the error bound we get

<!-- formula-not-decoded -->

and similarly in all the further steps. This shows that our error bound is the best possible in general.

12. The scaled vectors

<!-- formula-not-decoded -->

approach their limit [1 1/3]T (corresponding to ^ = 7) in a somewhat irregular way during these first steps, indicating that the sequence begins with a linear combination ofthe two eigenvectors with a substantial contribution of each. The other eigenvector is [1/3 1]T , corresponding to À ~3.

- gence is determined by the ratio 11:8, approximately . The approximations obtained are

<!-- formula-not-decoded -->

## SECTION 18.9. Tridiagonalization and QR-Factorization, page 929

Purpose  Explanation of an optimal method for determining the whole spectrum of a real symmetric matrix by first reducing the matrix to a tridiagonal matrix with the same spec trum and then applying the QR-method;, an iteration in which each step consists of a factorization (5) and a multiplication (6).

## Comment on Content

Householder steps correspond to similarity transformations; hence the spectrum is preserved. The same holds for QR

## SOLUTIONS TO PROBLEM SET 18.9, page 937

<!-- formula-not-decoded -->

6S-values of the eigenvalues are 14.2005, ~6.30525, 2.10476. Hence the diagonal entries are more accurate than one would expect by looking at the size of the off-diagonal entries.

<!-- formula-not-decoded -->

The spectrum is 0.72, 0.36, 0.09.

## SOLUTIONS TO CHAPTER 18 REVIEW , page 938

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

28. Reorder to get convergence. Equation 1 becomes 2, 2 becomes 3, 3 becomes 1. Solution X1 ~2, X2 = 8, X3 =1 The iteration gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

40. 8.8 19.15 = 168.5. The matrix is ill-conditioned.

42. y = 2.89 + 0.505x

44. y= 1.95 2.217x + 1.067x2

34. 2.4,

2.48, 1.2

## CHAPTER 19 Numerical Methods for Differential Equations

## Major Changes

These include automatic variable step size selection in modern codes, the discussion of the Runge-Kutta-Fehlberg method; and the extension of Euler and Runge-Kutta methods to systems and higher order equations.

## SECTION 19.1. Methods for First-Order Differential Equations; page 942

Purpose; To explain   three   numerical methods   for   solving   initial value   problems y f(x, y) Y(xo) yo by stepwise computing approximations to the solution at X1 = xo + h, X2 = Xo + 2h, etc.

## Main Content; Important Concepts

Euler' s method (3)

Automatic variable step size selection

Improved Euler method (7)

Classical Runge-Kutta method (Table 19.4)

Error and step size control

Runge-Kutta-Fehlberg method

## Comments on Content

Euler' s method is good for explaining the principle but is too crudeto be of practical value.

The improved Euler method is a simple case of a predictor-corrector method.

Principles for a good choice of h are important in any method.

f in the equation must be such that the problem has a solution (see Sec. 1.9) unique

## SOLUTIONS TO PROBLEM SET page 951 19.1,

2. y = 1.01170 &gt; 1, Y1o comes out complex and is meaningless.

|   Xn | Yn      | Error X 105   |
|------|---------|---------------|
|  0.1 | 0.15708 | 65            |
|  0.2 | 0.31221 | ~319          |
|  0.3 | 0.46144 | 745           |
|  0.4 | 0.60079 | 1301          |
|  0.5 | 0.72636 | 1926          |
|  0.6 | 0.83433 |               |
|  0.7 | 0.92092 | 2991          |
|  0.8 | 0.98214 | 3109          |
|  0.9 | 1.01170 | 2401          |
| 10   |         |               |

4. y = tan x X (special Riccati equation; set y 4 u, then u = u2 + 1, etc.) The computation gives
2. 6 y = 1/(1 Bernoulli equation; see Sec. 1.6. special
8. y = tan 2x. Note that the error is first negative and then positive and rapidly increasing, due to the behavior of the tangent.
10. The error of y(l) is -0.0036, hence comparable to that in Prob. 7. The eITor of is +0.0067, hence twice that in Prob. 7 and of the opposite sign. y(2)
12. y = 0,0.2055,0.4276,0.6587,0.8924; error 0, 0.0101,0.0221,0.0322,0.0409. Hence the error is about 209 less.

|   Xn | Yn        | y(xn)     | Error 106   |
|------|-----------|-----------|-------------|
|  0.1 | 0.000 000 | 0.000 335 | 335         |
|  0.2 | 0.001 000 | 0.002 710 | 1 710       |
|  0.3 | 0.005 040 | 0.009 336 | 4 296       |
|  0.4 | 0.014 345 | 0.022 793 | 8 448       |
|  0.5 | 0.031 513 | 0.046 302 | 14 789      |
|  0.6 | 0.059 764 | 0.084 137 | 24 373      |
|  0.7 | 0.103 292 | 0.142 288 | 38 996      |
|  0.8 | 0.167 820 | 0.229 639 | 61 818      |
|  0.9 | 0.261 488 | 0.360 158 | 98 670      |
|  1   | 0.396 393 | 0.557 408 | 161 014     |

|   Xn |       Yn |   Error X 106 |
|------|----------|---------------|
|  0.1 | 0.524969 |            10 |
|  0.2 | 0.549813 |            21 |
|  0.3 | 0.574411 |            32 |
|  0.4 | 0.598645 |            42 |
|  0.5 | 0.622407 |            53 |
|  0.6 | 0.645593 |            63 |
|  0.7 | 0.668114 |            74 |
|  0.8 | 0.68989  |            84 |
|  0.9 | 0.710855 |            94 |
|  1   | 0.730955 |           104 |

|   Xn | Yn      |   Error X 105 |
|------|---------|---------------|
| 0.05 | 0.10050 |            17 |
| 0.1  | 0.20304 |            33 |
| 0.15 | 0.30981 |            48 |
| 0.2  | 0.42341 |            62 |
| 0.25 | 0.54702 |            72 |
| 0.3  | 0.68490 |            76 |
| 0.35 | 0.84295 |            66 |
| 0.4  | 1.02989 |            25 |
| 0.45 | 1,25930 |           +86 |
| 0.5  | 1.55379 |           362 |

- 14 ) 20,0.1033,0.2134,0.3280,0.4456,0.5650,0.6852,0.8058,0.9261; error 0,0.0011, 0.0022, 0.0071; about 159 of that in Prob. 11.
16. For   instance, = 0.5, y 0.632 114 762 (error 0.58 10-5); = 1 y = 0.864 660 452 (error 0.43 10-5); hence the error is substantially and it is interesting that it is not increasing: for x 0.1, 1.0, it is 0.26,0.42, 0.52, 0.57, 0.58, 0.57, 0.54, 0.51, 0.47, 0.43 times less, 10-5 .
- ~9.3. ~5.1,

| Xn   | Yn                         | Error Estimate (10) X 109   | Error X 109   |
|------|----------------------------|-----------------------------|---------------|
| 0.1  | 1.20033 46725              | 3.0                         | ~0.4          |
| 0.2  | 1.40271 00374 .60933 62546 | 3.7                         | =19           |
| 0.3  | 1                          | 5.9                         | 5.0           |
| 0.4  | 1.82279 32298              | 9.4                         | ~11.0         |
| 0.5  | 2.04630 25124              | 13.1                        | 22.5          |
| 0.6  | 2.28413 68531              | 14.4                        |               |
| 0.7  | 2.54228 84689              |                             | ~88.4         |
|      | 2.82963 87346              | 38.8                        | 177.6         |
| 0.9  | 3.16015 85865              | 191.1                       | 369.0         |
| 1.0  | 3.55740 85377              | 699.9                       | 813.0         |

20.

## SECTION 19.2. Multistep Methods, page 952

Purposes To explain the idea of a multistep method in terms of the practically important Adams-Moulton method; a predictor\_corrector method that in each computation uses four preceding values.

## Main Content; Important Concepts

Adams-Bashforth method (5)

Adams-Moulton method (7)

## SOLUTIONS TO PROBLEM SET 19.2, page 955

|    |   Xn | Starting Yn   | Predicted Yn   | Corrected Yn   | Exact     |
|----|------|---------------|----------------|----------------|-----------|
|    |  0   | 1.000 000     |                |                |           |
|    |  0.1 | 1.105 171     |                |                |           |
|    |  0.2 | 1.221 403     |                |                |           |
| 3  |  0.3 |               |                |                |           |
| 4  |  0.4 |               | 1.491 821      | 1.491 825      | 1.491 825 |
| 5  |  0.5 |               | 1.648 717      | 1.648 722      | 1.648 721 |
| 6  |  0.6 |               | 1.822 114      | 1.822 120      | 1.822 119 |
| 7  |  0.7 |               | 2.013 748      | 2.013 754      | 2.013 753 |
| 8  |  0.8 |               | 2.225 536      | 2.225 543      | 2.225 541 |
| 9  |  0.9 |               | 2.459 598      | 2.459 605      | 2.459 603 |
| 10 |  1   |               | 2.718 277      | 2.718 285      | 2.718 282 |

| Xn   | Yn       | Exact    | Error X 106   |
|------|----------|----------|---------------|
| 1.0  |          |          |               |
| 1l   | 0.104394 | 0.104394 |               |
| 1.2  | 0.215563 | 0.215563 |               |
| 1.3  | 0.331199 | 0.331199 |               |
| 1.4  | 0.449688 | 0.449886 | 2.3           |
|      | 0.569871 | 0.569867 | 3.5           |
| 1.6  | 0.690911 | 0.690907 | 3.8           |
| 1.7  | 0.812198 | 0.812195 |               |
| 18   | 0.933284 | 0.933280 |               |

## 6. Solution y2 x2 = 8.

8. y = tan x + x + 1. tan x

12 y

=

Some of the values and errors are:

e*?

|   Xn |   Yn (h 0.05) | Error X 106   |   Yn (h = 0.1) | Error X 106   |
|------|---------------|---------------|----------------|---------------|
|  0.1 |       1.01005 |               |        1.01005 |               |
|  0.2 |       1.04082 |               |        1.04081 |               |
|  0.3 |       1.09419 | 14            |        1.09422 | 50            |
|  0.4 |       1.17353 | 24            |        1.17362 | =112          |
|  0.5 |       1.28406 | 38            |        1.28422 | 194           |
|  0.6 |       1.43339 | 58            |        1.43364 | 307           |
|  0.7 |       1.6324  | 87            |        1.63278 | ~466          |
|  0.8 |       1.89661 | ~131          |        1.89718 | 694           |
|  0.9 |       2.2481  | 197           |        2.24893 | 1023          |
|  1   |       2.71858 | 297           |        2.71978 | 1503          |

The errors differ by a factor 4 to 5, approximately .

<!-- formula-not-decoded -->

## SECTION 19.3. Methods for Systems and Higher Order Differential Equations, page 956

der equations.

| Xn   |      Yn |
|------|---------|
| 1.2  | 3.07246 |
| 1.4  | 3.15595 |
| 1.6  | 3.24962 |
| 1.8  | 3.35261 |
| 2.0  | 3.4641  |
| 2.2  | 3.5833  |
|      | 3.70945 |
| 2.6  | 3.84188 |
| 2.8  | 3.97995 |
| 3.0  | 4.12311 |

## Content

Euler' s method for systems (5)

Classical Runge\_Kutta method extended to systems (6)

Runge-Kutta-Nyström method (7)

## SOLUTIONS TO PROBLEM SET 19.3, page 961

2. See Fig: 82 in Sec. 3.3. The discussion in Sec. 3.3 is not needed for the present purpose. The computation gives:
4. y = 0 ~0.15, ~0.3, ~0.44925, -0.596996, ~0.742481. The etror increases monotone from 0 to 0.0081.
6. Much more accurate values .
4. 8 from Ref:. [1] in Appendix 1.

|     | Y1      | Y2      |
|-----|---------|---------|
| 0   |         |         |
| 0.2 | 0.8     | 3.2     |
|     | 1.28    | 2.4     |
| 0.6 | 1.504   | 1.664   |
| 0.8 | 1.536   | 1.0304  |
| 1.0 | 1.43488 | 0.51712 |

|     |     Y(x) | 108 X Error of y(x)   | y (x)    |
|-----|----------|-----------------------|----------|
| 0.1 | 0.804837 |                       | ~1.90484 |
| 0.2 | 0.618731 | ~15                   | =181873  |
| 0.3 | 0.440818 |                       | 1.74082  |

|     |    Jo(x) |           |      |
|-----|----------|-----------|------|
| 1   | 0.765198 | 0.440051  |      |
| 1.5 | 0.511903 | ~0.558002 | ~76  |
| 2   | 0.224008 | ~0.576897 | ~117 |
| 2.5 | 0.048289 | ~0.497386 | ~95  |
| 3   | 0.260055 | ~0.339446 | +3   |
| 3.5 | 0.380298 | ~0.137795 | 170  |

10.

|   Xn |     Yn | Yn     | Yn     |   Exact (4S) | Error   |
|------|--------|--------|--------|--------------|---------|
|  0.2 | 0.02   | 0.2    | 1.21   |       0.0214 | 0.0014  |
|  0.4 | 0.0842 | 0.4420 | 1.4631 |       0.0918 | 0.0076  |
|  0.6 | 0.2019 | 0.7346 | 1.7682 |       0.2221 | 0.0202  |
|  0.8 | 0.3842 | 1.0883 | 2.1362 |       0.4255 |         |
| 10   | 0.6446 |        |        |       0.7183 | 0.0737  |

12. T(2/3) (3/2)1(5/3) by (25); now use interpolation in Table A2, etc.

|   Xn | Yn         |            |            | k3         | k4         | 106 X Error of yn   |
|------|------------|------------|------------|------------|------------|---------------------|
|  1   | 0.765 198  | 0.081 287  | ~0.056 989 | ~0.061 848 | ~0.034 604 |                     |
|  1.5 | 0.511 819  | ~0.034 970 | ~0.007 296 | ~0.011 250 | +0.015 740 | +9                  |
|  2   | 40.223 946 | +0.016 098 | +0.041 840 | +0.038 979 | 0.061 098  | ~55                 |
|  2.5 | ~0.048 241 | 0.061 767  | 0.080 770  | 0.079 042  | 0.092 562  | 143                 |
|  3   | ~0.259 845 | 0.093 218  | 0.102 154  | 0.101 466  | 0.104 389  | 207                 |
|  3.5 | ~0.379 914 |            |            |            |            |                     |

In the present case the errors of the two methods are of the same order of magnitude. An exact comparison is not possible since the errors sign in a different fashion in each method. change

## SECTION 19.4. Methods for Elliptic Partial Differential Equations, page 962

Purpose. To explain numerical methods for the Dirichlet problem involving the Laplace equation; the typical representative of elliptic equations:

## Main Content, Important Concepts

Elliptic, parabolic, hyperbolic equations

Dirichlet; Neumann; mixed problems

Difference analogs (7), (8) of Poisson's and Laplace' s equations

Coefficient scheme (9

Liebmann's method of solution (identical with Gauss-Seidel, Sec. 18.3)

Peaceman-Rachford' s ADI method (15)

Short Courses. Omit the ADI method.

## Comments on Content

Neumann's problem and the mixed problem follow in the next section; including the modification in the case of irregular boundaries.

The distinction between the three kinds of equations (elliptic; parabolic, hyperbolic) is not merely a formal matter because the solutions of the three types behave differently in principle; and the boundary and initial conditions are different; this necessitates different numerical methods, as we shall see.

## SOLUTIONS TO PROBLEM SET 19.4, page 969

2. 6 steps. Some results are

| [93.75   | 90.625 65.625            | (Step 2)   |
|----------|--------------------------|------------|
| [87.8906 | 87.6953 62.6953 62.5977] | (Step 4)   |
| [87.5244 | 87.5122 62.5122 62.5061] | (Step 6    |
| [87.5001 | 87.5 62.5 62.5]          |            |

(Step 10)

- 4 The values obtained by the Gauss elimination agree with those of the exact solution of the problem; u(x, y) = x3 3xy2. Gauss-Seidel would need 14 to produce 6S-values or 9 steps for 3S-values. steps
- 6 This shows the importance of starting values; it then does not take until the approximations come close to the solution. A rule of thumb is to take a rough estimate of the average of the boundary values at the points that enter the linear system. By starting from 0 we obtain good long

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

10. All the isotherms must begin and end at a corner. The diagonals are isotherms u 25, because of the data obtained and for reasons of symmetry  Hence we obtain a qualitative picture as follows.
12. (a) U1l 66
3. (b) By symmetry, we can reduce the problem to four equations in four unknowns. Solution:

Section 19.4. Problem 10

<!-- image -->

<!-- formula-not-decoded -->

Six of the boundary values are zero, and the on the upper edge are V3/2 = 0.866 025. on the right we substitute the starting values 0. With this, two Also,

<!-- formula-not-decoded -->

our four equations become

<!-- formula-not-decoded -->

The solution is from the first two equations

<!-- formula-not-decoded -->

and from the other two equations

<!-- formula-not-decoded -->

First Now come columns; for these, (14b) is step.

<!-- formula-not-decoded -->

With the boundary values and the previous solution on the right, this becomes

<!-- formula-not-decoded -->

The solution is

<!-- formula-not-decoded -->

Second Rows. We can use the previous equations; changing only the right sides: step.

Solution:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Second step. Columns. The equations with the new right sides are

<!-- formula-not-decoded -->

Final result (solution of these equations):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- the values arranged as the points in the xy-plane; is

|   160 |   170 |   157 |   110 |
|-------|-------|-------|-------|
|   138 |   145 |   125 |    75 |
|   138 |   145 |   125 |    75 |
|   160 |   170 |   157 |   110 |

Twenty steps gave accuracies of 3S-5S, with slight variations between the components of the output vector.

## SECTION 19.5. Neumann and Mixed Problems. Irregular Boundary, page 971

Purpose. Continuing our discussion of elliptic equations; we explain the ideas needed for handling Neumann and mixed problems and the modifications required when the domain is no longer a rectangle.

## Main Content, Important Concepts

Mixed problem for a Poisson equation (Example 1)

Modified stencil (6) (notation in 428)

## Comments on Content

Neumann' s problem can be handled as explained in Example 1.

In all the cases of an elliptic equation we need only one boundary condition at each point (given u or given un)

## SOLUTIONS TO PROBLEM SET 19.5, page 975

2. 0 u\_1,1) gives 2h condition on the right edge; so that the equations are (u11 U\_1,1 141

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Uo1 ~0.25, 0.75, = 2; this agrees with the values of the exact solution u(x, y) = x2 \_ y2 of the problem. 131

Exact 3D values:

4. The exact solution of the Poisson equation is u = x2y2 . The approximate solution results from Au = b, where

<!-- formula-not-decoded -->

where the six equations correspond to P1l P32, in our usual Or der. The components of b are of the form a c with a resulting from + y2) and from the boundary values; thus, 4 0 = 4 10 0 10, 20 12 = 8 10 9 = 1, 16 36 = 20, 26 81 48 = 103. The solution of this system = = = 9, U32 + 12 and = + 48 produced entries 2 in A and ~12 and ~48 in b. 2(x2

6. Exact solution u = b, where

<!-- formula-not-decoded -->

8.54733, € 243 -15.5885. The solution of this system is (exact values of u in parentheses)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

14. Let u denote the unknown boundary potential. Then v occurs in Au = b, where

<!-- formula-not-decoded -->

The solution of this linear is u [5 10 10 16]T. From this and 19 5v/19 100 (the potential at P11) we have v = 380 as the constant boundary potential on the indicated portion of the boundary . system

16. Two equations are as usual:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where the right side is due to the fact that we are with the Poisson equation. The third equation results from (6) with a = p = 9 = 1 and b = 1/2. We dealing get

<!-- formula-not-decoded -->

The first two terms are zero and ~2; these are given boundary values: There remains

<!-- formula-not-decoded -->

Our three equations for the three unknowns have the solution

<!-- formula-not-decoded -->

## SECTION 19.6. Methods for Parabolic Equations, page 976

## Content

Purpose; To show the numerical solution of the heat equation, the prototype of a para(initial temperature) and one boundary condition on each of the two vertical boundaries:

Direct method based on (5), convergence condition (6)

Crank-Nicolson method based on (8)

Special case (9) of (8)

## Comment on Content

Condition (6) restricts the size of time too much; a disadvantage that the Crank \_ Nicolson method avoids. steps

## SOLUTIONS TO PROBLEM SET 19.6, page 981

- 23.3. The other ters decrease much more rapidly and contribute practically nothing: 6 = u(1 X, 0) and the boundary conditions imply u(x, t) = u(1 t. The calculation gives
- (0, 0.2, 0.35, 0.35,0.2, 0)
- (0, 0.1875, 0.3125, 0.3125, 0.1875, 0)
- (0, 0.171875, 0.28125, 0.28125, 0.171875, 0)
- (0, 0.15625, 0.253906, 0.253906, 0.15625, 0)
- (0, 0.141602, 0.229492, 0.229492, 0.141602, 0)
- 8 We have k = 0.01. The boundary condition on the left is that the normal derivative is zero. Now if we were at an inner point; we would have; by (5),

by the central difference formula for the normal derivative (partial derivative with respect to x) we get Here,

<!-- formula-not-decoded -->

- =

so that the previous formula gives what we need,

The underlying idea is quite similar to that in Sec. 19.5. The computation gives

|      | x = 0   | x = 0.2   | 0.4    | =0.6   | 0.8    |            |
|------|---------|-----------|--------|--------|--------|------------|
| 0    |         | 0         |        |        |        |            |
| 0.01 |         |           |        |        |        | 0.5        |
| 0.02 |         |           |        |        | 0.125  | 0.866 025  |
| 0.03 |         |           | 0      | 0.031  | 0.279  |            |
| 0.04 |         | 0         | 0.008  | 0.085  | 0.397  | 0.866 025  |
| 0.05 | 0       | 0.002     |        | 0.144  | 0.437  | 0.5        |
| 0.06 | 0.001   | 0.007     | 0.049  | 0.187  | 0.379  |            |
| 0.07 | 0.004   | 0.016     | 0.073  | 0.201  | 0.236  |            |
| 0.08 | 0.010   | 0.027     | 0.091  | 0.178  | 0.043  | ~0.866 025 |
| 0.09 | 0.019   | 0.039     | 0.097  | 0.122  | ~0.601 |            |
| 0.1  | 0.029   | 0.048     | 0.089  | 0.065  | ~0.520 | ~0.866 025 |
| 0.11 | 0.039   | 0.054     | 0.040  | ~0.140 | ~0.493 | ~0.5       |
| 0.12 | 0.046   | 0.047     | ~0.002 | ~0.183 | 0.406  |            |

10. = klh? = 1, k = 1, 2 steps. The series in Sec. 11.5 gives (with L = 10, t = 2, b1 2.58012, b2 = 0, b3 = 0.09556)

<!-- formula-not-decoded -->

The values for t = 2 and x = 0, 1, 10 are (exact values in parentheses) 0 (0), 0.6691 (0.6546), 1.2619 (1.2449), 1.7212 (1.7135), 2.0075 (2.0143),2.1043 (2.1179), 2.0075 (2.0143), etc. (symmetric)

12. CAS PROJECT. u(0, t) = u(1, t) = 0, u(0.2, t) = u(0.8, t), u(0.4, t) u(0.6, t), where

Explicit CN Exact (6D)

| 0.2               |    x 0.4 |
|-------------------|----------|
| 0.587785          | 0.951057 |
| 0.393432 0.399274 | 0.636586 |
| 0.263342          | 0.646039 |
| 0.396065          | 0.640846 |
|                   | 0.426096 |
| 0.271221          | 0.438844 |
| 0.266878          | 0.431818 |
| 0.176267          | 0.285206 |
| 0.184236          | 0.2981   |
| 0.179829          | 0.29097  |
| 0.117983          | 0.190901 |
| 0.125149          | 0.202495 |
| 0.121174          | 0.196063 |
| 0.078972          | 0.127779 |
| 0.085012          | 0.137552 |
| 0.081650          | 0.132112 |

## SECTION 19.7. Methods for Hyperbolic Equations; page 982

## Comments on Content

Purpose; Explanation of the numerical solution of the wave equation; the prototype of a hyperbolic equation, on region of the same type as in the last section; subject t0 initial and boundary conditions that guarantee the uniqueness of the solution.

We now have two initial conditions (given initial displacement and given initial velocity) in contrast to the heat equation in the last section; where we had only one initial condition.

The computation by (6) is simple. Formula (8) gives the values of the first time steps in terms of the initial data.

## SOLUTIONS TO PROBLEM SET 19.7, page 984

- 2 Note that the curve of f(x) is no longer symmetric with respect to x = 0.5. The solution was required for 0 = t = 1. We present it here for a full cycle 0 = t = 2
4. By (14), Sec. 11.4, with c = 1 the left side of (6) is

|      | X = 0.2   | 0.4    | x = 0.6   | x 0.8   |
|------|-----------|--------|-----------|---------|
|  0   | 0.032     | 0.096  | 0.144     | 0.128   |
|  0.2 | 0.048     | 0.088  | 0.112     | 0.072   |
|  0.4 | 0.056     | 0.064  | 0.016     | ~0.016  |
|  0.6 | 0.016     | ~0.016 | ~0.064    | ~0.056  |
|  0.8 | 0.072     | ~0.112 | 0.088     | ~0.048  |
| 10   | 0.128     | ~0.144 | ~0.096    | 0.032   |
|  1.2 | ~0.072    | ~0.112 | ~0.088    | ~0.048  |
|  1.4 | 0.016     | ~0.016 | ~0.064    | ~0.056  |
|  1.6 | 0.056     | 0.064  | 0.016     |         |
|  1.8 | 0.048     | 0.088  | 0.112     | 0.072   |
|  2   | 0.032     | 0.096  | 0.144     | 0.128   |

<!-- formula-not-decoded -->

and the right side is the sum of the six terms

<!-- formula-not-decoded -->

Four of these six terms cancel in pairs; and the remaining expression equals the right side of (A).

6. From (13), Sec. 11.4, with c = 1 we get the exact solution

<!-- formula-not-decoded -->

From (8) we have kg; 0.1gi = 0.1 sin 0.1mi. Because of the symmetry with respect

to x 0.5 we may list only the following values (with the exact values in parentheses):

|     | x = 0.1               | 0.2                   | 0.3                   | x = 0.4               | 0.5                   |
|-----|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| 0   | 0                     |                       |                       |                       |                       |
| 0.1 | 0.030 902 (0.030 396) | 0.058 779 (0.057 816) | 0.080 902 (0.079 577) | 0.095 106 (0.093 549) | 0.100 000 (0.098 363) |
| 0.2 | 0.058 779 (0.057 816) | 0.111 804 (0.109 973) | 0.153 885 (0.151 365) | 0.180 902 (0.177 941) | 0.190 212 (0.187 098) |
| 0.3 | 0.080 902 (0.079 577) | 0.153 885 (0.151 365) | 0.211 804 (0.208 337) | 0.248 991 (0.244 914) | 0.261 804 (0.257 518) |
| 0.4 | 0.095 106 (0.093 549) | 0.180 902 (0.177 941) | 0.248 991 (0.244 914) | 0.292 706 (0.287 914) | 0.307 770 (0.302 731) |

- 8 Since u(x, 0) = f(x), the derivation is immediate. Formula (8) results if the integral equals
10. Exact solution: u(x, t) = (x + t)?. The values obtained in the computation are those tions = (0.2i)?, gi 0.2i. In connection with the left boundary condition we can use the central difference formula 121'

<!-- formula-not-decoded -->

to obtain and then (8) to compute uo1 and (6) to compute uo,j+1'

## SOLUTIONS TO CHAPTER 19 REVIEW, page 984

22. y = Computed values are

|   Xn | Yn        | y(xn)     |   Error X 106 | Error in Prob. 21   |
|------|-----------|-----------|---------------|---------------------|
| 0.01 | 1.010 000 | 1.010 050 |            50 |                     |
| 0.02 | 1.020 100 | 1.020 201 |           101 |                     |
| 0.03 | 1.030 301 | 1.030 455 |           154 |                     |
| 0.04 | 1.040 604 | 1.040 811 |           207 |                     |
| 0.05 | 1.051 010 | 1.051 271 |           261 |                     |
| 0.06 | 1.061 520 | 1.061 837 |           316 |                     |
| 0.07 | 1.072 135 | 1.072 508 |           373 |                     |
| 0.08 | 1.082 857 |           |           430 |                     |
| 0.09 | 1.093.685 | 1.094 174 |           489 |                     |
| 0.1  | 1.104 622 | 1.105 171 |           549 | 0.005 171           |

We see that the error of the last value has decreased by factor 10, approximately, due to the smaller step.

<!-- formula-not-decoded -->

| Xn   | Yn     | Error X 104   |
|------|--------|---------------|
| 0.1  | 2.8205 | 8             |
| 0.2  | 2.6790 | 15            |
|      |        | 22            |
| 0.4  | 2.5033 | 27            |
| 0.5  | 2.4662 | 32            |
| 0.6  | 2.4612 | 36            |
| 0.7  | 2.4871 | 39            |
| 0.8  | 2.5429 | 42            |
| 0.9  | 2.6276 | 44            |
| 10   | 2.7404 | ~46           |

<!-- formula-not-decoded -->

28. From y' =x + y and the given formula we get;, with h = 0.2,

<!-- formula-not-decoded -->

and from this

<!-- formula-not-decoded -->

The computed values are

|   Xn | Yn        | Error X 106   |
|------|-----------|---------------|
|  0   | 0.000 000 |               |
|  0.2 | 0.021 333 | 69            |
|  0.4 | 0.091 655 | 170           |
|  0.6 | 0.221 808 | 311           |
|  0.8 | 0.425 035 | 506           |
|  1   | 0.717 509 | 772           |

30. Solution y tan x =x + 4

|     |      Yn |   Error X 106 |
|-----|---------|---------------|
| 0.8 | 4.22969 |            52 |
| 1   | 4.55686 |          4548 |

The starting values were obtained by classical Runge-Kutta.

36. Y1 ~2e9x e32 errors of y1: ~1 X ~3 X 10-3, X errors of y2: 10-4, ~10 X 10-4, ~25 X 10-4 10-3 10-3
2. ~3.30955; y2 = 0 5.17403. Exact solution 4y12 + y22 = 16 (ellipse).

## 38. The computed values are

| Xn   | Yn         | Yn         | Yexact   | Error     | Yexact   | Error     |
|------|------------|------------|----------|-----------|----------|-----------|
| 0.0  |            |            |          |           |          |           |
| 0.1  | ~0.3       |            | ~0.299   | 0.001     | ~2.97    | 0.03      |
| 0.2  | ~0.597     | ~2.94      | ~0.592   | 0.005     | ~2.88    | 0.06      |
|      | ~0.884 985 | ~2.819 700 | ~0.873   | 0.011 985 | ~2.73    | 0.089 7   |
| 0.4  | ~1157 910  | ~2.638 796 |          | 0.021 910 |          | 0.118 796 |
| 0.5  | ~1.409 698 |            | ~1.375   | 0.034 698 | ~2.25    |           |

40. u(P11) = u(P12) 105, u(P21) = 155, u(P22) = 115

42.1.96, 7.86, 29.46

44. From the 3D-values given below we see that at each x 0 the temperature oscillates with a and a maximum amplitude that decreases with decreasing x point phase lag

|      | x = 0   | x = 0.2   | = 0.4   | 0.6    | x 0.8   | 1.0        |
|------|---------|-----------|---------|--------|---------|------------|
|      | 0       | 0         | 0       |        |         |            |
| 0.02 | 0       |           |         |        |         | 0.5        |
| 0.04 | 0       | 0         |         | 0      | 0.250   | 0.866 025  |
| 0.06 |         |           | 0       | 0.125  | 0.433   |            |
| 0.08 | 0       | 0         | 0.062   | 0.217  | 0.562   | 0.866 025  |
| 0.10 | 0       | 0.031     | 0.108   | 0.312  | 0.541   | 0.5        |
| 0.12 | 0       | 0.054     | 0.172   | 0.325  | 0.406   |            |
| 0.14 | 0       | 0.086     | 0.189   | 0.289  | 0.162   | 0.5        |
| 0.16 |         | 0.095     | 0.188   | 0.176  | ~0.105  | ~0.866 025 |
| 0.18 |         | 0.094     | 0.135   | 0.041  | ~0.345  |            |
| 0.20 |         | 0.068     | 0.067   | ~0.105 |         | ~0.866 025 |
| 0.22 |         | 0.034     | ~0.019  | ~0.206 |         | ~0.5       |
| 0.24 | 0       | ~0.009    | ~0.086  | ~0.252 | ~0.353  | 0          |

## PART F OPTIMIZATION. GRAPHS

## CHAPTER 20 Unconstrained Optimization. Linear Programming

## Major Change

The simplex method of linear programming has been completely rewritten in the spirit of matrix techniques, without making reference to other chapters (6 or 18)

## SECTION 20.1. Basic Concepts. Unconstrained Optimization; page 990

Purpose; To explain the concepts needed throughout this chapter. To discuss Cauchy' s method of steepest descent or gradient method, a popular method of unconstrained mization. opti -

## Main Content, Important Concepts

Objective function

Control variables

Constraints; unconstrained optimization

Cauchy' s method

## SOLUTIONS TO PROBLEM SET 20.1, page 993

2. f(x) = (x1 3)2 + 1)2 13. Calculation gives 4(x2
4. f(x) = 0.8(x1 + 1.4)2 + + 0.3)2 + const. 1-3 give 0.35(x2 Steps

|      X1 |       X2 |
|---------|----------|
| 3.73846 | 1.04615  |
| 3.11077 | 0.889231 |
| 3.0818  | 1.00511  |

|      X1 | X2        |
|---------|-----------|
| 1.48804 | 0.979908  |
| 1.29286 | ~0.261496 |
| 1.40147 | ~0.278573 |

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

From this,

For this t,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

From this, with X1 = 1, x2 = 1, we get successively

<!-- formula-not-decoded -->

The student should sketch this, to see that it is reasonable. The process continues indefinitely, as had to be expected.

## 8. The calculation gives for steps 1-5

| X1       | X2       |
|----------|----------|
| 1.33333  | 2.66667  |
| 3.55556  | ~1.77778 |
| 2.37037  | ~4.74074 |
| 6.32099  | 3.16049  |
| ~4.21399 | 8.42798  |

This is the beginning of a broken line of segments spiraling away from the origin. At the corner points, f is alternatingly positive and negative and increases monotone in absolute value.

10. CAS PROJECT. (c) For f(x) = X1 the values converge relatively rapidly to [0

| X1          |           |
|-------------|-----------|
| 0.410245    | ~0.589755 |
| ~0.00977922 | ~0.16973  |
| 0.007137    | ~0.152814 |
| ~0.00550786 | ~0.140169 |
| 0.00441861  | ~0.130242 |
| ~0.00364745 | ~0.122176 |

Similarly for f(x) = x4 + x24:

| X1          | X2         |
|-------------|------------|
| ~0.352941   | 0.705882   |
| ~0.249135   | ~0.124567  |
| 0.043965    | ~0.08793   |
| 0.0310341   | 0.0155171  |
| ~0.00547661 | 0.0109532  |
| ~0.00386584 | 0.00193292 |

## SECTION 20.2. Linear Programming; page 994

amples.

## Main Content, Important Concepts

Linear programming problem

Its normal form. Slack variables

Feasible solution; basic feasible solution

Optimal solution

## Comments on Content

Fhereas the function to be maximized (or minimized) by Cauchy' s method was arbitrary (differentiable) but we had no constraints; we now simply have linear objective function; but constraints; so that calculus no longer helps .

No systematic method of solution is discussed in this section; these follow in the next sections .

## SOLUTIONS TO PROBLEM SET 20.2, page 997

2. No. For instance, f = 5x1 + yields maximum f = 12 for every point on the segment AB. 2x2 profit
2. 8 The first inequality could be dropped from the problem because it does not restrict the region determined by the other inequalities: Note that that region is unbounded (stretches to infinity) This would cause a problem in maximizing an objective function with positive coefficients.
6. Ordinarily a vertex of a region is the intersection of only two straight lines given by inequalities taken with the equality sign. Here; (5, 4) is the intersection of three such lines. This may merit special attention in some cases;, as we discuss in Sec. 20.4
10. f(9, 4) = 270 + 40 = 310 is the maximum.
12. No solution because the region is unbounded

<!-- formula-not-decoded -->

14. = fmax
18. X1 = Number of = Number of days of operation of kiln II. Objective function f = 4 Constraints: days 4OOx1

<!-- formula-not-decoded -->

fmin = f(1, 3) = 2200, as can be seen from a sketch of the region in the x1x2-plane resulting from the constraints in the first quadrant:.  Operate kiln I one and kiln I three in that order. Note that the region determined by the constraints in the first quadrant of the xx2-plane is unbounded, which causes no difficulty because we minimize (not maximize) the objective function. day days filling

20. X1 units of A and x2 units of B cost f = 1.5x1 + Constraints are 2x2:

<!-- formula-not-decoded -->

From a sketch of the region we see that fmin f(3, 2) = 8.50. Hence the minimum cost diet consists of 3 units A and 2 units B.

## SECTION 20.3. Símplex Method, page 998

Purpose. To discuss the standard method of linear programming for systematically findan optimal solution by a finite sequence of transformations of matrices. ing

Normal form of the problem

Initial simplex table

Pivoting, further simplex tables (augmented matrices)

## Comment on Concepts and Method

The given form of the problem involves inequalities. By introducing slack variables we convert the problem to the normal form. This is a linear system of equations. The initial simplex table is augmented matrix. It is transformed by first selecting the column of pivot and then the row of that pivot. The rules for this are entirely different from those for pivoting in connection with the solution of a linear system of equations. The selection of a pivot is followed by a process of elimination by row operations similar to that in the Gauss-Jordan method (Sec. 6.7). This is the first step, leading to another simplex table (another augmented matrix). The next step is done by the same rules; and so on. The process comes to an end when the first row of the simplex table obtained contains no more negative entries. From this final simplex table one can read the optimal solution of the problem. its

## SOLUTIONS TO PROBLEM SET 20.3, page 1001

## 2. The normal form is

The calculation is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

800/2 400, 600/5 120, pivot 5

<!-- formula-not-decoded -->

600/2, pivot 16/5

<!-- formula-not-decoded -->

X1 = 250/5 = 50, X2 560/1 175, Zmax f(SO, 175)

4. The matrices and pivot selections are

<!-- formula-not-decoded -->

550/3 650/5, pivot 5

<!-- formula-not-decoded -->

160/8 650/4, pivot 8/5

<!-- formula-not-decoded -->

fmax 150 at X1 250/5 50, X2 160/(8/5) 100.

- 6 The matrices and pivot selections are

<!-- formula-not-decoded -->

pivot 3 in row 4

<!-- formula-not-decoded -->

pivot 2/3 in row 3

<!-- formula-not-decoded -->

780 at X1 = 21/3 7, x2 = = 3 . fmax

- 8 The matrices and pivot selections are

<!-- formula-not-decoded -->

60/4 = 15 20/1 pivot 4 20,

<!-- formula-not-decoded -->

60/5 30/3, pivot 3

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SECTION 20.4. Simplex Method: Degeneracy, Difficulties in Starting; page 1002

Purpose. To explain ways of overcoming difficulties that may arise in applying the simplex method.

## Main Content, Important Concepts

Degenerate feasible solution

Artificial variable (for overcoming difficulties in starting)

## SOLUTIONS TO PROBLEM SET 20.4, page 1007

2. In the second step in Prob. 1 we had a choice of the pivot; and in the present due to our rule of choice, we took the other pivot. The result remained the same. The calculation is prob lem,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This gives X1 = 4, X2 = 48/12 = 4, X3 = 0, X4 = 0, Xs = 0, f(4, 4) = 72

4. The calculation is as follows .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- = 4500 is the same as in the step before. But we shall now be able to reach the maximum f(10, 5) 5500 in the final step.

<!-- formula-not-decoded -->

We see that *1 20/2 = 10, X2 10/2 5, X3 = 0, X4 30/6 = 5, X5 0 = 5500.

Problem 5 shows that the extra step (which gave no increase of z = f(x)) could have been avoided if we had chosen 4 (instead of 2) as the first pivot

6. The maximum f(O, 2.4, 0) = 2.4 is obtained as follows.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

From T2 we see that X1 0/8 = 0, X2 = = = 0, X4 = 0, X5 = 0 = 12/5.

- X2: The result is ñ(2, 3) = ~1, hence fmin = 1. The calculation is as follows. An artificial variable X6 is defined by ~2x1

<!-- formula-not-decoded -->

A corresponding objective function is

<!-- formula-not-decoded -->

The corresponding matrix is

<!-- formula-not-decoded -->

From this we obtain

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

We see that X1 = 2/1 = = 6/2 = 3,x3 = 0, X4 = 0, X; = 18, 10. An artificial variable x6 is defined by

<!-- formula-not-decoded -->

and a corresponding objective function by

<!-- formula-not-decoded -->

This gives the matrix

<!-- formula-not-decoded -->

and from it

<!-- formula-not-decoded -->

and from this

<!-- formula-not-decoded -->

which still contains M.

## SOLUTIONS TO CHAPTER 20 REVIEW , page 1007

12. 9 give the solution [~1, 2] to 6s. 1-5 give steps Steps

| X1        |      X2 |
|-----------|---------|
|           | 3.77669 |
| ~0.888521 | 2.07432 |
| 1.00054   | 2.06602 |
| ~0.995857 | 2.00276 |
| 1.00002   | 2.00245 |

| X1        |       X2 |
|-----------|----------|
|           | 0.231924 |
| ~0.758212 | 1.51642  |
| 1.01056   | 1.5725   |
| ~0.941538 | 1.88308  |
| 1.00255   | 1.89664  |

Gradients (times a scalar) are obtained by calculating differences of subsequent va] ues. Orthogonality follows from the fact that we direction when we are tangent to level curve and then proceed perpendicular to it. change

14. The values obtained are

<!-- formula-not-decoded -->

## CHAPTER 21 Graphs and Combinatorial Optimization

## SECTION 21.1. Graphs and Digraphs, page 1010

Purpose. To explain the concepts of a graph and a digraph (directed graph) and related concepts; as well as their computer representations.

## Main Content; Important Concepts

Graph, vertices, edges Incidence of a vertex v with an edge; degree of v Digraph Adjacency matrix Incidence matrix Vertex incidence edge incidence list

## Comment on Content

Graphs and digraphs have become more and more important; due to an increase of sup ply and demand ~a supply of more and more powerful methods of handling graphs and digraphs; and a demand for those methods in more and more problems and fields of application. Our chapter, devoted to the modern central area of combinatorial optimization; will give us a chance to feeling for the usefulness of graphs and digraphs in general get

## SOLUTIONS TO PROBLEM SET 21.1, page 1014

10.

16. Join 01 to U2 Uns then 03 to U4, Un, etc. then take the sum 1 + 2 + . + (n 1) = 1), the number of edges you have used in that process.

<!-- image -->

|    |    | 1   | 0   | 0   | 1   |     |        |                |
|----|----|-----|-----|-----|-----|-----|--------|----------------|
|  2 | 1  |     |     |     | 0   |     | Vertex | Incident Edges |
|  3 | 0  |     |     |     |     | 20. | 2      | 'e2, e3, e1    |
|  4 |    | 0   |     |     |     |     | 3      | e2, =e3        |
|  5 |    | 0   |     | 0   |     |     |        | e4             |

## SECTION 21.2. Shortest Path Problems. Complexity, page 1015

## Main Content, Important Concepts

Purpose. To explain method (by Moore) of determining a shortest path from a given vertex to a given vertex in a graph, all of whose edges have length 1.

Moore' s algorithm (Table 21.1)

BFS (Breadth First Search), DFS (Depth First Search)

Complexity of an algorithm

Efficient; polynomially bounded

## Comment on Content

The basic idea of Moore's algorithm is quite simple: A few related ideas and problems are illustrated in the problem set.

## SOLUTIONS TO PROBLEM SET 21.2, page 1019

2. There are 3 shortest paths; of length 4 each:

<!-- image -->

Which one we obtain in backtracking depends on the numbering (not labelingl) of the vertices and on the backtracking rule. For the rule in Example 1 and the numshown in the following figure we get (B) bering

<!-- image -->

If we the rule and let the computer look for largest (instead of smallest) numbers; we get (A). change

- 4 n 1. If it had more, a vertex would appear more than once and the corresponding cycle could be omitted . One edge.
6. This is true for = 0 since then v s. Let it be true for an l ~ 1 for the predecessor U-1 of v on a shortest We claim that when labeled, v is still unlabeled (so that we shall have A(v) = wanted) . Inpath gets

8. No

12. Delete the edge (2, 4)

<!-- formula-not-decoded -->

16. Let T: s - s be a shortest postman trail and v any vertex. Since T includes each edge, to the first visit of v and T2: the other portion of T. Then the trail v consisting of T2 followed by T1 has the same length as T and solves the postman problem.

## page 1020

Purpose. This section extends the previous one to graphs whose edges have any (positive) length and explains a popular corresponding algorithm (by Dijkstra).

## Main Content, Important Concepts

Bellman' s optimality principle, Bellman's equations

Dijkstra's algorithm (Table 21.2)

## Comment on Content

Throughout this chapter; one should emphasize that algorithms are needed because most practical problems are so large that solution by inspection would fail, even if one were satisfied with approximately optimal solutions.

## SOLUTIONS TO PROBLEM SET 21.3, page 1023

2. Let j be the vertex that gave k its present label Lks namely, L; + ljk: After this label was assigned, j did not change its label, since it was then removed from $S. Next; find the vertex that gave j its permanent label, etc This backward search traces a from 1 to k, whose length is exactly Lk' path
4. The algorithm gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

6. Dijkstra' s algorithm gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The answer is (1, 3), (2, 4), (3, 5), (4, 5);

8. Dijkstra' s algorithm gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The answer is (1, 5), (2, 3), (2, 5), (4, 6), (5, 6); L6 = 7.

## SECTION 21.4. Shortest Spanning Trees. Kruskal's Greedy Algorithm, page 1024

Purpose. After the discussion of shortest between two given vertices; this section is devoted to the construction of a tree in a given graph that is spanning (contains all ver tices of the graph) and is of minimum length. paths

## Main Content, Important Concepts

```
Tree Cycle Kruskal' s greedy algorithm (Table 21.3)
```

## Comment on Content

Figure 459 illustrates that Kruskal s algorithm does not necessarily give a tree during each intermediate step, in contrast to another algorithm to be discussed in the next section.

## SOLUTIONS TO PROBLEM SET 21.4, page 1027

<!-- image -->

<!-- image -->

4 \_3

Note that trees, just as general graphs, can be sketched in different ways.

<!-- image -->

8. Order the edges in descending order of length and delete them in this order, retainan edge only if it would lead to the omission of a vertex Or to a disconnected graph. ing
2. be different. Let = (w; x) be in P1 but not in P2: Then P1 without e together with P2 is a connected graph. Hence it contains a path
10. Order the edges in descending order of length and choose them in this order, rejectan edge when a would arise. cycle ing
16. True for n 2 Assume truth for all trees with less than n vertices. Let T be a tree with n 2 2 vertices; and (u, v) an edge of T. Then T without (u, v) contains no by Prob. 14. Hence this graph is disconnected. Let G1, G2 be its connected components, having n1 and n2 vertices, hence n1 1 and n2 1 edges, respectively, by the induction hypothesis; so that G has n1 1 + n2 =n 1 edges. path
18. Extend an e into a by adding to its ends if such exist. A new edge attached at the end of the introduces a new vertex, or closes a cycle, which is impossible. This extension terminates on both sides of e, yielding two vertices of degree 1. edges path edge path

20. If G is a tree, it has no cycles, and has n 1 edges by Prob. 16. have no cycles and n 1 edges. Then G has 2 vertices of Conversely, let G degree 1 by Prob. 18. Now prove connectedness by induction. True when n = 2. Assume true for n k 1. Let G with k vertices have no cycles and k 1 edges. Omit a vertex v and its incident edge e, apply the induction hypothesis and add e and v back on.

## SECTION 21.5. Prim's Algorithm for Shortest Spanning Trees; page 1028

## Comments on Content

Purpose: To explain another algorithm (by Prim) for constructing a shortest spanning tree in a given graph whose edges have arbitrary (positive) lengths.

In contrast to Kruskal' s greedy algorithm (Sec. 21.4), Prim's algorithm gives a tree at each intermediate step.

The problem set illustrates a few concepts that can be fit into the present of ideas cycle

## SOLUTIONS TO PROBLEM SET 21.5, page 1030

2. In 2 we first select a smallest Z1j for the n 1 vertices outside U; these are 2 comparisons. 3 then requires n 2 updatings (pairwise the next round we have n 3 comparisons in 2 and n 3 comparisons). In updatings in 3 and so until we finally end up with 1 comparison and 1 updating: The sum of all these numbers is (n 2)(n 1) = O(n?). Step Step Step Step on,
6. The algorithm gives
3. 4 An algorithm for minimum spanning trees must examine each entry of the distance matrix at least once; because an not looked upon might have been one that should have been included in a shortest spanning tree. Hence, examining the relevant given information is already O(n?) work. entry

| Vertex   | Initial Label   | Relabeling   | Relabeling   | Relabeling   |
|----------|-----------------|--------------|--------------|--------------|
| 2 3      | = 6 113 =       | =3           |              |              |
| 4 5      | 15              | 134 10 15    | 10 125 = 9   | l54 = 2      |

We see that we got

<!-- formula-not-decoded -->

The tree has the length L = 15.

To visualize the effect of the algorithm; use the graph (the figure) and for each circle U and then go the "circle" and look for the shortest edge that crosses it. step along

## 8. The algorithm gives

|        | Initial   | Relabeling   | Relabeling   | Relabeling   | Relabeling   | Relabeling   | Relabeling   |
|--------|-----------|--------------|--------------|--------------|--------------|--------------|--------------|
| Vertex | Label     |              | (()          | ([)          | (IV)         |              | (VI)         |
| 2      | l12 = 3   |              |              |              |              |              |              |
| 3      | 0         | l23 = 4      |              |              |              |              |              |
|        |           |              | 134 = 3      | 164 = 1      |              |              |              |
|        |           | 0            | 135 = 5      | 135 = 5      | 135 = 5      |              |              |
| 6      |           | 126 10       | 136 = 2      |              |              |              |              |
|        |           |              | 137 = 6      | l37 = 6      | l37 = 6      | l37 =6       |              |
| 8      | l18 8     | 128          | 128 =7       | 128 =7       | 128 = 7      |              | l28 = 7      |

We see that we got

<!-- formula-not-decoded -->

The length is L = 28.

## 10. The algorithm proceeds as follows.

|        | Initial   | Relabeling   | Relabeling   | Relabeling   | Relabeling   |
|--------|-----------|--------------|--------------|--------------|--------------|
| Vertex | Label     |              |              |              |              |
| 2      | 20        | l12 20       | 132 =4       | =4 l32       |              |
| 3      |           | 153 = 6      |              |              |              |
| 4      |           | l54 12       | l34 = 2      |              |              |
| 5      | l15 =8    |              |              |              |              |
| 6      | 116 = 30  | l16 30       | 30           | 30           | 10           |

Hence we 'successively got

<!-- formula-not-decoded -->

In Prob. 6 of Sec. 21.4 we got the same edges, but in the order

12. We obtain; in this order, the tree

<!-- formula-not-decoded -->

The length is 40.

14. TEAM PROJECT. (a) e(1) = 16, €(2) = 22, €(3) 12.
2. (b) d(G) = 24, r(G) = 12 = e(3), center {3}.
3. (c) 20, 14, center {3, 4}
4. (e) Let T* be obtained from Tby deleting all endpoints (= vertices of degree 1) together with the edges to which belong. Since for fixed u, max dlu, v) oc CUrS only when v is an endpoint; €(u) is one less in T* than it is in T. Hence the vertices of minimum eccentricity in T are the same as those in T*. Thus T has the same center as T*. Delete the endpoints of T* to get a tree T** whose center is the same as that of T, etc. The process terminates when only one vertex or two adjacent vertices are left. they

- (f) Choose a vertex u and find a farthest v1 From v1 find a farthest v2. Find w such that d(w, v1) is as close as possible to being

## SECTION 21.6. Networks. Flow Augmenting Paths, page 1031

## Main Content; Important Concepts

Purpose. After shortest paths and spanning trees we discuss in this section third class of practically important problems; the optimization of flows in networks.

Network; source; target (sink)

Edge condition; vertex condition

Path in a digraph, forward edge; backward edge

Flow augmenting path

Cut set, Theorems 1 and 2

Augmenting theorem for flows path

Max-flow min-cut theorem

## Comment on Content

An algorithm for determining flow augmenting paths follows in the next section

## SOLUTIONS TO PROBLEM SET 21.6, page 1037

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

8. One is interested in flows from $ to +, not in the opposite direction
2. = = 5, A25 = 3; A13 = 4, 435 = 9 From these numbers we see that flow augmenting paths are

<!-- formula-not-decoded -->

14. Flow augmenting are paths

<!-- formula-not-decoded -->

16. The maximum flow is f = 14. It can be realized by f12 = 8, f13 = 6, f24 = 8, f43 = 4, f35 10, f4s = 4
18. The maximum flow is f = 4. It is realized by

<!-- formula-not-decoded -->

f is unique, but the way in which it is achieved is not; in general. In the present case we can change f4s from 0 to 1, f46 from 3 to 2, f56 from 1 to 2

<!-- formula-not-decoded -->

## SECTION 21.7. Ford-Fulkerson Algorithm for Maximum Flow; page 1038

Purpose: To discuss an algorithm (by Ford and Fulkerson) for systematically increasing flow in a network the zero flow) by constructing flow augmenting until the maximum flow is reached. paths

## Main Content; Important Concepts

Forward edge, backward edge

Ford-Fulkerson algorithm (Table 21.8)

Scanning of a labeled vertex

## Comment on Content

Note that this is the first section in which we are dealing with digraphs.

## SOLUTIONS TO PROBLEM SET 21.7, page 1040

2. Scanning the vertices in the order of their numbers, we a flow augmenting path get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

with At = 1, but no further flow augmenting Since the initial flow was 2, this gives the total flow f = 4. path.

4. The given flow equals 9 We first get the flow augmenting path

<!-- formula-not-decoded -->

then the augmenting path flow

<!-- formula-not-decoded -->

and finally the flow augmenting path

<!-- formula-not-decoded -->

The maximum flow is 9 + 2 + 5 + 1 = 17.

6. No. This follows from Theorem 4 in Sec. 21.6.
8. Not more work than in Example 1. Steps 1-7 are similar to those in the example and give the flow augmenting path

<!-- formula-not-decoded -->

which augments the flow from 0 to 11.

In determining a second flow augmenting we scan 1, labeling 2 and 4 and get9, 44 = 10. In scanning 2, that is, trying to label 3 and 5, we cannot label 3 because Cij C23 = fij = f23 = 11, and we cannot label 5 because fs2 = 0. In scanning 4 (ie , labeling 5) we = 7. In scanning 5 we cannot label 3 because f35 0, and we further get 46 = 3. Hence a flow augmenting is path get path with At 1 and then

<!-- formula-not-decoded -->

and At 3. Together we the maximum flow 11 4 3 = 14 because no further flow augmenting paths can be found: The result agrees with that in Example 1. get

10. The forward edges of the set are used to capacity; otherwise one able to label their other ends. Similarly for the backward would have been edges of the set; which carry no flow.
2. on those paths a flow f by f(e) = 1 on each of their Then f is maximum. Now let be obtained from G by edges that of ñ. Then; since each edge has capacity 1, there exist š carry nO portion =k edge-disjoint paths in G* edges. G* deleting
14. Since (S, T) is a cut set;, there is no directed path $ ~ t in G with the deleted . Since all edges have edges of (S, T) capacity 1, we thus obtain

<!-- formula-not-decoded -->

Now let Eo be a set of 4 edges whose deletion destroys all directed paths s t;, and Go denote G without these 9 edges. Let Vo be the set of all those vertices v in for which there is a directed Let V1 be the set of the other Go vertices in G. contains none of the has 9 edges. Now (S, T) is a minimum cut set; and all the edges have 1. Thus, capacity let path

Together, cap (S, T) = 9.

<!-- formula-not-decoded -->

## SECTION 21.8. Assignment Problems. Bipartite Matching, page 1041

Purpose. As the class of problems, in this section we explain assignment problems consists of two subsets S and T and vertices in $ are assigned (related graph tices in T. by edges) to ver last

## Main Content; Important Concepts

Bipartite graph G = (V,E) = (S, T; E)

Exposed vertex

Matching; maximum cardinality matching

Alternating path, augmenting path

Matching algorithm (Table 21.9)

## Comment on Content

few additional problems on graphs; related to the present circle of ideas as well as of a more general nature; are contained in the problem set:.

## SOLUTIONS TO PROBLEM SET 21.8, page 1045

4. = {1,4, 5, 8} Yes,
2. 2 $ = {1, 5}; T = {2, 3,4}. Just move 2 down and you see it.

6. No, as for a triangle, septangle, whereas square, hexagon, octagon, are bipartite. etc.,
2. 8.
10. (1, 4), (2, 3), (5, 7)
12. From the answer to Prob. 9 we see that as matching of cardinality 3 we can take (1, 4), (3,6), (7, 8) Addition of (2, 5) gives the desired matching of maximum cardinality 4.
5. 14

16

|    | Period   | Period   | Period   | Period   |
|----|----------|----------|----------|----------|
|    |          | 2        | 3        |          |
| T1 | C4       | C3       | C1       |          |
| T2 | C1       | C4       | C3       | C2       |
| T3 |          | C2       | C4       | C3       |

20. One might perhaps mention that the particular significance of K5 and K3,3 results from Kuratowskis theorem, stating that a graph is planar if and only if it contains no subdivision of Ks or (that is, it contains no subgraph obtained from Ks or by subdividing the edges of these graphs by introducing new vertices on them).

## SOLUTIONS TO CHAPTER 21 REVIEW, page 1046

<!-- image -->

| Vertex   | Incident Edges   |
|----------|------------------|
| 1        | e1 e3            |
| 2        |                  |
| 3        | e2, e5           |
| 4        |                  |
|          | e6               |
| 6        | e7               |

22.

24. (1, 2), (1, 4), (2, 3); L2 = 2, L3 = 5, L4 = 5
34. (1, 6), (4, 5), (2, 3), (7, 8)

## PART G. PROBABILITY AND STATISTICS

## CHAPTER 22 Data Analysis. Probability Theory

## Change

The beginning is a new section on data analysis; explaining stem-and-leaf plots  and boxplots and motivating probability by relative frequency.

## SECTION 22.1. Data: Representation; Average; Spread; page 1050

Purpose To discuss standard graphical representations of data in statistics. To introduce concepts that characterize the average size of the data values and their spread (their variability).

## Main Content, Important Concepts

Stem-and-leaf plot

Histogram

Boxplot

Absolute frequency, relative frequency

Outliers

Cumulative relative frequency

Mean

Variance; standard deviation

## Comment on Content

discussed in this section have become standard in connection with statistical methods . Average size and variability give the two most important general characterizations of data. Relative frequency will motivate probability as its theoretical counterpart : This is a main reason for presenting this material here before the beginning of our discussion of probability in this chapter. Randomness is not mentioned here because the introduction of samples (random samples) as a concept can wait until 23 when we shall need them in connection with statistical methods . The connection with this section will then be immediate and will provide no difficulty or duplication Chap.

## SOLUTIONS TO PROBLEM SET 22.1, page 1054

= = 17, qu 17.5. Not symmetric with respect to

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

14. 7 = 12.6 but qM 7. The data are not sufficiently symmetric. $ = 9.07.
18. Points to consider are the amounts of calculation; the size of the data (in using quartiles we lose information\_the larger the number of data points, the more informatry we have better agreement between quartiles on the one hand and mean and variance on the other, as in the case of data with considerable deviation from symmetry .
16. 5 xj = Xmax: Now sum over j from 1 to n. Then divide by n to get = Xmin Xmin Xmax'

## SECTION 22.2. Experiments, Outcomes, Events, page 1055

Purpose. To introduce basic concepts needed throughout 22 and 23. Chaps.

## Main Content, Important Concepts

Experiment

Sample space $, outcomes, events

Union; intersection; complements of events

Mutually exclusive events

Representation of sets by Venn diagrams

## Comment on Content

To make the chapter self-contained; we explain the modest amount of set-theoretical concepts needed in the next sections; although most students will be familiar with these matters.

## SOLUTIONS TO PROBLEM SET 22.2, page 1057

- 2.62 36 outcomes, which are ordered (1, 1), (1, 2), (6, 6), where the first number refers 'to the first die and the second number to the second die. pairs
6. A n B = S | ({RRR} U {LLL}). Yes, we cannot obtain 2 right-handed 2 left-handed screws in the same trial because we draw only 3 screws. and No,
4. Let A: Six, N Ac: No Six. Then the infinitely many outcomes are A, NA, NNA, NNNA, etc.
8. A = {(1, 1), (6, 6)}, B = {(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (3, 1)},A n B = {(1, 1) (2, 2)}, etc.
10. With the notation in Prob. 4 we have

The complement is

<!-- formula-not-decoded -->

Ec: Rolling 6 or more times to the first Six get

Section 22.2. Problem 12

<!-- image -->

14. For instance; for the first formula we can proceed as follows (see the figure) . On the right;

A U B: All except 3

<!-- formula-not-decoded -->

and the intersection of these two is

On the left,

Right side: All except 3 and 5.

<!-- formula-not-decoded -->

and the union of these two gives the same as on the right Similarly for the other formula.

Section 22.2. Problem 14

<!-- image -->

## SECTION 22.3. Probability; page 1058

Purpose. To introduce

1. Laplace' s elementary probability concept based on equally likely outcomes;

## Main Content; Important Concepts

- 2 The general probability concept defined axiomatically.

Definition 1 of probability

Definition 2 of probability

Motivation of the axioms of probability by relative frequency

Complementation rule, addition rules

Conditional probability

Multiplication rule, independent events

Sampling with and without replacement

## Comments on Content

Whereas Laplace' s definition of probability takes care of some applications and some statistical methods (for instance; nonparametric methods in Sec. 23.8), the major part of ap plications and will be based on the axiomatic definition of probability, which should thus receive the main emphasis in this section theory

Sampling with and without replacement will be discussed in detail in Sec. 22.7.

## SOLUTIONS TO PROBLEM SET 22.3, page 1063

2. Ac = {(5, 6), (6, 5), (6, 6)}, P(AC) = 3/36. Answer: 1 3/36 = 11/12
2. LR. For RR the probability decreases; whereas the other two probabilities increase. Answer: 780/870 = 0.89655 &gt; 8/9 = 0.88889
6. P = 1/6 + 1/6 + 1/6 1/36 1/36 1/36 + 1/216 = 91/216. Check by the complementation rule: 1 53/216 91/216 because each of the dice can independently show one of the numbers 1, 5, whereas 6 is out
4. 10 100 outcomes. Answer: 1 6/100 = 949
10. By the multiplication rule (Theorem 4) we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- Same as (a)

Since (a)~(c) exhaust all possibilities; these probabilities must add up to 1, which provides a way of checking results in this and similar cases.

<!-- formula-not-decoded -->

12. P4 = 0.99 gives P = 0.99749 as the probability that a single switch does not fail dur a given time interval; and the answer is the complement of this, namely, 0.259. ing
14. Drawing without replacement from the (hypothetically infinite) production that is go-on\_ The probabilities are ing
- a) 0.982 96.049
- c) 0.022 = 0.049
5. () 2 0.98 0.02 3.929

and the sum is 1.

16. We list the outcomes that favor the event whose probability we want to determine; and after each outcome the corresponding probability (F female, M = male):

$$FF 1/4$$

$$MFF 1/8$$

$$FMF 1/8$$

$$MMFF 1/16$$

$$MFMF 1/16$$

FMMF 1/16

where B and A 0 BC are disjoint because B and BC are disjoint: Hence by Axiom 3,

<!-- formula-not-decoded -->

because P(A n BC) is a probability, hence nonnegative.

This gives the answer 11/16.

## 18. We have

20. We have

<!-- formula-not-decoded -->

## SECTION 22.4. Permutations and Combinations; page 1064

## Main Content

Purpose; To discuss permutations and combinations as tools necessary for systematic counting in experiments with a number of outcomes . large

Theorems 1-3 contain the main properties of permutations and combinations we must know

Formulas (5)-(14) contain the main properties of factorials and binomial coefficients we need in practice.

## Comment on Content

The student should become aware of the surprisingly size of the numbers involved in (1)-(4), even for relatively modest numbers n of given elements; a fact that would make attempts to list cases a very impractical matter . large

## SOLUTIONS TO PROBLEM SET 22.4, page 1068

2. The 51/3! 120/6 = 20 permutations are

<!-- formula-not-decoded -->

The 10 combination without repetition are obtained from the previous list by regarding the two pairs consisting of the same two letters (in opposite orders) as equal: + 2 \_ The 2 1) = 15 combinations with repetitions consist of the 10 combinations just mentioned plus the 5 combinations

<!-- formula-not-decoded -->

- 4 In 7! = 5040 ways

<!-- formula-not-decoded -->

- 100) 8. There are 10

100 '97 ular one is 1/ Now the number of samples containing the 3 male mice is 10 because these are obtained by picking the 3 male mice and then 7 female mice from 97 97, which can be done in ways. Hence the answer is

<!-- formula-not-decoded -->

- = 120 ways
- 12 (a) 1/84, (b) 5/21
14. The complementary event (no two people have a common birthday) has probability

<!-- formula-not-decoded -->

(which can also be nicely computed by the Stirling formula). This gives the answer 419, which is surprisingly large.

- () The theorem holds when k = 1. Assuming that it holds for any fixed positive n + k k, we show that the number of combinations of (k + I)th order is From 4
16. TEAM PROJECT. (a) There are n choices for the first and we terminate with the kth for which we have n ~ k + 1 choices. thing thing

n + k the assumption it follows that there are combinations of (k + I)th order whose first element is 1 (this is the number of combinations of kth order) . n + k = 2) Then there are combinations of (k + I)th order whose first elek ment is 2 (this is the number of combinations of kth order of the n 1 elements n + k - 3 2, 3, n) Then there are combinations of (k + I)th order k whose first element is 3, etc., and, by (13),

<!-- formula-not-decoded -->

- (d) akbn-k is obtained by picking k of the n factors

<!-- formula-not-decoded -->

and choosing a from each of k factors (and b from the remaining n k factors); by Theorem 3, this can be done in ways.

- (e Apply the binomial theorem to

<!-- formula-not-decoded -->

+ b" has the coefficient on the right and 2 on the left.

## SECTION 22.5. Random Variables; Probability Distributions; page 1069

Purpose; To introduce the concepts of discrete and continuous random variables and their distributions (to be followed up by the most important special distributions in Secs. 22.7 and 22.8).

## Main Content, Important Concepts

Random variable X, distribution function F(x)

Discrete random variable; its probability function

## Comments on Content

Continuous random variable; its density

The definitions in this section are general; but the student should not be scared because the number of distributions one needs in practice is small, as we shall see.

For both kinds of random variables X the definition of the distribution function F(x) is the same, namely, F(x) = P(X = x) s0 that it permits a uniform treatment of all X For discrete X the function F(x) is piecewise constant; for continuous X it is continuous. For obtaining an impression of the distribution of X the probability function or densityissmoce useful than F(x)

Discrete random variables occur in experiments in which we count, continuous ran dom variables in experiments in which we measure.

## SOLUTIONS TO PROBLEM SET 22.5, page 1074

2. k = 1/8 because of (6) and 1 + 3 + 3 + 1 = 8
6. and 4.
3. k = 1/100 because of (6) and 1 + 8 + 27 + 64 = 100

This problem and Prob. 7 are important to the student in explaining the two basic tasks.

- 1 Find P for given x,
2. Find x for given P

in the simplest possible situation.

10. 42/90, 42/90, 6/90, 0, 48/90

<!-- formula-not-decoded -->

- 12 To have the area under the density curve equal to 1, we must have k = 5. If A denotes "Defective and B = Ac, we have

<!-- formula-not-decoded -->

s0 that about 50 of the 500 axles will be defective. This can also be seen without calculation.

14. The outcomes and their probabilities are (A: Six, B = A9)

<!-- formula-not-decoded -->

Hence the event X = x; First Six in rolling x times has the probability

<!-- formula-not-decoded -->

We can now verify (6) by applying the sum formula of the geometric series:

<!-- formula-not-decoded -->

Here x =

16. Integrating the density, we obtain the distribution function

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

About 500 of thë cans will contain 100 gallons or more because Y = 100 corresponds to X = 0 and F(O) = 0.5. Similarly, Y = 99.5 corresponds to X = ~0.5 and F(-0.5) = 0.125; this is the probability that a can will contain less than 99.5 gallons. Finally, F(-1) = 0 is the answer to the last question.

18. By differentiation;

Furthermore, that is, 559.

20. P(X = c) = P(X = b) + P(b &lt; X = c) = P(X = b) because all probabilities are nonnegative.

## SECTION 22.6. Mean and Variance of a Distribution, page 1075

of X (also called expectation of X), which measures the central location of the values of X, and the variance of X, which measures the spread of those values. 02

## Main Content;, Important Concepts

Mean @ given by (1)

Variance given by (2), standard deviation 0 02

Standardized random variable (6)

Short Courses. Mention definitions of mean and variance and go on to the special distributions in the next two sections.

## Comments on Content

Important practical applications follow in Secs: 22.7, 22.8, and later;

Moments (8) and (9) will play no great role in our further work, but would be more important in more theoretical approach on higher level We shall use them in Sec. 23.2.

The transformation theorem (Theorem 2) will be basic in Sec. 22.8 and will have var ious applications in Chap. 23.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SOLUTIONS TO PROBLEM SET 22.6, page 1078

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

8. 20.89 because for a nondefective bolt we obtain

<!-- formula-not-decoded -->

where x = 1

10. About 70

12. We are asking for the sale x such that F(x) 0.95. Integration of f(x) gives

<!-- formula-not-decoded -->

From this we get the solution 0.8646, meaning that with a probability of 959 the sale will not exceed 8646 gallons (because here we measure in ten thousands of gallons) Thus

<!-- formula-not-decoded -->

and the complementary event that the sale will exceed 8646 gallons thus has a 5% chance;

<!-- formula-not-decoded -->

and then the tank will be empty if it has a capacity of 8660 gallons.

14. He should pay the expected gain per game; which is the mean of 0.1 X, where X is the number that shows up; thus,

<!-- formula-not-decoded -->

- = E(X)

<!-- formula-not-decoded -->

where E(X) = various practical and theoretical applications.

- () g(x) = X and the definition of expectation gives the defining formula for the mean Similarly for (11). For E(l) we the sum of all possible values or the integral of the density taken over the x-axis, and in both cases the value is 1 because of (6) and (10) in Sec. 22.5. get
- (c)  E(Xk) ~ ak+l)/[(b ~ a)(k + 1)] by straightforward integration. (bk+1
- = t, write T instead of t, set T = ~t; and use f(u Then

<!-- formula-not-decoded -->

- (e) = 4/23/2 = V2
- = 5. But for distributions of interest in applications; the skewness will serve its purpose.

## SECTION '22.7. Binomial; Poisson; and Hypergeometric Distributions; page 1079

Purpose.  To introduce the three most important discrete distributions and to illustrate them by typical applications.

## Main Content, Important Concepts

Binomial distribution (2) (4)

Poisson distribution (5), (6)

Hypergeometric distribution (8)-(10)

Short Courses. Discuss the binomial and hypergeometric distributions in terms of Examples 1 and 4.

## Comments on Content

The 'symmetric case p = 9 = 1/2 of the binomial distribution with probability function (2*) is of particular practical interest:. Formulas (3) and (4) will be needed from time to time. The approximation of the binomial distribution by the normal distribution follows in the next section.

## SOLUTIONS TO PROBLEM SET 22.7, page 1083

2. 1 0.754 68.369, where 0.754 is the probability of not hitting the target in the 4 trials.
- 100) 4. f(x) = 0.04*0.5 4*e-4Ix!. Values 0.018, 0.073, 0.0.195, 0.195, 96100-~ 147,

0.156. Sum 0.784. This leaves 21.69 for the remaining x-values.

- = 0.02, 9 0.98, hence 0. = 749 9815
8. Let X be the number of customers per minute. The average number is 120/60 =2 mean 2 Waiting occurs if X &gt; 4. The probability of the complement is P(X = 4) = 0.9473 (see Table 6). Hence the answer is 1 0.9473 =
10. For this problem, the hypergeometric distribution has the probability function

The numerical values are

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

These values sum up to 1, as should. they

- 12 If a package of N = 100 items contains precisely M 10 defectives; then the probability that 10 items drawn without replacement contain no defectives is

<!-- formula-not-decoded -->

Answer: 679, 80 the method is very poor.

- 14 TEAM PROJECT. (a) In each differentiation we get a factor xj by the chain so that rule,

<!-- formula-not-decoded -->

If we now set t = 0, the exponential function becomes 1 and we are left with the definition of E(Xk) . Similarly for a continuous random variable.

- (d) By differentiation;

<!-- formula-not-decoded -->

This gives; since p + 9 = 1,

<!-- formula-not-decoded -->

From this we finally obtain thè desired result;

<!-- formula-not-decoded -->

- G(t) gives G(0) = 1 and furthermore (e)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(summation over x from 0 to n). Now

<!-- formula-not-decoded -->

Thus

Now (14), Sec. 22.4, is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(summation over k from 0 to r)

- By definition;

<!-- formula-not-decoded -->

x we have 1 and the formula gives

<!-- formula-not-decoded -->

## SECTION 22.8. Normal Distribution, page 1085

important distribution; and the practical use of the normal tables.

## Main Content, Important Concepts

Normal distribution; its density (1) and distribution function (2)

Distribution function @(z), Tables A7, A8 in Appendix 5

De Moivre-Laplace limit theorem

Short Course. Emphasis on the use of Tables A7 and A8 in terms of some of the given examples and problems.

## Comments on Content

Most important is that the student learn how to use Tables A7 and A8. Second, the student should get a feeling for the distribution of values as expressed in (6) or (7).

Bernoulli' s law of numbers is included in the problem set. large

Applications of the De Moivre-Laplace theorem follow in Chap. 23.

## SOLUTIONS TO PROBLEM SET 22.8, page 1090

2. From Table A7 in Appendix 5 we get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

4. We have

<!-- formula-not-decoded -->

Thus; from Table A8 in Appendix 5,

<!-- formula-not-decoded -->

This could be seen without calculation. Next,

<!-- formula-not-decoded -->

From the table,

<!-- formula-not-decoded -->

Finally,

<!-- formula-not-decoded -->

6. Smaller: This should help the student in qualitative thinking and an understanding of standard deviation and variance.
8. We have np = 4040 . 2 Moivre-Laplace theorem we thus obtain

<!-- formula-not-decoded -->

Hence the event actually observed has a not too small probability of occurring under

10. Applying the De Moivre-Laplace theorem; we get

<!-- formula-not-decoded -->

(The exact value is 0.583.)

12. We get the maximum load from the condition

<!-- formula-not-decoded -->

By Table A8 in Appendix 5,

<!-- formula-not-decoded -->

14. TEAM PROJECT. (c) Let e denote the exponential function in (1). Then

<!-- formula-not-decoded -->

- (d)  Proceeding as suggested; we obtain

<!-- formula-not-decoded -->

The integral over equals 27, which cancels the factor in front; and the integral over equals 1, which proves the desired result.

<!-- formula-not-decoded -->

- (e = u and dx = we obtain du,

<!-- formula-not-decoded -->

- (f) We have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

~0 B % as n -&gt; %, Hence the above probability approaches €(%o)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SECTION 22.9. Distributions of Several Random Variables, page 1091

Purpose. To discuss distributions of two-dimensional random variables, with an extension to n-dimensional random variables near the end of the section.

## Main Content, Important Concepts

Discrete two-dimensional random variables and distributions

Continuous two-dimensional random variables and distributions

Marginal distributions

Independent random variables

Addition of means and variances

Short Courses. Omit this section. (Use the addition theorems for means and variances in

## Comments on Content

The addition theorems (Theorems 1 and 3) resulting from the present material will be needed in 23; this is the main reason for the inclusion of this section. Chap.

Note well that the addition theorem for variances holds for independent random ables only. In contrast, the addition of means is true without that condition. vari-

## SOLUTIONS TO PROBLEM SET 22.9, page 1099

2. The answers are 0 and 1/32. Since the density is constant in that triangle; these results can be seen from a sketch of the triangle and the regions determined by the inequalities x &gt; &gt; 4 and x = I,y = 1, respectively, without any integrations.
4. We have to integrate f(x, y) = 1/32 over y from 0 to 8 x, where this upper integration limit follows from x + y = 8. This gives the density of the desired marginal distribution in the form

<!-- formula-not-decoded -->

- 6 By Theorem 1 the mean is 10 000 2 = 20 By Theorem 3, assuming indepen dence (which is reasonable), we find the variance 10 000 0.032 9, hence the stan dard deviation 3 grams. Note that the mean is multiplied by n 10 000, whereas the standard deviation is multiplied only by Vn 100. kg;
8. From the given distributions we obtain

<!-- formula-not-decoded -->

A pin fits the hole if X &lt; 1 and P(X &lt; 1) = 509 .

10. By Theorem 1 the mean is 105 1b. By Theorem 3, assuming independence; we get the variance 0.04 4 0.25, hence the standard deviation Vo.29 = 0.539 1b.
14. (X, Y) takes a value in A, B, C, or D (see the figure) with probability F(b1 b2), a value in A Or C value in C Or D with probability F(b1; a2), a value in C with probability F(a1 a2), hence a value in B with probability given by the right side of (2).
12. No. Whereas for the mean it is not essential that the trials are not independent and MIN (single trial) the result j nMIN (n trials) via Theorem 1, one cannot use Theorem 3 here; indeed, the variance M(N M)IN2 (single trial) does not lead to (10), Sec. 22.7. 02
16. In the continuous case; (18) is obtained from (17) by differentiation; and (17) is obtained from (18) by integration. In the discrete case the proof results from the foltheorem: Two random variables X and Y are independent if and only if the events of the form a1 &lt; X=b1 and a2 &lt; Y= b2 are independent.  This theorem can be proved as follows. From (2), Sec. 22.5, we have lowing

Section 22.9. Problem 14

<!-- image -->

In the case of independence of the variables X and Y we conclude from (17) that the expression on the right equals

Hence, by (2),

<!-- formula-not-decoded -->

versely, suppose that the events are independent for any a1 b1 a2, b2. Then

<!-- formula-not-decoded -->

9 0 and set b1 b2 = y. This yields (17), that is, X and Y are independent.

## SOLUTIONS TO CHAPTER 22 REVIEW, page 1100

<!-- formula-not-decoded -->

- = = 4.0125, s2 = 16.1
30. Xmin = X; = Sum over j from 1 to n to get Xmax'

Divide by n.

<!-- formula-not-decoded -->

32. HHH, HHT, HTH, THH, HTT, THT, TTH, TTT
34. Obviously, A € B implies A 0 B = A. Conversely, if A n B = A, then every element of A must also be in B, by the definition of intersection; hence A € B.

<!-- formula-not-decoded -->

- (d) 27, 1. Note that the sum of (b) through (e) is 220.
38. f(x) = From this and the definition of mean we first have

<!-- formula-not-decoded -->

This can be summed by the derivative of the geometric series with 9 = 2, as follows.

<!-- formula-not-decoded -->

Now multiply the last series by 9 to get q/(1 on the right, and take 9 4; then the right side equals 2 and the left side equals our series for the mean. Hence the answer is u 2

40. 68 outcomes; The 6! permutations of 1, 2, 3, 4, 5, 6 are of the desired type. Answer: 5/324 1.59

44.

46. We first need

<!-- formula-not-decoded -->

In the   further   integrations we can use the defining   integrals of   E[X ~ p)?] and E[(X p)3] or, more simply;

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and similarly,

This gives

48. 0.1587, 0.6306, 0.5, 0.4950

50. 25.71 cm, 0.0205 cm

## CHAPTER 23 Mathematical Statistics

## Changes

The first section on random sampling is new. At the end of the chapter an introduction to correlation analysis has added. been

## Main Content, Important Concepts

Population Sample Random numbers, random number generator Sample mean: 7; see (1) Sample variance see (2)

## Comments on Content

Sample mean and sample variance are the two most important parameters of a sample. 7 measures the central location of the sample values and s2 their spread (their variabil ity). Small s2 may indicate high quality of production; high accuracy of measurement, etc.

Note well that 7 and s2 will generally vary from sample to sample taken from the same conceptual distinction that should be mentioned explicitly to the students.

## SECTION 23.2. Estimation of Parameters, page 1106

Purpose. As a first statistical task we discuss methods for obtaining approximate values of unknown population parameters from samples; this is called estimation of parameters:

## Main Content, Important Concepts

Point estimate, interval estimate

Method of moments

Maximum likelihood method

## SOLUTIONS TO PROBLEM SET 23.2, page 1108

- 4 a)n is maximum if b ~a is as small as possible; that is, a equal to the smallest sample value and b equal to the largest.
6. =
8. ô = 2, =1 e-22 if x = 0 and 0 otherwise. A graph shows that the step function (the sample distribution function) approximates F(x) reasonably well. (For goodness of fit, see Sec. 23.7.) F(x)

10. The likelihood function is (we can the binomial factors) drop

The logarithm is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equating the derivative with respect to p to zero, we get

<!-- formula-not-decoded -->

Multiplication by p) gives

<!-- formula-not-decoded -->

By simplification;

The result is

## 12. The likelihood function is

The logarithm is

Differentiating and equating the derivative to zero, we get

<!-- formula-not-decoded -->

Hence the answer is

<!-- formula-not-decoded -->

14. p = 2/(7 + 6) = 2/13, by Prob. 13.

## SECTION 23.3. Confidence Intervals;, page 1109

Purpose; To obtain interval estimates ("'confidence intervals") for unknown population parameters for the normal distribution and other distributions.

## Main Content; Important Concepts

Confidence interval for J if 02 is known

Confidence interval for j if 02 is unknown t-distribution; its occurrence (Theorem 2)

Confidence interval for 02

Chi-square distribution; its occurrence (Theorem 3)

Distribution of a sum of independent normal random variables

Central limit theorem

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Comments on Content

The present methods are designed for the normal distribution; but the central limit theorem permits their extension to other distributions; provided we have available sufficiently large samples.

We see that; although our task is the development of methods for the normal distribu tion; other distributions (t and chi-square) appear in the mathematical foundation of those methods .

The theorems giving the theory underlying the present methods also serve as the theoretical basis of tests in the next section: Hence these theorems are of basic importance.

## SOLUTIONS TO PROBLEM SET 23.3, page 1117

- 2.2.576 3/V100 0.773. Length increase by 309. The shift of 7 causes corre sponding shift (3 units) of the interval.
- 4 n 8, c = 0.832, so that we obtain the confidence interval

6. Reduction of the sample size by a factor 4 corresponds to an increase of the length by a factor 2.
8. n 290 gives Llo ~ 0.3, hence L ~ 0.18, L/2 2 0.09, so that the confidence inter val is

10. n 1 4; F(c) = 0.995 gives c = 4.60. From the sample we compute

<!-- formula-not-decoded -->

12. n = 24 000, 7 = = xln 0.5005. Now the random variable

<!-- formula-not-decoded -->

is approximately normal with mean 24 and variance 24 OOOp(1 p). Estima tors are OOOp

<!-- formula-not-decoded -->

For the standardized normal random variable we get from Table A8 in Appendix 5 and @(c) = 0.995 the value

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and so that

and by division by n,

14. degrees of freedom; F(c1) = 0.025,c1 = 2.70, F(c2) = 19.02 from Table AlO. From the sample,

<!-- formula-not-decoded -->

Hence k1 = 54.5/2.70 = 20.19, k2 54.5/19.02 2.86. From Table 23.3 we thus obtain the confidence interval

<!-- formula-not-decoded -->

16. degrees of freedom; F(c1) = 0.025, C1 = 1.69, F(c2) = 0.975, c2 16.01 from Table Alo. From the sample,

<!-- formula-not-decoded -->

Hence k1 = 0.437, k2 0.046. The answer is

<!-- formula-not-decoded -->

18. By Theorem 1 in this section and by Team Project in Sec. 22.8, the distribu tion of 4X1 Xz is normal with mean 4 16 12 52 and variance 16 8 + 2 = 130. 14(g)
20. By Theorem 1, the load Z is normal with mean 4ON and variance 4N, where Nis the number of Now bags.

<!-- formula-not-decoded -->

gives the condition

<!-- formula-not-decoded -->

by Table A8. The answer is N = 49 (since N must be an integer).

## SECTION 23.4. Testing of Hypotheses; Decisions, page 1118

Purpose. Our third big task is testing of hypotheses. This section contains the basic ideas and the corresponding mathematical formalism. Applications to further tasks of testing follow in Secs. 23.5-23.8.

## Main Content, Important Concepts

Hypothesis (null hypothesis)

Alternative (alternative hypothesis) , one- and two-sided

Type I error (probability œ significance level)

Type II error (probability B; 1 B = power of a test)

Test for J with unknown 02 (Example 3)

Test for (Example 4) 02

Comparison of means (Example 5)

Comparison of variances (Example 6)

## Comment on Content

Special procedures based on the present ideas have been developed for controlthe quality of production processes (Sec. 23.5), for assessing the quality of produced goods (Sec. 23.6), for determining whether some function F(x) is the unknown distribu tion function of some population (Sec. 23.7), and for situations in which the distribution of a population need not be known in order to perform a test (Sec. 23.8) testing ling

## SOLUTIONS TO PROBLEM SET 23.4, page 1127

2. If the hypothesis p = 0.5 is true, X = Number of heads in 4040 trials is approximately normal with 2020, 02 1010 (Sec. 22.8). P(X = c) @([c 2020]/V1010) 0.95, c = 2072 2048, do not reject the hypothesis.
2. 4 Left-sided test; 02In 9/20 = 0.45. From Table A8 in Appendix 5 we obtain

Hence

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and we reject the hypothesis.

6. We obtain

<!-- formula-not-decoded -->

- = we obtain

<!-- formula-not-decoded -->

Hence we reject the hypothesis and assert that the manufacturer' s claim is justified.

12. Hypothesis Ho: not better. Alternative H1: better. Under Ho the random variable

<!-- formula-not-decoded -->

is approximately normal with mean u = np 300 and variance = npq 75. = 59 we get 02

<!-- formula-not-decoded -->

Since the observed value 310 is not greater than c, we do not reject the hypothesis. This indicates that the results obtained so far do not establish the superiority.

14. We test the hypothesis 0o2 = 25 against the alternative that 25. As in Example 4, we now get 02

<!-- formula-not-decoded -->

From Table AlO with 27 degrees of freedom and the condition

<!-- formula-not-decoded -->

Since y = 1.08,2 = 1.08 = 13.23 and the test is left-sided, we reject the hypothesis and assert that it will be less expensive to replace all the batteries simultaneously . 3.52

16. We test the hypothesis 012 = 022 against the alternative 012 &gt; 022 We proceed as in Example 6. By computation;

<!-- formula-not-decoded -->

59 and (5, 6) degrees of freedom: Table All gives 4.39. Since 5.65 is greatex, we reject the hypothesis and assert that the variance of the first population is greater than that of the second.

18. In this two-sided test we use (11), obtaining

<!-- formula-not-decoded -->

From the t-table with n1 + n2 ~ 2 = 28 degrees of freedom we obtain c2 = 2.05 reject the hypothesis and assert that the population means are different.

## SECTION 23.5. Quality Control, page 1128

Purpose. Quality control is a testing procedure performed every hour (or every half hour, etc:) in an ongoing process of production in order to see whether the process is running properly ("is under control; is producing items satisfying the specifications) or not (''is out of control) , in which case the process is halted in order to search for the trouble and remove it. These tests may concern the mean; variance; range; etc. being

## Main Content

Control chart for the mean

Control chart for the variance

## Comment on Content

Control charts have also been developed for the range, the number of defectives; the number of defects per unit; for attributes; etc. (see the problem set)

## SOLUTIONS TO PROBLEM SET 23.5, page 1132

2. 1 = 3 . 0.02/V4 = 1
2. 4 Decrease by a factor V2 = 1.41. By a factor 2.58/1.96 1.32. Hence the two operations have almost the same effect.
6. LCL = 3.5, UCL = 6.5
10. The random variable Z = Number of defectives in a sample of size n has the variance npq. Hence X = ZIn has the variance 02 = 0.04 0.96/100 0.000 384. This gives npqln?

<!-- formula-not-decoded -->

From the given values we see that the process is not in control.

14. LCL npo 2.580 UCL npo + 2.580 as follows from Theorem 1 in Sec. 23.3. Vn, Vn;
12. Choose 4 times the original sample size.

## SECTION 23.6. Acceptance Sampling; page 1133

Purpose. This is a test for the quality of a produced lot designed to meet the interests of both the producer and the consumer of the lot; as expressed in the terms listed below.

## Main Content, Important Concepts

Sampling plan, acceptance number, fraction defective

Operating characteristic curve (OC curve)

Acceptable quality level (AQL)

Rejectable quality level (RQL)

Rectification

Average outgoing quality limit (AOQL)

## Comments on Content

Basically, acceptance sampling first leads to the hypergeometric distribution; which, however; can be approximated by the simpler Poisson distribution and simple formulas resulting from it; or in other cases by the binomial distribution, which can in turn be approximated by the normal distribution. Typical cases are included in the problem set.

## SOLUTIONS TO PROBLEM SET 23.6, page 1136

2. We expect a decrease of values because of the exponential function in (3), which involves n. The probabilities are 0.9098 (down from 0.9825), 0.7358, 0.0404.
4. P(A; 0) = e + 200) from (3). From 504 we find œ and ß. For 0 = 1.59 we obtain P(A; 0.015) 96.39, hence œ 3.79 Also B = P(A; 0.075) = 55.89 , which is very poor. ~200(1
6. 300)]' 0 gives 0 = 0.054 and the value 0.028.
8. The approximation is 09(1 0)? and is fairly accurate; as the following values show:
10. From the definition of the hypergeometric distribution we now obtain

|     |   Exact (2D) |   Approximate |
|-----|--------------|---------------|
| 0   |         1    |          1    |
| 0.2 |         0.63 |          0.64 |
| 0.4 |         0.35 |          0.36 |
| 0.6 |         0.15 |          0.16 |
| 0.8 |         0.03 |          0.04 |
| 1   |         0    |          0    |

<!-- formula-not-decoded -->

This gives P(A; 0.1) = 0.72 (instead of 0.81 in Example 1) and P(A; 0.2) = 0.49 (in-

12. P(A; 0) ~208(1 + 200). [0P(A; 0]' 0 gives 8 = 0.0809, 0P(A; 0) 0.0420.

14. For 0 = 0.05 we should get P(A; 0) = 0.98. (Figure 504 illustrates this; for differ -= 100, we get np = 5 and the variance npq =5 . 0.95 = 4.75. the normal approximation of the binomial distribution; we thus obtain; with c to be determined, Using

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

From this and Table A8 we get (by interpolation)

<!-- formula-not-decoded -->

The answer is that we should choose 9 or 10 as c.

## SECTION 23.7. Goodness of Fit. X2-Test, page 1137

the previous tests for unknown parameters in known types of distributions.

## Main Content

Chi-square test

Test of normality

## Comments on Content

The present method includes many practical problems; some of which are illustrated in the problem set.

Recall that the chi-square distribution also occurred in connection with confidence intervals and in our basic section on testing

## SOLUTIONS TO PROBLEM SET 23.7, page 1140

2. Xo? = 0.4 &lt; c = 3.84. Assert that the coin is fair.
4. Xo? = 94.19 &gt; 11.07; reject:. As usual, it is interesting to see the contributions of the various terms to Xo? In the present case these vary considerably, between 1.6 and 52:

<!-- formula-not-decoded -->

6. Xo? = 8)2 + (3 = 8)2 + (8 8)2] = 6.25 &gt; 3.84 because p = (13 + 3 + 8)/600 = 49 was estimated, so that we have K - 1 1 = 1 degree of freedom. The difference between the numbers of defectives is significant.
8. The maximum likelihood estimates for the two parameters are 7 = 59.87, $ 1.504. K ~ 1 = 2 = 2 degrees  of freedom. From Table 23.10 we get the critical value 9.21 &gt; Xo? = 6.10. Accept the hypothesis that the population from which the sample was taken is normally distributed. Xo? is obtained as follows.

|       |        |   Expected | Observed   |   Terms in (1) |
|-------|--------|------------|------------|----------------|
| ~0.91 | 0.1812 |      14.31 | 14         |           0.01 |
| ~0.25 | 0.4028 |      17.51 | 17         |           0.01 |
| 0.42  | 0.6623 |      20.5  | 27         |           2.06 |
| 1.08  | 0.8608 |      15.68 | 8          |           3.76 |
|       |        |      11    |            |           0.36 |

<!-- formula-not-decoded -->

Slightly different results due t0 rounding are possible.

10. Let 50 + b be that number\_
12. K = 2 classes (dull, sharp). Expected values 10 dull, 390 sharp; 1 degree of freedom; hence

<!-- formula-not-decoded -->

Reject the claim. Two are interesting here. First; 16 dull blades (an excess of 609 over the expected value!) would not have been sufficient to reject the claim at the 59 level. Second, 49/10 contributes much more to Xo? than 49/390 does; in other applications the situation will often be qualitatively similar. things

14. TEAM PROJECT. n = 3 77 = 231.
2. (a) a; = 231/20 = = 30.14 (œ 59, 19 degrees of freedom). Accept the hypothesis.
- b) Xo2 = 13.10 &gt; c = 3.84 (œ = 59, 1 degree of freedom) Reject the hypothesis.
4. (c) Xo? = 10.62 &gt; c = 3.84 (œ 59, 1 degree of freedom). Reject the hypothesis.

## SECTION 23.8. Nonparametric Tests, page 1142

Purpose. To introduce the student to the ideas of nonparametric tests in terms of two typical examples selected from a wide variety of tests in that field

## Main Content

Median; a test for it

Trend, a test for it

## Comment on Content

Both tasks have not yet been considered in the previous sections. Another approach to trend follows in the next section.

## SOLUTIONS TO PROBLEM SET 23.8, page 1143

2. 46 + 6.(3)8 + 15 = 349 is the probability of at most 2 negative values if ñ = 0, which we do not reject.
2. 4 We 0 from the sample. Let X = Number of positive values. Under the hypothesis we get the probability drop

<!-- formula-not-decoded -->

Accordingly, we reject the hypothesis that there is no difference between A and B and assert that the observed difference is significant:.

- 6 Under the hypothesis the probability of obtaining at most 3 negative differences (80 85, 90 95, 60 75) is

<!-- formula-not-decoded -->

We reject the hypothesis and assert that B is better.

8. Let X = Number of positive values among 8 values: If the hypothesis is true; a pOSitive value is as probable as a negative value and thus has probability 1/2. Hence, un der the hypothesis the probability of getting at most 1 positive value is

<!-- formula-not-decoded -->

Hence we reject the hypothesis and assert that the is too low . setting

10. n = 5 values, with 2 transpositions; namely,

<!-- formula-not-decoded -->

s0 that from Table Al2 we obtain

<!-- formula-not-decoded -->

and we do not reject the hypothesis.

12. = 8 values, with 4 transpositions; namely,

33.4 before 31.6

35.3 before 31.6,35.0

37.6 before 36.5.

<!-- formula-not-decoded -->

Reject the hypothesis that the amount of fertilizer has no effect and assert that the yield increases with increasing amounts of fertilizer.

14. We order by increasing x Then we have 10 transpositions:

<!-- formula-not-decoded -->

Hypothesis no trend  alternative positive trend, P(T = 10) = 1.49 by Table Al2 in Appendix 5. Reject the hypothesis.

## SECTION 23.9. Regression Analysis. Fitting Straight Lines, page 1145

Purpose. This section is a short introduction to regression analysis; restricted to linear regression and involving the famous least squares principle.

## Main Content

Distinction between correlation and regression

Gauss's least squares method

Sample regression sample regression coefficient line,

Population regression coefficient, a confidence interval for it

Table Al2 gives .

## SOLUTIONS TO PROBLEM SET 23.9, page 1150

2. y = 2 0.55x
4. y = 2.99x, k = 1/2.99
6. y ~120.5 + 9.15x, y(35) 200. The negative constant 120.5 simply indicates that our linear interpolation by the least squares principle is meaningful only over relatively short interval where we can approximate the actual function y(x) by a lin-
4. = 14.9225, 14.95, k1 0.067, = 4.30 (2 degrees of freedom) from (13) and the t-table, K = 0.35197, so that the answer is

<!-- formula-not-decoded -->

10. Multiplying out the square; we get three terms, hence three sums,

<!-- formula-not-decoded -->

and the last of these three terms cancels half of the second term; giving the result.

## SECTION 23.10. Correlation Analysis, page 1150

Purpose. Correlation analysis deals with the interrelation of X and Yin a two-dimensional random variable (X, Y). This section is an introduction without proofs.

## Main Content; Important Concepts

Sample covariance

Sample correlation coefficient r

Population correlation coefficient P

Independence of X and Y implies p 0 ("uncorrelatedness")-

Two-dimensional normal distribution

If (X, Y) is normal, P = 0 implies independence of X and Y.

Test for p 0

## SOLUTIONS TO CHAPTER 23 REVIEW, page 1153

= 20.325, s2 = 2.133

28. û = 20.325, ô2 (7/8)52 3.982

30. k = 1.96

32. k = 2.576 3.2/V8 =

34. k = 2.06 7/v2 2.9 from the t-table in Appendix 5 with 24 degrees of freedom.
36. n 1 = 3 degrees of freedom; F(c1) = 0.22, 0.975, C2 = 9.35 from Table AlO in Appendix 5; hence k1 = 0.05/0.22 = 0.227,k2 = 0.05/9.35 = 0.005 F(c2)

by Table 23.3 in Sec. 23.3. The answer is

<!-- formula-not-decoded -->

38. The test is two-sided. We have 02/n 0.025, as before. Table A8 gives

<!-- formula-not-decoded -->

and 15.0 0.31 14.69 as the left endpoint of the acceptance region. Now 7 = 14.5 14.7, and we reject the hypothesis.

- 40 We proceed as in Example 3 in Sec. 23.4. The test is right-sided. From Table A9 with n 1 = 19 degrees of freedom and

<!-- formula-not-decoded -->

we get c = 2.54. From the sample we compute

<!-- formula-not-decoded -->

and reject the hypothesis.

44. Because the sample size n is finite.
2. = 376.3,j = 335.3, s12 = 1009.3, s22 = 869.3, to = 1.64 c = 2.92 (œ = 2 degrees of freedom); do not reject the hypothesis. 59,
46. = 1 (1 0)6 = 5.859,  when = 0.01. For 8 159 we obtain (1 0)6
48. We the two rods of exact length; Then we have a sample of 18. Under the hy pothesis that no adjustment is needed; longer rods and shorter rods have the same probability 2Hence the probability of getting three or fewer shorter rods is drop

<!-- formula-not-decoded -->

and we reject the hypothesis and accept the alternative.

50. y = 3.4 1.85x