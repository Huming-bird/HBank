#!/usr/bin/python3
"""
This script holds our checker functions
"""

import re


def name_check(value):
    """ function checks the supplied value and
    returns either True if value is a string
    and false if otherwise """

    pattern = r'^[a-zA-Z]{10}$'

    if re.match(pattern, value):
        return True
    return "enter a valid name"


def valid_dob(value):
    """
    validates a date 0f birth using regex
    """

    pattern = r'^\d{4}-\d{2}-(\d{1}\d{2})$'

    if re.match(pattern, value):
        return True
    return "enter a valid DOB using YY-MM-DD format"


def acct_check(value):
    """
    validates either savings or current acct.
    Returns True if either savings or current
    """

    if value.lower() == 'savings' or value.lower() == 'current':
        return True
    return "acct type not supported. Use either savings or current"


def phone_check(value):
    """
    this func validates the phone num. phone num must be 11digits
    """

    pattern = r'^\d{11}$'

    if re.match(pattern, value):
        return True
    return "enter a valid 11 digit phone number"


def addr_check(value):
    """
    function validates address. Returns True if
    address is string and number.
    """

    if value.isalnum():
        return True
    return "enter a valid address"


def password_check(password):
    upper, lower, special = 0, 0, 0
    for i in password:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i in "[!@#$%^&*()_+{}\[\]:;<>,.'?~\\\"-]":
            special += 1

    al_num = (any(c.isalpha() for c in password) and
              any(c.isdigit() for c in password))

    if upper >= 1 and lower >= 1 and special >=1 and al_num and len(password) >= 8:
        return True
    return False
