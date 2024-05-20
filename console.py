#!/usr/bin/python3
"""
Entry point for the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the AirBnB clone
    """
    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # To ensure the prompt goes to a new line
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print([str(obj) for obj in storage.all().values()])
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in storage.all().values() if type(obj).__name__ == arg])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            setattr(obj, attr_name, attr_type(attr_value))
        else:
            setattr(obj, attr_name, attr_value)
        obj.save()

    def do_help(self, arg):
        """Help command to show the list of available commands"""
        if arg:
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                print(f"No help on {arg}")
                return
            func()
        else:
            cmd.Cmd.do_help(self, arg)

    def default(self, line):
        """Handle commands in the form <class name>.action()"""
        if '.' not in line:
            print("*** Unknown syntax: {}".format(line))
            return
        try:
            cls_name, command = line.split('.')
            command, args = command.split('(')
            args = args.rstrip(')')
            if cls_name not in self.classes:
                print("** class doesn't exist **")
                return
            if command == "all":
                self.do_all(cls_name)
            elif command == "count":
                self.do_count(cls_name)
            elif command == "show":
                self.do_show(f"{cls_name} {args.strip('\"')}")
            elif command == "destroy":
                self.do_destroy(f"{cls_name} {args.strip('\"')}")
            elif command == "update":
                self.do_update(f"{cls_name} {args.replace(', ', ' ')}")
            else:
                print("*** Unknown syntax: {}".format(line))
        except ValueError:
            print("*** Unknown syntax: {}".format(line))

    def do_count(self, cls_name):
        """Retrieve the number of instances of a class"""
        count = sum(1 for obj in storage.all().values() if type(obj).__name__ == cls_name)
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
