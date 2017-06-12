""" Selectors for Desktop Navigation """
from selenium.webdriver.common.by import By


TOP_NAVIGATION_CONTAINER = (By.CSS_SELECTOR, '#oe_main_menu_placeholder > ul')
TOP_NAVIGATION_ITEM = \
    (By.CSS_SELECTOR, '#oe_main_menu_placeholder > ul > li > a')

LEFT_NAVIGATION_CONTAINER = (
    By.CSS_SELECTOR,
    '.openerp_webclient_container .oe_webclient '
    'td.oe_leftbar .oe_secondary_menus_container'
)

LEFT_NAVIGATION_ITEMS = (
    By.CSS_SELECTOR,
    '.openerp_webclient_container .oe_webclient '
    'td.oe_leftbar .oe_secondary_menu_container '
    '.oe_secondary_menu .oe_secondary_submenu > li > a'
)
