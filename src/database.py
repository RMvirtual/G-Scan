import json
import file_system

from departments import Department, Departments
from documents import DocumentTypes, Document


ExpectedJsonFormat = dict[str, dict[str, str|list[str]]]


def load_department(
        short_code: str = None, full_name: str = None) -> Department:
    if not (short_code or full_name):
        raise ValueError("Department parameter not selected.")

    departments = load_all_departments()

    return (
        departments.from_full_name(full_name) if full_name
        else departments.from_short_code(short_code)
    )


def load_all_departments() -> Departments:
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
