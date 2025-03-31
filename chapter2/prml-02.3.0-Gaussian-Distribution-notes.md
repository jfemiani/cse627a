# Lecture Notes: PRML Chapter 2.3.0 – The Gaussian Distribution

## Prerequisite Knowledge

- **Eigenvectors and Eigenvalues:**  
  An *eigenvector* of a matrix is a nonzero vector that, when multiplied by the matrix, is only scaled by a corresponding *eigenvalue*. For symmetric matrices (like a covariance matrix), these eigenvectors can be chosen to be orthogonal.  
  
- **Jacobian vs. Hessian:**  
  The *Jacobian* is the matrix of first derivatives that describes how a change in one coordinate system affects another. In contrast, the *Hessian* is the matrix of second derivatives, describing curvature.  

- **Determinant as Product of Eigenvalues:**  
  For any square matrix, its determinant equals the product of its eigenvalues.  

- **Central Limit Theorem:**  
  The theorem states that the sum (or average) of many independent random variables tends toward a Gaussian distribution, regardless of the original distributions.  

---

## Introduction and Key Concepts

This section introduces the Gaussian distribution—a cornerstone in probability and statistics—and explains its use in modeling continuous data. The univariate and multivariate forms are presented, emphasizing the role of the covariance matrix in shaping the distribution. In particular, we discuss the transformation (or whitening) of data using the eigen-decomposition of $\Sigma$, and the significance of *general*, *diagonal*, and *isotropic* covariance forms.

---

## 1. Univariate Gaussian Distribution

**Why it matters:**  
The univariate Gaussian is the simplest model for continuous data. It underpins many statistical methods and is used as a starting point for understanding more complex, multidimensional distributions.

**Formula (2.42):**  
$$
\mathcal{N}(x|\mu,\sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\!\Bigl\{-\frac{1}{2\sigma^2}(x-\mu)^2\Bigr\}
\tag{2.42}
$$

**Explanation:**  
This formula represents the familiar bell curve. The upside-down parabola $(x-\mu)^2$ in the exponent shows that values far from the mean $\mu$ become exponentially less likely. The denominator normalizes the distribution so the total probability is 1.

Some observations:

1. The exponent is an upside down parabola, zero at the mean.
2. The term in front normalizes it ... so that it integrates to one.
3. The natural logarithm is the exponent (qudratic) + $\ln \sigma$ + const. 
4. A **standard** normal has $\mu=0, \sigma=1$ and this is just a translation by $\mu$ and scale by $\frac{1}{\sigma}$ of the $x$

---

## 2. Multivariate Gaussian Distribution
**Why it matters:**  
The multivariate Gaussian is a fundamental model for multidimensional data. It appears in many practical applications, from Bayesian inference to principal component analysis (PCA), and provides the basis for models in regression, classification, and beyond.

$$
\mathcal{N}(x|\mu,\Sigma) = \frac{1}{(2\pi)^{D/2}|\Sigma|^{1/2}} \exp\!\Bigl\{-\frac{1}{2}(x-\mu)^\top\Sigma^{-1}(x-\mu)\Bigr\}
\tag{2.43}
$$

**Explanation:**  
This is the generalization of the univariate case to $D$ dimensions. The quadratic form $(x-\mu)^\top \Sigma^{-1}(x-\mu)$ replaces the squared difference, adapting the distance measure to account for correlations among dimensions. The normalization factor involving $|\Sigma|$ ensures that the density integrates to 1.



---

## 3. Mahalanobis Distance
**Why it matters:**  
The Mahalanobis distance is central to understanding the shape of the Gaussian distribution. It defines ellipsoidal contours of equal probability density and is critical for tasks like outlier detection and classification.

$$
\Delta^2 = (x-\mu)^\top \Sigma^{-1}(x-\mu)
\tag{2.44}
$$

**Explanation:**  
This distance measure generalizes the Euclidean distance by incorporating the covariance matrix $\Sigma$. When $\Sigma$ is the identity matrix, $\Delta$ is the usual Euclidean distance. Otherwise, it accounts for scaling and correlation between variables.


## 4. Eigendecomposition of the Covariance Matrix
**Why it matters:**  
Understanding the eigendecomposition of $\Sigma$ is key to many advanced techniques, including dimensionality reduction and data whitening. It reveals the intrinsic geometry of the data distribution and is essential for interpreting the shape of the Gaussian density.

**Eigenvector Equation (2.45):**  
$$
\Sigma u_i = \lambda_i u_i
\tag{2.45}
$$

**Orthogonality (2.46) and Identity (2.47):**  
$$
u_i^\top u_j = I_{ij} \quad \text{with} \quad I_{ij} =
\begin{cases}
1, & \text{if } i=j, \\
0, & \text{otherwise.}
\end{cases}
\tag{2.46, 2.47}
$$

**Expansion of $\Sigma$ (2.48):**  
$$
\Sigma = \sum_{i=1}^D \lambda_i\, u_i u_i^\top
\tag{2.48}
$$

**Expansion of $\Sigma^{-1}$ (2.49):**  
$$
\Sigma^{-1} = \sum_{i=1}^D \frac{1}{\lambda_i}\, u_i u_i^\top
\tag{2.49}
$$

**Explanation:**  
These formulas decompose the covariance matrix into its eigenvectors and eigenvalues. Each eigenvector $u_i$ indicates a principal direction, and its eigenvalue $\lambda_i$ represents the variance along that direction. The expansions show how both $\Sigma$ and its inverse can be reconstructed from these components.




---

## 5. Transformation to Whitened Coordinates

**Why it matters:**  
Transforming to whitened coordinates simplifies many calculations, as the Gaussian density factorizes into independent univariate densities. This insight is widely used in statistical inference and machine learning algorithms.

**Definition (2.51):**  
$$
y_i = \mathbf{u}_i^\top (\mathbf{x}-\boldsymbol{\mu})
\tag{2.51}
$$

**Vector Form (2.52):**  
$$
\mathbf{y} = U(\mathbf{x}-\boldsymbol{\mu})
\tag{2.52}
$$  
where $U$ is the matrix whose rows are $u_i^\top$, satisfying $UU^\top = I$.

**Explanation:**  
This transformation projects the data onto the eigenvectors of $\Sigma$, effectively rotating and shifting the coordinate system so that in the new coordinates, the covariance matrix becomes diagonal. This “whitening” process makes the variables independent.


---

## 6. Jacobian of the Transformation
**Why it matters:**  
The Jacobian is essential for correctly transforming probability densities between coordinate systems. Its value of 1 here shows that the probability mass is preserved under the rotation and shift.

**Definition (2.53):**  
$$
J_{ij} = \frac{\partial x_i}{\partial y_j} = U_{ji}
\tag{2.53}
$$

**Result (2.54):**  
$$
|J| = 1
\tag{2.54}
$$

**Explanation:**  
The Jacobian matrix $J$ captures how volume elements transform under the coordinate change from $x$ to $y$. Since $U$ is orthogonal, the transformation preserves volume, meaning the determinant of $J$ is 1.



---

## 7. Determinant of the Covariance Matrix

**Why it matters:**  
Understanding this relationship is key to grasping how changes in the covariance (and thus in the eigenvalues) affect the _shape and spread_ of the probability density. It also simplifies computations in many practical applications.

**Formula (2.55):**  
$$
|\Sigma|^{1/2} = \prod_{j=1}^D \lambda_j^{1/2}
\tag{2.55}
$$

**Explanation:**  
This equation expresses the normalization factor of the multivariate Gaussian in terms of the eigenvalues of $\Sigma$. Since the determinant equals the product of the eigenvalues, this formula connects the spread of the data (through the eigenvalues) with the overall volume scaling.


---

## 8. Gaussian Distribution in Whitened Coordinates
**Why it matters:**  
This factorization is powerful because it simplifies integration and inference. It is the basis for many algorithms that assume independent components after appropriate transformation.

**Formula (2.56):**  
$$
p(y) = \prod_{j=1}^D \frac{1}{\sqrt{2\pi\lambda_j}} \exp\!\Bigl\{-\frac{y_j^2}{2\lambda_j}\Bigr\}
\tag{2.56}
$$

**Explanation:**  
After transforming the variable from $x$ to $y$, the multivariate Gaussian density becomes a product of independent univariate Gaussians. Each component $y_j$ has variance $\lambda_j$.

---

## 9. Normalization and Moments

**Why it matters:**  
Knowing the mean and covariance of the distribution is critical for summarizing data. They are the primary parameters in Gaussian models and are used for tasks such as parameter estimation and hypothesis testing.

**Normalization (2.57):**  
$$
\int p(y)\,dy = 1
\tag{2.57}
$$

**Mean (2.59):**  
$$
E[x] = \mu
\tag{2.59}
$$


**Second-order Moment (2.62):**  
$$
E[xx^\top] = \mu\mu^\top + \Sigma
\tag{2.62}
$$

**Covariance (2.64):**  
$$
\text{cov}[x] = \Sigma
\tag{2.64}
$$

**Explanation:**  
These results show that the spread (or variability) of the data around the mean is fully captured by the covariance matrix $\Sigma$. The mean $\mathbf{mu}$ captures its location. 


## 10. Restricted Covariance Matrices

The normal distribution has $O(D^2)$ parameters which causes several issues:
 
1. It is not cheep in terms of memory or computation for large $D$. 
2. More degrees of freedom require more data to determine the parameters
3. More degrees of freedom make it more sensitive to overfitting / noise

Often we can bring some prior knowledge into hwo to model the features so that a restricted model works. 

**Restrictions:**  

- **General Covariance:**  
  $\Sigma$ is a full symmetric matrix with $\frac{D(D+1)}{2}$ free parameters.  
  **Why it matters:**  
  This form is the most flexible, capturing all pairwise correlations but at the cost of high complexity.

- **Diagonal Covariance:**  
  $\Sigma = \text{diag}(\sigma_1^2, \dots, \sigma_D^2)$ reduces the number of free parameters to $2D$.  
  **Why it matters:**  
  This simplification assumes no correlation between different dimensions, reducing computational cost.

- **Isotropic Covariance:**  
  $\Sigma = \sigma^2 I$ further reduces the parameters to $D+1$, implying the same variance in all directions.  
  **Why it matters:**  
  This is the simplest model, useful when the data is roughly uniform in every direction but it may be too restrictive to capture real correlations.

