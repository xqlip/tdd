import unittest

from FizzBuzzWhizz.fizzbuzzwhizz import FizzBuzzWhizz


class TestFizzBuzzWhizz(unittest.TestCase):

    def test_0_raises_value_error(self):
        with self.assertRaises(ValueError):
            FizzBuzzWhizz(0)

    def test_1_does_not_raise_value_error(self):
        assert FizzBuzzWhizz(1).number == 1

    def test_minus_1_raises_value_error(self):
        with self.assertRaises(ValueError):
            FizzBuzzWhizz(-1)

    def test_101_raises_value_error(self):
        with self.assertRaises(ValueError):
            FizzBuzzWhizz(101)

    def test_1_return_1(self):
        assert FizzBuzzWhizz(1).result == 1

    def test_2_return_2(self):
        assert FizzBuzzWhizz(2).result == 2

    def test_3_return_Fizz(self):
        assert FizzBuzzWhizz(3).result == 'Fizz'

    def test_6_return_Fizz(self):
        assert FizzBuzzWhizz(6).result == 'Fizz'

    def test_5_return_Buzz(self):
        assert FizzBuzzWhizz(5).result == 'Buzz'

    def test_10_return_Buzz(self):
        assert FizzBuzzWhizz(10).result == 'Buzz'

    def test_7_return_Whizz(self):
        assert FizzBuzzWhizz(7).result == 'Whizz'

    def test_14_return_Whizz(self):
        assert FizzBuzzWhizz(14).result == 'Whizz'

    def test_15_return_FizzBuzz(self):
        assert FizzBuzzWhizz(15).result == 'FizzBuzz'

    def test_21_return_FizzWhizz(self):
        assert FizzBuzzWhizz(21).result == 'FizzWhizz'

    def test_70_return_BuzzWhizz(self):
        assert FizzBuzzWhizz(70).result == 'BuzzWhizz'

    def test_13_return_Fizz(self):
        assert FizzBuzzWhizz(13).result == 'Fizz'

    def test_23_return_Fizz(self):
        assert FizzBuzzWhizz(23).result == 'Fizz'
