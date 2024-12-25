import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# تولید داده‌های نمونه
np.random.seed(0)
x = np.random.uniform(-10, 10, 100)
x2=x*2
y = 2 ** x + np.random.normal(0, 1, 100)  # مدل خطی به اضافه نویز

# ایجاد DataFrame
data = pd.DataFrame({'x': x, 'y': y, 'x2':x2})

min_val = np.min(data)
max_val = np.max(data)

# نرمال‌سازی کمینه-بیشینه
data_normalized = (data - min_val) / (max_val - min_val)

# اضافه کردن یک ستون ثابت برای مدل رگرسیون
X = sm.add_constant(data_normalized['x'])
model = sm.OLS(data_normalized['y'], X).fit()  # برازش مدل رگرسیون

# مشاهده نتایج مدل
print(model.summary())

# پیش‌بینی مقادیر y با استفاده از مدل برازش‌شده
data_normalized['y_pred'] = model.predict(X)
data['y_pred'] = model.predict(X)

# رسم نمودار پراکندگی و خط رگرسیون
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.scatterplot(x=data['x'] ,y=data['x'] ,color='blue', label='data')
plt.plot(data['x'], data['x'], color='red', linewidth=2, label='Fitted Line')
plt.xlabel('Independent Variable (x)')
plt.ylabel('Dependent Variable (y)')
plt.title('data_normalized')

plt.subplot(1, 2, 2)
sns.scatterplot(x=data['x'], y=data['y'], color='blue', label='Data')
plt.plot(data['x'], data['y_pred'], color='red', linewidth=2, label='Fitted Line')
plt.xlabel('Independent Variable (x)')
plt.ylabel('Dependent Variable (y)')
plt.title('Scatter Plot with Fitted Regression Line')
plt.legend()
plt.show()

sns.heatmap(data_normalized.corr(), annot=True, cmap='jet')
plt.xlabel('Independent Variable (x)')
plt.ylabel('Dependent Variable (y)')
plt.title('data_normalized')

plt.legend()
plt.show()
