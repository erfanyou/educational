import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

model = joblib.load(r'F:\jupyter\educational-\exercise\salary developer\pre_Salary.joblib')

#---------------------------------------------------------------------------------------------------

country_col=['c_Argentina',
        'c_Australia', 'c_Austria', 'c_Bangladesh', 'c_Belgium', 'c_Brazil',
        'c_Canada', 'c_Czech Republic', 'c_Denmark', 'c_Finland', 'c_France',
        'c_Germany', 'c_Greece', 'c_Hungary', 'c_India',
        'c_Iran, Islamic Republic of...', 'c_Israel', 'c_Italy', 'c_Mexico',
        'c_Netherlands', 'c_New Zealand', 'c_Norway', 'c_Pakistan', 'c_Poland',
        'c_Portugal', 'c_Romania', 'c_Russian Federation', 'c_South Africa',
        'c_Spain', 'c_Sweden', 'c_Switzerland', 'c_Turkey', 'c_Ukraine',
        'c_United Kingdom of Great Britain and Northern Ireland',
        'c_United States of America']


#----------------------------------------------------------------------------------------------------
st.title('Get your salary💰')


Age = st.selectbox("Age", ["Teenager", "Young",'Adult' , 'Elderly'])
Gender = st.selectbox("Gender", ["Man", "Woman"])
EdLevel = st.selectbox("EdLevel", ["Bachelor’s", "Master’s",'doctoral','students / school'])
YearsCodePro = st.slider("Years of Professional Coding Experience", 0, 50)
Country=st.selectbox('country',['United Kingdom of Great Britain and Northern Ireland', 'Israel',
        'Netherlands', 'United States of America', 'Czech Republic',
        'Austria', 'Italy', 'Germany', 'Poland', 'Norway', 'Canada',
        'Brazil', 'Sweden', 'France', 'Spain', 'Romania', 'India',
        'Belgium', 'Russian Federation', 'Mexico', 'Switzerland',
        'South Africa', 'Finland', 'Denmark', 'Australia', 'Greece',
        'Portugal', 'Hungary', 'Bangladesh', 'Ukraine', 'Pakistan',
        'Iran, Islamic Republic of...', 'Turkey', 'Argentina',
        'New Zealand'])

#-------------------------------------------------------------------------------------------------------

df = pd.DataFrame({
    "Age": [Age],
    "Gender": [Gender],
    "EdLevel": [EdLevel],
    "YearsCodePro": [YearsCodePro],
    "Country": [Country],
})



#---------------------------------------------------------------------------------
df['Gender'].replace({'Man': 1, 'Woman': 0}, inplace=True)
df['EdLevel'] = df['EdLevel'].map({
    'Master’s': 3,
    'Bachelor’s': 2,
    'students / school': 1,
    'doctoral': 4
})
df['Age'] = df['Age'].map({
    'Young': 2,
    'Adult': 3,
    'Elderly': 4,
    'Teenager': 1
})

for i in country_col:
    if i in df['Country'].values:
        df[i]=True
    else:
        df[i]=False

df.columns= df.columns.str.replace('Iran, Islamic Republic of...','')

df.drop(columns='Country',inplace=True)

def predict():
    prediction = model.predict(df)
    st.write(f"your salary will be : {prediction[0]:,.0f} $")

st.button('Predict', on_click=predict)
