import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# داده‌های نمونه
data = np.array([3, 6, 5, 3, 9, 5, 4, 3])
data = np.append(data, [-50,-10, -15, 25, 20,100])

# محاسبه IQR
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

# محاسبه مقادیر MAX و MIN برای شناسایی داده‌های پرت
MAX = Q3 + 1.5 * IQR
MIN = Q1 - 1.5 * IQR

# شناسایی داده‌های پرت با استفاده از IQR
outliers_iqr = data[(data < MIN) | (data > MAX)]
print("Outliers (IQR method):", outliers_iqr)

################################################################

mean = np.mean(data)
std_dev = np.std(data)

# تعیین محدوده‌های پرت با استفاده از انحراف معیار
MIN_STD = mean - 3 * std_dev
MAX_STD = mean + 3 * std_dev

# شناسایی داده‌های پرت با استفاده از انحراف معیار
outliers_std = data[(data < MIN_STD) | (data > MAX_STD)]
print("Outliers (Standard Deviation method):", outliers_std)

################################################################

# ایجاد نمودار جعبه‌ای و هیستوگرام با داده‌های نمونه
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.histplot(data, kde=True, color='blue')
plt.title('Histogram')

plt.subplot(1, 2, 2)
sns.boxplot(data,color='purple',orient='h')
plt.title('Boxplot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.tight_layout()
plt.show()
