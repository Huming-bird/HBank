#!/usr/bin/python3
"""
contains customers model
"""

import models
import random
from models.basemodel import BaseModel, Base
from models.checkers import name_check, valid_dob, acct_check, phone_check, addr_check
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Customer(BaseModel):
    num_of_cust = 0
    acct_num = ""

    def __init__(self, first, last, dob, sex, email, acct_type, phone="", addr="", mid=""):
        if name_check(first) and name_check(last) and valid_dob(dob) and acct_check(acct_type) and phone_check(phone) and addr_check(addr) and name_check(mid):
            super().__init__()
            self.first = first
            self.last = last
            self.dob = dob
            self.sex = sex
            self.email = email
            self.mid = ""
            self.phone = ""
            self.addr = ""
            Customer.num_of_cust += 1
            self.create_acct(acct_type)




    def create_acct(self, acct_type):
        random_number = random.randint(0, 999999999)
        if acct_type == 'savings':
            acct_number = '1' + str(random_number).zfill(9)
        elif acct_type == 'current':
            acct_number = '0' + str(random_number).zfill(9)
        self.acct_num = acct_number
        return f"This is your acct number {acct_number}"

