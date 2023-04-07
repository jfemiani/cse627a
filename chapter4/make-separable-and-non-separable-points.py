import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
np.random.seed(42)

# Define the optimal decision surface as a diagonal line
w = np.array([1, 1])
b = 0
# Generate separable data points with a margin of 0.5
num_separable_points = 100
separable_X = np.random.uniform(low=-2, high=2, size=(num_separable_points, 2))
separable_y = np.sign(separable_X.dot(w))
distance = np.abs(separable_X.dot(w) + b) / np.sqrt(w.dot(w))
margin_indices = distance > 0.5
# margin_indices = np.abs(separable_X.dot(w)) > (np.sqrt(2) / 2) - 0.5
margin_X = separable_X[margin_indices]
margin_y = separable_y[margin_indices]

# Generate non-separable data points by flipping the labels on the margin
nonseparable_X = separable_X.copy()
nonseparable_y = separable_y.copy()
nonseparable_y[~margin_indices] *= -1


def plot_decision_boundary(ax, w, b, x_range=None, label='Decision Boundary'):
    """Plot the decision boundary defined by w and b"""
    if x_range is None:
        x_range = np.linspace(-2, 2)
    y_range = -(w[0]/w[1])*x_range - b/w[1]
    ax.plot(x_range, y_range, color='red', label=label)

    
    
# Plot the data points
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 4))
ax1.scatter(margin_X[:, 0], margin_X[:, 1], c=margin_y)
plot_decision_boundary(ax1, w, b)
ax1.set_title("Separable Data with Margin")
ax2.scatter(nonseparable_X[:, 0], nonseparable_X[:, 1], c=nonseparable_y)
ax2.set_title("Non-Separable Data")
plot_decision_boundary(ax2, w, b)
plt.show()
