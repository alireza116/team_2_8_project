from flask import Flask, jsonify
from models.APIs import PlacesApi
from flask.ext.cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/place', methods=["GET"])
def getPlaces():
    api = PlacesApi.PlaceAPI()
    places = api.getPlaces()
    print("done!")
    return jsonify(places)

if __name__ == '__main__':
    app.run(debug=True)
