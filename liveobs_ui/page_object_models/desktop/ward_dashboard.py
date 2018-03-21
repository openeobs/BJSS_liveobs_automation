""" Ward Dashboard Page Object Model """
from liveobs_ui.page_object_models.desktop.kanban_view_common import \
    BaseKanbanViewPage
from liveobs_ui.selectors.desktop.kanban_selectors import KANBAN_CARD_BUTTON


class WardDashboardPage(BaseKanbanViewPage):
    """ Interaction with the Ward Dashboard page """

    def go_to_ward_dashboard(self):
        """ Navigate the user to the ward dashboard """
        self.go_to_page('Ward Dashboard')

    def open_acuity_board(self, ward_name):
        """
        Open the Acuity Board for the supplied ward name

        :param ward_name: Name of the ward to open the Acuity Board of
        """
        ward_card = self.get_kanban_card_by_name(ward_name)
        acuity_board_button = ward_card.find_element(*KANBAN_CARD_BUTTON)
        self.click_and_verify_change(
            acuity_board_button, KANBAN_CARD_BUTTON, hidden=True)
