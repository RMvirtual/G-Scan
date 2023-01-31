import json
from src.main import file_system


class UserSettings:
    def __init__(self):
        self.scan_dir = ""
        self.dest_dir = ""
        self.department = ""
        self.document_type = ""


def get_settings() -> UserSettings:
    with open(file_system.user_settings_path(), "r") as user_settings:
        contents = json.loads(user_settings.read())

    result = UserSettings()
    result.scan_dir = contents["scan_directory"]
    result.dest_dir = contents["dest_directory"]
    result.department = contents["department"]
    result.document_type = contents["document_type"]

    return result
