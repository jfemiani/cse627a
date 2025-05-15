# Lecture Notes: PRML Chapter 6 – Kernel Methods

## Prerequisites
- Familiarity with linear parametric models for regression and classification  
- Understanding of feature‐space mappings φ(x) and the design matrix Φ  
- Regularization and the least‐squares error function  
- Inner products (dot products) and positive‑definite matrices  

## Key Terminology
- **Kernel function**  
  A symmetric function  
  $$k(x,x')=\phi(x)^\top\phi(x')$$  
  corresponding to an inner product in feature space.

- **Linear kernel**  
  $$k(x,x') = x^\top x'\quad(\phi(x)=x)$$  

- **Kernel trick (kernel substitution)**  
  Replacing every $x^\top x'$ in an algorithm with $k(x,x')$ to handle nonlinear mappings implicitly.

- **Dual representation**  
  Expressing model parameters as a linear combination of feature maps at the training points, e.g.  
  $$w = \sum_{n=1}^N a_n\,\phi(x_n).$$

- **Gram matrix**  
  The $N\times N$ matrix $K$ with elements  
  $$K_{nm} = k(x_n,x_m).$$

- **Memory‑based methods**  
  Techniques (e.g., Parzen density estimators, nearest neighbours) that store and use training points at prediction time.

- **Stationary kernel**  
  Invariant to translations:  
  $$k(x,x') = k(x - x').$$

- **Homogeneous (radial basis) kernel**  
  Depends only on distance magnitude:  
  $$k(x,x') = k(\|x - x'\|).$$

## Why It Matters
- **Nonlinear modeling without explicit features:** Kernels enable algorithms to operate in very high—or infinite—dimensional feature spaces without ever computing φ(x) directly.  
- **Unified framework:** Many algorithms (PCA, Fisher discriminant, SVMs, Gaussian processes) can be “kernelized,” extending their power to complex data structures.  
- **Dual formulations:** Allow predictions to be expressed purely in terms of kernels and training targets, often leading to sparser solutions and clear probabilistic interpretations (e.g., Gaussian processes).

## Key Ideas

### 1. Kernel definition and symmetry  
- **Formal definition:**  
  $$k(x,x') = \phi(x)^\top\phi(x')\,. $$  
- **Symmetry:** $k(x,x') = k(x',x)$ by properties of the inner product.

### 2. Dual representation for regularized least squares  
- **Primal objective:**  
  $$J(w) = \tfrac12\sum_{n=1}^N\bigl(w^\top\phi(x_n) - t_n\bigr)^2 + \tfrac\lambda2\,w^\top w.$$
- **Expressing** $w=\Phi^\top a$ **yields**  
  $$a = (K + \lambda I_N)^{-1}t\,,\quad
    y(x) = k(x)^\top (K + \lambda I)^{-1} t.$$
- But what the heck is $k(x)$ with one parameter? $$k(x) = [k_1(x), k_2(x) \dots k_N(x)]^T$$ with $$k_n(x)=k(x_n, x)$$. 
- **Implication:** All computations depend only on $K$ and the kernel vector $k(x)$, not on the (potentially infinite) φ.

### 3. Kernel trick  
- **Idea:** If an algorithm uses only inner products $x^\top x'$, replace with $k(x,x')$.  
- **Examples:** (Not covered ... at least no yet)  
  - Kernel PCA (Schölkopf et al., 1998)  
  - Kernel Fisher discriminant (Mika et al., 1999)  
  - Support vector machines (Boser et al., 1992)

### 4. Constructing kernels  
- **Via feature maps:** Choose φ(x) explicitly and compute  
  $$k(x,x') = \sum_{i=1}^M \phi_i(x)\,\phi_i(x').$$  
- **Direct construction:** Ensure positive definiteness.  
  - **Example:**  
    $$k(x,z) = (x^\top z)^2$$  
    corresponds to the feature map of all pairwise products of components.

### 5. Stationary and homogeneous kernels  
- **Stationary:** $k(x,x') = k(x - x')$  
- **Homogeneous (RBF):** $k(x,x') = k(\|x - x'\|)$  

## Relevant Figures from PRML
- ![alt text](images/fig16.1.png)  
  **Figure 6.1:** Diagram showing the mapping $x\mapsto\phi(x)$ into feature space and the computation of $k(x,x')=\phi(x)^\top\phi(x')$, illustrating how kernels implicitly capture higher‑order feature interactions.



## Learning Outcomes

After studying the kernel‐methods excerpt (Chapter 6, Sections 6.1–6.2), students will be able to:

1. **Define a kernel function** and state its key properties (symmetry, positive‑definiteness).  
2. **Derive the dual coefficient vector** $a$ in regularized least squares in terms of the Gram matrix $K$.  
3. **Interpret the prediction formula**  
   $$
     y(x) \;=\; k(x)^\top\,(K + \lambda I)^{-1}t
   $$  
   and explain the role of the kernel vector $k(x)$.  
4. **Apply the kernel trick**, recognizing which algorithms can or cannot be “kernelized” by replacing dot‑products with $k(x,x')$.  
5. **Identify and classify common kernels** (linear, polynomial, Gaussian RBF, sigmoid) and distinguish stationary vs. non‑stationary kernels.  
6. **Construct explicit feature maps** for simple polynomial kernels (e.g.\ for $k(x,z)=(x^\top z)^2$).  
7. **Distinguish memory‑based methods** (e.g.\ Parzen window density estimation, nearest neighbours) from parametric models.  
8. **Evaluate computational trade‑offs** between primal and dual formulations (inversion costs for $M\times M$ vs. $N\times N$ matrices).  
9. **Assess kernel validity**, determining whether a proposed function satisfies Mercer’s (positive‑definiteness) conditions.  
