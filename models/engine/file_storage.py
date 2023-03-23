#!/usr/bin/python3
"""This serialize and deserialize the dict from base model class"""
import json
from models.base_model import BaseModel
from models.user import User


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

        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new data entry to the __objects attribute
        for it to be serialized
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes the attributes class __objects
        into the the json file __file_path
        """

        with open(FileStorage.__file_path, 'w') as f:
            for key in FileStorage.__objects:
                if type(FileStorage.__objects[key]) != dict:
                    FileStorage.__objects[key] = FileStorage.__objects[key].to_dict()
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """
        This deserializes the attributes of the basemodel
        classes and gives it back to the class private
        attribute __objects
        """

        try:
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            pass
