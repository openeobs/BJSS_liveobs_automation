# pylint:disable=invalid-name
""" Common functionality for ward board pages """
from liveobs_ui.page_object_models.desktop.desktop_common import \
    BaseDesktopPage
from liveobs_ui.selectors.desktop.view_selectors import VIEW_MANAGER_WAIT


class WardBoardPage(BaseDesktopPage):
    """ Interaction patterns for wardboard page """

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

    def wait_for_data_refresh(self):
        """ Wait until the data on the page is refreshed (via JS timeout) """
        self.wait_for_element(VIEW_MANAGER_WAIT, wait_time=45)
