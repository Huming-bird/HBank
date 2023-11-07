#!/usr/bin/python3
"""
this script holds authenticatication class
"""

# from models.basemodel import Base, BaseModel
from models.checkers import password_check
from models.basemodel import BaseModel, Base
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Authentication(BaseModel, Base):
    """
    instantiates authentication objetcs
    """


    if models.storage_t == 'db':
        __tablename__ = 'authentications'
        
        password = Column(String(64), nullable=True)


    def signup(self):
        """
        this method will allow customers signup for an acct
        after autheticating their password
        """

        password = input('Pls provide a strong password: ')

        if password_check(password):
            self.password = password
            print('signup successful')
            return True
        return False

    def login(self):
        """
        this method allows users to login to their acct
        """

        password = input('Pls provide your password: \n')

        if password_check(password):
            if self.password == password:
                return True
            return False
        return False

    def update_password(self, password):
        """
        this updates customerpassword
        """
        if self.id:
            if password_check(password):
                self.password = password

    def __init__(self, *args, **kwargs):
        """
        instantiates authentication object
        """
        super().__init__(*args, **kwargs)
