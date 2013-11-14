import unittest
from features.driver.server_driver import ServerDriver
from hamcrest import assert_that, is_
import requests


SERVER_PORT = 8080
SERVER_CMD = ['gunicorn', 'yose:APP', '-w', '1', '-b', '0.0.0.0:{port}'.format(port=SERVER_PORT)]


class PingChallenge(unittest.TestCase):

    def setUp(self):
        self.response = requests.get('http://{server_address}:{server_port}/ping'.format(server_address='localhost', server_port=SERVER_PORT))

    def test_server_should_responds_200_on_ping_route(self):
        assert_that(self.response.status_code, is_(200))

    def test_server_says_its_alive(self):
        response = self.response.json()
        assert_that(response['alive'], is_(True))

    @classmethod
    def setUpClass(cls):
        cls.server = ServerDriver(name='Yose', port=SERVER_PORT)
        cls.server.start(cmd=SERVER_CMD)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
