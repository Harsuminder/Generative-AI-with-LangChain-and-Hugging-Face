import pandas as pd
import numpy as np
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Making function to load data set and extract features
@st.cache
def load_data():
    iris=load_iris()
    df=pd.DataFrame(iris.data, columns=iris.feature_names)
    X=iris.data
    y=iris.target
    y_names= iris.target_names
    return df,X, y, y_names

#retrieve values
df,X, target_values, target_names= load_data()

#Model 
model= RandomForestClassifier()
model.fit(X, target_values) # model.fit(x,y)

#Slider
sepal_length=st.sidebar.slider("Sepal length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width=st.sidebar.slider("Sepal Width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length=st.sidebar.slider("Petal length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width=st.sidebar.slider("Petal width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

#Save the input in form of list, will be used for prediction
input= [[sepal_length, sepal_width,petal_length, petal_width]]

# Prediction
prediction= model.predict(input)

#Mapping with species name
predicted_species= target_names[prediction[0]]

# Display Result
st.write("Prediction")
st.write(f"The predicted species is: {predicted_species}")