from models.place import Place
import unittest

class test_user(unittest.TestCase):

    def test_city_id(self):
        self.assertTrue(type(Place.city_id) is str)

    def test_user_id(self):
        self.assertTrue(type(Place.user_id) is str)

    def test_name(self):
        self.assertTrue(type(Place.name) is str)

    def test_description(self):
        self.assertTrue(type(Place.description) is str)

    def test_number_rooms(self):
        self.assertTrue(type(Place.number_rooms) is int)

    def test_number_bathrooms(self):
        self.assertTrue(type(Place.number_bathrooms) is int)

    def test_max_guest(self):
        self.assertTrue(type(Place.max_guest) is int)

    def test_price_by_night(self):
        self.assertTrue(type(Place.price_by_night) is int)

    def test_latitude(self):
        self.assertTrue(type(Place.latitude) is float)

    def test_longitude(self):
        self.assertTrue(type(Place.longitude) is float)

    def test_amenity_ids(self):
        self.assertTrue(type(Place.amenity_ids) is list)
