<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt

# داده‌های نمونه
data = np.array([1, 10, 100, 1000, 10000])
data_log_transformed = np.log(data)

# رسم داده‌های اصلی و داده‌های تبدیل شده
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(data, 'o-')
plt.title('Original Data')
plt.xlabel('Index')
plt.ylabel('Value')

plt.subplot(1, 2, 2)
plt.plot(data_log_transformed, 'o-')
plt.title('Log Transformed Data')
plt.xlabel('Index')
plt.ylabel('Log(Value)')

plt.tight_layout()
plt.show()
=======
import numpy as np
import matplotlib.pyplot as plt

# داده‌های نمونه
data = np.array([1, 10, 100, 1000, 10000])
data_log_transformed = np.log(data)

# رسم داده‌های اصلی و داده‌های تبدیل شده
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(data, 'o-')
plt.title('Original Data')
plt.xlabel('Index')
plt.ylabel('Value')

plt.subplot(1, 2, 2)
plt.plot(data_log_transformed, 'o-')
plt.title('Log Transformed Data')
plt.xlabel('Index')
plt.ylabel('Log(Value)')

plt.tight_layout()
plt.show()
>>>>>>> 462e300dbcb4cf0751f6b76a297dabc18c342638
