import unittest
import sys
import os
from pathlib import Path

main_src_path = str(Path(os.getcwd()).parent) + "\\src"
sys.path.append(main_src_path)

import app.validation.file_naming as fn

class TestFileNaming(unittest.TestCase):
    """A class for testing the file naming module."""

    def test_create_backup_file_name(self):
        pass

    