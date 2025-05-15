# Lecture Notes: PRML Chapter 5.3 – Error Backpropagation

## Prerequisites
- Understanding of feedforward neural networks (Section 5.1)
- Chain rule from multivariate calculus
- Gradient descent optimization
- Activation functions (e.g., tanh, sigmoid, softmax)
- Error functions (e.g., sum-of-squares, cross-entropy)

## Key Terminology
- **Backpropagation**: An efficient method for computing derivatives of the error function with respect to weights in a feedforward neural network by propagating error signals backward.
- **Local gradient (δ)**: The derivative of the error function with respect to the weighted input of a unit, i.e., $\delta_j = \frac{\partial E_n}{\partial a_j}$.
- **Forward propagation**: Computing the activations of each layer in the network from input to output.
- **Jacobian matrix**: Matrix of partial derivatives $\frac{\partial y_k}{\partial x_i}$ measuring sensitivity of output to input.
- **Hessian matrix**: Matrix of second-order partial derivatives $\frac{\partial^2 E}{\partial w_i \partial w_j}$ representing curvature of the error surface.

## Why It Matters
Backpropagation is the backbone of modern deep learning. Without it, computing gradients for large networks would be prohibitively expensive. Its elegance lies in converting global derivative computation into a local message-passing scheme. Mastery of backprop is essential for implementing and understanding modern ML models.

## Key Ideas

### Why It Matters
Training neural networks requires efficient computation of gradients of an error function with respect to a large number of weights. Backpropagation exploits the structure of the network to compute these gradients in time linear in the number of weights.

### Backpropagation Recursion

Backpropagation computes the partial derivatives of the error with respect to each weight by recursively computing *local gradients* (δ terms).

Each unit $j$ receives input $a_j = \sum_i w_{ji} z_i$ and produces activation $z_j = h(a_j)$. We define:

$$
\delta_j \equiv \frac{\partial E_n}{\partial a_j}
$$

For **output units**, we use the chain rule:

$$
\delta_k = \frac{\partial E_n}{\partial a_k} = \frac{\partial E_n}{\partial y_k} \cdot \frac{dy_k}{da_k}
$$

The form of $\delta_k$ depends on the loss and output activation.

For **hidden units**, the error is propagated backward:

$$
\delta_j = h'(a_j) \sum_k w_{kj} \delta_k
$$

This allows gradients to be computed in reverse through the network using local information.

---

### 🔍 Derivatives of Common Activations

#### Sigmoid
$$
\sigma(a) = \frac{1}{1 + e^{-a}}, \quad \sigma'(a) = \sigma(a)(1 - \sigma(a))
$$

#### Tanh
$$
\tanh(a) = \frac{e^a - e^{-a}}{e^a + e^{-a}}, \quad \tanh'(a) = 1 - \tanh^2(a)
$$

---

## Worked Examples
### 1. MSE Loss, Tanh Hidden Units, Linear Outputs

**Forward Computation:**

1. **Input to Hidden Layer:**  
   For each hidden unit \(j\), compute the weighted input:  
   $$
   a_j^{(1)} = \sum_i w_{ji}^{(1)} x_i \quad \text{(plus bias if applicable)}
   $$

2. **Hidden Activation:**  
   Apply the tanh function:  
   $$
   z_j^{(1)} = \tanh\Big(a_j^{(1)}\Big)
   $$

3. **Hidden to Output Layer:**  
   For each output unit \(k\), compute the weighted sum:  
   $$
   a_k^{(2)} = \sum_j w_{kj}^{(2)} z_j^{(1)} \quad \text{(plus bias if applicable)}
   $$

4. **Output Activation:**  
   With a linear output, the activation is:  
   $$
   y_k = a_k^{(2)}
   $$

5. **Loss Calculation:**  
   Compute the Mean Squared Error (MSE):  
   $$
   E_n = \frac{1}{2} \sum_k \Big(y_k - t_k\Big)^2
   $$

**Backward Propagation:**

1. **Output Layer:**  
   Compute the gradient of the loss with respect to \(y_k\):  
   $$
   \frac{\partial E_n}{\partial y_k} = y_k - t_k
   $$
   Since the output activation is linear $\frac{dy_k}{da_k^{(2)}} = 1$,  
   $$
   \delta_k^{(2)} = \frac{\partial E_n}{\partial a_k^{(2)}} = y_k - t_k
   $$

2. **Hidden Layer:**  
   The derivative of the tanh activation is:  
   $$
   h'(a_j^{(1)}) = 1 - \tanh^2\Big(a_j^{(1)}\Big) = 1 - \Big(z_j^{(1)}\Big)^2
   $$
   Then, backpropagate the error:  
   $$
   \delta_j^{(1)} = \Big(1 - \Big(z_j^{(1)}\Big)^2\Big) \sum_k w_{kj}^{(2)} \delta_k^{(2)}
   $$

3. **Weight Updates:**  
   - For weights from input to hidden layer:  
     $$
     \frac{\partial E_n}{\partial w_{ji}^{(1)}} = \delta_j^{(1)} \, x_i
     $$  
   - For weights from hidden to output layer:  
     $$
     \frac{\partial E_n}{\partial w_{kj}^{(2)}} = \delta_k^{(2)} \, z_j^{(1)}
     $$

---

### 2. Cross-Entropy Loss, Sigmoid Output

**Forward Computation:**

1. **Input to Output Layer:**  
   Compute the weighted input for the output unit:  
   $$
   a^{(1)} = \sum_i w_i^{(1)} x_i \quad \text{(plus bias if applicable)}
   $$

2. **Output Activation:**  
   Apply the sigmoid function:  
   $$
   y = \sigma\Big(a^{(1)}\Big) = \frac{1}{1 + e^{-a^{(1)}}}
   $$

3. **Loss Calculation:**  
   Compute the cross-entropy loss for a binary classification target \(t\):  
   $$
   E_n = -t \log y - (1 - t) \log (1 - y)
   $$

**Backward Propagation:**

1. **Output Layer:**  
   Compute the derivative of the loss with respect to \(y\):  
   $$
   \frac{\partial E_n}{\partial y} = -\frac{t}{y} + \frac{1 - t}{1 - y}
   $$
   The derivative of the sigmoid function is:  
   $$
   \frac{dy}{da^{(1)}} = y(1 - y)
   $$
   Using the chain rule, we have:  
   $$
   \delta^{(1)} = \frac{\partial E_n}{\partial a^{(1)}} = \frac{\partial E_n}{\partial y} \cdot \frac{dy}{da^{(1)}}
   $$
   However, for sigmoid activation combined with cross-entropy loss, these terms simplify to:  
   $$
   \delta^{(1)} = y - t
   $$

2. **Weight Update:**  
   For weights from input to the output layer:  
   $$
   \frac{\partial E_n}{\partial w_i^{(1)}} = \delta^{(1)} \, x_i
   $$

---

### 3. Example: ReLU → Sigmoid → Cross-Entropy

**Forward Computation:**

1. **Input to Hidden Layer 1:**  
   Compute the weighted input for the first hidden layer:  
   $$
   a^{(1)} = W_1 x + b_1
   $$

2. **Hidden Layer 1 Activation (ReLU):**  
   Apply the ReLU function:  
   $$
   z^{(1)} = \text{ReLU}\Big(a^{(1)}\Big) = \max\big(0, a^{(1)}\big)
   $$

3. **Hidden Layer 1 to Hidden Layer 2:**  
   Compute the weighted input for the second hidden layer:  
   $$
   a^{(2)} = W_2 z^{(1)} + b_2
   $$

4. **Hidden Layer 2 Activation (Sigmoid):**  
   Apply the sigmoid function:  
   $$
   z^{(2)} = \sigma\Big(a^{(2)}\Big) = \frac{1}{1 + e^{-a^{(2)}}}
   $$

5. **Output Calculation:**  
   Set the output as:  
   $$
   y = z^{(2)}
   $$

6. **Loss Calculation:**  
   Compute the cross-entropy loss for a binary target \(t\):  
   $$
   E = -t \log y - (1 - t) \log(1 - y)
   $$

**Backward Propagation:**

1. **Output Layer (Hidden Layer 2):**  
   Compute the gradient at the output using the sigmoid-cross-entropy identity:  
   $$
   \delta^{(2)} = y - t
   $$

2. **Hidden Layer 2 (Sigmoid):**  
   The derivative of the sigmoid is:  
   $$
   \sigma'(a^{(2)}) = z^{(2)} \big(1 - z^{(2)}\big)
   $$
   But the simplified gradient remains:  
   $$
   \delta^{(2)} = y - t
   $$

3. **Backpropagation to Hidden Layer 1 (ReLU):**  
   The derivative of the ReLU activation is:  
   $$
   \frac{d}{da^{(1)}} \text{ReLU}\Big(a^{(1)}\Big) =
   \begin{cases}
   1 & \text{if } a^{(1)} > 0 \\
   0 & \text{otherwise}
   \end{cases}
   $$
   Backpropagate the error:  
   $$
   \delta^{(1)} = \mathbf{1}\Big[a^{(1)} > 0\Big] \cdot \big(W_2^\top \delta^{(2)}\big)
   $$

4. **Weight Updates:**  
   - For weights from Hidden Layer 1 to Hidden Layer 2:  
     $$
     \frac{\partial E}{\partial W_2} = \delta^{(2)} \cdot \big(z^{(1)}\big)^\top
     $$
   - For weights from Input to Hidden Layer 1:  
     $$
     \frac{\partial E}{\partial W_1} = \delta^{(1)} \cdot x^\top
     $$

This version now includes layer superscripts for clarity.

## Jacobian Matrix

Assume the output $y_k$ *is* the loss (e.g., scalar regression or reduced objective). Then the **Jacobian** of the loss with respect to inputs is:

$$
J_{ki} = \frac{\partial y_k}{\partial x_i}
$$

This measures how much the loss would change with respect to each input component $x_i$. The Jacobian is useful for sensitivity analysis, interpretability, and adversarial robustness.
