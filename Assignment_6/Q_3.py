import numpy as np
import matplotlib.pyplot as plt

np.random.seed(102317160)
data = np.random.randn(50)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].plot(np.cumsum(data), marker='o', linestyle='-', color='b')
axes[0].set_title("Cumulative Sum Line Plot")
axes[0].set_xlabel("Index")
axes[0].set_ylabel("Cumulative Sum")
axes[0].grid(True)

axes[1].scatter(range(50), data, color='r', alpha=0.6)
axes[1].set_title("Scatter Plot with Random Noise")
axes[1].set_xlabel("Index")
axes[1].set_ylabel("Value")
axes[1].grid(True)

fig.tight_layout()
plt.show()
