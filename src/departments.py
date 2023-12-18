import dataclasses
import json
import file_system
import documents

from documents import DocumentTypes

ExpectedJsonFormat = dict[str, dict[str, str|list[str]]]


@dataclasses.dataclass
class Department:
    short_code: str = ""
    full_name: str = ""
    short_name: str = ""
    document_types: DocumentTypes = DocumentTypes()


class Departments:
    def __init__(self, departments: list[Department] = None):
        if not departments:
            self.departments: list[Department] = []

    def __contains__(self, short_code: str) -> bool:
        return len(short_code == other for other in self.short_names())

    def __iter__(self):
        return self.departments.__iter__()

    def short_names(self) -> list[str]:
        return [document.short_code for document in self.departments]

    def full_names(self) -> list[str]:
        return [document.full_name for document in self.departments]

    def from_short_code(self, short_code) -> Department:
        for department in self.departments:
            if department.short_code == short_code:
                return department

        self._raise_department_invalid(short_code)

    def from_full_name(self, full_name) -> Department:
        for department in self.departments:
            if department.full_name == full_name:
                return department

        self._raise_department_invalid(full_name)

    def _raise_department_invalid(self, department_name: str) -> None:
        raise ValueError(f"Department {department_name} does not exist.")


def load(short_code: str = None, full_name: str = None) -> Department:
    if not (short_code or full_name):
        raise ValueError("Department parameter not selected.")

    departments = load_all()

    return (
        departments.from_full_name(full_name) if full_name
        else departments.from_short_code(short_code)
    )


def load_all() -> Departments:
    json_file = file_system.config_directory().joinpath("departments.json") 
    
    with open(json_file) as file_stream:
        json_contents: ExpectedJsonFormat = json.load(file_stream)
    
    result = Departments()

    result.departments = [
        Department(
            short_code,
            values["full_name"],
            values["short_name"], 
            _document_types(values)
        ) for short_code, values in json_contents.items()
    ]

    return result


def _document_types(values: dict[str, any]) -> DocumentTypes:
    result = DocumentTypes()

    result.documents = [
        document for document in documents.load_all()
        if document.short_code in values["document_types"]
    ]

    return result
