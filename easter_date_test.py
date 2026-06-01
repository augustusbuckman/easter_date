# Do not modify the code in this file
# Test for easter date

import unittest
import easter_date
import tud_test_base as tud


def computus(year):
    lunar_year_cycle_position = year % 19
    weekday_slide_part_1 = year % 4
    weekday_slide_part_2 = year % 7

    leap_year_100 = year // 100
    leap_year_400 = leap_year_100 // 4

    lunar_orbit_correction = (13 + 8 * leap_year_100) // 25

    century_start = (
        15
        - lunar_orbit_correction
        + leap_year_100
        - leap_year_400
    ) % 30

    sunday_offset = (
        4
        + leap_year_100
        - leap_year_400
    ) % 7

    days_added = (
        19 * lunar_year_cycle_position
        + century_start
    ) % 30

    day_of_week_offset = (
        2 * weekday_slide_part_1
        + 4 * weekday_slide_part_2
        + 6 * days_added
        + sunday_offset
    ) % 7

    total_days_added = (
        22
        + days_added
        + day_of_week_offset
    )

    day_of_easter = total_days_added % 31
    month_of_easter = 3 + (total_days_added // 31)

    return month_of_easter, day_of_easter


class TestEasterDate(unittest.TestCase):

    def run_student_program(self, year):
        tud.set_keyboard_input([str(year)])

        easter_date.main()

        return tud.get_display_output()

    def verify_year(self, year):
        month, day = computus(year)

        output = self.run_student_program(year)

        # Must produce exactly:
        # prompt
        # final answer
        self.assertEqual(
            len(output),
            2,
            f"Unexpected output produced for year {year}: {output}"
        )

        self.assertEqual(
            output[0],
            "Enter year: ",
            f"Incorrect prompt for year {year}"
        )

        self.assertEqual(
            output[1],
            f"In {year} Easter Sunday is on {month}/{day}/{year}.",
            f"Incorrect Easter date for year {year}"
        )

    # Example given in assignment
    def test_2001(self):
        self.verify_year(2001)

    # Recent years
    def test_2020(self):
        self.verify_year(2020)

    def test_2021(self):
        self.verify_year(2021)

    def test_2022(self):
        self.verify_year(2022)

    def test_2023(self):
        self.verify_year(2023)

    def test_2024(self):
        self.verify_year(2024)

    def test_2025(self):
        self.verify_year(2025)

    # Earlier years
    def test_1980(self):
        self.verify_year(1980)

    def test_1985(self):
        self.verify_year(1985)

    def test_1990(self):
        self.verify_year(1990)

    def test_1995(self):
        self.verify_year(1995)

    # Century tests
    def test_1901(self):
        self.verify_year(1901)

    def test_1950(self):
        self.verify_year(1950)

    def test_2000(self):
        self.verify_year(2000)

    def test_2099(self):
        self.verify_year(2099)

    # Bulk test to catch hardcoded solutions
    def test_multiple_years(self):
        years = [
            1905,
            1910,
            1925,
            1937,
            1948,
            1959,
            1967,
            1974,
            1988,
            1999,
            2007,
            2011,
            2016,
            2028,
            2035,
            2042,
            2057,
            2075,
            2088
        ]

        for year in years:
            with self.subTest(year=year):
                self.verify_year(year)


if __name__ == "__main__":
    unittest.main()
