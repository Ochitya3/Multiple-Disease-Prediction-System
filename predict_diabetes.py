import streamlit as st
import pickle
import numpy as np

def load_model():
    return pickle.load(open('diabetes_model.sav', 'rb'))

model = load_model()

def show_predict_diabetes():
    st.title("Diabetes Prediction")

    st.write("### Predict diabetes by providing the following information:")

    form_key = "diabetes_form"
    with st.form(form_key, clear_on_submit=True):
        name = st.text_input("Patient Name (required):")
        pregnancy = st.slider("Pregnancies", 0, 20, 0)
        glucose = st.number_input("Glucose Level", min_value=0.0, step=1.0)
        pressure = st.number_input("Blood Pressure", min_value=0.0, step=1.0)
        thickness = st.number_input("Skin Thickness", min_value=0.0, step=1.0)
        insulin = st.number_input("Insulin Level", min_value=0.0, step=1.0)
        bmi = st.number_input("BMI", min_value=0.0, step=0.1)
        function = st.number_input("Diabetes Pedigree Function", min_value=0.0, step=0.01)
        age = st.slider("Age", 0, 150, 18)

        submitted = st.form_submit_button("Predict Diabetes")

        if submitted:
            if not name.strip():
                st.error("Patient Name is required. Please fill it in before proceeding.")
            else:
                input_data = np.array([pregnancy, glucose, pressure, thickness, insulin, bmi, function, age])
                input_data_reshaped = input_data.reshape(1, -1)

                prediction = model.predict(input_data_reshaped)

                if prediction[0] == 0:
                    st.success(f"{name} is not diabetic.")
                else:
                    st.error(f"{name} is diabetic.")

show_predict_diabetes()
