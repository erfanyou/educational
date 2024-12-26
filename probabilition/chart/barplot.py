<<<<<<< HEAD
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
=======
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
>>>>>>> 462e300dbcb4cf0751f6b76a297dabc18c342638
plt.show()