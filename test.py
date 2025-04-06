# test.py
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

# Load test data
test_data = pd.read_csv("dataset/test.tsv", sep="\t")
X_test = test_data["tweet"]
y_test = test_data["label"]

# Load the trained model
model = joblib.load("sentiment_model.pkl")

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions
print("Accuracy on twitter data: {:.2f}%".format(accuracy * 100))
