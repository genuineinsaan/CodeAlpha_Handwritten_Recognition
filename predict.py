from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

model = load_model("model/handwritten_model.keras")

def predict_digit(image_path):

    img = Image.open(image_path).convert('L')

    img = ImageOps.invert(img)

    img = img.resize((28, 28))

    img = np.array(img)

    img = img.astype("float32") / 255.0

    img = img.reshape(1, 28, 28, 1)

    prediction = model.predict(img, verbose=0)[0]

    digit = int(np.argmax(prediction))

    confidence = float(np.max(prediction) * 100)

    top_indices = np.argsort(prediction)[::-1][:3]

    top_predictions = []

    for idx in top_indices:

        top_predictions.append({
            "digit": int(idx),
            "confidence": round(float(prediction[idx] * 100), 2)
        })

    return digit, confidence, top_predictions