"""
Page Object Model for Data Entry Page
The Data Entry Page allows the user to submit observations and escalation tasks
"""
from liveobs_ui.selectors.mobile.data_entry_selectors import \
    PATIENT_INFO_POPUP, FULL_SCREEN_PATIENT_INFO_BUTTON, \
    PATIENT_INFO_POPUP_CLOSE_BUTTON
from liveobs_ui.selectors.mobile.modal import \
    FULLSCREEN_MODAL, FULLSCREEN_MODAL_BUTTON, MODAL_DIALOG
from liveobs_ui.selectors.mobile.get_selector_by_something import \
    get_element_selector

from liveobs_ui.page_object_models.mobile.mobile_common import BaseMobilePage
from liveobs_ui.page_object_models.mobile.modal_page import ModalPage
from liveobs_ui.selectors.mobile.form import PATIENT_INFO_BUTTON, \
    FORM_CANCEL_BUTTON, FORM_SUBMIT_BUTTON, FORM


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

    @staticmethod
    def locate_attribute_path(field_input):
        """
        Identify the class of the input field and return the specific locator
        for their attributes

        :param field_input: the general locator for the field
        :return: locator for the attribute in the DOM
        """
        attribute = field_input.get_attribute("class")
        if attribute == "block obsField":
            return field_input.find_element_by_xpath(
                "div[@class='input-header']/input")
        elif attribute == "block obsSelectField":
            return field_input.find_element_by_xpath(
                "div[@class='input-body']/select")
        else:
            raise ValueError(" {} element doesn't belong to specified classes"
                             .format(field_input))

    def verify_obs_form_displayed(self, obs_type):
        """
        Finds the data-type attribute for the currently open observation form
        and compares the result to the expected data-type as per the obs_type
        selected

        :param obs_type: the observation selected
        """
        obs_form = self.driver.find_element_by_id('obsForm')
        self.element_is_displayed(obs_form)
        return self.get_data_model_from_form() == \
            get_element_selector(obs_type)

    def verify_obs_field_displayed(self, obs_field):
        """
        Locates a specific field in an observation form and verifies its
        visibility

        :param obs_field: the observation field to look for
        """
        field_selector = get_element_selector(obs_field)
        obs_fields = self.driver.find_element(*field_selector)
        return self.element_is_displayed(obs_fields)

    def verify_obs_field_not_displayed(self, obs_field):
        """
        Locate a specific field in an observation form and verifies it is not
        visible

        :param obs_field: the observation field to look for
        """
        field_selector = get_element_selector(obs_field)
        obs_fields = self.driver.find_element(*field_selector)
        return self.element_is_not_displayed(obs_fields)
