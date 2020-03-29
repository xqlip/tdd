class FizzBuzzWhizz:
    def __init__(self, number):
        if FizzBuzzWhizz._is_valid_number(number):
            self.number = number

    @staticmethod
    def _is_valid_number(number):
        if number <= 0 or number > 100:
            raise ValueError('Number must between 0 and 101')
        return True

    @property
    def result(self):
        if self._is_number_include_three():
            return 'Fizz'
        if self._is_number_divisible_by(3, 5, 7):
            return 'FizzBuzzWhizz'
        elif self._is_number_divisible_by(3, 5):
            return 'FizzBuzz'
        elif self._is_number_divisible_by(3, 7):
            return 'FizzWhizz'
        elif self._is_number_divisible_by(5, 7):
            return 'BuzzWhizz'
        elif self._is_number_divisible_by(3):
            return 'Fizz'
        elif self._is_number_divisible_by(5):
            return 'Buzz'
        elif self._is_number_divisible_by(7):
            return 'Whizz'
        return self.number

    def _is_number_divisible_by(self, first_divisor, second_divisor=None, third_divisor=None):
        if first_divisor and not second_divisor and not third_divisor:
            return self.number % first_divisor == 0
        elif first_divisor and second_divisor and third_divisor:
            return self._is_number_divisible_by(first_divisor) and self._is_number_divisible_by(
                second_divisor) and self._is_number_divisible_by(third_divisor)
        elif first_divisor and second_divisor:
            return self._is_number_divisible_by(first_divisor) and self._is_number_divisible_by(second_divisor)

    def _is_number_include_three(self):
        if '3' in str(self.number):
            return True


if __name__ == '__main__':
    for i in range(1, 101):
        print(FizzBuzzWhizz(i).result)


