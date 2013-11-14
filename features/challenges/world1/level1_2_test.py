import unittest
from features.driver.server_driver import ServerDriver
from hamcrest import assert_that, is_
import requests

SERVER_PORT = 8080
SERVER_CMD = ['gunicorn', 'yose:APP', '-w', '1', '-b', '0.0.0.0:{port}'.format(port=SERVER_PORT)]


class ShareChallenge(unittest.TestCase):

    def test_server_should_respond_on_root_route(self):
        response = requests.get('http://{server_address}:{server_port}/'.format(server_address='localhost', server_port=SERVER_PORT))

        assert_that(response.status_code, is_(200))

    @classmethod
    def setUpClass(cls):
        cls.server = ServerDriver(name='Yose', port=SERVER_PORT)
        cls.server.start(cmd=SERVER_CMD)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
