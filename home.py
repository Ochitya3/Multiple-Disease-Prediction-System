import streamlit as st
from predict_diabetes import show_predict_diabetes
from predict_heart import show_predict_heart

def main():
    if "page" not in st.session_state:
        st.session_state.page = "home"
    
    if st.session_state.page == "home":
        st.title("Welcome to HealthScope 🩺")
        st.subheader("Your one-stop solution for disease prediction!")
        st.write(
            """
            **HealthScope** provides tools to predict diseases based on patient data.  
            Select a disease below to start the prediction process.
            """
        )

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🩺 Diabetes Prediction"):
                st.session_state.page = "diabetes"
        with col2:
            if st.button("❤️ Heart Disease Prediction"):
                st.session_state.page = "heart"

    elif st.session_state.page == "diabetes":
        st.button("⬅️ Back to Home", on_click=lambda: st.session_state.update(page="home"))
        show_predict_diabetes()

    elif st.session_state.page == "heart":
        st.button("⬅️ Back to Home", on_click=lambda: st.session_state.update(page="home"))
        show_predict_heart()

if __name__ == "__main__":
    main()
