"""
Page Object Model for List Page
The List Page is a base class for the task and patient lists as they use the
same template to render content
"""
from liveobs_ui.page_object_models.mobile.mobile_common import BaseMobilePage
from liveobs_ui.selectors.mobile.list import LIST_ITEM, LIST_CONTAINER, \
    LIST_ITEM_DATA_NAME, LIST_ITEM_DATA_INFO


class ListPage(BaseMobilePage):
    """
    Class that handles generic list page functionality
    """

    def get_list_items(self):
        """
        Get a list of the items in the task / patient list

        :return: A list of ``a`` tags from the list
        :rtype: list
        """
        return self.driver.find_elements(*LIST_ITEM)

    def get_list_item(self, text_to_find):
        """
        Get a specific item from the list

        :param text_to_find: Text that should be in the list item to be found
        :type text_to_find: str
        :return: The list item if found or None
        """
        list_items = self.get_list_items()
        list_item = [el for el in list_items if text_to_find in el.text]
        if list_item:
            return list_item[0]
        return None

    def open_item(self, list_item):
        """
        Open (click on) the supplied list item and ensure that the page has
        been successfully loaded

        :param list_item: List Item to click on
        :return: True if successfully opened item, False if not
        """
        list_item_url = list_item.get_attribute('href')
        self.click_and_verify_change(list_item, LIST_CONTAINER, hidden=True)
        return list_item_url in self.driver.current_url

    @staticmethod
    def get_patient_from_item(list_item):
        """
        Get the patient's name from list item

        :param list_item: WebElement for List Item
        :return: name of patient the list item is about
        """
        patient_name_el = list_item.find_element(*LIST_ITEM_DATA_NAME)
        return patient_name_el.text

    @staticmethod
    def get_task_info_from_item(list_item):
        """
        Get the .taskInfo element from the list item

        :param list_item: WebElement for List Item
        :return: text inside .taskInfo element of List Item
        """
        task_info_el = list_item.find_element(*LIST_ITEM_DATA_INFO)
        return task_info_el.text
