from selenium import webdriver


class PDFViewer:
    """A class representing a PDF Viewer window that runs
    in Google Chrome."""

    def __init__(self):
        """Constructor method."""

        self.pdf_window = webdriver.Chrome()
        self.pdf_window.get("https://www.google.com")

    def show_image(self, file_name, scan_directory):
        """Loads image in Google Chrome."""

        self.pdf_window.get(
            "file:" + scan_directory + "/" + file_name)

    def close(self):
        """Closes the PDF viewer."""

        self.pdf_window.quit()
