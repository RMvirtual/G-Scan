import dataclasses

from documents import DocumentTypes


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
