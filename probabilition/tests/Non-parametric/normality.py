import scipy.stats as st

H0='normal distribution'
H1='not normal distribution'

data_1 = st.norm(0,1).rvs(size=1000)
data_2 = st.uniform(-2,2).rvs(size=1000)


stat, p_value = st.shapiro(data_1)
print('shapiro_normal :')
print(f'Statistic: {stat}, p-value: {p_value}')
if p_value < 0.05:
    print(f'{H0} is not rejected', end='\n\n')
else:
    print(f'{H0} is rejected', end='\n\n')


stat, p_value = st.shapiro(data_2)
print('shapiro_uniform :')
print(f'Statistic: {stat}, p-value: {p_value}')
if p_value < 0.05:
    print(f'{H0} is not rejected', end=4*'\n\n')
else:
    print(f'{H0} is rejected', end=4*'\n\n')
#######################################################

stat , p_value = st.kstest(data_1, 'norm')
print('kstest_normal :')
print(f'Statistic: {stat}, p-value: {p_value}')
if p_value < 0.05:
    print(f'{H0} is not rejected', end='\n\n')
else:
    print(f'{H0} is rejected', end='\n\n')


stat , p_value = st.kstest(data_2, 'uniform')
print('kstest_uniform :')
print(f'Statistic: {stat}, p-value: {p_value}')
if p_value < 0.05:
    print(f'{H0} is not rejected', end=4*'\n\n')
else:
    print(f'{H0} is rejected', end=4*'\n\n')
#######################################################

stat, p_value = st.normaltest(data_1)
print('normaltest_normal :')
print(f'Statistic: {stat}, p-value: {p_value}')
if p_value < 0.05:
    print(f'{H0} is not rejected', end='\n\n')
else:
    print(f'{H0} is rejected', end='\n\n')


stat, p_value = st.normaltest(data_2)
print('normaltest_uniform :')
print(f'Statistic: {stat}, p-value: {p_value}')
if p_value < 0.05:
    print(f'{H0} is not rejected', end=4*'\n\n')
else:
    print(f'{H0} is rejected', end=4*'\n\n')

#######################################################

result = st.anderson(data_1)
print('anderson_normal :')
print(f'Statistic: {result.statistic}')
for i in range(len(result.critical_values)):
    sl, cv = result.significance_level[i], result.critical_values[i]
    if result.statistic < cv:
        print(f' normal at the {sl} level')
    else:
        print(f'non_normal at the {sl} level')

print('\n\n')

result = st.anderson(data_2)
print('anderson_uniform :')
print(f'Statistic: {result.statistic}')
for i in range(len(result.critical_values)):
    sl, cv = result.significance_level[i], result.critical_values[i]
    if result.statistic < cv:
        print(f' normal at the {sl} level')
    else:
        print(f'non_normal at the {sl} level')

print(4*'\n\n')




