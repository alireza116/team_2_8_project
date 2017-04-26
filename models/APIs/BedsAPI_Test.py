import unittest
from models.APIs import BedsApi


class testBedsAPI(unittest.TestCase):

    def setUp(self):
        self.api = BedsApi.BedsApi()

    def test_create(self):
        bed = self.api.createNewBed(0,432,12,1)
        self.assertEqual(bed.bed_id, 0)
        self.assertEqual(bed.availability,1)
        self.assertEqual(bed.guest_id,432)
        self.assertEqual(bed.placeid,12)

    def save_new_bed(self):
        bed = self.api.createNewBed(0,432,12,1)
        savedBed = self.api.saveNewBed(bed)
        self.assertEqual(savedBed,True)

    def set_new_guest(self):
        bed = self.api.setNewGuest(432,13)
        self.assertEqual(bed,False)




if __name__ == '__main__':
    unittest.main()
