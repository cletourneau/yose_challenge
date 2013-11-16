import unittest
from hamcrest import assert_that, is_
from nose.tools import istest
from yose.prime_factors import prime_factors_of


class PrimeFactorsTest(unittest.TestCase):

    @istest
    def one(self):
        assert_that(prime_factors_of(1), is_([]))

    @istest
    def two(self):
        assert_that(prime_factors_of(2), is_([2]))

    @istest
    def three(self):
        assert_that(prime_factors_of(3), is_([3]))

    @istest
    def four(self):
        assert_that(prime_factors_of(4), is_([2, 2]))

    @istest
    def six(self):
        assert_that(prime_factors_of(6), is_([2, 3]))

    @istest
    def eight(self):
        assert_that(prime_factors_of(8), is_([2, 2, 2]))

    @istest
    def nine(self):
        assert_that(prime_factors_of(9), is_([3, 3]))

    @istest
    def sixteen(self):
        assert_that(prime_factors_of(16), is_([2, 2, 2, 2]))
