import streamlit as st
from predict_diabetes import show_predict_diabetes
from predict_heart import show_predict_heart

st.set_page_config(page_title="Disease Prediction", page_icon="🩺", layout="wide")

st.sidebar.title("Disease Prediction System")
st.sidebar.write("Choose the disease to predict from the menu below:")

menu = st.sidebar.selectbox("Select a Disease", ["Diabetes", "Heart Disease"])

if menu == "Diabetes":
    show_predict_diabetes()
elif menu == "Heart Disease":
    show_predict_heart()
