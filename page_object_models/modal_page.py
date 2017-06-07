"""
Page Object Model for Modals
While Technically Modals are not 'pages' there are common interaction patterns
with modals that merit their own Page Object Model. This is that Page Object
Model.
"""
from selenium.webdriver.common.by import By
from liveobs_ui.page_object_models.mobile_common import BaseMobilePage
from liveobs_ui.selectors.modal import MODAL_DIALOG, MODAL_TITLE, \
    MODAL_BUTTONS, MODAL_CONTENT


class ModalPage(BaseMobilePage):
    """
    Class that handles interacting with Modals
    """

    @staticmethod
    def _get_selector_for_modal(modal):
        """
        Given a modal return a By selector

        :param modal: Modal to generate selector for
        :return: By selector
        """
        modal_id = modal.get_attribute('id')
        return (By.ID, modal_id)

    def close_modal(self, modal):
        """
        Close supplied modal

        :param modal: Modal object (.dialog) to close
        """
        modal_selector = self._get_selector_for_modal(modal)
        cover = self.get_cover_for_modal(modal)
        self.click_and_verify_change(cover, modal_selector, hidden=True)

    def get_open_modals(self):
        """
        Get the currently open modals on the page

        :return: list of modal objects
        """
        return self.driver.find_elements(*MODAL_DIALOG)

    def get_cover_for_modal(self, modal):
        """
        Get the cover that is associated with the modal

        :param modal: Modal to find cover for
        :return: cover object
        """
        modal_id = modal.get_attribute('id')
        cover_selector = (By.CSS_SELECTOR, '.cover[data-target={}]'.format(
            modal_id))
        return self.driver.find_element(*cover_selector)

    @staticmethod
    def get_modal_title(modal):
        """
        Get the title text for the supplied modal

        :param modal: Modal to get title for
        :return: Text content of the title element
        """
        title = modal.find_element(*MODAL_TITLE)
        return title.text

    @staticmethod
    def get_modal_options(modal):
        """
        Get the option buttons for the supplied modal

        :param modal: Modal to find option buttons for
        :return: List of button elements
        """
        return modal.find_elements(*MODAL_BUTTONS)

    @staticmethod
    def get_modal_content(modal):
        """
        Get the text content of the supplied modal

        :param modal: Modal to get content of
        :return: Text content of modal
        """
        content = modal.find_element(*MODAL_CONTENT)
        return content.text

    def click_modal_option(self, modal, option_title):
        """
        Locate the option in the modal options and click it

        :param modal: Modal to find option in
        :param option_title: Title of the button to click
        """
        options = self.get_modal_options(modal)
        button = None
        for option in options:
            if option.text == option_title:
                button = option
        if button:
            modal_selector = self._get_selector_for_modal(modal)
            self.click_and_verify_change(button, modal_selector, hidden=True)
