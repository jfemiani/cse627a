# Lecture Notes: PRML Chapter 1.5 – Decision Theory

## Key Terminology

- **Decision theory**: A formal framework for making optimal decisions under uncertainty, given probabilistic beliefs and a specified loss function.
- **Loss function**: A mapping from true outcomes and predicted actions to a scalar penalty. It encodes the cost of being wrong in specific ways.
- **Expected loss (or risk)**: The average loss one expects to incur, weighted by the posterior probabilities of outcomes.
- **Bayes decision rule**: The rule that minimizes expected loss, and thus defines the optimal action under uncertainty.
- **Decision boundary**: The surface (in input space) where the predicted class changes — i.e., where expected losses of competing actions become equal.

---

## Key Ideas

### 1. Expected Loss vs. Posterior Probability

- In many problems, we compute a **posterior distribution** $p(C_i \mid \mathbf{x})$ over possible outcomes.
- To make a decision, we must translate that distribution into a concrete action — e.g., classifying $\mathbf{x}$ as a specific class $C_i$.
- The **Bayes optimal decision rule** chooses the action that minimizes **expected loss**:
  $$
  \text{Choose } C_i \text{ that minimizes } R(C_i \mid \mathbf{x}) = \sum_j L_{ij} \, p(C_j \mid \mathbf{x})
  $$
- If the loss matrix assigns 0 loss for correct predictions and 1 for incorrect predictions — that is, $L_{ij} = \mathbb{I}[i \ne j]$ — then the Bayes-optimal decision rule simplifies to:
  $$
  \text{Choose the class with highest posterior probability}
  $$
  > (Note: This case is often referred to as “0-1 loss” in the broader ML literature, but PRML does not use that label.)
- Thus: **maximizing posterior probability is a special case** of minimizing expected loss — when the loss function is symmetric and discrete.

> Don't conflate the two. In many real-world settings (e.g., medical diagnosis, spam filtering), the cost of errors is asymmetric. The highest-probability outcome may not be the optimal decision.

---

### 2. Regression is Also Decision Theory

- Although Section 1.5 frames decision theory in terms of classification, **regression is also a decision problem**:
  - Predicting a numeric value $\hat{y}$ for an input $\mathbf{x}$, where the true value $y$ is drawn from $p(y \mid \mathbf{x})$.

- We define a **loss function $L(y, \hat{y})$**, and minimize expected loss:
  $$
  \mathbb{E}[L(y, \hat{y})] = \int L(y, \hat{y}) \, p(y \mid \mathbf{x}) \, dy
  $$

- Common choices:
  - **Squared error (MSE)**: $L(y, \hat{y}) = (y - \hat{y})^2$
    - Minimizing expected squared error yields:
      $$
      \hat{y}_{\text{opt}} = \mathbb{E}[y \mid \mathbf{x}]
      $$
    - This justifies **predicting the conditional mean** under MSE.
  - **Absolute error (L1 loss)**: $L(y, \hat{y}) = |y - \hat{y}|$
    - Minimizing expected absolute error yields the **conditional median**.
  - **Huber loss**: Quadratic near zero, linear for large errors
    - Robust to outliers, commonly used in practice

> These are not just tricks — they are **different notions of what it means to be wrong**. Choosing a loss function encodes your tolerance for outliers, asymmetry, or sharp penalties.

---

## Why It Matters

- **Separating modeling from decision**: We can estimate a posterior using a probabilistic model, but our ultimate goal may not be to predict probabilities — it’s to make good decisions given them.
- **Practical impact**: The right decision may depend on the application’s cost structure, not just probabilities.
- **Loss-awareness**: Good ML systems should be sensitive to the real-world cost of decisions — and this is exactly what decision theory formalizes.

---

## Relevant Figures from PRML

- **Figure 1.11**: Shows decision boundaries under 0-1 and asymmetric loss for a two-class Gaussian classification problem.
  - With 0-1 loss, the decision boundary falls where the posteriors are equal.
  - With asymmetric loss, the boundary shifts toward the class with **lower penalty for mistakes**.

