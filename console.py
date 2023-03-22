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
            storage.reload()
            ls_obj = storage.all()
            k = cl.replace(' ', '.')
            for key, value in ls_obj.items():
                if key == k:
                    val = value
            print(val)

    def do_destroy(self, cl):
        """
        This deletes a key and value pair of an instance stored
        in the file.json based on the class name and id
        """
        ls = cl.split(' ')
        val = "** no instance found **"

        if cl == '':
            print("** class name missing **")
        elif ls[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(ls) == 1:
            print("** instance id missing **")
        else:
            key = cl.replace(' ', '.')
            storage.reload()
            ls_obj = storage.all()
            if key in ls_obj:
                del ls_obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line=""):
        """
        This print all instance stored in file.json
        in dictionary format
        """

        storage.reload()
        dic = storage.all()
        ls = [str(dic[key]) for key in dic]
        if line == "" or line == "BaseModel":
            print(ls)
        else:
            print("** class doesn't exist **")

    def do_update(self, line=""):
        ls = line.split()
        # This code below avoid the attribute name added from saving
        # some specific data types

        st = ['"', "'"]
        if len(ls) >= 4:
            if ls[3].isdigit():
                ls[3] = int(ls[3])
                ls = [ls[i] for i in range(4)]
            else:
                try:
                    ls[3] = float(ls[3])
                    ls = [ls[i] for i in range(4)]
                except Exception:
                    if ls[3][0] not in st:
                        ls = [ls[i] for i in range(2)]
                    else:
                        ls = [ls[i] for i in range(4)]

        # This code below avoid the instance attribute of BaseModel
        # from being updated using the update command

        if len(ls) > 2:
            x = ['id', 'created_at', 'updated_at']
            for i in x:
                if i == ls[2]:
                    ls = [ls[i] for i in range(2)]
                    break

        # Main code Algorithm

        if len(ls) == 0 or ls[0] not in ["BaseModel"]:
            if len(ls) == 0:
                print("** class name missing **")
            elif ls[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
        elif len(ls) < 2:
            print("** instance id missing **")
        elif len(ls) < 3 or len(ls[2]) == 36 or ls[2] in ["BaseModel"]:
            print("** attribute name missing **")
        elif len(ls) < 4:
            print("** value missing **")
        else:
            key = f"{ls[0]}.{ls[1]}"
            storage.reload()
            ls_obj = storage.all()
            if key in ls_obj:
                if type(ls[3]) == str:
                    s = ''
                    for i in range(1, len(ls[3]) - 1):
                        s += ls[3][i]
                    ls[3] = s
                dic = {ls[2]: ls[3]}
                ls_obj[key].__dict__.update(dic)
                storage.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
