""" Interaction with the Nursing Shift Change Wizard """
from liveobs_ui.page_object_models.desktop.modal_view_common import \
    BaseModalPage
from liveobs_ui.page_object_models.desktop.allocation_wizard import \
    AllocationWizard
from liveobs_ui.selectors.desktop.nursing_shift_change_selectors import \
    WIZARD_VISIBLE_BUTTON, MODAL_TABLE_ROW, \
    DEALLOCATION_TABLE_BED_COL, DEALLOCATION_TABLE_NURSE_COL,\
    DEALLOCATION_TABLE_HCA_COL, ALLOCATE_WIZARD_BUTTON, \
    ALLOCATE_TABLE_BED_COL, WIZARD_STAGE_CONTAINER, WIZARD_DEALLOCATE_BUTTON, \
    WIZARD_ROLL_CALL_BUTTON, WIZARD_ALLOCATION_BUTTON
from liveobs_ui.selectors.desktop.allocation_wizard_selectors import \
    ALLOCATION_WIZARD_TITLE
from liveobs_ui.selectors.desktop.view_selectors import VIEW_MANAGER_WAIT
from liveobs_ui.selectors.desktop.form_selectors import FORM_MANY2ONE_INPUT, \
    FORM_MANY2ONE_TEXTAREA


class NursingShiftChangeWizard(BaseModalPage):
    """
    Interacting with the Nursing Shift Change Wizard and it's different
    stages
    """

    def start_nursing_shift_change(self):
        """
        Click the Nursing Shift Change menu item to start the wizard
        """
        self.go_to_page('Nursing Shift Change')
        self.wait_for_element(WIZARD_STAGE_CONTAINER)

    def get_confirm_button(self):
        """
        Get the button to take the user to next stage of the wizard

        :return: webelement for button
        """
        return self.driver.find_element(*WIZARD_VISIBLE_BUTTON)

    def confirm_stage(self):
        """
        Confirm the data in the current stage and move to the next one
        """
        confirm_button = self.get_confirm_button()
        self.click_and_verify_change(confirm_button, VIEW_MANAGER_WAIT)

    def go_to_deallocate_stage(self):
        """ Go to the deallocation stage """
        self.confirm_stage()
        self.wait_for_element(WIZARD_DEALLOCATE_BUTTON)

    def go_to_roll_call(self):
        """ Go to the roll call stage """
        self.confirm_stage()
        self.wait_for_element(WIZARD_ROLL_CALL_BUTTON, wait_time=120)

    def go_to_allocation(self):
        """ Go to the allocation stage """
        self.confirm_stage()
        self.wait_for_element(WIZARD_ALLOCATION_BUTTON)

    def go_to_end(self):
        """ Go to the end of the wizard """
        self.confirm_stage()
        self.wait_for_element(WIZARD_STAGE_CONTAINER, hidden=True)

    def set_ward_for_shift_change(self, ward_name):
        """
        Set ward in ward selection box in Nursing Shift Change Wizard

        :param ward_name: Name of the ward to set
        """
        modal = self.get_currently_open_modal()
        ward_select = modal.find_element(*FORM_MANY2ONE_INPUT)
        self.enter_input_value(ward_select, ward_name, autocompleted=True)

    def select_ward(self, ward_name):
        """
        Get currently logged in user's ward and select it in dropdown

        :param ward_name: Name of ward to select for Nursing Shift change
        """
        self.set_ward_for_shift_change(ward_name)

    def collect_current_allocation(self):
        """
        Get the current user(s) -> bed allocation from the de-allocation screen

        :return: list of dictionaries representing beds and the different nurse
            and HCA users allocated to that bed
        """
        self.wait_for_element(MODAL_TABLE_ROW)
        self.wait_for_element(VIEW_MANAGER_WAIT, hidden=True)
        table_rows = self.driver.find_elements(*MODAL_TABLE_ROW)
        user_map = {}
        for table_row in table_rows:
            bed = table_row.find_element(*DEALLOCATION_TABLE_BED_COL).text
            nurse = table_row.find_element(*DEALLOCATION_TABLE_NURSE_COL).text
            hcas = table_row.find_element(*DEALLOCATION_TABLE_HCA_COL).text
            user_map[bed] = {
                'nurse': nurse,
                'hcas': hcas.split(',')
            }
        return user_map

    def roll_call(self, user_list):
        """
        Add all users that were originally on ward back into ward

        :param user_list: list of names to enter into input so these users can
             then be allocated to the beds in the ward
        """
        modal = self.get_currently_open_modal()
        user_select = modal.find_element(*FORM_MANY2ONE_TEXTAREA)
        for user in user_list:
            self.enter_many2one_tag_value(user_select, user)
        self.confirm_stage()

    def allocate(self, allocation_map):
        """
        Allocate users to beds

        :param allocation_map: dictionary containing mapping of users to beds
        """
        self.wait_for_element(MODAL_TABLE_ROW)
        self.wait_for_element(VIEW_MANAGER_WAIT, hidden=True)
        table_rows = self.driver.find_elements(*MODAL_TABLE_ROW)
        for row_number in range(0, len(table_rows)):
            self.wait_for_element(MODAL_TABLE_ROW)
            self.wait_for_element(VIEW_MANAGER_WAIT, hidden=True)
            table_row = self.driver.find_elements(*MODAL_TABLE_ROW)[row_number]
            allocate_button = table_row.find_element(*ALLOCATE_WIZARD_BUTTON)
            bed_name = table_row.find_element(*ALLOCATE_TABLE_BED_COL).text
            allocation = allocation_map.get(bed_name)
            if allocation:
                self.click_and_verify_change(
                    allocate_button, ALLOCATION_WIZARD_TITLE)
                allocation_wizard = AllocationWizard(self.driver)
                allocation_wizard.set_allocation(
                    allocation.get('nurse'), allocation.get('hcas'))
