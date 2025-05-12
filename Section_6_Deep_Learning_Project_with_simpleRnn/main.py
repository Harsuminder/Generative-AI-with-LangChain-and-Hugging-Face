# Load Libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model



## Load IMDB dataset word index

word_index= imdb.get_word_index()
reverse_word_index= { value: key for key,value in word_index.items()}

## Load pre-trained model with ReLU activation

import os
model_path = r'D:\Datascience_projects\Github\GenAI\Generative-AI-with-LangChain-and-Hugging-Face\Section_6_Deep_Learning_Project_with_simpleRnn\simple_rnn.h5'
model = load_model(model_path)


# Step 2: Helper FInction


# Function to decode reviews

def decode_review (encoded_review):
    return(' '.join([reverse_word_index.get(i-3, '?') for i in sample_review]))

# Function to preprocess user input

def preprocess_text(text):
    words= text.lower().split()
    encoded_review= [word_index.get(word, 2) + 3 for word in words]
    paded_review= sequence.pad_sequences([encoded_review], maxlen=500)
    return paded_review

## Design Streamlit App

import streamlit as st

st.title('IMDB Moview Review Sentiment Analysis')
st.write('ENter a movie review to classify it as positive or negative.')

# User Input

user_input= st.text_area('Movie Review')

if st.button('Classify'):
    preprocessed_input= preprocess_text(user_input)

    ## Make Prediction
    prediction= model.predict(preprocessed_input)
    sentiment=  sentiment= 'Positive' if prediction[0][0]>0.5 else 'Negative'

    # Display the result
    st.write(f'Sentiment: {sentiment}')
    st.write(f'Prediction Score: {prediction[0][0]}')
else:
    st.write('Please enter a movie review.')
