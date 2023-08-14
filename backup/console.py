#!/usr/bin/python3
"""
HBNBCommand class used to make a command line interpretr
"""
import re
from shlex import split
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class inherits from the cmd class
    used to simulate a command line interpreter with python
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "Review",
        "Place",
        "State",
        "City",
        "Amenity"
    }

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg):
        """
        create a new class instance with given
        key value and prints the id in return
        """
        try:
            if not arg:
                raise SyntaxError()
            my_list = arg.split(" ")
            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = tuple(my_list[i].split("="))
                if value[0] == '""':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        display the string representation of a
        class instance of a given id
        """
        arg = parse(arg)
        objdict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, line):
        """
        delete a class instance of given id
        """
        args = parse(line)
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], arg[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict[f"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, line):
        """
        display string representation of all instances of
        a given class . if no class specifiied displays
        all instantiated ojects.
        """
        args = parse(line)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objs = []
            objs_in_storage = storage.all()
            for obj in objs_in_storage.values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objs.append(obj.__str__())
                elif len(args) == 0:
                    objs.append(obj.__str__())
            print(objs)

    def do_update(self, line):
        """
        update a class instance of given id by adding or updating atributes.
        """
        args = parse(line)
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        if len(args) == 1:
            print("** instance id missing **")
        if f"{args[0]}.{args[1]}" not in objdict.values():
            print("** no instance found **")
        if len(args) == 2:
            print("** attribute name missing **")
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")

        if len(args) == 4:
            obj_to_update = objdict[f"{args[0]}.{arg[1]}"]
            if args[2] in obj_to_update.__class__.__dict__.keys():
                value_type = type(obj_to_update.__class__.__dic__[args[2]])
                obj_to_update.__dict__[args[2]] = value_type(args[3])
            else:
                obj_to_update.__dict__[args[2]] = args[3]

        storage.save()

    def emptyLine(self):
        """do nothing upon recieving an empty line"""
        pass

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """end of file signal to quit the program"""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
