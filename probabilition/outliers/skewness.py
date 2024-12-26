<<<<<<< HEAD
import numpy as np
from scipy.stats import skew
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
# داده‌های نمونه
data = np.array([3, 6, 5, 3, 9, 5, 4, 3, -10, -15, 25, 20, 100])

# محاسبه چولگی
skewness_scipy = skew(data)
print("Skewness (scipy):", skewness_scipy)

##############################################

# محاسبه چولگی با pandas
data_series = pd.Series(data)
skewness_pandas = data_series.skew()
print("Skewness (pandas):", skewness_pandas)

##############################################

# رسم نمودار
plt.figure(figsize=(12, 6))

# نمودار هیستوگرام
plt.subplot(1, 2, 1)
sns.histplot(data_series, kde=False, color='blue', bins=10)
plt.title('Histogram')

# نمودار KDE
plt.subplot(1, 2, 2)
sns.kdeplot(data_series, color='red')
plt.title('KDE Plot')

plt.tight_layout()
plt.show()

##############################################################################################

#رفع چولگی

data_log = np.log1p(data)
skewness_log = stats.skew(data_log)
print("Skewness after Log Transformation:", skewness_log)

# تبدیل ریشه‌دار
data_sqrt = np.sqrt(data - np.min(data) + 1)  # Add 1 to handle zero values
skewness_sqrt = stats.skew(data_sqrt)
print("Skewness after Square Root Transformation:", skewness_sqrt)

# تبدیل معکوس
data_inv = 1 / (data - np.min(data) + 1)  # Add 1 to avoid division by zero
skewness_inv = stats.skew(data_inv)
print("Skewness after Inverse Transformation:", skewness_inv)

# تبدیل باکس-کاکس
data_boxcox, lambda_ = stats.boxcox(data - np.min(data) + 1)  # Add 1 to handle zero values
skewness_boxcox = stats.skew(data_boxcox)
print("Skewness after Box-Cox Transformation:", skewness_boxcox)

# رسم نمودارها
plt.figure(figsize=(15, 10))

# هیستوگرام اصلی
plt.subplot(2, 3, 1)
sns.histplot(data, kde=True, color='blue')
plt.title('Original Data')

# هیستوگرام پس از تبدیل لگاریتمی
plt.subplot(2, 3, 2)
sns.histplot(data_log, kde=True, color='green')
plt.title('Log Transformation')

# هیستوگرام پس از تبدیل ریشه‌دار
plt.subplot(2, 3, 3)
sns.histplot(data_sqrt, kde=True, color='red')
plt.title('Square Root Transformation')

# هیستوگرام پس از تبدیل معکوس
plt.subplot(2, 3, 4)
sns.histplot(data_inv, kde=True, color='purple')
plt.title('Inverse Transformation')

# هیستوگرام پس از تبدیل باکس-کاکس
plt.subplot(2, 3, 5)
sns.histplot(data_boxcox, kde=True, color='orange')
plt.title('Box-Cox Transformation')

plt.tight_layout()
plt.show()
=======
import numpy as np
from scipy.stats import skew
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
# داده‌های نمونه
data = np.array([3, 6, 5, 3, 9, 5, 4, 3, -10, -15, 25, 20, 100])

# محاسبه چولگی
skewness_scipy = skew(data)
print("Skewness (scipy):", skewness_scipy)

##############################################

# محاسبه چولگی با pandas
data_series = pd.Series(data)
skewness_pandas = data_series.skew()
print("Skewness (pandas):", skewness_pandas)

##############################################

# رسم نمودار
plt.figure(figsize=(12, 6))

# نمودار هیستوگرام
plt.subplot(1, 2, 1)
sns.histplot(data_series, kde=False, color='blue', bins=10)
plt.title('Histogram')

# نمودار KDE
plt.subplot(1, 2, 2)
sns.kdeplot(data_series, color='red')
plt.title('KDE Plot')

plt.tight_layout()
plt.show()

##############################################################################################

#رفع چولگی

data_log = np.log1p(data)
skewness_log = stats.skew(data_log)
print("Skewness after Log Transformation:", skewness_log)

# تبدیل ریشه‌دار
data_sqrt = np.sqrt(data - np.min(data) + 1)  # Add 1 to handle zero values
skewness_sqrt = stats.skew(data_sqrt)
print("Skewness after Square Root Transformation:", skewness_sqrt)

# تبدیل معکوس
data_inv = 1 / (data - np.min(data) + 1)  # Add 1 to avoid division by zero
skewness_inv = stats.skew(data_inv)
print("Skewness after Inverse Transformation:", skewness_inv)

# تبدیل باکس-کاکس
data_boxcox, lambda_ = stats.boxcox(data - np.min(data) + 1)  # Add 1 to handle zero values
skewness_boxcox = stats.skew(data_boxcox)
print("Skewness after Box-Cox Transformation:", skewness_boxcox)

# رسم نمودارها
plt.figure(figsize=(15, 10))

# هیستوگرام اصلی
plt.subplot(2, 3, 1)
sns.histplot(data, kde=True, color='blue')
plt.title('Original Data')

# هیستوگرام پس از تبدیل لگاریتمی
plt.subplot(2, 3, 2)
sns.histplot(data_log, kde=True, color='green')
plt.title('Log Transformation')

# هیستوگرام پس از تبدیل ریشه‌دار
plt.subplot(2, 3, 3)
sns.histplot(data_sqrt, kde=True, color='red')
plt.title('Square Root Transformation')

# هیستوگرام پس از تبدیل معکوس
plt.subplot(2, 3, 4)
sns.histplot(data_inv, kde=True, color='purple')
plt.title('Inverse Transformation')

# هیستوگرام پس از تبدیل باکس-کاکس
plt.subplot(2, 3, 5)
sns.histplot(data_boxcox, kde=True, color='orange')
plt.title('Box-Cox Transformation')

plt.tight_layout()
plt.show()
>>>>>>> 462e300dbcb4cf0751f6b76a297dabc18c342638
