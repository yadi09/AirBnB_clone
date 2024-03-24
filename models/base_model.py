#!/usr/bin/env python3
"""class that defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """BaseModel class"""

    def __init__(self, *agrs, **kwargs):
        if kwargs:
            obj_args = {}
            for key, value in kwargs.items():
                if key != '__class__':
                    if key != 'created_at' and key != 'updated_at':
                        setattr(self, key, value)
                    else:
                        setattr(self, key, datetime.fromisoformat(value))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        "__str__ function"
        return "\
[{}] ({}) {}\
".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        "updates the public instance attribute updated_at"
        self.updated_at = datetime.now()
        models.storage.save()

    def all(self):
        return models.storage.all()

    def update_object(self, key, attr, value):
        models.storage.update_object(key, attr, value)

    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        obj_dict = {}
        for key, value in self.__dict__.items():
            if type(value) is datetime:
                obj_dict[key] = value.isoformat()
            else:
                obj_dict[key] = value
        obj_dict['__class__'] = __class__.__name__
        return obj_dict
