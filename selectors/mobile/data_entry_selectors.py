""" Selectors for Data Entry Page """
from selenium.webdriver.common.by import By

PATIENT_INFO_POPUP = (By.ID, 'patient_info')
PATIENT_INFO_POPUP_CLOSE_BUTTON = \
    (By.CSS_SELECTOR, '#patient_info .options li:first-child() a')
FULL_SCREEN_PATIENT_INFO_BUTTON = (By.ID, 'patient_obs_fullscreen')
