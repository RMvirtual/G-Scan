import src.main.file_system.file_system as file_system
from src.main.file_names.naming_attributes import FileNamingAttributes


def file_names(
        attributes: FileNamingAttributes, backup_directory: str) -> tuple:
    """Creates the file names required for processing."""

    job_ref = attributes.job_reference
    backup = backup_file_name(attributes, backup_directory)
    destination = destination_file_name(attributes)

    return job_ref, backup, destination


def backup_file_name(
        attributes: FileNamingAttributes, backup_directory: str) -> str:
    """Creates the backup file name including the job reference,
    paperwork counter (if applicable), paperwork type and file
    extension.
    
    Checks if there is a duplicate-named file already in the backup
    directory and loops through appending increasing page numbers
    to the file name till it is no longer duplicate.
    """
    file_name = (attributes.job_reference + "_" + attributes.paperwork_type)

    duplicate_files = file_system.matching_file_names(
        file_name, backup_directory)

    if duplicate_files > 1:
        file_name += duplicate_files

    return file_name + attributes.file_extension


def destination_file_name(attributes: FileNamingAttributes) -> str:
    flags = paperwork_type_flags(attributes.paperwork_type)

    return "++" + attributes.job_reference + flags + attributes.file_extension


def paperwork_type_flags(paperwork_type: str) -> str:
    return _all_flags()[paperwork_type]


def _all_flags() -> dict:
    return {
        "Cust PW": "++xShPaxIsVs0++OPSPWAT++Customer_Paperwork",
        "Loading List": "++xShxPaxIsVs0++OPSLDLST++Loading_List",
        "POD": "++xShxPaIsVs2++KPIPOD++Scanned_POD"
    }
