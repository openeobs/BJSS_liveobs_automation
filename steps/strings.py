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


def get_string_regex(nice_human_name):
    """
    Get a string regex by supplying a nicer name or something, I dunno
    :param nice_human_name:
    :return:
    """
    return re.compile(REGEXES.get(nice_human_name))
