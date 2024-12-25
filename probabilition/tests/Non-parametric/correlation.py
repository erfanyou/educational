import scipy.stats as st
import numpy as np

H0='correlated'

data_1=np.random.randn(100)
data_2=np.random.randn(100)

mouth=np.array([132,24,324,355,53,126,97,348,229,109])
year=mouth**2+np.random.randn(len(mouth))*83


stat, p_value = st.pearsonr(year,mouth)
print('pearson_age :')
print(f'Statistic: {stat}, p-value: {p_value}')
if p_value < 0.05:
    print(f'{H0} is rejected', end='\n\n')
else:
    print(f'{H0} is not rejected', end='\n\n')


stat, p_value = st.pearsonr(data_1,data_2)
print('pearson_raw :')
print(f'Statistic: {stat}, p-value: {p_value}')
if p_value < 0.05:
    print(f'{H0} is rejected', end=4*'\n\n')
else:
    print(f'{H0} is not rejected', end=4*'\n\n')

############################################################

stat,p_value = st.spearmanr(year,mouth)
print('spearman_age :')
print(f'Statistic: {stat}, p-value: {p_value}')
if p_value < 0.05:
    print(f'{H0} is rejected', end='\n\n')
else:
    print(f'{H0} is not rejected', end='\n\n')


stat,p_value = st.spearmanr(data_1,data_2)
print('spearman_raw :')
print(f'Statistic: {stat}, p-value: {p_value}')
if p_value < 0.05:
    print(f'{H0} is rejected', end=4*'\n\n')
else:
    print(f'{H0} is not rejected', end=4*'\n\n')

#############################################################

stat,p_value = st.kendalltau(year,mouth)
print('kendall_age :')
print(f'Statistic: {stat}, p-value: {p_value}')
if p_value < 0.05:
    print(f'{H0} is rejected', end='\n\n')
else:
    print(f'{H0} is not rejected', end='\n\n')


stat,p_value = st.kendalltau(data_1,data_2)
print('kendall_raw :')
print(f'Statistic: {stat}, p-value: {p_value}')
if p_value < 0.05:
    print(f'{H0} is rejected', end=4*'\n\n')
else:
    print(f'{H0} is not rejected', end=4*'\n\n')





