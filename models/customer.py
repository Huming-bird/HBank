#!/usr/bin/python3
"""
contains customers model
"""

import random
import models
from models.basemodel import BaseModel, Base
from models.auth import Authentication
from models.account import Account
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Customer(BaseModel, Base):
    """
    this is the blue print for all customer objects
    """

    if models.storage_t == 'db':
        __tablename__ = 'customers'
        __table_args__ = {'extend_existing': True}
        first = Column(String(128), nullable=False)
        last = Column(String(128), nullable=False)
        dob = Column(String(128), nullable=False)
        sex = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)
        phone = Column(String(128), nullable=True)
        addr = Column(String(128), nullable=True)
        mid = Column(String(128), nullable=True)
        

    def __init__(self, *args, **kwargs):
        """
        this method instantiates a customer object
        """

        super().__init__(*args, **kwargs)
