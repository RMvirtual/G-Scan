import json
from src.main import file_system
from src.main import departments
from src.main import documents

class UserSettings:
    def __init__(self):
        self.scan_dir = ""
        self.dest_dir = ""
        self.department = None
        self.document_type = None


def get_settings() -> UserSettings:
    with open(file_system.user_settings_path(), "r") as user_settings:
        contents = json.loads(user_settings.read())

    result = UserSettings()
    result.scan_dir = contents["scan_directory"]
    result.dest_dir = contents["dest_directory"]
    result.department = departments.load(contents["department"])
    result.document_type = documents.load_type(contents["document_type"])

    return result
