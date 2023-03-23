#!/usr/bin/python3
"""
This module creates a BaseModel instance along with
information about the place from Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    This creates place information using class attributes

    Args:
        city_id (str): city id
        user_id (str): user id
        name (str): name of the place
        description (str): about the house
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): maximum number of guest
        price_by_night (int):  cost per night
        latitude (float): location of the place
        longitude (float): location of the place
        amenity_ids (list) : list of amenity id's
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
