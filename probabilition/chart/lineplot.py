import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x=np.array(['sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri'])
y=np.array([10,7,7,3,5,7,20])

plt.figure(dpi=100)
sns.lineplot(x=x, y=y,color='purple',marker='o',linestyle='--')
plt.title('Lineplot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()