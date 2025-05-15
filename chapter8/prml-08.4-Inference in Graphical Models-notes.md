---
title: "Lecture Notes: PRML 8.4 – Inference in Graphical Models"
author: "John Femiani"
date: "2025-05-07"
description: "Inference in chain-structured graphical models using message passing. Includes derivations, complexity analysis, and a worked example of computing $p(x_3)$."
---


## Prerequisites

- Graphical model types: Bayesian Networks, Markov Random Fields
- Factorization and potential functions
- Marginalization and conditional probability
- Chain rule and sum-product operations

## Key Terminology

- **Message passing**: Local computation scheme where nodes send and receive functions summarizing downstream information.
- **Sum-product algorithm**: A general framework for computing marginals via message propagation.
- **Forward message ($\mu_\alpha$)**: Information propagated from earlier nodes in a chain or tree.
- **Backward message ($\mu_\beta$)**: Information propagated from later nodes.
- **Markov chain**: A special case of a graphical model where each variable depends only on its predecessor.
- **Clamping**: Fixing a variable to an observed value (e.g., evidence).
- **Recursive marginalization**: Exploiting conditional independence and factor structure to reduce computational complexity.

## Why It Matters

Inference is the core operation in probabilistic models. Efficient inference makes it possible to compute beliefs, make decisions, or learn parameters from incomplete data. This section shows how message passing enables tractable exact inference in chain graphs.  These notes focus on chains, but we will extend to tree structured graphs.

## Key Ideas

### Graphical Interpretation of Bayes’ Rule

Given a directed graph where $x \to y$, observing $y$ leads to “flipping” the edge to represent $x \mid y$:

- Joint: $p(x, y) = p(x)p(y|x)$  
- Posterior: $p(x|y) = \frac{p(y|x)p(x)}{p(y)}$

This illustrates how **inference updates graphical semantics**.

### Inference on a Chain

Given a chain-structured undirected model:

$$
x_1 — x_2 — x_3 — x_4 — x_5
$$

The joint distribution factorizes as:

$$
p(x) = \frac{1}{Z} \prod_{i=1}^{4} \psi_{i,i+1}(x_i, x_{i+1})
$$

To compute a marginal like $ p(x_3) $, we could naively sum over all other variables:

$$
\begin{aligned}
p(x_3) &= \sum_{x_1} \sum_{x_2} \sum_{x_4} \sum_{x_5}
\frac{1}{Z}
\psi_{1,2}(x_1, x_2)
\psi_{2,3}(x_2, x_3)
\psi_{3,4}(x_3, x_4)
\psi_{4,5}(x_4, x_5)
\end{aligned}
$$

This direct approach has complexity $ O(K^4) $ (or $ O(K^{N-1}) $ in general), which is infeasible for large $ N $.

---

We can drastically reduce this cost by **distributing the summations** and using **message passing**. We reorganize the computation:

$$
\begin{aligned}
p(x_3) &= \frac{1}{Z}
\underbrace{
\left(
\sum_{x_2}

\psi_{2,3}(x_2, x_3)\cdot\underbrace{\left( \sum_{x_1} \psi_{1,2}(x_1, x_2) \right)
}_{\mu_2^\alpha(x_2)}
\right)
}_{\mu_3^\alpha(x_3)}
\cdot
\underbrace{
\left( \sum_{x_4} \psi_{3,4}(x_3, x_4)
\underbrace{
\left( \sum_{x_5} \psi_{4,5}(x_4, x_5) \right)
}_{\mu_4^\beta(x_4)}
\right)
}_{\mu_3^\beta(x_3)}
\\[1.2em]
&= \frac{1}{Z} \cdot \mu_3^\alpha(x_3) \cdot \mu_3^\beta(x_3)
\end{aligned}
$$

---

### Interpretation

- $ \mu_2^\alpha(x_2) = \sum_{x_1} \psi_{1,2}(x_1, x_2) $ — forward message into $ x_2 $
- $ \mu_3^\alpha(x_3) = \sum_{x_2} \mu_2^\alpha(x_2) \cdot \psi_{2,3}(x_2, x_3) $— forward message into $ x_3 $
- $ \mu_4^\beta(x_4) = \sum_{x_5} \psi_{4,5}(x_4, x_5) $ — backward message into $ x_4 $
- $ \mu_3^\beta(x_3) = \sum_{x_4} \psi_{3,4}(x_3, x_4) \cdot \mu_5^\beta(x_4) $ — backward message into $x_3$
- Finally:  
  $ p(x_3) \propto \mu_3^\alpha(x_3) \cdot \mu_3^\beta(x_3) $

---

This transformation reduces the overall computation to linear time: $ O(NK^2) $, enabling scalable exact inference in chains.

Use recursive **message passing**:

- Forward:
  $$
  \mu_\alpha(x_n) = \sum_{x_{n-1}} \psi_{n-1,n}(x_{n-1}, x_n)\mu_\alpha(x_{n-1})
  $$
- Backward:
  $$
  \mu_\beta(x_n) = \sum_{x_{n+1}} \psi_{n+1,n}(x_{n+1}, x_n)\mu_\beta(x_{n+1})
  $$
- Marginal:
  $$
  p(x_n) = \frac{1}{Z} \mu_\alpha(x_n)\mu_\beta(x_n)
  $$

### Efficiency

Total cost is $O(NK^2)$ — one forward pass and one backward pass.

### Clamped Variables (Observed)

When a variable $x_k$ is observed:

- Its summation disappears.
- Potentials involving $x_k$ get replaced by indicator functions: $I(x_k = \hat{x}_k)$.

### Pairwise Marginals

We can also compute:
$$
p(x_{n-1}, x_n) = \frac{1}{Z} \mu_\alpha(x_{n-1}) \psi_{n-1,n}(x_{n-1}, x_n) \mu_\beta(x_n)
$$

> These principles extend to trees, and will later generalize into the full **sum-product algorithm** for arbitrary graphs.

---

### Example: Computing $p(x_3)$ in a Chain-Structured MRF

Suppose we have five binary variables arranged in a chain:

$$
x_1 — x_2 — x_3 — x_4 — x_5
$$

The joint distribution is defined as:

$$
p(x_1, x_2, x_3, x_4, x_5) = \frac{1}{Z} \psi_{1,2}(x_1, x_2)\psi_{2,3}(x_2, x_3)\psi_{3,4}(x_3, x_4)\psi_{4,5}(x_4, x_5)
$$

All variables are binary: $x_i \in \{0, 1\}$.  
We will compute the marginal distribution $p(x_3)$ via message passing.

---

### Potentials

**$\psi_{1,2}(x_1, x_2)$**

| $x_1$ | $x_2$ | Value |
|------:|------:|-------:|
| 0     | 0     | 3.0    |
| 0     | 1     | 2.0    |
| 1     | 0     | 1.0    |
| 1     | 1     | 4.0    |

**$\psi_{2,3}(x_2, x_3)$**

| $x_2$ | $x_3$ | Value |
|------:|------:|-------:|
| 0     | 0     | 1.0    |
| 0     | 1     | 2.0    |
| 1     | 0     | 3.0    |
| 1     | 1     | 1.0    |

**$\psi_{3,4}(x_3, x_4)$**

| $x_3$ | $x_4$ | Value |
|------:|------:|-------:|
| 0     | 0     | 1.0    |
| 0     | 1     | 1.0    |
| 1     | 0     | 2.0    |
| 1     | 1     | 3.0    |

**$\psi_{4,5}(x_4, x_5)$**

| $x_4$ | $x_5$ | Value |
|------:|------:|-------:|
| 0     | 0     | 1.0    |
| 0     | 1     | 1.0    |
| 1     | 0     | 2.0    |
| 1     | 1     | 1.0    |

---

### Step 1: Forward Messages to $x_3$

We compute:

$$
\mu_2^\alpha(x_2) = \sum_{x_1} \psi_{1,2}(x_1, x_2)
$$

| $x_2$ | $\mu_2^\alpha(x_2)$ |
|------:|---------------------:|
| 0     | $3.0 + 1.0 = 4.0$    |
| 1     | $2.0 + 4.0 = 6.0$    |

Then:

$$
\mu_3^\alpha(x_3) = \sum_{x_2} \mu_2^\alpha(x_2) \cdot \psi_{2,3}(x_2, x_3)
$$

| $x_3$ | $\mu_3^\alpha(x_3)$ |
|------:|---------------------:|
| 0     | $4.0 \cdot 1.0 + 6.0 \cdot 3.0 = 4.0 + 18.0 = 22.0$ |
| 1     | $4.0 \cdot 2.0 + 6.0 \cdot 1.0 = 8.0 + 6.0 = 14.0$  |

---

### Step 2: Backward Messages to $x_3$

We compute:

$$
\mu_4^\beta(x_4) = \sum_{x_5} \psi_{4,5}(x_4,x_5)
$$

| $x_4$ | $\mu_4^\beta(x_4)$ |
|------:|--------------------:|
| 0     | $1.0 + 1.0 = 2.0$   |
| 1     | $2.0 + 1.0 = 3.0$   |

Then:

$$
\mu_3^\beta(x_3) = \sum_{x_4} \psi_{3,4}(x_3,x_4) \cdot \mu_4^\beta(x_4)
$$

| $x_3$ | $\mu_3^\beta(x_3)$ |
|------:|---------------------:|
| 0     | $1.0 \cdot 2.0 + 1.0 \cdot 3.0 = 2.0 + 3.0 = 5.0$   |
| 1     | $2.0 \cdot 2.0 + 3.0 \cdot 3.0 = 4.0 + 9.0 = 13.0$ |

---

### Step 3: Final Marginal $p(x_3)$

$$
p(x_3) \propto \mu_3^\alpha(x_3) \cdot \mu_3^\beta(x_3)
$$

| $x_3$ | unnormalized | normalized |
|------:|--------------:|-------------:|
| 0     | $22 \cdot 5 = 110$ | $110 / 292 \approx 0.377$ |
| 1     | $14 \cdot 13 = 182$ | $182 / 292 \approx 0.623$ |

So:

$$
p(x_3 = 0) \approx 0.377,\quad p(x_3 = 1) \approx 0.623
$$

---

> This demonstrates how directional message passing enables tractable computation  
> of marginals even in graphs that would otherwise require exponential summation.
