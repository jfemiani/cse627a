# Lecture Notes: PRML Chapter 1.4 – The Curse of Dimensionality

## Key Terminology

- **Curse of dimensionality**: A collection of challenges that arise in high-dimensional spaces, including data sparsity, unintuitive geometry, and increased computational cost.

- **Nearest neighbor degradation**: In high dimensions, distances between points concentrate around their mean, making it harder to distinguish close neighbors from far ones — weakening the usefulness of distance-based methods.

- **Volume concentration**: In some high-dimensional distributions (e.g. standard Gaussians), most probability mass lies in a thin shell at a characteristic distance from the origin. This arises when density depends primarily on distance from the origin.

---

## Key Ideas

### 1. Data becomes sparse in high dimensions

- Imagine associating each data point with a small ball of fixed radius $r$.
- In low dimensions, a modest number of such balls can cover a meaningful fraction of the space.
- In high dimensions, you need exponentially more balls to cover the same fraction — because volume increases rapidly with dimension.
- For any fixed number of points, the **fraction of space covered by data becomes vanishingly small** as dimension increases.
- This makes local generalization unreliable unless the dataset size grows exponentially.

---

### 2. Most of the probability mass lies far from the origin

In certain well-behaved high-dimensional distributions — such as the standard multivariate Gaussian — most of the probability mass concentrates in a thin shell at a characteristic distance from the origin.

Let $\mathbf{x} = (x_1, x_2, \dots, x_D)$, where each $x_i \sim \mathcal{N}(0, 1)$ independently.

The squared distance from the origin is:
$$
\|\mathbf{x}\|^2 = x_1^2 + x_2^2 + \dots + x_D^2
$$

Since each $x_i$ has variance 1, the expected value of $x_i^2$ is also 1. Therefore:
$$
\mathbb{E}[\|\mathbf{x}\|^2] = D
$$
and the typical magnitude of a random Gaussian vector in $\mathbb{R}^D$ is approximately:
$$
\|\mathbf{x}\| \approx \sqrt{D}
$$

> This fact has practical implications in machine learning.
> For example, in neural networks and transformers, inputs and weights are often scaled by $1/\sqrt{D}$ to keep dot products and activations within a stable range.

As dimension increases:
- The **average** distance from the origin grows like $\sqrt{D}$
- The **spread** (standard deviation) of these distances grows more slowly
- As a result, samples concentrate in a thin spherical shell

Why does this happen?

It’s due to a **balance between two effects**:
1. Gaussian **density** decreases exponentially as $r$ increases:
   $$
   \text{Density at radius } r \propto e^{-r^2/2}
   $$
2. The **surface area** of a $D$-dimensional sphere increases with $r$:
   $$
   \text{Surface area at radius } r \propto r^{D - 1}
   $$

These combine to produce the radial distribution of mass:
$$
f(r) \propto r^{D - 1} e^{-r^2/2}
$$

This function is maximized at $r \approx \sqrt{D}$. Here's a sketch of the derivation:

Let:
$$
\log f(r) = (D - 1) \log r - \frac{r^2}{2}
$$
Differentiate:
$$
\frac{d}{dr} \log f(r) = \frac{D - 1}{r} - r
$$
Set this to zero:
$$
r^2 = D - 1 \quad \Rightarrow \quad r \approx \sqrt{D}
$$

> **Important clarification**: This does not mean that points lie on a surface.
> Rather, the thin shell at radius $\sqrt{D}$ covers so much surface area that — despite lower density — most of the mass ends up there.
> Meanwhile, the origin, though having highest density, contributes almost no mass due to its vanishing volume in high dimensions.

---

### 3. The center of the space contains negligible volume

Even in uniform distributions, such as over the unit cube $[0,1]^D$, high-dimensional geometry behaves unintuitively.

- The volume of the “central” subcube $[0, 0.5]^D$ is $(0.5)^D$, which vanishes rapidly as $D$ increases.
- To retain 95% of the cube’s volume, nearly the entire length of each axis must be included:
  $$
  s = (0.95)^{1/D} \to 1 \quad \text{as } D \to \infty
  $$
- So central regions that appear "large" in low dimensions contain almost none of the space in high dimensions.

---

## Why It Matters

- **Nearest-neighbor distances collapse**: In high dimensions, the relative difference between the closest and farthest neighbor becomes small. This weakens the performance of algorithms like k-NN and kernel methods.

- **Spatial indexing fails**:  
  Data structures like KD-trees, which give $O(\log N)$ performance in low dimensions, degrade in high dimensions — often reverting to brute-force $O(N)$ behavior.

- **Generalization becomes harder**:  
  Algorithms relying on local neighborhoods require exponentially more data to maintain accuracy as dimension increases.

- **Geometric intuition breaks down**:  
  Concepts from 2D/3D space — like the origin being “central” — become misleading. Most of the mass lies far away from the origin, and uniform sampling fails to adequately populate space.

---

## Relevant Figures from PRML

- **Figure 1.8**:  
  Shows how much of the unit cube must be included along each axis to retain 95% of the volume. As dimension increases, nearly the full cube must be included.

- **Figure 1.9**:  
  Plots the distribution of $\|\mathbf{x}\|^2$ for Gaussian vectors in increasing dimensions. The peak sharpens and shifts outward toward $D$, illustrating the shell effect.
