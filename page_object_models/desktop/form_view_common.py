""" Common form view functionality """
from liveobs_ui.page_object_models.desktop.desktop_common import \
    BaseDesktopPage
from liveobs_ui.selectors.desktop.form_selectors import \
    FORM_ACTIONBAR_BUTTON, FORM_TABS


class BaseFormViewPage(BaseDesktopPage):
    """ Interaction with form view """

    def get_actionbar_buttons(self):
        """
        Get the buttons that sit in the form's actionbar

        :return: List of button elements
        """
        return self.driver.find_elements(*FORM_ACTIONBAR_BUTTON)

    def get_actionbar_button_by_name(self, button_name):
        """
        Get a button that sits in the form's actionbar that has the specified
        name

        :param button_name: Name of button to get
        :return: Button element
        """
        buttons = self.get_actionbar_buttons()
        for button in buttons:
            if button_name in button.text:
                return button

    def get_tabs(self):
        """
        Get tabs on form view

        :return: List of tab elements
        """
        return self.driver.find_elements(*FORM_TABS)

    def get_tab_by_name(self, tab_name):
        """
        Get tab in form view with specified name

        :param tab_name: Name of the tab to get
        :return: tab element
        """
        tabs = self.get_tabs()
        for tab in tabs:
            if tab_name in tab.text:
                return tab
