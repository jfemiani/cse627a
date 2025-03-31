# Lecture Notes: PRML Chapter 1.1 – Polynomial Curve Fitting

## Key Terminology

- **Overfitting**: A situation where a model captures noise in the training data, leading to poor performance on unseen data.
- **Polynomial curve fitting**: Modeling a relationship by fitting a polynomial function to data points.
- **Maximum likelihood estimation (MLE)**: A method to estimate parameters by maximizing the probability of observed data.
- **Regularization**: A technique to prevent overfitting by adding a penalty term to the error function, discouraging large parameter values.
- **Root Mean Square (RMS) error**: A performance metric that reflects the average magnitude of prediction errors, in the same units as the target variable.

---

## Key Formulas

### Polynomial Model:
$$
y(x, \mathbf{w}) = \sum_{j=0}^M w_j x^j
$$

### Sum-of-Squares Error Function (unregularized):
$$
E(\mathbf{w}) = \frac{1}{2} \sum_{n=1}^N \left( y(x_n, \mathbf{w}) - t_n \right)^2
$$

### Regularized Error Function:
$$
\tilde{E}(\mathbf{w}) = E(\mathbf{w}) + \frac{\lambda}{2} \|\mathbf{w}\|^2
$$

### Root Mean Square Error:
$$
\text{RMS} = \sqrt{\frac{2E(\mathbf{w}^*)}{N}}
$$

---

## Important Ideas and Gotchas

- **Increasing model complexity can reduce training error** but often increases test error due to overfitting.
- **Regularization smooths the solution** by penalizing large weights, promoting simpler models.
- **High-degree polynomials may oscillate dramatically**, particularly near the edges of the input domain (Runge's phenomenon).
- **Training error is not a reliable indicator of generalization**; always evaluate performance on separate validation or test data.
- **MLE assumes Gaussian noise** in the target variable when used with the sum-of-squares error function.
- **RMS error is a scale-sensitive, interpretable performance metric** commonly used in regression problems.

---
