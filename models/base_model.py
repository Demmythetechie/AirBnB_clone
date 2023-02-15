#!/usr/bin/piython3
"""
    This is the BaseModel class where all other classes
    that makes up the airbnb website inherits from, which
    gives each creation of an object in the website a
    unique id along with date and time of creation. And an
    update in case an attribute of the class was updated

    Note: d serves as datetime (line 13)
"""


from datetime import datetime as d
import models
import uuid


class BaseModel:
    """
    This is the BaseModel class where all other classes
    that makes up the airbnb website inherits from, which
    gives each creation of an object in the website a
    unique id along with date and time of creation. And an
    update in case an attribute of the class was updated.
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

        if len(kwargs) != 4:
            self.created_at = d.now()
            self.id = str(uuid.uuid4())
            self.updated_at = d.now()
            models.storage.new(self)
        else:
            self.created_at = d.fromisoformat(kwargs.get('created_at'))
            self.id = kwargs.get('id')
            self.updated_at = d.fromisoformat(kwargs.get('updated_at'))

    def __str__(self):
        """
        Returns a string representation for instance whenever
        they are printed
        """

        class_n = __class__.__name__
        return f"[{class_n}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Saves the attributes in dictionary to the json file
        """
        self.updated_at = d.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns attributes of the class to a dictionary format
        """
        class_n = __class__.__name__
        created = self.created_at.isoformat()
        updated = self.updated_at.isoformat()
        dic = {
            '__class__': class_n,
            'updated_at': updated,
            'id': self.id,
            'created_at': created
        }
        return dic
