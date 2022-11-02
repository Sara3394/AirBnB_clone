#!/usr/bin/python3
""""Uses Cmd module"""
import re
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models import storage
class HBNBCommand(cmd.Cmd):
    """Class HBNB"""
    prompt = "(hbnb)"
    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ End of file marker"""
        return True

    def emptyline(self):
        """Empty commad"""
        pass

    def do_create(self, line):
        """ creates class instance """
        if len(line) == 0:
            print("** class name missing **")
        elif globals().get(line) is None:
            print("** class doesn't exist **")
        else:
            ins = eval(line)()
            ins.save()
            print(ins.id)

    def do_show(self, line):
        """show instance"""
        a = []
        for m in line.split(" "):
            a.append(m)
        if len(line) == 0:
            print("** class name missing **")
        elif globals().get(a[0]) is None:
            print("** class doesn't exist **")
        elif len(a) == 1:
            print("** instance id missing **")
        elif a[0]+"."+a[1] not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[a[0]+"."+a[1]])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        a = []
        for m in line.split(" "):
            a.append(m)
        if len(line) == 0:
            print("** class name missing **")
        elif globals().get(a[0]) is None:
            print("** class doesn't exist **")
        elif len(a) == 1:
            print("** instance id missing **")
        elif a[0] + "." + a[1] not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[a[0] + "." + a[1]]
            storage.save()
    def do_all(self, line):
        """  Prints all string representation of all instances based or not on the class name """
        if len(line) == 0:
            for k, v in storage.all().items():
                print(storage.all())
        elif globals().get(line) is None:
            print("** class doesn't exist **")
        else:
            for k, v in storage.all().items():
                if line in k:
                    print(storage.all()[k])
    def default(self, line):
        """custom """
        a = []
        for i in line.split('.'):
            a.append(i)
        if len(line) < 1:
            print("format Error")
        elif globals().get(a[0]) is None:
            print("** class doesn't exist **")
        else:
            check_c = re.sub("[\(\[].*?[\)\]]", "", a[1])
            if check_c == "all":
                HBNBCommand.do_all(self, a[0])
            elif check_c == "count":
                HBNBCommand.count(self, a[0])
            elif check_c == "show":
                HBNBCommand.do_show(self,a[0]+" "+a[1][len(re.sub("[\(\[].*?[\)\]]", "", a[1]))+2:-2])
            elif check_c == "destroy":
                HBNBCommand.do_destroy(self, a[0] + " " + a[1][len(re.sub("[\(\[].*?[\)\]]", "", a[1])) + 2:-2])
            elif check_c == "update":
                lists = a[1][len(re.sub("[\(\[].*?[\)\]]", "", a[1])) + 1:-1].split(",")
                l1 = lists[0].replace('"',"").strip()
                p = lists[1].replace('"',"").strip() + " " + lists[2].replace('"',"").strip()
                HBNBCommand.do_update(self, a[0] + " " + l1 + " " + p)

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or updating attribute """
        a = []
        for m in line.split(" "):
            a.append(m)
        if len(line) == 0:
            print("** class name missing **")
        elif globals().get(a[0]) is None:
            print("** class doesn't exist **")
        elif len(a) == 1:
            print("** instance id missing **")
        elif a[0] + "." + a[1] not in storage.all():
            print("** no instance found **")
        elif len(a) == 2:
            print("** attribute name missing **")
        elif len(a) == 3:
            print("** value missing **")
        else:
            for k,v in storage.all().items():
               if a[0] + "." + a[1] == k:
                   #print(storage.all()[k])
                   setattr(storage.all()[k], a[2], a[3])
                   storage.save()
                   break
    def count(self, line):
        """ count instances"""
        i = 0
        if len(line) == 0:
            print("** class name missing **")
        elif globals().get(line) is None:
            print("** class doesn't exist **")
        else:
            for k, v in storage.all().items():
                if line in k:
                    i = i + 1
            print(i)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
