import unittest
from models.APIs import PlacesApi
from models.Resources import beds, places
import models.setUpConnection as CD


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.new = PlacesApi.PlaceAPI()
        self.name = "alireza"
        self._id = 0
        self.address = "1306 Ivy Meadow"
        self.X = -85.32
        self.Y = 72.99
        self.connection_data = CD.ConnectionData()
        self.cursor = CD.ConnectionUtility().getConnection(self.connection_data).cursor()


    def test_new_place(self):
        new = PlacesApi.PlaceAPI()
        new_place = new.createNewPlace(self._id,self.name,self.address,self.X,self.Y)
        result = new.saveNewPlace(new_place)
        self.assertEqual(result, True)
        self.cursor.execute("SELECT * FROM places WHERE Adress = (%s)",self.address)
        result = self.cursor.fetchone()
        self.assertEqual(result[1], self.name)
        self.assertEqual(result[3], self.address)



    def test_duplicate(self):
        new = PlacesApi.PlaceAPI()
        new_place = new.createNewPlace(123,self.name,self.address,self.X,self.Y)
        result = new.saveNewPlace(new_place)
        self.assertEqual(result, False)

    def test_createNewPlace(self):
        newPlace = places.Place(self.id, self.name, self.address, self.X, self.Y)
        apiPlace = self.new.createNewPlace(self.id, self.name, self.address, self.X, self.Y)

        self.assertEqual(newPlace.id, apiPlace.id)
        self.assertEqual(newPlace.name, apiPlace.name)
        self.assertEqual(newPlace.address, apiPlace.address)
        self.assertEqual(newPlace.X, apiPlace.X)
        self.assertEqual(newPlace.Y, apiPlace.Y)



if __name__ == '__main__':
    unittest.main()
