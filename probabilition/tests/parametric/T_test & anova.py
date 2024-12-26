<<<<<<< HEAD
import scipy.stats as st
import numpy as np

H0= 'equality of mean of samples'
H1= 'not equality of mean of samples'

x=np.array([123,243,343,143,315,126,147,188,209,110])
y=np.array([234,145,235,345,311,225,105,195,125,305])
z=np.array([123,243,388,209,110,145,105,195,125,305])


print('                                     t_test',end='\n\n')
def t_test(x,y,alternative="two-sided"):
    print('ttest_ind :')
    if alternative=="two-sided":
        t,p=st.ttest_ind(x,y)
        print(f"t={t}, p={p}")
        if p<0.05:
            print(f"reject : {H0}")
        else:
            print(f"not reject : {H0} ")
    elif alternative=="greater":
        t,p=st.ttest_ind(x,y,alternative="greater")
        print(f"t={t}, p={p}")
        if p<0.05:
            print(f"reject : {H0}")
        else:
            print(f"not reject : {H0} ")
    elif alternative=="less":
        t,p=st.ttest_ind(x,y,alternative="less")
        print(f"t={t}, p={p}")
        if p<0.05:
            print(f"reject : {H0}")
        else:
            print(f"not reject : {H0} ")
    print(1*"\n\n")

t_test(x,y,"less")

#############

stat , p_value = st.ttest_rel(x,y)
print('ttest_rel :')
print(f'Statistic: {stat}, p-value: {p_value}')
if p_value<0.05:
    print(f"reject : {H0}")
else:
    print(f"not reject : {H0} ")
print(4*"\n\n")

#####################################################
print('                                       anova',end='\n\n')


stat , p_value = st.f_oneway(x,y,z)
print('f_oneway :')
=======
import scipy.stats as st
import numpy as np

H0= 'equality of mean of samples'
H1= 'not equality of mean of samples'

x=np.array([123,243,343,143,315,126,147,188,209,110])
y=np.array([234,145,235,345,311,225,105,195,125,305])
z=np.array([123,243,388,209,110,145,105,195,125,305])


print('                                     t_test',end='\n\n')
def t_test(x,y,alternative="two-sided"):
    print('ttest_ind :')
    if alternative=="two-sided":
        t,p=st.ttest_ind(x,y)
        print(f"t={t}, p={p}")
        if p<0.05:
            print(f"reject : {H0}")
        else:
            print(f"not reject : {H0} ")
    elif alternative=="greater":
        t,p=st.ttest_ind(x,y,alternative="greater")
        print(f"t={t}, p={p}")
        if p<0.05:
            print(f"reject : {H0}")
        else:
            print(f"not reject : {H0} ")
    elif alternative=="less":
        t,p=st.ttest_ind(x,y,alternative="less")
        print(f"t={t}, p={p}")
        if p<0.05:
            print(f"reject : {H0}")
        else:
            print(f"not reject : {H0} ")
    print(1*"\n\n")

t_test(x,y,"less")

#############

stat , p_value = st.ttest_rel(x,y)
print('ttest_rel :')
print(f'Statistic: {stat}, p-value: {p_value}')
if p_value<0.05:
    print(f"reject : {H0}")
else:
    print(f"not reject : {H0} ")
print(4*"\n\n")

#####################################################
print('                                       anova',end='\n\n')


stat , p_value = st.f_oneway(x,y,z)
print('f_oneway :')
>>>>>>> 462e300dbcb4cf0751f6b76a297dabc18c342638
print(f'Statistic: {stat}, p-value: {p_value}')