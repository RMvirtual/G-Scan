import unittest
import sys
import os
from pathlib import Path

main_src_path = str(Path(os.getcwd()).parent) + "\\src"
sys.path.append(main_src_path)

import app.validation.string_formatting as sf

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
                sf.remove_alphabetical_characters(string))

            is_not_alphabetic = not formatted_string.isalpha()
            self.assertTrue(is_not_alphabetic)



