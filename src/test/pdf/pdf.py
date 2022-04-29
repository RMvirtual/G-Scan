import unittest
import src.main.file_system.file_system as file_system
import src.main.pdf.reader as pdf_reader


class TestPdfReader(unittest.TestCase):
    def test_should_read_one_page_pdf(self):
        pdf_file_path = (
            file_system.test_resources_directory() +
            "/correct_files/one_page.pdf"
        )

        self._open_pdf_file_and_check_page_quantity(pdf_file_path, 1)

    def test_should_read_three_page_pdf(self):
        pdf_file_path = (
            file_system.test_resources_directory() +
            "/correct_files/three_pages.pdf"
        )

        self._open_pdf_file_and_check_page_quantity(pdf_file_path, 3)

    def _open_pdf_file_and_check_page_quantity(
            self, file_path: str, correct_no_of_pages: int):
        pdf_file = pdf_reader.read_pdf(source=file_path)
        self.assertEqual(correct_no_of_pages, pdf_file.number_of_pages())

    def test_should_write_pdf(self):
        pdf_file = self._setup_pdf()

        output_path = (
            file_system.test_resources_directory() +
            "/output/pdf_write_attempt.pdf"
        )

        pdf_writer.write_pdf(pdf_file, output_path)
        self._open_pdf_file_and_check_page_quantity(output_path, 1)


if __name__ == "__main__":
    unittest.main()
