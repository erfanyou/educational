import pandas as pd

# داده‌های نمونه
data = pd.DataFrame({'x': [7, 7, 8, 9, 11], 'y': [5, 4, 3, 2, 1]})

# محاسبه کوواریانس
cov_matrix = data.cov()
print("Covariance matrix:\n", cov_matrix)

# کوواریانس بین x و y
cov_xy = cov_matrix.loc['x', 'y']
print("Covariance between x and y:", cov_xy, '\n\n')

#####################################################

corr_matrix_1 = data.corr()
print("Correlation matrix:\n", corr_matrix_1)

corr_xy_1 = corr_matrix_1.loc['x', 'y']
print("Correlation between x and y:", corr_xy_1, '\n\n')

#####################################################

corr_matrix_2= data.corr(method='pearson')
print("Correlation pearson matrix:\n", corr_matrix_2)

corr_xy_2 = corr_matrix_2.loc['x', 'y']
print("Correlation between x and y:", corr_xy_2, '\n\n')

######################################################

corr_matrix_3 = data.corr(method='spearman')
print('Correlation spearman matrix:\n', corr_matrix_3)

corr_xy_3 = corr_matrix_3.loc['x', 'y']
print('Correlation between x and y:', corr_xy_3, '\n\n')
