class FizzBuzz:
    def __init__(self, number, a=3, b=5):
        self.a = a
        self.b = b
        if FizzBuzz.is_valid_number(number):
            self.number = number

    @property
    def result(self):
        return "Fizz"[self.number % self.a * 4:] + "Buzz"[self.number % self.b * 4:] or self.number

    @staticmethod
    def is_valid_number(number):
        if number <= 0 or number > 100:
            raise ValueError('Number must between 0 and 101')
        return True

