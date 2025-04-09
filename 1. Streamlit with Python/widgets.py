import streamlit as st
import pandas as pd
## Input Box
st.title("Streamlit Text Input")

name=st.text_input("Entre your Name")

if name: 
    st.write(f"Hello, {name}")

##Slider
age= st.slider("Select your age:",0,100,25)
st.write(f"Your age is {age}")

#Dropdown Menu
options=['Python', 'Java', 'C++', 'JavaScript']
choice= st.selectbox("Choose your favourite language:", options)
st.write(f"You selected {choice}")

##DataFrame or Table
data={
    "Name":["John","Jane","Jake","Jill"],
    "Age":[28,25,30,45],
    "City":["New York","Los Angeles","Chicago","Houston"]
}
df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

##Upload Button
uploaded_file= st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    st.write(df)

