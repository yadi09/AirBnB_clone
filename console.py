#!/usr/bin/env python3
"entry point of the command interpreter:"

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import sys


class HBNBCommand(cmd.Cmd):
    "entry point of the command interpreter:"
    
    prompt = "(hbnb) "

    def do_quit(self, arg):
        "exit the program"
        return True

    def do_EOF(self, arg):
        "exit the program"
        return True

    def help(self):
        return cmd.Cmd.help(self)

    def emptyline(self):
        pass

    def do_create(self, cls_name=None):
        arg_list = cls_name.split(" ")
        if cls_name == '':
            print("** class name missing **")
        else:
            try:
                self.obj = globals()[cls_name]()
            except Exception:
                print("** class doesn't exist **")
                return False

            self.obj.save()
            print(self.obj.id)

    def do_show(self, key=None):
        key_list = key.split(" ")
        if key == '':
            print("** class name missing **")
        else:
            try:
                cls_name = globals()[key_list[0]]
            except Exception:
                print("** class doesn't exist **")
                return False

            if len(key_list) == 2:
                key_str = ".".join(key_list)
                try:
                    print(self.obj.all()[key_str])
                except Exception:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

    def do_destroy(self, key=None):
        key_list = key.split(" ")
        if key == '':
            print("** class name missing **")
        else:
            try:
                cls_name = globals()[key_list[0]]
            except Exception:
                print("** class doesn't exist **")
                return False

            if len(key_list) > 1:
                key_str = ".".join(key_list)
                try:
                    del self.obj.all()[key_str]
                    self.obj.save()
                except Exception:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

    def do_all(self, cls_name=None):
        empty = True
        objs_list = []
        try:
            Cname = globals()[cls_name]
        except Exception:
            if cls_name != '':
                print("** class doesn't exist **")
                empty = False
        try:
            all_objs = self.obj.all()
            for key, value in all_objs.items():
                objs_list.append(str(value))
            print(objs_list)
        except Exception:
            if empty:
                print([])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
