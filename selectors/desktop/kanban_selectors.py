""" Selectors for Kanban Views """
from selenium.webdriver.common.by import By

KANBAN_CONTAINER = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_view_manager .oe_view_manager_view_kanban '
    '.oe_kanban_groups'
)
KANBAN_COLUMN_HEADER = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_view_manager .oe_view_manager_view_kanban '
    '.oe_kanban_groups .oe_kanban_groups_headers .oe_kanban_group_header'
)
KANBAN_COLUMN_BODY = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_view_manager .oe_view_manager_view_kanban '
    '.oe_kanban_groups .oe_kanban_groups_records .oe_kanban_column')
KANBAN_COLUMN_MENU = (
    By.CSS_SELECTOR, '.oe_dropdown_toggle.oe_dropdown_kanban')
KANBAN_COLUMN_MENU_ITEM = (
    By.CSS_SELECTOR,
    '.oe_dropdown_kanban.oe_opened '
    '.oe_dropdown_menu li a[@data-action=toggle-fold]'
)
KANBAN_CARD = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_view_manager .oe_view_manager_view_kanban '
    '.oe_kanban_column_cards .oe_kanban_card'
)
KANBAN_CARD_CONTENT = (By.CLASS_NAME, 'oe_kanban_content')
