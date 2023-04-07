import numpy as np
import matplotlib.pyplot as plt

# Generate non-linearly separable data
np.random.seed(0)
X = np.random.randn(500, 2)
y = np.array([1 if np.linalg.norm(x) < 1 else -1 for x in X])

# Plot non-linearly separable data
plt.figure(figsize=(10,5))
plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title('Non-linearly separable data')

# Apply polar transformation to make data linearly separable
def polar_transform(X):
    r = np.linalg.norm(X, axis=1)
    theta = np.arctan2(X[:, 1], X[:, 0])
    return np.column_stack((r, theta))

X_transformed = polar_transform(X)

# Plot transformed data
plt.subplot(122)
plt.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y)
plt.title('$\phi(x)$ linearly separable after transformation')
plt.show()
