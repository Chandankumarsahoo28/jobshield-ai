import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("fake_job_posting.csv")

# Select columns
df = df[['title', 'company_profile', 'description',
         'requirements', 'benefits', 'fraudulent']]

# Fill missing values
df = df.fillna('')

# Combine text
df['text'] = (
    df['title'] + ' ' +
    df['company_profile'] + ' ' +
    df['description'] + ' ' +
    df['requirements'] + ' ' +
    df['benefits']
)

# Features and labels
X = df['text']
y = df['fraudulent']

# TF-IDF
vectorizer = TfidfVectorizer(
    stop_words='english',
    max_features=15000,
    ngram_range=(1,2)
)

X = vectorizer.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Model
model = RandomForestClassifier(
    n_estimators=300,
    class_weight='balanced',
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

print(classification_report(y_test, pred))

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model Saved Successfully")