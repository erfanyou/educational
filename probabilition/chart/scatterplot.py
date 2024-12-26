<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x=np.random.random(100)
y=x**2*np.random.random(100)

size=np.arange(100)

plt.figure(dpi=100)
sns.scatterplot(x=x, y=y,color='purple',size=size,alpha=0.5)
plt.title('Scatterplot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

=======
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x=np.random.random(100)
y=x**2*np.random.random(100)

size=np.arange(100)

plt.figure(dpi=100)
sns.scatterplot(x=x, y=y,color='purple',size=size,alpha=0.5)
plt.title('Scatterplot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

>>>>>>> 462e300dbcb4cf0751f6b76a297dabc18c342638
plt.show()