<<<<<<< HEAD
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# داده‌های نمونه
data = pd.DataFrame({
    'name': ['erfan', 'ali', 'elyas'],
    'math': [20, 15, 14],
    'correct': [19, 13, 10],
})

# ایجاد نمودار
plt.figure(figsize=(10, 6), dpi=100, facecolor='w', edgecolor='black')

# رسم نمودارهای ستونی با seaborn
plt.subplot(1, 2, 1)
sns.barplot(data=data, x='name', y='math', label='Math', color='black', alpha=0.5)
sns.barplot(data=data, x='name', y='correct', label='Correct', color='green', alpha=0.5)

# افزودن برچسب‌ها و عنوان
plt.legend()
plt.xlabel('Name')
plt.ylabel('Scores')
plt.title('Bar Plot of Math and Correct Scores')

plt.subplot(1, 2, 2)
sns.barplot(data=data, x='math', y='name', label='Math', color='black', alpha=0.5 , orient='h')
sns.barplot(data=data, x='correct', y='name', label='Correct', color='green', alpha=0.5, orient='h')

# افزودن برچسب‌ها و عنوان
plt.legend()
plt.xlabel('score')
plt.ylabel('name')
plt.title('Bar Plot of Math and Correct Scores')

# نمایش نمودار
plt.show()
=======
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# داده‌های نمونه
data = pd.DataFrame({
    'name': ['erfan', 'ali', 'elyas'],
    'math': [20, 15, 14],
    'correct': [19, 13, 10],
})

# ایجاد نمودار
plt.figure(figsize=(10, 6), dpi=100, facecolor='w', edgecolor='black')

# رسم نمودارهای ستونی با seaborn
plt.subplot(1, 2, 1)
sns.barplot(data=data, x='name', y='math', label='Math', color='black', alpha=0.5)
sns.barplot(data=data, x='name', y='correct', label='Correct', color='green', alpha=0.5)

# افزودن برچسب‌ها و عنوان
plt.legend()
plt.xlabel('Name')
plt.ylabel('Scores')
plt.title('Bar Plot of Math and Correct Scores')

plt.subplot(1, 2, 2)
sns.barplot(data=data, x='math', y='name', label='Math', color='black', alpha=0.5 , orient='h')
sns.barplot(data=data, x='correct', y='name', label='Correct', color='green', alpha=0.5, orient='h')

# افزودن برچسب‌ها و عنوان
plt.legend()
plt.xlabel('score')
plt.ylabel('name')
plt.title('Bar Plot of Math and Correct Scores')

# نمایش نمودار
plt.show()
>>>>>>> 462e300dbcb4cf0751f6b76a297dabc18c342638
