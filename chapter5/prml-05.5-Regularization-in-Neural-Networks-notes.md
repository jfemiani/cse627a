# Lecture Notes: PRML Chapter 5.5 – Regularization in Neural Networks

## Prerequisites
- Neural network architecture: input/hidden/output layers, weights, biases
- Maximum likelihood estimation and overfitting
- Sum-of-squares error function
- Gaussian priors and Bayesian interpretation of regularization
- Jacobian and Hessian (basic familiarity)


---

## Key Terminology

- **Regularization**: Technique for reducing overfitting by adding constraints or penalties to the loss function.
- **Weight decay**: A common form of regularization that penalizes large weights by adding a quadratic penalty term.
- **Early stopping**: Halting training when validation performance degrades, preventing overfitting.
- **Tangent propagation**: Regularization method that encourages local invariance to specific input transformations.
- **Convolutional layer**: Network layer with localized receptive fields and shared weights, enforcing spatial translation invariance.
- **Soft weight sharing**: A regularization approach where weights are softly clustered using a mixture of Gaussian priors.

---

---

## Core Framing: Capacity, Overfitting, and Regularization

### Model Capacity
The **capacity** of a model refers to its ability to fit a wide variety of functions. Formally, it can be related to:
- The number and flexibility of parameters (weights and biases)
- The complexity of functions representable by the model
- The model’s ability to interpolate or extrapolate training data

High-capacity models (e.g. deep networks with many hidden units) can represent intricate decision boundaries or regression surfaces, but are also prone to **overfitting** — learning patterns specific to the training data that do not generalize.

### Overfitting and Capacity Mismatch
**Overfitting** typically occurs when the model's effective capacity exceeds the complexity of the underlying data-generating process *and* the training data is insufficient to constrain the model’s parameters. Importantly:
- This is not just about the *number* of parameters exceeding the number of training examples.
- A model can overfit even with fewer parameters if they are too flexible, or if the data has significant noise or bias.
- The true issue is the **imbalance between model capacity and the quantity/quality of training data.**

---

## Strategies to Address Overfitting

### 1. Increase the Amount of Data
- **More data** improves generalization by better constraining the solution space.
- **Data augmentation** (e.g., rotating images, adding noise) synthetically increases data diversity.
- **Synthetic data generation** can inject new plausible samples (e.g., GANs, simulations).
- **Limitations**: Costly, may not match the true distribution, and doesn't scale well with model size.

### 2. Reduce the Number of Parameters
- Shrinking the model (fewer hidden units, lower depth) can reduce capacity.
- **Downside**: This imposes *discrete* constraints and may remove useful structure or necessary expressivity.
- Leads to coarser control of complexity, often suboptimal for nuanced tasks.

### 3. Add Regularization
**Regularization** imposes soft constraints on the solution space, augmenting the loss function with additional penalty terms or architectural constraints. This:
- Provides *continuous* control over model complexity.
- Allows us to inject **prior knowledge**: e.g., favoring smoothness, small weights, or specific invariances.
- Can guide training toward *simpler* or *more generalizable* solutions.

Examples of prior beliefs we can encode:
- *Don’t be overconfident*: Keeping weights small prevents sharp activation changes; if outputs are interpreted as probabilities (e.g., via a sigmoid), this prevents overconfident classification.
- *Intermediate layer sufficiency*: Auxiliary tasks like "predict the target from layer 4 alone" enforce robustness and layer-wise feature relevance.



## Why It Matters

Regularization lies at the heart of generalization. Without it, modern neural networks—often vastly overparameterized—would fail to perform well outside their training set. Unlike capacity reduction, regularization enables nuanced, continuous control over model complexity, and can encode domain-specific biases (e.g., invariance to transformations or confidence calibration). It is the primary tool by which we make deep learning work in finite-data regimes.

---

## Key Ideas

### Weight Decay and Gaussian Priors

#### Formula
The simplest regularized error function:
$$
\tilde{E}(w) = E(w) + \frac{\lambda}{2} \|w\|^2
$$
where $\lambda > 0$ controls the strength of the penalty.

#### Explanation
This encourages small weight magnitudes, leading to smoother and more stable predictions. Bayesian interpretation: corresponds to placing a zero-mean isotropic Gaussian prior on weights.

> Note: This form **is not invariant** under linear transformations of the input or output.

---

### Scale-Consistent Regularization

#### Problem
Weight decay penalizes all weights equally, which can distort scale-invariant mappings. For instance, rescaling inputs or outputs may necessitate compensating changes in weights.

#### Solution
Use **layer-specific regularizers**:
$$
\frac{\lambda_1}{2} \sum_{w \in W_1} w^2 + \frac{\lambda_2}{2} \sum_{w \in W_2} w^2
$$
This supports **input/output rescaling** if $\lambda_1$ and $\lambda_2$ are adjusted accordingly.

#### Bayesian view
This corresponds to an **anisotropic Gaussian prior** with different precision parameters $\alpha_1$, $\alpha_2$ per layer:
$$
p(w) \propto \exp\left( -\frac{\alpha_1}{2} \|W_1\|^2 - \frac{\alpha_2}{2} \|W_2\|^2 \right)
$$

---

### Early Stopping

#### Idea
Monitor performance on a **validation set**. Stop training when validation error increases, even if training error continues to decrease.

#### Explanation
During training, model complexity effectively grows. Early stopping halts before reaching high-complexity (overfit) states.

#### Theoretical Insight
In quadratic loss landscapes, early stopping behaves similarly to weight decay. The product $\tau \eta$ (iteration count × learning rate) acts like $\lambda^{-1}$.

---

### Tangent Propagation

#### Idea
Encourage invariance to smooth transformations (e.g. small rotations, translations) by penalizing sensitivity in that direction.

#### Tangent Vector
Let $s(x, \xi)$ be a transformation of input $x$ parameterized by $\xi$. Then the tangent vector is:
$$
\tau = \left. \frac{\partial s(x, \xi)}{\partial \xi} \right|_{\xi=0}
$$

#### Regularized Loss
Add a penalty based on change in output w.r.t transformation:
$$
\tilde{E} = E + \lambda \Omega,\quad \text{where} \quad \Omega = \frac{1}{2} \sum_n \sum_k \left( \sum_i J_{k i} \tau_i \right)^2
$$

---

### Training with Transformed Data

#### Idea
Augment the training set with multiple transformed versions of each input.

#### Equivalence
Mathematically, this is equivalent to **tangent propagation** in the small-noise limit. The regularizer becomes:
$$
\Omega = \frac{1}{2} \int \|\nabla y(x)\|^2 p(x) dx
$$
This is known as **Tikhonov regularization**.

---

### Convolutional Neural Networks (CNNs)

CNNs encode translation invariance via architectural constraints:
1. **Local receptive fields**: Units receive input from local regions.
2. **Weight sharing**: All units in a feature map share parameters.
3. **Subsampling**: Downsampling layers promote insensitivity to small shifts.

> Key Point: CNNs use **hardwired invariance** instead of learned regularizers.

---

### Soft Weight Sharing

#### Idea
Encourage weights to form clusters, but allow flexibility. Assign a **mixture of Gaussians** as a prior over weights:
$$
p(w_i) = \sum_{j=1}^M \pi_j \mathcal{N}(w_i \mid \mu_j, \sigma_j^2)
$$

#### Regularization Term
Total regularized error:
$$
\tilde{E}(w) = E(w) - \lambda \sum_i \ln \left( \sum_j \pi_j \mathcal{N}(w_i \mid \mu_j, \sigma_j^2) \right)
$$

#### Learning
The mixture parameters $\{\mu_j, \sigma_j, \pi_j\}$ are learned jointly with the weights. This encourages grouping, but not strict tying (as in CNNs).

---

## Relevant Figures from PRML

- **Figure 5.9**: Examples of networks with different hidden units. Shows underfitting ($M=1$), good fit ($M=3$), overfitting ($M=10$).
- **Figure 5.10**: Validation error vs. number of hidden units. Emphasizes how local minima can obscure generalization performance.
- **Figure 5.11**: Effect of hyperparameters in Gaussian priors on network function shape.
- **Figure 5.12**: Training vs. validation error during early stopping. Clear visualization of ideal stopping point.
- **Figure 5.13**: Weight space trajectory—why early stopping resembles weight decay.
- **Figure 5.14**: Warped digit examples—motivates invariance and tangent propagation.
- **Figure 5.15–16**: Tangent vector derivation and illustration via infinitesimal image rotation.
- **Figure 5.17**: Architecture of CNNs with convolution and subsampling layers.
- **Figure 5.18**: Forward/inverse kinematics of a robot arm—motivates the need for mixture models in inverse problems.