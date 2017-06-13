""" Selectors for form view """
from selenium.webdriver.common.by import By


FORM_ACTIONBAR = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_view_manager .oe_view_manager_body '
    '.oe_formview .oe_form_container .oe_form header'
)
FORM_ACTIONBAR_BUTTON = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_view_manager .oe_view_manager_body '
    '.oe_formview .oe_form_container .oe_form header .oe_form_button'
)
FORM_BODY = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_view_manager .oe_view_manager_body '
    '.oe_formview .oe_form_container .oe_form_sheetbg'
)
FORM_TABS = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_view_manager .oe_view_manager_body '
    '.oe_formview .oe_form_container .oe_form_sheetbg .ui-tabs .ui-tabs-nav '
    '> li > a'
)
