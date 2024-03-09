import streamlit as st
from tensorflow.keras.utils import img_to_array, load_img
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

model_path = 'model/model.h5'
model = tf.keras.models.load_model(model_path)

class_names = ['no','yes']

st.set_page_config(page_title="Brain Tumor Detection")

st.header("🧠Brain Tumor Detection")
st.text("It's Just a prediction 💁‍♂️, Trust Doctor 🧑‍⚕️")

#sidebar in streamlit
with st.sidebar:
    #add a title for sidebar
    st.header('Brain Tumor Detection using CNN')
    st.markdown("##### BE-final year project 2023-24")
    
def proccess(img1):
    img = tf.keras.preprocessing.image.load_img(
        img1, target_size=(180,180)
    )
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    pred = class_names[np.argmax(score)]
    score1 = 100 * np.max(score)

    return pred, score1


    
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
        
    st.image(uploaded_file, caption='Uploaded Image', width=200)

    


submit = st.button("Analyze")

if submit:
    response = proccess(uploaded_file)
    st.text("Prediction is: ")
    st.text(response)