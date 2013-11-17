import json
import unittest
from hamcrest import is_, assert_that, has_length
from nose.tools import istest
from yose import APP as app


class PowerOfTwoChallengeMultipleEntriesTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.response = self.app.get('/primeFactors?number=300&number=120&number=hello')

    @istest
    def insecurely_returns_an_array(self):
        assert_that(isinstance(json.loads(self.response.data), list))

    @istest
    def size_of_array_is_same_as_the_count_of_numbers_asked(self):
        assert_that(json.loads(self.response.data), has_length(3))

    @istest
    def numbers_in_request_are_responded(self):
        response = json.loads(self.response.data)

        primes_of_300 = response[0]
        primes_of_120 = response[1]

        assert_that(primes_of_300['number'], is_(300))
        assert_that(primes_of_120['number'], is_(120))

        assert_that(primes_of_300['decomposition'], is_([2, 2, 3, 5, 5]))
        assert_that(primes_of_120['decomposition'], is_([2, 2, 2, 3, 5]))

    @istest
    def errors_in_request_are_responded(self):
        response = json.loads(self.response.data)

        not_a_number_error = response[2]

        assert_that(not_a_number_error['number'], is_('hello'))
        assert_that(not_a_number_error['error'], is_('not a number'))
