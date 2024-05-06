#!/usr/bin/python3
"""
this Handles I/O, writing and reading, of JSON for storage of all class instances
"""

import json
from models import base_model, amenity, city, place, review, state, user
from datetime import datetime

class FileStorage:
    """Handles I/O, writing and reading of JSON for storage of all class instances"""

    CNC = {
        'BaseModel': base_model.BaseModel,
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
    }

    __file_path = './dev/file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns private attribute: __objects"""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Sets / updates in __objects the obj with key <obj class name>.id"""
        bm_id = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[bm_id] = obj

    def get(self, cls, id):
        """Gets specific object"""
        all_class = self.all(cls)
        for obj in all_class.values():
            if id == str(obj.id):
                return obj
        return None

    def count(self, cls=None):
        """Count of instances"""
        return len(self.all(cls))

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        data = {key: obj.to_json() for key, obj in self.__objects.items()}
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(data, f)

    def reload(self):
        """If file exists, deserializes JSON file to __objects, else nothing"""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                data = json.load(f)
                self.__objects = {}
                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    obj_class = self.CNC[class_name]
                    self.__objects[key] = obj_class(**obj_data)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj"""
        if obj is None:
            return
        for key in list(self.__objects.keys()):
            if obj.id == key.split(".")[1] and key.split(".")[0] == type(obj).__name__:
                del self.__objects[key]
                self.save()

    def close(self):
        """Calls the reload() method for deserialization from JSON to objects"""
        self.reload()
