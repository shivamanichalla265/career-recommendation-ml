import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
data = pd.read_csv("data.csv")

# Combine features into one text
data['text'] = data['skills'] + " " + data['interest'] + " " + data['education']

# Convert text → numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['text'])

# Encode output
le_career = LabelEncoder()
y = le_career.fit_transform(data['career'])

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save everything
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
pickle.dump(le_career, open("le_career.pkl", "wb"))

print("Smart model trained successfully!")