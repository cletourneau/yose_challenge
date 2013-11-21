import unittest
from hamcrest import assert_that
from nose.tools import istest
from test.flask.matchers.element_in_pyquery_page_matcher import is_in_page
from yose import APP as app
from pyquery import PyQuery as pq


class PrimeFactorFormTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        test_client = app.test_client()
        response = test_client.get('/primeFactors/ui')
        self.page = pq(response.data)

    @istest
    def has_a_title(self):
        assert_that('#title', is_in_page(self.page))

    @istest
    def has_an_invitation(self):
        assert_that('#invitation', is_in_page(self.page))

    @istest
    def has_an_input_number_in_a_form(self):
        assert_that('form input#number', is_in_page(self.page))

    @istest
    def has_a_button_to_submit_the_form(self):
        assert_that('form button#go', is_in_page(self.page))
