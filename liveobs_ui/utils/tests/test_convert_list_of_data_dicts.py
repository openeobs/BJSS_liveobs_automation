""" Test convert_list_of_data_dicts """
from unittest import TestCase
from liveobs_ui.utils.converters import convert_list_of_data_dicts


class TestConvertListOfDataDicts(TestCase):
    """
    Test that convert_list_of_data_dicts returns a list of dictionaries with
    converted values
    """

    def test_list_of_numbers(self):
        """
        Test that returns list of strings when a list of dicts with ints and
        floats is passed
        """
        raw_list = [
            {
                'value': 666
            },
            {
                'value': 666.6
            }
        ]
        expected_list = [
            {
                'value': '666'
            },
            {
                'value': '666.6'
            }
        ]
        self.assertEqual(convert_list_of_data_dicts(raw_list), expected_list)
