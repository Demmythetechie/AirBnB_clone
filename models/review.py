#!/usr/bin/python3
"""
This module creates a BaseModel instance along with
review information from Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This creates review information using class attributes

    Args:
        place_id (str): place.id
        user_id (str): user.id
        text (str): user review message
    """

    place_id = ""
    user_id = ""
    text = ""
