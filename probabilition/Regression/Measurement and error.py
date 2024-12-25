import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score



# 1. تولید داده‌ها و آماده‌سازی آن‌ها
np.random.seed(0)
x = np.random.uniform(-10, 10, 100)
y = 2 * x + np.random.normal(0, 1, 100)  # مدل خطی به اضافه نویز

# ایجاد DataFrame
data = pd.DataFrame({'x': x, 'y': y})

# نرمال‌سازی کمینه-بیشینه
scaler = MinMaxScaler()
data[['x', 'y']] = scaler.fit_transform(data[['x', 'y']])

# 2. فیت کردن مدل رگرسیون
X = data[['x']]
y = data['y']

model = LinearRegression()
model.fit(X, y)  # برازش مدل رگرسیون

# 3. ارزیابی مدل
# پیش‌بینی مقادیر y با استفاده از مدل برازش‌شده
data['y_pred'] = model.predict(X)
residuals = data['y'] - data['y_pred']

# رسم نمودار پراکندگی و خط رگرسیون
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.scatterplot(x=data['x'], y=data['y'], color='blue', label='Data')
plt.plot(data['x'], data['y_pred'], color='red', linewidth=2, label='Fitted Line')
plt.xlabel('Independent Variable (x)')
plt.ylabel('Dependent Variable (y)')
plt.title('Scatter Plot with Fitted Regression Line')
plt.legend()

# رسم نمودار باقی‌مانده‌ها
plt.subplot(1, 2, 2)
sns.scatterplot(x=data['y_pred'], y=residuals, color='purple', label='Residuals')
plt.axhline(0, color='gray', linestyle='--')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.title('Residuals Plot')
plt.legend()

plt.tight_layout()
plt.show()

# رسم نمودار Q-Q برای باقی‌مانده‌ها
import scipy.stats as stats

plt.figure(figsize=(8, 6))
stats.probplot(residuals, dist="norm", plot=plt)
plt.title('Q-Q Plot of Residuals')
plt.show()

# محاسبه و چاپ معیارهای ارزیابی
mse = mean_squared_error(data['y'], data['y_pred'])
r2 = r2_score(data['y'], data['y_pred'])

print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R-squared: {r2:.4f}")

mse=y-data['y_pred']

plt.figure(figsize=(8, 6))
sns.histplot(mse, kde=True, palette='Set1', edgecolor='black')
plt.title('Q-Q Plot of Residuals')
plt.show()
