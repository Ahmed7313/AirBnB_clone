import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test class for console.py"""

    def test_help(self):
        """Test the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
            self.assertIn("Documented commands (type help <topic>):", output)

    def test_help_quit(self):
        """Test the help quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            output = f.getvalue()
            self.assertIn("Quit command to exit the program", output)

    def test_help_EOF(self):
        """Test the help EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            output = f.getvalue()
            self.assertIn("EOF command to exit the program", output)

    def test_create_missing_class(self):
        """Test create command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue()
            self.assertIn("** class name missing **", output)

    def test_create_invalid_class(self):
        """Test create command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            output = f.getvalue()
            self.assertIn("** class doesn't exist **", output)

    def test_create_valid_class(self):
        """Test create command with valid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue()
            self.assertTrue(len(output.strip()) > 0)

    def test_show_missing_class(self):
        """Test show command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue()
            self.assertIn("** class name missing **", output)

    def test_show_invalid_class(self):
        """Test show command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            output = f.getvalue()
            self.assertIn("** class doesn't exist **", output)

    def test_show_missing_id(self):
        """Test show command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            output = f.getvalue()
            self.assertIn("** instance id missing **", output)

    def test_show_invalid_id(self):
        """Test show command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 1234-5678-9101")
            output = f.getvalue()
            self.assertIn("** no instance found **", output)

    def test_all_invalid_class(self):
        """Test all command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            output = f.getvalue()
            self.assertIn("** class doesn't exist **", output)

    def test_destroy_missing_class(self):
        """Test destroy command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue()
            self.assertIn("** class name missing **", output)

    def test_destroy_invalid_class(self):
        """Test destroy command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            output = f.getvalue()
            self.assertIn("** class doesn't exist **", output)

    def test_destroy_missing_id(self):
        """Test destroy command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            output = f.getvalue()
            self.assertIn("** instance id missing **", output)

    def test_destroy_invalid_id(self):
        """Test destroy command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 1234-5678-9101")
            output = f.getvalue()
            self.assertIn("** no instance found **", output)

    def test_update_missing_class(self):
        """Test update command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            output = f.getvalue()
            self.assertIn("** class name missing **", output)

    def test_update_invalid_class(self):
        """Test update command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
            output = f.getvalue()
            self.assertIn("** class doesn't exist **", output)

    def test_update_missing_id(self):
        """Test update command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            output = f.getvalue()
            self.assertIn("** instance id missing **", output)

    def test_update_invalid_id(self):
        """Test update command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 1234-5678-9101")
            output = f.getvalue()
            self.assertIn("** no instance found **", output)

    def test_update_missing_attribute_name(self):
        """Test update command with missing attribute name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 1234-5678-9101")
            output = f.getvalue()
            self.assertIn("** attribute name missing **", output)

    def test_update_missing_value(self):
        """Test update command with missing value"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 1234-5678-9101 first_name")
            output = f.getvalue()
            self.assertIn("** value missing **", output)

    def test_update_with_dict(self):
        """Test update command with dictionary"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User 1234-5678-9101 {"first_name": "John", "age": 89}')
            output = f.getvalue()
            self.assertIn("** no instance found **", output)


if __name__ == "__main__":
    unittest.main()
