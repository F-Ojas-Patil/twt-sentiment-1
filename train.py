# train.py
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load training data (assuming tab separated values)
train_data = pd.read_csv("dataset/train.tsv", sep="\t")
X_train = train_data["tweet"]
y_train = train_data["label"]

# Build a simple pipeline: vectorizer + classifier
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', LogisticRegression(max_iter=1000))
])

# Train the model
pipeline.fit(X_train, y_train)

# Save the model to a file
joblib.dump(pipeline, "sentiment_model.pkl")
print("Model trained and saved as sentiment_model.pkl")
