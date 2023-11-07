#!/usr/bin/python3
""" console """

import cmd
from datetime import datetime
import models
import os
from models.customer import Customer
from models.basemodel import BaseModel
from models.account import Account
from models.auth import Authentication
from models.checkers import password_check
import shlex  # for splitting the line along spaces except in double quotes

classes = {"Customer": Customer, "Account": Account, "Authentication": Authentication}

models.storage_t = 'db'
class HBANKCommand(cmd.Cmd):
    """ HBANK console """
    prompt = '(hbank) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] == "Customer":
            new_dict = self._key_value_parser(args[1:])
            instance = Customer(**new_dict)
            #auth = Authentication(id=instance.id)
            acct = Account(id=instance.id)
            #if auth.signup():
            acct.create_acct()
            print("account created successfully")
            print(f" This is your acct num {acct.acct_num}")
            instance.save()
            #auth.save()
            acct.save()
            #else:
             #   print('something went wrong. Provide a strong password and try again')
        else:
            print("** class doesn't exist **")
            return False

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** acct number missing **")
        args = shlex.split(arg)
        for key, val in models.storage.all().items():
            if 'Account' in key:
                if val.acct_num == args[0]:
                    id = val.id
                    break
        for i in classes:
            try:
                if id:
                    key = i + '.' + id
                    print(models.storage.all()[key])
            except Exception as err:
                print("** Customer not found **")
                break

    def do_destroy(self, arg):
        """removes an instance from storage"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** acct number missing **")
        for key, val in models.storage.all().items():
            if 'Account' in key:
                if val.acct_num == args[0]:
                    id = val.id
                    break
        for i in classes:
            try:
                if id:
                    key = i + '.' + id
                    models.storage.all().pop(key)
                    models.storage.save()
            except Exception as err:
                print("** customer not found **")
                break

    def do_all(self, arg):
        """Prints string representations of instances"""

        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_deposit(self, arg):
        """ this method initiates a deposit for customers """

        # passwd = input('password: \n')
        args = shlex.split(arg)
        for key, val in models.storage.all().items():
            if 'Account' in key:
                if val.acct_num == args[0]:
                    id = val.id
                    obj = 'Authentication' + '.' + id
                    obj = models.storage.all()[obj]
                    try:
                        if obj.login():
                            val.deposit(int(args[1]))
                            val.save()
                            print('Transaction Successful')
                        else:
                            print('Pls check your password and try again')
                        break
                    except Exception as err:
                        print('Unsuccessful, Something went wrong')
                        break

        else:
            print('User not found')

    def do_withdraw(self, arg):
        """ this method initiates a withdrawal for customers """

        # passwd = input('password: \n')
        args = shlex.split(arg)
        for key, val in models.storage.all().items():
            if 'Account' in key:
                if val.acct_num == args[0]:
                    id = val.id
                    obj = 'Authentication' + '.' + id
                    obj = models.storage.all()[obj]
                    try:
                        if obj.login():
                            val.withdraw(int(args[1]))
                            val.save()
                            print('Transaction Successful')
                        else:
                            print('Pls check your password and try again')
                        break
                    except Exception as err:
                        print('Unsuccessful, Something went wrong')
                        break
        else:
            print('User not found')

    def do_transfer(self, arg):
        """ this method initiates a deposit for customers """

        # passwd = input('password: \n')
        args = shlex.split(arg)
        frm = args[0]
        to = args[1]
        amt = args[2]
        acct2 = ""
        for key, obj in models.storage.all().items():
            if 'Account' in key:
                if obj.acct_num == args[0]:
                    id = obj.id
                    auth1 = 'Authentication' + '.' + id
                    auth1 = models.storage.all()[auth1]
                    acct1 = obj
                elif obj.acct_num == args[1]:
                    id = obj.id
                    acct2 = obj
        if isinstance(acct2, Account):
            try:
                if auth1.login():
                    try:
                        if acct1.withdraw(int(args[2])):
                            acct2.deposit(int(args[2]))
                            acct1.save()
                            acct2.save()
                            print("transfer successful")
                        else:
                            print('withdrawal not succesful')
                    except Exception as err:
                        print("Unsuccessful, Something went wrong")
                else:
                    print("Login Unsuccessful")
            except Exception as err:
                print('User not found')
        else:
            print('Receiver acct not found')

    def do_update_password(self, arg):
        """ this method updates customer password """

        args = shlex.split(arg)
        for key, val in models.storage.all().items():
            if 'Account' in key:
                if val.acct_num == args[0]:
                    id = val.id
                    k = 'Authentication' + '.' + id
                    obj = models.storage.all()[k]
                    break
        try:
            if password_check(args[1]):
                obj.password = args[1]
                print(f"Password for acct {args[0]} changed successfully")
                obj.save()
            else:
                print("Password change unsuccessful")
        except Exception as err:
            print("try again, something went wrong")
            

    def do_update_customer(self, arg):
        """ this method update scustomer details """

        args = shlex.split(arg)

        accept = ['first', 'last', 'mid', 'sex', 'dob', 'phone', 'email']

        for key, val in models.storage.all().items():
            if 'Account' in key:
                if val.acct_num == args[0]:
                    id = val.id
                    user = 'Customer' + '.' + id
                    user = models.storage.all()[user]
                    while True:
                        val = input('provide attrib to update (press 7 to exit): ')
                        if val == '7':
                            break
                        if val in accept:
                            new_val = input('provide new {val}: ')
                            setattr(user, val, new_val)
                            print(f'customer details {val} updated successfully')
                            user.save()
                        else:
                            print('unacceptable change')
                else:
                    print('Customer not found')


if __name__ == '__main__':
    HBANKCommand().cmdloop()
