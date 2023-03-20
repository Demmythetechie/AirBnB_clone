#!/usr/bin/python3
"""This serialize and deserialize the dict from base model class"""
from models.base_model import BaseModel
import json


class FileStorage:
    """
    This is the file storage engine that makes it
    possible to store our data to a json file
    """

    # private class Atribute for json.file
    __file_path = "file.json"

    # private class Attributes for attribute dict
    __objects = {}

    def all(self):
        """Returns all the data saved in form of dictionary"""

        return self.__objects

    def new(self, obj):
        """
        Adds a new data entry to the __objects attribute
        for it to be serialized
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes the attributes class __objects
        into the the json file __file_path
        """

        with open(self.__file_path, 'w') as f:
            for key in self.__objects:
                if type(self.__objects[key]) != dict:
                    self.__objects[key] = self.__objects[key].to_dict()
            json.dump(self.__objects, f)

    def reload(self):
        """
        This deserializes the attributes of the basemodel
        classes and gives it back to the class private
        attribute __objects
        """

        try:
            with open(self.__file_path, encoding="utf-8") as f:
                with open(self.__file_path, 'r') as f:
                    for obj in json.load(f).values():
                        self.new(eval(obj["__class__"])(**obj))
        except Exception:
            pass
