import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load('tip_predictor.pkl')

# Title of the app
st.title('Tip Prediction App')

# Inputs for the features
total_bill = st.number_input("Total Bill (in $)", min_value=0.0, step=0.1)
sex = st.selectbox("Sex", ["Male", "Female"])
smoker = st.selectbox("Smoker?", ["No", "Yes"])
day = st.selectbox("Day", ["Thur", "Fri", "Sat", "Sun"])
time = st.selectbox("Time", ["Lunch", "Dinner"])
size = st.number_input("Size", min_value=1, step=1)

# Convert categorical inputs to numerical values
sex_value = 0 if sex == 'Male' else 1
smoker_value = 0 if smoker == 'No' else 1
day_value = {"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3}[day]
time_value = 0 if time == 'Lunch' else 1

# Prediction button
if st.button("Predict Tip"):
    # Create a numpy array for the model input
    features = np.array([[total_bill, sex_value, smoker_value, day_value, time_value, size]])

    # Predict the tip using the model
    predicted_tip = model.predict(features)[0]

    # Display the prediction
    st.write(f"The predicted tip is: ${predicted_tip:.2f}")

