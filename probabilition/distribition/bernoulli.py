import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
# پارامتر توزیع برنولی
p = 1 / 6  # احتمال موفقیت (آوردن عدد 4)

# مقادیر x برای توزیع برنولی
x = np.array([0, 1])

# محاسبه PMF و CDF
pmf = bernoulli.pmf(x, p)
cdf = bernoulli.cdf(x, p)

# رسم نمودارهای 2 بعدی
plt.figure(figsize=(12, 6))

sns.set(style="whitegrid")

# PMF نمودار
plt.subplot(1, 2, 1)
sns.barplot(x=x, y=pmf, palette="Blues_d", edgecolor='black')
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.xticks(x, ['Failure (Not 4)', 'Success (4)'])
plt.title('Bernoulli PMF for Rolling a Die')

# CDF نمودار
plt.subplot(1, 2, 2)
plt.step(x, cdf, where='post', color='blue', marker='o')
plt.xlabel('Outcome')
plt.ylabel('Cumulative Probability')
plt.xticks([0, 1], ['Failure (Not 4)', 'Success (4)'])
plt.title('Bernoulli CDF for Rolling a Die')

plt.tight_layout()
plt.show()

# رسم نمودار 3 بعدی
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# تبدیل داده‌ها برای رسم
x_3d = np.concatenate([x, x])
pmf_3d = np.concatenate([pmf, np.zeros_like(pmf)])
cdf_3d = np.concatenate([np.zeros_like(cdf), cdf])

# رسم نوارهای 3 بعدی برای PMF و CDF
ax.bar(x_3d, pmf_3d, zs=0, zdir='y', width=0.5, color='cyan', alpha=0.7, label='PMF')
ax.bar(x_3d + 1, cdf_3d, zs=1, zdir='y', width=0.5, color='magenta', alpha=0.7, label='CDF')

# تنظیمات نمودار
ax.set_xlabel('Outcome')
ax.set_ylabel('Type')
ax.set_zlabel('Probability')
ax.set_title('Bernoulli Distribution PMF and CDF in 3D')
ax.set_yticks([0, 1])
ax.set_yticklabels(['PMF', 'CDF'])
ax.legend()
ax.grid(True)

plt.show()
