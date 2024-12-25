import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# داده‌های نمونه
data = np.array([3, 6, 5, 3, 9, 5, 4, 3])
data = np.append(data, [-50,-10, -15, 25, 20,100])

min_val = np.min(data)
max_val = np.max(data)

# نرمال‌سازی کمینه-بیشینه
data_normalized = (data - min_val) / (max_val - min_val)
print("Normalized Data (Min-Max):", data_normalized)

# ایجاد نمودار جعبه‌ای و هیستوگرام با داده‌های نمونه
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.histplot(data_normalized, kde=True, color='blue')
plt.title('Histogram')

plt.subplot(1, 2, 2)
sns.boxplot(data_normalized,color='purple',orient='h')
plt.title('Boxplot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.tight_layout()
plt.show()

###########################################################

mean = np.mean(data)
std_dev = np.std(data)

# استانداردسازی
data_standardized = (data - mean) / std_dev
print("Standardized Data:", data_standardized)

# ایجاد نمودار جعبه‌ای و هیستوگرام با داده‌های نمونه
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.histplot(data_standardized, kde=True, color='blue')
plt.title('Histogram')

plt.subplot(1, 2, 2)
sns.boxplot(data_standardized,color='purple',orient='h')
plt.title('Boxplot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.tight_layout()
plt.show()