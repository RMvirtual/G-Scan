import datetime


class Date:
    def __init__(self, month_number: int, month_name: str, year: int) -> None:
        self.month_no = month_number
        self.month_name = month_name
        self.year = year

    def format(self, format: str) -> str:
        """Accepts formats of a combination of yy, yyyy, mm, mmm."""

        return format.lower() \
            .replace("mmm", self.month_name) \
            .replace("yyyy", str(self.year)) \
            .replace("mm", self._two_digit_month_no()) \
            .replace("yy", str(self.year)[-2:])

    def month_name_hyphen_number(self) -> str:
        return self.month_name + " - " + self._two_digit_month_no()

    def _two_digit_month_no(self) -> str:
        return str(self.month_no).zfill(2)


class Calendar:
    def __init__(self) -> None:
        self._numbers_to_names = {
            1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
            6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
            11: "November", 12: "December"
        }

    def months(self, year: int) -> list[Date]:
        return [
            Date(number, name, year)
            for number, name in self._numbers_to_names.items()
        ]

    def month_name_from_number(self, number: int) -> str:
        return self.months_as_strings()[number - 1]

    def months_as_strings(self):
        return [
            month.month_name() for month in self.months(self.current_year())]

    def years(self) -> tuple[int, int]:
        return self.current_year(), self.last_year()

    def years_as_strings(self) -> tuple:
        return [str(year) for year in self.years()]

    def current_month(self):
        return Date(
            self.current_month_number(),
            self.current_month_name(), 
            self.current_year()
        )

    def current_month_name(self) -> str:
        return self.__current_time_as_string("%B")

    def current_month_number(self) -> int:
        return self.__current_time_as_int("%m")

    def current_year(self) -> int:
        return self.__current_time_as_int("%Y")

    def current_year_as_two_digits(self) -> int:
        return self.__current_time_as_int("%y")

    def last_year(self) -> int:
        return self.__current_time_as_int("%Y") - 1

    def last_year_as_two_digits(self) -> int:
        return self.__current_time_as_int("%y") - 1

    def __current_time_as_string(self, format: str) -> str:
        return datetime.now().strftime(format)

    def __current_time_as_int(self, format: str) -> int:
        return int(self.__current_time_as_string(format))

    def month_names_and_numbers(self) -> list[str]:
        return [
            month.month_name_hyphen_number()
            for month in self.months(self.current_year())
        ]

    def months_as_xxx_mm_to_number(self) -> dict:
        months_dictionary = {}
        month_and_name_strings = self.month_names_and_numbers()
        month_number = 1

        for month_and_name in month_and_name_strings:
            months_dictionary[month_and_name] = month_number
            month_number += 1

        return months_dictionary

    def date(self, month: int, year: int) -> Date:
        return self.months(year)[month - 1]

    def date_from_month_name_and_number(
            self, month_name_and_number: str, year) -> Date:
        month_names_and_numbers = self.months_as_xxx_mm_to_number()

        month_number = month_names_and_numbers[month_name_and_number]
        month_name = self.month_name_from_number(month_number)

        return Date(month_number, month_name, year)
