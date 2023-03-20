#!/usr/bin/python3
"""
This module holds a class BaseModel which will
be inherited by all other class to get it time of
creation and unique id
"""
import uuid
from datetime import datetime as dt
import models


class BaseModel:
    """
    This class is to be inherited by all other
    classes of this project which assigns a uuid
    for each object created by any of the clases
    """

    def __init__(self, *args, **kwargs):
        """
        This method intializes three attributes that helps
        keep track of the creation and alredy created objects
        Args:
            id (uuid object): creates an id for new object
            created_at (datetime):
            updated_at (datetime):
            kwargs (dict):
            args (tuple):
        """

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            models.storage.new(self)
        else:
            self.id = kwargs["id"]
            self.created_at = dt.fromisoformat(kwargs["created_at"])
            self.updated_at = dt.fromisoformat(kwargs["updated_at"])

    def __str__(self):
        """
        Returns a string representation for instance whenever
        they are printed
        """

        st = f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
        return st

    def save(self):
        """
        Saves the attributes in dictionary to the json file
        """

        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns attributes of the class to a dictionary format
        """

        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        dic = {
                "__class__": __class__.__name__,
                }
        dic.update(self.__dict__)
        return dic
