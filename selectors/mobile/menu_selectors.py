"""
Menu Item Selectors
Selectors for menu items so can navigate to the pages in the menu
"""
from selenium.webdriver.common.by import By

TASK_ITEM = (By.ID, 'taskNavItem')
PATIENT_ITEM = (By.ID, 'patientNavItem')
LOGOUT_BUTTON = (By.CSS_SELECTOR, '.header-main li.logout .button')
