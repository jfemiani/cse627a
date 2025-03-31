# Lecture Notes: PRML Chapter 1.6 – Information Theory

## Key Terminology

- **Entropy ($H[x]$)**: A measure of uncertainty in a discrete probability distribution. It quantifies the expected amount of information (in bits) contained in a random variable.
- **Information content**: The "surprise" or information gained by observing a specific outcome $x$. Given by $-\log p(x)$.
- **Relative entropy / Kullback-Leibler (KL) divergence**: A measure of how one probability distribution differs from another.
- **Mutual information ($I[x, y]$)**: The reduction in uncertainty about $x$ given knowledge of $y$; equivalently, the amount of information $x$ and $y$ share.

---

## Key Ideas

### 1. Entropy – Measuring Uncertainty

Given a discrete random variable $x$ with distribution $p(x)$, the entropy is defined as:

$$
H[x] = -\sum_x p(x) \log p(x)
$$

- High entropy implies a more uniform distribution — i.e., higher uncertainty.
- Low entropy means the distribution is concentrated and predictable.
- Entropy is **maximized** when $p(x)$ is uniform.
- This is the best any lossless code can do — no other encoding can, on average, use fewer bits.
- Real-world compression schemes (like Huffman coding) aim to approximate this bound.
#### Units:
- If log base 2 is used, entropy is measured in **bits**.
- If log base $e$ is used, the units are **nats**.

#### Example:
For a fair coin:  
$$
H[x] = -\left( \frac{1}{2} \log_2 \frac{1}{2} + \frac{1}{2} \log_2 \frac{1}{2} \right) = 1 \text{ bit}
$$

---

### 2. KL Divergence – Comparing Distributions

The Kullback-Leibler divergence from distribution $p(x)$ to $q(x)$ is defined as:

$$
\text{KL}(p \| q) = \sum_x p(x) \log \frac{p(x)}{q(x)}
$$

#### Properties:
- **Non-negative**:
  $$
  \text{KL}(p \| q) \ge 0, \quad \text{with equality iff } p(x) = q(x)
  $$
- **Asymmetric**:  
  $\text{KL}(p \| q) \ne \text{KL}(q \| p)$ in general.
- **Not a metric**: It does not satisfy symmetry or triangle inequality.

#### Interpretation:
- Measures how inefficient it is to assume $q(x)$ when the true distribution is $p(x)$.
- Used heavily in variational inference and model comparison.

#### Sketch Proof of KL $\ge$ 0:

Let $f(x) = \log x$, which is concave. Apply Jensen’s inequality:

$$
\sum_x p(x) \log \frac{q(x)}{p(x)} \le \log \left( \sum_x p(x) \frac{q(x)}{p(x)} \right) = \log \left( \sum_x q(x) \right) = \log 1 = 0
$$

Therefore:
$$
-\text{KL}(p \| q) \le 0 \Rightarrow \text{KL}(p \| q) \ge 0
$$

Equality holds if and only if $p(x) = q(x)$ for all $x$.

---

### 3. Mutual Information – Shared Information

Mutual information between two variables $x$ and $y$ is defined as:

$$
I[x, y] = \sum_{x,y} p(x, y) \log \frac{p(x, y)}{p(x) p(y)}
$$

#### Equivalently:
- The **KL divergence between the joint and the product of marginals**:
  $$
  I[x, y] = \text{KL}(p(x, y) \| p(x)p(y))
  $$
- The **reduction in uncertainty** of one variable given the other:
  $$
  I[x, y] = H[x] - H[x \mid y] = H[y] - H[y \mid x]
  $$

#### Symmetric:
- Unlike KL divergence, mutual information **is symmetric**:
  $$
  I[x, y] = I[y, x]
  $$

#### Special Case:
If $x$ and $y$ are independent, then:
$$
p(x, y) = p(x)p(y) \Rightarrow I[x, y] = 0
$$

---

## Why It Matters

- **Entropy** gives a principled way to measure uncertainty — foundational for compression, communication, and model evaluation.
- **KL divergence** quantifies the cost of mismatch between models and reality — crucial in model selection and approximation (e.g., variational inference).
- **Mutual information** provides a bridge between joint and marginal behaviors — often used in feature selection, information bottleneck methods, and more.

---

## Relevant Figures from PRML

- **Figure 1.14**: Illustrates the entropy of binary variables as a function of $p(x)$. Shows maximum entropy at $p = 0.5$ and symmetric decay toward 0.
- **Figure 1.15**: Compares $\text{KL}(p \| q)$ and $\text{KL}(q \| p)$ for Gaussian distributions. Highlights asymmetry visually.
