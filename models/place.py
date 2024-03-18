#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """The place.

    Attributes:
        city_id (str): City id.
        user_id (str): User id.
        name (str): The name of the place.
        description (str): place description.
        number_rooms (int): rooms of the place.
        number_bathrooms (int): bathrooms of the place.
        max_guest (int): max guests of the place.
        price_by_night (int): nights price of the place.
        latitude (float): place's latitude.
        amenity_ids (list): Amenity ids list.
        longitude (float): place's longitude.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
