import re
from src.main.date.date import Date

def gr_reference(full_job_no:str) -> str:
    return "GR" + __strip_alphabet(full_job_no)
    
def quick_gr_reference(brief_job_no:str, date:Date) -> str:
    full_job_no = job_number_from_brief(brief_job_no, date)

    return gr_reference(full_job_no)

def job_number_from_brief(brief_job_no:str, date:Date) -> str:
    clean_brief_job_no = __strip_alphabet(brief_job_no)

    template_job_no = template_job_number(
        date=date, digits_to_exclude=len(clean_brief_job_no))
   
    return template_job_no + clean_brief_job_no

def template_job_number(date:Date, digits_to_exclude:int=0) -> str:
    year = date.year_as_two_digits()
    month = date.month_number_as_two_digits()
    zeroes_padding = (5 - digits_to_exclude) * "0"

    return year + month + zeroes_padding

def is_full_input_length(inputted_reference: str) -> bool:
    return len(inputted_reference) == 9

def is_quick_input_length(inputted_reference:str) -> bool:
    return 4 <= len(inputted_reference) <= 9

def __strip_alphabet(string_to_modify:str) -> str:
    return re.sub("[^0-9]", "", string_to_modify)