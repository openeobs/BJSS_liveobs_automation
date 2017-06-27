""" Selectors for View mode and page changing """
from selenium.webdriver.common.by import By

VIEW_MANAGER_SWITCH_CONTAINER = \
    (By.CSS_SELECTOR, '.oe_webclient .oe_header_row .oe_view_manager_switch')
VIEW_MANAGER_SWITCH_KANBAN_BUTTON = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_header_row .oe_view_manager_switch .oe_vm_switch_kanban'
)
VIEW_MANAGER_SWITCH_LIST_BUTTON = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_header_row .oe_view_manager_switch .oe_vm_switch_list'
)
VIEW_MANAGER_SWITCH_FORM_BUTTON = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_header_row .oe_view_manager_switch .oe_vm_switch_form'
)
VIEW_MANAGER_KANBAN = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_view_manager_wrapper '
    '.oe_view_manager_view_kanban'
)
VIEW_MANAGER_LIST = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_view_manager_wrapper '
    '.oe_view_manager_view_list'
)
VIEW_MANAGER_FORM = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_application .oe_view_manager_wrapper '
    '.oe_view_manager_view_form'
)

VIEW_MANAGER_PAGER_CONTAINER = \
    (By.CSS_SELECTOR, '.oe_webclient .oe_header_row .oe_view_manager_pager')
VIEW_MANAGER_PAGER_PREVIOUS = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_header_row .oe_view_manager_pager '
    ' a[data-pager-action=previous]'
)
VIEW_MANAGER_PAGER_NEXT = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_header_row .oe_view_manager_pager '
    ' a[data-pager-action=next]'
)
VIEW_MANAGER_WAIT = (By.CSS_SELECTOR, 'body.oe_wait')
VIEW_MANAGER_BREADCRUMB = (
    By.CSS_SELECTOR,
    '.oe_webclient .oe_header_row a.oe_breadcrumb_item'
)
