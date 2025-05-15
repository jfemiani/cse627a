Quiz title: 07.1 – Support Vector Machines  
Quiz description: This quiz tests understanding of key concepts from Section 7.1 of PRML, including maximum margin classifiers, hinge loss, kernelization, sparsity, and SVM extensions such as regression and one-class SVMs.  
shuffle answers: true  
show correct answers: false


Title: medium – understand – non-edge – Why margin can be fixed to 1  
Points: 1  
1. Why is it valid to impose the constraint $t_n(w^\top \phi(x_n) + b) \ge 1$ when formulating the SVM optimization problem?  
a) Because all training points are scaled to have unit norm, so this margin condition holds by construction  
... Incorrect. No such normalization of inputs is assumed or required in the SVM formulation.  
*b) Because the margin is defined in a scaled space; fixing the margin and shrinking the scale, or fixing the scale and increasing the margin, are equivalent  
... Correct. The optimization is scale-invariant, so we can fix the margin arbitrarily without changing the decision boundary.  
c) Because the kernel function enforces unit distance between support vectors and the separating hyperplane  
... Incorrect. The kernel computes similarity; it does not enforce specific distances or margins.  
d) Because the constraint ensures that the hinge loss will be exactly zero for correctly classified points  
... Incorrect. The hinge loss becomes zero beyond the margin, but the margin value itself is a modeling choice, not a loss property.  


Title: medium – understand – non-edge – Why only support vectors matter  
Points: 1  
1. Why do only support vectors appear in the SVM prediction function?  
a) Because they are closest to the decision boundary and define the margin directly  
... Incorrect. That’s true descriptively, but not the reason they contribute in the formula.  
*b) Because only training points with nonzero weights ($a_n > 0$) matter in the final model, and those are the support vectors  
... Correct. All other points have $a_n = 0$ and do not contribute to prediction.  
c) Because the kernel evaluates to zero for points far from the decision boundary  
... Incorrect. Kernel values are unrelated to margin or sparsity, especially if they are multiplied by $a_n=0$!  
d) Because prediction confidence is used to filter non-support vectors during optimization  
... Incorrect. SVMs do not remove points based on prediction confidence.  


Title: medium – apply – edge – Interpreting $\xi_n > 1$ in soft-margin SVM  
Points: 1  
1. In a soft-margin SVM, what does it mean if a slack variable $\xi_n$ exceeds 1 for a training point?  
a) The point lies exactly on the margin but does not violate the constraint  
... Incorrect. Margin boundary corresponds to $\xi_n = 0$ for support vectors; $\xi_n > 0$ means a violation.  
*b) The point is misclassified and lies on the wrong side of the decision boundary  
... Correct. $\xi_n > 1$ implies $t_n y_n < 0$, meaning the classifier got it wrong.  
c) The point lies just inside the margin but is still correctly classified  
... Incorrect. That would correspond to $0 < \xi_n \le 1$.  
d) The point is ignored during optimization because it violates the margin  
... Incorrect. Violating the margin increases the loss — it does not remove the point.  


Title: hard – analyze – edge – Why soft-margin SVMs produce sparse solutions  
Points: 1  
1. Why does a soft-margin SVM often produce a sparse solution, where many dual variables $a_n$ are zero?  
a) Because the optimizer selects only the $k$ points with the highest classification uncertainty  
... Incorrect. SVMs don’t explicitly select a fixed number of points — sparsity emerges from the loss structure.  
*b) Because points correctly classified with margin incur zero hinge loss, and assigning $a_n > 0$ to them would increase the regularization penalty without reducing loss  
... Correct. The flat region in the hinge loss and the $\|w\|^2$ penalty together encourage zero weights for non-critical points.  
c) Because the kernel function penalizes redundant contributions from similar training points  
... Incorrect. The kernel defines similarity but doesn’t directly induce sparsity.  
d) Because the constraint $\sum_n a_n t_n = 0$ forces most $a_n$ to be zero  
... Incorrect. That constraint ensures balance but doesn’t by itself cause sparsity.  


Title: concept-check – understand – non-edge – Horizontal axis of hinge loss  
Points: 1  
1. In a graph of the hinge loss function used in soft-margin SVMs, what quantity is plotted on the horizontal axis?  
a) The distance from the input $x_n$ to the decision boundary in input space  
... Incorrect. The hinge loss is not based on input-space distances.  
*b) The product of the true label and the model output, $t_n y_n$  
... Correct. This signed value measures margin confidence — it determines when loss is zero or positive.  
c) The squared norm of the weight vector, $\|w\|^2$  
... Incorrect. That appears in the regularization term, not the loss axis.  
d) The kernel similarity between the input and a support vector  
... Incorrect. Kernel values aren't plotted on the hinge loss curve.  


Title: concept-check – remember – non-edge – Zero region of hinge loss  
Points: 1  
1. For which values of $t_n y_n$ does the hinge loss become exactly zero?  
a) Whenever $y_n > 0$  
... Incorrect. That’s not sufficient — the prediction must also be confident and correct.  
*b) When $t_n y_n \ge 1$  
... Correct. The hinge loss is zero when the prediction is correct and the margin is at least 1.  
c) Only if $t_n y_n = 0$  
... Incorrect. That value gives maximal loss — not zero.  
d) For all correctly classified training points  
... Incorrect. Only those classified correctly with a margin of at least 1 have zero loss.  


Title: medium – analyze – edge – Comparing hinge loss to squared error  
Points: 1  
1. Compared to squared error loss, what is a key advantage of hinge loss for classification tasks?  
a) It penalizes large-margin predictions more strongly, improving generalization  
... Incorrect. Hinge loss ignores large-margin predictions, which is the opposite  
*b) It penalizes only points near or within the margin, leading to sparser solutions  
... Correct. This selective penalty reduces unnecessary weight updates  
c) It ensures the model is probabilistic and outputs calibrated confidence  
... Incorrect. Hinge loss does not produce probability estimates  
d) It converges faster because it uses second-order derivatives  
... Incorrect. Hinge loss is non-smooth; second-order optimization is harder, not easier  


Title: medium – apply – non-edge – Support vector condition from hinge loss  
Points: 1  
1. What condition determines whether a training point becomes a support vector in a soft-margin SVM?  
a) The point must be misclassified by the current model  
... Incorrect. Even correctly classified points can be support vectors if they lie on the margin  
*b) The point must have nonzero hinge loss, or lie exactly on the margin boundary  
... Correct. These points correspond to $0 < t_n y_n \le 1$ and yield $a_n > 0$  
c) The point must have a dual variable equal to C  
... Incorrect. That only happens for misclassified or heavily penalized points  
d) The point must have highest kernel similarity to the decision boundary  
... Incorrect. Kernel similarity does not determine support vector status  


Title: medium – apply – non-edge – Kernel in the SVM prediction function  
Points: 1  
1. In the dual form of the SVM, how is the prediction $y(x)$ computed for a test input?  
a) By applying the kernel function between $x$ and all training points, then summing the results with their targets and weights  
... Incorrect. Only support vectors are used in the summation — not all training points.  
*b) By summing over support vectors: $y(x) = \sum_{n \in S} a_n t_n k(x, x_n) + b$  
... Correct. The kernel computes similarity between $x$ and each support vector, weighted by $a_n t_n$.  
c) By projecting $x$ onto the weight vector $w$ learned in the primal  
... Incorrect. The primal form uses $w$, but in the dual, $w$ is never explicitly formed.  
d) By selecting the training point most similar to $x$ and copying its label  
... Incorrect. That’s nearest-neighbor classification, not SVM.  


Title: medium – understand – non-edge – Effect of $C$ in soft-margin SVM  
Points: 1  
1. In a soft-margin SVM, what happens when you increase the value of $C$?  
a) The margin becomes wider to reduce the influence of noisy points  
... Incorrect. A larger $C$ makes the model focus more on minimizing errors, not on margin width.  
*b) The model allows fewer margin violations and may overfit the training data  
... Correct. A larger $C$ increases the penalty for mistakes, so the model fits the data more tightly.  
c) More points are forced to lie exactly on the margin boundary  
... Incorrect. This depends on the data and doesn't follow directly from $C$.  
d) The model becomes less sensitive to outliers in the training set  
... Incorrect. Larger $C$ makes the model **more** sensitive to outliers, not less.  


Title: medium – understand – non-edge – Why maximize the margin  
Points: 1  
1. Why does an SVM choose the separating hyperplane that maximizes the margin between classes?  
a) To ensure the smallest possible training error on the dataset  
... Incorrect. Margin maximization doesn’t guarantee zero training error, especially in soft-margin SVMs.  
*b) To improve generalization by reducing sensitivity to small changes in input data  
... Correct. A wider margin creates a buffer zone, making the classifier more robust to new data.  
c) To reduce the number of support vectors needed for classification  
... Incorrect. The number of support vectors depends on the data, not on a goal of minimization.  
d) Because kernel methods require the margin to be fixed before training  
... Incorrect. The kernel does not depend on margin width — margin arises from optimization.  


Title: medium – understand – edge – Interpreting VC dimension  
Points: 1  
1. What does the VC dimension of a classifier measure?  
a) The number of training errors the model makes during optimization  
... Incorrect. VC dimension is about capacity, not training performance.  
*b) The largest number of points for which the classifier can represent all possible binary labelings correctly  
... Correct. This is the definition of VC dimension: the maximum number of points that can be shattered by the model.  
c) The number of support vectors used in the final prediction function  
... Incorrect. Support vector count varies with data and optimization — not model capacity.  
d) The maximum size of the feature space used by the kernel  
... Incorrect. A model can have an infinite feature space and still low VC dimension depending on the margin.  


Title: medium – understand – non-edge – Margin and model complexity  
Points: 1  
1. Why does the SVM choose the hyperplane with the largest margin among all that separate the data?  
a) Because it minimizes the training error on the support vectors  
... Incorrect. All separating hyperplanes have zero training error in the hard-margin case.  
*b) Because it selects the lowest-capacity (simplest) classifier that still fits the training data  
... Correct. A wider margin corresponds to a simpler model, which improves generalization.  
c) Because the kernel function requires a fixed margin size to operate correctly  
... Incorrect. Kernels apply regardless of margin width.  
d) Because it minimizes the number of features needed in the decision function  
... Incorrect. The number of features is fixed — margin width doesn’t reduce dimensionality.  


Title: medium – analyze – edge – SVM vs. logistic regression  
Points: 1  
1. How does the SVM differ from logistic regression in how it treats well-classified points?  
a) Logistic regression ignores these points, while SVM penalizes them to improve margin  
... Incorrect. Logistic regression continues to adjust weights for all points; SVM ignores well-classified ones beyond the margin.  
*b) SVM ignores well-classified points beyond the margin, while logistic regression continues to adjust for them  
... Correct. The hinge loss becomes flat past the margin, leading to sparsity; logistic loss keeps contributing.  
c) SVM uses probabilistic outputs, while logistic regression does not  
... Incorrect. Logistic regression is probabilistic; SVM is not.  
d) Logistic regression enforces a hard margin; SVM allows soft violations  
... Incorrect. SVM can have hard or soft margins; logistic regression has no explicit margin at all.  


Title: medium – understand – non-edge – Kernel-induced decision boundaries  
Points: 1  
1. What role does the kernel function play in shaping the SVM decision boundary?  
a) It guarantees that the decision boundary remains linear in input space  
... Incorrect. The boundary becomes nonlinear in input space when kernels are used.  
*b) It allows a linear separation in a transformed feature space, resulting in a nonlinear boundary in input space  
... Correct. The kernel implicitly computes dot products in a high-dimensional space, enabling nonlinear separation.  
c) It adds noise to the decision function to prevent overfitting  
... Incorrect. Kernels reshape similarity; they don’t introduce noise.  
d) It removes the need for support vectors by embedding all data into a lower-dimensional subspace  
... Incorrect. Kernels typically **increase**, not decrease, dimensionality, and support vectors are still needed.  


Title: medium – analyze – edge – RBF vs. polynomial kernel  
Points: 1  
1. How does using an RBF kernel differ from using a polynomial kernel in an SVM?  
a) The RBF kernel produces linear boundaries in input space, while the polynomial kernel does not  
... Incorrect. Both kernels typically yield nonlinear decision boundaries in input space.  
*b) The RBF kernel gives localized similarity around training points, while the polynomial kernel captures global interactions  
... Correct. RBFs decay with distance; polynomial kernels encode broader structural relationships.  
c) The polynomial kernel is always preferred because it avoids overfitting  
... Incorrect. No kernel is universally preferred; overfitting depends on data and hyperparameters.  
d) RBF kernels are only valid for inputs in two dimensions  
... Incorrect. RBFs are valid in any input dimension.  


Title: medium – understand – non-edge – Kernel validity criteria  
Points: 1  
1. What must be true for a function $k(x, x')$ to be a valid kernel in an SVM?  
a) It must be normalized so that $k(x, x) = 1$ for all $x$  
... Incorrect. Kernels need not be normalized — only symmetric and positive semi-definite.  
*b) It must be symmetric and generate a positive semi-definite Gram matrix for all input sets  
... Correct. This ensures the kernel corresponds to an inner product in some feature space.  
c) It must compute Euclidean distance between inputs  
... Incorrect. Distance is not required — similarity is encoded via inner products.  
d) It must output values between 0 and 1 for all inputs  
... Incorrect. Kernel values can be negative or unbounded, depending on the function.  



Title: medium – understand – non-edge – Support vectors and model complexity  
Points: 1  
1. What does a large number of support vectors typically indicate about an SVM model?  
a) That the margin is unusually wide and generalization is excellent  
... Incorrect. More support vectors usually occur with smaller margins.  
*b) That the decision boundary is highly sensitive to the training data  
... Correct. Many support vectors suggest the model fits closely to the data and may overfit.  
c) That the model is underfitting and not learning patterns  
... Incorrect. Underfitting would likely lead to fewer support vectors and larger errors.  
d) That the kernel function is not symmetric  
... Incorrect. Kernel symmetry is unrelated to the number of support vectors.  



Title: medium – understand – edge – Extending SVMs to multiclass problems  
Points: 1  
1. Which of the following best describes a common strategy for applying binary SVMs to multiclass classification tasks?  
a) Train a single SVM using one large kernel matrix shared across all classes  
... Incorrect. Standard SVMs are binary and don’t support multiclass training in one model without extensions.  
*b) Train one binary SVM for each class against all others, then choose the class with the highest output score  
... Correct. This is the "one-vs-rest" approach — a common method for multiclass SVMs.  
c) Use a softmax layer on top of the dual coefficients to normalize predictions across classes  
... Incorrect. Softmax is from probabilistic models like logistic regression, not used in SVMs.  
d) Assign each support vector a class label and average their labels using kernel-weighted voting  
... Incorrect. SVMs predict by thresholding the sign of a score — they don’t average class labels.  



Title: concept-check – remember – non-edge – SVM classifier type  
Points: 1  
1. How is a standard SVM best categorized in terms of model type?  
a) A generative model that estimates $p(x, t)$ and samples new data  
... Incorrect. SVMs do not model the joint distribution or generate data.  
*b) A discriminative model that defines a decision boundary without modeling probabilities  
... Correct. SVMs directly define decision boundaries through margin maximization.  
c) A probabilistic classifier that estimates posterior class probabilities  
... Incorrect. Standard SVMs produce scores, not calibrated probabilities.  
d) A hierarchical model trained by maximizing likelihood over a latent space  
... Incorrect. That describes models like EM for GMMs or deep generative models.  



Title: medium – understand – edge – Idea behind SVM regression  
Points: 1  
1. What is the key idea behind SVM regression (support vector regression)?  
a) To assign each output to a discrete bin based on support vector similarity  
... Incorrect. SVR performs continuous regression, not classification into bins.  
*b) To fit the simplest function that stays within an $\epsilon$-margin of the target values, even if it underfits the trend  
... Correct. SVR minimizes complexity and tolerates deviations inside the $\epsilon$-tube.  
c) To minimize squared error while ensuring that predictions remain maximally separated  
... Incorrect. SVR does not use squared error and does not seek maximal separation in regression.  
d) To learn a probability distribution over outputs using a likelihood-based loss function  
... Incorrect. SVR is not probabilistic and does not model distributions over outputs.  


Title: medium – understand – non-edge – Purpose of one-class SVM  
Points: 1  
1. What is the main purpose of a one-class SVM?  
a) To assign each input to one of several mutually exclusive classes  
... Incorrect. That describes multiclass classification, not one-class SVM.  
*b) To find a simple boundary that encloses most of the data and treats distant points as anomalies  
... Correct. One-class SVM separates mapped inputs from the origin in feature space — it does not model density.  
c) To reduce the number of support vectors required for binary classification  
... Incorrect. One-class SVMs are not designed for model compression or binary tasks.  
d) To estimate the likelihood of each input under a Gaussian kernel density model  
... Incorrect. One-class SVMs are not probabilistic and do not compute likelihoods.  


Title: medium – understand – edge – Margin location relative to class boundaries  
Points: 1  
1. In a linear SVM trained with a hard margin, where does the decision boundary lie relative to the training data?  
a) It passes through the positive class and avoids the negative class using slack variables  
... Incorrect. Hard-margin SVMs use no slack; the boundary does not pass through any data points.  
*b) It is equidistant from the nearest points of each class and maximizes the gap between them  
... Correct. The margin is symmetric between the closest oppositely labeled points.  
c) It is positioned to ensure an equal number of misclassifications from each class  
... Incorrect. Hard-margin SVMs make no misclassifications — they separate the data completely.  
d) It aligns with the direction of the largest principal component in the input space  
... Incorrect. SVMs optimize for margin, not variance like PCA does.  


Title: hard – analyze – edge – Diagnosing excessive support vector count  
Points: 1  
1. A linear SVM trained on 10,000 points results in 9,800 support vectors. What is the most likely cause, and how might you address it?  
a) The regularization term is too strong; you should increase $C$ to simplify the model  
... Incorrect. Increasing $C$ reduces regularization, often worsening overfitting.  
*b) The model overfits the training data; you should reduce $C$ or consider a feature selection step  
... Correct. Too many support vectors suggest a narrow margin — reducing $C$ or simplifying features can improve generalization.  
c) The kernel trick is disabled; you should switch to an RBF kernel to enforce sparsity  
... Incorrect. Kernel choice affects flexibility, but doesn’t guarantee fewer support vectors.  
d) The optimization algorithm failed; retraining with the same settings should fix the issue  
... Incorrect. Retraining won’t solve structural overfitting — a design change is needed.  



Title: medium – analyze – edge – Handling noisy or overlapping classes  
Points: 1  
1. You train a hard-margin SVM on data with overlapping classes and find high training error. What’s the appropriate adjustment?  
a) Reduce $C$ to allow the model to ignore training points far from the margin  
... Incorrect. Hard-margin SVM doesn’t use $C$ — and reducing $C$ in soft-margin SVM increases tolerance, not margin sharpness.  
*b) Switch to a soft-margin SVM and choose $C$ to balance margin width and error tolerance  
... Correct. When data is not linearly separable, soft margins allow better tradeoff between fit and complexity.  
c) Normalize the support vectors to improve decision boundary location  
... Incorrect. You can’t normalize support vectors — they're learned.  
d) Switch to one-class SVM to capture uncertainty in the input distribution  
... Incorrect. One-class SVM is for outlier detection, not binary classification.  



Title: medium – analyze – edge – Tuning kernel flexibility  
Points: 1  
1. Your SVM with an RBF kernel shows perfect training accuracy but poor test performance. What’s the likely cause, and what could you do?  
a) The margin is too wide; reduce $C$ to increase training focus  
... Incorrect. Reducing $C$ increases margin softness — it won’t help if you're already overfitting.  
*b) The kernel bandwidth is too small; increase it to reduce model sensitivity to individual points  
... Correct. A small RBF bandwidth makes the model behave like nearest neighbors — increasing it smooths the boundary.  
c) The data isn't normalized; normalize the kernel outputs to prevent bias  
... Incorrect. Normalizing kernel outputs doesn’t fix overfitting — the kernel width matters more.  
d) The decision function is not probabilistic; add Platt scaling to calibrate predictions  
... Incorrect. Calibration may help probabilities, but not overfitting of the boundary.  


Title: medium – analyze – edge – Overfitting from kernel degree  
Points: 1  
1. After switching from a linear kernel to a 5th-degree polynomial kernel, your SVM's training accuracy improves but test error worsens. What’s the most likely cause, and what should you do?  
a) The kernel is too weak; increase the degree further to improve generalization  
... Incorrect. A higher-degree polynomial increases model complexity and overfitting risk.  
*b) The kernel is too flexible; reduce its degree or consider returning to a linear kernel  
... Correct. High-degree polynomials can overfit by warping the decision boundary excessively.  
c) The regularization is too strong; increase $C$ to reduce test error  
... Incorrect. Increasing $C$ may further overfit the high-capacity kernel.  
d) The input features are too high-dimensional; apply PCA first to reduce dimensionality  
... Incorrect. Dimensionality isn't the issue here — the kernel's expressiveness is.  



Title: medium – analyze – edge – Biased predictions and class imbalance  
Points: 1  
1. You train a binary SVM and observe that it predicts the majority class on nearly all test inputs. What’s the most likely cause, and what could help address it?  
a) The SVM loss penalizes misclassifications too symmetrically; you should retrain using a kernel with stronger curvature  
... Incorrect. Kernel curvature affects boundary shape, not class bias.  
*b) The SVM objective does not account for class imbalance; you could adjust the prediction threshold or, more robustly, use a weighted SVM  
... Correct. Standard SVMs optimize margin, not class balance — both thresholding and class-weighted training are valid responses.  
c) The support vectors are overfit to the majority class; remove them and retrain  
... Incorrect. Support vectors are learned — removing them breaks the model entirely.  
d) The regularization parameter $C$ is too large; reducing it ensures more margin violations from the majority class  
... Incorrect. Changing $C$ affects margin softness, not class balance.  
