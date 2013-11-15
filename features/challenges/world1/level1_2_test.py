from httplib import OK
import unittest
from features.challenges.world1 import disable_annoying_selenium_logs, phantomjs_path
from hamcrest import assert_that, is_, contains_string
from nose.tools import istest
import requests
from splinter import Browser
from testconfig import config


class ShareChallenge(unittest.TestCase):

    def setUp(self):
        self.server_url = config['server_url']
        self.response = requests.get(self.server_url)

        disable_annoying_selenium_logs()

    @istest
    def responds_status_OK(self):
        assert_that(self.response.status_code, is_(OK))

    @istest
    def responds_html_content_type(self):
        assert_that(self.response.headers['content-type'], contains_string('text/html'))

    @istest
    def provides_name_of_the_game_in_source_code(self):
        with Browser(driver_name='phantomjs', executable_path=phantomjs_path()) as browser:
            browser.visit(self.server_url)

            a = browser.find_by_css('a#repository-link').first
            a.click()

            assert_that(browser.is_text_present('YoseTheGame'))
