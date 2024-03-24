#!/usr/bin/env python3
"classes that inherit from BaseModel"
from models.base_model import BaseModel


class Review(BaseModel):
    "classes that inherit from BaseModel"
    place_id = ""
    user_id = ""
    text = ""
