class LeapYear:
    def __init__(self, year_input: int):
        self._year_input = year_input

    def _is_year_input_century_year(self) -> bool:
        return self._year_input % 100 == 0

    def _is_century_year_equal_leap_year(self) -> bool:
        return self._year_input % 400 == 0

    def _is_normal_year_equal_leap_year(self) -> bool:
        return self._year_input % 4 == 0

    def is_leap_year(self):
        if self._is_year_input_century_year():
            return self._is_century_year_equal_leap_year()
        else:
            return self._is_normal_year_equal_leap_year()


class CliHandler:

    def start(self):
        while True:
            try:
                year_input = int(input('Enter the year:'))
            except ValueError:
                print("Invalid input.\tTry again.")
                continue
            leap_year = LeapYear(year_input)
            print(leap_year.is_leap_year())


if __name__ == "__main__":
    CliHandler().start()
