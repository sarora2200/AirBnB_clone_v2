#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

     def __init__(self):
        """Initializes a FileStorage instance"""
        self.model_classes = {
            'BaseModel': import_module('models.base_model').BaseModel,
            'User': import_module('models.user').User,
            'State': import_module('models.state').State,
            'City': import_module('models.city').City,
            'Amenity': import_module('models.amenity').Amenity,
            'Place': import_module('models.place').Place,
            'Review': import_module('models.review').Review
        }

    def all(self, cls=None):
        """Returns a dictionary of models"""
        if not cls:
            return FileStorage.__objects
        else:
            newdict = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    newdict[key] = value
            return newdict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {key: val.to_dict() for key, val
                in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(os.path.abspath(FileStorage.__file_path),
                      "r", encoding="UTF8") as fd:
                data = json.load(fd)
                for val in data.values():
                    class_name = val.pop("__class__", None)
                    if class_name and class_name in globals():
                        cls = globals()[class_name]
                        self.new(cls(**val))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects.pop(key, None)

    def close(self):
        """Deserializing the JSON file to objects"""
        self.reload()
