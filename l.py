#!/usr/bin/python3
from models import storage
from models.basemodel import BaseModel
from models.customers import Customer

print("-- Create a new Customer--")
customer = Customer()
customer.first = 'ahmed'
customer.last = 'ola'
customer.save()
print(customer)

cus = Customer()
cus.first = 'tolu'
cus.save()

cus.deposit(1500)
cus.transfer(200, customer)

print(cus.__dict__)
print(customer.__dict__)
