""" Page Object Model for Acuity Board """

from liveobs_ui.page_object_models.desktop.wardboard_common import \
    WardBoardPage
from liveobs_ui.page_object_models.desktop.kanban_view_common import \
    BaseKanbanViewPage
from liveobs_ui.selectors.desktop.kanban_selectors import KANBAN_CARD


class AcuityBoardPage(WardBoardPage, BaseKanbanViewPage):
    """ Interact with the Acuity Board """

    def go_to_the_acuity_board(self):
        """ Navigate to the Acuity Board """
        self.go_to_page('Acuity Board')

    def wait_for_data_refresh(self):
        """ Wait for the kanban data to refresh """
        super(AcuityBoardPage, self).wait_for_data_refresh()
        self.wait_for_element(KANBAN_CARD)
