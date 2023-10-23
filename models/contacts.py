#!/usr/bin/python3
"""
this script holds the contacts class
"""

import models
from models.basemodel import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

class Contact(BaseModel, Base):
    """ Represents customer contact details """

    if models.storage_t == 'db':
        __tablename__ = 'contacts'
        email = Column(String(128), nullable=False)
        phone_num = Column(String(128), nullable=True)
        address = Column(String(128), nullable=True)
        state = Column(String(128), nullable=False)
        city = Column(String(128), nullable=True)
        country = Column(String(128), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
