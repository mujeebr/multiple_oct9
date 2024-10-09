import streamlit as st
import joblib
st.title("House prediction app")
st.image("naresh_it.jpeg")

House_size=st.number_input("Please enter House Size:")
Bedrooms=st.number_input('Please enter No of Bedrooms:')

model = joblib.load("mul_lin.pkl")

if st.button("Predict"):
    output= model.predict([[House_size,Bedrooms]])
    st.write(f"The price of the house is {output[0]}")


