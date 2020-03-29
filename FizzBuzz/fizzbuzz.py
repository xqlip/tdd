class FizzBuzz:
    def __init__(self, number):
        if FizzBuzz.is_valid_number(number):
            self.number = number
    # @property
    # def result(self):
    #     if self.number == 3 or self.number == 6:
    #         return 'Fizz'
    #     elif self.number == 5 or self.number == 10:
    #         return 'Buzz'
    #     elif self.number == 15 or self.number == 30:
    #         return 'FizzBuzz'
    #     return self.number
    # @property
    # def result(self):
    #     if self.number % 3 == 0 and self.number % 5 == 0:
    #         return 'FizzBuzz'
    #     elif self.number % 3 == 0:
    #         return 'Fizz'
    #     elif self.number % 5 == 0:
    #         return 'Buzz'
    #     return self.number
    
    @property
    def result(self):
        if self._is_number_divisible_by(3, 5):
            return 'FizzBuzz'
        elif self._is_number_divisible_by(3):
            return 'Fizz'
        elif self._is_number_divisible_by(5):
            return 'Buzz'
        return self.number

    def _is_number_divisible_by(self, first_divisor, second_divisor=None):
        if first_divisor and not second_divisor:
            return self.number % first_divisor == 0
        else:
            return self._is_number_divisible_by(first_divisor) and \
                   self._is_number_divisible_by(second_divisor)

    @staticmethod
    def is_valid_number(number):
        if number <= 0 or number > 100:
            raise ValueError('Number must betwen 0 and 101')
        return True

    # def _is_number_divisible_by(self, divisor):
    #     return self.number % divisor == 0


