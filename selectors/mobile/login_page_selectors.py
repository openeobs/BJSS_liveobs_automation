"""
Login Form Selectors
Selectors for elements on the login pages
"""

from selenium.webdriver.common.by import By

USERNAME_FIELD = (By.ID, 'username')
LOGIN_FIELD = (By.ID, 'login')
PASSWORD_FIELD = (By.ID, 'password')
DATABASE_DROPDOWN = (By.ID, 'database')
SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type=submit]')
LOGIN_ERROR_ALERT = (By.CLASS_NAME, 'alert')
