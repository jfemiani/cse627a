Quiz title: 06.3 – Radial Basis Function Networks  
Quiz description: This quiz tests understanding of key concepts from Section 6.3 of PRML.  
shuffle answers: true  
show correct answers: false


Title: medium – understand – non-edge – Meaning of Nadaraya–Watson
Points: 1
1. Which of the following best explains the Nadaraya–Watson model in kernel regression?
a) It assigns the label of the nearest training input to each test point
... Incorrect. That describes nearest-neighbor classification, not kernel regression.
*b) It computes a smooth, weighted average of training targets using normalized kernel similarities
... Correct. NW performs local averaging where the influence of each training point is kernel-weighted.
c) It fits a linear model to kernel-transformed features
... Incorrect. That’s a kernel ridge regression idea, not NW.
d) It learns a parametric mapping from inputs to outputs using basis expansions
... Incorrect. NW is nonparametric and does not learn explicit parameters for the mapping.


Title: medium – understand – edge – Parzen interpretation of Nadaraya–Watson
Points: 1
1. When all training targets are 1, what does the Nadaraya–Watson model reduce to?
a) A hard decision boundary based on the largest kernel response
... Incorrect. NW performs smoothing, not thresholding.
*b) A Parzen window estimate of the input probability-density
... Correct. This follows directly from summing normalized kernels with constant targets.
c) A support vector machine with Gaussian kernel
... Incorrect. That’s a discriminative classifier, not density estimation.
d) A histogram of the training data
... Incorrect. Histograms are not kernel-based and lack smoothness.


Title: medium – understand – non-edge – Input noise causes kernel smoothing in NW
Points: 1
1. In the Nadaraya–Watson model, each input $x_n$ is assumed to be observed with noise — that is, the true input becomes $x_n + \xi$, where $\xi$ is a random variable with distribution $\nu(\xi)$ (often a kernel function). How does this affect the model's predictions?
a) The model averages nearby inputs before mapping them to a shared target
... Incorrect. The inputs are not averaged or combined directly.
*b) The model smooths predictions by averaging target values, weighted by how likely each training input is to match the noisy observation
... Correct. Input noise leads to a kernel-weighted average of target values — a local conditional expectation.
c) The model adjusts target values based on how far they are from the mean
... Incorrect. The targets are not modified — only the weights are.
d) The model fits a parametric regression surface by marginalizing over noise
... Incorrect. NW is a nonparametric model using stored data and no explicit surface.


Title: concept-check – remember – non-edge – Definition of RBF
Points: 1
1. What defines a radial basis function (RBF)?
a) A function that depends on both $x$ and $\mu_j$ independently
... Incorrect. RBFs depend only on the distance between $x$ and $\mu_j$.
*b) A function that depends only on $\|x - \mu_j\|$
... Correct. Radial basis functions are isotropic and depend only on the distance to a center.
c) A feature map that includes all polynomial terms of $x$
... Incorrect. That's related to polynomial kernels, not RBFs.
d) A linear function of the input vector $x$
... Incorrect. Linear functions are not basis functions of radial type.


Title: concept-check – remember – non-edge – What radial means
Points: 1
1. In a radial basis function, what does the term “radial” refer to?
a) The use of circular basis functions in 2D input space
... Incorrect. RBFs are not limited to 2D or circular geometry.
*b) Dependence only on the distance $\|x - \mu_j\|$ from a center
... Correct. “Radial” means isotropic dependence on distance.
c) The angular orientation of basis vectors in feature space
... Incorrect. RBFs are not direction-dependent.
d) A basis that rotates with the input distribution
... Incorrect. Basis functions are fixed and do not rotate.


Title: medium – understand – non-edge – RBF design matrix
Points: 1
1. What does the design matrix $\Phi$ represent in an RBF network?
a) The covariance matrix of the RBF kernel
... Incorrect. That would be the Gram matrix $K$, not $\Phi$.
*b) The activations of all basis functions for each training input
... Correct. $\Phi_{nj} = \phi_j(x_n)$ encodes how inputs activate the RBFs.
c) A matrix of learned parameters between the input and hidden layer
... Incorrect. RBF weights are not learned per input dimension.
d) The projection of the inputs into a higher-dimensional feature space
... Incorrect. This is a generic description of feature maps, not $\Phi$ specifically.


Title: medium – understand – edge – Convex combinations in normalized RBFs
Points: 1
1. Why do normalized RBF networks always produce outputs within the range of training targets?
a) Because the network minimizes squared error between the predicted and actual outputs
... Incorrect. Minimizing squared error does not imply constraints on output range.
*b) Because predictions are convex combinations of training targets with non-negative weights summing to 1
... Correct. This ensures predictions lie in the convex hull of target values.
c) Because the output layer has a softmax activation
... Incorrect. Softmax is not part of RBF networks.
d) Because the kernel matrix $K$ is positive definite
... Incorrect. Positive definiteness affects uniqueness, not range of outputs.


Title: concept-check – remember – edge – Partition of unity
Points: 1
1. Which of the following best describes why normalized RBFs produce stable, bounded predictions?
a) Their values are all equal for any given input
... Incorrect. Kernel values differ by distance.
*b) Their values are non-negative and sum to 1 for any input
... Correct. This defines a partition of unity. This term was clarified in lecture notes and Canvas; it's used to describe the behavior of normalized kernels.
c) They are orthogonal in feature space
... Incorrect. Orthogonality is unrelated.
d) They cover all directions in the input space
... Incorrect. This describes basis completeness, not normalization.


Title: medium – understand – non-edge – Role of bandwidth in Gaussian RBFs
Points: 1
1. How does increasing the bandwidth (σ) in a Gaussian RBF affect the model?
a) It makes the basis functions more peaked and localized
... Incorrect. Larger σ makes them wider and smoother.
*b) It causes each basis function to respond to a wider neighborhood of inputs
... Correct. Higher σ broadens the influence of each center.
c) It removes the need for normalization
... Incorrect. Bandwidth and normalization are orthogonal.
d) It reduces the model to a nearest-neighbor predictor
... Incorrect. That would occur with very small σ, not large.


Title: medium – understand – edge – Exact interpolation with RBFs
Points: 1
1. What is a drawback of using one RBF centered at each training point without regularization?
a) The model cannot fit nonlinear functions
... Incorrect. It can model nonlinearities.
*b) The model will interpolate the training data and overfit noisy observations
... Correct. Exact interpolation leads to poor generalization with noisy data.
c) The model will ignore distant training points completely
... Incorrect. Gaussian RBFs decay but do not ignore.
d) The model cannot be trained using least squares
... Incorrect. Least squares is still applicable.


Title: hard – analyze – edge – Interpolation vs. generalization
Points: 1
1. Which situation best illustrates the tradeoff between interpolation and generalization in RBF networks?
*a) A model trained with many centers achieves zero training error but performs poorly on test data
... Correct. This is classic overfitting from interpolation.
b) A model with few centers interpolates the training set exactly
... Incorrect. Few centers usually mean underfitting, not perfect interpolation.
c) A model with high training and test error due to regularization
... Incorrect. High error on both implies underfitting, not an interpolation tradeoff.
d) A model using random Fourier features to approximate kernels
... Incorrect. This is an unrelated kernel approximation method.


Title: medium – understand – non-edge – Why not center RBFs on all points?
Points: 1
1. Why is it often undesirable to use one RBF center per training point in practice?
a) It leads to underfitting due to lack of expressiveness
... Incorrect. More centers increase, not limit, expressiveness.
*b) It becomes computationally expensive at prediction time
... Correct. Each prediction must sum over all basis functions.
c) It increases training error due to overfitting
... Incorrect. Overfitting increases test error, not training error.
d) It prevents the use of Gaussian kernels
... Incorrect. Kernel type is unrelated to center count.


Title: hard – analyze – edge – Reducing prediction cost in RBF networks
Points: 1
1. Which strategy most directly reduces the computational cost of making predictions with an RBF network?
a) Switching from Gaussian to polynomial radial basis functions
... Incorrect. This changes the shape but not the number of evaluations.
*b) Reducing the number of RBF centers using clustering or greedy selection
... Correct. Fewer centers means fewer basis function evaluations at test time.
c) Replacing the RBF layer with a linear layer followed by ReLU
... Incorrect. That would change the model class entirely.
d) Increasing the number of training points to improve generalization
... Incorrect. More data increases cost, not reduces it.


Title: medium – apply – non-edge – Choosing centers for RBFs
Points: 1
1. Why might one choose to place RBF centers using K-means clustering rather than randomly?
a) It guarantees optimal generalization performance
... Incorrect. No such guarantee is provided.
*b) It summarizes the input distribution by covering high-density regions more efficiently
... Correct. Clustering places centers where data is denser.
c) It ensures all training examples are exactly interpolated
... Incorrect. That would require one center per training point.
d) It simplifies the loss function to a closed-form solution
... Incorrect. The loss function form is not affected by center selection strategy.


Title: medium – apply – edge – OLS center selection
Points: 1
1. What is the main idea behind Orthogonal Least Squares (OLS) for selecting RBF centers?
a) To choose all RBF centers at once based on variance explained
... Incorrect. OLS adds centers one at a time, not all at once.
*b) To incrementally add centers that most reduce residual training error
... Correct. OLS is a greedy, stepwise method that prioritizes error reduction.
c) To perform orthogonalization of all input dimensions before training
... Incorrect. OLS works on basis functions, not input features.
d) To sample from a distribution over all possible RBF center placements
... Incorrect. OLS is deterministic and greedy, not stochastic.


Title: medium – understand – non-edge – Locality of RBFs
Points: 1
1. Why are RBF networks considered “local” models?
a) Because they use a separate model for each input region
... Incorrect. That describes mixture-of-experts models, not RBFs.
*b) Because each basis function responds most strongly to nearby inputs and decays with distance
... Correct. RBFs have localized support centered around specific points.
c) Because they divide the input space into non-overlapping Voronoi cells
... Incorrect. That describes nearest-neighbor or K-means quantization.
d) Because they learn separate weights for every input dimension
... Incorrect. Weight sharing is not dimension-specific in RBFs.


Title: hard – analyze – edge – RBF network vs. kernel method
Points: 1
1. How does an RBF network differ from a standard kernel method?
a) RBF networks do not use kernel functions to compute input similarities
... Incorrect. RBFs are defined via kernels like Gaussians.
*b) RBF networks explicitly learn weights on basis functions, rather than relying solely on similarities to training data
... Correct. Kernel methods compute predictions via kernel-weighted sums over training data; RBFs learn a parametric combination of fixed basis functions.
c) Kernel methods require gradient descent while RBF networks do not
... Incorrect. Both can be trained using least squares or other optimization.
d) Kernel methods use radial basis functions, but RBF networks do not
... Incorrect. That reverses the naming — RBF networks are defined by their use of radial functions.


Title: hard – analyze – edge – Nadaraya–Watson vs. RBF networks
Points: 1
1. Which of the following best distinguishes the Nadaraya–Watson model from a standard RBF network?
a) Nadaraya–Watson requires training weights, while RBF networks use kernel averages
... Incorrect. This reverses the roles — NW uses fixed averages; RBFs train weights.
*b) Nadaraya–Watson computes predictions as normalized kernel-weighted averages without learning parameters
... Correct. NW is nonparametric; RBF networks learn a weight vector.
c) RBF networks cannot be implemented using kernel functions
... Incorrect. RBFs are typically defined using radial kernels.
d) Nadaraya–Watson assumes inputs lie on a regular grid
... Incorrect. Grid placement is unrelated to NW.
