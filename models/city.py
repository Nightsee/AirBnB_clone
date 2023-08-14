#!/usr/bin/python3
"""
city class inheriting from the BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    subclass of base model,
    attributes:
        state_id : str
        name : str
    """
    state_id = ""
    name = ""
