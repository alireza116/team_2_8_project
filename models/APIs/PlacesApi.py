from models.DAOs import PlacesDao
from models.Resources import places

class PlaceAPI():
    def __init__(self):
        self._place_Dao = PlacesDao.PlaceDao()

    def createNewPlace(self,id,name, address, X, Y):
        newPlace = places.Place(id,name,address, X,Y)
        return newPlace

    def saveNewPlace(self, newPlace):

        result = self._place_Dao.createNewPlace(newPlace)
        return result

    def getPlaces(self):
        result = self._place_Dao.getPlaces()
        return result

    def getPlaceCounts(self):
        result = self._place_Dao.getPlaceCounts()
        return result

