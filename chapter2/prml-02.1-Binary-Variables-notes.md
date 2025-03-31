# Lecture Notes – Binary Variables (PRML Section 2.1)

## Key Terminology

- **Bernoulli distribution**: A distribution over a binary variable $x \in \{0,1\}$, parameterized by $\mu \in [0, 1]$.
- **Likelihood**: The probability of observed data given a parameter, e.g., $p(x|\mu) = \mu^x(1 - \mu)^{1 - x}$.
- **Maximum Likelihood Estimate (MLE)**: The value of $\mu$ that maximizes the likelihood given observed data.
- **Conjugate prior**: A prior that ensures the posterior is in the same *parametric family* as the prior. This makes Bayesian updating analytically tractable and aligns with Bayes' theorem’s functional structure.
- **Beta distribution**: A flexible distribution on $[0,1]$ with parameters $a, b > 0$, commonly used as the conjugate prior for Bernoulli/binomial models.
- **Posterior mean**: The expected value of the parameter under the posterior distribution.
- **Entropy**: A measure of uncertainty. For Bernoulli-distributed $x$:
  $$
  H[\mu] = -\mu \ln \mu - (1 - \mu) \ln (1 - \mu)
  $$

---

## Key Ideas

### 1. Likelihood for Binary Variables

For $x \in \{0,1\}$, the likelihood is:
$$
p(x|\mu) = \mu^x (1 - \mu)^{1 - x}
$$

For $N$ independent observations:
$$
p(\mathbf{x}|\mu) = \mu^m (1 - \mu)^{N - m}
$$
where $m = \sum x_n$ is the number of ones.

The **MLE** is:
$$
\mu_{\text{ML}} = \frac{m}{N}
$$

---

### 2. Bayesian Inference and the Beta Prior

The **Beta distribution**:
$$
\text{Beta}(\mu|a,b) \propto \mu^{a - 1}(1 - \mu)^{b - 1}
$$

It is a **conjugate prior** for the Bernoulli model, meaning the posterior has the same form:
$$
\text{Beta}(\mu | a + m, b + N - m)
$$

This structural match between prior and posterior is what makes conjugate priors useful: it preserves the functional form throughout Bayesian updating, consistent with Bayes' theorem:
$$
\text{posterior} \propto \text{likelihood} \times \text{prior}
$$

The **posterior mean** is:
$$
\mathbb{E}[\mu] = \frac{a + m}{a + b + N}
$$
a weighted average of the prior mean and the MLE.

If $a > 1$ and $b > 1$, the **mode** is:
$$
\frac{a - 1}{a + b - 2}
$$

---

### 3. Binary Variables in $\{-1, 1\}$

An alternative form for binary $x \in \{-1, 1\}$:
$$
p(x|\mu) = \frac{1}{2}(1 + \mu x), \quad \mu \in [-1, 1]
$$
This representation simplifies algebra in some ML models, particularly involving symmetry.

---

### 4. Binomial Distribution

The distribution over the number of successes $m$ in $N$ Bernoulli trials:
$$
\text{Bin}(m|N, \mu) = \binom{N}{m} \mu^m (1 - \mu)^{N - m}
$$

**Normalization via the binomial theorem**:
$$
\sum_{m=0}^N \binom{N}{m} \mu^m (1 - \mu)^{N - m} = (\mu + (1 - \mu))^N = 1
$$

**Variance**:
$$
\mathrm{Var}[m] = N \mu (1 - \mu)
$$

---

### 5. Properties of the Beta Distribution

- **Mean**:
  $$
  \frac{a}{a + b}
  $$
- **Mode** (if $a,b > 1$):
  $$
  \frac{a - 1}{a + b - 2}
  $$
- **Normalization** uses the **Beta function**:
  $$
  B(a, b) = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a + b)}
  $$

---

## Why It Matters

- Binary models are foundational in classification and many probabilistic frameworks.
- The conjugate Beta prior enables closed-form Bayesian updates — a powerful property for both theory and computation.
- These ideas generalize to multinomial models and other exponential family distributions.

---

## Relevant Figures from PRML

- **Figure 2.1**: Shows how likelihood and posterior distributions evolve as more data is observed, visualizing the sharpening of belief around the true $\mu$.
- **Figure 2.2**: Illustrates the influence of different Beta priors on the posterior. Higher pseudo-counts result in stronger prior influence.

