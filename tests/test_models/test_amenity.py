from models.amenity import Amenity
import unittest

class test_user(unittest.TestCase):

    def test_name(self):
        self.assertTrue(type(Amenity.name) is str)
