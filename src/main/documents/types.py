from src.main import file_system


class Document:
    def __init__(self) -> None:
        self.short_code = ""
        self.full_name = ""
        self.analysis_code = ""


class DocumentTypes:
    def __init__(self):
        self.documents = []

    def __contains__(self, short_code: str) -> bool:
        return len(
            document.short_code == short_code for document in self.documents)

    def __iter__(self):
        return self.documents.__iter__()

    def short_codes(self) -> list[str]:
        return [document.short_code for document in self.documents]

    def full_names(self) -> list[str]:
        return [document.full_name for document in self.documents]


def load_type(short_code: str) -> Document:
    return _document(key=short_code, values=_json_contents()[short_code])


def load_all_types() -> DocumentTypes:
    result = DocumentTypes()
    key_values = _json_contents().items()

    result.documents = [
        _document(short_code, values) for short_code, values in key_values]

    return result


def _document(key: str, values: dict[str, any]) -> Document:
    result = Document()
    result.short_code = key
    result.full_name = values["full_name"]
    result.analysis_code = values["analysis_code"]

    return result


def _json_contents() -> dict[str, any]:
    return file_system.load_json(file_system.document_types_path())