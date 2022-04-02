import unittest
import src.main.file_system.file_system as file_system
from src.main.pdf.reader import PdfReader


class TestPdfReader(unittest.TestCase):
    def test_should_get_number_of_pages(self):
        pdf_file = (
            file_system.test_resources_directory() +
            "/correct_files/one_page.pdf"
        )

        reader = PdfReader(source=pdf_file)
        no_of_pages = reader.number_of_pages()
        correct_no_of_pages = 1

        self.assertEqual(correct_no_of_pages, no_of_pages)


if __name__ == '__main__':
    unittest.main()
