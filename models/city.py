#!/usr/bin/python3
"""
This module creates a BaseModel instance along with
city information in states from City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This creates City information using class attributes
    Args:
        state_id (str): State.id
        name (str): name of city
    """

    state_id = ""
    name = ""
