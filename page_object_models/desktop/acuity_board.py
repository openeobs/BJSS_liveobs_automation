""" Page Object Model for Acuity Board """
from liveobs_ui.page_object_models.desktop.desktop_common import \
    BaseDesktopPage
from liveobs_ui.selectors.desktop.kanban_selectors import KANBAN_CARD, \
    KANBAN_CARD_CONTENT, KANBAN_CONTAINER


class AcuityBoardPage(BaseDesktopPage):
    """ Interact with the Acuity Board """

    def go_to_the_acuity_board(self):
        """ Navigate to the Acuity Board """
        self.go_to_page('Acuity Board')

    def group_by_clinical_risk(self):
        """ Group the Acuity Board by Clinical Risk """
        self.select_group_by('Clinical Risk')

    def group_by_ward(self):
        """ Group the Acuity Board by Ward """
        self.select_group_by('Ward')

    def select_no_risk_filter(self):
        """ Select the No Risk Filter """
        self.select_filter('No Risk')

    def select_low_risk_filter(self):
        """ Select the Low Risk Filter """
        self.select_filter('Low Risk')

    def select_medium_risk_filter(self):
        """ Select the Medium Risk Filter """
        self.select_filter('Medium Risk')

    def select_high_risk_filter(self):
        """ Select the High Risk Filter """
        self.select_filter('High Risk')

    def select_deteriorating_trend_filter(self):
        """ Select the Deteriorating Trend filter """
        self.select_filter('Deteriorating Trend')

    def select_improving_trend_filter(self):
        """ Select the Improving Trend filter """
        self.select_filter('Improving Trend')

    def select_unchanged_trend_filter(self):
        """ Select the Unchanged Trend filter """
        self.select_filter('Unchanged Trend')

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
