import json
import unittest
from hamcrest import assert_that, has_length, equal_to
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
    def all_numbers_in_request_are_responded(self):
        response = json.loads(self.response.data)

        assert_that(response[0], equal_to({
            'number': 300,
            'decomposition': [2, 2, 3, 5, 5],
        }))

        assert_that(response[1], equal_to({
            'number': 120,
            'decomposition': [2, 2, 2, 3, 5]
        }))


    @istest
    def errors_in_request_are_responded(self):
        response = json.loads(self.response.data)

        assert_that(response[2], equal_to({
            'number': 'hello',
            'error': 'not a number'
        }))
