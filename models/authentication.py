#!/usr/bin/python3
"""
this script holds authenticatication class 
"""

from models.basemodel import Base, BaseModel
from models.checkers import password_check

class Authentication:
    """
    instantiates authentication objetcs
    """
    @property
    def password(self):
        """does nothing"""
        pass

    @password.setter
    def password(self, password):
        """sets a user password"""
        self.__passwd = password


    def signup(self, password):
        """
        this method will allow customers signup for an acct
        after autheticating their password
        """

        if self.id:
            if password_check(password):
                return True
            return False
        return False

    def login(self, password):
        """
        this method allows users to login to their acct
        """

        if self.id and isinstance(self, Customer):
            if password_check(password):
                if self.__passwd == password:
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
        does nothing
        """
        pass
