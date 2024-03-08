#!/usr/bin/python3
from models.base_model import BMdl


class Usr(BMdl):
    """Creates a new user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
