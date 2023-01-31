import json
from src.main import departments, documents, file_system


class UserSettings:
    def __init__(self):
        self.scan_dir: str = ""
        self.dest_dir:str = ""
        self.department: departments.Department or None = None
        self.document_type: documents.Document or None = None


def get_settings() -> UserSettings:
    with open(file_system.user_settings_path(), "r") as user_settings:
        contents = json.loads(user_settings.read())

    result = UserSettings()
    result.scan_dir = contents["scan_directory"]
    result.dest_dir = contents["dest_directory"]
    result.department = departments.load(contents["department"])
    result.document_type = documents.load_type(contents["document_type"])

    return result


def save_settings(settings: UserSettings) -> None:
    values = {
        "scan_directory": settings.scan_dir,
        "dest_directory": settings.dest_dir,
        "department": settings.department.short_code,
        "document_type": settings.document_type.short_code
    }

    json_content = json.dumps(values)
    print(json_content)
