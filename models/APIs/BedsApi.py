from models.DAOs import BedsDao
from models.Resources import beds

class BedsApi():
    def __init__(self):
        self._beds_Dao = BedsDao.BedDao()

    def createNewBed(self,bed_id, guest_id, placeid, availability):
        newBed = beds.Bed(bed_id, guest_id, placeid, availability)
        return newBed

    def saveNewBed(self, newBed):

        result = self._beds_Dao.createNewBed(newBed)
        return result

    def getBeds(self, place_id):
        result = self._beds_Dao.getBeds(place_id)
        return result

    def getAvailableBeds(self,place_id):
        result = self._beds_Dao.getBeds(place_id)
        return result

    def setNewGuest(self, bed_id, new_guest):
        result = self._beds_Dao.setNewGuest(bed_id, new_guest)
        return result

    def removeGuest(self, bed_id):
        result = self._beds_Dao.removeGuest(bed_id)
        return result



