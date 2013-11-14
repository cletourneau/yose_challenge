def disable_selenium_debug():
    import logging
    selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
    # Only display possible problems
    selenium_logger.setLevel(logging.WARNING)
