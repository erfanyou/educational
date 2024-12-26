<<<<<<< HEAD
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data= st.norm(4,3).rvs(size=1000)
def ml_mean(x,mean):
    return np.log(st.norm.pdf(x,mean,scale=1)).sum()

def ml_var(x,std,mean):
    return np.log(st.norm.pdf(x,mean,std)).sum()

mean = np.linspace(-10,10,1000)
ml = [ml_mean(data,mean[i]) for i in range(len(mean))]

mean_estimation = mean[ml.index(max(ml))]

plt.figure(figsize=(8, 6))
sns.histplot(data, kde=True, palette='Set1', edgecolor='black')
plt.axvline( mean_estimation, color='red', linestyle='--', label='Mean Estimation')
plt.legend()
plt.show()


std= np.linspace(0.001,11,1000)
ml = [ml_var(data,i,mean_estimation) for i in std]

std_estimation = std[ml.index(max(ml))]

plt.figure(figsize=(8, 6))
sns.histplot(data, kde=True, palette='Set1', edgecolor='black')
plt.axvline( std_estimation, color='red', linestyle='--', label='Std Estimation')
plt.legend()
plt.show()
=======
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data= st.norm(4,3).rvs(size=1000)
def ml_mean(x,mean):
    return np.log(st.norm.pdf(x,mean,scale=1)).sum()

def ml_var(x,std,mean):
    return np.log(st.norm.pdf(x,mean,std)).sum()

mean = np.linspace(-10,10,1000)
ml = [ml_mean(data,mean[i]) for i in range(len(mean))]

mean_estimation = mean[ml.index(max(ml))]

plt.figure(figsize=(8, 6))
sns.histplot(data, kde=True, palette='Set1', edgecolor='black')
plt.axvline( mean_estimation, color='red', linestyle='--', label='Mean Estimation')
plt.legend()
plt.show()


std= np.linspace(0.001,11,1000)
ml = [ml_var(data,i,mean_estimation) for i in std]

std_estimation = std[ml.index(max(ml))]

plt.figure(figsize=(8, 6))
sns.histplot(data, kde=True, palette='Set1', edgecolor='black')
plt.axvline( std_estimation, color='red', linestyle='--', label='Std Estimation')
plt.legend()
plt.show()
>>>>>>> 462e300dbcb4cf0751f6b76a297dabc18c342638
