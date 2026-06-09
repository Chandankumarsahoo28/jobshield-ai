import pickle
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).parent
DATASET_PATH = BASE_DIR / "fake_job_postings.csv"

if not DATASET_PATH.exists():
    raise FileNotFoundError(
        "fake_job_postings.csv not found. Dataset file ko project folder me rakho."
    )

# Load dataset
df = pd.read_csv(DATASET_PATH)

required_columns = [
    "title",
    "company_profile",
    "description",
    "requirements",
    "benefits",
    "fraudulent",
]

missing = [col for col in required_columns if col not in df.columns]
if missing:
    raise ValueError(f"Dataset me ye columns missing hain: {missing}")

# Select useful columns and clean
df = df[required_columns].fillna("")

# Combine all important text fields
df["text"] = (
    df["title"].astype(str) + " " +
    df["company_profile"].astype(str) + " " +
    df["description"].astype(str) + " " +
    df["requirements"].astype(str) + " " +
    df["benefits"].astype(str)
)

X = df["text"]
y = df["fraudulent"].astype(int)

# Stronger NLP vectorizer
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=25000,
    ngram_range=(1, 2),
    min_df=2,
    sublinear_tf=True,
)

X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

# Logistic Regression works well for TF-IDF text classification
model = LogisticRegression(
    class_weight="balanced",
    max_iter=3000,
    C=2.0,
    solver="liblinear",
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, pred))

print("\nClassification Report:")
print(classification_report(y_test, pred))

with open(BASE_DIR / "model.pkl", "wb") as f:
    pickle.dump(model, f)

with open(BASE_DIR / "vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model and vectorizer saved successfully!")
