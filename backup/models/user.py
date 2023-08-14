#!/usr/bin/python3
"""
User class inheriting from the BaseModel class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class:
    attributes :
        email : string
        password : string
        firs_name: string
        last_name : string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
