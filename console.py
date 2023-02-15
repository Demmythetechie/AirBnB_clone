#!/usr/bin/python3

"""
"""

from cmd import Cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(Cmd):

    prompt = "(hbnb) "

    def do_EOF(self, Line):
        """Ends the command line prompt"""
        return True

    def emptyline(self , line):
        """This ignores an empty line in the command prompt"""

        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line=""):
        """Creates new instances of the base model class"""
        if line == "BaseModel":
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)
        elif line == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, cl=''):
        """Prints the string representation of an instance based
        on the class name and id"""

        ls = cl.split(' ')
        val = "** no instance found **"

        if cl == '':
            print("** class name missing **")
        elif ls[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(ls) == 1:
            print("** instance id missing **")
        else:
            ls_obj = storage.all()
            k = cl.replace(' ', '.')
            for key, value in ls_obj.items():
                if key == k:
                    val = value
            print(val)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
