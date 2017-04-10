import unittest
from models.APIs import PlacesApi

class MyTestCase(unittest.TestCase):
    def test_something(self):
        new = PlacesApi.PlaceAPI()
        new_place = new.createNewPlace(37,"test", "TestTest",39, 48)
        result = new.saveNewPlace(new_place)
        self.assertEqual(result, True)
        new = PlacesApi.PlaceAPI()
        new_place = new.createNewPlace(37,"test", "TestTest",39, 48)
        result = new.saveNewPlace(new_place)
        self.assertEqual(result, False)



if __name__ == '__main__':
    unittest.main()
