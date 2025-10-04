## Chapter 1

## 1.1

- (a) One dimensional, multichannel, discrete time, and digital.
- (b) Multi dimensional, single channel, continuous-time, analog.
- (c) One dimensional, single channel, continuous-time, analog.
- (d) One dimensional, single channel, continuous-time, analog.
- (e) One dimensional, multichannel, discrete-time, digital.

## 1.2

- (a) f = 0 . 01 π 2 π = 1 200 ⇒ periodic with N p = 200.
- (c) f = 3 π 2 π = 3 2 ⇒ periodic with N p = 2.
- (b) f = 30 π 105 ( 1 2 π ) = 1 7 ⇒ periodic with N p = 7.
- (d) f = 3 2 π ⇒ non-periodic.
- (e) f = 62 π 10 ( 1 2 π ) = 31 10 ⇒ periodic with N p = 10.

## 1.3

- (a) Periodic with period T p = 2 π 5 .
- (c) f = 1 12 π ⇒ non-periodic.
- (b) f = 5 2 π ⇒ non-periodic.
- (d) cos ( n 8 ) is non-periodic; cos ( πn 8 ) is periodic; Their product is non-periodic.
- (e) cos ( πn 2 ) is periodic with period N p =4 sin ( πn 8 ) is periodic with period N p =16 cos ( πn 4 + π 3 ) is periodic with period N p =8 Therefore, x(n) is periodic with period N p =16. (16 is the least common multiple of 4,8,16).

## 1.4

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Then,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 1.5

## (a) Refer to fig 1.5-1 (b)

Figure 1.5-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 1.5-2:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 1.6

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

But T/T p = f ⇒ x ( n ) is periodic if f is rational.

- (b) If x(n) is periodic, then f=k/N where N is the period. Then,

<!-- formula-not-decoded -->

Thus, it takes k periods ( kT p ) of the analog signal to make 1 period ( T d ) of the discrete signal. (c) T d = kT p ⇒ NT = kT p ⇒ f = k/N = T/T p ⇒ f is rational ⇒ x(n) is periodic.

## 1.7

- (a) F max = 10 kHz ⇒ F s ≥ 2 F max = 20 kHz .
- (c) F=9kHz will alias to 1kHz.
- (b) For F s = 8 kHz,F fold = F s / 2 = 4 kHz ⇒ 5 kHz will alias to 3kHz.

## 1.8

- (a) F max = 100 kHz,F s ≥ 2 F max = 200 Hz .
- (b) F fold = F s 2 = 125 Hz.

<!-- formula-not-decoded -->

(c)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

1.10

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

1.11

<!-- formula-not-decoded -->

## 1.12

(a) For F s = 300 Hz ,

<!-- formula-not-decoded -->

## 1.13

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 1.14

## 1.15

- (a) Refer to fig 1.15-1. With a sampling frequency of 5kHz, the maximum frequency that can be represented is 2.5kHz. Therefore, a frequency of 4.5kHz is aliased to 500Hz and the frequency of 3kHz is aliased to 2kHz.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 1.15-1:

<!-- image -->

(b) Refer to fig 1.15-2. y(n) is a sinusoidal signal. By taking the even numbered samples, the sampling frequency is reduced to half i.e., 25kHz which is still greater than the nyquist rate. The frequency of the downsampled signal is 2kHz.

## 1.16

- (a) for levels = 64, using truncation refer to fig 1.16-1. for levels = 128, using truncation refer to fig 1.16-2. for levels = 256, using truncation refer to fig 1.16-3.

Figure 1.16-1:

<!-- image -->

Figure 1.16-3:

<!-- image -->

- (b) for levels = 64, using rounding refer to fig 1.16-4. for levels = 128, using rounding refer to fig 1.16-5. for levels = 256, using rounding refer to fig 1.16-6.

Figure 1.16-4:

<!-- image -->

Figure 1.16-6:

<!-- image -->

(c) The sqnr with rounding is greater than with truncation. But the sqnr improves as the number of quantization levels are increased.

(d)

| levels               | 64        | 128       | 256       |
|----------------------|-----------|-----------|-----------|
| theoretical sqnr     | 43 . 9000 | 49 . 9200 | 55 . 9400 |
| sqnr with truncation | 31 . 3341 | 37 . 359  | 43 . 7739 |
| sqnr with rounding   | 32 . 754  | 39 . 2008 | 44 . 0353 |

The theoretical sqnr is given in the table above. It can be seen that theoretical sqnr is much higher than those obtained by simulations. The decrease in the sqnr is because of the truncation and rounding.

## Chapter 2

## 2.1

(a)

.

<!-- formula-not-decoded -->

Refer to fig 2.1-1.

(b) After folding s(n) we have

Figure 2.1-1:

<!-- image -->

<!-- formula-not-decoded -->

After delaying the folded signal by 4 samples, we have

<!-- formula-not-decoded -->

On the other hand, if we delay x(n) by 4 samples we have

<!-- formula-not-decoded -->

Now, if we fold x ( n -4) we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(d) To obtain x ( -n + k ), first we fold x ( n ). This yields x ( -n ). Then, we shift x ( -n ) by k samples to the right if k &gt; 0, or k samples to the left if k &lt; 0. (e) Yes.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

2.2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(e)

{

x

(

n

-

1)

δ

(

n

-

3) =

. . .

0

↑

,

0

,

1

,

0

, . . .

}

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(h)

## 2.3

(a)

<!-- formula-not-decoded -->

## 2.4

Let

Since and

it follows that

The decomposition is unique. For we have

and

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

First, we prove that

2.6

(a) No, the system is time variant. Proof: If

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Then,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(3)

{

y

(

n

-

2) =

0

↑

,

0

,

1

,

0

,

0

,

0

,

0

,

-

1

<!-- formula-not-decoded -->

(5)

{

y

2

(

n

) =

0

↑

,

0

,

1

,

0

,

0

,

0

,

0

<!-- formula-not-decoded -->

The system is time invariant, but this example alone does not constitute a proof. (d) (1)

y

(

n

) =

nx

(

n

)

,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

}

,

1

-

}

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 2.7

- (a) Static, nonlinear, time invariant, causal, stable.
- (b) Dynamic, linear, time invariant, noncausal and unstable. The latter is easily proved. For the bounded input x ( k ) = u ( k ) , the output becomes

<!-- formula-not-decoded -->

since y ( n ) →∞ as n →∞ , the system is unstable.

- (c) Static, linear, timevariant, causal, stable.
- (d) Dynamic, linear, time invariant, noncausal, stable.
- (e) Static, nonlinear, time invariant, causal, stable.
- (f) Static, nonlinear, time invariant, causal, stable.
- (g) Static, nonlinear, time invariant, causal, stable.
- (h) Static, linear, time invariant, causal, stable.
- (i) Dynamic, linear, time variant, noncausal, unstable. Note that the bounded input x ( n ) = u ( n ) produces an unbounded output.
- (j) Dynamic, linear, time variant, noncausal, stable.
- (k) Static, nonlinear, time invariant, causal, stable.
- (l) Dynamic, linear, time invariant, noncausal, stable.
- (m) Static, nonlinear, time invariant, causal, stable.
- (n) Static, linear, time invariant, causal, stable.

## 2.8

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

by the linearity property of T 1 . Similarly, if

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

then by the linearity property of T 2 . Since

<!-- formula-not-decoded -->

then yields

<!-- formula-not-decoded -->

y 2 ( n ) = y ( n -2) ⇒ the system is time variant.

/negationslash

it follows that yields the output

- (b) True. For T 1 , if

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where T = T 1 T 2 . Hence T is linear.

For T 2 , if

Hence, For T 1 T 2 , if

Then,

Hence T is linear. (h) True.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Therefore, T = T 1 T 2 is time invariant.

- (d) True. Combine (a) and (b).

(c) True. T 1 is causal ⇒ v ( n ) depends only on x(k) for k ≤ n . T 2 is causal ⇒ y ( n ) depends only on v ( k ) for k ≤ n. Therefore, y ( n ) depends only on x ( k ) for k ≤ n . Hence, T is causal.

- (e) True. This follows from h 1 ( n ) ∗ h 2 ( n ) = h 2 ( n ) ∗ h 1 ( n )

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

- (f) False. For example, consider

Then,

- (g) False. For example, consider

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

T 1 is stable ⇒ v ( n ) is bounded if x ( n ) is bounded.

T 2 is stable ⇒ y ( n ) is bounded if v ( n ) is bounded .

Hence, y(n) is bounded if x(n) is bounded ⇒T = T 1 T 2 is stable.

(i) Inverse of (c). T 1 and for T 2 are noncausal ⇒T is noncausal. Example:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

which is causal. Hence, the inverse of (c) is false.

Inverse of (h): T 1 and/or T 2 is unstable, implies T is unstable. Example:

<!-- formula-not-decoded -->

But T : y ( n ) = x ( n ) , which is stable. Hence, the inverse of (h) is false.

2.9

(a)

<!-- formula-not-decoded -->

For a BIBO system, lim n →∞ | h ( n ) | = 0 . Therefore,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(b) Let x ( n ) = x o ( n ) + au ( n ) , where a is a constant and x o ( n ) is a bounded signal with lim n →∞ x o ( n ) = 0 .

<!-- formula-not-decoded -->

clearly, ∑ n x 2 o ( n ) &lt; ∞⇒ ∑ n y 2 o ( n ) &lt; ∞ (from (c) below) Hence,

<!-- formula-not-decoded -->

Then,

and, thus, lim n →∞ y ( n ) = a ∑ n k =0 h ( k ) = constant. (c)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

But

Therefore,

For a BIBO stable system,

Hence,

## 2.10

The system is nonlinear. This is evident from observation of the pairs

<!-- formula-not-decoded -->

If the system were linear, y 2 ( n ) would be of the form

<!-- formula-not-decoded -->

because the system is time-invariant. However, this is not the case.

## 2.11

since

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

But this is not the case.

<!-- formula-not-decoded -->

and the system is linear, the impulse response of the system is

<!-- formula-not-decoded -->

If the system were time invariant, the response to x 3 ( n ) would be

<!-- formula-not-decoded -->

## 2.12

- (a) Any weighted linear combination of the signals x i ( n ) , i = 1 , 2 , . . . , N .
- (b) Any x i ( n -k ), where k is any integer and i = 1 , 2 , . . . , N .

## 2.13

A system is BIBO stable if and only if a bounded input produces a bounded output.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where | x ( n -k ) | ≤ M x . Therefore, | y ( n ) | &lt; ∞ for all n, if and only if

## 2.14

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

If h ( k ) = 0 for k &lt; 0, then

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

On the other hand, if y ( n ) = 0 for n &lt; 0, then

<!-- formula-not-decoded -->

## 2.15

<!-- formula-not-decoded -->

/negationslash

(b) For M = 0 , | a | &lt; 1, and N →∞ ,

<!-- formula-not-decoded -->

2.16

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

## 2.17

(a)

<!-- formula-not-decoded -->

- (b) By following the same procedure as in (a), we obtain

<!-- formula-not-decoded -->

- (c) By following the same procedure as in (a), we obtain

<!-- formula-not-decoded -->

- (d) By following the same procedure as in (a), we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 2.18

(a)

(b)

<!-- formula-not-decoded -->

## 2.19

<!-- formula-not-decoded -->

Therefore,

## 2.20

- (a) 131 x 122 = 15982

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) 1.31 x 12.2 = 15.982.
- (e) These are different ways to perform convolution.

## 2.21

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 2.22

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) y 2 ( n ) and y 4 ( n ) are smoother than y 1 ( n ) , but y 4 ( n ) will appear even smoother because of the smaller scale factor.
- (d) System 4 results in a smoother output. The negative value of h 5 (0) is responsible for the non-smooth characteristics of y 5 ( n )

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We can express the unit sample in terms of the unit step function as δ ( n ) = u ( n ) -u ( n -1). Then,

<!-- formula-not-decoded -->

Using this definition of h ( n )

## 2.24

If produces the output

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Hence, the system is linear. If the input is x ( n -1), we have

<!-- formula-not-decoded -->

Hence, the system is time variant. If x ( n ) = u ( n ), then | x ( n ) | ≤ 1. But for this bounded input, the output is

<!-- formula-not-decoded -->

which is unbounded. Hence, the system is unstable.

## 2.25

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 2.26

With x(n) = 0, we have

<!-- formula-not-decoded -->

## 2.27

Consider the homogeneous equation:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The characteristic equation is

<!-- formula-not-decoded -->

Hence,

The particular solution to

Thus, and, therefore,

The total solution is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Substitute this solution into the difference equation. Then, we obtain

<!-- formula-not-decoded -->

For n = 2,

<!-- formula-not-decoded -->

Therefore, the total solution is

<!-- formula-not-decoded -->

To determine c 1 and c 2 , assume that y ( -2) = y ( -1) = 0. Then,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 2.28

Fig. 2.28-1 shows the transient response, y zi ( n ), for y ( -1) = 1 and the steady state response, y zs ( n ).

<!-- image -->

Figure 2.28-1:

<!-- formula-not-decoded -->

## 2.29

Then

Hence,

Therefore,

The total solution is

<!-- formula-not-decoded -->

The characteristic equation is

Hence, λ = 4 , -1 and

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Since 4 is a characteristic root and the excitation is

<!-- formula-not-decoded -->

we assume a particular solution of the form

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

. For n = 2 ,

<!-- formula-not-decoded -->

The total solution is

<!-- formula-not-decoded -->

To solve for c 1 and c 2 , we assume that y ( -1) = y ( -2) = 0. Then,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

From 2.30, the characteristic values are λ = 4 , -1 . Hence

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This yields, c 1 = 6 5 and c 2 = -1 5 . Therefore,

<!-- formula-not-decoded -->

When x ( n ) = δ ( N ) , we find that

Hence,

## 2.32

<!-- formula-not-decoded -->

- (b) Partial overlap from left:

<!-- formula-not-decoded -->

Full overlap: low N 1 + M 2 high N 2 + M 1

Partial overlap from right:

(c)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Partial overlap from left: n = -3 n = -1 L 1 = -3

<!-- formula-not-decoded -->

Partial overlap from right: n = 4 n = 6 L 2 = 6

<!-- formula-not-decoded -->

The characteristic equation is

(b)

<!-- formula-not-decoded -->

The characteristic equation is

λ = 1 2 , 1 5 Hence,

With x ( n ) = δ ( n ) , we have

<!-- formula-not-decoded -->

The step response is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

λ = 0 . 2 , 0 . 4 Hence,

<!-- formula-not-decoded -->

With x ( n ) = δ ( n ) , the initial conditions are

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The step response is

<!-- formula-not-decoded -->

## 2.34

<!-- formula-not-decoded -->

By continuing this process, we obtain

<!-- formula-not-decoded -->

## 2.35

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

First, we determine

2.37

2.38

<!-- formula-not-decoded -->

For x ( n ) = u ( n +5) -u ( n -10), we have the response

<!-- formula-not-decoded -->

From figure P2.33,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

h ( n ) = a n u ( n ) . The response to u ( n ) is

<!-- formula-not-decoded -->

## 2.40

We may use the result in problem 2.36 with a = 1 2 . Thus,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 2.41

(a)

(b)

2.42

(a)

(b) No.

2.43

(a) x ( n ) δ ( n -n 0 ) = x ( n 0 ) . Thus, only the value of x ( n ) at n = n 0 is of interest. x ( n ) ∗ δ ( n -n 0 ) = x ( n -n 0 ) . Thus, we obtain the shifted version of the sequence x ( n ). (b)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(a) s ( n ) = -a 1 s ( n -1) -a 2 s ( n -2) -. . . -a N s ( n -N ) + b 0 v ( n ) . Refer to fig 2.44-1. (b) v ( n ) = 1 b 0 [ s ( n ) + a 1 s ( n -1) + a 2 s ( n -2) + . . . + a N s ( n -N )] . Refer to fig 2.44-2

Figure 2.44-1:

<!-- image -->

Figure 2.44-2:

<!-- image -->

<!-- formula-not-decoded -->

2.45

2.46

(a) Refer to fig 2.46-1

(b) Refer to fig 2.46-2

## 2.47

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 2.46-1:

<!-- image -->

<!-- formula-not-decoded -->

Figure 2.46-2:

<!-- image -->

<!-- formula-not-decoded -->

(e) from part(a), h ( n ) = 0 for n &lt; 0 ⇒ the system is causal.

<!-- formula-not-decoded -->

## 2.48

<!-- formula-not-decoded -->

(c) b = 1 -a in both cases.

2.49

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Let us first consider the response of the sytem

<!-- formula-not-decoded -->

to x ( n ) = δ ( n ) . Since y (0) = 1, it folows that c = 1. Then, the impulse response of the original system is

<!-- formula-not-decoded -->

- (b) The inverse system is characterized by the difference equation

<!-- formula-not-decoded -->

Refer to fig 2.49-1

## 2.50

<!-- formula-not-decoded -->

Figure 2.49-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

2.51

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(c)

<!-- formula-not-decoded -->

(d) All three systems are IIR.

(e)

## 2.52

<!-- formula-not-decoded -->

(b) The only question is whether

<!-- formula-not-decoded -->

For c 0 = 0 , the quadratic has a real solution if and only if

<!-- formula-not-decoded -->

2.53

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

## 2.54

(a)

<!-- formula-not-decoded -->

## 2.55

Obviously, the length of h ( n ) is 2, i.e.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 2.56

## 2.58

From problem 2.57,

With y (0) = 1 , y (1) = 3 , we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

From (2.5.9) we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The particular solution is

By substituting (2.5.10) for y ( n ) and (A) into (2.5.6), we obtain L.H.S = R.H.S.

## 2.57

<!-- formula-not-decoded -->

Substituting this solution into the difference equation, we obtain

<!-- formula-not-decoded -->

For n = 2 , k (1 + 4 + 4) = 2 ⇒ k = 2 9 . The total solution is

<!-- formula-not-decoded -->

From the initial condtions, we obtain y (0) = 1 , y (1) = 2. Then,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 2.60

Let h ( n ) be the impulse response of the system

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

2.61

The range of non-zero values of γ xx ( l ) is determined by which implies

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For a given shift l , the number of terms in the summation for which both x ( n ) and x ( n -l ) are non-zero is 2 N +1 -| l | , and the value of each term is 1. Hence,

For γ xy ( l ) we have

## 2.62

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

we observe that y ( n ) = x ( -n +3), which is equivalent to reversing the sequence x ( n ). This has not changed the autocorrelation sequence.

## 2.63

## 2.64

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Therefore, the normalized autocorrelation is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) γ xx ( l ) has peaks at l = 0 , ± k 1 , ± k 2 and ± ( k 1 + k 2 ). Suppose that k 1 &lt; k 2 . Then, we can determine γ 1 and k 1 . The problem is to determine γ 2 and k 2 from the other peaks.
- (c) If γ 2 = 0, the peaks occur at l = 0 and l = ± k 1 . Then, it is easy to obtain γ 1 and k 1 .

## 2.65

- (a) The shift at which the crosscorrelation is maximum is the amount of delay D.
- (b) variance = 0.01. Refer to fig 2.65-1.
- (b) Delay D = 20. Refer to fig 2.65-1.
- (c) variance = 0.1. Delay D = 20. Refer to fig 2.65-2.
- (d) Variance = 1. delay D = 20. Refer to fig 2.65-3.
- (e) x ( n ) = {-1 , -1 , -1 , +1 , +1 , +1 , +1 , -1 , +1 , -1 , +1 , +1 , -1 , -1 , +1 } . Refer to fig 2.65-4.
- (f) Refer to fig 2.65-5.

Figure 2.65-1: variance = 0.01

<!-- image -->

Figure 2.65-3: variance = 1

<!-- image -->

Figure 2.65-5:

<!-- image -->

## 2.66

- (a) Refer to fig 2.66-1.
- (b) Refer to fig 2.66-2.

<!-- image -->

--&gt; n

Figure 2.66-1:

- (c) Refer to fig 2.66-3.

(d) The step responses in fig 2.66-2 and fig 2.66-3 are similar except for the steady state value after n=20.

Figure 2.66-2:

<!-- image -->

Figure 2.66-3:

<!-- image -->

## 2.67

Refer to fig 2.67-1.

Figure 2.67-1:

<!-- image -->

## Chapter 3

3.1

(a)

<!-- formula-not-decoded -->

3.2

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and

∑

a

-

n

z

-

n

=

ROC:

z

|

∞

n

=0

1

(1

1

a

z

-

)

|

1

a

<!-- formula-not-decoded -->

-

|

|

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

1

2

&gt;

(c)

(d)

(e)

(g)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The pole-zero patterns are as follows:

- (a) Double pole at z = 1 and a zero at z = 0.
- (b) Poles at z = a and z = 1 a . Zeros at z = 0 and z = 1 2 ( a + 1 a ).
- (d) Double poles at z = ae jw 0 and z = ae -jw 0 and zeros at z = 0, z = ± a .
- (c) Pole at z = -1 2 and zero at z = 0.
- (e) Double poles at z = ae jw 0 and z = ae -jw 0 and zeros are obtained by solving the quadratic

<!-- formula-not-decoded -->

- (f) Poles at z = re jw 0 and z = ae -jw 0 and zeros at z = 0, and z = rcos ( w 0 -φ ) /cosφ .
- (g) Triple pole at z = 1 3 and zeros at z = 0 and z = 1 3 . Hence there is a pole-zero cancellation so

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

that in reality there is only a double pole at z = 1 3 and a zero at z = 0. (h) X ( z ) has a pole of order 9 at z = 0. For nine zeros which we find from the roots of

<!-- formula-not-decoded -->

Note the pole-zero cancellation at z = 1 2 .

3.3

<!-- formula-not-decoded -->

The ROC is 1 3 &lt; | z | &lt; 2. (b)

<!-- formula-not-decoded -->

The ROC is 1 3 &lt; | z | &lt; 2. (d)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The ROC is 1 2 &lt; | z | &lt; 3.

3.4

<!-- formula-not-decoded -->

(b)

(c)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

From formula (9) in table 3.3 with a = -1,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(f)

## 3.5

<!-- formula-not-decoded -->

The term ∑ -1 n = n 0 x r ( n ) z -n converges for all z except z = ∞ . The term ∑ ∞ n =0 x r ( n ) z -n converges for all | z | &gt; r 0 where some r 0 . Hence X r ( z ) converges for r 0 &lt; | z | &lt; ∞ when n 0 &lt; 0 and | z | &gt; r 0 for n 0 &gt; 0

<!-- formula-not-decoded -->

The first term converges for some | z | &lt; r l . The second term converges for all z , except z = 0. Hence, X l ( z ) converges for 0 &lt; | z | &lt; r l when n 0 &gt; 0, and for | z | &lt; r l when n 0 &lt; 0.

Finite-Duration Two-sided sequence : x ( n ) = 0 , n &gt; n 0 and n &lt; n 1 , where n 0 &gt; n 1

<!-- formula-not-decoded -->

The first term converges everywhere except z = ∞ .

<!-- formula-not-decoded -->

The second term converges everywhere except z = 0. Therefore, X ( z ) converges for 0 &lt; | z | &lt; ∞ .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

3.7

3.8

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

3.9

y ( n ) = x ( n ) e jw 0 n . From the scaling theorem, we have Y ( z ) = X ( e -jw 0 z ). Thus, the poles and zeros are phase rotated by an angle w 0 .

3.10

3.11

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

3.12

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 3.14

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(e)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(g)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(i)

## 3.15

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

(b)

<!-- formula-not-decoded -->

3.17

3.18

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(c)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

3.19

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 3.20

<!-- formula-not-decoded -->

Zero at z = 0 and poles at z = re ± jw 0 = r ( cosw 0 ± jsinw 0 ). (b)

<!-- formula-not-decoded -->

(c) X 1 ( z ) and X 2 ( z ) differ by a constant, which can be determined by giving the value of X 1 ( z ) at z = 1.

## 3.21

Assume that the polynomial has real coefficients and a complex root and prove that the complex conjugate of the root will also be a root. Hence, let p ( z ) be a polynomial and z 1 is a complex root. Then,

<!-- formula-not-decoded -->

The complex conjugate of (1) is

<!-- formula-not-decoded -->

Therefore, z ∗ 1 is also a root.

## 3.22

<!-- formula-not-decoded -->

Convolution property:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

3.24

(a)

(b)

<!-- formula-not-decoded -->

partial check: x (0) = 1 , x (1) = 0 . 5016 , x (2) = -0 . 3476 , x ( ∞ ) = 0. From difference equation, x ( n ) -0 . 5 x ( n -1) + 0 . 6 x ( n -2) = δ ( n ) we obtain, x (0) = 1 , x (1) = 0 . 5 , x (2) = -0 . 35 , x ( ∞ ) = 0.

3.25

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 3.26

3.27

## 3.28

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Conjugation property:

3.29

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where the radius of the contour c is r c &gt; | a | . For n &lt; 0, let w = 1 z . Then,

<!-- formula-not-decoded -->

where the radius of c ′ is 1 r c . Since 1 r c &lt; | a | , there are no poles within c ′ and, hence x ( n ) = 0 for n &lt; 0.

## 3.30

x ( n ) = x ( N -1 -n ) , since x ( n ) is even. Then

<!-- formula-not-decoded -->

If we substitute z -1 for z and multiply both sides by z -( N -1) we obtain

<!-- formula-not-decoded -->

Hence, X ( z ) and X ( z -1 ) have identical roots. This means that if z 1 is root (or a zero) of X ( z ) then 1 z 1 is also a root. Since x ( n ) is real, then z ∗ 1 must also be a root and so must 1 z ∗ 1

## 3.31

From the definition of the Fibonacci sequence, y ( n ) = y ( n -1) + y ( n -2) , y (0) = 1 . This is equivalent to a system described by the difference equation y ( n ) = y ( n -1) + y ( n -2) + x ( n ) ,

where x ( n ) = δ ( n ) and y ( n ) = 0 , n &lt; 0. The z-transform of this difference equation is Y ( z ) = z -1 Y ( z ) + z -2 Y ( z ) = X ( z ) Hence, for X ( z ) = 1 , we have

<!-- formula-not-decoded -->

## 3.32

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Therefore, (a) and (b) are equivalent systems.

## 3.33

<!-- formula-not-decoded -->

Both x 1 ( n ) and x 2 ( n ) have the same autocorrelation sequence. Another sequence is obtained from X ( z -1 ) = 1 1 -az

<!-- formula-not-decoded -->

We observe that x 3 ( n ) has the same autocorrelation as x 1 ( n ) and x 2 ( n )

3.35

(a) h ( n ) = ( 1 3 ) n u ( n ) H ( z ) = 1 1 -1 3 z -1 x ( n ) = ( 1 2 ) n cos πn 3 u ( n ) X ( z ) = 1 -1 4 z -1 1 -1 2 z -1 + 1 4 z -2 Y ( z ) = H ( z ) X ( z ) = 1 -1 4 z -1 (1 -1 3 z -1 )(1 -1 2 z -1 + 1 4 z -2 ) = 1 7 1 -1 3 z -1 + 6 7 (1 -1 4 z -1 1 -1 2 z -1 + 1 4 z -2 + 3 √ 3 7 √ 3 4 z -1 1 -1 2 z -1 + 1 4 z -2 Therefore, y ( n ) = [ 1 7 ( 1 3 ) n + 6 7 ( 1 2 ) n cos πn 3 + 3 √ 3 7 ( 1 2 ) n sin πn 3 ] u ( n ) (b) h ( n ) = ( 1 2 ) n u ( n ) H ( z ) = 1 1 -1 2 z -1 x ( n ) = ( 1 3 ) n u ( n ) + ( 1 2 ) -n u ( -n -1)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(c)

<!-- formula-not-decoded -->

Therefore,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Therefore,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 3.36

## 3.37

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

⇒ System is stable

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Since the poles of H ( z ) are inside the unit circle, the system is stable (poles at z = 1 2 , 1 4 ).

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

H ( z ) has zeros at z = 0 , 1, and poles at z = 1 ± j 2 . Hence, the system is stable.

<!-- formula-not-decoded -->

(d)

<!-- formula-not-decoded -->

Triple pole on the unit circle ⇒ the system is unstable.

Step Response:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

⇒ zeros at z = 0, poles at p 1 = 1 2 , p 2 = 2 5 system is stable.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

zeros at z = 0 , 2, and poles at z = 1 2 , 1 5 . Hence, the system is stable.

Impulse Response: X ( z ) =

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

3.39

<!-- formula-not-decoded -->

Zero at

(b)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

1, Poles at

-

<!-- formula-not-decoded -->

= 2

,

1

1

p

p

∗

<!-- formula-not-decoded -->

All poles and zeros are rotated by π 3 in a counterclockwise direction. The ROC for X 2 ( z ) is the same as the ROC of X ( z ).

## 3.40

,

and

z

= 0.

z

z

=

<!-- formula-not-decoded -->

(a)

<!-- formula-not-decoded -->

(c) Refer to fig 3.40-1.

(d) The poles of the system are inside the unit circle. Hence, the system is stable.

Figure 3.40-1:

<!-- image -->

<!-- formula-not-decoded -->

## 3.41

Refer to fig 3.41-1.

<!-- image -->

Figure 3.41-1:

<!-- formula-not-decoded -->

3.42

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) Determine the response caused by the initial conditions and add it to the response in (b).

<!-- formula-not-decoded -->

## 3.43

<!-- formula-not-decoded -->

## 3.44

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(b)

<!-- formula-not-decoded -->

- (c) Let us compute the zero-input response and add it to the response in (b). Hence,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where A,B and C are determined from the equations

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

3.46

<!-- formula-not-decoded -->

- (c) y ( n ) = -0 . 8 y ( n -1) + Cx ( n ) -1 . 5 √ 3 Cx ( n -1) + 2 . 25 Cx ( n -2). Refer to fig 3.46-1.
- (b) The poles are inside the unit circle, so the system is stable.

3.47

<!-- formula-not-decoded -->

Figure 3.46-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) Since both x 1 ( n ) and x 2 ( n ) are causal, the one-sided and two-sided transform yield identical results. Thus,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By convolution,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By one-sided z-transform,

<!-- formula-not-decoded -->

- (d) Both x 1 ( n ) and x 2 ( n ) are causal. Hence, both types of transform yield the same result, i.e,

<!-- formula-not-decoded -->

## 3.48

## 3.49

(a)

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(c)

<!-- formula-not-decoded -->

3.50

If h ( n ) is real, even and has a finite duration 2 N +1, then (with M = 2 N +1)

<!-- formula-not-decoded -->

with M = 2 N +1, the expression becomes

<!-- formula-not-decoded -->

Now, suppose z 1 is a root of H ( z ), i.e.,

<!-- formula-not-decoded -->

This implies that H ( 1 z 1 ) = 0 since we again have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) The system can be causal if the ROC is z &gt; 3, but it cannot be stable.

<!-- formula-not-decoded -->

| |

(1) The system can be causal; (2) The system can be anti-causal; (3) There are two other noncausal responses.The corresponding ROC for each of these possibilities are :

ROC 1 : | z | &gt; 3; ROC 2 : | z | &lt; 3; ROC 3 : 1 2 &lt; | z | &lt; 2; ROC 4 : 2 &lt; | z | &lt; 3;

## 3.52

x ( n ) is causal. (a)

<!-- formula-not-decoded -->

(b)(i) X ( z ) = ( z -1 2 ) 4 ( z -1 3 ) 3 ⇒ lim z →∞ X ( z ) = ∞⇒ x ( n ) is not causal.

(iii) X ( z ) = ( z -1 3 ) 2 ( z -1 2 ) 3 ⇒ lim z →∞ X ( z ) = 0. Hence X ( z ) can be associated wih a causal sequence.

(ii) X ( z ) = (1 -1 2 z -2 ) 2 1 -1 3 z -1 ⇒ lim z →∞ X ( z ) = 1 Hence X ( z ) can be associated wih a causal sequence.

## 3.53

The answer is no. For the given system h 1 ( n ) = a n u ( n ) ⇒ H 1 ( z ) = 1 1 -az -1 , | a | &lt; 1 . This system is causal and stable. However when h 2 ( n ) = a n u ( n +3) ⇒ H 2 ( z ) = a -3 z 3 1 -az -1 the system is stable but is not causal.

## 3.54

Initial value theorem for anticausal signals: If x ( n ) is anticausal, then x (0) = lim z → 0 X ( z )

<!-- formula-not-decoded -->

## 3.55

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

H

(

z

) has zeros at

z

<!-- formula-not-decoded -->

= 0

,

1 and a pole at

z

=

1

3

.

- (c) The system is not causal, but it is stable since the pole is inside the unit circle.
- (b) h ( n ) = 81 δ ( n +2) -54 δ ( n +1) -18( 1 3 ) n u ( n )

## 3.56

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By continuing this process, we find that x ( n ) = 0 for n &lt; 0. (b)

<!-- formula-not-decoded -->

For n ≥ 0, there are no poles enclosed in c and, hence, x ( n ) = 0. For n &lt; 0, we have

<!-- formula-not-decoded -->

(c)

For n &lt; 0 , we let w 1

(d)

Alternatively, we may change variables by letting w = z -1 . Then,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where the radius of the contour c is greater than | z | = 1 2 . Then, for n ≥ 0

<!-- formula-not-decoded -->

## 3.58

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Chapter 4

## 4.1

(a) Since x a ( t ) is periodic, it can be represented by the fourier series

<!-- formula-not-decoded -->

/negationslash

Hence, the spectrum of x a ( t ) consists of spectral lines of frequencies k τ , k = 0 , ± 1 , ± 2 , . . . with amplitude | c k | and phases c k .

(b) P x = 1 τ ∫ τ 0 x 2 a ( t ) dt = 1 τ ∫ τ 0 A 2 sin 2 ( πt τ ) dt = A 2 2 (c) The power spectral density spectrum is | c k | 2 , k = 0 , ± 1 , ± 2 , . . . . Refer to fig 4.1-1. (d) Parseval's relation

<!-- formula-not-decoded -->

<!-- image -->

Figure 4.1-1:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

4.2

(a)

Refer to fig 4.2-1

Figure 4.2-1:

<!-- image -->

<!-- formula-not-decoded -->

(b)

Refer to fig 4.2-2

## 4.3

(a) Refer to fig 4.3-1.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Alternatively, we may find the fourier transform of

<!-- formula-not-decoded -->

/negationslash

/negationslash

<!-- formula-not-decoded -->

Figure 4.2-2:

<!-- image -->

Figure 4.3-1:

<!-- image -->

Then,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

(c) From (a) and (b), we have c k = 1 T p X a ( k T p )

4.4

(a)

<!-- formula-not-decoded -->

4.5

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

4.6

(a)

Hence,

Similarly,

Hence,

Therefore,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

/negationslash

/negationslash

/negationslash

<!-- formula-not-decoded -->

where c 1 k is the DTFS coefficients of cos 2 πn 3 and c 2 k is the DTFS coefficients of sin 2 πn 5 . But

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(c) x ( n ) = cos 2 πn 3 sin 2 πn 5 = 1 2 sin 16 πn 15 -1 2 sin 4 πn 15 . Hence, N = 15. Following the same method as in (b) above, we find that

(d)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

/negationslash

(e)

(f)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

N

c

k

c

0

c

1

c

2

c

3

c

4

=

=

=

=

=

=

=

=

=

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

5

1

5

1

5

2

5

2

5

2

5

2

5

2

5

2

5

Therefore,

4

n

x

=0

[

∑

1 +

e

-

cos

(

cos

(

cos

(

cos

(

cos

(

πk

5

π

5

)

n

e

j

-

2

πk

5

)

)

2

π

5

3

π

5

4

π

5

e

e

-

)

2

j

πnk

5

]

jπk

5

-

jπ

5

e

)

e

)

e

-

-

-

j

2

5

j

3

5

j

4

5

(

π

π

π

4.7

(a)

<!-- formula-not-decoded -->

(c)

4.8

(a)

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

/negationslash

<!-- image -->

<!-- formula-not-decoded -->

Therefore, the fourier transform does not exist. (f)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

4.10

(a)

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

4.11

4.12

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(c)

<!-- formula-not-decoded -->

## 4.13

## 4.14

/negationslash

- (a) X (0) = n x ( n ) = -1 (b) X ( w ) = π for all w 1 π π (d)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

4.16

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 4.15-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 4.17

<!-- formula-not-decoded -->

Now, suppose that holds. Then

<!-- formula-not-decoded -->

(f)

4.18

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Then,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(b)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 4.18-1:

<!-- image -->

4.20

4.21

<!-- formula-not-decoded -->

(a)

(b)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(c)

(d)

## 4.23

(a) Y 1 ( w ) = ∑ n y 1 ( n ) e -jwn = ∑ n,n even x ( n ) e -jwn The fourier transform Y 1 ( w ) can easily be obtained by combining the results of (b) and (c). (b)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Refer to fig 4.23-1. (c)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 4.23-1:

<!-- image -->

<!-- formula-not-decoded -->

We now return to part(a). Note that y 1 ( n ) may be expressed as

<!-- formula-not-decoded -->

Hence, Y 1 ( w ) = Y 2 (2 w ). Refer to fig 4.23-2.

Figure 4.23-2:

<!-- image -->

<!-- image -->

## Chapter 5

## 5.1

- (a) Because the range of n is ( -∞ , ∞ ), the fourier transforms of x ( n ) and y ( n ) do not exist. However, the relationship implied by the forms of x ( n ) and y ( n ) is y ( n ) = x 3 ( n ). In this case, the system H 1 is non-linear.
- (b) In this case,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Note however that the system may also be nonlinear, e.g., y ( n ) = x 3 ( n ).

(c) and (d). Clearly, there is an LTI system that produces y ( n ) when excited by x ( n ), e.g. H ( w ) = 3, for all w , or H ( π 5 ) = 3.

(e) If this system is LTI, the period of the output signal would be the same as the period of the input signal, i.e., N 1 = N 2 . Since this is not the case, the system is nonlinear.

## 5.2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Refer to fig 5.2-1

Figure 5.2-1:

<!-- image -->

<!-- formula-not-decoded -->

(b) (1)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

--&gt; w

Figure 5.4-1:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

--&gt; w

Figure 5.4-2:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 5.4-3:

<!-- image -->

Figure 5.4-4:

<!-- image -->

Figure 5.4-5:

<!-- image -->

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

Figure 5.4-6:

<!-- image -->

--&gt; w

Figure 5.4-7:

<!-- formula-not-decoded -->

Figure 5.4-8:

<!-- image -->

<!-- formula-not-decoded -->

Refer to fig 5.4-9. (j)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

--&gt; w

Figure 5.4-9:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

Figure 5.4-10:

<!-- image -->

--&gt; w

Figure 5.4-11:

<!-- image -->

--&gt; w

Figure 5.4-12:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Refer to fig 5.4-14.

5.5

(a)

Refer to fig 5.5-1. (b)

Figure 5.4-13:

<!-- image -->

Figure 5.4-14:

<!-- image -->

<!-- image -->

--&gt; w

Figure 5.5-1:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Transient Response:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

(c) Note that H ( π 2 ) = 2 and H ( π 4 ) = 0. Therefore, the filter does not pass the signal cos ( π 4 n ).

<!-- formula-not-decoded -->

5.9

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

5.10

(a)

<!-- formula-not-decoded -->

Figure 5.10-1:

<!-- image -->

Refer to fig 5.10-2. (c)

<!-- formula-not-decoded -->

Refer to fig 5.10-3.

<!-- image -->

Figure 5.10-2:

<!-- image -->

--&gt; w

Figure 5.10-3:

## 5.12

<!-- formula-not-decoded -->

- (c) The filter is lowpass.

<!-- formula-not-decoded -->

- (d) For | H ( w 0 ) | 2 = 1 2 ⇒ w 0 = 3 . 036. This filter is a highpass filter.

## 5.13

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) for f 0 = 1 96 , refer to fig 5.13-1 for f 0 = 1 32 , refer to fig 5.13-2 1
- (c) for f 0 = 1 96 , refer to fig 5.13-4 for f 0 = 1 32 , refer to fig 5.13-5 1

for f 0 = 256 , refer to fig 5.13-3

for f 0 = 256 , refer to fig 5.13-6

The total harmonic distortion(THD) reduces as the number of terms in the Taylor approximation is increased.

Figure 5.13-1:

<!-- image -->

Figure 5.13-2:

<!-- image -->

Figure 5.13-3:

<!-- image -->

Figure 5.13-4:

<!-- image -->

Figure 5.13-5:

<!-- image -->

## 5.14

(a) Refer to fig 5.14-1

(b)

f

0

=

1

50

Figure 5.14-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 5.13-6:

<!-- image -->

## 5.15

(a) Refer to fig 5.15-1 (b) Refer to fig 5.15-2

<!-- image -->

The response of the system to x i ( n ) can be seen from fig 5.15-3

<!-- image -->

<!-- image -->

/negationslash

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

5.17

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.18

(a)

Refer to fig 5.18-1. (b)

Figure 5.17-1:

<!-- image -->

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

(c) The filter blocks the frequency at w = π 2 .

## 5.19

<!-- formula-not-decoded -->

5.20

<!-- formula-not-decoded -->

y ( n ) = x 2 ( n ) This is a non-linear, time-invariant system

<!-- formula-not-decoded -->

Figure 5.18-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 5.20-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.21

<!-- formula-not-decoded -->

- (b) Yes. Refer to fig 5.21-1

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 5.21-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(a)

Refer to fig 5.22-1. (b)

<!-- formula-not-decoded -->

Figure 5.21-2:

<!-- image -->

Figure 5.22-1:

<!-- image -->

5.23

(a)

(b) Let

Then, and

5.24

(a)

/negationslash

/negationslash

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(b)

(c)

## 5.25

Refer to fig 5.25-1.

## 5.26

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.27

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.28

<!-- formula-not-decoded -->

Figure 5.25-1:

<!-- image -->

<!-- formula-not-decoded -->

- (d) Refer to fig 5.28-3.
- (e) Refer to fig 5.28-4.

obviously, this is a highpass filter. By selecting b = -1, the frequency response of the highpass filter is improved.

## 5.29

Figure 5.27-1:

<!-- image -->

filter is causal, it is also stable. Refer to fig 5.28-2. (c)

<!-- formula-not-decoded -->

The maximum occurs at w = 0. Hence,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Direct form I:

<!-- image -->

## Direct form II :

Figure 5.28-1:

<!-- image -->

Figure 5.28-2:

<!-- image -->

Figure 5.28-3:

<!-- image -->

Figure 5.28-4:

<!-- image -->

<!-- formula-not-decoded -->

5.30

Refer to fig 5.30-1

5.31

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

5.32

<!-- formula-not-decoded -->

Figure 5.30-1:

<!-- image -->

5.33

<!-- formula-not-decoded -->

Figure 5.32-1:

<!-- image -->

The filter in (b) provides somewhat better smoothing because of its sharper attenuation at the high frequencies.

## 5.34

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The corresponding analog frequencies are kF s 9 , k = 1 , 2 , 3 , 4, or 1 9 kHz, 2 9 kHz, 3 9 kHz, 4 9 kHz.

## 5.35

Refer to fig 5.35-1.

Figure 5.35-1:

<!-- image -->

5.36

<!-- formula-not-decoded -->

Hence proved. (b)

Hence proved. (c)

<!-- formula-not-decoded -->

Hence proved. (d) Refer to fig 5.36-1.

5.37

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 5.36-1:

<!-- image -->

(a)

Hence proved. (b)

Hence proved. (c)

Hence proved.

## 5.38

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

/negationslash

(c)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (e) Refer to fig 5.38-1.

Figure 5.38-1:

<!-- image -->

<!-- formula-not-decoded -->

By comparing the results of (a) and (b), we find that cosw 2 &gt; cosw 1 and, hence w 2 &lt; w 1 Therefore, the second filter has a smaller 3dB bandwidth.

## 5.40

5.41

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(b)Refer to fig 5.41-1.

(c)

<!-- formula-not-decoded -->

use the coupled-form oscillator shown in figure 5.38 and multiply the two outputs by cos Θ and sin Θ, respectively, and add the products, i.e.,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 5.41-1:

<!-- image -->

<!-- formula-not-decoded -->

## 5.42

- (a) poles: p 1 , 2 = re ± jw jw 0
- 0 zeros: z 1 , 2 = e ±

(b) For w = w 0 , H ( w 0 ) = 0 For w = w 0 , the poles and zeros factors in H ( w ) cancel, so that H ( w ) = 1. Refer to fig 5.42-1. (c)

/negationslash

<!-- formula-not-decoded -->

Figure 5.42-1:

<!-- image -->

<!-- formula-not-decoded -->

- (d) Refer to fig 5.42-2. (e)

In the vicinity of w = w , we have

<!-- formula-not-decoded -->

## 5.43

For the sampling frequency F s = 500samples/sec., the rejected frequency should be w 1 = 2 π ( 60 100 ) = 6 25 π . The filter should have unity gain at w 2 = 2 π ( 200 500 ) = 4 5 π . Hence,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.44

From (5.4.22) we have,

<!-- formula-not-decoded -->

Figure 5.42-2:

<!-- image -->

<!-- formula-not-decoded -->

5.45

5.46

5.47

## 5.48

Refer to fig 5.48-1. y 1 ( n ) = Acosnw 0 u ( n ) , y 2 ( n ) = Asinnw 0 u ( n )

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.49

- (a) Replace z by z 8 . We need 8 zeros at the frequencies w = 0 , ± π 4 , ± π 2 , ± 3 π 4 , π Hence,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(b) Zeros at 1 , e ± j π 4 , e ± j π 2 , e ± j 3 π 4 , -1 Poles at a 1 8 , a 1 8 e ± j π 4 , a 1 8 e ± j π 2 , a 1 8 e ± j 3 π 4 , -1. Refer to fig 5.49-1. (c)

/negationslash

<!-- formula-not-decoded -->

Figure 5.48-1:

<!-- image -->

Refer to fig 5.49-2.

## 5.50

We use F s /L = 1cycle/day. We also choose nulls of multiples of 1 14 = 0 . 071, which results in a narrow passband of k ± 0 . 067. Thus, M +1 = 14 or, equivalently M = 13

Figure 5.49-1:

<!-- image -->

Figure 5.49-2:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Hence, we need two delays and four multiplies per output point.

## 5.52

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

5.54

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) H ( z ) as given above.

(c) Refer to fig 5.54-1. The filter designed is not a good approximation of the desired response.

5.55

<!-- formula-not-decoded -->

(b) y ( n ) = x ( n -1) -jnx ( n ). the system is unstable and time-variant.

## 5.56

Hence,

Figure 5.54-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.57

y ( n ) = x ( n ) -x ( n ) ∗ h ( n ) = [ δ ( n ) -h ( n )] ∗ x ( n ) The overall system function is 1 -H ( z ) and the frequency response is 1 -H ( w ). Refer to fig 5.57-1.

Figure 5.57-1:

<!-- image -->

## 5.58

(a) Since X ( w ) and Y ( w ) are periodic, it is observed that Y ( w ) = X ( w -π ). Therefore, y ( n ) = e jπn x ( n ) = ( -1) n x ( n ) (b) x ( n ) = ( -1) n y ( n ).

## 5.59

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(c) Since the impulse response is complex, a real input signal produces a complex-valued output signal. For the output to be real, the bandpass filter should have a complex conjugate pole.

## 5.60

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

(b) D consists of two terms, both of which are positive. For | H ( w ) | = 0, D is minimized by selecting Θ( w ) = 0, in which case the second term becomes zero.

## 5.61

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Therefore f ( a ) is maximum at a = 1 and decreases monotonically as a → 0. Consequently, w 3 increases as a → 0. (d)

<!-- formula-not-decoded -->

The 3-dB bandwidth increases as a → 0.

## 5.62

Refer to fig 5.62-1.

## 5.63

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 5.62-1:

<!-- image -->

Zero at z = -1 and a pole at z = 0. The system is stable. (b)

<!-- formula-not-decoded -->

Zero at z = 1 and a pole at z = 0. The system is stable. (c)

<!-- formula-not-decoded -->

Three zeros at z = -1 and three poles at z = 0. The system is stable.

## 5.64

<!-- formula-not-decoded -->

Refer to fig 5.64-1.

Figure 5.64-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Refer to fig 5.64-2.

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

## 5.65

<!-- formula-not-decoded -->

6 th order pole at z = 0. Refer to fig 5.65-1.

- (b)Refer to fig 5.65-2.
- (c) H in ( z ) = z 6 z 6 0 . 95 . r = (0 . 95) 1 6 . Refer to fig 5.65-3.

-(d)Refer to fig 5.65-4.

Figure 5.64-2:

<!-- image -->

Figure 5.65-1:

<!-- image -->

Figure 5.65-2:

<!-- image -->

Figure 5.65-3:

<!-- image -->

Figure 5.65-4:

<!-- image -->

(a)

(b)

<!-- formula-not-decoded -->

5.67

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

From H ( z ) , the difference equation is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.68

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.69

<!-- formula-not-decoded -->

The roots(zeros) are 0 . 8084 ± j 0 . 3370 , -0 . 3750 ± j 0 . 6074 , -1 . 0 , -0 . 7667 All the roots of H ( z

- All the roots of H ( z ) are inside the unit circle. Hence, the system is minimum phase.

) are inside the unit circle. Hence, the system is minimum phase. (b) h ( n ) = { 5 , 4 , -3 , -4 , 0 , 2 , 1 } H ( z ) = 5 + 4 z -1 -3 z -2 -4 z -3 +2 z -5 + z -6 The roots(zeros) are 0 . 7753 ± j 0 . 2963 , -0 . 4219 ± j 0 . 5503 , -0 . 7534 ± j 0 . 1900

## 5.70

The impulse response satisfies the difference equation

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

It is apparent that the coefficients { a n } can be determined if we know the order N and the values h (0) , h (1) , . . . , h ( N ). If we do not know the filter order N, we cannot determine the { a n } .

## 5.71

h ( n ) = b 0 δ ( n ) + b 1 δ ( n -D ) + b 2 δ ( n -2 D ) (a) If the input to the system is x ( n ), the output is y ( n ) = b 0 x ( n )+ b 1 x ( n -D )+ b 2 x ( n -2 D ). Hence, the output consists of x ( n ), which is the input signal, and the delayed signals x ( n -D ) and x ( n -2 D ). The latter may be thought of as echoes of x ( n ).

(b)

<!-- formula-not-decoded -->

## 5.72

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(c) If | b 0 + b 2 | &lt;&lt; | b 1 | , then the dominant term is b 1 e -jwD and

<!-- formula-not-decoded -->

and | H ( w ) | has maxima and minima at w = ± D π, k = 0 , 1 , 2 , . . . (d) The phase Θ( w ) is approximately linear with a slope of -D .

- Refer to fig 5.71-1.

Figure 5.71-1:

<!-- image -->

k

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By solving these equations recursively, we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.73

x ( n ) is a real-valued, minimum-phase sequence. The sequence y ( n ) must satisfy the conditions, y (0) = x (0) , | y ( n ) | = | x ( n ) | , and must be minimum phase. The solution that satisfies the condition is y ( n ) = ( -1) n x ( n ). The proof that y ( n ) is minimum phase proceeds as follows:

<!-- formula-not-decoded -->

This preserves the minimum phase property since a factor (1 -αz -1 ) → (1 + αz -1 )

## 5.74

Consider the system with real and even impulse response h ( n ) = { 1 4 , 1 , 1 4 } and frequency response H ( w ) = 1 + 1 2 cosw . Then H ( z ) = z -1 ( 1 4 z 2 + z + 1 4 ). The system has zeros at z = -2 ± √ 3. We observe that the system is stable, and its frequency response is real and even. However, the inverse system is unstable. Therefore, the stability of the inverse system is not guaranteed.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

But H b ( w ) = 2 Re { H ( w ) } is a zero-phase system.

## 5.76

(a) Correct. The zeros of the resulting system are the combination of the zeros of the two systems. Hence, the resulting system is minimum phase if the inividual system are minimum phase. (b) Incorrect. For example, consider the two minimum-phase systems.

<!-- formula-not-decoded -->

-3 -

<!-- formula-not-decoded -->

## 5.77

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.78

<!-- formula-not-decoded -->

- (a) There are four different FIR systems with real coefficients:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

H ( z ) is the minimum-phase system. (b)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Clearly, h 3 ( n ) is minimum phase and h 2 ( n ) is maximum phase.

## 5.79

- (a) The new system function is H ′ ( z ) = H ( λ -1 z )

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

If p k is a pole of H ( z ), then λp k is a pole of H ′ ( z ). Hence, λ &lt; 1 | p max | is selected then | p k λ | &lt; 1 for all k and, hence the system is stable. (b) y ( n ) = -∑ N k =1 a k λ k y ( n -k ) = x ( n )

## 5.80

- (a) The impulse response is given in pr10fig 5.80-1.
- (b) Reverberator 1: refer to fig 5.80-2.

Figure 5.80-1:

<!-- image -->

Figure 5.80-2:

<!-- image -->

Reverberator 2: refer to fig 5.80-2.

- (c) Unit 2 is a better reverberator.
- (d) For prime number of D 1 , D 2 , D 3 , the reverberations of the signal in the different sections do not overlap which results in the impulse response of the unit being more dense.
- (e) Refer to fig 5.80-3.
- (f) Refer to fig 5.80-4 for the delays being prime numbers.

## 5.81

- (a) Refer to fig 5.81-1.
- (b) Refer to fig 5.81-2.

<!-- image -->

Figure 5.81-2:

<!-- image -->

<!-- formula-not-decoded -->

- (b) Refer to fig 5.82-1.
- (c) It satisfies the objectives but this filter is not recommended in a practical application because

Figure 5.82-1:

<!-- image -->

in a speech application linear phase for the filter is desired and this filter does not provide linear phase for all frequencies.

## 5.83

Refer to fig 5.83-1. Practical:

Theoretical:

## 5.84

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For r very close to 1, the theoretical and practical values match.

Figure 5.83-1:

<!-- image -->

<!-- formula-not-decoded -->

H ap( z ) has a flat magnitude response. To get a flat magnitude response for the system, connect a system which is the inverse of H min ( z ), i.e.,

<!-- formula-not-decoded -->

- (b) Refer to fig 5.84-1 and fig 5.84-2.

<!-- image -->

270

Figure 5.84-1:

<!-- image -->

Figure 5.84-2:

<!-- image -->

## Chapter 6

## 6.1

- (a) Fourier transform of dx a ( t ) /dt is ˆ X a ( F ) = j 2 πFX a ( F ), then F s ≥ 2 B
- (c) Fourier transform of x a (2 t ) is ˆ X a ( F ) = 2 X a ( F/ 2), then F s ≥ 4 B
- (b) Fourier transform of x 2 a ( t ) is ˆ X a ( F ) = X a ( F ) ∗ X a ( F ), then F s ≥ 4 B
- (d) Fourier transform of x a ( t ) cos(6 πBt ) is ˆ X a ( F ) = 1 2 X a ( F +3 B ) + 1 2 X a ( F -3 B ) resulting in F L = 2 B and F H = 4 B . Hence, F s = 2 B
- (d) Fourier transform of x a ( t ) cos(7 πBt ) is ˆ X a ( F ) = 1 2 X a ( F +3 . 5 B ) + 1 2 X a ( F -3 . 5 B ) resulting in F L = 5 B/ 2 and F H = 9 B/ 2. Hence, k max = /floorleft F H B /floorright = 2 and F s = 2 F H /k max = 9 B/ 2

## 6.2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 6.3

Since filter cut-off frequency, F c = 102 . 5, then terms with | n | /T p &gt; F c will be filtered resulting

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Sampling this signal with Fs = 1 /T = 1 / 0 . 005 = 200 = 20 /T p results in aliasing

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where a = e -T . Define x 1 ( n ) = a n u a ( n ). The Fourier transform of x 1 ( n ) is

<!-- formula-not-decoded -->

Using the differentiation in frequency domain property of the Fourier transform

<!-- formula-not-decoded -->

- (b) The Fourier transform of x a ( t ) is

<!-- formula-not-decoded -->

Fig. 6.4-1(a) shows the original signal x a ( t ) and its spectrum X a ( F ). Sampled signal x ( n ) and its spectrum X ( F ) are shown for F s = 3 Hz and F s = 1 Hz in Fig. 6.4-1(b) and Fig. 6.4-1(c), respectively.

(c) Fig. 6.4-2 illustrates the reconstructed sugnal ˆ x a ( t ) and its spectrum for F s = 3 Hz and F s = 1 Hz.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 6.5

The Fourier transfrom of y ( t ) = ∫ t -∞ x ( τ ) dτ is

Then,

<!-- formula-not-decoded -->

Figure 6.4-1:

<!-- image -->

Figure 6.4-2:

<!-- image -->

(a) B = F 2 -F 1 is the bandwidth of the signal. Based on arbitrary band positioning for first-order sampling,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

6.7

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Combining A and D , and B and C , we obtain,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We observe that a ( t ) = B + C and b ( t ) = A + D . Q.E.D.

6.8

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

3. The linear interpolator is defined as

<!-- formula-not-decoded -->

Taking the Fourier transform, we obtain

<!-- formula-not-decoded -->

Fig. 6.8-1 shows magnitude and phase responses of the ideal interpolator (dashed-dotted line), the linear interpolator (dashed line), and the sample-and-hold interpolator (solid line).

6.9

<!-- formula-not-decoded -->

(b)

- (c) Refer to fig 6.9-1
- (d) Refer to fig 6.9-2
- (e) Aliasing occurs at F s = 10Hz.

## 6.10

<!-- formula-not-decoded -->

<!-- image -->

F

Figure 6.8-1:

<!-- formula-not-decoded -->

Figure 6.9-1:

<!-- image -->

Figure 6.9-2:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The output y 1 ( t ) is basically the square of the input signal y a ( t ). For the second system,

<!-- image -->

x 2 ( t ) X ( w ) X ( w ), the bandwidth is basically 2 B . The spectrum of the sampled signal is

Figure 6.12-3: a ↔ ∗

given in fig 6.12-3.

(b)

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

6.13

6.14

<!-- formula-not-decoded -->

If

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Substituting a = -j 2 πf

Then,

<!-- formula-not-decoded -->

6.16

(a)

<!-- formula-not-decoded -->

Figure 6.15-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 6.17

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Refer to fig 6.17-1.

Figure 6.17-1:

<!-- image -->

## 6.18

Let P d denote the power spectral density of the quantization noise. Then (a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Thus, SQNR will increase by 3dB if F s is doubled.

(b) The most efficient way to double the sampling frequency is to use a sigma-delta modulator.

## 6.19

<!-- formula-not-decoded -->

6.20

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(c)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(b) N analog sinusoids can be generated. There are N possible different starting phases.

6.22

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 6.23

- (a) Refer to fig 6.23-1.
- (b) Refer to fig 6.23-2.
- (c) Refer to fig 6.23-3. The first order hold interpolator performs better than the zero order interpolator because the frequency response of the first order hold is more closer to the ideal interpolator than that of the zero order hold case.
- (d) Refer to fig 6.23-4.
- (e) Refer to fig 6.23-5. Higher order interpolators with more memory or cubic spline interpolators would be a better choice.

Figure 6.23-1:

<!-- image -->

Figure 6.23-2:

<!-- image -->

<!-- image -->

Figure 6.23-5:

<!-- image -->

(a) x p ( t ) = ∑ ∞ n = -∞ x a ( t -nT s ) is a periodic signal with period T s . The fourier coefficients in a fourier series representation are

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(b) Let

<!-- formula-not-decoded -->

/negationslash

- (c) If T &lt; 2 τ , there will be aliasing in every period of x p ( t ). Hence, x a ( t ) = x p ( t ) w ( t ) and consequently, x a ( t ) cannot be recovered from x p ( t ).

<!-- formula-not-decoded -->

## Chapter 7

## 7.1

Since x ( n ) is real, the real part of the DFT is even, imaginary part odd. Thus, the remaining points are { 0 . 125 + j 0 . 0518 , 0 , 0 . 125 + j 0 . 3018 }

7.2

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

= { 4 , 1 -j 2 . 4142 , 0 , 1 -j 0 . 4142 , 0 , 1 + j 0 . 4142 , 0 , 1 + j 2 . 4142 } similarly, X 2 ( k ) = { 1 . 4966 , 2 . 8478 , -2 . 4142 , -0 . 8478 , -0 . 6682 , -0 . 8478 , -2 . 4142 , 2 . 8478 } DFT of x 1 ( n ) 8 © x 2 ( n ) = X 1 ( k ) X 2 ( k ) = { 5 . 9864 , 2 . 8478 -j 6 . 8751 , 0 , -0 . 8478 + j 0 . 3512 , 0 , -0 . 8478 -j 0 . 3512 , 0 , 2 . 8478 + j 6 . 8751 }

For sequences of part (b)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 7.3

- ˆ x ( k ) may be viewed as the product of X ( k ) with

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

F ( k ) represents an ideal lowpass filter removing frequency components from ( k c + 1) 2 π N to π . Hence ˆ x ( n ) is a lowpass version of x ( n ).

7.4

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(c)

<!-- formula-not-decoded -->

7.5

(a)

(b)

<!-- formula-not-decoded -->

7.6

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

7.7

7.8

7.9

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

7.11

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

7.12

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

7.13

(a)

<!-- formula-not-decoded -->

7.14

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Solving yields sequence

.

## 7.15

Define H 1 ( z ) /triangle = H -1 ( z ) and corresponding time signal h 1 ( n ). The use of 64-pt DFTs of y ( n ) and h 1 ( n ) yields x ( n ) = y ( n ) 64 © h 1 ( n ) whereas x ( n ) requires linear convolution. However we can simply recognize that

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 7.16

<!-- formula-not-decoded -->

g ( . ) represents a close approximation to an inverse system, but not an exact one.

7.17

/negationslash

<!-- formula-not-decoded -->

## 7.19

Call the two real even sequences x e 1 ( . ) and x e 2 ( . ), and the odd ones x o 1 ( . ) and x o 2 ( . ) (a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The DFT of the four sequences can be computed using the results of part (a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Therefore, y ( . ) is a periodic sequence with period N. So

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(d) X 3 (0) and X 4 (0), because sin ( N k ) = 0.

7.20

<!-- formula-not-decoded -->

If k is even, W k 2 = 1 , and X ( k ) = 0 (b) If k is odd, W k 2 = -1 , Therefore,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 7.21

(a) F s ≡ F N = 2 B = 6000 samples/sec (b)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 7.22

## 7.23

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(e)

(f)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(h)

7.24

(a)

7.25

(a)

(b)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This is apparent from the fact that v ( n ) is one period (0 ≤ n ≤ 7) of a periodic sequence obtained by repeating x ( n ).

## 7.26

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Hence, x ( n ) is periodic with period N, i.e.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(a)

(b)

<!-- formula-not-decoded -->

## 7.28

(a) Refer to fig 7.28-1.

(b)

<!-- image -->

- (c) Refer to fig 7.28-1.
- (d) Refer to fig 7.28-1.

∑

<!-- image -->

---&gt; n

Figure 7.28-2:

Figure 7.28-3:

<!-- image -->

7.29 Refer to fig 7.29-1. The time domain aliasing is clearly evident when N=20.

## 7.30

<!-- formula-not-decoded -->

## 7.31

(a) c k = { 2 π , -1 π , 2 3 π , -1 2 π . . . } (b) Refer to fig 7.31-1. The DFT of x ( n ) with N = 128 has a better resolution compared to one with N = 64.

<!-- formula-not-decoded -->

Figure 7.29-1:

<!-- image -->

7.32

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 7.30-1:

<!-- image -->

<!-- formula-not-decoded -->

Larger N ⇒ narrower main lobe of | Y ( w ) | . T 0 in Y ( j Ω) has the same effect. (d)

<!-- formula-not-decoded -->

- (e) The frequency samples 2 π N k fall on the zeros of Y ( w ). By increasing the sampling by a factor of two, for example, we will obtain a frequency sample between the nulls.

<!-- formula-not-decoded -->

Figure 7.31-1:

<!-- image -->

## Chapter 8

## 8.1

Since ( e j 2 π N k ) N = e j 2 πk = 1 , e j 2 π N k satisfies the equation X N = 1. Hence e j 2 π N k is an N th root of unity. Consider ∑ N -1 n =0 e j 2 π N kn e j 2 π N ln . If k = l , the terms in the sum represent the N equally spaced roots in the unit circle which clearly add to zero. However, if k = l , the sum becomes ∑ N -1 n =0 1 = N . see fig 8.1-1

/negationslash

<!-- image -->

## Roots for N=12

Figure 8.1-1:

## 8.2

- (a) W q W q ( l -1) = e -j 2 π N q e -j 2 π N q ( l -1) = e -j 2 π N ql = W ql
- N N N (b) Let ˆ W q N = W q N + δ where ˆ W q N is the truncated value of W q N . Now ˆ W ql N = ( W q N + δ ) l ≈ W ql N + lδ .

Generally, single precision means a 32-bit length or δ = 5x10 -10 ; while 4 significant digits means 5 5

δ = 5x10 -. Thus the error in the final results would be 10 times larger. (c) Since the error grows as lδ , after N iterations we have an error of Nδ . If W ql N is reset to -j after every ql = N 4 iterations, the error at the last step of the iteration is lδ = [ N 4 q ] δ . Thus, the error reduced by approximately a factor 4 q .

## 8.3

## 8.4

Create three subsequences of 8-pts each

<!-- formula-not-decoded -->

where Y 1 , Y 2 , Y 3 represent the 8-pt DFTs of the subsequences.

## 8.5

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Temporal aliasing occurs in first two points of x ′ ( n ) because X ( z ) is not sampled at sufficiently small spacing on the unit circle.

## 8.6

<!-- formula-not-decoded -->

Figure 8.6-1:

<!-- image -->

<!-- formula-not-decoded -->

## 8.8

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

which are the same as F 1 ( k ) and F 2 ( k ) in (8.1.26)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Refer to Fig.8.1.9. The first stage of butterflies produces (2, 2, 2, 2, 0, 0, 0, 0). The twiddle factor multiplications do not change this sequence. The nex stage produces (4, 4, 0, 0, 0, 0, 0, 0) which again remains unchanged by the twiddle factors. The last stage produces (8, 0, 0, 0, 0, 0, 0, 0). The bit reversal to permute the sequence into proper order unscrambles only zeros so the result remains (8, 0, 0, 0, 0, 0, 0, 0).

## 8.9

See Fig. 8.1.13.

## 8.10

Using (8.1.45), (8.1.46), and (8.1.47) the fig 8.10-1 is derived:

## 8.11

Using DIT following fig 8.1.6:

<!-- formula-not-decoded -->

Figure 8.10-1:

<!-- image -->

<!-- formula-not-decoded -->

Using DIF following fig 8.1.11:

<!-- formula-not-decoded -->

## 8.12

Let

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

As every F ( i ) = 0 except F (0) = -F (2) = 4,

<!-- formula-not-decoded -->

which means that X (4) = X (12) = 8 . X ( k ) = 0 for other K .

## 8.13

- (a) 'gain' = W 0 8 W 0 8 ( -1) W 2 8 = -W 2 8 = j
- (b) Given a certain output sample, there is one path from every input leading to it. This is true for every output.
- (c) X (3) = x (0) + W 3 8 x (1) -W 2 8 x (2) + W 2 8 W 3 8 x (3) -W 0 8 x (4) -W 0 8 W 3 8 x (5) + W 0 8 W 2 8 x (6) + W 0 8 W 2 8 W 3 8 x (7)

## 8.14

Flowgraph for DIF SRFFT algorithm for N=16 is given in fig 8.14-1. There are 20 real, non trivial multiplications.

## 8.15

For the DIT FFT, we have

<!-- formula-not-decoded -->

The first term can be obtained from an N 2 -point DFT without any additional multiplications. Hence, we use a radix-2 FFT. For the second term, we use a radix-4 FFT. Thus, for N=8, the DFT is decomposed into a 4-point, radix-2 DFT and a 4-point radix-4 DFT. The latter is

<!-- formula-not-decoded -->

The computation of X ( k ) , X ( k + N 4 ) , X ( k + N 2 ) , X ( k + 3 N 4 ) for k = 0 , 1 , . . . , N 4 -1 are performed from the following:

<!-- formula-not-decoded -->

Figure 8.14-1:

<!-- image -->

<!-- formula-not-decoded -->

The basic butterfly is given in fig 8.15-1

Figure 8.15-1:

<!-- image -->

<!-- formula-not-decoded -->

8.16

<!-- image -->

8.17

## 8.19

<!-- formula-not-decoded -->

where z k = re -j 2 π N k , k = 0 , 1 , . . . , N -1 are the N sample points. It is clear that X ( z k ) , k = 0 , 1 , . . . , N -1 is equivalent to the DFT (N-pt) of the sequence x ( n ) r -n , n ∈ [0 , N -1].

## 8.18

<!-- formula-not-decoded -->

L = 1 is a trivial case with no zeros inserted and

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Let F ( t ) , t = 0 , 1 , . . . , N -1 be the DFT of the sequence on k X ( k ) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

8.21

<!-- formula-not-decoded -->

## 8.22

The standard DFT table stores N complex values W k N , k = 0 , 1 , . . . , N -1. However, since W k + N 2 N = -W k N , we need only store W k N k = 0 , 1 , . . . , N 2 -1. Also, W k + N 4 N = -jW k N which is

merely an interchange of real and imaginary parts of W k N and a sign reversal. Hence all essential quantities are easily obtained from W k N k = 0 , 1 , . . . , N 4 -1

## 8.23

The radix-2 FFT algorithm for computing a 2N-pt DFT requires 2 N N log 2 2 N = N + Nlog 2 N complex multiplications. The algorithm in (8.2.12) requires 2[ N 2 log 2 N + N 2 ] = N 2 + log 2 N complex multiplications.

## 8.24

## 8.25

<!-- formula-not-decoded -->

Total number of complex multiplies is 28 and the operations can be performed in-place. see fig 8.25-1

## 8.26

<!-- formula-not-decoded -->

Compute N + 1-pt DFTs of sequences { b 0 , b 1 , . . . , b M , 0 , 0 , . . . , 0 } and { 1 , a 1 , . . . , a N } (assumes N &gt; M ), say B ( k ) and A ( k ) k = 0 , . . . , N

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 8.25-1:

<!-- image -->

<!-- formula-not-decoded -->

The number of required complex multiplications is 28. The operations can be performed in-place. see fig 8.26-1

## 8.27

(a)Refer to fig 8.27-1 (b)Refer to fig 8.27-2

Figure 8.26-1:

<!-- image -->

(c) DIF is preferable for computing all points. It is also better when only X (0) , X (1) , X (2) , X (3) are to be calculated. The rule is to compare the number of nontrivial complex multiplies and choose the algorithm with the fewer.

- (d) If M &lt;&lt; N and L &lt;&lt; N , the percentage of savings is

N

2

log

2

N

N

2

-

ML

2

log

2

N

log

2

N

×

100% = (1

-

ML

N

)

×

100%

Figure 8.27-1:

<!-- image -->

Figure 8.27-2:

<!-- image -->

(a)Refer to fig 8.28-1. If data shuffling is not allowed, then X (0) , . . . , X (3) should be computed

Figure 8.28-1:

<!-- image -->

by one DSP. Similarly for X (4) , . . . , X (7) and X (8) , . . . , X (11) and X (12) , . . . , X (15). From the flow diagram the output of every DSP requires all 16 inputs which must therefore be stored in each DSP.

(b)Refer to fig 8.28-2

- (c) The computations necessary for a general FFT are shown in the figure for part (a), N g = N 2 log 2 N . Parallel computation of the DFTs requires

<!-- formula-not-decoded -->

Complex operations, as is seen in the figure for (b). Thus

<!-- formula-not-decoded -->

Figure 8.28-2:

<!-- image -->

8.29 Refer to fig 8.29-1

<!-- formula-not-decoded -->

This result can be obtained from the forward DIT FFT algorithm by conjugating each occurrence of W i N → W -i N and multiplying each output by 1 8 (or 1 2 can be multiplied into the outputs of each stage).

## 8.30

<!-- formula-not-decoded -->

Similar to the DIT case (prob. 8.29) result can be obtained by conjugating each W i N and scaling by 1 8 . Refer to fig 8.30-1

Figure 8.29-1:

<!-- image -->

8.31

Figure 8.30-1:

<!-- image -->

<!-- formula-not-decoded -->

Since the IDFT of a Hermitian symmetric sequence is real, we may conjugate all terms in the sum yielding

<!-- formula-not-decoded -->

In general, the IDFT of an N-length sequence can be obtained by reversing the flow of a forward FFT and introducing a scale factor 1 N . Since the IDFT is apparently capable of producing the (scaled) DFT for a Hermitian symmetric sequence, the reversed flow FFT will produce the desired FFT.

## 8.32

## 8.33

- (a) 11 frequency points must be calculated. Radix-2 FFT requires 1024 2 log 2 1024 ≈ 5000 complex multiplies or 20,000 real multiplies. FFT of radix-4 requires 0 . 75 × 5000 = 3 , 750 complex multiplies or 15,000 real multiplies. Choose Goertzel.

(b) In this case, direct evaluation requires 10 6 complex multiplies, chirp-z 22 × 10 3 comples multiplies, and FFT 1000 + 5000 2 × 13 = 33 × 10 3 complex multiplies. Choose chirp-z.

## 8.34

In the DIF case, the number of butterflies affecting a given output is N 2 in the first stage, N 4 in the second, . . . . The total number is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This can be viewed as the convolution of the N-length sequence x ( n ) with the impusle response of a linear filter.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Every butterfly requires 4 real multiplies, and the eror variance is δ 2 12 . Under the assumption that the errors are uncorrelated, the variance of the total output quantization error is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(a)

<!-- formula-not-decoded -->

The other inequalities are verified similarly. (b)

<!-- formula-not-decoded -->

By similar means using (*), it can be shown that the same inequality holds if A &lt; 0. Also, from the pair of equations fro computing the butterfly outputs, we have

<!-- formula-not-decoded -->

By a similar method to that employed above, it can be shown that

<!-- formula-not-decoded -->

## 8.36

Refer to fig 8.36-1.

(d) (1) The frequency interval between successive samples for the plots in parts (a), (b), (c) and (d) are 1 64 , 1 64 , 1 128 and 1 64 respectively.

- (2) The dc values computed theoretically and from the plots are given below:

<!-- formula-not-decoded -->

Both theoretical and practical dc values match except in the last case because of the finite word length effects the dc value is not a perfect zero.

- (3) Frequency interval = π N 1 .
- (4) Resolution is better with N = 128.

## 8.37

- (a) Refer to fig 8.37-1.
- (b) Refer to fig 8.37-1.
- (c) Refer to fig 8.37-1.
- (d) Refer to fig 8.37-1.
- (e) Refer to fig 8.37-2.

Figure 8.36-1:

<!-- image -->

Figure 8.37-1:

<!-- image -->

Figure 8.37-2:

<!-- image -->

## Chapter 9

## 9.1

<!-- formula-not-decoded -->

Figure 9.1-1:

<!-- image -->

9.2

Refer to fig 9.2-1

<!-- formula-not-decoded -->

Figure 9.1-2:

<!-- image -->

<!-- formula-not-decoded -->

Since K 2 &gt; 1, the system is not minimum phase.

## 9.3

<!-- formula-not-decoded -->

Figure 9.2-1: (a) Direct form. (b) Lattice form

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

## 9.5

<!-- formula-not-decoded -->

Refer to fig 9.5-1

## 9.6

## 9.4

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

9.7

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Since the poles are inside the unit circle, the system is stable.

<!-- formula-not-decoded -->

Figure 9.5-1:

<!-- image -->

<!-- formula-not-decoded -->

The system is unstable. (c)

9.8

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(c)Refer to fig 9.8-1 (d)

Refer to fig 9.8-2.

/negationslash

<!-- formula-not-decoded -->

Figure 9.8-2:

<!-- image -->

<!-- formula-not-decoded -->

<!-- image -->

Figure 9.9-1:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Refer to fig 9.9-2

(c)

Figure 9.9-2:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Refer to fig 9.9-3 (d)

Refer to fig 9.9-4 (e)

Refer to fig 9.9-5 (f) H ( z ) = 1 -z -1 + z -2 1 -z -1 +0 . 5 z -2 ⇒ Complex valued poles and zeros.Refer to fig 9.9-6 All the above

Figure 9.9-3:

<!-- image -->

systems are stable.

Figure 9.9-4:

<!-- image -->

Figure 9.9-5:

<!-- image -->

Direct form I:

## Direct form II, cascade, parallel:

Figure 9.9-6:

<!-- image -->

Refer to fig 9.10-1

Figure 9.10-1:

<!-- image -->

<!-- formula-not-decoded -->

By combining (1) and (2) we obtain

<!-- formula-not-decoded -->

Use (4) to eliminate W ( z ) in (3). Thus,

<!-- formula-not-decoded -->

9.11

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9.12

Refer to fig 9.12-1

Figure 9.12-1:

<!-- image -->

<!-- formula-not-decoded -->

## 9.13

```
YJM1 = G * XIN DO 20 J=1,K YJ=B(J,0) * XIN + W1(J) W1(J) = B(J,1)*XIN - A(J,1)*YJ + W2(J) W2(J) = B(J,2)*XIN - A(J,2)*YJ YJM1 = YJM1 + YJ 20 CONTINUE YOUT = YJM1 RETURN
```

## 9.14

```
YJM1 = XIN DO 20 J=1,K W=-A(J,1) * WOLD1 - A(J,2) * WOLD2 + YMJ1 YJ = W + B(J,1)*WOLD1 + B(J,2)*WOLD2 WOLD2 = WOLD1 WOLD1 = W YJM1 = YJ 20 CONTINUE YOUT = YJ RETURN
```

## 9.15

## 9.16

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

the zeros of H ( z ).

## 9.17

(a) Refer to fig 9.17-1

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) If the magnitude of the last coefficient | k N | = 1, i.e., k N = ± 1, all the zeros lie on the unit circle.
- (d) Refer to fig 9.16-1. We observe that the filters are linear phase filters with phase jumps at

Figure 9.16-1:

<!-- image -->

Figure 9.17-1:

<!-- image -->

<!-- formula-not-decoded -->

(b) H ( z ) = 1 + 0 . 157 z -1 +0 . 0032 z -2 +0 . 8 z -3 . Refer to fig 9.17-2

Figure 9.17-2:

<!-- image -->

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

.

73

z

-

1

1

.

67

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

From the equations, we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

z

-

2

The equivalent lattice-ladder structure is: Refer to fig 9.18-1 (b) A 3 ( z ) = 1 + 0 . 9 z -1 -0 . 8 z -2 +0 . 5 z -3 , | k 1 | &gt; 1 and | k 2 | &gt; 1 ⇒ the system is unstable.

Figure 9.18-1:

<!-- image -->

## 9.19

## Refer to fig 9.19-1

<!-- formula-not-decoded -->

The system has a zero at z = 0 and poles at z = re ± j Θ .

## 9.20

<!-- formula-not-decoded -->

where

Figure 9.19-1:

<!-- image -->

<!-- formula-not-decoded -->

or, equivalently,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## (b) Refer to fig 9.21-1

Direct form:

Figure 9.21-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Refer to fig 9.22-1

- (b) When r = 1, the system becomes an oscillator.

Figure 9.22-1:

<!-- image -->

<!-- formula-not-decoded -->

## 9.23

## 9.24

<!-- formula-not-decoded -->

## 9.25

<!-- formula-not-decoded -->

<!-- image -->

Thus the lattice-ladder structure is: Refer to fig 9.23-1

Figure 9.23-1:

<!-- image -->

Figure 9.24-1:

<!-- image -->

## 9.26

<!-- formula-not-decoded -->

Figure 9.25-1:

<!-- image -->

Figure 9.27-1:

<!-- image -->

<!-- formula-not-decoded -->

9.27

## (a) Refer to fig 9.27-1

<!-- formula-not-decoded -->

Refer to fig 9.27-2. The region of stability in the a 1 -a 2 plane is shaded in the figure. There are

Figure 9.27-2:

<!-- image -->

nine integer pairs ( a 1 , a 2 ) which satisfy the stability conditions. These are (with corresponding system functions):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(d) see above.

## 9.28

Refer to fig 9.28-1

Note that 4 multiplications and 3 additions are required to implement H 1 ( z ). The advantage

Figure 9.28-1: Structure of H 1 ( z )

<!-- image -->

of Horner's method is in evaluating H 1 ( z ) for a specific z 0 . Thus, if

<!-- formula-not-decoded -->

the 3 multiplications and 3 additions are required for the evaluation of 9.1 in the field of z . If the various powers of z are prestored, then Horner's scheme has no advantage over the direct evaluation of 9.1. Refer to fig 9.28-2

This requires 4 multiplications and 3 additions. The linear-phase system is written as

Figure 9.28-2: Structure of H ( z ) = b 0 z -3 + b 0 b 1 z -2 + b 0 b 1 b 2 z -1 + b 0 b 1 b 2 b 3

<!-- image -->

<!-- formula-not-decoded -->

By applying Horner's scheme, we can rewrite this as

<!-- formula-not-decoded -->

Assuming that z -1 and z are given, a direct evaluation of H ( z ) at z = z 0 requires 8 multiplications and 6 additions. Using Horner's scheme based on 9.28, requires the same number of operations as direct evaluation of H ( z ). Hence, Horner's scheme does not offer any savings in computation.

## 9.29

- (a) When x 1 and x 2 are positive, the result is obvious. If x 1 and x 2 are negative, let

$$x 1 = - 0 n 1 n 2 . . . n b = - 0 n 1 n 2 . . . n b +000 . . . 0 1 x 2 = - 0 m 1 m 2 . . . m b = - 1 m 1 m 2 . . . m b +000 . . . 0 1 x 3 = x 1 + x 2 = - 0 n 1 0 . . . 0 + 0 m 1 0 . . . 0 + c where c = 0 0 n 2 . . . n b +00 m 2 . . . m b +000 . . . 0 1 0$$

If the sign changes, there are two possibilities

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

9.30

<!-- formula-not-decoded -->

- (b) Refer to fig 9.30-1
- (c) If | ˆ a | = | -ˆ a | , where ˆ a means the quantized value of a , then the filter remains all-pass.

<!-- image -->

a

Figure 9.30-1:

- (d) Refer to fig 9.30-2
- (e) Yes, it is still all-pass.

<!-- formula-not-decoded -->

## 9.31

<!-- formula-not-decoded -->

Errors occur when number becomes small.

Figure 9.30-2:

<!-- image -->

<!-- formula-not-decoded -->

## 9.33

<!-- formula-not-decoded -->

<!-- image -->

## Figure 9.33-1:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Refer to fig 9.34-1 Cascade the three systems in six possible permutations to obtain six realiza-

Figure 9.34-1:

<!-- image -->

tions. (b) Error sequence e i ( n ) is uniformly distributed over interval ( 1 2 2 -b , 1 2 2 -b ). So σ 2 e i = 2 -2 b 12 for any i (call it σ 2 e )

<!-- formula-not-decoded -->

9.34

<!-- formula-not-decoded -->

Figure 9.34-2:

<!-- image -->

(c) consider cascade H 1 -H 2 -H 3 Refer to fig 9.34-2

<!-- formula-not-decoded -->

9.35

<!-- formula-not-decoded -->

3

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 9.36

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Define ρ /triangle = rcosθ, ρ /triangle = rsinθ for convenience, (a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

when H 1 ( z ) and H 2 ( z ) are as defined in the problem statement

<!-- formula-not-decoded -->

9.38

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

Figure 9.39-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

9.39

Refer to fig 9.39-1

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) Refer to fig 9.40-1.

(c) Refer to fig 9.40-2.

Refer to fig 9.40-3.

Refer to fig 9.40-4.

<!-- image -->

Direct form II and cascade structure:

<!-- image -->

Figure 9.40-1:

<!-- image -->

---&gt; n

Figure 9.40-2:

<!-- image -->

<!-- image -->

<!-- image -->

(a)

<!-- image -->

Figure 9.41-1:

<!-- image -->

Refer to fig 9.41-1b. (c) Refer to fig 9.41-2. (e) Refer to fig 9.41-3.

Figure 9.41-2:

<!-- image -->

- (f) Finite word length effects are visible in h ( n ) for part f.

## 9.42

Refer to fig 9.42-1.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 9.41-3:

<!-- image -->

## Parallel form structure:

<!-- image -->

Parallel form structure using 2nd-order coupled-form state-space sections

Figure 9.42-1:

<!-- image -->

## Chapter 10

## 10.1

- (a) To obtain the desired length of 25, a delay of 25 -1 2 = 12 is incorporated into H d ( w ). Hence,

<!-- formula-not-decoded -->

(b) H ( w ) = h ( n ) e plot H ( w ) and H ( w ). Refer to fig 10.1-1.

- where w ( n ) is a rectangular window of length N = 25. ∑ 24 n =0 -jwn ⇒ | | (c) Hamming window:

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

Refer to fig 10.1-2.

Figure 10.1-2:

<!-- image -->

(d) Bartlett window:

Refer to fig 10.1-3.

Figure 10.1-3:

<!-- image -->

10.2

<!-- formula-not-decoded -->

- (b) Rectangular window:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## (c) Hamming window:

Figure 10.2-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Refer to fig 10.2-2. (d) Bartlett window:

Refer to fig 10.2-3.

Note that the magnitude responses in (c) and (d) are poor because the transition region is wide. To obtain sharper cut-off, we must increase the length N of the filter.

Figure 10.2-3:

<!-- image -->

## 10.3

- (a) Hanning window: w ( n ) = (1 cos ) , 0 n 24. Refer to fig 10.3-1.
- (b) Blackman window: w ( n ) = 0 . 42 0 . 5 cos +0 . 08 cos .
- 1 2 -πn 12 ≤ ≤ πn πn

-12 6 Refer to fig 10.3-2.

Figure 10.3-1:

<!-- image -->

## 10.4

- (a) Hanning window: Refer to fig 10.4-1.
- (b) Blackman window: Refer to fig 10.4-2.

The results are still relatively poor for these window functions.

## 10.5

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 10.3-2:

<!-- image -->

<!-- formula-not-decoded -->

Figure 10.4-2:

<!-- image -->

## 10.7

10.8

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Solving the above eqn yields,

<!-- formula-not-decoded -->

h ( n ) = { 0 . 3189 , 0 . 0341 , -0 . 1079 , -0 . 0365 , 0 . 0667 , 0 . 0412 , -0 . 0498 , 0 . 4667 0 . 4667 , -0 . 0498 , 0 . 0412 , 0 . 0667 , -0 . 0365 , -0 . 1079 , 0 . 0341 , 0 . 3189 }

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Solving the above eqn yields,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Refer to fig 10.8-2.

we note that the digital differentiator has a frequency response that resembles the response of the analog differentiator. (d)

<!-- formula-not-decoded -->

/negationslash

/negationslash

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 10.8-1:

<!-- image -->

<!-- formula-not-decoded -->

Figure 10.8-2:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

Note that for small w , sin w 2 ≈ w 2 and H ( w ) ≈ jwe -j w 2 , which is a suitable approximation to the differentiator in (c).

Refer to fig 10.8-3.

(e) The value H ( w 0 ) is obtained from (d) above. Then y ( n ) = A | H ( w 0 ) | cos ( w 0 n + θ + π 2 -w 0 2 )

## 10.9

/negationslash

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

With a Hamming window, we obtain the following frequency response: Refer to fig 10.9-1.

## 10.10

H ( s ) has two zeros at z 1 = -0 . 1 and z 2 = ∞ and two poles p 1 , 2 = -0 . 1 ± j 3. The matched z-transform maps these into:

<!-- formula-not-decoded -->

From the impulse invariance method we obtain

<!-- formula-not-decoded -->

Figure 10.9-1:

<!-- image -->

The poles are the same, but the zero is different.

## 10.11

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In order to compare the result with example 10.4.2, let

<!-- formula-not-decoded -->

By substituting into the equation above, we obtain

<!-- formula-not-decoded -->

/negationslash

/negationslash

## 10.12

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) The digital integrator closely matches the magnitude characteristics of the analog integrator. The two phase characteristics are identical.
- (e) The integrator has a pole at w = 0. To avoid overflow problems, we would have E [ x ( n )] = 0, i.e., a signal with no dc component.

## 10.13

(a)

<!-- formula-not-decoded -->

- (b) Refer to fig 10.13-1

## 10.14

- (a) There are only zeros, thus H ( z ) is FIR. (b)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 10.13-1:

<!-- image -->

<!-- formula-not-decoded -->

Therefore, H ( w ) is linear phase.

- (c) Refer to fig 10.14-1

## 10.15

From the design specifications we obtain

<!-- formula-not-decoded -->

Figure 10.14-1:

<!-- image -->

<!-- formula-not-decoded -->

From the design specifications we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 10.17

Passband ripple = 1dB ⇒ /epsilon1 = 0 . 509

Stopband attenuation = 60dB ⇒ δ = 1000

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Special software package, such as MATLAB or PC-DSP may be used to obtain the filter coefficients. Hand computation of these coefficients for N = 14 is very tedious.

## 10.18

Passband ripple = 0.5dB ⇒ /epsilon1 = 0 . 349 Stopband attenuation = 50dB

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Use a computer software package to determine the filter coefficients.

## 10.19

(a) MATLAB is used to design the FIR filter using the Remez algorithm. We find that a filter of length M = 37 meets the specifications. We note that in MATLAB, the frequency scale is normalized to 1 2 of the sampling frequency. Refer to fig 10.19-1.

<!-- formula-not-decoded -->

Figure 10.19-1:

<!-- image -->

With equation (10.2.94) we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Note (10.2.95) is a better approximation of M .

## (c) Refer to fig 10.19-2.

Note that this filter does not satisfy the specifications.

Figure 10.19-2: M=37 FIR filter designed by window method with Hamming window

<!-- image -->

(d)The elliptic filter satisfies the specifications. Refer to fig 10.19-3.

(e)

## 10.20

(a)

<!-- formula-not-decoded -->

(b) | H ( w ) | = | 2 cos 4 w +4 cos 3 w +6 cos 2 w +8 cosw +5 | . Refer to fig 10.20-1.

|              |   FIR |   IIR |
|--------------|-------|-------|
| order        |    37 |     5 |
| storage      |    19 |    16 |
| No. of mult. |    19 |    16 |

10.21

(a)

<!-- formula-not-decoded -->

Figure 10.19-3:

<!-- image -->

Figure 10.20-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

10.22

<!-- formula-not-decoded -->

Let h s ( n ) = h d ( n ) w ( n ) , -100 ≤ n ≤ 100( M = 101) Then, h ( n ) = h s ( n -100) will be the impulse of the filter for 0 ≤ n ≤ 200

<!-- formula-not-decoded -->

H ( w ) will match H d ( w ) at 201 points in frequency. The filter will contain large ripples in between the sampled frequencies. Transition values should be specified to reduce the ripples in both the passbands and the stopband.

<!-- formula-not-decoded -->

(a)

w l = 5 π 12 Ω l = tan w l 2 ( for T = 2) w u = 7 π 12 Ω u = tan w u 2 Analog: lowpass to bandpass s → s 2 +Ω l Ω u s (Ω u -Ω l ) Bilinear: Analog to digital s → z -1 z +1 = 1 -z -1 1 + z -1 combine the two steps: s → ( 1 -z -1 1+ z -1 ) 2 +Ω l Ω u 1 -z -1 1+ z -1 (Ω u -Ω l ) = (1 -z -1 ) 2 +Ω u Ω l (1 + z -1 ) 2 (1 -z -1 )(Ω u -Ω l ) Therefore, H ( z ) = 1 [ (1 -z -1 ) 2 +Ω u Ω l (1+ z -1 ) 2 (1 -z -2 )(Ω u -Ω l ) ] 2 + √ 2 [ (1 -z -1 ) 2 +Ω u Ω l (1+ z -1 ) 2 (1 -z -2 )(Ω u -Ω l ) ] +1 (b) Ω u Ω l = tan 7 π 24 tan 5 π 24 = 1 . 7 (1) Ω u Ω l = 1 . 43 (2) Ω u Ω l = 1 . 8 (3) Ω u Ω l = 1 . 82 (4) Ω u Ω l = 1 . 7

filter (4) satisfies the constraint

## 10.24

<!-- formula-not-decoded -->

This filter is FIR with zeros at z = 1 , e ± j π 6 , e ± j π 2 , e ± j 5 π 6 , -0 . 5528 ± j 0 . 6823 and 0 . 3028 ± j 0 . 7462 (b) It is a highpass filter.

(c)

<!-- formula-not-decoded -->

## 10.25

(a)

Refer to fig 10.25-1.

- (b) The ideal lowpass filter has a passband of -0 . 04 ≤ f ≤ 0 . 04. Hence,

Figure 10.25-1:

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

-0.04

0

Hence,

<!-- formula-not-decoded -->

(b)

10.27

<!-- formula-not-decoded -->

h ( n ) is the impulse response of the lowpass filter H ( w )

<!-- formula-not-decoded -->

10.26

(a)

<!-- formula-not-decoded -->

By differentiating E with respect to each coefficient and setting the derivatives to zero, we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By carrying out the minimization we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

x ( n ) is a periodic sequence with period N. Hence, y ( n ) is also periodic with period N. Let

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

If p +1 ≤ N , the N equations above are sufficient to determine a 1 , a 2 , . . . , a p and their order. If p +1 &gt; N , it is not possible to determine the { a k } and the order p .

## 10.28

- (1) The set of linear equations are:

<!-- formula-not-decoded -->

- (2) Refer to fig 10.28-1.
- (3) Refer to fig 10.28-2.

Figure 10.28-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 10.28-2:

<!-- image -->

## 10.29

(a) Since δ ( n -k ) = 0 except for n = k , equation (1) reduces to

<!-- formula-not-decoded -->

(b) Since δ ( n -k ) = 0 except for n = k , equation (1) reduces to

<!-- formula-not-decoded -->

(c) We use the linear equation given in (b) to solve for the filter parameters { a k } . Then we use values for the { a k } in the linear equation fiven in (a) and solve for the parameters { b k } .

## 10.30

We can see that by setting M = 0 and N = 1 in

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

we can provide a perfect match to H d ( z ) as given in

<!-- formula-not-decoded -->

Figure 10.28-3:

<!-- image -->

With δ ( n ) as the input to H ( z ), we obtain the output

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Substituting for h d ( n ), we obtain a 1 = -1 2 . To solve for b 0 , we use the equation given in 10.29(a) with h ( n ) = h d ( n ) ,

<!-- formula-not-decoded -->

For n = 0 this equation yields b 0 = 2. Thus

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For n &gt; M = 1, we have or, equivalently,

(b)

<!-- formula-not-decoded -->

By differentiating with respect to the parameters { a k } , we obtain the set of linear equations of the form

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The solution of these linear equations yield to the filter parameters { a k } .

- (c) We can find the least-squares solution for { b k } from the minimization of

<!-- formula-not-decoded -->

Thus we obtain a set of linear equations for the parameters { b k } , in the form

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where, where

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

h d ( n ) can be found by substituting x ( n ) = δ ( n ). Fig 10.32-1 shows the h d ( n

<!-- formula-not-decoded -->

Figure 10.32-1:

<!-- image -->

- (b) The poles and zeros obtained using Shanks' method are listed in Table 10.32. The magnitude response for each case together with the desired response is shown in Fig. 10.32-2. The frequency response characteristics illustrate that Shanks' method yields very good designs when the number of poles and zeros equals or exceeds the number of poles and zeros in the actual filter. Thus the inclusion of zeros in the approximation has a significant effect in the resulting design.

| Filter Order   | Poles                        | Zeros                   |
|----------------|------------------------------|-------------------------|
| N=3 M=2        | 0.5348 0 . 6646 ± j 0 . 4306 | - 0 . 2437 ± j 0 . 5918 |
| N=3            | 0.3881                       | -1                      |
| M=3            | 0 . 5659 ± j 0 . 4671        | 0 . 1738 ± j 0 . 9848   |
| N=4            | -0.00014 0.388               | -1                      |
| M=3            | 0 . 566 ± j 0 . 4671         | 0 . 1738 ± j 0 . 9848   |

Figure 10.32-2:

<!-- image -->

## Chapter 11

## 11.1

- (a) Let the corresponding baseband spectrum be called X b (Ω). Then

<!-- formula-not-decoded -->

With frequencies normalized to F x ,

- . The sequence x ( n ) has DTFT

<!-- formula-not-decoded -->

modulation by cos (0 . 8 π ) causes shifts up and down by 0 . 8 π (and scaling by 1 2 ) of each

Figure 11.1-1:

<!-- image -->

component in the spectrum. Refer to fig 11.1-1. Ideal LPF preserves only the baseband spectrum (of each period). Refer to fig 11.1

<!-- formula-not-decoded -->

Figure 11.1-2:

<!-- image -->

The downsampling produces the figure in fig 11.1, where w ′′ = Ω F y = Ω D F x = 10 w ′ . Note that there is no aliasing in the spectrum | Y ( w ′′ ) | because the decimated sample rate, in terms of w ′ , is 2 π 10 &gt; 0 . 04 π .

(b) The assumed spectral amplitude normalization in fig 11.1-1 implies that the analog FT (magnitude spectrum) of x a ( t ) is (refer to fig 11.1-4).

The given sample rate is identical to F y above, F y = 250Hz. The DTFT of samples taken at this rate is ˜ Y (Ω) = 1 T y ∑ q X a (Ω -q Ω y ) where Ω y = 2 πF y . On a scaled frequency axis w ′′ = Ω T y = Ω F y , ˜ Y ( w ′′ ) = 1 T y ∑ q X a ( w ′′ -q 2 π ). Consequently ˜ y ( n ) = y ( n ).

Figure 11.1-3:

<!-- image -->

## 11.2

<!-- formula-not-decoded -->

## 11.3

(a)Refer to fig 11.3-1 (b)

Figure 11.3-1:

<!-- image -->

Figure 11.1-4:

<!-- image -->

<!-- formula-not-decoded -->

## 11.4

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (c) Refer to fig 11.3-2

Figure 11.3-2:

<!-- image -->

<!-- formula-not-decoded -->

- (a) Let w ′ = Ω F x , w ′′ = Ω D F x . Refer to fig 11.4-1 Let x ′′ ( n ) be the downsampled sequence.

<!-- formula-not-decoded -->

Figure 11.4-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

As long as Dw ′ m ≤ π , X ( w ′ ) [hence x ( n )] can be recovered from X ′′ ( w ′′ )[ x ′′ ( n ) = x ( Dn )] using interpolation by a factor D :

<!-- formula-not-decoded -->

The given sampling frequency is w ′ s = 2 π D . The condition Dw ′ m ≤ π → 2 w ′ m ≤ 2 π D = w ′ s (b) Let x a ( t ) be the ral analog signal from which samples x ( n ) were taken at rate F x . There exists a signal, say x ′ a ( t ′ ), such that x ′ a ( t ′ ) = X a ( t T x ). x ( n ) may be considered to be the samples of x ′ ( t ′ ) taken at rate f x = 1. Likewise x ′′ ( n ) = x ( nD ) are samples of x ′ ( t ′ ) taken at rate f ′′ x = f x D = 1 D . From sampling theory, we know that x ′ ( t ′ ) can be reconstructed from its samples x ′′ ( n ) as long as it is bandlimited to f m ≤ 1 2 D , or w m ≤ π D , which is the case here. The reconstruction formula is where

Refer to fig 11.4-2

Actually the bandwidth of the reconstruction filter may be made as small as w ′ m , or as large as 2 π D -w ′ m , so h r may be

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where w ′ m ≤ w ′ c ≤ 2 π D -w ′ m . In particular x ( n ) = x ′ ( t ′ = n ) so

<!-- formula-not-decoded -->

Figure 11.4-2:

<!-- image -->

(c) Clearly if we define

<!-- formula-not-decoded -->

then, we may write 11.4 as

0

<!-- formula-not-decoded -->

so x ( n ) is reconstructed as (see fig 11.4-3)

Figure 11.4-3:

<!-- image -->

(a)

<!-- image -->

see fig 11.5-2

No information is lost since the decimated sample rate still exceeds twice the bandlimit of

Figure 11.5-2:

<!-- image -->

the original signal.

## 11.6

A filter of length 30 meets the specification. The cutoff frequency is w c = π 5 and the coefficients are given below:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.7

A filter of length 30 meets the specification. The cutoff frequency is w c = π 2 and the coefficients are given below:

```
h (1) = h (30) = 0 . 006026 h (2) = h (29) = -0 . 01282 h (3) = h (28) = -0 . 002858 h (4) = h (27) = 0 . 01366 h (5) = h (26) = -0 . 004669 h (6) = h (25) = -0 . 01970 h (7) = h (24) = 0 . 01598 h (8) = h (23) = 0 . 02138 h (9) = h (22) = -0 . 03498 h (10) = h (21) = -0 . 01562 h (11) = h (20) = 0 . 06401 h (12) = h (19) = -0 . 007345 h (13) = h (18) = -0 . 1187 h (14) = h (17) = 0 . 09805 h (15) = h (16) = 0 . 4923 p k ( n ) = h (2 n + k ) , k = 0 , 1; n = 0 , 1 , . . . , 14
```

<!-- formula-not-decoded -->

corresponding polyphase filter structure (see fig 11.6-1)

Figure 11.6-1:

<!-- image -->

## 11.8

The FIR filter that meets the specifications of this problem is exactly the same as that in Problem 11.6. Its bandwidth is π 5 . Its coefficients are

<!-- formula-not-decoded -->

A polyphase filter would employ two subfilters, each of length 15

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.9

(a)

Figure 11.7-1:

<!-- image -->

<!-- formula-not-decoded -->

/negationslash

- (b) suppose D = dk and I = ik and d, i are relatively prime.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Thus y 2 ( n ) = y 1 ( n ) iff d = dk or k = 1 which means that D and I are relatively prime.

## 11.10

- (a) Refer to fig 11.10-1

<!-- formula-not-decoded -->

<!-- image -->

<!-- image -->

Figure 11.10-1:

<!-- formula-not-decoded -->

Let ˜ h ( n ) be the IR corresponding to H ( z I )

<!-- formula-not-decoded -->

11.11

(a)

(b)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.12

The output of the upsampler is X ( z 2 ). Thus, we have

<!-- formula-not-decoded -->

## 11.13

- (a) Refer to Fig. 11.13-1 for I/D = 5 / 3.
- (b) Refer to Fig. 11.13-2 for I/D = 3 / 5.

Figure 11.13-1:

<!-- image -->

## 11.14

- (a) The desired implementation is given in Fig. 11.14-1
- (b) The polyphase decomposition is given by

<!-- formula-not-decoded -->

## 11.15

<!-- formula-not-decoded -->

where

Let m = N -1 -n . Then

(b)

Figure 11.14-1:

<!-- image -->

Figure 11.13-2:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 11.15-1: Type 1 Polyphase Decomposition

<!-- image -->

Figure 11.15-2: Type 2 Polyphase Decomposition

<!-- image -->

## 11.17

<!-- formula-not-decoded -->

Figure 11.16-1:

<!-- image -->

<!-- formula-not-decoded -->

The coefficients of the two filters can be obtained using a number of DSP software packages.

## 11.18

To avoid aliasing F sc ≤ F x 2 D . Thus D = I = 50.

Single stage

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Use DSP software to obtain filter coefficients.

## 11.19

b + ( n ) is nonzero for 0 ≤ n ≤ 2 N -2 with N even. Let c ( n ) = b + [ n -( N -1)]. So c ( n ) is nonzero for -( N -1) ≤ n ≤ N -1. From (11.11.35)

/negationslash

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

## 11.21

Suppose the output of the analysis section is x a 0 ( m ) and x a 1 ( m ). After interpolation by 2, they become y 0 ( m ) and y 1 ( m ). Thus

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The final output is one stage:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Passband 0 ≤ F ≤ 90

<!-- formula-not-decoded -->

Transition band 90 &lt; F ≤ 19 , 900

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Passband 0 ≤ F ≤ 90 Transition band 90 &lt; F ≤ 9 , 900

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In the same manner, it can be shown that

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 11.22

Refer to fig 11.22-1, where h i ( n ) is a lowpass filter with cutoff freq. π I i . After transposition (refer

Figure 11.22-1: I = I 1 I 2 . . . I L L -stage interpolator

<!-- image -->

to fig 11.22-2). As D = I , let D i = I L +1 -i , then D = D 1 D 2 . . . D L . Refer to fig 11.22-3 Obviously, this is equivalent to the transposed form above.

Figure 11.22-2:

<!-- image -->

Figure 11.22-3: L -stage decimator

<!-- image -->

Suppose that output is y ( n ). Then T y = k I T x . F y = 1 T y = I k 1 T x = I k F x . Assume that the lowpass filter is h ( n ) of length M = kI (see fig 11.23-4)

Figure 11.23-4:

<!-- image -->

11.24

<!-- image -->

<!-- formula-not-decoded -->

## 11.25

(a) Refer to fig 11.25-1.

(b)

Figure 11.25-1:

<!-- image -->

<!-- formula-not-decoded -->

(c) Refer to fig 11.25-2.

(d) Refer to fig 11.25-3.

Figure 11.25-2:

<!-- image -->

Figure 11.25-3:

<!-- image -->

## 11.26

## 11.27

where

Then,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Therefore, H k ( z ) , 0 ≤ k ≤ N -1 can be expressed in matrix form as

<!-- formula-not-decoded -->

Figure 11.26-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(b) From part (a), we have

<!-- formula-not-decoded -->

where W id the DFT matrix. (c)

Figure 11.27-1:

<!-- image -->

Figure 11.27-2:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Then,

<!-- formula-not-decoded -->

Note that the impulse response h k ( n ) are complex-valued, in general. Consequently, | H k ( w ) | is not symmetric with respect to w = 0.

(b) Let us use the polyphase implementation of the uniform filter bank. We have

<!-- formula-not-decoded -->

This yields P 0 ( z ) = 1, P 1 ( z ) = 1, P 2 ( z ) = 3, and P 3 ( z ) = 4. By using the results in Problem 11.27, we have the equation for the synthesis filter bank as

<!-- formula-not-decoded -->

where W denotes the DFT matrix. Thus, we have the analysis filter bank given in fig 11.28-1. (c) The synthesis filter bank in fig. 11.28-2

## 11.29

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Therefore, H ( z -1 ) and H ( z ) hve roots that are symmetric, such that if z i is not a root, then 1 /z i is also a root. This implies that H ( z ) has linera phase.

Figure 11.28-1:

<!-- image -->

Figure 11.28-2:

<!-- image -->

(b) We may express H ( z ) as:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Thus, we have the coefficients:

Therefore, H ( z ) is a half-band filter.

/negationslash

Figure 11.29-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

11.30

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 11.30-1: Anaylsis section

<!-- image -->

<!-- formula-not-decoded -->

<!-- image -->

-

-

Figure 11.30-2: QMF in a polyphase realization

(d) For perfect reconstruction,

<!-- formula-not-decoded -->

where C is a constant. We have

<!-- formula-not-decoded -->

(c)

## 11.31

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where Q ( z ) = Cz -k [ P ( z )] -1 . But

<!-- formula-not-decoded -->

By selecting C = 4 and k = 1, we have

Therefore,

(c)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 11.31-1:

<!-- image -->

(b) The synthesis filters are given as

<!-- formula-not-decoded -->

## Chapter 12

## 12.1

(a)

12.3

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) The whitening filter is H -1 ( z ) = 1 -z -1 + 1 2 z -2

## 12.2

<!-- formula-not-decoded -->

︸ ︷︷ ︸ [ min.pk. ] (b) Must invert the min. pk. filter to obtain a stable whitening filter.

For a stable filter, denominator (1 -1 2 z 1 ) must be chose. However, either numerator factor may be used. H ( z ) = (1 -1 3 z 1 ) (1 -1 2 z 1 ) or (1 -1 3 z ) (1 -1 2 z )

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

12.5

12.6

(a)

Refer to fig 12.6-1

Figure 12.6-1:

<!-- image -->

<!-- image -->

<!-- formula-not-decoded -->

(c) If | k p | = 1, the zeros of H ( z ) = A p ( z ) are on the unit circle. Refer to fig 12.6-2.

12.7

## 12.8

Let y ( m ) = x (2 n -p -m ). Then, the backward prediction of x ( n -p ) becomes the forward prediction of y ( n ). Hence, its linear prediction error filter is just the noise whitening filter of the corresponding anticausal AR(p) process.

## 12.9

Figure 12.6-2:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 12.10

<!-- formula-not-decoded -->

Refer to fig 12.9-1.

Figure 12.9-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Refer to fig 12.10-1.

## 12.11

The Levinson-Durbin algorithm for the forward filter coefficients is

<!-- formula-not-decoded -->

This is the Levinson-Durbin algorithm for the backward filter.

Figure 12.10-1:

<!-- image -->

## 12.12

Let

Then,

Hence,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

we also obtain the recursion

<!-- formula-not-decoded -->

## 12.13

Equations for the forward linear predictor:

<!-- formula-not-decoded -->

where the elements of c m are γ xx ( l + m ) , l = 1 , 2 , . . . , p . The solution of a m is

<!-- formula-not-decoded -->

where α m is the solution to Γ m α m = γ m

The coefficients for the m-step backward predictor are b m = a b m .

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Since we know the { a k } we can solve for γ xx ( m ) , m = 0 , 1 , 2 , 3. Then we can obtain γ xx ( m ) for m&gt; 3, by the above recursion. Thus,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

12.15

<!-- formula-not-decoded -->

The minimum-phase system function H ( z ) is

<!-- formula-not-decoded -->

- (b) The mixed-phase stable system has a system function

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(b) As r → 1 , k 2 → 1 and k 1 →-cos Θ

## 12.17

(a)

12.16

(a)

<!-- formula-not-decoded -->

First, we determine the reflection coefficients. Clearly, k 3 = -1, whcih implies that the roots of A 3 ( z ) are on the unit circle. We may factor out one root. Thus,

<!-- formula-not-decoded -->

Hence, the roots of A 3 ( z ) are z = 1 , α, and α ∗ . (b) The autocorrelation function satisfies the equations

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(c) Note that since k 3 = -1, the recursion E f m = E f m -1 (1 -| k m | 2 ) implies that E f 3 = 0. This implies that the 4x4 correlation matrix Γ xx is singular. Since E f 3 = 0, then σ 2 w = 0

## 12.18

<!-- formula-not-decoded -->

Use the Levinson-Durbin algorithm

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(a)

12.20

<!-- formula-not-decoded -->

is the minimum-phase solution. The difference equation is

<!-- formula-not-decoded -->

where w ( n ) is a white noise sequence with zero mean and unit variance. (b) If we choose

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 12.21

<!-- formula-not-decoded -->

where B p -1 ( z ) is the reverse polynomial of A p -1 ( z ).

For | k p | = 1, A p ( z ) is symmetric, which implies that all the roots are on the unit circle.

For | k p | &lt; 1, we have all the roots inside the unit circle as previously shown.

For | k p | &gt; 1, A p ( z ) = A s ( z ) + /epsilon1B p -1 ( z ) z -1 , where A s ( z ) is the symmetric polynomial with all the roots on the unit circle and B p -1 ( z ) has all the roots outside the unit circle. Therefore, A p ( z ) will have all its roots outside the unit circle.

## 12.22

## 12.23

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

= 0 , by the orthogonality property

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

E [ f i ( n ) f j ( n )] = E { f i ( n )[ x ( n ) + j ∑ k =1 a j ( k ) x ( n -k )] } = E { f i ( n ) x ( n ) } = E i = E max( i, j ) where i &gt; j has been assumed (e)

<!-- formula-not-decoded -->

when 0 ≤ t ≤ i -j, x ( n -t -1) , x ( n -t -2) , . . . , x ( n -t -j ) are just a subset of x ( n -1) , x ( n -2) , . . . , x ( n -i ) Hence, from the orthogonality principle,

<!-- formula-not-decoded -->

Also, when -1 ≥ t ≥ i -j holds, via the same method we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

when 0 ≤ t ≤ i -j, { x ( n -t ) , x ( n -t -1) , . . . , x ( n -t -j ) } is a subset of { x ( n ) , . . . , x ( n -i +1) } Hence, from the orthogonality principle,

<!-- formula-not-decoded -->

Also, when 0 ≥ t ≥ i -j +1 we obtain the same result (g)

/negationslash

(h)

(i)

(j)

(k)

<!-- formula-not-decoded -->

suppose i &gt; j

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 12.24

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 12.25

suppose i &gt; j

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Therefore, k 2 = -γ xx (2)+ k 1 γ xx (1) γ xx (0)+ k ∗ 1 γ xx (1) = γ xx (0) γ xx (2) -γ 2 xx (1) γ 2 xx (1) -γ 2 xx (0) Let,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where A = γ xx (3) + k 1 γ xx (2) + k 1 k 2 γ xx (2) + k 2 γ xx (1) , and B = k 2 γ xx (3) + k 1 k 2 γ xx (2) + k 1 γ xx (2) + γ xx (1)

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This is the same result obtained from the Levinson Algorithm.

## 12.26

The results of section 11.1 apply directly to this problem. We may express Γ xx ( f ) as

<!-- formula-not-decoded -->

where H ( f ) is a filter with transfer function

<!-- formula-not-decoded -->

The prediction error filter whitens the input process, so that the output process is white with spectral density σ 2 w = exp[ v (0)]. Therefore, the minimum MSE is

<!-- formula-not-decoded -->

12.27

12.28

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(b)Refer to fig 12.28-1

## 12.29

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

Figure 12.28-1:

<!-- formula-not-decoded -->

where the last step follows from prob. 12.24 property (g)

## 12.30

<!-- formula-not-decoded -->

## 12.32

Refer to fig 12.32-1 h t ( n ) mininizes E [ e 2 ( n )] (wiener filter) length M = 2 (a)

<!-- formula-not-decoded -->

Refer to fig 12.31-1

<!-- image -->

Figure 12.31-1:

Figure 12.32-1:

<!-- image -->

<!-- formula-not-decoded -->

We can either formally invert this z-transform, or use the following idea: The inverse ztransform of 12.1 will have the form

<!-- formula-not-decoded -->

From the AR model for s ( n ) it is easy to show

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

So the normal equations are

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 12.33

## 12.34

Using quantities in prob. 12-33,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Increasing the length of the filter decreases the MMSE.

## 12.36

## 12.37

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

x ( n )is ARMA(p,p). Suppose

Comparing parameters of the two numerators

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

There are p +1 equations in p +1 unknown parameters σ 2 n , b p (1) , . . . , b p ( p ). Note that b p (0) = 1.

## Chapter 13

## 13.1

By carrying out the minimization we obtain the set of linear equations:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where,

## 13.2

If we assume the presence of a near-end echo only, the received signal is

<!-- formula-not-decoded -->

The receiver filter eliminates the noise outside the frequency band occupied by the signal and after sampling at the symbol rate we obtain,

<!-- formula-not-decoded -->

If we assume that the delay d 1 is a multiple of the symbol time interval, that is, d 1 = DT s , then,

The LS criterion minimizes

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

∣ ∣ The equations for the coefficients of the adaptive echo canceler are

<!-- formula-not-decoded -->

where,

## 13.3

Assume that the sample autocorrelation and crosscorrelation are given by the unbiased estimates:

<!-- formula-not-decoded -->

Then,

<!-- formula-not-decoded -->

Since E [ w 2 ( n -l ) w 3 ( n -k )] = 0, we obtain

<!-- formula-not-decoded -->

or

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Further simplifications are obtained if w 1 , w 2 , w 3 are white and x is uncorrelated with w 2 .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 13.4

We need to prove that

<!-- formula-not-decoded -->

Thus,

But,

Hence,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

From the definition of K m +1 ( n ) in (13.3.29) we obtain

<!-- formula-not-decoded -->

## 13.5

We need to prove that

By definition

Use the relations:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 13.6

## 13.7

We will derive the FAEST algorithm in Table 13.7 line by line. The alternative Kalman gain is defined as

From (13.2.74)

<!-- formula-not-decoded -->

Define ˜ a m ( n ) = 1 /a m ( n ). Then,

<!-- formula-not-decoded -->

FAEST-line 1:

FAEST-line 2:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

FAEST-line 3: From (13.3.50)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

FAEST-line 4: From (13.3.83)

<!-- formula-not-decoded -->

But a m -1 ( n -1) f ∗ m -1 ( n ) = ˜ f ∗ m -1 ( n, n ), thus,

<!-- formula-not-decoded -->

FAEST-line 5:

<!-- formula-not-decoded -->

Use the partition (13.3.32) to write

<!-- formula-not-decoded -->

Thus,

<!-- formula-not-decoded -->

FAEST-line 6: We need to find the update formula for the step ˜ K m +1 ( n +1) -→ ˜ K m ( n +1) .

<!-- formula-not-decoded -->

Using partition (13.3.27) we obtain

<!-- formula-not-decoded -->

Thus,

Write

<!-- formula-not-decoded -->

We identify

<!-- formula-not-decoded -->

FAEST-line 7: Using the partition of ˜ K m ( n ) in step-6 we obtain

<!-- formula-not-decoded -->

C m -1 ( n ) = K m -1 ( n ) + ˜ c mm ( n ) b m -1 ( n -1) = ⇒ K m -1 ( n ) = C m -1 ( n ) -˜ c mm ( n ) b m -1 ( n -1) FAEST-line 8: From (13.3.91)

<!-- formula-not-decoded -->

But, a m ( n ) = 1 / ˜ a m ( n ) and f m -1 ( n ) = ˜ f m -1 ( n, n )˜ a m -1 ( n -1). Thus,

<!-- formula-not-decoded -->

FAEST-line 9: ˜ a m ( n ) = 1 + ˜ K t m ( n ) X m ( n ) . If we use the partition of step-6 then

<!-- formula-not-decoded -->

FAEST-line 10: From (13.3.61)

<!-- formula-not-decoded -->

FAEST-line 11: From (13.3.84)

<!-- formula-not-decoded -->

But, g m ( n ) a m ( n ) = ˜ g m ( n, n ), so that,

<!-- formula-not-decoded -->

FAEST-line 12: The time-update of b m ( n ) is given by (13.3.51)

<!-- formula-not-decoded -->

But, K m ( n ) = ˜ K m ( n ) a m ( n ) and a m ( n ) g m ( n ) = ˜ g m ( n, n ), so that

<!-- formula-not-decoded -->

FAEST-line 13: By definition e M ( n ) = d ( n ) -h t m ( n -1) X m ( n ) FAEST-line 14,15: From (13.2.76)

<!-- formula-not-decoded -->

where,

<!-- formula-not-decoded -->

where

Thus, where,

<!-- formula-not-decoded -->

Since R m is Hermitian, it assumes the decomposition R m = U Λ U H , where Λ is a diagonal matrix with elements λ k , 0 ≤ k ≤ m -1, the eigenvalues of R m , and U is a normalized modal matrix such that UU H = I .

Thus, or

or

## 13.9

<!-- formula-not-decoded -->

The complex gradient vector is ∂ε ( n ) /∂h H M :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Premultiplying the above by U H we obtain

<!-- formula-not-decoded -->

where h 0 m ( n +1) = U H E [ h m ( n +1)], r 0 m = U H r m . The values of /triangle that ensure convergence of the mean of the coefficient vector should satisfy

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Then, in the steepest-descent method, we update the coeficient vector as follows:

<!-- formula-not-decoded -->

## 13.10

The normalized LMS algorithm is given as:

<!-- formula-not-decoded -->

DEfine the error vector ε ( n ) as

<!-- formula-not-decoded -->

Also, define the mean square derivation of the error vector as

Then,

Hence,

<!-- formula-not-decoded -->

We observe that the mean square derivation decreases exponentially with an increase in n , provided that

Approximation:

and

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

With the approximations, we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We can reduce the number of computations needed by m -1 multiplications if we avoid the update of the Kalman gain

<!-- formula-not-decoded -->

If we use the alternative Kalman gain this step takes the form

<!-- formula-not-decoded -->

As in the a-priori case, the update of the alternative Kalman gain vector ˜ K m ( n ), is carried out in two steps,

<!-- formula-not-decoded -->

using the following Levinson-type recursions:

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

With ˜ K m ( n ) we associate the scalar ˜ a m ( n )

<!-- formula-not-decoded -->

This parameter is updated as (see prob. 13.8)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

FAST RLS algorithm: Version A (a-posteriori version)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Initialization:

<!-- formula-not-decoded -->

In this version we need 5 extra multiplications for the calculation of f m -1 ( n ) ˜ a m -1 ( n -1) , | f m -1 ( n ) | 2 wE f m -1 ( n -1) , g m -1 ( n )˜ c mm ( n ), g m -1 ( n ) ˜ a m -1 ( n -1) , e m ( n ) ˜ a m ( n ) and we save m multiplications from the estimation of ˜ K m -1 ( n ). FAST RLS algorithm: Version B (a-posteriori version)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Initialization:

<!-- formula-not-decoded -->

In this version we need 3 extra multiplications for the calculation of f m -1 ( n ) ˜ a m -1 ( n -1) , g m -1 ( n ) ˜ a m -1 ( n -1) , e m ( n ) ˜ a m ( n ) and we save m multiplications from the estimation of ˜ K m -1 ( n ).

## 13.12

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 13.13

Let

The sequence { h k } is related to the sequence { H n } by the inverse discrete Fourier transform

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

When h k , given above is substituted in the expression for H ( z ) the double sum that results can be simplified to yield

<!-- formula-not-decoded -->

The filter structure is shown in Fig. 13.13-1.

1. Let y k ( n ) be the output at time t = nT of the filter with transfer function

<!-- formula-not-decoded -->

Figure 13.13-1:

<!-- image -->

Then the response of the recursive filter at t = nT is

<!-- formula-not-decoded -->

where { H k ( n ) } are the filter coefficients at t = nT . If e ( n ) = d -ˆ d ( n ) then, an algorithm for adjusting the coefficients H k ( n ) is given by

<!-- formula-not-decoded -->

2. The cascade of the comb filter 1 -z -M M with each of the single-pole filter forms a system with frequency response

Thus,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

∣ ∣ ∣ ∣ We observe that | H k ( f ) | = 0 at the frequencies f = n/M , n = k and | H k ( f ) | = 1 at f = k/M .

/negationslash

Thus, the k th system has a resonant frequency at f = k/M , and it is zero at the resonant frequencies of all the other systems. This means that if the desired signal is

<!-- formula-not-decoded -->

the coefficient of each single-pole filter can be adjusted independently without any interaction from the other filters.

## 13.14

Thus,

<!-- formula-not-decoded -->

1. For an overdamped system,

## 13.15

Normal Equations:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

2. Fig. 13.14-1 contains a plot of J ( n ) vs. n . The step /triangle was set to 0 . 5 and the initial value of h was set to 0. In Fig. 13.14-2 we have plotted J ( h ( n )) vs. h ( n ). As it is observed from the figures the minimum value of J which is -372, is reached within 5 iterations of the algorithm.

Figure 13.14-1:

<!-- image -->

<!-- formula-not-decoded -->

Figure 13.14-2:

<!-- image -->

<!-- formula-not-decoded -->

Power spectral density of v 2 ( n ):

<!-- formula-not-decoded -->

Thus,

Hence,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Assuming that x ( n ), w 1 ( n ), w 2 ( n ), w 3 ( n ) are mutually uncorrelated, it follows that

<!-- formula-not-decoded -->

where h ( k ) = 0 . 5 k . Thus,

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

The normal equations take the form

<!-- formula-not-decoded -->

## 13.16

<!-- formula-not-decoded -->

But,

<!-- formula-not-decoded -->

Thus, we obtain the system with solution a 1 = a , a 2 = 0.

<!-- formula-not-decoded -->

Figure 13.15-1:

<!-- formula-not-decoded -->

## 13.17

The optimum linear predictor in Prob. 13.16 is a first order filter with transfer function

<!-- formula-not-decoded -->

Thus, the corresponding lattice has one stage with the forward and backward errors given by

<!-- formula-not-decoded -->

Since f 0 ( n ) = b 0 ( n ) = x ( n ), we obtain

<!-- formula-not-decoded -->

Comparing with the prediction error:

<!-- formula-not-decoded -->

we identify K as -a .

Figure 13.17-1:

<!-- image -->

<!-- formula-not-decoded -->

## 13.18

where y ( n ) is the input of the adaptive FIR filter B ( z )

<!-- formula-not-decoded -->

where s ( n ) is the output of the system C ( z ).

If x ( n ) is white with variance σ 2 x then,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

If x ( n ) and w ( n ) are uncorrelated then,

<!-- formula-not-decoded -->

Thus, we obtain the system:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Solving for k M , we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

With σ 2 x and σ 2 w known, we can determine b 0 , b 1 .

## 13.19

(a)

Therefore,

<!-- formula-not-decoded -->

where

Now,

Then,

<!-- formula-not-decoded -->

But k m ( n ) = u m ( n ) /v m ( n ). Therefore,

<!-- formula-not-decoded -->

and, then

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Chapter 14

## 14.1

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

14.3

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 14.4

Assume that x ( n ) is the output of a linear system excited by white noise input w ( n ), where σ 2 x = 1. Then p xx ( f ) = Γ xx ( f ) p ww ( f ). From prob. 12.3, (a), (b) and (c), we have

<!-- formula-not-decoded -->

## 14.5

<!-- formula-not-decoded -->

Note that this is just the Goertzel algorithm for computing the DFT. Then,

<!-- formula-not-decoded -->

## 14.6

From (14.2.18) we have

<!-- formula-not-decoded -->

by the definition of U in (14.2.12)

## 14.7

- (a) (1) Divide x ( n ) into subsequences of length M 2 and overlapped by 50% to produce 4 k subsequences. Each subsequence is padded with M 2 zeros.
- (2) Compute the M-point DFT of each frame or subsequence.
- (3) Compute the magnitude square of each DFT.
- (4) Average the 4 k M-point DFT's.
- (5) Perform the IDFT to obtain an estimate of the autocorrelation sequence. (b)

<!-- formula-not-decoded -->

- (c) Instead of zero-padding, we can combine two subsequences to produce a single M-point subsequence and thus reduce the number of sequences form 4 k to 2 k . Then, we use the relation in (b) for the DFT.

## 14.8

<!-- formula-not-decoded -->

- /triangle (b) From (14.2.53), the quality factor is Q B = 1 . 1 N /triangle f . This expression does not depend on M ; hence, there is no advantage to increasing the value of M beyond 90.

## 14.9

- (a) From table 14.1, we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For the Bartlett estimate,

<!-- formula-not-decoded -->

For the Welch estimate with 50% overlap,

<!-- formula-not-decoded -->

For the Blackman-Tukey estimate,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 14.10

- (a) Suppose P ( i ) B ( f ) is the periodogram based on the Bartlett method. Then,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 14.11

Let R ( i ) xx be defined as follows:

<!-- formula-not-decoded -->

Then,

## 14.12

To prove the recursive relation in (12.3.19) we make use of the following relations:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We substitute for f m ( n ) and g m ( n -1) from (2) into (1), and we expand the expressions. Then, use the relations for ˆ E m -1 and ˆ k m to reduce the result.

## 14.13

To determine the autocorrelation, we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

14.14

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 14.16

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) The maximum phase system is H ( z ) = 1 √ 62 (1 -5 z -1 +6 z -2 )
- (c) There are two possible mixed-phase systems: H 1 ( z ) = 1 √ 62 (3 -7 z -1 + 2 z -2 ) H 2 ( z ) = 1 √ 62 (2 -7 z -1 +3 z -2 )

## 14.17

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 14.18

proof is by contradiction.

(a) Assume the | k m | &gt; 1. Since E m = (1 - | k m | 2 ) E m -1 , this implies that either E m &lt; 0 or E m -1 &lt; 0. Hence, σ 2 w &lt; 0, and is not positive definite.

<!-- formula-not-decoded -->

(b) From the Schur-Cohn test, A p ( z ) is stable if | k m | &lt; 1. Hence, the roots of A p ( z ) are inside the unit circle.

## 14.19

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The values of the parameters d m = q ∑ k =0 b k b k + m are as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) The MA (2) , MA (4) and MA (8) models have spectra that contain negative values. On the other hand, the spectrum of the AR process is shown below. Clearly, the MA models do not provide good approximations to the AR process. Refer to fig 14.19-1.

## 14.20

<!-- formula-not-decoded -->

Figure 14.19-1:

<!-- image -->

<!-- formula-not-decoded -->

The solution is

<!-- formula-not-decoded -->

Refer to fig 14.20-1.

## 14.21

(a) (1)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 14.20-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (b) Refer to fig 14.21-1. (c) For (2),

<!-- formula-not-decoded -->

/negationslash

For (3), the AR process has coefficients a 0 = 1 , a 1 = 0 and a 2 = 0 . 81.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 14.21-1:

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 14.22

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(b) The inverse system is

This is a stable system.

## 14.24

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

14.26

14.27

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Hence, y ( n ) is an ARMA(p,p) process

<!-- formula-not-decoded -->

14.28

(a)

<!-- formula-not-decoded -->

(b)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Thus, a is an eigenvector corresponding to the eigenvalue λ . Substitute Γ yy a = λa into E . Then, E = λ . To minimize E , we select th smallest eigenvalue, namely, σ 2 w .

## 14.30

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 14.31

(a) To determine the optimum filter that minimizes σ 2 y subject to the constraint, we differentiate ε ( h ) with respect to h H (compute the complex gradient):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Thus,

.

(b) To solve for the Langrange multipliers using the constraint, we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By substituting for µ ∗ in the result given in (a) we obtain the optimum filter as

<!-- formula-not-decoded -->

Thus,

## 14.32

The periodogram spectral estimate is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where

By substituting X ( f ) into P xx ( f ), we obtain

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Then,

## 14.33

We use the Pisasenko decomposition method. First, we compute the eigqnvalues of the correlation matrix.

<!-- formula-not-decoded -->

Thus, λ = 5 , 3 , 1 and the noise varinace is λ min = 1. The corresponding eigenvector is

<!-- formula-not-decoded -->

The frequency is found from the equation 1 + z -2 = 0 ⇒ z = ± j . Therefore, e jw = ± j yields w = ± π/ 2 and the power is P = 2.

## 14.34

The eigenvalues are found from

∣ and the normalized eigenvectors are

<!-- formula-not-decoded -->

By computing the denominator of (14.5.28), we find that the frequency is ω = π/ 2 or f = 1 / 4. We may also find the frequency by using the eigenvectors v 2 and v 3 to construct the two polynomials (Boot Music Method):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Then, we form the polynomials

<!-- formula-not-decoded -->

It is easily verified that the polynomial has a double root at z = j or, equivalently, at ω = π/ 2. The other two roots are spurious roots that are neglected. Finally, the power of the exponential signal is P 1 = 1.

## 14.35

The denominator can be expressed as

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 14.36

(a) V k ( z ) = ∑ M -1 n =0 v k ( n +1) z -n and V k ( f ) = V k ( z ) | z = e j 2 πf Then, the denominator in P MUSIC ( f ) may be expressed as

<!-- formula-not-decoded -->

- (b) For the roots of Q ( z ), we consruct (from Problem 14.34) Q ( z ) as

<!-- formula-not-decoded -->

Thus polynomial has a double root at z = j and two spurious roots. Therefore, the desired frequency is ω = π/ 2.

## 14.37

(a)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(c) As M increases, the SNR increases.

## 14.38

Refer to fig 14.38-1.

## 14.39

Refer to fig 14.39-1.

Figure 14.39-1:

<!-- image -->

## Corrections to Digital Signal Processing, 4 t h Edition

## by John G. Proakis and Dimitris G. Manolakis

1. Page 18, two lines below equation (1.3.18)

sk(n) should be s k (n)

2. Page 34, Figure 1.4.8

The quantized value of the signal between 2T and 3T should be 4GLYPH&lt;0&gt;

3. Page 66, line below equation (2.2.43)

'is relaxed' should be 'is non-relaxed'

4. Page 101, last term of equation (2.4.24)
2. n GLYPH&lt;0&gt; n should be    GLYPH&lt;0&gt; N
5. Page 147, last sentence above Section 3.1

Move this sentence to line above, just before the word 'Finally, '

6. Page 161, figure 5.2.1

The mapping is w = a -1 z

7. Page 237, line 2 from the top of page

'radian' should be 'radial'

8. Page 321, Figure 5.2.3, magnitude plot

Scale on the ordinate should be multiplied by 5

9. Page 387, line 8 below equation (6.1.15)

X(Fs ) should be X(F)

10. Page 390, Figure 6.1.3(b)

X(F/Fs ) should be X(F)

11. Page 391, Figure 6.1.5 upper right-hand part of the figure X(F/Xf ) should be X(F)
12. Page 396, Figure 6.2.3, graph of Y(F)

For F&lt;0, the F s on the abscissa should be -F s

13. Page 424, two lines below equation (6.4.68)

The word 'envelop' should be 'envelope'

14. Page 454, equation on line above Section 7.1.2

<!-- formula-not-decoded -->

- 15.Page 463, line below equation (7.1.39)

<!-- formula-not-decoded -->

- 16.Page 506, problem 7.23(e)

The exponent should be j(2GLYPH&lt;0&gt;  /N) k o n

17. Page 526, Figure 8.1.10

Delete the factor of 2 in the expression for B

18. Page 582, line 4 from the top

<!-- formula-not-decoded -->

19. Page 646, Problem 9.22

In the denominator of H(z), the term r2 should be r 2

20. Page 672, two lines below equation (10.2.35)

<!-- formula-not-decoded -->

21. Page 679, line above equation (10.2.52) and in equation (10.2.52)

Add the term

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

22. Page 680, line above Case 4:

The equation should be

<!-- formula-not-decoded -->

23. Page 725, Figure 10.3.14, graph on left

The value of 1 is the peak value

24. Page 742, problem 10.2.3, lines 4 and 6

Add subscripts l and u on the expressions for GLYPH&lt;0&gt;

H(s) should b H a (s)

25. Page 809, equation (11.12.15)

<!-- formula-not-decoded -->

26. Page 811, in Solution of example 11.12.1

The matrix for G 0 (z), G 1 (z) and G 2 (z) should be transposed

Thus,

<!-- formula-not-decoded -->

27. Page 818, problem 11.16

Change the statement of the problem to the following:

Use the result in Problem 11.15 to determine the type II form of the I=3 interpolator in Figure 11.5.12(b)

28. Page 821, third line from bottom of page

Should be f 0 = 1/6 and GLYPH&lt;0&gt; f = 1/3

29. Page 958, problem 13.19

In the expression for the least squares error, f(m)n should be f m ( l )    and    gm(n) should be g m ( l

30. Page 962, equations (14.1.6), (14.1.7) and (14.1.8)

X(F/X(F)) should be X(F)

31. Page 964, in Solution of Example 14.1.1, line 2

Figure 10.2.2(a) should be Figure 10.2.2

32. Page 1038, problem 14.35

In the denominator of the equation, v k v k should be v k v k H

)