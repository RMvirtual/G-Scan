import numpy
import unittest
import src.main.file_system.file_system as file_system
import src.main.pdf.reader as pdf_reader


class TestPdfReader(unittest.TestCase):
    DOCUMENT_HEIGHT = 300
    DOCUMENT_WIDTH = 300
    PIXEL_COLOURS = 3

    def test_should_read_300x300_pdf(self):
        self._populate_correct_pdf_values()

        pdf_path = (
            file_system.test_resources_directory() +
            "/correct_files/300x300.pdf"
        )

        page = pdf_reader.read_pdf(source=pdf_path)[0]

        self.assertEqual(self.DOCUMENT_HEIGHT, page.height)
        self.assertEqual(self.DOCUMENT_WIDTH, page.width)

        for row in range(self.DOCUMENT_HEIGHT):
            for column in range(self.DOCUMENT_WIDTH):
                pixel = page.pixel(row, column)
                correct_pixel = self.CORRECT_PDF_VALUES[column, row]

                for pixel_no in range(self.PIXEL_COLOURS):
                    self.assertEqual(
                        pixel[pixel_no], correct_pixel[pixel_no],
                        msg=("\nRow: " + str(row) + ", Column: " + str(column))
                    )

    def _populate_correct_pdf_values(self):
        black_pixels = self._150x300_matrix((255, 255, 255))
        white_pixels = self._150x300_matrix((0, 0, 0))

        self.CORRECT_PDF_VALUES = numpy.concatenate(
            (white_pixels, black_pixels), axis=0)

    def _150x300_matrix(self, fill_value):
        return numpy.full(
            shape=(150, 300, 3),
            fill_value=fill_value
        )


if __name__ == "__main__":
    unittest.main()
