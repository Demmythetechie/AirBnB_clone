#!/usr/bin/python3


import json
from models.base_model import BaseModel


class FileStorage:
    """
    This is the file storage engine that makes it
    possible to store our data to a json file
    """

    #private class Atribute for json.file
    __file_path = "file.json"

    #private class Attributes for attribute dict
    __objects = {}

    def all(self):
        """
        Returns all the data saved in form of dictionary
        """

        return self.__objects

    def new(self, obj):
        """
        Adds a new data entry to the __object attribute
        for it to be serialized
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes the attributes class __object
        into the the json file __file_path
        """

        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage, f)


    def reload(self):
        """
        This deserializes the attributes of the basemodel
        classes and gives it back to the class private
        attribute __object
        """

        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
