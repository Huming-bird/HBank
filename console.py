#!/usr/bin/python3
""" console """

import cmd
from datetime import datetime
import models
from models.customers import Customer
from models.basemodel import BaseModel
from models.checkers import password_check
import shlex  # for splitting the line along spaces except in double quotes

classes = {"Customer": Customer}


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
            instance = classes[args[0]](**new_dict)
            if instance.signup():
                instance.create_acct()
                print(instance.acct_num)
                instance.save()
            else:
                print('something went wrong')
        else:
            print("** class doesn't exist **")
            return False

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** acct number missing **")
        args = shlex.split(arg)
        for key in models.storage.all():
            obj = models.storage.all()[key]
            if obj.acct_num == args[0]:
                print(obj)
            else:
                print("** customer not found **")

    def do_destroy(self, arg):
        """removes an instance from storage"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** acct number missing **")
        args = shlex.split(arg)
        for key in models.storage.all():
            obj = models.storage.all()[key]
            if obj.acct_num == args[0]:
                models.storage.all().pop(key)
                models.storage.save()
                break
        else:
            print("** customer not found **")

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
        for key in models.storage.all():
            obj = models.storage.all()[key]
            if obj.acct_num == args[0]:
                try:
                    if obj.login():
                        obj.deposit(int(args[1]))
                        obj.save()
                    else:
                        print('Login unsuccessful')
                    break
                except Exception as err:
                    print('Unsuccessful, Something went wrong')
                    break

        else:
            print('User not found')

    def do_withdraw(self, arg):
        """ this method initiates a withdrawal from customers """

        # passwd = input('password: \n')
        args = shlex.split(arg)
        for key in models.storage.all():
            obj = models.storage.all()[key]
            if obj.acct_num == args[0]:
                try:
                    if obj.login():
                        obj.withdraw(int(args[1]))
                        obj.save()
                    else:
                        print('Login unsuccessful')
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
        for key in models.storage.all():
            obj = models.storage.all()[key]
            if obj.acct_num == args[0]:
                if obj.login():  # for loop needs to be seperated
                    for key in models.storage.all():
                        obj2 = models.storage.all()[key]
                        if obj2.acct_num == args[1]:
                            try:
                                if obj.withdraw(int(args[2])):
                                    obj2.deposit(int(args[2]))
                                    obj.save()
                                    obj2.save()
                                    print("transfer successful")
                                    break
                                else:
                                    print('withdrawal not succesful')
                                    break
                            except Exception as err:
                                print("Unsuccessful, Something went wrong")
                                break
                    else:
                        print('Receiver acct not found')
                        break
                else:
                    print("Login Unsuccessful")
                break
            else:
                print('User not found')

    def do_update_password(self, arg):
        """ this method updates customer password """

        args = shlex.split(arg)
        for key in models.storage.all():
            obj = models.storage.all()[key]
            if obj.acct_num == args[0]:
                if password_check(args[1]):
                    obj.password = args[1]
                    print(f"Password for acct {args[0]} changed successfully")
                else:
                    print("Password change unsuccessful")
    
    def do_update_customer(self, arg):
        """ this method update scustomer details """

        args = shlex.split(arg)

        accept = ['first', 'last', 'mid', 'sex', 'dob', 'phone', 'email']

        for key in models.storage.all():
            obj = models.storage.all()[key]
            if obj.acct_num == args[0]:
                while True:
                    val = input('What do you want to update or press 7 to exit: ')
                    if val == '7':
                        break
                    if val in accept:
                        new_val = input('provide new {val}: ')
                        setattr(obj, val, new_val)
                        print(f'customer details {val} updated successfully')
                    else:
                        print('unacceptable values')
            else:
                print('Customer not found')

if __name__ == '__main__':
    HBANKCommand().cmdloop()
