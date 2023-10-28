#!/usr/bin/python3

from models.basemodel import BaseModel, Base
from models.authentication import Authentication
from models.customers import Customer
from models.accounts import Account
from models.checkers import password_check
from models import storage
from models.basemodel import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("=================================")
ahmed = Customer()
ahmed.first = 'Ahmed'
ahmed.last = 'Ola'
ahmed.sex = 'Male'
ahmed.email = 'ahmed.ola@email.com'
ahmed.dob = '1996-04-20'
ahmed.phone = '08127929274'
#ahmed.save()

nike = Customer()
nike.first = 'Nike'
nike.last = 'tianah'
nike.sex = 'Female'
nike.email = 'nike.tianah@email.com'
nike.dob = '1997-10-15'
nike.phone = '08159963648'
#nike.save()

print(ahmed)
print(nike)

ahmed.update_password('Ahmed100$')

print("==========================================")

ahmed.deposit(1500)
ahmed.withdraw(300)
#ahmed.transfer(200)
ahmed.save()

print(ahmed)

