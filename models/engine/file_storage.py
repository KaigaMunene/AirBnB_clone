#!/usr/bin/python3
"""
    This contains the FileStorage module
"""
import json
from models.base_model import BaseModel
from models.user import User


valid_classes = {"BaseModel": BaseModel,
                 "User": User}


class FileStorage():
    """
        Comment
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """A method that returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """A method that serializes __objects to the JSON file."""
        with open(self.__file_path, 'w', encoding="utf-8") as fp:
            jdict_ = {}
            for k, v in self.__objects.items():
                dict_ = self.__objects[k].to_dict()
                jdict_[k] = dict_
            fp.write(json.dumps(jdict_))

    def reload(self):
        """A method that deserializes the JSON file to __objects."""
        dict_ = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as fp:
                str_ = fp.read()
                dict_ = json.loads(str_)
                for k, v in dict_.items():
                    class_ = v['__class__']
                    create_class = valid_classes[class_]
                    self.__objects[k] = create_class(**v)
