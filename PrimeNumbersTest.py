import unittest
from PrimeNumbers import PrimeNumbers


class MyTestCase(unittest.TestCase):
    def test_list_generation(self):
        specimen = PrimeNumbers()

        count = 100

        specimen.generate_list(count)

        self.assertEqual(len(specimen.NumbersList), count)

    def test_is_number_is_prime_with_not_prime(self):
        specimen = PrimeNumbers()

        number = 8
        is_prime = specimen.is_number_prime(number)

        self.assertEqual(is_prime, False)

    def test_is_number_is_prime_with_prime(self):
        specimen = PrimeNumbers()

        number = 2
        is_prime = specimen.is_number_prime(number)

        self.assertEqual(is_prime, True)


if __name__ == '__main__':
    unittest.main()
