#!/usr/bin/python3
"""
This module creates a BaseModel instance along with
users information from user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This creates user information using class attributes

    Args:
        email (str): users email
        password (str): users password
        first_name (str): users first name
        last_name (str): users last name

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
