<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as st

data_1=np.random.randn(100)

plt.figure(dpi=100,figsize=(10,6))

plt.subplot(1, 2, 1)
sns.boxplot(data_1,color='purple',orient='h')
plt.title('Boxplot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

healthy =['healthy'if np.random.rand()>0.5 else 'sick' for _ in range(100)]
data_2=st.norm(0,1).rvs(100)

plt.subplot(1, 2, 2)
sns.boxplot(x=healthy,y=data_2,color='green',palette='Blues_d')
plt.title('Boxenplot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

=======
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as st

data_1=np.random.randn(100)

plt.figure(dpi=100,figsize=(10,6))

plt.subplot(1, 2, 1)
sns.boxplot(data_1,color='purple',orient='h')
plt.title('Boxplot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

healthy =['healthy'if np.random.rand()>0.5 else 'sick' for _ in range(100)]
data_2=st.norm(0,1).rvs(100)

plt.subplot(1, 2, 2)
sns.boxplot(x=healthy,y=data_2,color='green',palette='Blues_d')
plt.title('Boxenplot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

>>>>>>> 462e300dbcb4cf0751f6b76a297dabc18c342638
plt.show()