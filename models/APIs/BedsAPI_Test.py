import unittest
from models.APIs import BedsApi
import models.setUpConnection as CD

class testBedsAPI(unittest.TestCase):

    def setUp(self):
        self.api = BedsApi.BedsApi()
        self._bed_id = 5000
        self._guest_id = -1
        self._place_id = 16
        self._availability = 1
        self._new_guest = 5555
        self.connection_data = CD.ConnectionData()
        self.cursor = CD.ConnectionUtility().getConnection(self.connection_data).cursor()
        self.cursor.execute("DELETE FROM beds WHERE bed_id = (%s)", self._bed_id)


    def test_create(self):
        bed = self.api.createNewBed(self._bed_id, self._guest_id, self._place_id, self._availability)
        self.assertEqual(bed.bed_id, self._bed_id)
        self.assertEqual(bed.availability,self._availability)
        self.assertEqual(bed.guest_id,self._guest_id)
        self.assertEqual(bed.placeid,self._place_id)

    def test_save_new_bed(self):
        bed = self.api.createNewBed(self._bed_id, self._guest_id, self._place_id, self._availability)
        self.api.saveNewBed(bed)
        self.cursor.execute("select * from beds where bed_id = (%s)", self._bed_id)
        result = self.cursor.fetchone()
        self.assertEqual(result[2],self._bed_id)
        self.assertEqual(result[0], self._place_id)


    def test_reserve_bed(self):
        bed = self.api.createNewBed(self._bed_id, self._guest_id, self._place_id, self._availability)
        self.api.saveNewBed(bed)
        self.api.setNewGuest(self._bed_id,self._new_guest)
        self.cursor.execute("select * from beds where bed_id = (%s)", self._bed_id)
        result = self.cursor.fetchone()
        print(result)
        self.assertEqual(result[3],0)
        self.assertEqual(result[1],self._new_guest)

    def test_reserve_bed(self):
        bed = self.api.createNewBed(self._bed_id, self._guest_id, self._place_id, self._availability)
        self.api.saveNewBed(bed)
        self.api.setNewGuest(self._bed_id,self._new_guest)
        self.api.removeGuest(self._bed_id, self._new_guest)
        self.cursor.execute("select * from beds where bed_id = (%s)", self._bed_id)
        result = self.cursor.fetchone()
        print(result)
        self.assertEqual(result[3],1)
        self.assertEqual(result[1],-1)

    def test_checkout_bed(self):
        bed = self.api.createNewBed(self._bed_id, self._guest_id, self._place_id, self._availability)
        self.api.saveNewBed(bed)
        self.api.setNewGuest(self._bed_id,self._new_guest)
        self.api.removeGuest(self._bed_id, 3455)
        self.cursor.execute("select * from beds where bed_id = (%s)", self._bed_id)
        result = self.cursor.fetchone()
        print(result)
        self.assertEqual(result[3],0)
        self.assertEqual(result[1],self._new_guest)


if __name__ == '__main__':
    unittest.main()
