## Cholesky Factorization

- Partition matrices in A = LL T = U T U

<!-- formula-not-decoded -->

## A = 6 15 55 15 55 225 55 225 979

## U = 2.44949 6.123724 22.45366 0 4.1833 20.9165 0 0 6.110101

## When does a Symmetric matrix not factorable?

## Singular Value Decomposition

## Introduction

- The singular value decomposition of a matrix (usually referred to as the SVD) is the final and best factorization of a matrix:

- where U is orthogonal, Σ is diagonal, and V is orthogonal.
- A can be any matrix.

## Introduction

## · The SVD was invented/discovered by

<!-- image -->

Eugenio Beltrami (1835-1900) (Italy)

Marie E Camille Jordan (1838-1922) (France)

<!-- image -->

James Sylvester (1814-1897) (England)

<!-- image -->

## Introduction

- The SVD was invented/discovered by

Erhard Schmidt (1876-1959) (Germany)

<!-- image -->

Hermann Weyl (1885-1955) (Switzerland)

<!-- image -->

## Thin Singular Value Decomposition

- 𝐴 ∈ 𝑅 𝑚 𝑥 𝑛 , skinny and full rank

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- In matrix form, the above equation is AV = U Σ
- Since V is orthogonal, A = U Σ V T

## Thin Singular Value Decomposition

- The thin SVD for 𝐴 ∈ 𝑅 𝑚 𝑥 𝑛 with Rank(A) = r

<!-- formula-not-decoded -->

<!-- image -->

## Full Singular Value Decomposition

- Adding extra orthonormal columns to U

<!-- formula-not-decoded -->

- Also adding extra rows of zeros to Σ , so

<!-- formula-not-decoded -->

<!-- image -->

## SVD: example

<!-- formula-not-decoded -->

Use [U,S,V] = svd(A) in Matlab

<!-- formula-not-decoded -->

## SVD: example

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SVD: example

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- Hence:
- v i are eigenvectors of A T A while,
- ui are eigenvectors of AA T
- σ i = √ λ i

## SVD and eigenvectors

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SVD Application: Image Compression

<!-- image -->

Rank 384 Sample

<!-- image -->

Rank 50 Sample

<!-- image -->

Rank 200 Sample

<!-- image -->

Rank 25 Sample

<!-- image -->

Rank 100 Sample

<!-- image -->

Rank 10 Sample

<!-- image -->