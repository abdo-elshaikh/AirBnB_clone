#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """ City class """
    state_id = ""
    name = ""
