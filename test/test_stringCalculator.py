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