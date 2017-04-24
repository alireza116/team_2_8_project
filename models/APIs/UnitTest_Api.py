import unittest
from models.APIs import BedsApi
from models.APIs import PlacesApi
from models.Resources import beds, places


class TestBedsApi(unittest.TestCase):
    def setUp(self):
        self.new = BedsApi.BedsApi()
        self.bed_id = 0
        self.guest_id = 35
        self.new_guest_id = 36
        self.placeid = 12
        self.availability = 1

    def test_createNewBed(self):
        newBed = beds.Bed(self.bed_id, self.guest_id, self.placeid, self.availability)
        bed = self.new.createNewBed(self.bed_id, self.guest_id, self.placeid, self.availability)
        self.assertEqual(newBed.bed_id, bed.bed_id)
        self.assertEqual(newBed.guest_id, bed.guest_id)
        self.assertEqual(newBed.placeid, bed.placeid)
        self.assertEqual(newBed.availability, bed.availability)

    def test_saveNewBed(self):
        testbed = beds.Bed(self.bed_id, self.guest_id, self.placeid, self.availability)
        self.assertEqual(self.new.saveNewBed(testbed), True)

    def test_getBeds(self):
        self.assertGreater(len(self.new.getBeds(self.placeid)), 0)

    def test_getAvailableBeds(self):
        self.assertGreater(len(self.new.getAvailableBeds(self.placeid)), 0)

    def test_setNewGuest(self):
        self.assertEqual(self.new.setNewGuest(self.bed_id, self.new_guest_id), True)

    def test_removeGuest(self):
        self.assertEqual(self.new.removeGuest(self.bed_id), True)


class TestPlacesApi(unittest.TestCase):
    def setUp(self):
        self.new2 = PlacesApi.PlaceAPI()
        self.id = 37
        self.name = "TestName"
        self.address = "TestAddress"
        self.X = 39
        self.Y = 48

    def test_createNewPlace(self):
        newPlace = places.Place(self.id, self.name, self.address, self.X, self.Y)
        apiPlace = self.new2.createNewPlace(self.id, self.name, self.address, self.X, self.Y)
        print(newPlace)
        # self.assertEqual(newPlace.id, apiPlace.id)
        # self.assertEqual(newPlace.name, apiPlace.name)
        # self.assertEqual(newPlace.address, apiPlace.address)
        # self.assertEqual(newPlace.X, apiPlace.X)
        # self.assertEqual(newPlace.Y, apiPlace.Y)

    def test_saveNewPlace(self):
            self.assertEqual(self.new2.saveNewPlace(self.new2.createNewPlace(self.id, self.name, self.address, self.X, self.Y)), True)
            # Mock needed?

    def test_getPlaces(self):
        self.assertEqual(self.new2.getPlaces(), True)

    def test_getPlaceCounts(self):
        self.assertEqual(self.new2.getPlaceCounts(), True)


if __name__ == '__main__':
    unittest.main()
