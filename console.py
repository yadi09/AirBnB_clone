#!/usr/bin/env python3
"entry point of the command interpreter:"

import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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

    def do_count(self, arg):
        count = 0
        obj_dict = storage.all()
        for key in obj_dict:
            if (arg in key):
                count += 1
        print(count)

    def precmd(self, line):
        if '.' in line and "()" in line:
            parts = line.replace("()", "").split(".")
            parts.reverse()
            line = " ".join(parts)
        elif "." in line and "(\"" in line:
            parts = line.replace(".", " ")
            parts = parts.replace("(\"", " ").replace("\")", " ")
            parts = parts.split(" ")
            temp = parts[0]
            parts[0] = parts[1]
            parts[1] = temp
            line = " ".join(parts)
        return cmd.Cmd.precmd(self, line)

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
        if empty:
            try:
                all_objs = self.obj.all()
                for key, value in all_objs.items():
                    objs_list.append(str(value))
                    print(objs_list)
            except Exception:
                if empty:
                    print([])

    def do_update(self, args):
        args_list = args.split(" ")
        TF = True

        if args == '':
            print("** class name missing **")
            TF = False
        elif TF:
            try:
                cls_name = globals()[args_list[0]]
            except Exception:
                print("** class doesn't exist **")
                TF = False

        if len(args_list) < 2 and TF:
            print("** instance id missing **")
            TF = False
        elif TF:
            key = ".".join(args_list[:2])
            try:
                key_value = self.obj.all()[key]
            except Exception:
                print("** no instance found **")
                TF = False

        if len(args_list) < 3 and TF:
            print("** attribute name missing **")
            TF = False
        elif len(args_list) < 4 and TF:
            print("** value missing **")
            TF = False
        elif TF:
            attr = args_list[2]
            value = args_list[3]
            self.obj.update_object(key, attr, value.replace("\"", ""))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
