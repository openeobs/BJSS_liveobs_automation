""" Selectors for therapeutic information on the patient form. """
from selenium.webdriver.common.by import By


THERAPEUTIC_LEVEL = (
    By.XPATH,
    "//tr[td/label/@class = 'therapeutic_level']/td[2]/span/span"
)
THERAPEUTIC_FREQUENCY = (By.CSS_SELECTOR, '.therapeutic_frequency')
THERAPEUTIC_STAFF_TO_PATIENT_RATIO = (By.CSS_SELECTOR, '.therapeutic_staff_to_patient_ratio')
