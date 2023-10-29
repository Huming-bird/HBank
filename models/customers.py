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


class Customer(Account, Authentication):
    """
    this is the blue print for all customer objects
    """

    num_of_cust = 0
    __acct_num = ""
    first = ""
    last = ""
    dob = ""
    sex = ""
    email = ""
    phone = ""
    addr = ""
    mid = ""
    __passwd = "Huming100&"
    
    

    def __init__(self, *args, **kwargs):
        """
        this method instantiates a customer object
        """
        #if name_check(first) and name_check(last) and valid_dob(dob) and acct_check(acct_type) and phone_check(phone) and addr_check(addr) and name_check(mid):
        
        super().__init__(*args, **kwargs)
        self.signup(self.__passwd)    #default password to be changed by customer
        # self.__acct_num = self.create_acct()
        # self.__acct_bal = 0
        # self.__tid_list = []
        Customer.num_of_cust += 1
