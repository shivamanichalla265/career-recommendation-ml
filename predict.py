import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
le_skill = pickle.load(open("le_skill.pkl", "rb"))
le_interest = pickle.load(open("le_interest.pkl", "rb"))
le_edu = pickle.load(open("le_edu.pkl", "rb"))
le_career = pickle.load(open("le_career.pkl", "rb"))

# Input
skills = "python;ml;statistics"
interest = "ai"
education = "ug"

# Convert input
skills_enc = le_skill.transform([skills])
interest_enc = le_interest.transform([interest])
edu_enc = le_edu.transform([education])

# Predict
prediction = model.predict([[skills_enc[0], interest_enc[0], edu_enc[0]]])

# Output
career = le_career.inverse_transform(prediction)

print("Recommended Career:", career[0])