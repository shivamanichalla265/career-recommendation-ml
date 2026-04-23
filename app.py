import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
le_career = pickle.load(open("le_career.pkl", "rb"))

st.title("AI Career Recommendation System")

# User input (FREE TEXT now)
skills = st.text_input("Enter your skills (e.g., python ml data analysis)")
interest = st.text_input("Enter your interest (ai, web, cloud, cybersecurity)")
education = st.selectbox("Education", ["ug", "pg"])

if st.button("Predict Career"):
    user_input = skills + " " + interest + " " + education

    # Convert input
    X_input = vectorizer.transform([user_input])

    # Predict
    prediction = model.predict(X_input)
    career = le_career.inverse_transform(prediction)

    st.success(f"Recommended Career: {career[0]}")