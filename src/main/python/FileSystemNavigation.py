import os

class FileSystemNavigation():
    """A class for providing file system functionalities."""

    def __init__(self):
        """Constructor method."""

        pass

    def get_item_directory(self, path):
        """Gets the directory of a path."""

        directory, item = os.path.split(path)

        return directory

    def get_full_path(self, path):
        """Returns the absolute version of a path."""

        return os.path.abspath(path)

    def delete_file(self, path):
        """Deletes a file in a path."""

        os.remove(path)

    def get_current_path(self):
        """Gets the full current working path the file using this
        method resides in."""

        return os.getcwd()
    
    def get_directory_items(self, path):
        """Returns a list of folders and files in a directory."""
        return os.listdir(path)

    def get_directory_path(self):
        """Gets the directory path of the G-Scan folder that all the files
        and subfolders reside in."""

        current_path = self.get_current_path()

        directory_structure = current_path.split("\\")
        directory_path = ""

        for folder in directory_structure:
            directory_path += folder + "\\"

            if folder == "G-Scan":
                break
        
        return directory_path

    def get_base_name(self, path):
        """Returns the full file name (including the extension) of a
        file from a given path."""

        return os.path.basename(path) 

    def get_file_name(self, path):
        """Returns the name of a file (excluding the extension) of a
        file from a given path."""

        base_name = self.get_base_name(path)
        file_name, file_ext = os.path.splitext(base_name)

        return file_name

    def get_file_ext(self, path):
        """Returns the name of a file (excluding the extension) of a
        file from a given path."""

        base_name = self.get_base_name(path)
        file_name, file_ext = os.path.splitext(base_name)

        return file_ext

    def get_resources_directory(self):
        """Returns the path of the resources folder that resides in
        the src\main directory of the program directory."""

        return self.get_directory_path() + "src\\main\\resources\\"

    def check_path_is_directory(self, path):
        """Returns a boolean value describing whether the path provided
        is a directory or not."""

        return os.path.isdir(path)
    
    def check_path_exists(self, path):
        """Returns a boolean value describing whether the path provided
        exists or not."""

        return os.path.exists(path)