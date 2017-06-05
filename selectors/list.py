"""
Selectors for List Component
The list component is used in the mobile to show the list of tasks and the list
of patients
"""

from selenium.webdriver.common.by import By

LIST_CONTAINER = (By.CLASS_NAME, 'tasklist')
LIST_ITEM = (By.CSS_SELECTOR, '.tasklist li a')
UNKNOWN_CLINICAL_RISK_LIST_ITEM = \
    (By.CSS_SELECTOR, '.tasklist li a.level-not-set')
LOW_CLINICAL_RISK_LIST_ITEM = (By.CSS_SELECTOR, '.tasklist li a.level-one')
MEDIUM_CLINICAL_RISK_LIST_ITEM = (By.CSS_SELECTOR, '.tasklist li a.level-two')
HIGH_CLINICAL_RISK_LIST_ITEM = (By.CSS_SELECTOR, '.tasklist li a.level-three')
STATUS_LIST_ITEM = (By.CSS_SELECTOR, '.tasklist li.status-alert')
STATUS_LIST_ITEM_FLAG = \
    (By.CSS_SELECTOR, '.tasklist li.status-alert .status-flag')
LIST_ITEM_DATA_ROW = (By.CSS_SELECTOR, '.tasklist li a .task-meta')
LIST_ITEM_DATA_LEFT = (By.CSS_SELECTOR, '.tasklist li a .task-meta .task-left')
LIST_ITEM_DATA_RIGHT = \
    (By.CSS_SELECTOR, '.tasklist li a .task-meta .task-right')
LIST_ITEM_DATA_INFO = (By.CSS_SELECTOR, '.tasklist li a .task-meta .taskInfo')
LIST_ITEM_DATA_NAME = (By.CSS_SELECTOR, 'a .task-meta .task-left strong')
