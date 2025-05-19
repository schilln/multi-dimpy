# Introduction to dimensioned linear algebra

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

## Terminology and notation

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

## Vectors

When is a dot product between column vectors defined?
Assuming
$
\mathbf a
= \begin{bmatrix}
  \mathbf a_1 & \mathbf a_2 & \ldots & \mathbf a_n
\end{bmatrix}^\top
\in \mathbb R^n
$
(and similar for $\mathbf b$),
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
$
\mathbf a^\sim
\coloneqq \begin{bmatrix}
  \mathbf a_1^\sim & \cdots & \mathbf a_n^\sim
\end{bmatrix}
$.
(Note that the shape is *transposed*, so the dimensional inverse of a column vector is a row vector).
It follows that $\mathbf a^\sim \mathbf a \sim 1$.

Then we can restate the requirement for to vectors to have a dot product:
$\mathbf a^\top \mathbf b$ is defined exactly when $\mathbf a \approx \mathbf b^{\sim \top}$.

### Examples of vector dot products

$$
\begin{align*}
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
\end{align*}
$$

In the first example, observe that $\mathbf a \sim \text{m s } \cdot \mathbf b^{\sim \top}$ (so $\mathbf a \approx \mathbf b^{\sim \top}$),
and in the second example $\mathbf a \sim 1 \cdot \mathbf b^{\sim \top}$, but in the third example there is no dimensioned $c$ such that $\mathbf a \sim c \mathbf b^{\sim \top}$.

## Matrices

We're finally ready to discuss dimensioned matrices.
First recall from [Vectors](#vectors) how we defined two vectors having the ***same dimensional form*** or being ***dimensionally parallel*** in terms of corresponding components.
Likewise the ***dimensional inverse*** of a matrix is obtained by inverting the dimensions of components and then taking the transpose of the matrix.

When is the product of two matrices defined?
Again assuming $\mathbf a_{(i)}, \mathbf b_{(j)} \in \mathbb R^n$ for all $i, j$, we'll define two matrices $\mathbf A$ and $\mathbf B$ in terms of the $\{\mathbf a_{(i)}\}$ and $\{\mathbf b_{(j)}\}$:
$$
\begin{align*}
  \mathbf A
  &= \begin{bmatrix}
    \mathbf a_{(1)}^\top \\
    \vdots \\
    \mathbf a_{(m)}^\top
  \end{bmatrix} \in M_{m \times n} \\\\

  \mathbf B
  &= \begin{bmatrix}
    \mathbf b_{(1)} & \cdots & \mathbf b_{(k)}
  \end{bmatrix} \in M_{n \times k}.
\end{align*}
$$
Then the $(i, j)$ entry of the product $\mathbf A \mathbf B$ is
$$
[\mathbf A \mathbf B]_{i, j} = \mathbf a_{(i)}^\top \mathbf b_{(j)}
$$
which we know is defined exactly when $\mathbf a_{(i)} \approx \mathbf b_{(j)}^{\sim \top}$.
For a fixed $j$, this must be true for all $i$, so $\mathbf b_{(1)}^{\sim \top} \approx \mathbf a_{(1)} \approx \cdots \approx \mathbf a_{(m)}$.
So all the rows of $A$ are dimensionally parallel, and we can write
$$
A
\sim \begin{bmatrix}
  1 \\ c_2 \\ \vdots \\ c_m
\end{bmatrix}
[\text{the first row of A}]
= \mathbf c \mathbf a_{(1)}^\top
$$
where
$
\mathbf c
= \begin{bmatrix}
  1 & c_2 & \cdots & c_m
\end{bmatrix}^\top
$
is a dimensioned column vector.

The important point is that for $A$ to be multiplied on the right by a matrix, its dimensional form must be representable as an outer product.
It is useful to write this as $A \sim \mathbf u \mathbf v^\sim$ for some $\mathbf u, \mathbf v$.
We may likewise find that for $\mathbf B$ to be multiplied on the left by a matrix, we must have $\mathbf B \sim \mathbf x \mathbf y^\sim$ for some $\mathbf x, \mathbf y$.
Furthermore, we find
$$
\begin{align*}
  \mathbf A \mathbf B
  &\sim (\mathbf u \mathbf v^\sim)(\mathbf x \mathbf y^\sim) \\
  &\sim \mathbf u (\mathbf v^\sim \mathbf x) \mathbf y^\sim
\end{align*}
$$
which is defined exactly when $\mathbf x \approx \mathbf v$ (since $\mathbf (\mathbf v^\sim \mathbf x)^\top = \mathbf x^\top \mathbf v^{\sim \top}$).

<!-- TODO: Cite book again. -->
