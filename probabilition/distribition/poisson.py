import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
import seaborn as sns

# پارامتر توزیع پواسون
lambda_1_month = 2  # برای یک ماه
lambda_3_months = 6  # برای 3 ماه

# مقادیر x برای یک ماه و 3 ماه
x_1_month = np.arange(0, 10)  # تعداد وقوع‌ها از 0 تا 9
x_3_months = np.arange(0, 15)  # تعداد وقوع‌ها از 0 تا 14

# محاسبه PMF و CDF
pmf_1_month = poisson.pmf(x_1_month, lambda_1_month)
cdf_1_month = poisson.cdf(x_1_month, lambda_1_month)

pmf_3_months = poisson.pmf(x_3_months, lambda_3_months)
cdf_3_months = poisson.cdf(x_3_months, lambda_3_months)

# تنظیم سبک Seaborn
sns.set(style="whitegrid")

# رسم نمودار
plt.figure(figsize=(14, 10))

# PMF برای یک ماه
plt.subplot(2, 2, 1)
sns.barplot(x=x_1_month, y=pmf_1_month, palette="Blues_d")
plt.xlabel('Number of Servicing Events')
plt.ylabel('Probability')
plt.title('Poisson PMF (λ=2) for 1 Month')

# CDF برای یک ماه
plt.subplot(2, 2, 2)
sns.lineplot(x=x_1_month, y=cdf_1_month, marker='o', color='blue')
plt.xlabel('Number of Servicing Events')
plt.ylabel('Cumulative Probability')
plt.title('Poisson CDF (λ=2) for 1 Month')

# PMF برای 3 ماه
plt.subplot(2, 2, 3)
sns.barplot(x=x_3_months, y=pmf_3_months, palette="Reds_d")
plt.xlabel('Number of Servicing Events')
plt.ylabel('Probability')
plt.title('Poisson PMF (λ=6) for 3 Months')

# CDF برای 3 ماه
plt.subplot(2, 2, 4)
sns.lineplot(x=x_3_months, y=cdf_3_months, marker='o', color='red')
plt.xlabel('Number of Servicing Events')
plt.ylabel('Cumulative Probability')
plt.title('Poisson CDF (λ=6) for 3 Months')

plt.tight_layout()
plt.show()

# رسم نمودار 3 بعدی
fig = plt.figure(figsize=(16, 10))

# نمودار 3 بعدی برای PMF و CDF برای یک ماه
ax1 = fig.add_subplot(121, projection='3d')
x_3d_1_month = np.concatenate([x_1_month, x_1_month])
y_3d_1_month = np.concatenate([np.zeros_like(x_1_month), np.ones_like(x_1_month)])
z_3d_1_month_pmf = np.concatenate([pmf_1_month, np.zeros_like(pmf_1_month)])
z_3d_1_month_cdf = np.concatenate([np.zeros_like(cdf_1_month), cdf_1_month])

# رسم نوارهای 3 بعدی برای PMF و CDF برای یک ماه
ax1.bar(x_3d_1_month, z_3d_1_month_pmf, zs=0, zdir='y', width=0.5, color='blue', alpha=0.6, label='PMF (λ=2)')
ax1.bar(x_3d_1_month, z_3d_1_month_cdf, zs=1, zdir='y', width=0.5, color='red', alpha=0.6, label='CDF (λ=2)')

# تنظیمات نمودار
ax1.set_xlabel('Number of Servicing Events')
ax1.set_ylabel('Type')
ax1.set_zlabel('Probability')
ax1.set_title('Poisson PMF and CDF for 1 Month')
ax1.legend()

# نمودار 3 بعدی برای PMF و CDF برای 3 ماه
ax2 = fig.add_subplot(122, projection='3d')
x_3d_3_months = np.concatenate([x_3_months, x_3_months])
y_3d_3_months = np.concatenate([np.zeros_like(x_3_months), np.ones_like(x_3_months)])
z_3d_3_months_pmf = np.concatenate([pmf_3_months, np.zeros_like(pmf_3_months)])
z_3d_3_months_cdf = np.concatenate([np.zeros_like(cdf_3_months), cdf_3_months])

# رسم نوارهای 3 بعدی برای PMF و CDF برای 3 ماه
ax2.bar(x_3d_3_months, z_3d_3_months_pmf, zs=0, zdir='y', width=0.5, color='cyan', alpha=0.6, label='PMF (λ=6)')
ax2.bar(x_3d_3_months, z_3d_3_months_cdf, zs=1, zdir='y', width=0.5, color='magenta', alpha=0.6, label='CDF (λ=6)')

# تنظیمات نمودار
ax2.set_xlabel('Number of Servicing Events')
ax2.set_ylabel('Type')
ax2.set_zlabel('Probability')
ax2.set_title('Poisson PMF and CDF for 3 Months')
ax2.legend()

plt.tight_layout()
plt.show()
