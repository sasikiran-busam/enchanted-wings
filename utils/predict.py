import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import json

# Load model
model = load_model('model/enchanted-wings.h5')

# Load class labels
with open('model/class_indices.json', 'r') as f:
    class_indices = json.load(f)

# Reverse the dictionary to get index -> class
class_labels = {v: k for k, v in class_indices.items()}

def model_predict(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    pred_index = np.argmax(prediction)

    predicted_class = class_labels[pred_index]
    confidence = np.max(prediction)
    
    return f"{predicted_class} ({confidence*100:.2f}%)"
