import streamlit as st
import pickle
import numpy as np

with open("sales.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Sales Prediction",page_icon="📈",layout="centered")

st.title("📈Sales Prediction")
st.write("Predict the sales based on advertising expenditure.")

st.divider()

tv = st.number_input("TV Advertising Budget",min_value=0.0,value=150.0,step=1.0)

radio = st.number_input("Radio Advertising Budget",min_value=0.0,value=25.0,step=1.0)

newspaper = st.number_input("Newspaper Advertising Budget",min_value=0.0,value=20.0,step=1.0)

st.divider()

if st.button("Predict Sales", use_container_width=True):
    features = np.array([[tv, radio, newspaper]])
    prediction = model.predict(features)[0]
    st.success(f"Predicted Sales: {prediction:.2f}")