from date import Calendar, Date


class TestDate:
    def test_should_format_date_correctly(self) -> None:
        date = Date(12, "December", 2023)

        correct_results = {
            "yymm": "2312",
            "mmyy": "1223",
            "yyyymm": "202312",
            "yy mmm": "23 December",
            "mmm yyyy": "December 2023"
        }

        for format, correct_result in correct_results.items():
            assert date.format_as(format) == correct_result

    def test_should_format_as_month_name_hyphen_number(self) -> None:
        double_digit_date = Date(
            12, "December", 2023).month_name_hyphen_number()
        
        assert double_digit_date == "December - 12" 

        single_digit_date = Date(
            1, "January", 2023).month_name_hyphen_number()

        assert single_digit_date == "January - 01"


class TestCalendar:
    def test_should_get_months_from_calendar(self) -> None:
        calendar = Calendar()
        months = calendar.months(2023)

        assert len(months) == 12
        assert months[0].month_no == 1
        assert months[2].year == 2023
        
    def test_should_index_date(self) -> None:
        calendar = Calendar()
        date = calendar.date(month=6, year=1991)

        assert date.month_name == "June"
        assert date.year == 1991

    def test_should_index_month_name_and_number(self) -> None:
        calendar = Calendar()
        date = calendar.date_from_month_name_and_number("January - 01", 1992)

        assert date.month_name == "January"
        assert date.year == 1992

    def test_should_get_months_as_xxx_mm_to_number(self) -> None:
        calendar = Calendar()
        months = calendar.months_as_xxx_mm_to_number()

        assert len(months) == 12
        assert months["January - 01"] == 1
        assert months["December - 12"] == 12