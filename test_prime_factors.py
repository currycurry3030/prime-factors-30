from unittest import TestCase

from prime_factors import PrimeFactor
class PrimeFactorTest(TestCase):
    def test_prime_factor_of_1(self):
        prime_factor = PrimeFactor()
        self.assertEqual([],prime_factor.of(1))

