""" Selectors for list view """
from selenium.webdriver.common.by import By


LIST_VIEW_CONTAINER = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_view_manager_body .oe_list_content'
)
LIST_VIEW_ROW = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_view_manager_body '
    '.oe_list_content tbody:last-child() tr'
)
PATIENTS_BY_WARD_CHART_BUTTON = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_view_manager_body '
    '.oe_list_content tr .oe_list_field_action button[title=Chart]'
)
PATIENTS_BY_WARD_LIST_BUTTON = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_view_manager_body '
    '.oe_list_content tr .oe_list_field_action button[title=EWS]'
)
PATIENTS_WITHOUT_BED_PLACEMENT_BUTTON = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_view_manager_body '
    '.oe_list_content tr .oe_list_field_object button[title=Complete]'
)
LIST_ITEM_SELECT_BOX = (
    By.CSS_SELECTOR,
    '.oe_list_record_selector > input[type=checkbox]'
)
LIST_ITEM_SELECTED_SELECT_BOX = (
    By.CSS_SELECTOR,
    '.oe_list_record_selector > input:checked'
)
