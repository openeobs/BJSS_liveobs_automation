""" Page Object Model for Acuity Board """

from liveobs_ui.page_object_models.desktop.wardboard_common import \
    WardBoardPage
from liveobs_ui.page_object_models.desktop.kanban_view_common import \
    BaseKanbanViewPage


class AcuityBoardPage(WardBoardPage, BaseKanbanViewPage):
    """ Interact with the Acuity Board """

    def go_to_the_acuity_board(self):
        """ Navigate to the Acuity Board """
        self.go_to_page('Acuity Board')
