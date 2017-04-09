from flask import Flask, jsonify, send_file, request
from models.APIs import PlacesApi, BedsApi
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

@app.route("/place", methods=["POST"])
def createNewPlace():
    try:
        placeApi = PlacesApi.PlaceAPI()
        data = request.json
        newPlace = placeApi.createNewPlace(data["placeid"], data["name"], data["address"],
                                           data["X"], data["Y"])
        result = placeApi.saveNewPlace(newPlace)
        return jsonify(result)
    except Exception as e:
        print(e)
        return "cant"

@app.route('/place/counts', methods=["GET"])
def getPlaceCounts():
    api = PlacesApi.PlaceAPI()
    placeCounts = api.getPlaceCounts()
    print("done!")
    return jsonify(placeCounts)

@app.route("/bed", methods=["GET"])
def getBeds():
    placeid = request.args["placeid"]
    print(placeid)
    api = BedsApi.BedsApi()
    beds = api.getBeds(placeid)
    return jsonify(beds)

@app.route("/bed/available", methods=["GET"])
def getAvailableBeds():
    placeid = request.args["placeid"]
    api = BedsApi.BedsApi()
    beds = api.getAvailableBeds(placeid)
    return jsonify(beds)

@app.route("/bed/reserve" , methods=["PUT"])
def setNewGuest():
    data = request.json
    bedsapi = BedsApi.BedsApi()
    result = bedsapi.setNewGuest(data["bed_id"],data["guest_id"])
    return jsonify(result)

@app.route("/bed/checkout" , methods=["PUT"])
def removeGuest():
    data = request.json
    bedsapi = BedsApi.BedsApi()
    result = bedsapi.removeGuest(data["bed_id"])
    return jsonify(result)

@app.route("/bed", methods=["POST"])
def createNewBed():
    data = request.json
    bedsapi = BedsApi.BedsApi()
    new_bed = bedsapi.createNewBed(data["bed_id"],data["guest_id"],data["placeid"],data["availability"])
    result = bedsapi.saveNewPlace(new_bed)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
