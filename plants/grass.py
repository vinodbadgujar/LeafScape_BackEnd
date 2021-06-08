import base64
import matplotlib.pyplot as plt
import cv2
import numpy as np
import io
from PIL import Image
from keras.models import load_model
from flask.json import jsonify

model = load_model("trained_ml_models/grass.h5")

diseaseNames = {
    "[0]": "GrayLeafSpot",
    "[1]": "CommonRust",
    "[2]": "NorthernLeafBlight",
    "[3]": "Healthy",
}


def grass(imageString):

    image = base64.b64decode((imageString))
    image = np.array(Image.open(io.BytesIO(image)))

    input_im = cv2.resize(image, (224, 224), interpolation=cv2.INTER_LINEAR)
    input_im = input_im / 255.
    input_im = input_im.reshape(1, 224, 224, 3)
    pred = model.predict(input_im, 1, verbose=0)

    score = pred.max()
    score = score * 100

    res = np.argmax(pred, axis=1)
    disease = diseaseNames[str(res)]

    return jsonify({
        "diseaseName": disease,
        "conf": score,
    })
