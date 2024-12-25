import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.figure(figsize=(10, 6), dpi=100 , facecolor = 'w')

plt.subplot(1, 2, 1)
sns.barplot(x=x, y=y,orient="v",palette="Blues_d")

plt.subplot(2, 2, 2)
sns.barplot(x=x, y=y,orient="h",palette="Reds_d")

plt.tight_layout()
plt.show()