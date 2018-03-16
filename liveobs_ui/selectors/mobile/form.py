"""
Selectors for form component
The form component is used in the mobile to allow the user to input data for
observations and tasks
"""

from selenium.webdriver.common.by import By

PATIENT_INFO_CONTAINER = (By.CSS_SELECTOR, '#patientName')
PATIENT_INFO = (By.CSS_SELECTOR, '#patientName a')
PATIENT_INFO_BUTTON = (By.CSS_SELECTOR, '#patientName .icon-info')

FORM = (By.CSS_SELECTOR, '#obsForm')
FORM_FIELD_CONTAINER = (By.CSS_SELECTOR, '#obsForm .obsField')
FORM_SELECT_FIELD_CONTAINER = (By.CSS_SELECTOR, '#obsForm .obsSelectField')
FORM_HIDDEN_FIELD_CONTAINER = (By.CSS_SELECTOR, '#obsForm .obsField.valHide')
FORM_HIDDEN_SELECT_FIELD_CONTAINER = \
    (By.CSS_SELECTOR, '#obsForm .obsSelectField.valHide')
FORM_ERRORED_FIELD_CONTAINER = (By.CSS_SELECTOR, '#obsForm .obsField.error')
FORM_ERRORED_SELECT_FIELD_CONTAINER = \
    (By.CSS_SELECTOR, '#obsForm .obsSelectField.error')
FORM_FIELD_HEADER = (By.CSS_SELECTOR, '#obsForm .obsField .input-header')
FORM_SELECT_FIELD_HEADER = \
    (By.CSS_SELECTOR, '#obsForm .obsSelectField .input-header')
FORM_FIELD_LABEL = (By.CSS_SELECTOR, '#obsForm .obsField .input-header label')
FORM_SELECT_FIELD_LABEL = \
    (By.CSS_SELECTOR, '#obsForm .obsSelectField .input-header label')
FORM_FIELD_INPUT = (By.CSS_SELECTOR, '#obsForm .obsField input')
FORM_FIELD_TEXTAREA = (By.CSS_SELECTOR, '#obsform .obsField textarea')
FORM_SELECT_FIELD_DROPDOWN = \
    (By.CSS_SELECTOR, '#obsForm .obsSelectField select')
FORM_SELECT_FIELD_CHECKBOX_LIST = \
    (By.CSS_SELECTOR, '#obsForm .obsSelectField .checklist')
FORM_SELECT_FIELD_CHECKBOX_LIST_ITEM_INPUT = \
    (By.CSS_SELECTOR, '#obsForm .obsSelectField .checklist li input')
FORM_SELECT_FIELD_CHECKBOX_LIST_ITEM_LABEL = \
    (By.CSS_SELECTOR, '#obsForm .obsSelectField .checklist li label')
FORM_FIELD_BODY = (By.CSS_SELECTOR, '#obsForm .obsField .input-body')
FORM_SELECT_FIELD_BODY = \
    (By.CSS_SELECTOR, '#obsForm .obsSelectField .input-body')
FORM_FIELD_ERROR_MESSAGE = \
    (By.CSS_SELECTOR, '#obsForm .obsField .input-body .errors')
FORM_SELECT_FIELD_ERROR_MESSAGE = \
    (By.CSS_SELECTOR, '#obsForm .obsSelectField .input-body .errors')
FORM_FIELD_HELP_MESSAGE = \
    (By.CSS_SELECTOR, '#obsForm .obsField .input-body .help')
FORM_SELECT_FIELD_HELP_MESSAGE = \
    (By.CSS_SELECTOR, '#obsForm .obsField .input-body .help')
FORM_FIELD_REFERENCE = \
    (By.CSS_SELECTOR, '#obsForm .obsField .input-body .reference')
FORM_SELECT_FIELD_REFERENCE = \
    (By.CSS_SELECTOR, '#obsForm .obsSelectField .input-body .reference')

FORM_TITLE = (By.CSS_SELECTOR, '#obsForm > h3')
FORM_DESCRIPTION = (By.CSS_SELECTOR, '#obsForm > p')

FORM_CANCEL_BUTTON = \
    (By.CSS_SELECTOR, '#obsForm .obsConfirm input[type="reset"]')
FORM_SUBMIT_BUTTON = \
    (By.CSS_SELECTOR, '#obsForm .obsSubmit input[type="submit"]')
