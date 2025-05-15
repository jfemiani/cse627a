# Lecture Notes: PRML Chapter 5 – Neural Networks

## Prerequisites

- **Linear Models:** Understanding of regression and classification using linear combinations of fixed basis functions.
- **Logistic Regression & Curve Fitting:** Familiarity with maximum likelihood estimation and sum-of-squares error functions.
- **Basic Optimization:** Knowledge of gradient-based optimization techniques and nonconvex functions.
- **Matrix Calculus:** Basic skills in handling matrices, derivatives, and transformations.
- **Foundations in Pattern Recognition:** Exposure to the curse of dimensionality and the motivation for adaptive models (models with parameters estimated from data).

## Key Terminology

- **Neural Network:** A parametric model for pattern recognition that uses adaptive nonlinear basis functions.
- **Multilayer Perceptron (MLP):** A feed-forward neural network with one or more hidden layers of nonlinear units.
- **Feed-forward Network:** A network where the connections between units do not form cycles; information flows from input to output.
- **Hidden Units:** Neurons in the network that are neither inputs nor outputs; they perform intermediate nonlinear transformations. (Also called hidden variables.)
- **Activation Function:** A nonlinear function (e.g., logistic sigmoid, tanh, softmax) applied to the weighted sum of inputs.
- **Weights and Biases:** Parameters of the network; weights determine the strength of connections, and biases provide an offset.
- **Forward Propagation:** The process of computing the output of the network from the inputs by passing through each layer.
- **Backpropagation:** An efficient method for computing gradients of the network’s error function with respect to its parameters.
- **Weight-Space Symmetries:** The phenomenon where multiple distinct sets of weights produce the same input–output mapping.
- **Skip-Layer Connections:** Additional connections that bypass one or more layers, potentially enhancing network expressiveness.

## Why It Matters

Neural networks offer a flexible approach to modeling complex, nonlinear relationships in data. Unlike linear models with fixed basis functions, neural networks adapt their basis functions during training, enabling them to:

- **Capture Nonlinearity:** Represent complicated functions by stacking layers of nonlinear transformations.
- **Reduce Dimensionality:** Learn compact representations, potentially overcoming the curse of dimensionality.
- **Serve as Universal Approximators:** Given sufficient capacity, approximate any continuous function on a compact domain.
- **Enable Fast Evaluation:** Despite complex training, the resulting network can be computationally efficient during inference.
- **Facilitate Extensions:** Provide a foundation for advanced topics such as convolutional networks, Bayesian neural networks, and deep learning architectures.

## Key Ideas

- **Adaptive Basis Functions:**  
  Traditional linear models use fixed nonlinear basis functions, e.g. $\phi_i(\mathbf{x}_n)$. Neural networks extend this by making the basis functions adaptive; each hidden unit computes a nonlinear function of a weighted linear combination of inputs:
  $$
  a_j = \sum_{i=1}^D w^{(1)}_{ji} x_i + w^{(1)}_{j0} \quad \text{and} \quad z_j = h(a_j)
  \tag{5.2 \& 5.3}
  $$
  This allows the network to learn representations directly from the data.

  - $w_{ji}^{(1)}$ is a weight for _input_ $x_i$ to  _activation_  $a_j$ in _layer 1_, indicated by the superscript.
  - $w^{(1)}_{j0}$ is the _bias_ for activation $a_j$.
  - $a_j$ are _activations_ (before applying the activation function).  
    > Nomenclature is messy—sometimes $z_j$ are also called activations in practice, though that may not be strictly correct.
  - $h(\cdot)$ is an _activation function_ which adds nonlinearity to the basis.

- **Layered Architecture:**  
  The network is typically organized into layers. For example, a two-layer network (or single-hidden-layer network) has:
  - **Input Layer (Read-in layer):** Receives the raw input features and initial processing.
  - **Hidden Layer (Backbone):** Applies nonlinear transformations via activation functions (e.g., tanh, sigmoid). This layer extracts features or hidden representations.
  - **Output Layer (Read-out layer, or head):** Combines hidden unit outputs, often with task-specific activation functions (linear for regression, softmax for classification).
  
  The overall 2-layer network function can be written as:
  $$
  y_k(x,w) = \sigma\!\Bigl(\sum_{j=0}^{M} w^{(2)}_{kj}\, h\Bigl(\sum_{i=0}^{D} w^{(1)}_{ji} x_i\Bigr)\Bigr)
  \tag{5.9}
  $$
  where the inputs $x_0$ and hidden outputs $z_0$ are fixed to 1 to absorb bias terms.

- **Importance of Nonlinearity:**
  - Suppose you did nt have it...
     $W^{(2)}\Bigl(W^{(1}\mathbf{x}\Bigr) = \Bigl(W^{(2)}W^{(1)}\Bigr)\mathbf{x} = W\mathbf{x}$ for some W. So... w/o nonlinearity there is no point in multiple layers, we are stuck with a linear model.

- **Forward Propagation and Differentiability:**  
  - The process of computing outputs from inputs is called forward propagation.
  - Each step must be (mostly) differentiable, at least where it is evaluated.

- **Error Backpropagation:**  
  - Training the network involves minimizing an error (or loss) function.
  - Backpropagation is used to efficiently compute gradients of the loss with respect to the network’s parameters.
  - This enables methods like gradient descent to update weights and biases.
  - Discussed further in Section 5.3.

- **Weight-Space Symmetries:**  
  - Optimal weights are not unique (this discouraged early adoption).
  - Neural networks often exhibit symmetries.
  - For instance, flipping the sign of weights into a hidden unit and compensating by flipping the sign of outgoing weights leaves the overall function unchanged.
  - Similarly, changing the order of hidden units also leaves the function unchanged.

- **Universal Approximation Capability:**
  - Neural networks with at least one hidden layer (two-layer networks) can approximate any continuous function on a compact domain, given enough hidden units.
  - This universal approximation property motivates their widespread use in practice.

- **Network Generalization and Extensions:**  
  - Although nonconvex optimization appears problematic theoretically, neural networks have proven highly effective in practical applications.
  - Architectures can be extended by:
    - Adding more layers (deep networks)
    - Introducing skip (residual) connections
    - Imposing sparsity (convolutional neural networks)
    - Changing activation functions
    - Using dynamic or shared weights (transformers, recurrent networks)
  - These extensions improve network expressiveness and performance on complex tasks.

## Historical Context

Neural Netowrks have along history -- with periods of hyp and disfavors (AI winters).

- **1950s–1960s (Early Hype):**
  - Neural networks, such as Rosenblatt’s perceptron (introduced in 1957), generated substantial early excitement.
  - Initial theoretical and experimental successes led to optimistic predictions about imminent breakthroughs in artificial intelligence.

- **1970s–1980s (First Neural Network "Winter"):**
  - Minsky and Papert’s influential book, _Perceptrons_ (1969), highlighted critical limitations of single-layer networks, contributing to a significant decline in funding and interest in neural network research.
  - In particular, a single-layer network could not learn XOR (duh! )
  - The field entered a period of disfavor, marking the first "AI winter."
  - Other ideas (like PROLOG) were in vogue.

- **1980s–1990s (Second Wave & Shallow-Network Era):**
  - Renewed interest following the introduction of backpropagation (popularized by Rumelhart, Hinton, and Williams in 1986), which enabled training multi-layer neural networks (MLPs).
  - Universal approximation theorems demonstrated theoretically that even shallow networks (with just one hidden layer) could approximate arbitrary continuous functions, reinforcing an _incorrect_ belief that deeper networks were unnecessary.
    - But some (Hinton, LeCun, their progeny) trucked on.
  - Practical limitations (small datasets, insufficient computational resources) again led to disappointing real-world performance, and a second wave of disillusionment followed.
  - Other ideas (SVMs, Trees, Boosting) were in vogue.

- **Post-2012 (Deep Learning Revolution):**
  - Dramatic improvement in empirical performance driven by significantly deeper networks, larger datasets (e.g., ImageNet), and GPU-accelerated training.
  - This revolution challenged previous misconceptions, proving practically that deeper architectures are essential for high performance.
  - We keep waiting with a "Winter is Coming" dread, but it hasn't come yet ... (dependoing on when you read these notes)

## Relevant Figures from PRML

- **Figure 5.1 (Network Diagram):**  
  Illustrates the two-layer neural network architecture with inputs, hidden units, and outputs. The diagram shows the flow of information and highlights how bias parameters are incorporated.
  
- **Figure 5.2 (General Feed-forward Topology):**  
  Depicts a more complex network with skip-layer connections and varying degrees of connectivity. It emphasizes that the architecture remains feed-forward (acyclic), ensuring deterministic output computations.
  
- **Figure 5.3 (Function Approximation Examples):**  
  Demonstrates the network’s ability to approximate different functions (e.g., quadratic, sinusoidal, absolute value, and step functions) using a limited number of hidden units.
  
- **Figure 5.4 (Classification Example):**  
  Shows the decision boundaries formed by a neural network on a synthetic classification problem, along with the contours of hidden unit activations, illustrating how the network combines hidden units to achieve classification.
