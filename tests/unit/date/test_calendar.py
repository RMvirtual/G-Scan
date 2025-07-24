from date import Calendar


class TestCalendar:
    def test_should_index_date(self) -> None:
        calendar = Calendar()
        date = calendar.date(6, 1991)

        assert date.month_name == "June"
        assert date.year == 1991

    def test_should_get_months_from_calendar(self) -> None:
        calendar = Calendar()
        months = calendar.months(2023)

        assert len(months) == 12
        assert months[0].month_no == 1
        assert months[2].year == 2023

    def test_should_index_month_name_and_number(self) -> None:
        calendar = Calendar()
        date = calendar.date_from_month_name_and_number("January - 01", 1992)

        assert date.month_name == "January"
        assert date.year == 1992

    def test_should_index_month_name_by_name(self) -> None:
        calendar = Calendar()
        assert calendar.month_name_from_number(2) == "February"

    def test_should_get_months_as_xxx_mm_to_number(self) -> None:
        calendar = Calendar()
        months = calendar.months_as_xxx_mm_to_number()

        assert len(months) == 12
        assert months["January - 01"] == 1
        assert months["December - 12"] == 12
