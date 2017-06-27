""" Interaction with the Allocation Wizard """
from selenium.webdriver.common.keys import Keys
from liveobs_ui.page_object_models.desktop.modal_view_common import \
    BaseModalPage
from liveobs_ui.selectors.desktop.allocation_wizard_selectors import \
    ALLOCATION_WIZARD, ALLOCATION_NURSE_INPUT, ALLOCATION_HCA_INPUT, \
    ALLOCATION_SAVE_BUTTON


class AllocationWizard(BaseModalPage):
    """
    Interacting with the Allocation Wizard. The Allocation Wizard is presented
    to the user at the 4th stage of the Nursing Shift Change Wizard and the
    2nd stage of the Staff Re-allocation Wizard.
    """

    def get_currently_open_modal(self):
        """ Get the currently open Allocation Modal """
        return self.driver.find_element(*ALLOCATION_WIZARD)

    def set_nurse(self, nurse_name):
        """
        Enter the nurse for the allocation into the nurse input box

        :param nurse_name: Name of the nurse we want to add to the allocation
        """
        allocation_modal = self.get_currently_open_modal()
        nurse_input = allocation_modal.find_element(*ALLOCATION_NURSE_INPUT)
        self.enter_input_value(nurse_input, nurse_name, autocompleted=True)
        # Need to press tab again so the value actually get put into the field
        # in Odoo desktop as one tab just doesn't cut it
        nurse_input.send_keys(Keys.TAB)

    def set_hcas(self, hca_list):
        """
        Enter the HCAs for the allocation into the HCAs input box

        :param hca_list: List of HCA user names we want to add to the
            allocation
        """
        allocation_modal = self.get_currently_open_modal()
        hca_input = allocation_modal.find_element(*ALLOCATION_HCA_INPUT)
        for hca in hca_list:
            self.enter_many2one_tag_value(hca_input, hca)

    def save_wizard(self):
        """ Save the allocation in the wizard """
        allocation_modal = self.get_currently_open_modal()
        save_button = allocation_modal.find_element(*ALLOCATION_SAVE_BUTTON)
        self.click_and_verify_change(
            save_button, ALLOCATION_WIZARD, hidden=True)

    def set_allocation(self, nurse, hca_list):
        """
        Set the allocation for the wizard

        :param nurse: Nurse to set for the allocation
        :param hca_list: List of HCAs to set for the allocation
        """
        self.set_nurse(nurse)
        self.set_hcas(hca_list)
        self.save_wizard()
