<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as st

healthy =['healthy'if np.random.rand()>0.6 else 'sick' for _ in range(100)]
data_2=st.norm(0,1).rvs(100)

sns.swarmplot(x=healthy,y=data_2,color='green',palette='Blues_d')
=======
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as st

healthy =['healthy'if np.random.rand()>0.6 else 'sick' for _ in range(100)]
data_2=st.norm(0,1).rvs(100)

sns.swarmplot(x=healthy,y=data_2,color='green',palette='Blues_d')
>>>>>>> 462e300dbcb4cf0751f6b76a297dabc18c342638
plt.show()