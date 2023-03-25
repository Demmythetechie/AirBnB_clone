#!/usr/bin/python3
"""
"""


from cmd import Cmd
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.city import City


classes = ["BaseModel", "User", "Place", "State", "Amenity", "Review", "City"]



class HBNBCommand(Cmd):

    prompt = "(hbnb) "

    def do_EOF(self, Line):
        """Ends the command line prompt"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Returns prompt if no command is inputed"""
        pass

    def default(self, line):

        # Class Algoritm
        cls_name = ""
        for i in line:
            if i == ".":
                break
            else:
                cls_name += i


        line = line.split('"')

        # Command Algorithm
        ls = line[0].split('.')
        command = [ls[1][i] for i in range(len(ls[1]) - 1)]
        command = [i for i in command if i != '(']
        command = ''.join(command)


        # Input Algorithm
        arg = ""
        for i in range(len(line)):
            if i == 0:
                arg += cls_name + ' '
            if i % 2 != 0:
                if i == 5:
                    line[i] = '\"' + line[i] + '\"'
                    arg += line[i]
                else:
                    arg += line[i]
                if i != len(line) - 2:
                    arg += ' '


        if command == 'all':
            self.do_all(cls_name)
        elif command == 'count':
            self.do_count(cls_name)
        elif command == 'show':
            self.do_show(arg)
        elif command == 'destroy':
            self.do_destroy(arg)
        elif command == 'update':
            self.do_update(arg)
        


    def do_create(self, line=""):
        """Creates new instances of the base model class"""
        if line in classes:
            if line == "BaseModel":
                my_model = BaseModel()
            elif line == "User": 
                my_model = User()
            elif line == "Place":
                my_model = Place()
            elif line == "State":
                my_model = State()
            elif line == "Amenity":
                my_model = Amenity()
            elif line == "Review":
                my_model = Review()
            elif line == "City":
                my_model = City()
            storage.save()
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
        elif ls[0] not in classes:
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
        elif ls[0] not in classes:
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
        ls = []
        if line == "":
            ls = [str(dic[key]) for key in dic]
        elif line in classes:
            ls = [str(dic[key]) for key in dic if line in key]
        else:
            print("** class doesn't exist **")

        print(ls)


    def do_count(self, line):
        storage.reload()   
        dic = storage.all()
        ls = []
        if line in classes:
            ls = [str(dic[key]) for key in dic if line in key]
            count = len(ls)
        else:
            print("** class doesn't exist **")

        print(count)

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
                        if ls[3][-1] not in st or ls[len(ls) -1][-1] in st:
                            for i in range(4, len(ls)):
                                if ls[i][-1] not in st:
                                    ls[3] = ls[3] + " " + ls[i]
                                else:
                                    ls[3] = ls[3] + " " + ls[i]
                                    break
                            ls = [ls[i] for i in range(4)]
                        else:
                            ls = [ls[i] for i in range(2)]


        # This code below avoid the instance attribute of BaseModel
        # from being updated using the update command

        if len(ls) > 2:
            x = ['id', 'created_at', 'updated_at']
            for i in x:
                if i == ls[2]:
                    ls = [ls[i] for i in range(2)]
                    break

        # Main code Algorithm

        if len(ls) == 0 or ls[0] not in classes:
            if len(ls) == 0:
                print("** class name missing **")
            elif ls[0] not in classes:
                print("** class doesn't exist **")
        elif len(ls) < 2:
            print("** instance id missing **")
        elif len(ls) < 3 or len(ls[2]) == 36 or ls[2] in classes:
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
