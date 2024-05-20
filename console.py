#!/usr/bin/python3
"""
Entry point for the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the AirBnB clone
    """
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
