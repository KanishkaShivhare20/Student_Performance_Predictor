# Import libraries
import streamlit as st
import pandas as pd
import joblib

# Load model and preprocessing tools
model = joblib.load("artifacts/svc_model.pkl")
preprocessor = joblib.load("artifacts/preprocessor.pkl")
label_encoder = joblib.load("artifacts/label_encoder.pkl")


# Set custom page title and favicon
st.set_page_config(
    page_title="Student Grade Predictor",  # Tab title
    page_icon="🎓",                        # Favicon 
    layout="centered"                     
)

# App title
st.title("📊 Student Performance Predictor")
st.markdown("Enter the student details below to predict their academic grade.")

# Input form
gender = st.selectbox("Gender", ['male', 'female'])
lunch = st.selectbox("Lunch Type", ['standard', 'free/reduced'])
test_prep = st.selectbox("Test Preparation Course", ['completed', 'none'])
reading_score = st.slider("Reading Score", 0, 100, 70)
writing_score = st.slider("Writing Score", 0, 100, 70)

# Prepare input DataFrame
input_df = pd.DataFrame({
    'gender': [gender],
    'lunch': [lunch],
    'test_preparation_course': [test_prep],
    'reading_score': [reading_score],
    'writing_score': [writing_score]
})

# Select only trained features
input_features = input_df[['test_preparation_course', 'lunch', 'gender', 'writing_score', 'reading_score']]
X_input = preprocessor.transform(input_features)

# Predict button
if st.button("🎯 Predict Grade"):
    prediction = model.predict(X_input)
    predicted_label = label_encoder.inverse_transform(prediction)[0]
    st.success(f"🎓 Predicted Grade: **{predicted_label}**")
