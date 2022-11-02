#!/usr/bin/python3
"""
Module for user that inherits from baseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that represents a user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
