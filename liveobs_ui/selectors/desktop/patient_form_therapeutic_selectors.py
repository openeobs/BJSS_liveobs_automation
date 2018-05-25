""" Selectors for therapeutic information on the patient form. """
from selenium.webdriver.common.by import By


THERAPEUTIC_LEVEL = (
    By.XPATH,
    "//tr[td/label[contains(@class, 'therapeutic_level')]]/td[2]/span/span"
)
THERAPEUTIC_FREQUENCY = (
    By.XPATH,
    "//tr[td/label[contains(@class, 'therapeutic_frequency')]]/td[2]/span/span"
)
THERAPEUTIC_STAFF_TO_PATIENT_RATIO = (
    By.XPATH,
    "//tr[td/label[contains(@class, 'therapeutic_staff_to_patient_ratio')]]/td[2]/span/span"
)
