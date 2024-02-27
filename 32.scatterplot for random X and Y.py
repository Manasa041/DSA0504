import matplotlib.pyplot as plt
import numpy as np

# Generating random data
np.random.seed(0)  # for reproducibility
x = np.random.rand(50)
y = np.random.rand(50)

# Plotting the scatter graph
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', alpha=0.5)  # alpha controls transparency
plt.title('Random Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
