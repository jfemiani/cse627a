import numpy as np
import matplotlib.pyplot as plt

# Generate a synthetic dataset
np.random.seed(110)
n_samples = 100
X = nonseparable_X
y = nonseparable_y
# Fit logistic regression using IRLS
w_est = irwls(X, y, alpha=alpha)

# Plot the dataset and decision boundary
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdBu_r)
xlim = plt.xlim()
ylim = plt.ylim()
xx, yy = np.meshgrid(np.linspace(*xlim, 100), np.linspace(*ylim, 100))
Z = sigmoid(np.c_[xx.ravel(), yy.ravel()] @ w_est)
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, levels=20, zorder=-1)
plt.contour(xx, yy, Z, levels=[0.5], colors='k')
plt.xlim(xlim)
plt.ylim(ylim)
plt.title("Logistic regression using IRLS")
plt.show()
