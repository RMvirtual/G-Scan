from date.date import Date
from job_references.references import GrReference


def test_should_produce_full_gr_representation() -> None:
    date = Date(12, "December", 2023)
    result = GrReference(date, job_number="01234")

    assert result.job_number == "GR231201234"

