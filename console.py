#!/usr/bin/python3
"""
This module helps bring our code to live using a cmd interpreter
as the frontend for now. The cmd module act as a testing frontend
making it easy to test and debug our code easily without a GUI
frontend
"""
from cmd import Cmd


class HBNBCommand(Cmd):
    """
    This class contains all the command method
    that will be used during the testing
    """

    prompt = "(hbnb) "

    def do_quit(self, par1):
        """This exits the Command line interpreter"""
        return True

    def do_EOF(self, par1):
        """This exits the Command line interpreter"""
        return True

    def emptyline(self):
        return ''


if __name__ == '__main__':
    HBNBCommand().cmdloop()
