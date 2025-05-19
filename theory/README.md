# Overview

It should be clear that sums of quantities with different dimensions are not always defined.
Letting $\text m$ denote meters and $\text s$ denote seconds, we see that

$$
1 \text{ m} + 2 \text{ m} = 3 \text{ m},
$$

but

$$
1 \text{ m} + 2 \text{ s} = \;?
$$

In what follows we'll be concerned with the *physical dimensions* of scalars, vectors, and matrices, not their *numeric* components, so while the definitions are stated when working with real numbers $(\mathbb R)$, we could as easily work with complex numbers $(\mathbb C)$.

# Terminology and notation

Denote the physical dimension of a scalar with $\sim$;
for example, if $a$ represents a quantity of meters, write $a \sim \text{meters}$.
Thus, $a + b$ is defined exactly when $a \sim b$.
In this case we say $a$ and $b$ have the ***same dimensional form***.
We write the ***dimensionless*** quantity as simply $1$.

Additionally, we say $a$ and $b$ are ***dimensionally parallel*** if there is some dimensioned scalar $c$ such that $a \sim c b$.
We write this as $a \approx b$.

It'll also be useful to define the ***dimensional inverse*** of a scalar, denoted $a^\sim$ and defined by $a^\sim a \sim a a^\sim \sim 1$.
That is, the product of a scalar and its dimensional inverse is dimensionless.
For example, if $a \sim \text{ m} \cdot \text{s}^{-1}$, then $a^\sim \sim \text{ m}^{-1} \cdot \text{s}$.

# Vectors

When is a dot product between vectors defined?
Assuming $\mathbf a = [\mathbf a_1, \mathbf a_2, \ldots, \mathbf a_n]^\top \in \mathbb R^n$ (and similar for $\mathbf b$),
$$
\mathbf a \cdot \mathbf b
= \mathbf a^\top \mathbf b
= \sum_{i=1}^n \mathbf a_i \mathbf b_i,
$$
which is defined exactly when $\mathbf a_i \mathbf b_i \sim \mathbf a_j \mathbf b_j$ for all $i, j$, or equivalently, there is some dimensioned scalar $c$ such that $\mathbf a_i \mathbf b_i \sim c$ for all $i$ (in which case $\mathbf a^\top \mathbf b \sim c$).
This is true exactly when $\mathbf a_i \sim c \mathbf b_i^\sim$, (i.e., $\mathbf a_i \approx \mathbf b_i^\sim$) for all $i$.
(Note it is true that $\mathbf a_i \approx \mathbf b_i$ for all $i$, but it'll be more useful to write it the former way.)

We may extend the definitions of having the ***same dimensional form*** and being ***dimensionally parallel*** to vectors (and later to matrices) by requiring that, for two vectors (of the same shape), their corresponding components have the same dimensional form or are dimensionally parallel, respectively.
We also extend the definition of ***dimensional inverse***:
$\mathbf a^\sim \coloneqq [\mathbf a_1^\sim, \cdots, \mathbf a_n^\sim]$.
(Note that the shape is *transposed*, so the dimensional inverse of a column vector is a row vector).
It follows that $\mathbf a^\sim \mathbf a \sim 1$.

Then we can restate the requirement for to vectors to have a dot product:
$\mathbf a^\top \mathbf b$ is defined exactly when $\mathbf a \approx \mathbf b^{\sim \top}$.

## Examples of vector dot products

$$
\begin{align}
\mathbf a
&= \begin{bmatrix}
1 \text{ m} \\ 2 \text{ m} \\ 3 \text{ m}
\end{bmatrix} \\
\mathbf b
&= \begin{bmatrix}
1 \text{ s} \\ 2 \text{ s} \\ 3 \text{ s}
\end{bmatrix} \\
\mathbf a^\top \mathbf b
&= 1 \text{ m} \cdot \text{s}
+ 4 \text{ m} \cdot \text{s}
+ 9 \text{ m} \cdot \text{s} \\
&= 14 \text{ m} \cdot \text{s} \\\\

\mathbf a
&= \begin{bmatrix}
1 \text{ m}^1 \\ 2 \text{ m}^2 \\ 3 \text{ m}^3
\end{bmatrix} \\
\mathbf b
&= \begin{bmatrix}
1 \text{ m}^{-1} \\ 2 \text{ m}^{-2} \\ 3 \text{ m}^{-3}
\end{bmatrix} \\
\mathbf a^\top \mathbf b
&= 1 \text{ m}^1 \cdot \text{m}^{-1}
+ 4 \text{ m}^2 \cdot \text{m}^{-2}
+ 9 \text{ m}^3 \cdot \text{m}^{-3} \\
&= 14 \\\\

\mathbf a
&= \begin{bmatrix}
1 \text{ m}^1 \\ 2 \text{ m}^2 \\ 3 \text{ m}^3
\end{bmatrix} \\
\mathbf b
&= \begin{bmatrix}
1 \text{ m}^{-1} \\ 2 \text{ m}^{-1} \\ 3 \text{ m}^{-1}
\end{bmatrix} \\
\mathbf a^\top \mathbf b
&= 1 \text{ m}^1 \cdot \text{m}^{-1}
+ 4 \text{ m}^2 \cdot \text{m}^{-1}
+ 9 \text{ m}^3 \cdot \text{m}^{-1} \\
&= 1
+ 4 \text{ m}^1
+ 9 \text{ m}^2 \\
&= \; ?
\end{align}
$$

In the first example, observe that $\mathbf a \sim \text{m s } \cdot \mathbf b^{\sim \top}$ (so $\mathbf a \approx \mathbf b^{\sim \top}$),
and in the second example $\mathbf a \sim 1 \cdot \mathbf b^{\sim \top}$, but in the third example there is no dimensioned $c$ such that $\mathbf a \sim c \mathbf b^{\sim \top}$.

---

Dimensionally uniform vector (probably) has a 2-norm (magnitude):

$$
\mathbf p
= \begin{bmatrix}
1 \text{ m} \\ 2 \text{ m}
\end{bmatrix}
= (1 \text{ m}) 
\begin{bmatrix}
1 \\ 2
\end{bmatrix} \\

\lVert \mathbf p \rVert_2
= \sqrt{(1 \text{ m})^2 + (2 \text{ m})^2}
= \sqrt{1 \text{ m}^2 + 4 \text{ m}^2}
= \sqrt{5 \text{ m}^2}
= \sqrt 5 \text{ m}
$$

but otherwise no without additional care:

$$
\mathbf x
= \begin{bmatrix}
1 \text{ volts} \\ 2 \text{ amperes}
\end{bmatrix} \\

\lVert \mathbf x \rVert_2
= \sqrt{(1 \text{ volts})^2 + (2 \text{ amperes})^2}
= \sqrt{1 \text{ volts}^2 + 4 \text{ amperes}^2}
= \; ?
$$
pp. 7–9

<!-- TODO: Cite book again. -->

<!-- TODO: Maybe start from dimensioned vectors, outer products... p. 76 -->
---

Suppose we have two matrices

$$
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}, \qquad
B =
\begin{bmatrix}
s & u & x \\
t & v & y
\end{bmatrix}.
$$

Suppose further that the values in each matrix have *dimensions*, e.g., $x$ has dimensions of length.
What combination of dimensions among the values in $A$ and $B$ allow the matrix multiplication $AB$ to make sense?
That is, matrix multiplication consists of additions of products of the two matrices' entries, so what dimensions allow those additions to be *dimensionally* consistent, so that lengths are being added to lengths and not, say, to masses?

Let's write out the multiplications and additions:

$$
AB =
\begin{bmatrix}
as + bt & au + bv & ax + by \\
cs + dt & cu + dv & cx + dy
\end{bmatrix}.
$$

Say we let the values in $B$ be dimensionless, but at least $a$ has dimensions of length;
we'll denote this by $[a] = \texttt L$, while $[s] = 1$ denotes being dimensionless.
Of course, we must have $[as] = [bt]$ in order to add these two quantities.
Since $[s] = [t] = 1$, we have $[as] = [a] = \texttt L = [b] = [bt]$.
So $a$ and $b$ have the same dimension.
Likewise we can conclude that $c$ and $d$ have the same dimension.
