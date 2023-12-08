#!/usr/bin/python3
""" This module contains the entry point of the command interpreter """
import unittest
from unittest.mock import patch
from io import StringIO
import os
import console
HBNBCommand = console.HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.hbnb = HBNBCommand()
        self.prompt = '(hbnb) '

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        with patch('builtins.input', return_value="quit"):
            self.hbnb.cmdloop()
            self.assertEqual(mock_stdout.getvalue(), self.prompt)

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        with patch('builtins.input', return_value="EOF"):
            self.hbnb.cmdloop()
            self.assertEqual(mock_stdout.getvalue(), self.prompt)

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        with patch('builtins.input', return_value=""):
            self.hbnb.cmdloop()
            self.assertEqual(mock_stdout.getvalue(), self.prompt)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        with patch('builtins.input', return_value="create BaseModel"):
            self.hbnb.cmdloop()
            self.assertIn("created", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        with patch('builtins.input', return_value="create BaseModel"):
            self.hbnb.cmdloop()
        with patch('builtins.input', return_value="show BaseModel"):
            self.hbnb.cmdloop()
            self.assertIn("created", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        with patch('builtins.input', return_value="create BaseModel"):
            self.hbnb.cmdloop()
        with patch('builtins.input', return_value="destroy BaseModel"):
            self.hbnb.cmdloop()
            self.assertNotIn("created", mock_stdout.getvalue())
