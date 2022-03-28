class Date(object):    
    def __init__(self, month_number:int, month_name:str, year:int):
        self.__month_number = month_number
        self.__month_name = month_name
        self.__year = year

    def month_number(self) -> int:
        return self.__month_number

    def month_number_as_two_digits(self) -> str:
        return str(self.__month_number).zfill(2)

    def month_name(self) -> str:
        return self.__month_name

    def year(self) -> int:
        return self.__year

    def year_as_two_digits(self) -> str:
        return str(self.__year)[-2:]

    def month_name_hyphen_number(self) -> str:
        month_name = self.month_name()
        month_number = self.month_number_as_two_digits()
        month_string = month_name + " - " + month_number

        return month_string