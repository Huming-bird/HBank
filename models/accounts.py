#!/usr/bin/python3

import uuid
from models.basemodel import Base

class Account(Base):
    """
    this class is a blue print for all account transactions
    """


    def __init__(self):
        """
        this is a placeholder to ovveride init
        """
        pass


    def deposit(self, amt):
        """
        this method allows users to deposit funds
        """

        if isinstance(amt, float) or isinstance(amt, int):

            self.acct_bal += amt
            tid = uuid.uuid4()
            self.tid_list.append({str(tid): ["Credit", str(amt)]})
        else:
            return "Pls provide a valid amount"


    def withdraw(self, amt):
        """
        this method allows users to withdraw funds
        """

        if isinstance(amt, float) or isinstance(amt, int):
            if amt > self.acct_bal:
                return "Request declined, Insufficient Balance"

            self.acct_bal -= amt
            tid = uuid.uuid4()
            self.tid_list.append({str(tid): ["Debit", str(amt)]})
        else:
            return "Pls provide a valid amount"


    def transfer(self, amt, acct_number):
        """
        this method allows customers to transfer funds
        """

        if not isinstance(amt, float) and not isinstance(amt, int):
            return "Pls enter a valid amount"

        for obj in Account.all_accts:
            if self.acct_num == acct_number:
                return "Transaction not allowed"
            if obj.acct_num == acct_number:
                if amt > self.acct_bal:
                    return "Request declined, Insufficient Balance"
                else:
                    obj.acct_bal += amt
                    tid = uuid.uuid4()
                    obj.tid_list.append({str(tid): ["Credit", str(amt)]})
                    break
        else:
            return "acct not found"

        self.acct_bal -= amt
        self.tid_list.append({str(tid): ["Debit", str(amt)]})
