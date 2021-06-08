from flask import Flask, jsonify, request

# Different functions for different plant types are imported here from plant folder

from plants.tomato import tomato
from plants.apple import apple
from plants.aloevera import aloevera
from plants.beans import beans
from plants.citrus import citrus
from plants.coffee import coffee
from plants.grape import grape
from plants.grass import grass
from plants.potato import potato
from plants.rice import rice

#strting of an flask application

app = Flask(__name__)


@app.route('/predict', methods=["POST"])
def predict():
    request_data = request.get_json()
    planttype = request_data['type']
    imageString = request_data['img']

    print(planttype)

    prediction = ''

    if planttype == 'Tomato':
        prediction = tomato(imageString)

    elif planttype == 'Apple':
        prediction = apple(imageString)

    elif planttype == 'Corn' or planttype == 'Jowar':
        prediction = grass(imageString)

    elif planttype == 'Potato':
        prediction = potato(imageString)

    elif planttype == 'Grape':
        prediction = grape(imageString)

    elif planttype == 'Rice':
        prediction = rice(imageString)

    elif planttype == 'Lemon' or planttype == 'Orange' or planttype == 'Sweet Lemon':
        prediction = citrus(imageString)

    elif planttype == 'Black Eyed Beans' or planttype == 'Mung Beans' or planttype == 'Cluster Beans':
        prediction = beans(imageString)

    elif planttype == 'Coffee':
        prediction = coffee(imageString)

    elif planttype == 'Aloe Vera':
        prediction = aloevera(imageString)

    print(prediction)
    return prediction


if __name__ == '__main__':
    app.debug = true
    app.run(host="0.0.0.0", port="8080")
