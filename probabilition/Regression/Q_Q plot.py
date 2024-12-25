import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import scipy.stats as stats

# تولید داده‌های نمونه
np.random.seed(0)
x = np.random.uniform(-10, 10, 100)
y = 2 **x + np.random.normal(0, 1, 100)

# ایجاد DataFrame
data = pd.DataFrame({'x': x, 'y': y})

X = sm.add_constant(data['x'])
model = sm.OLS(data['y'], X).fit()

residuals = model.resid

plt.figure(figsize=(8, 6))
stats.probplot(residuals, dist="norm", plot=plt)
plt.title('Q-Q Plot of Residuals')
plt.show()
