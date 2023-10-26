#!/usr/bin/python3

from models.customers import Customer
import models

class Account(Customer):
    all_accts = []

    def __init__(self, customer):
        if isinstance(customer, Customer):
            self.id = customer.id
            self.acct_num = customer.acct_num
            self.acct_bal = 0
            self.tid_list = []
            Account.all_accts.append(self)
        else:
            return "Kindly provide a valid bank user"


    def deposit(self, amt):

        if isinstance(amt, float) or isinstance(amt, int):

            self.acct_bal += amt
            tid = uuid.uuid4()
            self.tid_list.append({str(tid): ["Credit", str(amt)]})
        else:
            return "Pls provide a valid amount"

    def withdraw(self, amt):

        if isinstance(amt, float) or isinstance(amt, int):
            if amt > self.acct_bal:
                return "Request declined, Insufficient Balance"

            self.acct_bal -= amt
            tid = uuid.uuid4()
            self.tid_list.append({str(tid): ["Debit", str(amt)]})
        else:
            return "Pls provide a valid amount"

    def transfer(self, amt, acct_number):

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
