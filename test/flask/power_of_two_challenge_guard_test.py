import json
import unittest
from hamcrest import is_, assert_that
from nose.tools import istest
from yose import APP as app


class PowerOfTwoChallengeGuardTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    @istest
    def repeats_bad_number_when_not_a_number(self):
        response = self.app.get('/primeFactors?number=yoyo')
        assert_that(json.loads(response.data)['number'], is_('yoyo'))

    @istest
    def says_its_not_a_number_when_not(self):
        response = self.app.get('/primeFactors?number=yaya')
        assert_that(json.loads(response.data)['error'], is_('not a number'))

    @istest
    def repeats_bad_number_when_too_big(self):
        response = self.app.get('/primeFactors?number=1000001')
        assert_that(json.loads(response.data)['number'], is_('1000001'))

    @istest
    def describes_error_when_too_big(self):
        response = self.app.get('/primeFactors?number=1000001')
        assert_that(json.loads(response.data)['error'], is_('too big number (>1e6)'))
