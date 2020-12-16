from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PDFViewer():
    """A class representing a PDF Viewer window that runs
    in Google Chrome."""

    def __init__(self):
        """Constructor method."""

        self.pdf_window = webdriver.Chrome()
        self.pdf_window.get("https://www.google.com")

    def show_image(self, master_application, file_name, scan_directory):
        """Loads image in Google Chrome."""

        master_application.write_log("Displaying " + file_name)
        self.pdf_window.get("file:" + scan_directory + "/" + file)

    def close(self):
        """Closes the PDF viewer."""

        self.pdf_window.quit()
    
