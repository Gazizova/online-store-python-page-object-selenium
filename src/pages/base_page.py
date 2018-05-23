from abc import abstractmethod

class BasePage(object):
    """All page obgects inherit from this"""
    def __init__(self, driver):
        self.driver = driver
        self._validate_page(driver)

    @abstractmethod
    def _validate_page(self, driver):
        return

class InvalidPageException(Exception):
    """If page is not found"""
    pass