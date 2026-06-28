import sys
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((36, 36))
    img_array = np.asarray(img) 
    img_array = img_array.reshape((1, 36, 36, 3)) 
    img_array = img_array / 255.0
    return img_array

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python predict_malaria.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]

    try:
        # Preprocess the image
        img_array = preprocess_image(image_path)

        # Load the model
        model = load_model("./aimodels/malaria.h5")

        # Make a prediction
        prediction = model.predict(img_array)[0]

        # Interpret the prediction
        class_labels = ["No Malaria", "Malaria"]
        predicted_class = np.argmax(prediction)  # Get the index of the highest probability
        confidence = prediction[predicted_class]  # Get the confidence of the predicted class

        print(f"Prediction: {class_labels[predicted_class]} (Confidence: {confidence:.2f})")
    except Exception as e:
        print("Error:", e)
        sys.exit(1)