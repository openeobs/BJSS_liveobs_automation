""" Page Object Model for interacting with Patients By Ward Page """
from liveobs_ui.page_object_models.desktop.list_view_common import \
    BaseListViewPage
from liveobs_ui.selectors.desktop.list_selectors import \
    PATIENTS_WITHOUT_BED_PLACEMENT_BUTTON
from liveobs_ui.selectors.desktop.modal_selectors import MODAL_CONTAINER


class PatientsWithoutBedPage(BaseListViewPage):
    """ Interaction with Patients Without Bed Page """

    def open_bed_placement_popup(self, patient_name):
        """
        Find the row in the list for the supplied patient then open the
        bed placement popup

        :param patient_name: Name of patient who we want to place in bed
        """
        list_row = self.get_list_item_by_name(patient_name)
        placement_button = \
            list_row.find_element(*PATIENTS_WITHOUT_BED_PLACEMENT_BUTTON)
        self.click_and_verify_change(placement_button, MODAL_CONTAINER)
