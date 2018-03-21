""" Selectors for Nursing Shift Change Wizard """
from selenium.webdriver.common.by import By


ALLOCATION_WIZARD_TITLE = (
    By.XPATH,
    '//div[@class="modal-header"]/h3[contains(text(), "Allocation")]'
)
ALLOCATION_WIZARD = (
    By.XPATH,
    '//body/div[@class=\'modal in\'][2]'
)
ALLOCATION_NURSE_INPUT = (
    By.CSS_SELECTOR,
    '.oe_form_group .oe_form_group_row:nth-child(2) .oe_form_field input'
)
ALLOCATION_HCA_INPUT = (
    By.CSS_SELECTOR,
    '.oe_form_group .oe_form_group_row:nth-child(3) .oe_form_field textarea'
)
ALLOCATION_SAVE_BUTTON = (
    By.CSS_SELECTOR,
    '.oe_form_button_save'
)
