#!/usr/bin/python3
""" this script holds the baseline for account class"""

from models.basemodel import BaseModel, Base
import uuid
import random
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

class Account(BaseModel, Base):
    """
    this class is a blue print for all account transactions
    """

    if models.storage_t == 'db':
        __tablename__ = 'accounts'
        acct_num = Column(String(16), nullable=False)
        acct_bal = Column(Integer, nullable=True)
        tid = Column(String(1064), nullable=True)
        id = Column(String(64), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)


    def __init__(self, *args, **kwargs):
        """
        this is a placeholder to ovveride init
        """
        super().__init__(*args, **kwargs)

    def deposit(self, amt):
        """
        this method allows users to deposit funds
        """
        print('i am iin acct class')
        self.acct_bal += amt
        tid = uuid.uuid4()
        self.tid_list['credit'].append((str(tid), str(amt)))
        print('i am done with deposit')
        return True

    def withdraw(self, amt):
        """
        this method allows users to withdraw funds
        """

        if amt > self.acct_bal:
            print("Request declined, Insufficient Balance")
            return False

        else:
            self.acct_bal -= amt
            tid = uuid.uuid4()
            self.tid_list['debit'].append((str(tid), str(amt)))
            return True

    def transfer(self, amt, acct_number):
        """
        this method allows customers to transfer funds
        """

        if not isinstance(amt, float) and not isinstance(amt, int):
            return "Pls enter a valid amount"

        for obj in Account.__all_accts:
            if self.acct_num == acct_number:
                return "Transaction not allowed"
            if obj.acct_num == acct_number:
                if amt > self.acct_bal:
                    return "Request declined, Insufficient Balance"
                else:
                    obj.acct_bal += amt
                    tid = uuid.uuid4()
                    obj.tid_list['debit'].append((str(tid), str(amt)))
                    break
        else:
            return "acct not found"

        self.acct_bal -= amt
        self.tid_list['credit'].append((str(tid), str(amt)))

    def create_acct(self):
        """
        this metod creates acct for customers
        """

        random_number = random.randint(0, 999999999)

        acct_number = '1' + str(random_number).zfill(9)
        self.acct_num = acct_number
        self.acct_bal = 0
        self.tid_list = {
                            'credit': [],
                            'debit': []
                        }
