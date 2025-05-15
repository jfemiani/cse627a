# Lecture Notes: PRML Chapter 5.2 – Network Training

## Prerequisites

- **Gradient-Based Optimization:** Familiarity with gradient descent and its use in fitting parametric models.
- **Probabilistic Modeling:** Understanding of maximum likelihood estimation and likelihood-based loss functions.
- **Multivariable Calculus:** Ability to interpret gradients, Hessians, and Taylor expansions.
- **Classification and Regression Tasks:** Understanding of regression vs classification, and common loss functions (e.g., cross-entropy, sum-of-squares).

## Key Terminology

- **Error or Loss Function:** A scalar function measuring discrepancy between predicted outputs and targets, typically minimized during training.
- **Maximum Likelihood Estimation (MLE):** A framework for estimating parameters by maximizing the probability of observed data.
- **Precision ($\beta$):** The inverse of variance, often used in Gaussian likelihoods.
- **Cross-Entropy Error:** A loss function used in classification based on negative log-likelihood of predicted Bernoulli-distributed probabilities.
- **Softmax Function:** An activation function that converts raw scores to a probability distribution over classes.
- **Hessian Matrix:** The matrix of second-order partial derivatives of a scalar function.
- **Stationary Point:** A point where the gradient of a function vanishes; may be a minimum, maximum, or saddle point.
- **Batch vs Online Gradient Descent:** Methods for computing weight updates using the full dataset vs a single (or small batch of) training example(s).
    > Watch out -- "MiniBatch" is sometimes abbreviated as "Batch" to confuse you!
- **Stochastic Gradient Descent**: Synonym for Online Gradient Descent.

## Why It Matters
Training neural networks is fundamentally an optimization problem. The challenge is compounded by:

- **Nonlinearity and Nonconvexity** of the model.
- The need to **match activation functions to error functions** appropriately.
- The choice of **optimization technique** and **loss function** significantly affecting generalization performance and convergence.

---

## Key Ideas

### 1. Training via Maximum Likelihood

**Why it matters:**  
Gives a principled foundation for both choosing an error function and interpreting the network’s predictions probabilistically.

- For **regression**, the network output $y(x, \mathbf{w})$ is treated as the mean of a Gaussian:
  $$
  p(t | x, \mathbf{w}) = \mathcal{N}(t \mid y(x,\mathbf{w}), \beta^{-1})
  \tag{5.12}
  $$
- The negative log-likelihood leads to a **sum-of-squares error function**:
  $$
  E(\mathbf{w}) = \frac{1}{2} \sum_{n=1}^N \{ y(\mathbf{x}_n, \mathbf{w}) - t_n \}^2
  \tag{5.14}
  $$
- The MLE for the precision:
  $$
  \frac{1}{\beta_{\text{ML}}} = \frac{1}{N} \sum_{n=1}^N \{ y(\mathbf{x}_n, \mathbf{w}_{\text{ML}}) - t_n \}^2
  \tag{5.15}
  $$
  (But we often don't estimate this in practice)

### 2. Classification and Matching Activation/Error Functions

**Why it matters:**  
Choosing compatible activations and loss functions ensures that training aligns with probabilistic modeling goals.

- For **binary classification**:
  - Output activation is **logistic sigmoid**:
    $$
    y = \sigma(a) = \frac{1}{1 + \exp(-a)}
    \tag{5.19}
    $$
  - Targets are Bernoulli distributed, leading to **cross-entropy loss**:
    $$
    E(\mathbf{w}) = - \sum_{n=1}^N \{ t_n \ln y_n + (1 - t_n) \ln (1 - y_n) \}
    \tag{5.21}
    $$
   - remember $t$ is 0 or 1 so this is essential "if /else"
- For **multiple independent binary outputs**:  
  Just add the energies together (multiply the probabilities)
  $$
E(\mathbf{w}) = - \sum_{n=1}^N \sum_{k=1}^K \{ t_{nk} \ln y_k(\mathbf{x}_n, \mathbf{w}) + (1 - t_{nk}) \ln (1 - y_k(\mathbf{x}_n, \mathbf{w})) \}
\tag{5.23}
  $$

- For **multiclass classification**:
  - Use **softmax** activation:
    $$
    y_k(x, \mathbf{w}) = \frac{\exp(a_k)}{\sum_j \exp(a_j)}
    \tag{5.25}
    $$
    - Sometimes you subtract the max activation for stabilty
    - This is essentially the same as the sigmoid, but overparameterized. 
  - Cross-entropy loss with 1-of-K targets:
    $$
    E(\mathbf{w}) = - \sum_{n=1}^N \sum_{k=1}^K t_{nk} \ln y_k(\mathbf{x}_n, \mathbf{w})
    \tag{5.24}
    $$


### Label Smoothing

**Why it matters:**  
One-hot encoding assumes perfect confidence in the target label. This can lead the model to become **overconfident**, especially in the presence of noisy labels or under-regularization. Label smoothing improves generalization by softening the target distribution.

- Instead of using $t_k = 1$ for the correct class and $0$ for all others, we smooth the target:
  $$
  t_k = 
  \begin{cases}
    1 - \epsilon, & \text{if } k = \text{correct class} \\
    \frac{\epsilon}{K - 1}, & \text{otherwise}
  \end{cases}
  $$
  where $\epsilon$ is a small constant (e.g., 0.1), and $K$ is the number of classes.

- This prevents the model from becoming overconfident and encourages **calibrated** output probabilities.
- Label smoothing can also reduce the effect of **label noise** and make training more stable when using softmax + cross-entropy.

> Note: Label smoothing modifies the **targets**, not the logits or the loss function itself. It must be applied *before* loss computation.


### 3. Optimization Landscape

**Why it matters:**  
Highlights that multiple solutions may exist, and shows why training is often framed as minimizing error rather than maximizing likelihood.

- The error function is nonconvex: it can have many **local minima**, **saddle points**, and **equivalent symmetric optima**.
- The goal is to find a weight vector $\mathbf{w}$ where the **gradient vanishes**:
  $$
  \nabla E(\mathbf{w}) = 0
  \tag{5.26}
  $$
- We try to design loss functions and activation functions so that the odds of encountering a plateau/saddle or max are low (heuristically)
- We minimize energy (negative log likelihood) by convention, because it is analogous to energy in physics. 
- Also reducing *error* is sometimes more natural to think about than maximizing probability.
- Minimization depends on positive-definite Hessian matrices; we rarely discuss negative matrices (again, convention)

### 4. Local Quadratic Approximation and the Hessian

**Why it matters:**  
Understanding curvature helps explain the behavior of optimization algorithms.

- Second-order Taylor expansion:
  $$
  E(\mathbf{w}) \approx E(\hat{\mathbf{w}}) + (\mathbf{w} - \hat{\mathbf{w}})^T \nabla E + \frac{1}{2} (\mathbf{w} - \hat{\mathbf{w}})^T H (\mathbf{w} - \hat{\mathbf{w}})
  \tag{5.28}
  $$
- If $\nabla E = 0$, the leading term is the **Hessian**:
  $$
  E(\mathbf{w}) = E(\mathbf{w}^*) + \frac{1}{2} (\mathbf{w} - \mathbf{w}^*)^T H (\mathbf{w} - \mathbf{w}^*)
  \tag{5.32}
  $$
- Geometry: eigenvectors of $H$ define **principal axes**, and eigenvalues $\lambda_i$ scale curvature:
  $$
  H \mathbf{u}_i = \lambda_i \mathbf{u}_i
  \tag{5.33}
  $$
- Large eigenvalues $\lambda_i$:
  - Indicate steep curvature in the error surface.
  - Small changes in weights along those directions lead to large changes in error.
  - This can result in **overly sensitive solutions** and **poorer generalization**.

- Small eigenvalues $\lambda_i$:
  - Correspond to flat directions in weight space.
  - These solutions tend to be **more stable** but can cause **slow convergence**.

- Zero or negative eigenvalues:
  - Imply the point is **not a local minimum**.
  - Negative values indicate a **saddle point** or **local maximum**.
  - Zero values suggest **degeneracy** or a **flat manifold** of solutions.

- Full computation of the Hessian $H$:
  - Is **infeasible** in large-scale networks due to its $O(D^2)$ size.
  - Second-order optimization methods are rarely practical.

- Practical alternatives:
  - Optimizers like **Adam** use **exponential moving averages** of first and second moments of gradients.
  - These provide some curvature information without explicitly computing $H$.

### 5. Gradient-Based Optimization

**Why it matters:**  
Gradient descent is the foundation of almost all practical training methods.

- Classic gradient descent:
  $$
  \mathbf{w}^{(\tau+1)} = \mathbf{w}^{(\tau)} - \eta \nabla E(\mathbf{w}^{(\tau)})
  \tag{5.41}
  $$

- Online (stochastic) gradient descent:
  $$
  \mathbf{w}^{(\tau+1)} = \mathbf{w}^{(\tau)} - \eta \nabla E_n(\mathbf{w}^{(\tau)})
  \tag{5.43}
  $$
  (Not the '$n$' in the subscript!)

**Batch vs Online:**
- Batch methods use full dataset; computationally expensive per step.
- Online methods update per example; more noise but can escape poor local minima and scale better.

> **GOTCHA ALERT**: "Batch" referes to the *entire* training set, "Minibatch" refers to a small sample of  e.g 32 samples.  Lazy people abbreviate "Minibatch" as "Batch" completely changing its meaning and confusing students. 

### 6. Practical Considerations

**Why it matters:**  
Real-world training demands efficiency and robustness.

- **Random restarts**: due to local minima.
- **Alternative optimizers**: conjugate gradient, quasi-Newton methods.
- **Regularization**: softmax outputs exhibit a degenerate direction unless regularized.

Your instructor's Advice:
 - Initilize weights with a model already trained on a simlar task
 - Regularize with a low regularizarion weight
 - Learning rates are often much lower than you expect
 - When using pyutorch, take carte if your loss function expect probabilities vs logits!
 - Add terms to the loss to guide the network. Rearely do you **just** want to minimize cross entropy.  Usually there are other aspects of a desirable output that you can put into the loss as $\alpha_0 \cdot  \mathcal{L}_0 + \alpha_1 \cdot \mathcal{L}_1, + ...$.
 - Pay attention to the relative impact of different losses -- often something dominates that you dont want. E.g. outliers. 
 - Look for per-iteration spikes when training -- these can indicate outliers (or bad data)
 - Watch for / check for NaN
 - Training is slow, save the weights often so you can resume if you get disconnected.
 - Use a *tiny subset* of the data to test things - and make sure training converges - without waiting for hours to find out.  

 - **PyTorch Pitfalls with Loss Functions:**
  - `CrossEntropyLoss` expects **raw logits** and applies `log_softmax` internally. Do **not** apply softmax yourself.
  - `BCELoss` expects **probabilities** in $(0,1)$; passing logits directly will break training.
  - Use `BCEWithLogitsLoss` if your model outputs logits — it wraps sigmoid + BCE in a numerically stable form.
  - Misusing these is a **common cause of silent failure** (e.g., exploding loss or no/slow learning).


---

## Relevant Figures from PRML

- **Figure 5.5**: Shows the error surface over weight space, depicting gradient direction and stationary points.
- **Figure 5.6**: Visualizes contours of the quadratic approximation to the error surface; axes aligned with Hessian eigenvectors.


