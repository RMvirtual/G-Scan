import unittest
import src.main.file_names.name_scheme as file_naming
import src.main.file_system.file_system as file_system

class TestFileNames(unittest.TestCase):
    def test_should_create_backup_file_name_with_no_page_suffix(self):        
        file_name = file_naming.backup_file_name(
            self.__file_naming_attributes(), self.__backup_directory())

        correct_file_name = "GR190100200_POD.pdf"
        self.assertEqual(correct_file_name, file_name)

    def __file_naming_attributes(self) -> file_naming.FileNamingAttributes:
        attributes = file_naming.FileNamingAttributes()
        attributes.job_reference = "GR190100200"
        attributes.paperwork_type = "POD"
        attributes.page_number = None
        attributes.file_extension = ".pdf"
        attributes.input_mode = "Normal"

        return attributes
        
    def __backup_directory(self) -> str:
        return file_system.test_resources_directory() + "/backup"


if __name__ == '__main__':
    unittest.main()