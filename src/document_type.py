import dataclasses


@dataclasses.dataclass
class DocumentType:
    short_code: str = ""
    full_name: str = ""
    analysis_code: str = ""
