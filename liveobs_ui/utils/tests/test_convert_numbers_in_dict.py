""" Test convert_numbers_in_dict """
from unittest import TestCase
from liveobs_ui.utils.converters import convert_numbers_in_dict


class TestConvertNumbersInDict(TestCase):
    """
    Test that convert_numbers_in_dict converts numerical values in dict to
    strings
    """

    def test_converts_int(self):
        """
        Test that given a dict with an int in it we get a string back
        """
        raw_dict = {
            'value': 666
        }
        expected_dict = {
            'value': '666'
        }
        self.assertEqual(convert_numbers_in_dict(raw_dict), expected_dict)

    def test_converts_float(self):
        """
        Test that given a dict with a float in it we get a string back
        """
        raw_dict = {
            'value': 666.6
        }
        expected_dict = {
            'value': '666.6'
        }
        self.assertEqual(convert_numbers_in_dict(raw_dict), expected_dict)
