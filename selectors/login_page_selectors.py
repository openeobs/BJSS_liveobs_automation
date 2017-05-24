"""
Login Form Selectors
Selectors for elements on the mobile login page
"""

from selenium.webdriver.common.by import By

USERNAME_FIELD = (By.ID, 'username')
PASSWORD_FIELD = (By.ID, 'password')
DATABASE_DROPDOWN = (By.ID, 'database')
SUBMIT_BUTTON = (By.ID, 'loginbutton')
LOGIN_ERROR_ALERT = (By.CLASS_NAME, 'alert')
