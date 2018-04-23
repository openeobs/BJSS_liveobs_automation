""" Selectors for form view """
from selenium.webdriver.common.by import By


THERAPEUTIC_LEVEL_FIELD = (
    By.CSS_SELECTOR,
    '.therapeutic_level > select'
)

THERAPEUTIC_LEVEL_FIELD_OPTIONS = (
    By.CSS_SELECTOR,
    '.therapeutic_level > select > option'
)

THERAPEUTIC_FREQUENCY_FIELD = (
    By.CSS_SELECTOR,
    'span.therapeutic_frequency'
)

THERAPEUTIC_FREQUENCY_FIELD_VALUE = (
    By.CSS_SELECTOR,
    '.therapeutic_frequency > select'
)

THERAPEUTIC_FREQUENCY_FIELD_OPTIONS = (
    By.CSS_SELECTOR,
    '.therapeutic_frequency > select > option'
)

THERAPEUTIC_STAFF_TO_PATIENT_RATIO_FIELD = (
    By.CSS_SELECTOR,
    'span.therapeutic_staff_to_patient_ratio'
)

THERAPEUTIC_STAFF_TO_PATIENT_RATIO_FIELD_OPTIONS = (
    By.CSS_SELECTOR,
    '.therapeutic_staff_to_patient_ratio > select > option'
)