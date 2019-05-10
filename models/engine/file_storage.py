#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Contains the FileStorage class
"""

import json
from models.base_model import BaseModel
from models.recipe import Recipe

classes = {"Recipe": Recipe, "BaseModel": BaseModel}


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __user_fav_path = "data/user_fav.json"
    # Where App will cache recipe to be reviewed by user are stored
    __cache_path = "data/cache.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}
    # dictionary - will store favorite objects by <class name>.id
    __favorites = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + str(obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        odict = {}
        for key in self.__objects:
            odict[key] = self.__objects[key].to_dict()
        with open(self.__cache_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def save_to_favorites(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        odict = {}
        for key in self.__favorites:
            odict[key] = self.__favorites[key].to_dict()
        with open(self.__user_fav_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self, js_file="objects"):
        """Deserializes the JSON file to __objects"""
        if js_file == "objects":
            try:
                with open(self.__cache_path, "r", encoding="utf-8") as f:
                    jo = json.load(f)
                for key in jo:
                    self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
            except FileNotFoundError:
                pass
        elif js_file == "favorites":
            try:
                with open(self.__user_fav_path, "r", encoding="utf-8") as f:
                    jo = json.load(f)
                for key in jo:
                    self.__favorites[key] = classes[jo[key]["__class__"]](**jo[key])
            except FileNotFoundError:
                pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """Get a single object from __objects

        Args:
            cls (str): string representing the class name
            id  (str): string representing the object ID

        Returns:
            Object base on the `class` and `id` or else `None`.
        """
        if cls is None or id is None:
            return None
        key = '{}.{}'.format(cls, id)
        return self.__objects.get(key, None)

    def count(self, cls=None):
        """counts all objects of a specific class (cls) in __objects
        or all objects if no `cls` name is passed

        Arsg:
            cls (str): String representing the class name. Default (None)

        Returns:
            `count` of all object in __objects is cls is None, else `count`
            of the specific onbject in __object.
        """
        if not cls:
            return len(self.__objects)
        return len([key for key in self.__objects if key.startswith(cls)])
