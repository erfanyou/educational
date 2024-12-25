import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt
import seaborn as sns

# پارامترهای توزیع باینومیال
n = 20  # تعداد سوالات
p = 1 / 5  # احتمال موفقیت

# محاسبه PMF و CDF
x = np.arange(0, n + 1)
pmf = binom.pmf(x, n, p)
cdf = binom.cdf(x, n, p)

sns.set(style="whitegrid")

# رسم نمودارهای 2 بعدی
plt.figure(figsize=(14, 6))

# PMF نمودار
plt.subplot(1, 2, 1)
sns.barplot(x=x, y=pmf, palette="Blues_d", edgecolor='black')
plt.xlabel('Number of Correct Answers')
plt.ylabel('Probability')
plt.title('Binomial PMF (n=20, p=0.2)')

# CDF نمودار
plt.subplot(1, 2, 2)
sns.lineplot(x=x, y=cdf, marker='o', color='red')
plt.xlabel('Number of Correct Answers')
plt.ylabel('Cumulative Probability')
plt.title('Binomial CDF (n=20, p=0.2)')

plt.tight_layout()
plt.show()

# رسم نمودار 3 بعدی برای توزیع باینومیال
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

# داده‌ها برای رسم نمودار 3 بعدی
x_3d = np.arange(0, n + 1)
y_3d_pmf = np.zeros_like(x_3d)
z_3d_pmf = pmf

y_3d_cdf = np.ones_like(x_3d)  # برای CDF
z_3d_cdf = cdf

# رسم نوارهای 3 بعدی برای PMF
ax.bar3d(x_3d, y_3d_pmf, np.zeros_like(z_3d_pmf), dx=0.6, dy=0.6, dz=z_3d_pmf, color='cyan', alpha=0.7, label='PMF')

# رسم نوارهای 3 بعدی برای CDF
ax.bar3d(x_3d, y_3d_cdf, np.zeros_like(z_3d_cdf), dx=0.6, dy=0.6, dz=z_3d_cdf, color='magenta', alpha=0.7, label='CDF')

# تنظیمات نمودار
ax.set_xlabel('Number of Correct Answers')
ax.set_ylabel('Type')
ax.set_zlabel('Probability')
ax.set_title('Binomial Distribution PMF and CDF in 3D')
ax.set_yticks([0, 1])
ax.set_yticklabels(['PMF', 'CDF'])
ax.legend()
ax.grid(True)

plt.show()
