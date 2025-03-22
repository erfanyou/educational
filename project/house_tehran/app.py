import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.base import BaseEstimator, TransformerMixin

# List of addresses in Tehran
addr=['Shahran', 'Pardis', 'Shahrake Qods', 'Shahrake Gharb',
        'North Program Organization', 'Andisheh', 'West Ferdows Boulevard',
        'Narmak', 'Saadat Abad', 'Zafar', 'Islamshahr', 'Pirouzi',
        'Shahrake Shahid Bagheri', 'Moniriyeh', 'Velenjak', 'Amirieh',
        'Southern Janatabad', 'Salsabil', 'Zargandeh', 'Feiz Garden',
        'Water Organization','ShahrAra', 'Gisha', 'Ray', 'Abbasabad',
        'Ostad Moein', 'Farmanieh', 'Parand', 'Punak', 'Qasr-od-Dasht',
        'Aqdasieh', 'Pakdasht', 'Railway', 'Central Janatabad',
        'East Ferdows Boulevard', 'Pakdasht KhatunAbad', 'Sattarkhan',
        'Baghestan', 'Shahryar', 'Northern Janatabad', 'Daryan No',
        'Southern Program Organization', 'Rudhen', 'West Pars', 'Afsarieh',
        'Marzdaran', 'Dorous', 'Sadeghieh', 'Chahardangeh', 'Baqershahr',
        'Jeyhoon', 'Lavizan', 'Shams Abad', 'Fatemi',
        'Keshavarz Boulevard', 'Kahrizak', 'Qarchak',
        'Northren Jamalzadeh', 'Azarbaijan', 'Bahar',
        'Persian Gulf Martyrs Lake', 'Beryanak', 'Heshmatieh',
        'Elm-o-Sanat', 'Golestan', 'Shahr-e-Ziba', 'Pasdaran',
        'Chardivari', 'Gheitarieh', 'Kamranieh', 'Gholhak', 'Heravi',
        'Hashemi', 'Dehkade Olampic', 'Damavand', 'Republic', 'Zaferanieh',
        'Qazvin Imamzadeh Hassan', 'Niavaran', 'Valiasr', 'Qalandari',
        'Amir Bahador', 'Ekhtiarieh', 'Ekbatan', 'Absard', 'Haft Tir',
        'Mahallati', 'Ozgol', 'Tajrish', 'Abazar', 'Koohsar', 'Hekmat',
        'Parastar', 'Lavasan', 'Majidieh', 'Southern Chitgar', 'Karimkhan',
        'Si Metri Ji', 'Karoon', 'Northern Chitgar', 'East Pars', 'Kook',
        'Air force', 'Sohanak', 'Komeil', 'Azadshahr', 'Zibadasht',
        'Amirabad', 'Dezashib', 'Elahieh', 'Mirdamad', 'Razi', 'Jordan',
        'Mahmoudieh', 'Shahedshahr', 'Yaftabad', 'Mehran', 'Nasim Shahr',
        'Tenant', 'Chardangeh', 'Fallah', 'Eskandari', 'Shahrakeh Naft',
        'Ajudaniye', 'Tehransar', 'Nawab', 'Yousef Abad',
        'Northern Suhrawardi', 'Villa', 'Hakimiyeh', 'Nezamabad',
        'Garden of Saba', 'Tarasht', 'Azari', 'Shahrake Apadana', 'Araj',
        'Vahidieh', 'Malard', 'Shahrake Azadi', 'Darband', 'Vanak',
        'Tehran Now', 'Darabad', 'Eram', 'Atabak', 'Sabalan', 'SabaShahr',
        'Shahrake Madaen', 'Waterfall', 'Ahang', 'Salehabad', 'Pishva',
        'Enghelab', 'Islamshahr Elahieh', 'Ray - Montazeri',
        'Firoozkooh Kuhsar', 'Ghoba', 'Mehrabad', 'Southern Suhrawardi',
        'Abuzar', 'Dolatabad', 'Hor Square', 'Taslihat', 'Kazemabad',
        'Robat Karim', 'Ray - Pilgosh', 'Ghiyamdasht', 'Telecommunication',
        'Mirza Shirazi', 'Gandhi', 'Argentina', 'Seyed Khandan',
        'Shahrake Quds', 'Safadasht', 'Khademabad Garden', 'Hassan Abad',
        'Chidz', 'Khavaran', 'Boloorsazi', 'Mehrabad River River',
        'Varamin - Beheshti', 'Shoosh', 'Thirteen November', 'Darakeh',
        'Aliabad South', 'Alborz Complex', 'Firoozkooh', 'Vahidiyeh',
        'Shadabad', 'Naziabad', 'Javadiyeh', 'Yakhchiabad']


# Columns used for prediction
columns = ['Area', 'Room', 'Parking', 'Warehouse', 'Elevator', 'Address']

# Load pre-trained model
model = joblib.load(r'F:\jupyter\educational-\exercise\house_tehran\pre_price.joblib')

# Streamlit app
st.title('lets go to predict your price of house:')

# Input widgets
Area = st.number_input("Input Area ", 0, 100000)
Room = st.slider("Choose number Room", 0, 10)
Parking = st.select_slider("you have Parking?", [0, 1])
warehouse = st.select_slider("you have Warehouse?", [0, 1])
Elevator = st.select_slider("you have Elevator?", [0, 1])
Address = st.text_input("Input your Address", "pasdaran") 

def predict():
    # Create DataFrame from user inputs
    row = np.array([Area, Room, Parking, warehouse, Elevator, Address]) 
    X = pd.DataFrame([row], columns=columns)

    # Explicitly convert columns to appropriate numeric types
    X['Area'] = pd.to_numeric(X['Area'], errors='coerce')
    X['Room'] = pd.to_numeric(X['Room'], errors='coerce')
    X['Parking'] = pd.to_numeric(X['Parking'], errors='coerce')
    X['Warehouse'] = pd.to_numeric(X['Warehouse'], errors='coerce')
    X['Elevator'] = pd.to_numeric(X['Elevator'], errors='coerce')

    # Prepare the one-hot encoded columns
    # Create a full DataFrame with all possible address columns, initialized to 0
    full_columns = model.feature_names_in_.tolist()
    
    # Remove the original feature columns
    base_columns = ['Area', 'Room', 'Parking', 'Warehouse', 'Elevator']
    address_columns = [col for col in full_columns if col not in base_columns]
    
    # Create a DataFrame with all zeros for all expected columns
    X_encoded = pd.DataFrame(0, index=X.index, columns=full_columns)
    
    # Copy the numeric features
    for col in base_columns:
        X_encoded[col] = X[col]
    
    # Set the correct address column to 1
    if Address in address_columns:
        X_encoded[Address] = 1
    
    # Ensure all columns are numeric
    X_encoded = X_encoded.apply(pd.to_numeric, errors='coerce')

    # Make prediction
    prediction = model.predict(X_encoded)
    st.write(f"Predicted House Price: {prediction[0]:,.0f} IRR")# Prediction button
trigger = st.button('Predict', on_click=predict)