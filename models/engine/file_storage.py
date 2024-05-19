#!/usr/bin/python3
"""
FileStorage module
"""

import json
import os


class FileStorage:
    """Serializes instances to a JSON file and deserializes"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {
            key: obj.to_dict() for key, obj in self.__objects.items()
        }
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists).
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, obj in obj_dict.items():
                    class_name = obj["__class__"]
                    module = __import__(
                        f"models.{class_name.lower()}",
                        fromlist=[class_name]
                    )
                    cls = getattr(module, class_name)
                    self.__objects[key] = cls(**obj)
