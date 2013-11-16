from httplib import BAD_REQUEST
import unittest
from hamcrest import is_, assert_that
from nose.tools import istest
from yose import APP as app


class PowerOfTwoChallengeTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.response = self.app.get('/primeFactors?number=hello')

    @istest
    def responds_bad_request(self):
        assert_that(self.response.status_code, is_(BAD_REQUEST))