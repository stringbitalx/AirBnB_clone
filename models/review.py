#!/usr/bin/python3
""" Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): Place id.
        user_id (str):  User id.
        text (str):  review's text.
    """

    place_id = ""
    user_id = ""
    text = ""
