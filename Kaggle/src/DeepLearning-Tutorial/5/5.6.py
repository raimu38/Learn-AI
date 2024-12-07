import numpy as np
import matplotlib.pyplot as plt

def tanh_function(x):
    return (np.exp(x)-np.exp(-x))/(np.exp(x) + np.exp(-x))

x = np.linspace(-5,5)
y = tanh_function(x)

plt.plot(x,y)
plt.savefig("result.png")