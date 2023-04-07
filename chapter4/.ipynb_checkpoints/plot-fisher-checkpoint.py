import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

def plot_fisher(X, y):
    # Separate data into classes
    X0 = X[y == 0]
    X1 = X[y == 1]

    # Calculate means of each class
    mean0 = np.mean(X0, axis=0)
    mean1 = np.mean(X1, axis=0)

    # Calculate covariance matrices for each class
    cov0 = np.cov(X0.T)
    cov1 = np.cov(X1.T)

    # Calculate within-class scatter matrix
    SW = cov0 + cov1

    # Calculate Fisher's linear discriminant
    w = np.linalg.inv(SW) @ (mean1 - mean0)
    w /= np.linalg.norm(w)

    # Project data onto Fisher's linear discriminant
    y0 = X0 @ w
    y1 = X1 @ w

    # Calculate threshold for Fisher's linear discriminant
    threshold = (mean0 @ w + mean1 @ w) / 2

    # Calculate points for separating line
    xline = np.linspace(np.min(X @ w), np.max(X @ w), 100)
    yline = xline * -w[0] / w[1] + threshold / w[1]

    # Calculate ellipse parameters
    eigvals0, eigvecs0 = np.linalg.eig(cov0)
    eigvals1, eigvecs1 = np.linalg.eig(cov1)

    # Plot data points and histograms
    fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(12, 6))

    ax0.scatter(X0[:, 0], X0[:, 1], color='red', marker='x')
    ax0.scatter(X1[:, 0], X1[:, 1], color='blue', marker='+')
    ax0.plot(mean0[0], mean0[1], color='red', marker='o', markersize=10)
    ax0.plot(mean1[0], mean1[1], color='blue', marker='o', markersize=10)

    ellipse0 = Ellipse(xy=mean0, width=eigvals0[0], height=eigvals0[1], angle=np.degrees(np.arctan2(*eigvecs0[:,0][::-1])), edgecolor='red', fill=False)
    ax0.add_artist(ellipse0)
    ellipse1 = Ellipse(xy=mean1, width=eigvals1[0], height=eigvals1[1], angle=np.degrees(np.arctan2(*eigvecs1[:,0][::-1])), edgecolor='blue', fill=False)
    ax0.add_artist(ellipse1)

    ax1.hist(y0, alpha=0.5, bins=20, color='red')
    ax1.hist(y1, alpha=0.5, bins=20, color='blue')

    # Plot Fisher's linear discriminant and threshold
    ax0.plot(xline, yline, color='green', linestyle='--', linewidth=2)
  
    # Plot projection line
    xproj = np.linspace(np.min(X[:, 0]), np.max(X[:, 0]), 100)
    yproj = xproj * -w[1] / w[0]

    

    # Plot threshold
    ax1.axvline(x=threshold, c='g', ls='--', lw=2)
    ax1.set_xlabel('Projection')
    ax1.set_ylabel('Density')
    plt.suptitle('Fisher Discriminant Analysis')
    plt.show()
