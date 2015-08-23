from unittest import TestCase
from strcalculator.string_calculator import StringCalculator

__author__ = 'SekthDroid'


class TestStringCalculator(TestCase):

    def test_should_return_0_when_empty_string_is_passed(self):
        string_calculator = StringCalculator()
        self.assertEqual(0, string_calculator.add(""))