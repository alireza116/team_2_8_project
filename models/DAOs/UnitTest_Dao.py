import unittest
from models.DAOs import BedsDao
from models.DAOs import PlacesDao
from models.Resources import beds
from models.Resources import places


class TestBedsDao(unittest.TestCase):

    def setUp(self):
        self.new = BedsDao.BedDao()
        self.bed_id = 40
        self.guest_id = 35
        self.new_guest_id = 36
        self.placeid = 12
        self.availability = 1
        self.bed = beds.Bed(self.bed_id, self.guest_id, self.placeid, self.availability)

    def test_createNewBed(self):

        self.assertEqual(self.bed.bed_id, self.bed_id)

    def test_getBeds(self):
        self.assertGreater(len(self.new.getBeds(self.placeid)), 0)

    def test_getAvailableBeds(self):
        self.assertGreater(len(self.new.getAvailableBeds(self.placeid)), 0)

    def test_setNewGuest(self):
        self.assertEqual(self.new.setNewGuest(self.bed_id, self.new_guest_id), True)

    def test_removeGuest(self):
        self.assertEqual(self.new.removeGuest(self.bed_id), True)


class TestPlacesDao(unittest.TestCase):

    def setUp(self):
        self.new = PlacesDao.PlaceDao()
        self.id = 37
        self.name = "TestName"
        self.address = "TestAddress"
        self.X = 39
        self.Y = 48
        self.place = places.Place(self.id, self.name, self.address, self.X, self.Y)

    def test_createNewPlace(self):
        self.assertEqual(self.place, True)

    def test_getPlaces(self):
        self.assertEqual(self.new.getPlaces(), True)

    def test_getPlaceCounts(self):
        self.assertEqual(self.new.getPlaceCounts(), True)

if __name__ == '__main__':
    unittest.main()
