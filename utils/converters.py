""" Converters for use with Selenium """


def convert_numbers_in_dict(values_dict):
    """
    Convert any values in dictionary that are values to string

    :param values_dict: dictionary of values used to submit
    :return: dictionary with all numerical values converted to a string
    """
    new_dict = values_dict.copy()
    for key, value in new_dict.iteritems():
        if isinstance(value, (int, float)):
            new_dict[key] = str(value)
    return new_dict


def convert_list_of_data_dicts(values_list):
    """
    Convert a list of dicts that contain data to fill out a form

    :param values_list: List of dictionaries that contain form data
    :return: list of dictionaries with converted values
    """
    new_list = values_list.copy()
    for item in new_list:
        item = convert_numbers_in_dict(item)
    return new_list
