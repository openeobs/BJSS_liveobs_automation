"""
Selectors for Stand-in List component
The stand-in list component is used to show the list of patients the user is
responsible for and the following data:
- The users the user has shared the patient with
- The users following the patient
- The users with invitations to follow the patient
"""

from selenium.webdriver.common.by import By

STAND_IN_LIST = (By.CLASS_NAME, 'sharelist')
STAND_IN_SHARE_ALL_BUTTON = (By.CSS_SELECTOR, '.sharelist .share_all')
STAND_IN_LIST_ITEM_SHARED = (By.CSS_SELECTOR, '.sharelist label.shared')
STAND_IN_LIST_ITEM_CHECKBOX = \
    (By.CSS_SELECTOR, '.sharelist label .patient-share')
STAND_IN_LIST_ITEM_PATIENT_DATA = \
    (By.CSS_SELECTOR, '.sharelist label .task-meta:first-child()')
STAND_IN_LIST_ITEM_SHARE_DATA = \
    (By.CSS_SELECTOR, '.sharelist label .task-meta:last-child() .taskInfo')
