import unittest
import os

import src.main.file_names.naming_scheme as fn
import src.main.file_system.file_system as fs

class TestFileNaming(unittest.TestCase):
    """A class for testing the file naming module."""

    def test_create_backup_file_name(self):
        file_name = self.create_dummy_file_name_structure()
        backup_directory = self.get_backup_directory()

        backup_file_name = fn.create_backup_file_name(
            file_name, backup_directory)

        self.assertTrue(
            backup_file_name == "GR190100200_POD.pdf",
            "Backup file name is actually: " + backup_file_name
        )

    def test_setup_and_tear_down(self):
        backup_directory = self.get_backup_directory()
        file_name = "GR190100200.pdf"

        self.setup_one_file(file_name, backup_directory)
        file_exists = fs.file_exists(file_name, backup_directory)
        self.assertTrue(file_exists)

        self.remove_one_file(file_name, backup_directory)
        file_removed = not fs.file_exists(file_name, backup_directory)
        self.assertTrue(file_removed)

    def setup_one_file(self, file_name: str, directory: str):
        f = open(directory + "\\" + file_name, "w")
        f.close()

    def remove_one_file(self, file_name: str, directory: str):
        os.remove(directory + "\\" + file_name)

    def create_dummy_file_name_structure(self) -> fn.FileNamingAttributes:
        file_name = fn.FileNamingAttributes()
        file_name.job_reference = "GR190100200"
        file_name.paperwork_type = "POD"
        file_name.file_extension = ".pdf"
        file_name.input_mode = "Normal"

        return file_name
        
    def get_backup_directory(self) -> str:
        return "C:\\Users\\rmvir\\Desktop\\testfolder\\backup"

if __name__ == '__main__':
    unittest.main()