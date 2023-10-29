#!/usr/bin/python3

import uuid
import random
from models.basemodel import Base, BaseModel

class Account(BaseModel, Base):
    """
    this class is a blue print for all account transactions
    """


    __all_accts = []
    
    @staticmethod
    def create_acct():
        """
        this metod creates acct for customers
        """

        random_number = random.randint(0, 999999999)

        acct_number = '1' + str(random_number).zfill(9)
        return acct_number
    
    
    def __init__(self, *args, **kwargs):
        """
        this is a placeholder to ovveride init
        """
        super().__init__(*args, **kwargs)
        Account.__all_accts.append(self)
        self.__acct_num = self.create_acct()
        self.__acct_bal = 0
        self.__tid_list = []


    def deposit(self, amt):
        """
        this method allows users to deposit funds
        """

        if isinstance(amt, float) or isinstance(amt, int):

            self.__acct_bal += amt
            tid = uuid.uuid4()
            self.__tid_list.append({str(tid): ["Credit", str(amt)]})
        else:
            return "Pls provide a valid amount"


    def withdraw(self, amt):
        """
        this method allows users to withdraw funds
        """

        if isinstance(amt, float) or isinstance(amt, int):
            if amt > self.__acct_bal:
                return "Request declined, Insufficient Balance"

            self.__acct_bal -= amt
            tid = uuid.uuid4()
            self.__tid_list.append({str(tid): ["Debit", str(amt)]})
        else:
            return "Pls provide a valid amount"


    def transfer(self, amt, acct_number):
        """
        this method allows customers to transfer funds
        """

        if not isinstance(amt, float) and not isinstance(amt, int):
            return "Pls enter a valid amount"

        for obj in Account.__all_accts:
            if self.__acct_num == acct_number:
                return "Transaction not allowed"
            if obj.__acct_num == acct_number:
                if amt > self.__acct_bal:
                    return "Request declined, Insufficient Balance"
                else:
                    obj.__acct_bal += amt
                    tid = uuid.uuid4()
                    obj.__tid_list.append({str(tid): ["Credit", str(amt)]})
                    break
        else:
            return "acct not found"

        self.__acct_bal -= amt
        self.__tid_list.append({str(tid): ["Debit", str(amt)]})
        
    @property
    def tid_list(self):
        """
        this method shows customer transaction details
        """
        print(f"your acct number is {self.__acct_num} and you have a balance of {self.__acct_bal}")
        return self.__tid_list
