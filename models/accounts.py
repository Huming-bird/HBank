#!/usr/bin/python3
""" this script holds the baseline for account class"""

import uuid
import random


class Account():
    """
    this class is a blue print for all account transactions
    """

    def create_acct(self):
        """
        this metod creates acct for customers
        """

        random_number = random.randint(0, 999999999)

        acct_number = '1' + str(random_number).zfill(9)
        self.__acct_num = acct_number
        self.__acct_bal = 0
        self.__tid_list = {
                            'credit': [],
                            'debit': []
                        }

    def __init__(self, *args, **kwargs):
        """
        this is a placeholder to ovveride init
        """
        super().__init__(*args, **kwargs)

    def deposit(self, amt):
        """
        this method allows users to deposit funds
        """

        self.acct_bal += amt
        tid = uuid.uuid4()
        self.__tid_list['credit'].append((str(tid), str(amt)))

    def withdraw(self, amt):
        """
        this method allows users to withdraw funds
        """

        if amt > self.acct_bal:
            return "Request declined, Insufficient Balance"

        self.acct_bal -= amt
        tid = uuid.uuid4()
        self.__tid_list['debit'].append((str(tid), str(amt)))

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
                    obj.__tid_list['debit'].append((str(tid), str(amt)))
                    break
        else:
            return "acct not found"

        self.__acct_bal -= amt
        self.__tid_list['credit'].append((str(tid), str(amt)))

    @property
    def tid_list(self):
        """
        this method shows customer transaction details
        """
        print("your acct number is {} and you have a balance of {}"
              .format(self.__acct_num, self.__acct_bal))
        return self.__tid_list

    @property
    def acct_num(self):
        """ this method returns acct_num """
        return self.__acct_num

    @property
    def acct_bal(self):
        """this method returns acct_bal"""
        return self.__acct_bal

    @acct_bal.setter
    def acct_bal(self, amt):
        """this method sets acct_bal"""
        self.__acct_bal = amt
