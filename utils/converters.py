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
