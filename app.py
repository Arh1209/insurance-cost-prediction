import streamlit as st
import pandas as pd
import joblib

model = joblib.load("insurance_model.pkl")

st.set_page_config(
    page_title="Medical Insurance Cost Predictor",
    page_icon="🏥"
)

st.title("🏥 Medical Insurance Cost Predictor")

st.write(
    "Enter patient details to predict estimated medical insurance charges."
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

sex = st.selectbox(
    "Sex",
    ["female", "male"]
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0,
    step=0.1
)

children = st.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0
)

smoker = st.selectbox(
    "Smoker",
    ["no", "yes"]
)

region = st.selectbox(
    "Region",
    [
        "northeast",
        "northwest",
        "southeast",
        "southwest"
    ]
)

if st.button("Predict Insurance Charges"):

    customer = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })

    prediction = model.predict(customer)[0]

    st.success(
        f"Estimated Insurance Charges: ${prediction:,.2f}"
    )