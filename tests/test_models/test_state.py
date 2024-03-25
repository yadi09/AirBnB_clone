from models.state import State
import unittest


class test_user(unittest.TestCase):

    def test_name(self):
        self.assertTrue(type(State.name) is str)
