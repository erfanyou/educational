import matplotlib.pyplot as plt

plt.figure(dpi=100)
plt.pie([20,30,50],
        labels=['a', 'b', 'c'],
        colors=['red', 'green', 'blue'],
        explode=(0, 0, 0.1),
        autopct='%1.1f%%',
        pctdistance=0.7,
        shadow=True,
        wedgeprops=dict(width=0.5))

plt.title('Doughnut Chart Example')
plt.show()
