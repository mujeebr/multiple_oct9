import streamlit as st
import numpy as np
import joblib
model = joblib.load("tips.pkl")

st.title("Tip Prediction Model")


total_bill=st.number_input("Please enter total_bill",min_value =0.0, step = 0.1) # 22
gender = st.selectbox("Sex",["Male","Female"]) # Male
smoker=st.selectbox("smoker",["Yes","No"]) # Yes
day=st.selectbox("day",["Thur","Fri","Sat","Sun"]) # Sun
time=st.selectbox("time",["Lunch","Dinner"]) # Dinner
size=st.number_input("Please enter the size",min_value=0,step =1) # 2

# gender = st.selectbox("Sex",["Male","Female"]) # Male
# smoker=st.selectbox("smoker",["Yes","No"]) # Yes
# day=st.selectbox("day",["Thur","Fri","Sat","Sun"]) # Sun
# time=st.selectbox("time",["Lunch","Dinner"]) # Dinner

gender_value = 0 if gender == "Male" else 1
smoker_value = 0 if smoker=="Yes" else 1
day_value = {"Thur":0, "Fri":1,"Sat":2,"Sun":3}[day]
time_value = 0 if time =="Lunch" else 1

if st.button("Predict"):
    result = model.predict([[total_bill,gender_value,smoker_value,day_value,time_value,size]])
    st.write(f"The predicted tip amount is ${result[0]:.2f}")