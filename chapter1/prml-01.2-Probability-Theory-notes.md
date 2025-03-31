# Lecture Notes: PRML Chapter 1.2 – Probability Theory

## Key Terminology

- **Probability distribution**: A function assigning probabilities to events or outcomes.
- **Joint probability**: The probability of two events occurring simultaneously, denoted $p(X, Y)$.
- **Marginal probability**: The probability of an event irrespective of others, e.g. $p(X) = \sum_Y p(X, Y)$.
- **Conditional probability**: The probability of an event given another, $p(X|Y) = \frac{p(X, Y)}{p(Y)}$.
- **Bayes’ theorem**: Relates conditional probabilities: $p(Y|X) = \frac{p(X|Y)p(Y)}{p(X)}$.
- **Independence**: $X$ and $Y$ are independent if $p(X,Y) = p(X)p(Y)$.
- **Expectation**: The average or mean value under a distribution.
- **Variance**: The expected squared deviation from the mean.
- **Gaussian distribution**: Also called the normal distribution, a bell-shaped continuous probability distribution.

---

## Key Formulas

### Sum and Product Rules:
$$
p(X) = \sum_Y p(X, Y)
$$
$$
p(X, Y) = p(Y|X) p(X)
$$

### Bayes’ Theorem:
$$
p(Y|X) = \frac{p(X|Y) p(Y)}{p(X)}
$$

### Expectation:
- Discrete:
  $$
  \mathbb{E}[f] = \sum_x p(x) f(x)
  $$
- Continuous:
  $$
  \mathbb{E}[f] = \int p(x) f(x) dx
  $$

### Variance:
$$
\mathrm{Var}[x] = \mathbb{E}[(x - \mathbb{E}[x])^2] = \mathbb{E}[x^2] - (\mathbb{E}[x])^2
$$

---

## Important Ideas and Gotchas

- **Probability theory provides the foundation** for all of PRML. Concepts like expectation, marginalization, and conditional probability appear throughout.
- **Bayes’ theorem is central** to both Bayesian inference and general probabilistic reasoning.
- **Independence reduces complexity** in multivariate models.
- **Variance decomposition**: Variance measures dispersion and is split between explained and unexplained variance in modeling.
- **Gaussian distribution is key** because of its analytical tractability and presence in the central limit theorem.

---

## Figures

### Figure 1.5 – Sum Rule
Illustrates marginalization over joint distributions, showing that integrating or summing out one variable yields the marginal of the other.

### Figure 1.6 – Product Rule
Visual depiction of how $p(X, Y) = p(X|Y)p(Y)$ assembles a joint distribution.

### Figure 1.7 – Bayes’ Theorem
Graphical illustration of how posterior probability is computed from prior and likelihood.

