#!/usr/bin/python3
"""
Here we will to import the file)storage class and create an
instance of it which will be used in the base_model.py file 
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
