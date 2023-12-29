import pytest

from models.date import Date
from models.job_references import JobReference


def test_should_produce_full_gr_representation() -> None:
    full_ref = JobReference(job_number="GR231201234")
    date_ref = JobReference(date=Date(12, "December", 2023))
    date_ref.job_number = "1234"

    for reference in [full_ref, date_ref]:
        assert str(reference) == "GR231201234"


def test_should_set_job_number_of_date_generated_ref() -> None:
    reference = JobReference(date=Date(12, "December", 2023))
    
    reference.job_number = "1234"
    assert reference.job_number == "01234"

    reference.job_number = "11234"
    assert reference.job_number == "11234"


def test_should_error_setting_invalid_job_number() -> None:
    reference = JobReference(date=Date(12, "December", 2023))

    for invalid_entry in ["123lol", "", "123456"]:
        with pytest.raises(ValueError):
            reference.job_number = invalid_entry
