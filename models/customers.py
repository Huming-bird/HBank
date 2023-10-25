#!/usr/bin/python3
"""
contains customers model
"""

import models
from models.basemodel import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Customer(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'customers'
        email = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        mid_name = Column(String(128), nullable=True)
        dob = Column(String(64), nullable=False)
        contacts = relationship("Contact", backref="user")
    else:
        email = ""
        first_name = ""
        last_name = ""
        mid_name = ""
        dob = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
