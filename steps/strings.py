""" Regex foo """

# pylint: disable=anomalous-backslash-in-string

import re


PARTIAL_NEWS_CLINICAL_RISK = \
    "At least (\w+) clinical risk, real risk may be higher"
PARTIAL_NEWS_SCORE = "At least (\d+) NEWS score, real NEWS score may be higher"
OBS_TITLE = "Successfully Submitted (\w+.)?(\w+) Observation"
REGEXES = {
    'Clinical Risk': PARTIAL_NEWS_CLINICAL_RISK,
    'Score': PARTIAL_NEWS_SCORE,
    'OBS': OBS_TITLE
}


def get_string_regex(element_reference):
    """
    Get a string regex by supplying an element reference as a parameter

    :param element_reference: reference to the specific regex
    :return: regex object
    """
    return re.compile(REGEXES.get(element_reference))
