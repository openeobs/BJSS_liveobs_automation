""" Selectors for Nursing Shift Change Wizard """
from selenium.webdriver.common.by import By


WIZARD_STAGE_CONTAINER = (
    By.CSS_SELECTOR,
    '.modal .oe_form_field_status'
)
WIZARD_STAGE = (
    By.CSS_SELECTOR,
    '.modal .oe_form_field_status .label'
)
WIZARD_BUTTON = (
    By.CSS_SELECTOR,
    '.modal .oe_form header .oe_form_button'
)
WIZARD_START_BUTTON = (
    By.XPATH,
    '//header/button/span[contains(text(), \'Start\')]'
)
WIZARD_DEALLOCATE_BUTTON = (
    By.XPATH,
    '//header/button/span[contains(text(), \'Deallocate\')]'
)
WIZARD_ROLL_CALL_BUTTON = (
    By.XPATH,
    '//header/button/span[contains(text(), \'Select\')]'
)
WIZARD_ALLOCATION_BUTTON = (
    By.XPATH,
    '//header/button/span[contains(text(), \'Confirm\')]'
)
WIZARD_VISIBLE_BUTTON = (
    By.CSS_SELECTOR,
    '.modal .oe_form header .oe_form_button:not(.oe_form_invisible)'
)

MODAL_TABLE = (
    By.CSS_SELECTOR,
    '.modal .oe_form_sheet .oe_form_field:not(.oe_form_invisible) '
    '.oe_list_content'
)
MODAL_TABLE_ROW = (
    By.CSS_SELECTOR,
    '.modal .oe_form_sheet .oe_form_field:not(.oe_form_invisible) '
    '.oe_list_content tbody tr'
)
DEALLOCATION_TABLE_BED_COL = (
    By.CSS_SELECTOR,
    'td[data-field=name]'
)
DEALLOCATION_TABLE_WM_COL = (
    By.CSS_SELECTOR,
    'td[data-field=assigned_wm_ids]'
)
DEALLOCATION_TABLE_NURSE_COL = (
    By.CSS_SELECTOR,
    'td[data-field=assigned_nurse_ids]'
)
DEALLOCATION_TABLE_HCA_COL = (
    By.CSS_SELECTOR,
    'td[data-field=assigned_hca_ids]'
)
ALLOCATE_WIZARD_BUTTON = (
    By.CSS_SELECTOR,
    'td button[title=Allocate]'
)
ALLOCATE_TABLE_BED_COL = (
    By.CSS_SELECTOR,
    'td[data-field=location_id]'
)
