""" Common functionality for list views """
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
