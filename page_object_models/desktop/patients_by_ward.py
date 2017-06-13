""" Page Object Model for interacting with Patients By Ward Page """
from liveobs_ui.page_object_models.desktop.desktop_common import \
    BaseDesktopPage
from liveobs_ui.selectors.desktop.list_selectors import \
    PATIENTS_BY_WARD_CHART_BUTTON, PATIENTS_BY_WARD_LIST_BUTTON, LIST_VIEW_ROW
from liveobs_ui.selectors.desktop.modal_selectors import MODAL_CONTAINER
from liveobs_ui.selectors.desktop.view_selectors import VIEW_MANAGER_FORM


class PatientsByWardPage(BaseDesktopPage):
    """ Interaction with Patients By Ward Page """

    def get_patient_list_items(self):
        """
        Get a list of patients in the Patients By Ward list

        :return: list of patients
        """
        return self.driver.find_elements(*LIST_VIEW_ROW)

    def get_patient_list_item_by_name(self, patient_name):
        """
        Get a specific list item for the supplied name

        :param patient_name: Name of the patient to find
        :return: element for patient
        """
        list_items = self.get_patient_list_items()
        for list_item in list_items:
            if patient_name in list_item.text:
                return list_item

    def open_patient_chart_popup(self, patient_name):
        """
        Find the row in the list for the supplied patient then open the chart
        popup

        :param patient_name: Name of patient who's chart we want to open
        """
        list_row = self.get_patient_list_item_by_name(patient_name)
        chart_button = list_row.find_element(*PATIENTS_BY_WARD_CHART_BUTTON)
        self.click_and_verify_change(chart_button, MODAL_CONTAINER)

    def open_patient_list_popup(self, patient_name):
        """
        Find the row in the list for the supplied patient then open the list
        popup

        :param patient_name: Name of the patient who's list we want to open
        """
        list_row = self.get_patient_list_item_by_name(patient_name)
        list_button = list_row.find_element(*PATIENTS_BY_WARD_LIST_BUTTON)
        self.click_and_verify_change(list_button, MODAL_CONTAINER)

    def open_patient_record(self, patient_name):
        """
        Find the row in the list for the supplied patient then open the
        patient record

        :param patient_name: Name of the patient who'd record we want to open
        """
        list_row = self.get_patient_list_item_by_name(patient_name)
        self.click_and_verify_change(list_row, VIEW_MANAGER_FORM)
