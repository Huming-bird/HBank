#!/usr/bin/python3
"""
this script holds the authentication class
"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Auth(Customer):
    """ this represents authentication claass """

    def signup(self, user_accounts, log_in, bank):
        """
        This function allows users to sign up.
        If both username and password meet the requirements:
        """

        username = input('Please provide your name: ')
        print("Pls provide at least 8chars long password. It should contain at least one uppercase, lowercase and numbers\n")
        password = input('please provide a valid password: ')


        if username not in user_accounts and username != password and password_check(password):
            user_accounts[username] = password
            log_in[username] = False
            bank[username] = 0
            return 'Congratulations!!, We Successfully Signed Up your account'
        else:
            return 'Something went wrong, please check your details and try again'

    def login(user_accounts, log_in):

    '''
    This function allows users to log in with their username and password.
    The user_accounts dictionary stores the username and associated password.
    The log_in dictionary stores the username and associated log-in status.

    If the username does not exist in user_accounts or the password is incorrect:
    - Returns False.
    Otherwise:
    - Updates the user's log-in status in the log_in dictionary, setting the value to True.
    - Returns True.
    '''

    username = input('Please provide your name: ')

    if username in user_accounts:
        print("'please provide a your password which is at least 8chars long\n")
        password = input()
        if password == user_accounts[username]:
            # Update log_in status to True
            log_in[username] = True
            return 'Login Successful'
        else:
            return "invalid password"
    else:
        return 'User doesn\'t exist'

