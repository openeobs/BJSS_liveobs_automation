""" Common Kanban view functionality """
from selenium.common.exceptions import NoSuchElementException
from liveobs_ui.page_object_models.desktop.desktop_common import \
    BaseDesktopPage
from liveobs_ui.selectors.desktop.kanban_selectors import KANBAN_CARD, \
    KANBAN_CARD_CONTENT, KANBAN_CONTAINER


class BaseKanbanViewPage(BaseDesktopPage):
    """ Interaction with Kanban views """

    def get_kanban_cards(self):
        """
        Get all the kanban cards in the current view

        :return: List of kanban card elements
        """
        try:
            self.wait_for_element(KANBAN_CARD)
        except NoSuchElementException:
            pass
        return self.driver.find_elements(*KANBAN_CARD)

    def get_kanban_card_by_name(self, search_string):
        """
        Get a kanban card that contains the specified search string

        :param search_string: String to find in kanban card content
        :return: Kanban card element
        """
        for kanban_item in self.get_kanban_cards():
            kanban_item_content = \
                kanban_item.find_element(*KANBAN_CARD_CONTENT)
            if search_string in kanban_item_content.text:
                return kanban_item

    def open_kanban_card(self, card):
        """
        Open the supplied kanban card

        :param card: Element for kanban card to open
        """
        self.click_and_verify_change(card, KANBAN_CONTAINER, hidden=True)

    def open_kanban_card_with_name(self, search_string):
        """
        Locate and click the kanban card that contains the specified search
        string

        :param search_string: String to find with kanban card content
        """
        self.open_kanban_card(self.get_kanban_card_by_name(search_string))

    def wait_for_kanban_view_to_load(self):
        """
        Wait until the kanban container has loaded, useful for ensuring that
        nothing is executed until the view has loaded
        """
        self.wait_for_element(KANBAN_CONTAINER)
