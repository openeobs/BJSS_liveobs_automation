""" Common Modal Page Object Model """
from liveobs_ui.page_object_models.desktop.desktop_common import \
    BaseDesktopPage
from liveobs_ui.selectors.desktop.modal_selectors import MODAL_TITLE, \
    MODAL_HEADER_CLOSE, MODAL_CONTAINER, MODAL_FOOTER_BUTTONS


class BaseModalPage(BaseDesktopPage):
    """ Common interaction patterns with modal dialogs """

    @staticmethod
    def get_modal_title(modal):
        """
        Get the title of the supplied modal

        :param modal: Modal to get title for
        :return: Title for supplied modal
        :rtype: str
        """
        title_el = modal.find_element(*MODAL_TITLE)
        return title_el.text

    def close_modal(self, modal):
        """
        Close the supplied modal

        :param modal: Modal to close
        """
        close_button = modal.find_element(*MODAL_HEADER_CLOSE)
        self.click_and_verify_change(
            close_button, MODAL_CONTAINER, hidden=True)

    @staticmethod
    def get_modal_buttons(modal):
        """
        Get the buttons in the supplied modal's footer

        :param modal: Modal to get buttons for
        :return: list of button elements
        """
        return modal.find_elements(*MODAL_FOOTER_BUTTONS)

    def get_modal_button_by_name(self, modal, name):
        """
        Get a button in the modal's footer with a specified name

        :param modal: Modal to find button in
        :param name: Name of button
        :return: button element
        """
        buttons = self.get_modal_buttons(modal)
        for button in buttons:
            if name in button.text:
                return button

    def click_modal_button_by_name(self, modal, name):
        """
        Click a button in modal's footer with a specified name

        :param modal: Modal to click button in
        :param name: Name of button to click
        """
        button = self.get_modal_button_by_name(modal, name)
        self.click_and_verify_change(button, MODAL_CONTAINER, hidden=True)

    def get_currently_open_modal(self):
        """
        Get the currently open modal on the screen

        :return: Modal element
        """
        return self.driver.find_element(*MODAL_CONTAINER)
