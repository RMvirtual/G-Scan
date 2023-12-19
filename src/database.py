import json
import file_system

from departments import Department 
from documents import DocumentTypes, Document
from user import UserSettings

ExpectedJsonFormat = dict[str, dict[str, str|list[str]]]


def load_department(short_code: str = "", full_name: str = "") -> Department:
    if not (short_code or full_name):
        raise ValueError("Department parameter not selected.")

    departments = load_all_departments()

    if full_name:
        filtered = [
            dept for dept in departments if dept.full_name == full_name]
    
        if not filtered:
            raise ValueError(f"Invalid department: {full_name}")

        return filtered[0]

    else:
        filtered = [
            dept for dept in departments if dept.short_code == short_code]

        if not filtered:
            raise ValueError(f"Invalid department: {short_code}")

        return filtered[0]


def load_all_departments() -> list[Department]:
    json_file = file_system.config_directory().joinpath("departments.json") 
    
    with open(json_file) as file_stream:
        json_contents: ExpectedJsonFormat = json.load(file_stream)
    
    return [
        Department(
            short_code,
            values["full_name"],
            values["short_name"], 
            _document_types(values)
        ) for short_code, values in json_contents.items()
    ]


def _document_types(values: dict[str, any]) -> DocumentTypes:
    result = DocumentTypes()

    result.documents = [
        document for document in load_all_documents()
        if document.short_code in values["document_types"]
    ]

    return result


def load_document(short_code: str = None, full_name: str = None) -> Document:
    documents = load_all_documents()

    if full_name:
        return documents.from_full_name(full_name)

    elif short_code:
        return documents.from_short_code(short_code)

    else:
        raise ValueError("No Document Type selected.")


def load_all_documents() -> DocumentTypes:
    json_file = file_system.config_directory().joinpath("document_types.json") 
    
    with open(json_file) as file_stream:
        json_contents = json.load(file_stream)
    
    result = DocumentTypes()
    
    result.documents = [
        Document(short_code, values["full_name"], values["analysis_code"])
        for short_code, values in json_contents.items()
    ]

    return result


def load_user_settings() -> UserSettings:
    user_settings = file_system.user_settings_path()

    if not user_settings.exists():
        json_file = file_system.config_directory().joinpath("user_defaults.json")

    else:
        json_file = user_settings
    
    with open(json_file, mode="r") as user_settings:
        contents = json.loads(user_settings.read())

    return UserSettings(
        contents["scan_directory"],
        contents["dest_directory"],
        load_department(short_code=contents["department"]),
        load_document(short_code=contents["document_type"])
    )


def save_user_settings(settings: UserSettings) -> None:
    values = {
        "scan_directory": settings.scan_dir,
        "dest_directory": settings.dest_dir,
        "department": settings.department.short_code,
        "document_type": settings.document_type.short_code
    }

    with open(file_system.user_settings_path(), mode="w") as user_settings:
        user_settings.write(json.dumps(values, indent=2))
