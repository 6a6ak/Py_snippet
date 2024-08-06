import numpy as np
import matplotlib.pyplot as plt

# Sample
np.random.seed(0)
x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.1, 100)

# Corralation 
correlation = np.corrcoef(x, y)[0, 1]
print("Correlation:", correlation)

# Plot
plt.scatter(x, y)
plt.title("Correlation x و y")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
