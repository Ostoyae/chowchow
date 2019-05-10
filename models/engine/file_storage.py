#!/usr/bin/python3
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
    __user_fav_path = "user_fav.json"
    # Where App will cache recipe to be reviewed by user are stored
    __cache_path = "cache.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}
    # dictionary - will store favorite objects by <class name>.id
    __favorites = {}

    def all(self, cls=None, dest="objects"):
        """returns the dictionary __objects"""
        if dest == "objects":
            all = self.__objects
        else:
            all == self.__favorites
        if cls is not None:
            new_dict = {}
            for key, value in all.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return all

    def new(self, obj, dest="objects"):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            if dest == "objects":
                new = self.__objects
            else:
                new = self.__favorites
            key = obj.__class__.__name__ + "." + obj.id
            new[key] = obj

    def save(self, dest="objects"):
        """serializes __objects to the JSON file (path: __file_path)"""
        odict = {}
        if dest == "objects":
            save = self.__objects
            path = self.__cache_path
        else:
            save = self.__favorites
            path = self.__user_fav_path
        for key in save:
            odict[key] = save[key].to_dict()
        with open(path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self, dest="objects"):
        """Deserializes the JSON file to __objects"""
        if dest == "objects":
            reload = self.__objects
            path = self.__cache_path
        else:
            reload = self.__favorites
            path = self.__user_fav_path
            try:
                with open(path, "r", encoding="utf-8") as f:
                    jo = json.load(f)
                for key in jo:
                    reload[key] = classes[jo[key]["__class__"]](
                        **jo[key])
            except FileNotFoundError:
                pass

    def delete(self, obj=None, dest="objects"):
        """Removes object from objects or favorites dictionary"""
        if obj is not None:
            if dest == "objects":
                delete = self.__objects
            else:
                delete = self.__favorites
            key = obj.__class__.__name__ + '.' + obj.id
            if key in delete:
                del delete[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id, dest="objects"):
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
        if dest == "objects":
            return self.__objects.get(key, None)
        else:
            return self.__favorites.get(key, None)

    def count(self, cls=None, dest="objects"):
        """counts all objects of a specific class (cls) in __objects
        or all objects if no `cls` name is passed

        Arsg:
            cls (str): String representing the class name. Default (None)

        Returns:
            `count` of all object in __objects is cls is None, else `count`
            of the specific onbject in __object.
        """
        all = self.__objects
        if dest != "objects":
            all = self.__favorites
        if not cls:
            return len(all)
        return len([key for key in all if key.startswith(cls)])
