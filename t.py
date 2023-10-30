#!/usr/bin/python3
from models import storage
from models.basemodel import BaseModel
from models.customers import Customer
from models.accounts import Account

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = Customer(first='nike', last='ola', dob='1996-04-20', email='ahmed.ola@gmail.com', sex='female', acct_type='savings')
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = Customer(first='ahmed', last='ola', dob='1996-04-20', email='ahmed.ola@gmail.com', sex='male', acct_type='savings')
my_user2.save()
print(my_user2)

print("-- Create a new account --")
user_1_acct = Account(my_user)
user_2_acct = Account(my_user2)
print(user_1_acct)
print(user_2_acct)
