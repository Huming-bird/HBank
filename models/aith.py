#!/usr/bin/python3
"""
this script holds authenticatication class
"""

# from models.basemodel import Base, BaseModel
from models.checkers import password_check


class Authentication():
    """
    instantiates authentication objetcs
    """
    @property
    def password(self):
        """does nothing"""
        return self.__passwd

    @password.setter
    def password(self, password):
        """sets a user password"""
        self.__passwd = password

    def signup(self):
        """
        this method will allow customers signup for an acct
        after autheticating their password
        """

        password = input('Pls provide a strong password: \n')

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
