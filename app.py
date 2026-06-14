from flask import Flask, render_template, request
from predict import predict_digit
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    digit, confidence, top_predictions = predict_digit(filepath)

    return render_template(
    "result.html",
    digit=digit,
    confidence=round(confidence, 2),
    image=filepath,
    top_predictions=top_predictions
)

if __name__ == "__main__":
    app.run(debug=True)