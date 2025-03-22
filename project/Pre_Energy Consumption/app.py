import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import MinMaxScaler
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

model = joblib.load(r'F:\jupyter\educational-\exercise\Pre_Energy Consumption\pre_Energy.joblib')

#----------------------------------------------------------------------------
st.title('Energy Consumption Prediction:🏭')

datetime = st.text_input("Input your Datetime", "2025-12-31 05:00:00")


sstart = datetime.replace(datetime[:datetime.find('-')]  ,  str(int(datetime[:datetime.find('-')])-1))

Datetime=pd.date_range(start=sstart, end=datetime, freq='H')


#----------------------------------------------------------------------------
df = pd.DataFrame({'Datetime': Datetime})
df['Datetime'] = pd.to_datetime(df['Datetime'])

df = df.set_index('Datetime')

def create_features(df):
    """
    Creates time series features from datetime index
    """
    df = df.copy()
    df['hour'] = df.index.hour
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    df['dayofmonth'] = df.index.day
    df['weekofyear'] = df.index.isocalendar().week
    
    return df

df = create_features(df)

features = [col for col in df.columns if col != 'PJME_MW']

scaler = MinMaxScaler()

df[features] = scaler.fit_transform(df[features])


#-----------------------------------------------------------------------------


def predict():
    prediction = model.predict(df)
    
    fig, ax = plt.subplots()
    ax.plot(df.index, prediction, color='purple')
    ax.set_title("PJME Power Consumption from a year ago to now")
    ax.set_xlabel("Time")
    ax.set_ylabel("Power Consumption (MW)")

    st.pyplot(fig)
    
    st.write(f"your Energy will be : {prediction[-1]:,.0f} ")

st.button('Predict', on_click=predict)
