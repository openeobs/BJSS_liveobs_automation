""" Patient Record Page Object Model """
from selenium.common.exceptions import NoSuchElementException

from liveobs_ui.page_object_models.desktop.form_view_common import \
    BaseFormViewPage
from liveobs_ui.selectors.desktop.view_selectors import VIEW_MANAGER_WAIT
from liveobs_ui.selectors.desktop.set_therapeutic_level_selectors \
    import THERAPEUTIC_LEVEL_FIELD_OPTIONS


class PatientRecordPage(BaseFormViewPage):
    """ Interaction with the patient record """

    def go_to_previous_spell(self):
        """ Go to the patient's previous clinical spell """
        button = self.get_actionbar_button_by_name('Previous Admission')
        self.click_and_verify_change(button, VIEW_MANAGER_WAIT)

    def open_wizard_with_name(self, button_name):
        """
        Open wizard via button name

        :param button_name: Name of button to press
        """
        button = self.get_actionbar_button_by_name(button_name)
        if not button:
            raise NoSuchElementException(
                "Could not find button with name '{}'".format(button_name))
        self.click_and_verify_change(button, THERAPEUTIC_LEVEL_FIELD_OPTIONS)

    def open_move_patient_wizard(self):
        """ Open the Move Patient wizard """
        self.open_wizard_with_name('Move Patient')

    def open_swap_bed_wizard(self):
        """ Open the Swap Bed wizard """
        self.open_wizard_with_name('Swap Beds')

    def open_print_report_wizard(self):
        """ Open the Print Report wizard """
        self.open_wizard_with_name('Print Report')

    def open_stop_observations_wizard(self):
        """ Open the Stop Observations wizard """
        self.open_wizard_with_name('Stop Observations')

    def open_set_therapeutic_obs_level_wizard(self):
        """ Open the Set Therapeutic Obs Level wizard """
        self.open_wizard_with_name('Set Therapeutic Obs Level')
