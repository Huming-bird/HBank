#!/usr/bin/python3
""" console """

import cmd
from datetime import datetime
import models
from models.customers import Customer
from models.basemodel import BaseModel
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
            
            instance.create_acct()
            print(instance.acct_num)
            instance.save()
        else:
            print("** class doesn't exist **")
            return False

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

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

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in Customer:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except Exception as err:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except Exception as err:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

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

    def do_password(self, arg):
        args = shlex.split(arg)
        for key in models.storage.all():
            obj = models.storage.all()[key]
            if obj.acct_num == args[0]:
                print(obj.password)


if __name__ == '__main__':
    HBANKCommand().cmdloop()
