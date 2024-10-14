import streamlit as st
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image
import numpy as np

# Load pre-trained MobileNetV2 model
model = MobileNetV2(weights="imagenet")

# Streamlit app title
st.title("Image Classification with MobileNetV2")

# Upload image through Streamlit
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open and display the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Preprocess the image
    img = image.resize((224, 224))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    
    # Make predictions
    preds = model.predict(img)
    
    # Decode the predictions
    decoded_preds = decode_predictions(preds, top=3)[0]
    
    # Display the predictions
    st.write("Predictions:")
    for i, (imagenet_id, label, score) in enumerate(decoded_preds):
        st.write(f"{i + 1}. {label}: {score:.4f}")

