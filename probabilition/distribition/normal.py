import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, binom

# پارامتر توزیع نرمال
mu = 8
sigma = 0.5

# سوال الف: درصد لوله‌ها با طول بین 7.5 تا 9 متر
z1 = (7.5 - mu) / sigma
z2 = (9 - mu) / sigma
percent_between_7_5_and_9 = norm.cdf(z2) - norm.cdf(z1)

# سوال ب: تعداد لوله‌هایی با طول بیشتر از 9.2 متر از 200 لوله
z_9_2 = (9.2 - mu) / sigma
prob_more_than_9_2 = 1 - norm.cdf(z_9_2)
number_more_than_9_2 = 200 * prob_more_than_9_2

# سوال ج: 97.5 درصد از لوله‌ها طولشان از چه مقداری کمتر است؟
z_97_5 = norm.ppf(0.975)
x_97_5 = mu + z_97_5 * sigma

# سوال د: درصد لوله‌هایی که طولشان کمتر از 8.4 متر با فرض اینکه طول حداقل 7.8 متر است
z_7_8 = (7.8 - mu) / sigma
z_8_4 = (8.4 - mu) / sigma
prob_between_7_8_and_8_4 = norm.cdf(z_8_4) - norm.cdf(z_7_8)
prob_more_than_7_8 = 1 - norm.cdf(z_7_8)
percent_less_than_8_4_given_more_than_7_8 = (prob_between_7_8_and_8_4 / prob_more_than_7_8) * 100

# سوال ه: احتمال اینکه حداکثر یک لوله از پنج لوله طولی بیش از 9 متر داشته باشد
p_longer_than_9 = 1 - norm.cdf((9 - mu) / sigma)
prob_max_1_longer_than_9 = binom.cdf(1, 5, p_longer_than_9)

# چاپ نتایج
print(f"الف - درصد لوله‌ها با طول بین 7.5 تا 9 متر: {percent_between_7_5_and_9 * 100:.2f}%")
print(f"ب - تعداد لوله‌ها با طول بیشتر از 9.2 متر: {number_more_than_9_2:.2f}")
print(f"ج - 97.5% از لوله‌ها طولشان از {x_97_5:.2f} متر کمتر است.")
print(f"د - درصد لوله‌هایی که طولشان کمتر از 8.4 متر با فرض طول حداقل 7.8 متر: {percent_less_than_8_4_given_more_than_7_8:.2f}%")
print(f"ه - احتمال اینکه حداکثر یک لوله از پنج لوله طولی بیش از 9 متر داشته باشد: {prob_max_1_longer_than_9:.4f}")

# رسم نمودارها با Seaborn
plt.figure(figsize=(18, 12))

# نمودار درصد لوله‌ها با طول بین 7.5 تا 9 متر
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)
pdf = norm.pdf(x, mu, sigma)
plt.subplot(2, 2, 1)
sns.lineplot(x=x, y=pdf, color='blue')
plt.fill_between(x, pdf, where=((x >= 7.5) & (x <= 9)), color='skyblue', alpha=0.4)
plt.title('Percentage of Pipes Between 7.5 and 9 meters')
plt.xlabel('Length (meters)')
plt.ylabel('Density')

# نمودار تعداد لوله‌ها با طول بیشتر از 9.2 متر
plt.subplot(2, 2, 2)
sns.lineplot(x=x, y=pdf, color='blue')
plt.fill_between(x, pdf, where=(x >= 9.2), color='salmon', alpha=0.4)
plt.title('Pipes Longer than 9.2 meters')
plt.xlabel('Length (meters)')
plt.ylabel('Density')

# نمودار درصد طول کمتر از 8.4 متر با فرض حداقل 7.8 متر
plt.subplot(2, 2, 3)
sns.lineplot(x=x, y=pdf, color='blue')
plt.fill_between(x, pdf, where=((x >= 7.8) & (x <= 8.4)), color='green', alpha=0.4)
plt.title('Percentage Less than 8.4 meters (Given Minimum 7.8 meters)')
plt.xlabel('Length (meters)')
plt.ylabel('Density')

# نمودار احتمال حداکثر یک لوله از پنج لوله طولی بیش از 9 متر
n = 5
x4 = np.arange(0, n+1)
pmf = binom.pmf(x4, n, p_longer_than_9)
plt.subplot(2, 2, 4)
sns.barplot(x=x4, y=pmf, palette="Oranges_d")
plt.title('Binomial PMF for Maximum 1 Pipe Longer than 9 meters')
plt.xlabel('Number of Pipes Longer than 9 meters')
plt.ylabel('Probability')

plt.tight_layout()
plt.show()
