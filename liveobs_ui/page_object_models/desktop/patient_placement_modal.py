""" Patient Placement Modal Interaction """
from liveobs_ui.page_object_models.desktop.modal_view_common import \
    BaseModalPage
from liveobs_ui.selectors.desktop.modal_selectors import MODAL_CONTAINER
from liveobs_ui.selectors.desktop.form_selectors import \
    FORM_MANY2ONE_DROPDOWN, FORM_VIEW_AUTOCOMPLETE_CONTAINER, \
    FORM_VIEW_AUTOCOMPLETE_ITEM, FORM_VIEW_BUTTON


class PatientPlacementModalPage(BaseModalPage):
    """ Interaction with the Patient Placement modal """

    def get_available_beds(self):
        """ Get list of beds available for placement """
        modal = self.driver.find_element(*MODAL_CONTAINER)
        autocomplete_dropdown = modal.find_element(*FORM_MANY2ONE_DROPDOWN)
        self.click_and_verify_change(
            autocomplete_dropdown, FORM_VIEW_AUTOCOMPLETE_CONTAINER)
        autocomplete_list = \
            modal.find_element(*FORM_VIEW_AUTOCOMPLETE_CONTAINER)
        return autocomplete_list.find_elements(
            *FORM_VIEW_AUTOCOMPLETE_ITEM)

    def select_bed_for_patient(self, bed):
        """
        Place the current open patient in a random bed

        :param bed: webelement for bed we want to place patient in
        """
        self.click_and_verify_change(
            bed, FORM_VIEW_AUTOCOMPLETE_CONTAINER, hidden=True)

    def submit_placement(self):
        """ Submit patient placement """
        modal = self.driver.find_element(*MODAL_CONTAINER)
        confirm_button = modal.find_element(*FORM_VIEW_BUTTON)
        self.click_and_verify_change(
            confirm_button, MODAL_CONTAINER, hidden=True)
