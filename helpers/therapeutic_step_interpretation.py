"""
Functions that help parse the wording therapeutic specific feature files into
primitives or objects that are usable in other operations.
"""
import re


def get_frequency_int_from_string(frequency_string):
    """
    Extracts the frequency from the wording in the step.

    :param frequency_string:
    :return:
    :rtype: int
    """
    if frequency_string == 'Every Hour':
        frequency_int = 60
    else:
        regex = re.compile(r"Every (\d+) Minutes")
        frequency_number = regex.match(frequency_string).group(1)
        frequency_int = int(frequency_number)
    return frequency_int


def get_staff_to_patient_ratio_int_from_string(staff_to_patient_ratio_string):
    """
    Extracts the staff-to-patient ratio from the wording in the step.

    :param staff_to_patient_ratio_string:
    :return:
    :rtype: int
    """
    first_number = staff_to_patient_ratio_string[0]
    staff_to_patient_ratio_int = int(first_number)
    return staff_to_patient_ratio_int
