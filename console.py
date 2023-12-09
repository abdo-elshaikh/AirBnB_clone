#!/usr/bin/python3
""" HBNB console"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ This command interpreter class """
    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        try:
            my_model = eval(args[0] + "()")
            my_model.save()
            print(my_model.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, line):
        """Prints all string representations of all
        instances based on the class name"""
        args = line.split()
        instance = []
        if len(args) == 0:
            for k, v in models.storage.all().items():
                instance.append(str(v))
            print(instance)
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        for k, v in models.storage.all().items():
            if args[0] == k.split('.')[0]:
                instance.append(str(v))
        print(instance)

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        """
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(models.storage.all()[key], args[2], args[3])
        models.storage.save()

    def do_count(self, line):
        """Prints the number of instances of a class"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        count = 0
        for k, v in models.storage.all().items():
            if args[0] == k.split('.')[0]:
                count += 1
        print(count)

    def default(self, line):
        """Handles unknown commands"""
        args = line.split(".")
        if len(args) == 2 and args[0] in self.classes:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                self.do_count(args[0])
            elif args[1].split("(")[0] == "show":
                self.do_show(args[0] + " " + args[1].split("(")[1][:-1])
            elif args[1].split("(")[0] == "destroy":
                self.do_destroy(args[0] + " " + args[1].split("(")[1][:-1])
            elif args[1].split("(")[0] == "update":
                self.do_update(
                    args[0] + " " + args[1].split("(")[1][:-1] + " "
                )
            else:
                print("*** Unknown syntax: {}".format(line))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
