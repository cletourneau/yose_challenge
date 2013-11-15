import inspect
import os


def disable_annoying_selenium_logs():
    import logging

    selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
    selenium_logger.setLevel(logging.WARNING)


def phantomjs_path():
    return get_current_file_dir(inspect.currentframe()) + '/../../../node_modules/phantomjs/bin/phantomjs'


def get_current_file_dir(currentframe):
    return os.path.dirname(get_current_file_path(currentframe))


def get_current_file_path(currentframe):
    return os.path.abspath(inspect.getfile(currentframe))