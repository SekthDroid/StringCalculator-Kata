from unittest import TestCase
from strcalculator.string_calculator import StringCalculator

__author__ = 'SekthDroid'


class TestStringCalculator(TestCase):
    def setUp(self):
        super().setUp()
        self.calculator = StringCalculator()

    def test_should_return_0_when_empty_string_is_passed(self):
        self.assertEqual(0, self.calculator.add(""))

    def test_should_return_number_if_only_1_number_is_passed(self):
        self.assertEqual(1, self.calculator.add("1"))
        self.assertEqual(2, self.calculator.add("2"))

    def test_should_return_sum_of_2_numbers(self):
        self.assertEqual(3, self.calculator.add("1,2"))
        self.assertEqual(5, self.calculator.add("2,3"))

    def test_should_return_sum_of_unknown_amount_of_numbers(self):
        self.assertEqual(6, self.calculator.add("1,2,3"))
        self.assertEqual(45, self.calculator.add("1,2,3,4,5,6,7,8,9"))

    def test_should_handle_new_lines_between_numbers(self):
        self.assertEqual(6, self.calculator.add("1\n2,3"))
        self.assertEqual(10, self.calculator.add("1\n2,3\n4"))

    def test_should_handle_new_delimiters_separated_by_a_new_line(self):
        self.assertEqual(6, self.calculator.add("//;\n1;2;3"))
        self.assertEqual(7, self.calculator.add("//;\n1;2;4"))