""" Module that contains the DesktopNotificationPage class. """
from liveobs_ui.page_object_models.desktop.modal_view_common \
    import BaseDesktopPage

from liveobs_ui.selectors.desktop.error_selectors import \
    NOTIFICATION_ERROR_MESSAGE_FIRST_LINE, \
    NOTIFICATION_ERROR_MESSAGE_LIST_ITEMS


class DesktopNotificationPage(BaseDesktopPage):
    """
    Page object for the desktop notification. This is the small black
    notification box that appears briefly in the upper right corner of the
    screen for things like required fields not being populated.
    """
    def get_error_message_first_line(self):
        """
        Get the first line of the error message.

        :return:
        :rtype: str
        """
        return self.driver.find_element(
            *NOTIFICATION_ERROR_MESSAGE_FIRST_LINE).text

    def get_error_message_list_items(self):
        """
        Get the text in the bullet pointed list of items that comes after the
        first line of the error message.

        :return:
        :rtype: str
        """
        list_elements = self.driver.find_elements(
            *NOTIFICATION_ERROR_MESSAGE_LIST_ITEMS)
        list_texts = [element.text for element in list_elements]
        return list_texts
