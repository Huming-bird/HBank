#!/usr/bin/python3
"""
this script holds authenticatication class 
"""

from models.basemodel import BaseModel
from models.customers import Customer
import models
from models.checkers import password_check

class Authentication(BaseModel):
    """
    instantiates authentication objetcs
    """
    def signup(self, customer, password):
        """
        this method will allow customers signup for an acct
        after autheticating their password
        """

        self.id = customer.id
        self.passwd = password

        if password_check():
            return True
        return False

    def login(customer, password):
        """
        this method allows users to login to their acct
        """

        if password_check():
            if customer._passwd == password:
                return True
            return False
        return False

    def __init__(self, customer, password):
        """
        this metho instantiates an authentication object
        """
        self.id = customer.id
        self.signup(customer, password)
        customer._password = password
