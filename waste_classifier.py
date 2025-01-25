import tensorflow as tf
import numpy as np
from PIL import Image
import requests
import os

# Pre-trained model download URL (replace with an actual URL of a pre-trained waste model)
MODEL_URL = "https://github.com/pedropro/TACO/releases/download/v1.0/waste_model.h5"
MODEL_PATH = "waste_model.h5"

# Download the model if it's not already in the working directory
if not os.path.exists(MODEL_PATH):
    print("Downloading the pre-trained waste classification model...")
    response = requests.get(MODEL_URL)
    with open(MODEL_PATH, "wb") as f:
        f.write(response.content)
    print("Model downloaded!")

# Load the pre-trained model
model = tf.keras.models.load_model(MODEL_PATH)

# Define the waste categories based on the model's training dataset
categories = [
    "Glass", "Plastic", "Metal", "Paper", "Organic", "E-waste", "Others"
]

def preprocess_image(image_path):
    """
    Preprocess the image to match the model's input requirements.
    :param image_path: Path to the image
    :return: Preprocessed image array
    """
    img = Image.open(image_path).resize((224, 224))  # Resize to model's input size
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

def classify_waste(image_path):
    """
    Classify the waste type from the input image.
    :param image_path: Path to the image
    :return: Predicted waste type and confidence score
    """
    # Preprocess the image
    img_array = preprocess_image(image_path)

    # Perform prediction
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions, axis=1)[0]
    confidence = predictions[0][predicted_index]

    # Map to the waste category
    waste_type = categories[predicted_index]
    return waste_type, confidence
# Example usage
image_path = "path_to_your_image.jpg"  # Replace with the actual path to the waste image
waste_type, confidence = classify_waste(image_path)

print(f"Waste Type: {waste_type}")
print(f"Confidence: {confidence * 100:.2f}%")