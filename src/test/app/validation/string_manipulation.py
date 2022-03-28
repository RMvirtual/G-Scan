import unittest
import sys
import os
from pathlib import Path

main_src_path = str(Path(os.getcwd()).parent) + "\\src"
sys.path.append(main_src_path)

import app.validation.string_manipulation as sm

class TestStringFormatting(unittest.TestCase):
    """A class for testing the string formatting module."""

    def test_remove_alphanumeric_characters(self):
        strings_to_test = [
            "GR190100100",
            "lolololol",
            "100000"
        ]

        for string in strings_to_test:
            formatted_string = (
                sm.remove_alphabetical_characters(string))

            is_not_alphabetic = not formatted_string.isalpha()
            self.assertTrue(is_not_alphabetic)

    def test_overwrite_string_from_right(self):
        strings_to_test = [
            "GR190100100",
            "lolololol",
            "100000"
        ]

        correct_strings = [
            "GR190100hai",
            "lololohai",
            "100hai"
        ]

        for string in strings_to_test:
            overwritten_string = sm.overwrite_from_right(string, "hai")
            self.assertTrue(overwritten_string in correct_strings)

if __name__ == '__main__':
    unittest.main()