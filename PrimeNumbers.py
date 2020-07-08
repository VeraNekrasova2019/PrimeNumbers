class PrimeNumbers:
    def __init__(self):
        self.NumbersList = list()

    def generate_list(self, count: int) -> bool:
        for x in range(0, count):
            self.NumbersList.append(x)
        return True

    def is_number_prime(self, number: int) -> bool:
        self.generate_list(number)

        for i in range(2, number):
            mod = number % i
            if mod == 0:
                return False
        return True
