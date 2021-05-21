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

        print(current_user.get_name())

        self.assertTrue(current_user.get_name() == "rmvir")

        