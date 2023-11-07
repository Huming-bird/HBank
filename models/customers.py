#!/usr/bin/python3
"""
contains customers model
"""

import random
import models
from models.basemodel import BaseModel, Base
from models.authentication import Authentication
from models.accounts import Account
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, JSON
from sqlalchemy.orm import relationship


class Customer(BaseModel, Account, Authentication, Base):
    """
    this is the blue print for all customer objects
    """

    if models.storage_t == 'db':
        __tablename__ = 'customers'
        first = Column(String(128), nullable=False)
        last = Column(String(128), nullable=False)
        dob = Column(String(128), nullable=False)
        sex = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)
        phone = Column(String(128), nullable=True)
        addr = Column(String(128), nullable=True)
        mid = Column(String(128), nullable=True)
        _Account__acct_num = Column(String(10), nullable=True)
        _Account__acct_bal = Column(Integer, nullable=True)
        _Account__tid_list = Column(JSON, nullable=True)
        _Authentication__passwd = Column(String(64), nullable=True)

    def __init__(self, *args, **kwargs):
        """
        this method instantiates a customer object
        """

        super().__init__(*args, **kwargs)
