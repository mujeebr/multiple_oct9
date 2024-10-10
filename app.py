import streamlit as st
import joblib
import numpy as np
st.title("House prediction app")
st.image("naresh_it.jpeg")

House_size=st.number_input("Please enter House Size:")
Bedrooms=st.number_input('Please enter No of Bedrooms:')

model = joblib.load("mul_linear.pkl")

if st.button("Predict"):
    features = np.array([[House_size,Bedrooms]])
    output= model.predict(features)
    st.write(f"The price of the house is {output[0]}")