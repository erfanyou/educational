import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import MinMaxScaler

model =joblib.load(r'E:\jupyter\educational-\exercise\Breast Cancer Wisconsin Diagnosis\pre_B_Cancer.joblib')

# Streamlit UI with improved design
st.set_page_config(page_title="Breast Cancer Prediction", page_icon="🩺", layout="centered")

# Custom styling
st.markdown(
    """
    <style>
        .main {background-color: #f0f2f6;}
        .stButton > button {background-color: #ff4b4b; color: white; font-size: 18px; border-radius: 10px;}
        .stTextInput, .stNumberInput {border-radius: 10px;}
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("🩺 Breast Cancer Prediction App")
st.write("### Enter the tumor characteristics below to predict whether it's **Malignant** or **Benign**.")

# Define input fields with two-column layout
columns = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
           'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave points_mean',
           'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se',
           'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se',
           'concave points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst',
           'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
           'compactness_worst', 'concavity_worst', 'concave points_worst',
           'symmetry_worst', 'fractal_dimension_worst']

input_data = []

col1, col2 = st.columns(2)
for i, col in enumerate(columns):
    with col1 if i % 2 == 0 else col2:
        value = st.number_input(f"{col.replace('_', ' ').title()}", value=0.0, format="%.4f")
        input_data.append(value)

input_df = pd.DataFrame([input_data], columns=columns)

scaler = MinMaxScaler()
input_df = scaler.fit_transform(input_df)

# Prediction button with styled result
if st.button("🔍 Predict"):
    prediction = model.predict(input_df)[0]
    result = "🩸 **Malignant (M)**" if prediction == "M" else "✅ **Benign (B)**"
    st.success(result)
    st.write("### Stay Healthy & Get Regular Check-ups! 🏥")
