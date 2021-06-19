from pathlib import Path
import sys
import unittest

main_src_path = Path.cwd().parent.joinpath("src")
sys.path.append(main_src_path)

import app.file_system as file_system

class TestFileSystem(unittest.TestCase):
    """A class for testing the file system module."""

    def test_get_current_directory(self):
        correct_directory = Path("C:/Users/rmvir/Desktop/gscan/G-Scan/test")
        current_directory = file_system.get_current_directory()

        self.assertEqual(correct_directory, current_directory)

    def test_get_root_directory(self):
        correct_directory = Path("C:/Users/rmvir/Desktop/gscan/G-Scan")
        root_directory = file_system.get_root_directory()

        self.assertEqual(correct_directory, root_directory,
            "Root directory returned is " + str(root_directory))