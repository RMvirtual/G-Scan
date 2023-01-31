from src.main import file_system


class Document:
    def __init__(self) -> None:
        self.short_code = ""
        self.full_name = ""
        self.analysis_code = ""


def load(short_code: str) -> Document:
    documents = _load_json()

    return _document_type(key=short_code, values=documents[short_code])


def _document_type(key: str, values: dict[str, any]) -> Document:
    result = Document()
    result.short_code = key
    result.full_name = values["full_name"]
    result.analysis_code = values["analysis_code"]

    return result


def load_all() -> list[Document]:
    documents = _load_json()
    result = []

    for short_code, values in documents.items():
        result.append(_document_type(key=short_code, values=values))

    return result


def _load_json() -> dict[str, any]:
    return file_system.load_json(file_system.document_types_path())