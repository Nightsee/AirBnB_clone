#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

"""
this is the parent class to all other classes in the airbnb project
"""
dateFormat = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    """ parent class, containing common methods and attributes """
    date_format = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, *args, **kwargs):
        """ intialize attributes """
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime
                    (kwargs["created_at"], date_format)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime
                    (kwargs["updated_at"], date_format)
                elif "__class__" == key:
                    pass
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ return class name, id, and dictionary """
        return ('[{}] ({}) {}'.format
                (self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ saves the self """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return a dic """
        dic = self.__dict__.copy()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["created_at"] = self.created_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
