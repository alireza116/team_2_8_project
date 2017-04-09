import unittest
from models.APIs import BedsApi
from models.APIs import PlacesApi
from models.resources import beds


class TestBedsApi(unittest.TestCase):

    def setup(self):
        self.new = BedsApi.BedsApi()
        self.bed_id = 40
        self.guest_id = 35
        self.new_guest_id = 36
        self.placeid = 12
        self.availability = 1

    def test_createNewBed(self):
        self.assertEqual(self.new.createNewBed(self.bed_id, self.guest_id, self.placeid, self.availability), True)

    def test_saveNewBed(self):
        testbed = beds.Bed(self.bed_id, self.guest_id, self.placeid, self.availability)
        self.assertEqual(self.new.saveNewBed(testbed), True)

    def test_getBeds(self):
        self.assertEqual(self.new.getBeds(self.placeid), True)

    def test_getAvailableBeds(self):
        self.assertEqual(self.new.getAvailableBeds(self.placeid), True)

    def test_setNewGuest(self):
        self.assertEqual(self.new.setNewGuest(self.bed_id, self.new_guest_id), True)

    def test_removeGuest(self):
        self.assertEqual(self.new.removeGuest(self.bed_id), True)


class TestPlacesApi(unittest.TestCase):

    def setup(self):
        self.new = PlacesApi.PlaceAPI()
        self.id = 37
        self.name = "TestName"
        self.address = "TestAddress"
        self.X = 39
        self.Y = 48

    def test_createNewPlace(self):
        self.assertEqual(self.new.createNewPlace(self.id, self.name, self.address, self.X, self.Y), True)

    def test_saveNewPlace(self):
        self.assertEqual(self.new.saveNewPlace(self.new.createNewPlace(self.id, self.name, self.address, self.X, self.Y)), True)
        # Mock needed?

    def test_getPlaces(self):
        self.assertEqual(self.new.getPlaces(), True)

    def test_getPlaceCounts(self):
        self.assertEqual(self.new.getPlaceCounts(), True)

if __name__ == '__main__':
    unittest.main()
