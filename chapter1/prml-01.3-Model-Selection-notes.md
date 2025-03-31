# Lecture Notes: PRML Chapter 1.3 – Model Selection

## Key Terminology

- **Overfitting**: When a model is too complex relative to the data, fitting noise instead of signal.
- **Underfitting**: When a model is too simple to capture underlying structure.
- **Training error**: Error computed on the data used to fit the model.
- **Test error**: Error on unseen data; used to assess generalization.
- **Validation set**: A hold-out subset used during training to evaluate generalization performance.
- **Test set**: A final evaluation set used only after model selection to assess unbiased generalization.
- **Regularization**: Penalizing model complexity to reduce overfitting.
- **Occam's razor**: The principle that, all else equal, simpler models are preferred.
- **Akaike Information Criterion (AIC)**: A penalized likelihood criterion balancing fit and complexity.
- **Cross-validation**: A method for evaluating model performance by repeatedly training and validating on different data splits.
- **Leave-one-out cross-validation (LOOCV)**: A special case of cross-validation where each data point is used once as a validation example. It has high computational cost but low bias.

---

## Key Ideas

- **Training error always decreases with complexity**, but **test error follows a U-shape**: it first decreases, then increases as overfitting sets in.
- **Model selection** balances the trade-off between complexity and generalization.
- **Validation sets** are essential for estimating test error during model development.
- **Test sets** are held out until after model selection to provide an unbiased final assessment.
- **AIC** provides a formal mechanism to trade off training fit and model complexity, based on maximum likelihood:
  $$
  \mathrm{AIC} = -2 \ln \mathcal{L}_{\text{max}} + 2k
  $$
  where $\mathcal{L}_{\text{max}}$ is the maximum likelihood of the model given the training data, and $k$ is the number of parameters.

- **Regularization** helps reduce overfitting by penalizing large parameters (e.g., weight decay).
- **Cross-validation**, especially useful with small data sets, reduces variance in model selection by averaging over multiple train/validation splits.
- **Leave-one-out cross-validation** is a low-bias, high-cost special case where each data point serves once as validation.
- **Occam’s Razor** is a guiding principle: prefer the simplest model that fits the data well.

---

## Important Visuals (from text)

- **Figure 1.4**: Shows training vs test error curves as polynomial model complexity increases.
- **Figure 1.3**: Demonstrates polynomial curve fitting with varying degrees (underfit, good fit, overfit).
