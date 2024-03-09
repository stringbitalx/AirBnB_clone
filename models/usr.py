#!/usr/bin/python3
from models.base_mdl import BaseMdl


class Usr(BaseMdl):
    """Creates a new user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
