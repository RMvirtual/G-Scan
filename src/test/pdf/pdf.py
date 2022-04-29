import unittest
import src.main.file_system.file_system as file_system
import src.main.pdf.reader as pdf_reader


class TestPdfReader(unittest.TestCase):
    def test_should_read_one_page_pdf(self):
        pdf_file_path = (
            file_system.test_resources_directory() +
            "/correct_files/one_page.pdf"
        )

        pdf_file = pdf_reader.read_pdf(source=pdf_file_path)
        no_of_pages = pdf_file.number_of_pages()
        correct_no_of_pages = 1

        self.assertEqual(correct_no_of_pages, no_of_pages)

    def test_should_read_three_page_pdf(self):
        pdf_file_path = (
            file_system.test_resources_directory() +
            "/correct_files/three_pages.pdf"
        )

        pdf_file = pdf_reader.read_pdf(source=pdf_file_path)
        no_of_pages = pdf_file.number_of_pages()
        correct_no_of_pages = 3

        self.assertEqual(correct_no_of_pages, no_of_pages)


if __name__ == "__main__":
    unittest.main()
