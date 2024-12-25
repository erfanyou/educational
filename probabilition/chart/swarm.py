import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as st

healthy =['healthy'if np.random.rand()>0.6 else 'sick' for _ in range(100)]
data_2=st.norm(0,1).rvs(100)

sns.swarmplot(x=healthy,y=data_2,color='green',palette='Blues_d')
plt.show()