## Key Ideas

### Multinomial Model

- The **multinomial distribution** describes the probability of observing a particular combination of category counts over $N$ trials, where each trial results in one of $K$ mutually exclusive outcomes.

- Each categorical observation $\mathbf{x}_n$ is a one-hot vector: exactly one entry is 1, the rest are 0.

- When viewed as a **probability distribution over outcomes**, the multinomial gives the probability of sample counts $(m_1, \dots, m_K)$ for fixed parameters $\boldsymbol{\mu}$:
  $$
  p(\mathbf{m}|\boldsymbol{\mu}) = \frac{N!}{m_1! \cdots m_K!} \prod_{k=1}^K \mu_k^{m_k}
  $$

- When viewed as a **likelihood function**, this same expression is interpreted differently:
  - It is the **joint probability of the observed data** (the sample counts), treated as a function of the parameters $\boldsymbol{\mu}$.
  - This distinction is essential: the likelihood tells us how likely the observed data is, given particular parameter values.

- This likelihood forms the basis for Bayesian inference. When combined with a **prior distribution over $\boldsymbol{\mu}$**, it produces a **posterior distribution** via Bayes’ theorem.

### Dirichlet Prior

- The **Dirichlet distribution** is a probability distribution over $K$-dimensional probability vectors. It serves as a **prior** for $\boldsymbol{\mu}$ in the multinomial model.
  $$
  \text{Dir}(\boldsymbol{\mu} | \boldsymbol{\alpha}) = \frac{1}{B(\boldsymbol{\alpha})} \prod_{k=1}^K \mu_k^{\alpha_k - 1}
  $$

- It is the **conjugate prior** of the multinomial distribution, meaning that the posterior has the same form:
  $$
  \boldsymbol{\alpha}' = \boldsymbol{\alpha} + \mathbf{m}
  $$

- The Dirichlet prior expresses belief about category frequencies **before** observing any data. The update rule simply adds the observed counts to the prior pseudo-counts.

