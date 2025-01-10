import streamlit as st
import pickle
import numpy as np

def load_model():
    return pickle.load(open("heart_disease_model.sav", "rb"))


model = load_model()

def show_predict_heart():
    st.title("Heart Disease Prediction")

    st.write("### Predict heart disease by providing the following information:")

    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    with st.form("heart_disease_form", clear_on_submit=True):
        name = st.text_input("Patient Name (required):")
        age = st.slider("Age", 0, 120, 30)
        sex = st.selectbox("Sex", ["Male", "Female"])
        cp = st.selectbox("Chest Pain Type (CP)", [0, 1, 2, 3])
        pressure = st.number_input(
            "Resting Blood Pressure (mmHg)", min_value=0, max_value=250, value=120
        )
        cholesterol = st.number_input(
            "Serum Cholesterol (mg/dL)", min_value=0, max_value=600, value=200
        )
        fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
        restecg = st.selectbox("Resting Electrocardiographic Results", [0, 1, 2])
        max_hr = st.number_input(
            "Maximum Heart Rate Achieved", min_value=0, max_value=250, value=150
        )
        exercise_angina = st.selectbox("Exercise-Induced Angina", [0, 1])
        oldpeak = st.number_input(
            "ST Depression Induced by Exercise", value=1.0, step=0.1
        )
        slope = st.selectbox("Slope of the Peak Exercise ST Segment", [0, 1, 2])
        ca = st.selectbox(
            "Number of Major Vessels Colored by Fluoroscopy (0-4)", [0, 1, 2, 3, 4]
        )
        thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

        submitted = st.form_submit_button("Predict Heart Disease")

        if submitted:
            if not name.strip():
                st.error(
                    "Patient Name is required. Please fill it in before proceeding."
                )
            else:
                sex_numeric = 1 if sex == "Male" else 0
                input_data = np.array(
                    [
                        age,
                        sex_numeric,
                        cp,
                        pressure,
                        cholesterol,
                        fasting_bs,
                        restecg,
                        max_hr,
                        exercise_angina,
                        oldpeak,
                        slope,
                        ca,
                        thal,
                    ]
                )
                input_data_reshaped = input_data.reshape(1, -1)
                prediction = model.predict(input_data_reshaped)

                if prediction[0] == 0:
                    st.success(f"{name} is unlikely to have heart disease.")
                else:
                    st.error(f"{name} is likely to have heart disease.")

show_predict_heart()
