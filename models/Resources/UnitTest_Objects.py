import unittest
from models.Resources import beds
from models.Resources import places


class TestBeds(unittest.TestCase):

    def setup(self):
        self.bed_id = 40
        self.guest_id = 35
        self.new_guest_id = 36
        self.placeid = 12
        self.availability = 1
        self.bed = beds.Bed(self.bed_id, self.guest_id, self.placeid, self.availability)

    def test_bed_id(self):
        self.assertEqual(self.bed.bed_id, self.bed_id)
        return

    def test_guest_id(self):
        self.assertEqual(self.bed.guest_id, self.guest_id)
        return

    def test_placeid(self):
        self.assertEqual(self.bed.placeid, self.placeid)
        return self.bed.placeid

    def test_availability(self):
        self.assertEqual(self.bed.availability, self.availability)

    def test_set_guest(self):
        self.assertEqual(self.bed.set_guest(self.new_guest_id), self.new_guest_id)
        self.assertEqual(self.bed.availability, False)

    def test_remove_guest(self):
        self.assertEqual(self.bed.guest_id, None)
        self.assertEqual(self.bed.availability, True)


class TestPlaces(unittest.TestCase):

    def test_setup(self):
        self.id = 37
        self.name = "TestName"
        self.address = "TestAddress"
        self.X = 39
        self.Y = 48
        self.place = places.Place(self.id, self.name, self.address, self.X, self.Y)

    def test_name(self):
        self.assertEqual(self.place.name(),self.name)

    def test_id(self):
        self.assertEqual(self.place.id(), self.id)

    def test_X(self):
        self.assertEqual(self.place.X(), self.X)

    def test_Y(self):
        self.assertEqual(self.place.Y(), self.Y)

    def test_address(self):
        self.assertEqual(self.place.address(), self.address)


if __name__ == '__main__':
    unittest.main()
