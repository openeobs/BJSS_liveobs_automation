""" Selectors for the patient information page """

from selenium.webdriver.common.by import By

ADHOC_OBS_MENU_BUTTON = (By.ID, 'take-observation')
OPEN_OBS_MENU = (By.ID, 'obs_menu')
OPEN_OBS_MENU_TITLE = (By.CSS_SELECTOR, '#obs_menu h2')
OPEN_OBS_MENU_LIST_ITEMS = (By.CSS_SELECTOR, '#obs_menu .menu li a')
OPEN_OBS_MENU_NEWS = (By.CSS_SELECTOR, '#obs_menu li a:first-child')
OPEN_OBS_MENU_CLOSE_BUTTON = \
    (By.CSS_SELECTOR, '#obs_menu options li:first-child() a')

