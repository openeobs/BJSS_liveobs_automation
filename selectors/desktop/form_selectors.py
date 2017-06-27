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
FORM_MANY2ONE_INPUT = (
    By.CSS_SELECTOR,
    '.oe_form_field_many2one .ui-autocomplete-input'
)
FORM_MANY2ONE_TEXTAREA = (
    By.CSS_SELECTOR,
    '.oe_form .oe_form_field textarea'
)
FORM_MANY2ONE_DROPDOWN = (
    By.CSS_SELECTOR,
    '.oe_form_field_many2one .oe_m2o_drop_down_button'
)
FORM_VIEW_AUTOCOMPLETE_CONTAINER = (
    By.CSS_SELECTOR,
    '.ui-autocomplete'
)
FORM_VIEW_AUTOCOMPLETE_TEXTDOWN = (
    By.CSS_SELECTOR,
    '.text-dropdown'
)
FORM_VIEW_AUTOCOMPLETE_ITEM = (
    By.CSS_SELECTOR,
    '.ui-menu-item a'
)
FORM_VIEW_BUTTON = (
    By.CSS_SELECTOR,
    '.oe_form_button'
)
