import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-6, 6.01, 0.01)

plt.plot(x, x * x - x - 6)
plt.show()
