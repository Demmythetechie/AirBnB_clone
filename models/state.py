#!/usr/bin/python3
"""
This module creates a BaseModel instance along with
states name information from State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    This creates state names information using class attributes

    Args:
        name (str): names of states
    """

    name = ""
