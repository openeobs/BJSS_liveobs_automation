""" Common functionality for list views """
from selenium.webdriver.common.by import By
from liveobs_ui.page_object_models.desktop.desktop_common import \
    BaseDesktopPage
from liveobs_ui.selectors.desktop.list_selectors import LIST_VIEW_ROW


class BaseListViewPage(BaseDesktopPage):
    """ Common functionality for list view pages """

    def get_list_items(self):
        """
        Get a list of items in the list view

        :return: list of list items
        """
        list_items = self.driver.find_elements(*LIST_VIEW_ROW)
        return [el for el in list_items if el.text.strip() != '']

    def get_list_item_by_name(self, search_string):
        """
        Get a specific list item for the supplied string

        :param search_string: String to find in row
        :return: element for list item with string it in
        """
        list_items = self.get_list_items()
        for list_item in list_items:
            if search_string in list_item.text:
                return list_item

    def open_list_item_by_name(self, search_string):
        """
        Find the row in the list for the search_string and open the item

        :param search_string: string to find in the list item
        """
        list_row = self.get_list_item_by_name(search_string)
        self.open_list_item(list_row)

    def open_list_item(self, list_item):
        """
        Open the supplied list item

        :param list_item: List Item to open
        """
        item_id = list_item.get_attribute('data-id')
        selector = LIST_VIEW_ROW
        if item_id:
            selector = (
                By.CSS_SELECTOR,
                '.oe_webclient .oe_application .oe_view_manager_body '
                '.oe_list_content tbody > tr[data-id=\'{}\']'.format(item_id)
            )
        self.click_and_verify_change(list_item, selector, hidden=True)

    def wait_for_list_view_to_load(self):
        """
        Wait until the list container has loaded, useful for ensuring that
        nothing is executed until the view has loaded
        """
        self.wait_for_element(LIST_VIEW_ROW)
