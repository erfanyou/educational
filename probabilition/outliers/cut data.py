import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# داده‌های نمونه
data = np.array([3, 6, 5, 3, 9, 5, 4, 3])
data = np.append(data, [-50,-10, -15, 25, 20,100])

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

# محاسبه مقادیر MAX و MIN برای شناسایی داده‌های پرت
MAX = Q3 + 1.5 * IQR
MIN = Q1 - 1.5 * IQR

# داده‌های بدون پرت با روش IQR
data_no_outliers_iqr = data[~((data < MIN) | (data > MAX))]

# داده‌های بدون پرت با روش انحراف معیار
data_no_outliers_std = data[~((data < MIN) | (data > MAX))]

# رسم نمودار جعبه‌ای برای داده‌های بدون پرت
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.histplot(data=data, palette='cool', kde=True)
plt.title('Box Plot of Original Data')

plt.subplot(1, 2, 2)
sns.histplot(data=data_no_outliers_iqr, palette='purple', kde=True)
plt.title('Box Plot of Data without Outliers (IQR)')

plt.tight_layout()
plt.show()
