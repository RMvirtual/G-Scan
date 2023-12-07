import json
from  import departments, documents, file_system


class UserSettings:
    def __init__(self):
        self.scan_dir: str = ""
        self.dest_dir:str = ""
        self.department: departments.Department or None = None
        self.document_type: documents.Document or None = None


def load_settings() -> UserSettings:
    with open(file_system.user_settings_path(), mode="r") as user_settings:
        contents = json.loads(user_settings.read())

    result = UserSettings()
    result.scan_dir = contents["scan_directory"]
    result.dest_dir = contents["dest_directory"]
    result.department = departments.load(short_code=contents["department"])
    result.document_type = documents.load(short_code=contents["document_type"])

    return result


def save_settings(settings: UserSettings) -> None:
    values = {
        "scan_directory": settings.scan_dir,
        "dest_directory": settings.dest_dir,
        "department": settings.department.short_code,
        "document_type": settings.document_type.short_code
    }

    with open(file_system.user_settings_path(), mode="w") as user_settings:
        user_settings.write(json.dumps(values, indent=2))
