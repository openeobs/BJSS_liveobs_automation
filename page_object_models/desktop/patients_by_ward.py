""" Page Object Model for interacting with Patients By Ward Page """
from liveobs_ui.page_object_models.desktop.list_view_common import \
    BaseListViewPage
from liveobs_ui.selectors.desktop.list_selectors import \
    PATIENTS_BY_WARD_CHART_BUTTON, PATIENTS_BY_WARD_LIST_BUTTON, \
    GROUPED_LIST_VIEW_ROW
from liveobs_ui.page_object_models.desktop.wardboard_common import \
    WardBoardPage
from liveobs_ui.selectors.desktop.modal_selectors import MODAL_CONTAINER


class PatientsByWardPage(BaseListViewPage, WardBoardPage):
    """ Interaction with Patients By Ward Page """

    def go_to_patients_by_ward(self):
        """ Navigate the user to the Patients By Ward page """
        self.go_to_page('Patients by Ward')

    def open_patient_chart_popup(self, patient_name):
        """
        Find the row in the list for the supplied patient then open the chart
        popup

        :param patient_name: Name of patient who's chart we want to open
        """
        list_row = self.get_list_item_by_name(patient_name)
        chart_button = list_row.find_element(*PATIENTS_BY_WARD_CHART_BUTTON)
        self.click_and_verify_change(chart_button, MODAL_CONTAINER)

    def open_patient_list_popup(self, patient_name):
        """
        Find the row in the list for the supplied patient then open the list
        popup

        :param patient_name: Name of the patient who's list we want to open
        """
        list_row = self.get_list_item_by_name(patient_name)
        list_button = list_row.find_element(*PATIENTS_BY_WARD_LIST_BUTTON)
        self.click_and_verify_change(list_button, MODAL_CONTAINER)

    def wait_for_list_view_to_load(self):
        """
        Override of the function that waits for the list view to load
        to take into consideration the fact that Patients By Ward is a grouped
        list view
        """
        self.wait_for_element(GROUPED_LIST_VIEW_ROW)

    def wait_for_data_refresh(self):
        """ Wait for the kanban data to refresh """
        super(PatientsByWardPage, self).wait_for_data_refresh()
        self.wait_for_list_view_to_load()
