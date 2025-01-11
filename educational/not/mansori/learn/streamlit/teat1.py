import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

#----------------------------------------

st.text("Text : This is Soheil Tehranipour")

st.write("Write : This is Soheil Tehranipour")

st.markdown("# This is Heading")

st.title("This is Title")

st.sidebar.header('User Input Parameters')


st.latex(r'''
...     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
...     \sum_{k=0}^{n-1} ar^k =
...     a \left(\frac{1-r^{n}}{1-r}\right)
...     ''')

#-------------------------------------------------
df = pd.read_csv("F:\jupyter\educational-\educational\csv\mansori\Iris.csv")
st.dataframe(df)
# st.table(df)

#-------------------------------------------------
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()
#-------------------------------------------------
st.subheader('User Input parameters')
st.write(df)
#-------------------------------------------------
iris = datasets.load_iris()
X = iris.data
Y = iris.target
#-------------------------------------------------
clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)
#-------------------------------------------------
st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)
#-------------------------------------------------
st.subheader('Prediction')
st.write(iris.target_names[prediction])
st.write(prediction)
#-------------------------------------------------
st.subheader('Prediction Probability')
st.write(prediction_proba)
#-------------------------------------------------
import time
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
#-------------------------------------------------
from PIL import Image
photo = Image.open(r"F:\jupyter\educational-\educational\not\mansori\learn\reg\drugtree.png")
st.image(photo)
#-------------------------------------------------
st.error("Error Message")

st.warning("Warning")

st.success("Success")
#-------------------------------------------------
st.button('Click here')

st.checkbox("Check1")
st.checkbox("Check2")
st.checkbox("Check3")
st.checkbox("Check4")

st.radio("RADIO",[1,2,3,4,5,6])

st.slider("Slide me",10,100)

st.file_uploader("Upload:.......")

st.color_picker("COLOR")