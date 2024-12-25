import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data=np.array([[1, 2, 3, 4,  5],
                [6, 7, 8, 9, 10],
                [4 ,3 ,1 ,5  ,2],
                [1 ,3 ,2 ,3  ,4]
])
sns.heatmap(np.corrcoef(data), annot=True, cmap='jet')

plt.show()