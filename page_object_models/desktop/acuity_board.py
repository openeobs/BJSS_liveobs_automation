""" Page Object Model for Acuity Board """

from liveobs_ui.page_object_models.desktop.wardboard_common import \
    WardBoardPage
from liveobs_ui.selectors.desktop.kanban_selectors import KANBAN_CARD, \
    KANBAN_CARD_CONTENT, KANBAN_CONTAINER


class AcuityBoardPage(WardBoardPage):
    """ Interact with the Acuity Board """

    def go_to_the_acuity_board(self):
        """ Navigate to the Acuity Board """
        self.go_to_page('Acuity Board')

    def open_patient_record(self, patient_name):
        """
        Select and open the patient record for the patient with the
        supplied name

        :param patient_name: Name of the patient that we want to open the
            record of
        """
        kanban_items = self.driver.find_elements(*KANBAN_CARD)
        for kanban_item in kanban_items:
            kanban_item_content = \
                kanban_item.find_element(*KANBAN_CARD_CONTENT)
            if patient_name in kanban_item_content.text:
                self.click_and_verify_change(
                    kanban_item, KANBAN_CONTAINER, hidden=True)
