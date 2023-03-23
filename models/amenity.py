#!/usr/bin/python3
"""
This module creates a BaseModel instance along with
amenity that a house has from Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This creates amenity information using class attributes
    Args:
        name (str): amenities in the house
    """

    name = ""
