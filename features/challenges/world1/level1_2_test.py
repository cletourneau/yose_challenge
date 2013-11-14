import unittest
from features.challenges.world1 import disable_selenium_debug
from features.driver.server_driver import ServerDriver
from hamcrest import assert_that, is_, contains_string
import requests
from splinter import Browser

SERVER_PORT = 8080
SERVER_CMD = ['gunicorn', 'yose:APP', '-w', '1', '-b', '0.0.0.0:{port}'.format(port=SERVER_PORT)]


class ShareChallenge(unittest.TestCase):

    def setUp(self):
        self.server_url = 'http://{server_address}:{server_port}/'.format(server_address='localhost', server_port=SERVER_PORT)
        self.response = requests.get(self.server_url)

        disable_selenium_debug()

    def test_server_should_respond_on_share_route(self):
        assert_that(self.response.status_code, is_(200))

    def test_share_route_should_be_of_html_content_type(self):
        assert_that(self.response.headers['content-type'], contains_string('text/html'))

    def test_share_route_should_contain_a_link_with_the_right_id(self):
        with Browser() as browser:
            browser.visit(self.server_url)

            a = browser.find_by_css('a#repository-link').first
            a.click()

            assert_that(browser.is_text_present('YoseTheGame'))

    @classmethod
    def setUpClass(cls):
        cls.server = ServerDriver(name='Yose', port=SERVER_PORT)
        cls.server.start(cmd=SERVER_CMD)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
