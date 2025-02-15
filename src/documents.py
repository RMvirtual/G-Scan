import dataclasses


@dataclasses.dataclass(frozen=True)
class DocumentType:
    short_code: str = ""
    full_name: str = ""
    analysis_code: str = ""
