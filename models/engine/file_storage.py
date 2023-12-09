#!/usr/bin/python3
import json
from models.base_model import BaseModel
import os
from models.user import User


class FileStorage:
    """
    FileStorage class
    attributes:
        __file_path: path to the JSON file
        __objects: dictionary of objects
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        """
        reload the objects from the JSON file
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for key, value in data.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        else:
            pass
