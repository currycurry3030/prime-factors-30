from unittest import TestCase

from prime_factors import PrimeFactor


class PrimeFactorTest(TestCase):
    def setUp(self):
        super().setUp()
        self.prime_factor = PrimeFactor()

    def test_prime_factor_of_1(self):
        self.assertEqual([], self.prime_factor.of(1))

    def test_prime_factor_of_prime(self):
        self.assertEqual([2], self.prime_factor.of(2))
        self.assertEqual([3], self.prime_factor.of(3))

    def test_prime_factor_of_composite(self):
        self.assertEqual([2, 2], self.prime_factor.of(4))
        self.assertEqual([2, 3], self.prime_factor.of(6))
        self.assertEqual([3, 3], self.prime_factor.of(9))
        self.assertEqual([2, 2, 3], self.prime_factor.of(12))
