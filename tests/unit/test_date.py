from models.date import Calendar, Date


def test_should_format_date_correctly() -> None:
    date = Date(12, "December", 2023)

    correct_results = {
        "yymm": "2312",
        "mmyy": "1223",
        "yyyymm": "202312",
        "yy mmm": "23 December",
        "mmm yyyy": "December 2023"
    }

    for format, correct_result in correct_results.items():
        assert date.format(format) == correct_result


def test_should_get_months_from_calendar() -> None:
    calendar = Calendar()
    months = calendar.months(2023)

    assert len(months) == 12
    assert months[0].month_no == 1
    assert months[2].year == 2023
    