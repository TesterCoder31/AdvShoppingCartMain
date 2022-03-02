import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


class AdvantageShoppingAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_main_advantage_shopping():
        methods.setup()
        methods.check_text_displayed()
        methods.create_new_user()
        methods.del_user()
        methods.tearDown()


