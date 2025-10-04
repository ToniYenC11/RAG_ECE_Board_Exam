## Polar form

The polar form combines each sine-cosine pair at the frequency nf into a single sinusoid:

<!-- formula-not-decoded -->

Here, C0  = 𝐴 0 ,  and Cn , θn are  the  polar  coefficients  and  are  related  to  the trigonometric coefficients 𝐴 n and Bn . This relationship is best found by comparing the phasor representation of the time-domain terms such that

<!-- formula-not-decoded -->

## FOURIER SERIES

Named after  its  developer  Jean-Baptiste  Joseph  Fourier,  the  Fourier  series describes  periodic  signals  by  combinations  of  harmonic  signals  or  sinusoids.  This representation unfolds a perspective of periodic signals in the frequency domain  in terms of their frequency content or spectrum.

## The Three Forms of the Fourier Series

## Trigonometric form

The trigonometric form represents the Fourier series as an algebraic sum of pairs of cosine and sine terms with a present dc component:

<!-- formula-not-decoded -->

The constant term 𝐴 0 accounts for any dc offset in x(t) , and 𝐴 0 , An and Bn are called the trigonometric Fourier series coefficients.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Exponential form

The exponential form invokes Euler's relation express each sine-cosine pair at the frequency nƒ by complex exponentials at  nƒ :

<!-- formula-not-decoded -->

Here the index n ranges from - ∞  to  ∞  and 𝑋0 = 𝐶0 = 𝐴 0 , where

<!-- formula-not-decoded -->

The coefficient X-n is simply the complex conjugate of Xn :

<!-- formula-not-decoded -->

How are the Fourier series Coefficients related?

<!-- image -->

Evaluating Xn directly is found as follows:

<!-- formula-not-decoded -->

Invoking Euler's relation , 𝑐𝑜𝑠(2𝜋𝑛𝑓𝑡) - 𝑗𝑠𝑖𝑛(2𝜋𝑛𝑓𝑡) = 𝑒 𝑗2𝜋𝑛𝑓𝑡 , to obtain

<!-- formula-not-decoded -->

The beauty of these results is that each coefficient is unique for any value of n, is computed independently and does not affect others.