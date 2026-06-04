# Do not modify the code in this file
# Test for easter date

import unittest
import ast
import easter_date
import tud_test_base as tud


def expected_easter(year):

    lunar_cycle = year % 19
    remainder_four = year % 4
    remainder_seven = year % 7

    century = year // 100
    leap_century = century // 4

    lunar_correction = (
        13 + 8 * century
    ) // 25

    century_start = (
        15
        - lunar_correction
        + century
        - leap_century
    ) % 30

    sunday_offset = (
        4
        + century
        - leap_century
    ) % 7

    days_added = (
        19 * lunar_cycle
        + century_start
    ) % 30

    weekday_offset = (
        2 * remainder_four
        + 4 * remainder_seven
        + 6 * days_added
        + sunday_offset
    ) % 7

    total_days = (
        22
        + days_added
        + weekday_offset
    )

    day = total_days % 31
    month = 3 + (total_days // 31)

    return month, day


class TestEasterDate(unittest.TestCase):

    #################################################
    # Helper Functions
    #################################################

    def run_program(self, year):

        tud.set_keyboard_input([str(year)])

        easter_date.main()

        return tud.get_display_output()

    def verify_year(self, year):

        month, day = expected_easter(year)

        output = self.run_program(year)

        self.assertEqual(
            output,
            [
                "Enter year: ",
                f"In {year} Easter Sunday is on {month}/{day}/{year}."
            ]
        )

    #################################################
    # 5 Marks - Correctness
    #################################################

    def test_assignment_example(self):
        self.verify_year(2001)

    def test_year_1988(self):
        self.verify_year(1988)

    def test_year_2000(self):
        self.verify_year(2000)

    def test_year_2024(self):
        self.verify_year(2024)

    def test_year_2099(self):
        self.verify_year(2099)

    #################################################
    # 2 Marks - Output Formatting
    #################################################

    def test_prompt(self):

        output = self.run_program(2001)

        self.assertEqual(
            output[0],
            "Enter year: "
        )

    def test_no_extra_output(self):

        output = self.run_program(2001)

        self.assertEqual(
            len(output),
            2,
            "Only the prompt and final answer should be displayed."
        )

    #################################################
    # 1 Mark - Hidden Tests
    #################################################

    def test_hidden_years(self):

        hidden_years = [
            1918,
            1947,
            1968,
            1986,
            2017,
            2032,
            2058
        ]

        for year in hidden_years:

            with self.subTest(year=year):

                self.verify_year(year)

    #################################################
    # 1 Mark - Header and Comments
    #################################################

    def test_header_and_comments(self):

        with open("easter_date.py") as f:
            code = f.read()
            lines = f.readlines()

        required_header_items = [
            "# File:",
            "# Description:",
            "# Assignment Number:",
            "# Name:",
            "# SID:",
            "# Email:",
            "# Grader:"
        ]

        for item in required_header_items:

            self.assertIn(
                item,
                code,
                f"Missing header item: {item}"
            )

        meaningful_comments = 0

        for line in lines[15:]:

            stripped = line.strip()

            if (
                stripped.startswith("#")
                and len(stripped) > 15
            ):
                meaningful_comments += 1

        self.assertGreaterEqual(
            meaningful_comments,
            2,
            "Expected at least two meaningful comments."
        )

    #################################################
    # 1 Mark - Readability
    #################################################

    def test_readability(self):

        with open("easter_date.py") as f:
            tree = ast.parse(f.read())

        assignments = 0
        bad_names = []

        allowed_short_names = {
            "year",
            "day",
            "month"
        }

        for node in ast.walk(tree):

            if isinstance(node, ast.Assign):

                assignments += 1

                for target in node.targets:

                    if isinstance(target, ast.Name):

                        name = target.id

                        if (
                            len(name) <= 2
                            and name not in allowed_short_names
                        ):
                            bad_names.append(name)

        self.assertGreaterEqual(
            assignments,
            8,
            "Program should be broken into logical steps."
        )

        self.assertLessEqual(
            len(bad_names),
            2,
            f"Use more descriptive variable names instead of {bad_names}"
        )

    #################################################
    # Sanity Check
    #################################################

    def test_main_exists(self):

        self.assertTrue(
            hasattr(easter_date, "main")
        )


if __name__ == "__main__":
    unittest.main()
