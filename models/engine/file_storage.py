#!/usr/bin/env python3
"class that serializes deserializes instances"
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

class FileStorage():
    "class that serializes deserializes instances"
    __file_path = "memory.json"
    __objects = {}

    def update_object(self, key, attr, value):
        self.__objects[key].__dict__[attr] = value

    def all(self):
        return self.__objects


    def new(self, obj):
        self.temp_obj = obj
        self.key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[self.key] = obj

    def save(self):
        with open(self.__file_path, "w") as fp:
            obj_dict = {}
            for key, value in self.__objects.items():
                obj_dict[key] = self.to_dict(value)
            json.dump(obj_dict, fp, indent=4)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as fp:
                dict_objs = json.load(fp)

            for key, value in dict_objs.items():
                class_obj = classes[value['__class__']]
                del value['__class__']
                obj = class_obj(**value)
                self.__objects[key] = obj

    def to_dict(self, obj):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        obj_dict = {}
        for key, value in obj.__dict__.items():
            if type(value) is datetime:
                obj_dict[key] = value.isoformat()
            else:
                obj_dict[key] = value
        obj_dict['__class__'] = obj.__class__.__name__
        return obj_dict
