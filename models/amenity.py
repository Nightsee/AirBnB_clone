#!/usr/bin/python3
"""
amenity class inheritting from the basemodel class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    subclass of baseModel class
    attributes:
        name: string
    """
    name = ""
