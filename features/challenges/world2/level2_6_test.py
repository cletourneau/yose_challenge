import unittest
from features.challenges.world1 import disable_annoying_selenium_logs, phantomjs_path
from hamcrest import assert_that, is_
from nose.plugins.attrib import attr
from nose.tools import istest
from splinter import Browser
from testconfig import config


@attr(needs_server=True)
class PrimeFactorsFormTest(unittest.TestCase):
    def setUp(self):
        self.server_url = config['server_url']

        disable_annoying_selenium_logs()

    @istest
    def has_a_form_to_input_number(self):
        with Browser(driver_name='phantomjs', executable_path=phantomjs_path()) as browser:
            browser.visit(self.server_url + '/primeFactors/ui')

            assert_that(browser.is_element_present_by_id('title'))
            assert_that(browser.is_element_present_by_id('invitation'))
            assert_that(browser.is_element_present_by_css('form input#number'))
            assert_that(browser.is_element_present_by_css('form button#go'))

    @istest
    def displays_the_decomposition_of_the_input_number(self):
        with Browser(driver_name='phantomjs', executable_path=phantomjs_path()) as browser:
            browser.visit(self.server_url + '/primeFactors/ui')

            browser.find_by_css('form input#number').first.fill('3240')
            browser.find_by_css('form button#go').first.click()

            assert_that(browser.find_by_id('result').first.value, is_('3240 = 2 x 2 x 2 x 3 x 3 x 3 x 3 x 5'))
