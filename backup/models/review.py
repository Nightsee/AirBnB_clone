#!/usr/bin/python3
"""
review class inheritting from base model class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    subclass of BaseModel class
    attributes :
        place_id :str
        user_id: str
        text: str
    """
    place_id = ""
    user_id = ""
    text = ""
