from httplib import OK
import unittest
from hamcrest import assert_that, is_
from nose.plugins.attrib import attr
from nose.tools import istest
import requests
from testconfig import config


@attr(needs_server=True)
class PowerOfTwoChallenge(unittest.TestCase):

    def setUp(self):
        self.response = requests.get('{0}/primeFactors?number=16'.format(config['server_url']))

    @istest
    def responds_json_content_type(self):
        assert_that(self.response.headers['content-type'], is_('application/json'))

    @istest
    def responds_status_OK(self):
        assert_that(self.response.status_code, is_(OK))

    @istest
    def responds_number_in_request(self):
        response = self.response.json()
        assert_that(response['number'], is_(16))

    @istest
    def responds_decomposition_in_request(self):
        response = self.response.json()
        assert_that(response['decomposition'], is_([2, 2, 2, 2]))
