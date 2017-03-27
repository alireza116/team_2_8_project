from flask import Flask, jsonify, send_file
from models.APIs import PlacesApi
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return send_file("templates/index.html")

@app.route('/place', methods=["GET"])
def getPlaces():
    api = PlacesApi.PlaceAPI()
    places = api.getPlaces()
    print("done!")
    return jsonify(places)

if __name__ == '__main__':
    app.run(debug=True)
