""" Selectors for error elements. """
from selenium.webdriver.common.by import By


MODAL_CONTAINER_ERROR_MESSAGE = (By.CSS_SELECTOR, '.oe_dialog_warning p')
NOTIFICATION_ERROR_MESSAGE_FIRST_LINE = \
    (By.CSS_SELECTOR, '.ui-notify-message:last-child h1')
NOTIFICATION_ERROR_MESSAGE_LIST_ITEMS = \
    (By.CSS_SELECTOR, '.ui-notify-message:last-child li')
