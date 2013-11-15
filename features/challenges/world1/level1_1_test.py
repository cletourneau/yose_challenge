from httplib import OK
import unittest
from hamcrest import assert_that, is_
from nose.tools import istest
import requests
from testconfig import config


class PingChallenge(unittest.TestCase):

    def setUp(self):
        self.response = requests.get('{0}/ping'.format(config['server_url']))

    @istest
    def server_responds_status_OK(self):
        assert_that(self.response.status_code, is_(OK))

    @istest
    def server_responds_json_content_type(self):
        assert_that(self.response.headers['content-type'], is_('application/json'))

    @istest
    def server_says_its_alive(self):
        response = self.response.json()
        assert_that(response['alive'], is_(True))
