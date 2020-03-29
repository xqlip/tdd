class FizzBuzzWhizz:
    def __init__(self, number, a=3, b=5, c=7):
        self.a = a
        self.b = b
        self.c = c
        if FizzBuzzWhizz._is_valid_number(number):
            self.number = number

    @staticmethod
    def _is_valid_number(number):
        if number <= 0 or number > 100:
            raise ValueError('Number must between 0 and 101')
        return True

    @property
    def result(self):
        return "Fizz"[0 if '3' in str(self.number) else 4:] or \
               "Fizz"[self.number % self.a * 4:] + "Buzz"[self.number % self.b * 4:] + "Whizz"[i % self.c * 5:] or \
               self.number


if __name__ == '__main__':
    for i in range(1, 101):
        print(FizzBuzzWhizz(i).result)
