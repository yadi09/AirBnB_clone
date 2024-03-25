from models.city import City
import unittest


class test_user(unittest.TestCase):

    def test_state_id(self):
        self.assertTrue(type(City.state_id) is str)

    def test_name(self):
        self.assertTrue(type(City.name) is str)
