import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x)*(1-sigmoid(x))

a = np.linspace(-10, 10, 1000)
sig = sigmoid(a)
sig_prime = sigmoid_derivative(a)
one_minus_sig = 1 - sig

plt.plot(a, sig, label='Sigmoid')
plt.plot(a, sig_prime, label='Sigmoid Derivative')
plt.plot(a, one_minus_sig, label='1 - Sigmoid')
plt.xlabel('a')
plt.legend()
plt.show()
