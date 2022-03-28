import unittest
from src.main.user.user import *

class TestUser(unittest.TestCase):
    """A class for testing the user module."""

    def test_get_user_settings(self):
        current_user = get_user_settings()
        self.assertTrue(current_user.get_name() == "rmvir")
    
    def test_create_new_user(self):
        user_settings_data = get_user_settings_file_connection()
        new_user = create_new_user("Ryan", user_settings_data)

        self.assertTrue(new_user.get_name() == "Ryan")

if __name__ == '__main__':
    unittest.main()