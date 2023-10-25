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

class Account(Auth):
    """ Represents account class """

    if models.storage_t == 'db':
        __tablename__ = 'accounts'

        account = relationship("Auth", backref="account")
        balance = Column(INT(64), nullable=True)

    else:
        balance = 0


    def __init__(self, *args, **kwargs):
        """ Initialises a contact object """
        super().__init__(*args, **kwargs)

    def deposit(bank, log_in):

    '''
    This function will credit the given user's bank account with the given amount.
    bank is a dictionary where the key is the username and the value is the user's account balance.
    log_in is a dictionary where the key is the username and the value is the user's log-in status.
    amount is the amount to update with, and can either be positive or negative.

    To credit the user's account with the amount, the following requirements must be met:
    - The user exists in log_in and his/her status is True, meaning, the user is logged in.

    If the user doesn't exist in the bank, create the user.
    - The given amount can not result in a negative balance in the bank account.

    Return True if the user's account was updated.
    '''
    # for a customer to make deposit, he/she must first have a bank account
    # to make deposit, customer has to be logged in
    # deposit amount has to be greaer than zero

    username = input('Please provide your name: ')

    try:
        amount = float(input('How much do you want to deposit: '))
    except ValueError as e:
        print("invalid entry")
        deposit(bank,log_in)


    if username not in bank:
        print("You  have no account with this bank. Would you like to sign up?\n type yes or no")
        answer = input()
        if answer.lower() == "yes":
            signup(user_accounts, log_in, bank)
            login(user_accounts, log_in)
            bank[username]+= amount
        else:
            print("Deposit not successful")

    # this condition checks if a user is already logged in
    if amount > 0 and not(log_in[username]):
        password = input('Please provide your password: ')
        if password == user_accounts[username]:
            log_in[username] = True
            bank[username]+= amount
            return 'Deposit Successful'
    elif amount > 0 and log_in[username]:
        bank[username]+= amount
        return 'Deposit Successful'
    else:
        return 'Invalid amount'
