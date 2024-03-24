from models.review import Review
import unittest

class test_user(unittest.TestCase):

    def test_place_id(self):
        self.assertTrue(type(Review.place_id) is str)

    def test_user_id(self):
        self.assertTrue(type(Review.user_id) is str)

    def test_text(self):
        self.assertTrue(type(Review.text) is str)
