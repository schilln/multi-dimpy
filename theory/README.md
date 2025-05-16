It should be clear that sums of quantities with different dimensions are not always defined:

$$
1 \text{ m} + 2 \text{ m} = 3 \text{ m},
$$

but

$$
1 \text{ m} + 2 \text{ s} = \;?
$$


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
