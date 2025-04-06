from flask import Flask, render_template, request
import joblib

# Load the trained model
model = joblib.load("sentiment_model.pkl")

app = Flask(__name__)

# Mapping model output to human-readable labels
sentiment_mapping = {
    1: "Positive",
    0: "Neutral",
    -1: "Negative"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == "POST":
        sentence = request.form.get("sentence")
        if sentence:
            pred = model.predict([sentence])[0]
            prediction = sentiment_mapping.get(pred, "Unknown")
    return render_template("index.html", prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5020)