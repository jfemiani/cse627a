Quiz title: Binary and Multinomial Variables Quiz  
Quiz description: This quiz focuses on fundamental concepts from sections 2.1 and 2.2, including binary variable likelihoods, conjugate priors, and multinomial models. This quiz covers key concepts and background material from sections 2.1 and 2.2. The questions are designed to help you prepare for exercises 2.1–2.12.

1. What is a conjugate prior in Bayesian inference?  
a) A prior unrelated to the likelihood function.  
... Incorrect. A conjugate prior is specifically chosen so that the posterior retains the same functional form as the prior.  
*b) A prior that results in a posterior distribution of the same form.  
... Correct. This is the standard definition of a conjugate prior.  
c) A prior that always increases the likelihood value.  
... Incorrect. The purpose of a conjugate prior is not to increase the likelihood, but to simplify the computation of the posterior.  
d) A prior that gives a flat posterior distribution.  
... Incorrect. A flat (noninformative) prior is not necessarily conjugate.

2. For a binary variable $x \in \{0,1\}$ with success probability $\mu$, which expression correctly represents the likelihood for a single observation?  
a) $p(x|\mu)= \mu$, regardless of $x$.  
... Incorrect. This does not distinguish between the cases $x=0$ and $x=1$.  
*b) $p(x|\mu)= \mu^x (1-\mu)^{1-x}$.  
... Correct. When $x=1$, the expression gives $\mu$, and when $x=0$, it gives $1-\mu$.  
c) $p(x|\mu)= \mu+(1-\mu)$.  
... Incorrect. This sums to 1 regardless of $x$ and does not vary with the observed value.  
d) $p(x|\mu)= x\,\mu\,(1-\mu)^{1-x}$.  
... Incorrect. Multiplying by $x$ incorrectly forces the likelihood to be 0 when $x=0$.

3. Given $N$ independent observations of a binary variable, what is the maximum likelihood estimate for $\mu$?  
*a) The fraction of observations equal to 1.  
... Correct. The MLE for $\mu$ is calculated as the number of successes divided by $N$.  
b) The sum of the observations.  
... Incorrect. While the sum equals the number of 1's, it must be divided by $N$ to obtain the probability estimate.  
c) The ratio of zeros to total observations.  
... Incorrect. This gives $1-\mu$, not $\mu$.  
d) The prior mean of $\mu$.  
... Incorrect. The prior mean is used in Bayesian inference, not in maximum likelihood estimation.

4. Which distribution is commonly used as the conjugate prior for a Bernoulli or binomial likelihood?  
a) Gaussian distribution.  
... Incorrect. Gaussians are not conjugate to the Bernoulli/binomial likelihood.  
b) Gamma distribution.  
... Incorrect. The Gamma distribution is conjugate to the Poisson or exponential likelihood, not the binomial.  
*c) Beta distribution.  
... Correct. The Beta distribution is the standard conjugate prior for Bernoulli and binomial models.  
d) Uniform distribution.  
... Incorrect. Although a uniform prior (Beta(1,1)) is a special case, it is not generally referred to as the conjugate prior.

5. Which expression best represents the Beta distribution density for $\mu$ (ignoring normalization)?  
a) $\mu^{a}(1-\mu)^{b}$  
... Incorrect. The proper exponents are $a-1$ and $b-1$, not $a$ and $b$.  
*b) $\mu^{a-1}(1-\mu)^{b-1}$  
... Correct. This is the functional form of the Beta density (up to the normalizing constant).  
c) $\mu^{a+1}(1-\mu)^{b+1}$  
... Incorrect. The exponents are incorrect by an additive factor.  
d) $\exp(-a\mu-b(1-\mu))$  
... Incorrect. This is not the form of the Beta distribution.

6. In the multinomial model, how is each observation typically represented?  
a) As a scalar taking one value from 1 to $K$.  
... Incorrect. Although the outcome is categorical, it is common to encode it in a one-hot vector for processing.  
*b) As a $K$-dimensional one-hot encoded vector.  
... Correct. This representation has exactly one element equal to 1 (indicating the observed category) and all others equal to 0.  
c) As a probability vector summing to 1.  
... Incorrect. While a probability vector sums to 1, each observation is represented by a one-hot vector, not a probabilistic mixture.  
d) As a binary vector with two ones.  
... Incorrect. A one-hot vector must contain exactly one 1.

7. What is the likelihood function for the multinomial distribution with counts $m_1,\dots,m_K$ and parameters $\mu_1,\dots,\mu_K$?  
a) $\prod_{k=1}^K \mu_k^{m_k}$  
... Incorrect. This expression omits the multinomial coefficient that accounts for the number of arrangements.  
*b) $\displaystyle \frac{N!}{m_1!\cdots m_K!}\prod_{k=1}^K \mu_k^{m_k}$  
... Correct. This is the full likelihood function, including the combinatorial coefficient.  
c) $\sum_{k=1}^K \mu_k^{m_k}$  
... Incorrect. A summation does not correctly represent the joint likelihood across categories.  
d) $\prod_{k=1}^K (m_k\,\mu_k)$  
... Incorrect. Multiplying the counts by the probabilities is not the correct formulation.

8. What constraints must the parameters $\mu_1,\dots,\mu_K$ of a multinomial distribution satisfy?  
a) $\mu_k>0$ for all $k$.  
... Partially correct. They must be positive, but there is an additional constraint.  
b) $\sum_{k=1}^K \mu_k = 1$.  
... Partially correct. They must sum to 1, but each must also be nonnegative.  
*c) Each $\mu_k>0$ and $\sum_{k=1}^K \mu_k = 1$.  
... Correct. Both conditions are required for a valid multinomial probability vector.  
d) They can be any real numbers.  
... Incorrect. The parameters must be nonnegative and sum to 1.

9. Which distribution serves as the conjugate prior for the parameters of a multinomial likelihood?  
a) Beta distribution.  
... Incorrect. The Beta is a two-dimensional case; for multiple categories, the Dirichlet distribution is used.  
*b) Dirichlet distribution.  
... Correct. The Dirichlet distribution generalizes the Beta to multiple dimensions.  
c) Gaussian distribution.  
... Incorrect. Gaussians are not used as conjugate priors for multinomial parameters.  
d) Poisson distribution.  
... Incorrect. The Poisson is unrelated to the multinomial likelihood.

10. In the context of Beta and Dirichlet priors, how are the hyperparameters best interpreted?  
a) As measures of variability in the data.  
... Incorrect. While they influence variability, their primary interpretation is different.  
*b) As pseudo-counts representing effective prior observations.  
... Correct. They act as prior counts, indicating the strength of prior belief.  
c) As arbitrary scaling constants.  
... Incorrect. Their values have a specific interpretation related to prior evidence.  
d) As maximum likelihood estimates.  
... Incorrect. They are set prior to observing the data, not estimated from it.

11. (May help answer Exercise 2.1) Which of the following expressions correctly gives the entropy of a Bernoulli random variable with parameter $\mu$?  
a) $\mu \ln \mu + (1-\mu) \ln (1-\mu)$  
... Incorrect. The entropy formula requires a negative sign to ensure a nonnegative result.  
*b) $-\mu \ln \mu - (1-\mu) \ln (1-\mu)$  
... Correct. This is the standard formula for the entropy of a Bernoulli variable.  
c) $\mu(1-\mu)$  
... Incorrect. This is the variance of a Bernoulli random variable, not its entropy.  
d) $\ln(\mu) - \ln(1-\mu)$  
... Incorrect. This does not correspond to the entropy formula.

12. (May help answer Exercise 2.2) For a binary variable $x \in \{-1,1\}$ with parameter $\mu \in [-1,1]$, which of the following forms is equivalent to its probability mass function?  
a) $p(x|\mu)= \left(\frac{1-\mu}{2}\right)^{\frac{1+x}{2}} \left(\frac{1+\mu}{2}\right)^{\frac{1-x}{2}}$  
... Incorrect. This formulation reverses the roles for $x=1$ and $x=-1$.  
b) $p(x|\mu)= \left(\frac{1+\mu}{2}\right)^{\frac{1-x}{2}} \left(\frac{1-\mu}{2}\right)^{\frac{1+x}{2}}$  
... Incorrect. This also does not correctly match the conventional parameterization.  
*c) $p(x|\mu)= \frac{1}{2}\Bigl(1+\mu\,x\Bigr)$  
... Correct. This is the standard representation for a binary variable on $\{-1,1\}$.  
d) $p(x|\mu)= \frac{1}{2}\Bigl(1-\mu\,x\Bigr)$  
... Incorrect. This would reverse the probabilities for $x=1$ and $x=-1$.

13. (May help answer Exercise 2.3) The binomial theorem states that  
    $$ (1+x)^N = \sum_{m=0}^{N} \binom{N}{m} x^m. $$  
    Which of the following uses this identity to prove that the binomial distribution is normalized?  
a) Applying the law of large numbers.  
... Incorrect. The law of large numbers is not used to show normalization.  
b) Using the combinatorial identity $\binom{N}{m} + \binom{N}{m-1} = \binom{N+1}{m}$.  
... Incorrect. Although true, this identity is not needed for normalization.  
*c) Recognizing that the sum of probabilities $\sum_{m=0}^{N} \binom{N}{m} \mu^m (1-\mu)^{N-m} = (\mu+(1-\mu))^N = 1^N$.  
... Correct. This directly uses the binomial theorem to confirm that the probabilities sum to one.  
d) Differentiating the generating function of the binomial coefficients.  
... Incorrect. Differentiation is unnecessary for demonstrating normalization.

14. (May help answer Exercise 2.4) What is the variance of a binomial distribution with parameters $N$ and $\mu$?  
a) $N\mu$  
... Incorrect. This is the expected value, not the variance.  
b) $\mu(1-\mu)$  
... Incorrect. This is the variance of a single Bernoulli trial; it must be scaled by $N$.  
*c) $N\mu(1-\mu)$  
... Correct. This is the well-known formula for the variance of a binomial distribution.  
d) $N^2\mu(1-\mu)$  
... Incorrect. Over-scaling the variance by an extra factor of $N$.

15. (May help answer Exercise 2.5) Which function is used to express the normalization constant of the Beta distribution?  
a) The exponential function.  
... Incorrect. The exponential function does not appear in the Beta normalization constant.  
*b) The Gamma function.  
... Correct. The Gamma function is used to construct the Beta function, which normalizes the distribution.  
c) The logarithm function.  
... Incorrect. The logarithm is not used in the normalization constant.  
d) The digamma function.  
... Incorrect. The digamma function is the derivative of the logarithm of the Gamma function, not the normalizing function itself.

16. (May help answer Exercise 2.6) What is the mean of a Beta distribution with parameters $a$ and $b$?  
a) $\frac{a-1}{a+b-2}$  
... Incorrect. This expression typically represents the mode (when $a,b>1$), not the mean.  
*b) $\frac{a}{a+b}$  
... Correct. The mean of a Beta distribution is given by $\frac{a}{a+b}$.  
c) $\frac{a+1}{a+b+2}$  
... Incorrect. This is not the standard formula for the mean.  
d) $\frac{b}{a+b}$  
... Incorrect. This would be the mean for $1-\mu$, not $\mu$.

17. (May help answer Exercise 2.6) Assuming $a>1$ and $b>1$, what is the mode of a Beta distribution with parameters $a$ and $b$?  
a) $\frac{a}{a+b}$  
... Incorrect. This is the mean, not the mode.  
b) $\frac{a-1}{a+b}$  
... Incorrect. The denominator should account for both parameters reduced by 1.  
*c) $\frac{a-1}{a+b-2}$  
... Correct. This is the standard formula for the mode of a Beta distribution when $a>1$ and $b>1$.  
d) $\frac{a}{a+b-1}$  
... Incorrect. This does not match the conventional formula for the mode.

18. (May help answer Exercise 2.7) In Bayesian updating for a Bernoulli likelihood with a Beta prior, the posterior mean is a weighted average of which two quantities?  
a) The sample variance and the prior variance.  
... Incorrect. Variances are not combined to yield the posterior mean.  
*b) The prior mean and the maximum likelihood estimate.  
... Correct. The posterior mean is a compromise between the prior mean and the observed data's maximum likelihood estimate.  
c) The prior mode and the sample mean.  
... Incorrect. The mode is not typically used to compute the posterior mean.  
d) The prior variance and the maximum likelihood estimate.  
... Incorrect. Variance is not used in forming a weighted average for the mean.

19. (May help answer Exercise 2.8) Which of the following equations represents the law of total expectation?  
a) $E[x] = E[x|y]$  
... Incorrect. This statement neglects the need to average over the distribution of $y$.  
*b) $E[x] = E_y\bigl[E[x|y]\bigr]$  
... Correct. The overall expectation is the expectation (over $y$) of the conditional expectation of $x$ given $y$.  
c) $E[x] = \operatorname{Var}[x|y] + \bigl(E[x|y]\bigr)^2$  
... Incorrect. This is related to the decomposition of the second moment, not the total expectation.  
d) $E[x] = E[y]$  
... Incorrect. There is no general reason for the expectation of $x$ to equal the expectation of $y$.

20. (May help answer Exercise 2.10) The Dirichlet distribution is a multivariate generalization of which distribution?  
a) Bernoulli distribution.  
... Incorrect. The Dirichlet generalizes the Beta distribution, not the Bernoulli.  
*b) Beta distribution.  
... Correct. The Dirichlet distribution is the multivariate extension of the Beta distribution.  
c) Binomial distribution.  
... Incorrect. The Binomial is a discrete distribution for counts, not the direct generalization here.  
d) Uniform distribution.  
... Incorrect. While a uniform distribution can be seen as a special case, it is not the correct generalization.

21. (May help answer Exercise 2.12) What is the mean of a uniform distribution on the interval $[a,b]$?  
a) $a$  
... Incorrect. This is the lower bound of the interval.  
b) $b$  
... Incorrect. This is the upper bound of the interval.  
*c) $\frac{a+b}{2}$  
... Correct. The mean of a uniform distribution is the midpoint of the interval.  
d) $\frac{b-a}{2}$  
... Incorrect. This expression gives half the length of the interval, not the mean.
