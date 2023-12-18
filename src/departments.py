import dataclasses
import json
import file_system
import documents

from documents import DocumentTypes


@dataclasses.dataclass
class Department:
    short_code: str = ""
    full_name: str = ""
    short_name: str = ""
    document_types: DocumentTypes = DocumentTypes()


class Departments:
    def __init__(self):
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
    departments = load_all()

    if full_name:
        return departments.from_full_name(full_name)

    elif short_code:
        return departments.from_short_code(short_code)

    else:
        raise ValueError("Department parameter not selected.")


def load_all() -> Departments:
    result = Departments()

    result.departments = [
        _department(key=short_code, values=values)
        for short_code, values in _load_json().items()
    ]

    return result


def _department(key: str, values: dict[str, any]) -> Department:
    return Department(
        key,
        values["full_name"],
        values["short_name"], 
        _document_types(values)
    )


def _document_types(values: dict[str, any]) -> DocumentTypes:
    result = DocumentTypes()

    result.documents = [
        document for document in documents.load_all()
        if document.short_code in values["document_types"]
    ]

    return result


def _load_json() -> dict[str, any]:
    json_file = file_system.config_directory().joinpath("departments.json") 
    
    with open(json_file) as file_stream:
        return json.load(file_stream)
