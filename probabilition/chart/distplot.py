import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st

data=st.norm(0,1).rvs(100)
plt.figure(figsize=(10, 6),dpi=100, facecolor='w', edgecolor='black')

plt.subplot(1, 2, 1)
sns.distplot(data, hist=False, kde=True, color='red')
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")


plt.subplot(1, 2, 2)
sns.histplot(data, color='blue')
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
