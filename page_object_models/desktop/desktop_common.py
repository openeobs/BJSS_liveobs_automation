""" Page Object Model that deals with common desktop functionality """
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from liveobs_ui.selectors.desktop.navigation_selectors import \
    LEFT_NAVIGATION_ITEMS
from liveobs_ui.selectors.desktop.search_selectors import \
    SEARCH_OPTIONS_DRAW_BUTTON, SEARCH_DRAWER, SEARCH_DRAWER_FILTER_ITEMS, \
    SEARCH_DRAWER_GROUP_BY_ITEMS, SEARCH_INPUT, SEARCH_AUTOCOMPLETE, \
    SEARCH_AUTOCOMPLETE_ITEM
from liveobs_ui.page_object_models.common.base_liveobs_page import \
    BaseLiveObsPage


class BaseDesktopPage(BaseLiveObsPage):
    """
        Base class to initialise the base page
        that will be called from all pages
    """

    def go_to_page(self, page_title):
        """
        Go to the supplied page in the left hand menu based on the title of
        the page

        :param page_title: Title of the page to go to
        """
        pages = self.driver.find_elements(*LEFT_NAVIGATION_ITEMS)
        for page in pages:
            if page_title in page.text:
                page_id = page.get_attribute('data-action-id')
                page_active_selector = (
                    By.CSS_SELECTOR,
                    '.oe_secondary_submenu li.active '
                    'a[@data-action-id={}]'.format(page_id)
                )
                self.click_and_verify_change(page, page_active_selector)

    def select_filter(self, filter_name):
        """
        Open up the search options draw and select a filter based on filter
        name

        :param filter_name: Name of the filter to select
        """
        self.open_search_options_draw()
        filter_items = self.driver.find_elements(*SEARCH_DRAWER_FILTER_ITEMS)
        for filter_item in filter_items:
            if filter_name in filter_item.text:
                data_id = filter_item.get_attribute('data-index')
                filter_selector = (
                    By.CSS_SELECTOR,
                    '.oe_webclient .oe_application .oe_view_manager '
                    '.oe_view_manager_body .oe_search_drawer '
                    '.oe_searchview_filters dd:first-child()'
                    'li.badge[@data-index={}]'.format(data_id)
                )
                self.click_and_verify_change(filter_item, filter_selector)

    def open_search_options_draw(self):
        """
        Open the search options draw on the current page
        """
        open_draw_button = \
            self.driver.find_element(*SEARCH_OPTIONS_DRAW_BUTTON)
        self.click_and_verify_change(open_draw_button, SEARCH_DRAWER)

    def close_search_options_draw(self):
        """
        Close the search options draw on the current page
        """
        close_draw_button = \
            self.driver.find_element(*SEARCH_OPTIONS_DRAW_BUTTON)
        self.click_and_verify_change(
            close_draw_button, SEARCH_DRAWER, hidden=True)

    def select_group_by(self, group_by_name):
        """
        Open the search options draw and select a group by based on the
        supplied name

        :param group_by_name: Name of the group by option to select
        """
        self.open_search_options_draw()
        group_by_items = \
            self.driver.find_elements(*SEARCH_DRAWER_GROUP_BY_ITEMS)
        for group_by_item in group_by_items:
            if group_by_name in group_by_item.text:
                data_id = group_by_item.get_attribute('data-index')
                group_by_selector = (
                    By.CSS_SELECTOR,
                    '.oe_webclient .oe_application .oe_view_manager '
                    '.oe_view_manager_body .oe_search_drawer '
                    '.oe_searchview_filters dd:last-child()'
                    'li.badge[@data-index={}]'.format(data_id)
                )
                self.click_and_verify_change(group_by_item, group_by_selector)

    def perform_search(self, search_query, search_type=None):
        """
        Using the searchview conduct a search with the supplied search query

        :param search_query: Query to input into the search box
        :param search_type: Type of search (uses Odoo Search autocomplete)
        """
        search_input = self.driver.find_element(*SEARCH_INPUT)
        search_input.send_keys(str(search_query))
        self.wait_for_element(*SEARCH_AUTOCOMPLETE)
        if not search_type:
            search_input.send_keys(Keys.ENTER)
        else:
            autocomplete_items = \
                self.driver.find_elements(*SEARCH_AUTOCOMPLETE_ITEM)
            for autocomplete_item in autocomplete_items:
                if search_type in autocomplete_item.text:
                    self.click_and_verify_change(
                        autocomplete_item, SEARCH_AUTOCOMPLETE, hidden=True)

    # Change view

    # Go to next record in list

    # Go to previous record in list
