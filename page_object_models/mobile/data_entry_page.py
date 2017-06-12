"""
Page Object Model for Data Entry Page
The Data Entry Page allows the user to submit observations and escalation tasks
"""
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from liveobs_ui.page_object_models.mobile.mobile_common import BaseMobilePage
from liveobs_ui.page_object_models.mobile.modal_page import ModalPage
from liveobs_ui.selectors.data_entry_selectors import PATIENT_INFO_POPUP, \
    FULL_SCREEN_PATIENT_INFO_BUTTON, PATIENT_INFO_POPUP_CLOSE_BUTTON
from liveobs_ui.selectors.form import PATIENT_INFO_BUTTON, \
    FORM_CANCEL_BUTTON, FORM_SUBMIT_BUTTON, FORM
from liveobs_ui.selectors.modal import \
    FULLSCREEN_MODAL, FULLSCREEN_MODAL_BUTTON, MODAL_DIALOG


class DataEntryPage(BaseMobilePage):
    """
    Class that handles interacting with the data entry form
    """

    def get_data_model_from_form(self):
        """
        Get the dataa model for the form so we can use this to determine what
        to do
        """
        form = self.driver.find_element(*FORM)
        return form.get_attribute('data-type')

    def open_patient_info(self):
        """
        Open the patient information popup in the floating header
        """
        patient_info_button = self.driver.find_element(*PATIENT_INFO_BUTTON)
        self.click_and_verify_change(patient_info_button, PATIENT_INFO_POPUP)

    def close_patient_info(self):
        """
        Close the patient information popup, opened by pressing the button in
        the floating header
        """
        close_button = \
            self.driver.find_element(*PATIENT_INFO_POPUP_CLOSE_BUTTON)
        self.click_and_verify_change(
            close_button, PATIENT_INFO_POPUP, hidden=True)

    def open_full_patient_info(self):
        """
        Open the full screen patient information popup
        """
        full_info_button = \
            self.driver.find_element(*FULL_SCREEN_PATIENT_INFO_BUTTON)
        self.click_and_verify_change(full_info_button, FULLSCREEN_MODAL)

    def close_full_patient_info(self):
        """
        Close the full screen patient information popup
        """
        full_close_button = self.driver.find_element(*FULLSCREEN_MODAL_BUTTON)
        self.click_and_verify_change(
            full_close_button, FULLSCREEN_MODAL, hidden=True)

    def submit_form(self):
        """
        Press the submit button on the form
        """
        form_submit_button = self.driver.find_element(*FORM_SUBMIT_BUTTON)
        self.click_and_verify_change(form_submit_button, MODAL_DIALOG)

    def cancel_form(self):
        """
        Press the cancel button on the form (if present)
        """
        form_cancel_button = self.driver.find_element(*FORM_CANCEL_BUTTON)
        self.click_and_verify_change(form_cancel_button, MODAL_DIALOG)

    def fill_out_form(self, data):
        """
        Using the provided list fill out the form

        Expected Data Format:

        .. code-block:: python

            {
                'name': 'respiration_rate',
                'value': '18',
                'type': 'textbox'
            }


        :data: list of dictionaries that contain field names, value to enter
            and field type
        """
        for field in data:
            value = field.get('value')
            name = field.get('name')
            data_type = field.get('type')
            field_locator = (By.NAME, name)

            if data_type == 'select':
                select_field = self.driver.find_element_by_name(name)
                select_select = Select(select_field)
                select_select.select_by_visible_text(value)
                select_field.send_keys(Keys.TAB)
                ui.WebDriverWait(self.driver, self.default_wait).until(
                    ec.text_to_be_present_in_element(field_locator, value)
                )
            else:
                input_field = self.driver.find_element_by_name(name)
                input_field.send_keys(value)
                input_field.send_keys(Keys.TAB)
                ui.WebDriverWait(self.driver, self.default_wait).until(
                    ec.text_to_be_present_in_element_value(
                        field_locator, value)
                )

    def confirm_submit_scored_ob(self):
        """
        Confirm the 'Submit Score of X for Y, Z' modal that pops up after
        first pressing the submit button for scored observations.
        """
        modal_page = ModalPage(self.driver)
        modals = modal_page.get_open_modals()
        scored_modal = modals[0]
        modal_page.click_modal_option(scored_modal, 'Submit')

    def take_escalation_task(self):
        """
        Take the escalation task presented to the user once an observation that
        has escalation tasks is submitted
        """
        modal_page = ModalPage(self.driver)
        modals = modal_page.get_open_modals()
        escalation_modal = modals[0]
        escalation_modal_options = \
            modal_page.get_modal_options(escalation_modal)
        if len(escalation_modal_options) > 1:
            modal_page.click_modal_option(escalation_modal, 'Confirm')
        else:
            modal_page.click_modal_option(escalation_modal, 'Go to My Tasks')

    def submit_cancellation_reason(self, cancel_reason):
        """
        Select the specified cancellation reason and submit the modal to
        cancel the task

        :param cancel_reason: Name of reason to select
        """
        modal_page = ModalPage(self.driver)
        modals = modal_page.get_open_modals()
        cancel_modal = modals[0]
        modal_page.select_reason_in_modal(cancel_modal, cancel_reason)
        modal_page.click_modal_option(cancel_modal, 'Submit')
