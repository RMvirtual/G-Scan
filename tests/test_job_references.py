from date import Date
from job_references import GrReference


def test_should_produce_full_gr_representation() -> None:
    full_ref = GrReference(job_number="GR231201234")
    date_ref = GrReference(Date(12, "December", 2023))
    date_ref.job_number = "1234"

    for reference in [full_ref, date_ref]:
        assert str(reference) == "GR231201234"

