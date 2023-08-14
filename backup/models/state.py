#!/usr/bin/python3
""" state class definition inherititng from the basemodel """
from models.base_model import BaseModel


class State(BaseModel):
    """
    a subclass of base model
    attributes :
        name : string
    """
    name = ""
