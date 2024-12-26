<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt

# پارامترهای توزیع یکنواخت
a = -3
b = 3

# ایجاد داده‌های توزیع یکنواخت
B_values = np.linspace(a, b, 1000)
pdf = np.ones_like(B_values) / (b - a)  # تابع چگالی احتمال یکنواخت

# ناحیه‌هایی که |B| >= 2
fill_between_x1 = np.linspace(-3, -2, 500)
fill_between_x2 = np.linspace(2, 3, 500)

# رسم نمودار
fig = plt.figure(figsize=(14, 6))

# توزیع یکنواخت به صورت 3 بعدی
ax = fig.add_subplot(111, projection='3d')

# رسم تابع چگالی احتمال یکنواخت
ax.plot(B_values, pdf, zs=0, zdir='y', label='Uniform Distribution PDF', color='blue')

# پر کردن ناحیه‌ای که |B| >= 2 به صورت نوارهای عمودی
ax.bar3d(fill_between_x1, 0, 0, dx=0.1, dy=1 / (b - a), dz=1, color='red', alpha=0.5)
ax.bar3d(fill_between_x2, 0, 0, dx=0.1, dy=1 / (b - a), dz=1, color='red', alpha=0.5)

# تنظیمات نمودار
ax.set_xlabel('B')
ax.set_ylabel('Probability Density')
ax.set_zlabel('Height')
ax.set_title('Uniform Distribution of B with Highlighted Region |B| >= 2')
ax.legend()
ax.grid(True)

plt.show()
=======
import numpy as np
import matplotlib.pyplot as plt

# پارامترهای توزیع یکنواخت
a = -3
b = 3

# ایجاد داده‌های توزیع یکنواخت
B_values = np.linspace(a, b, 1000)
pdf = np.ones_like(B_values) / (b - a)  # تابع چگالی احتمال یکنواخت

# ناحیه‌هایی که |B| >= 2
fill_between_x1 = np.linspace(-3, -2, 500)
fill_between_x2 = np.linspace(2, 3, 500)

# رسم نمودار
fig = plt.figure(figsize=(14, 6))

# توزیع یکنواخت به صورت 3 بعدی
ax = fig.add_subplot(111, projection='3d')

# رسم تابع چگالی احتمال یکنواخت
ax.plot(B_values, pdf, zs=0, zdir='y', label='Uniform Distribution PDF', color='blue')

# پر کردن ناحیه‌ای که |B| >= 2 به صورت نوارهای عمودی
ax.bar3d(fill_between_x1, 0, 0, dx=0.1, dy=1 / (b - a), dz=1, color='red', alpha=0.5)
ax.bar3d(fill_between_x2, 0, 0, dx=0.1, dy=1 / (b - a), dz=1, color='red', alpha=0.5)

# تنظیمات نمودار
ax.set_xlabel('B')
ax.set_ylabel('Probability Density')
ax.set_zlabel('Height')
ax.set_title('Uniform Distribution of B with Highlighted Region |B| >= 2')
ax.legend()
ax.grid(True)

plt.show()
>>>>>>> 462e300dbcb4cf0751f6b76a297dabc18c342638
