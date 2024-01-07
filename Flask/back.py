from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from PIL import Image
import io
from keras.models import load_model
import cv2

app = Flask(__name__)
CORS(app)

# Download Model From: "https://drive.google.com/file/d/13Ny-GL51Il_JluJ1btWggX2YE9lCSbxn/view?usp=drive_link"
model = load_model('BrainModel.h5')
class_dict = {0:'glioma tumor', 1:'meningioma tumor', 2:"normal", 3:"pituitary_tumor"}

def preprocess_image(image_bytes):
    npimg = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (256, 256))
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    return image

@app.route("/predict", methods=['POST'])
def predict_image():
    if 'image' in request.files:
        image_file = request.files['image']
        image_bytes = image_file.read()

        processed_image = preprocess_image(image_bytes)

        prediction = model.predict(processed_image)

        prediction_list = prediction.tolist()
        prediction_class = np.argmax(prediction_list)
        prediction_result = class_dict[prediction_class]
        print("____", prediction_result)

        return jsonify({"prediction": prediction_result})
    else:
        return "No image found in the request", 400

if __name__ == "__main__":
    app.run()