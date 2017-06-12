""" Selectors for Desktop Navigation """
from selenium.webdriver.common.by import By


SEARCH_CONTAINER = \
    (By.CSS_SELECTOR, '.oe_webclient .oe_application .oe_searchview')
SEARCH_INPUT = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_searchview .oe_searchview_input'
)
SEARCH_AUTOCOMPLETE = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_searchview .oe-autocomplete'
)
SEARCH_AUTOCOMPLETE_ITEM = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_searchview .oe-autocomplete ul li'
)
SEARCH_OPTIONS_DRAW_BUTTON = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_searchview .oe_searchview_unfold_drawer'
)
SEARCH_DRAWER = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_view_manager '
    '.oe_view_manager_body .oe_searchview_drawer'
)
SEARCH_DRAWER_FILTER_ITEMS = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_view_manager '
    '.oe_view_manager_body .oe_search_drawer '
    '.oe_searchview_filters:first-child() > dl > dd > ul > li'
)

SEARCH_DRAWER_GROUP_BY_ITEMS = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_view_manager '
    '.oe_view_manager_body .oe_search_drawer '
    '.oe_searchview_filters:last-child() > dl > dd > ul > li'
)
