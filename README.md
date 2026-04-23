# 🚀 AI Career Recommendation System

## 👋 About the Project

Choosing a career can be confusing when you have multiple skills and interests.  
This project is built to help solve that problem using **Machine Learning**.

It recommends a suitable career based on your **skills, interests, and education level** in a simple and intelligent way.

---

## 💡 What this project does

- Takes user input like skills, interest, and education
- Uses Machine Learning + NLP to understand the input
- Predicts the most suitable career path
- Displays results instantly in a web app

---

## 🎯 Example

**Input:**
- Skills: python ml data analysis  
- Interest: ai  
- Education: ug  

**Output:**
- Recommended Career: Data Scientist  

---

## 🛠 Tech Stack

- Python  
- Pandas  
- Scikit-learn  
- NLP (TF-IDF)  
- Streamlit  

---

## 🧠 How it works

1. A dataset of skills and careers is created  
2. Text data is converted into numerical form using TF-IDF  
3. A Machine Learning model is trained on this data  
4. When a user enters input, the model predicts the closest matching career  

---

 ## 📁 Project Structure


career-recommendation/
│── app.py # Web application (Streamlit)
│── model.py # Model training code
│── data.csv # Dataset
│── vectorizer.pkl # NLP vectorizer
│── model.pkl # Trained ML model
│── le_career.pkl # Label encoder


---

## 🚀 How to Run

```bash
git clone https://github.com/your-username/career-recommendation-ml.git
cd career-recommendation-ml
pip install -r requirements.txt
streamlit run app.py

📌 What I learned

Machine Learning model training
NLP using TF-IDF
Building web apps with Streamlit
Connecting ML models with UI
Using Git & GitHub for project management