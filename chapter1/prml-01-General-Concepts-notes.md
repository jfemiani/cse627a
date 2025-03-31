# General Concepts

## Learning Paradigms

- **Supervised Learning**  
  Learns a mapping from inputs $x$ to outputs $y$ using labeled data.  
  - *Examples*: Linear regression, logistic regression, neural networks  
  - *Goal*: Predict labels for new data

- **Unsupervised Learning**  
  Identifies structure in unlabeled data.  
  - *Examples*: Clustering, dimensionality reduction  
  - *Goal*: Discover latent structure or compress data

- **Reinforcement Learning**  
  Optimizes behavior through feedback in the form of rewards from an environment.  
  - *Goal*: Learn a policy that maximizes cumulative reward


## Generative vs. Discriminative Models

- **Discriminative Models**  
  Directly model the conditional distribution $p(y|x)$ — learning the boundary between classes.  
  - *Examples*: Logistic regression, SVM  
  - *Strengths*: Focused on prediction, often better asymptotic performance  
  - *Tradeoff*: May require more labeled data to generalize well

- **Generative Models**  
  Model the joint distribution $p(x, y)$ or $p(x|y)p(y)$, which allows generation of synthetic data.  
  - *Examples*: Naive Bayes, Gaussian mixture models  
  - *Strengths*: Handle missing data, model class priors, enable generation  
  - *Tradeoff*: Often involve more parameters and model aspects unrelated to classification


## Parametric vs. Non-Parametric Models

- **Parametric Models**  
  Have a fixed number of parameters, regardless of the size of the training data.  
  - *Examples*: Linear regression, logistic regression  
  - *Advantages*: Compact representation, fast training  
  - *Limitations*: Limited flexibility; may underfit complex patterns

- **Non-Parametric Models**  
  The complexity grows with data — the model structure adapts.  
  - *Examples*: Decision trees, k-nearest neighbors  
  - *Advantages*: High flexibility; can capture complex patterns  
  - *Limitations*: May overfit or be computationally intensive

 

## Model-Task Alignment

| Task                            | Paradigm           | Example Model              |
|----------------------------------|---------------------|----------------------------|
| Handwritten digit classification | Supervised          | Logistic regression        |
| Document clustering              | Unsupervised        | k-means                    |
| Movie recommendation             | Hybrid/Unsupervised | Matrix factorization       |
| Speech recognition               | Supervised          | Neural networks            |
| Market trend prediction          | Supervised          | Decision trees, SVM        |

 

## Learning Outcomes

After reviewing this module, you should be able to:

- Distinguish between supervised, unsupervised, and reinforcement learning based on data and objectives  
- Identify whether a model is generative or discriminative, and explain the practical implications  
- Classify models as parametric or non-parametric, and discuss the tradeoffs  
- Match common tasks with appropriate learning paradigms and model types  
- Recognize when modeling more of the data (generative) may be unnecessary or costly for predictive tasks
