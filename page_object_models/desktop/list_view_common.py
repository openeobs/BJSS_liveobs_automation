""" Common functionality for list views """
from liveobs_ui.page_object_models.desktop.desktop_common import \
    BaseDesktopPage
from liveobs_ui.selectors.desktop.list_selectors import LIST_VIEW_ROW
from liveobs_ui.selectors.desktop.view_selectors import VIEW_MANAGER_FORM


class BaseListViewPage(BaseDesktopPage):
    """ Common functionality for list view pages """

    def get_list_items(self):
        """
        Get a list of items in the list view

        :return: list of list items
        """
        return self.driver.find_elements(*LIST_VIEW_ROW)

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

    def open_list_item(self, search_string):
        """
        Find the row in the list for the search_string and open the item

        :param search_string: string to find in the list item
        """
        list_row = self.get_list_item_by_name(search_string)
        self.click_and_verify_change(list_row, VIEW_MANAGER_FORM)
