"""
Selectors for Header component
The header component is used in the mobile to show to floating menu at the
top of the page
"""
from selenium.webdriver.common.by import By

HEADER_CONTAINER = (By.CLASS_NAME, 'header')
HEADER_MAIN = (By.CLASS_NAME, 'header-main')
HEADER_LOGO = (By.CSS_SELECTOR, '.header .logo')
HEADER_META = (By.CLASS_NAME, 'header-meta')
HEADER_MENU = (By.CLASS_NAME, 'header-menu')
HEADER_MENU_LIST_ITEM = (By.CSS_SELECTOR, '.header-menu li')
HEADER_MENU_BADGE = (By.CSS_SELECTOR, '.header-menu li .urgent-badge')
HEADER_SELECTED_MENU_ITEM = (By.CSS_SELECTOR, '.header-menu li.selected')
