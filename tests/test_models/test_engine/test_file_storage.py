#!/usr/bin/env python3


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json


class Test_FileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.obj = BaseModel()

    def tearDown(self):
        if os.path.exists(self.storage.get_file_path()):
            os.remove(self.storage.get_file_path())

        if self.storage:
            self.storage.close()
        if self.obj:
            self.obj.close()

    def test_object_is_dict(self):
        self.assertEqual(type(self.storage.get_objects()), dict)
        self.assertTrue(self.storage.get_objects() != {})

    def test_file_path_is_not_empty(self):
        self.assertTrue(self.storage.get_file_path())

    def test_BaseModel_save(self):
        old_time = self.obj.updated_at
        self.obj.name = "Yadamzer"
        self.obj.save()
        new_time = self.obj.updated_at

        self.assertNotEqual(old_time, new_time)
        self.assertTrue(os.path.exists(self.storage.get_file_path()))

    def test_init_BaseModel(self):
        obj_dict = {'name': 'Yadamze', 'age': '21', 'sex': 'M'}
        Base_obj = BaseModel(obj_dict)

        self.assertTrue(hasattr(self.Base_obj, "age"))


    def test_reload(self):
        self.assertTrue(self.storage.get_objects() != {})

    def test_save(self):
        with open(self.storage.get_file_storage(), "r") as fp:
            file_content = fp.read()
        obj_dict = obj.__dict__
        obj_dict['__class__'] = obj.__class__.__name__

        self.assertEqual(file_content, json.dumps(obj_dict))
