import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.random.uniform(-3, 10, 100)
y = x**2 + np.random.normal(0, 1, 100)

plt.figure(dpi=100, figsize=(15, 6))

sns.jointplot(x=x, y=y, color='purple')
plt.title('Scatter Plot')

plt.tight_layout()
plt.show()

sns.jointplot(x=x, y=y, kind='kde', color='purple')
plt.title('KDE Plot')

plt.tight_layout()
plt.show()
