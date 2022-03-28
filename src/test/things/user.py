import unittest
import sys
import os
from pathlib import Path

main_src_path = str(Path(os.getcwd()).parent) + "\\src"
sys.path.append(main_src_path)

import user
from user import User

class TestUser(unittest.TestCase):
    """A class for testing the user module."""

    def test_get_user_settings(self):
        current_user = user.get_user_settings()
        self.assertTrue(current_user.get_name() == "rmvir")
    
    def test_create_new_user(self):
        user_settings_data = user.get_user_settings_file_connection()
        new_user = user.create_new_user("Ryan", user_settings_data)

        self.assertTrue(new_user.get_name() == "Ryan")