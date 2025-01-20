import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    return np.where(x<= 0, 0, 1)

x = np.linspace(-5, 5)
y = step_function(x)

plt.title("Step_Function")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)
plt.grid(True)

plt.savefig("result.png")
