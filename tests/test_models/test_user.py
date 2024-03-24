from models.user import User
import unittest

class test_user(unittest.TestCase):

    def test_email(self):
        self.assertTrue(type(User.email) is str)

    def test_password(self):
        self.assertTrue(type(User.password) is str)

    def test_first_name(self):
        self.assertTrue(type(User.first_name) is str)

    def test_last_name(self):
        self.assertTrue(type(User.last_name) is str)
