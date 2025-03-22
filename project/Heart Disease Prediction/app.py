import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib


model =joblib.load(r'E:\jupyter\educational-\exercise\Heart Disease Prediction\pre_Hdisease.joblib')

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

# Title and description
st.title("Heart Disease Prediction App")
st.write("Enter your health parameters to predict heart disease risk")


male = st.radio("Gender", ["Male", "Female"], format_func=lambda x: "Male" if x == "Male" else "Female")
age = st.number_input("Age", min_value=20, max_value=100, value=40)
education = st.slider("Education Level", min_value=1, max_value=4, value=2, 
                     help="1: Some High School, 2: High School/GED, 3: Some College, 4: College Graduate")
currentSmoker  = st.radio("Current Smoker", ["Yes", "No"])
cigsPerDay  = st.number_input("Cigarettes Per Day", min_value=0, max_value=100, value=0)
BPMeds  = st.radio("Blood Pressure Medication", ["Yes", "No"])
prevalentStroke  = st.radio("History of Stroke", ["Yes", "No"])
prevalentHyp  = st.radio("Hypertension", ["Yes", "No"])
diabetes  = st.radio("Diabetes", ["Yes", "No"])
totChol  = st.number_input("Total Cholesterol (mg/dL)", min_value=100, max_value=600, value=200)
sysBP  = st.number_input("Systolic Blood Pressure (mmHg)", min_value=90, max_value=200, value=120)
diaBP  = st.number_input("Diastolic Blood Pressure (mmHg)", min_value=60, max_value=130, value=80)
BMI  = st.number_input("BMI", min_value=15.0, max_value=50.0, value=25.0, step=0.1)
heartRate  = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=75)
glucose  = st.number_input("Glucose Level (mg/dL)", min_value=40, max_value=400, value=100)


columns =['male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes','totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose']
row = np.array([male, age, education, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes,totChol, sysBP, diaBP, BMI, heartRate, glucose]) 
x = pd.DataFrame([row], columns=columns)

x['male'].replace({'Male': 1, 'Female': 0}, inplace=True)
x.replace({'Yes': 1, 'No': 0}, inplace=True)


scaler = StandardScaler()
df = scaler.fit_transform(x)


def predict():
    prediction = model.predict(df)
    
    if prediction[0] == 1:
        st.warning("High Risk of Heart Disease")
    else:
        st.success("Low Risk of Heart Disease")
    st.write("Probability of Heart Disease:", model.predict_proba(df)[0][1])
    st.write("Probability of No Heart Disease:", model.predict_proba(df)[0][0])

    
# Add information section
with st.expander("About this app"):
    st.write(
    "This app predicts the 10-year risk of coronary heart disease (CHD) based on various health parameters."
    'The prediction model uses machine learning to analyze your input and provide a risk assessment.'
    
    'Please note that this is not a substitute for professional medical advice.'
    'Always consult with healthcare professionals for medical decisions.'
    )

# Add footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit")

trigger = st.button('Predict', on_click=predict)