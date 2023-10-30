#!/usr/bin/python3
"""
contains customers model
"""

import random
from models.basemodel import BaseModel, Base
from models.authentication import Authentication
from models.accounts import Account
from models.checkers import name_check, valid_dob, acct_check, phone_check, addr_check
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Customer(BaseModel, Account, Authentication, Base):
    """
    this is the blue print for all customer objects
    """

    num_of_cust = 0
    first = ""
    last = ""
    dob = ""
    sex = ""
    email = ""
    phone = ""
    addr = ""
    mid = ""
    __passwd = ""
    
    

    def __init__(self, *args, **kwargs):
        """
        this method instantiates a customer object
        """
        
        super().__init__(*args, **kwargs)
