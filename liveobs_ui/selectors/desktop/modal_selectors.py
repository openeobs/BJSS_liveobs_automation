""" Selectors for modal view """
from selenium.webdriver.common.by import By


MODAL_CONTAINER = (By.CSS_SELECTOR, '.modal .modal-dialog')
MODAL_HEADER = (By.CSS_SELECTOR, '.modal .modal-dialog .modal-header')
MODAL_BODY = (By.CSS_SELECTOR, '.modal .modal-dialog .modal-body')
MODAL_FOOTER = (By.CSS_SELECTOR, '.modal .modal-dialog .modal-footer')

MODAL_TITLE = (By.CSS_SELECTOR, '.modal-header .modal-title')
MODAL_HEADER_CLOSE = (By.CSS_SELECTOR, '.modal-header .close')

MODAL_BODY_VIEW_MANAGER = (
    By.CSS_SELECTOR,
    '.modal-body .oe_view_manager'
)

MODAL_FOOTER_BUTTONS = (
    By.CSS_SELECTOR,
    '.modal-footer .oe_form_buttons .oe_form_button'
)
