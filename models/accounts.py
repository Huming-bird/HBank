#!/usr/bin/python3
"""
this script holds the accounts class
"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Account(BaseModel, Base):
    """ this represents account claass """

