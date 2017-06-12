"""
Page Object Model for Patient Page
The Patient Page shows the observation data for the patient as well as allows
them to conduct an ad-hoc observation
"""
from liveobs_ui.page_object_models.mobile.mobile_common import BaseMobilePage
from liveobs_ui.selectors.patient_page_selectors import \
    ADHOC_OBS_MENU_BUTTON, OPEN_OBS_MENU, OPEN_OBS_MENU_LIST_ITEMS, \
    OPEN_OBS_MENU_CLOSE_BUTTON


class PatientPage(BaseMobilePage):
    """
    Class that handles interacting with patient graphs and ad-hoc observation
    menu
    """

    def open_adhoc_menu(self):
        """
        Press the 'Take Observation' button to open the ad-hoc observation
        list
        """
        menu_button = self.driver.find_element(*ADHOC_OBS_MENU_BUTTON)
        self.click_and_verify_change(menu_button, OPEN_OBS_MENU)

    def get_observation_menu_items(self):
        """
        Get a list of the ad-hoc observations in the 'Take Observation' menu
        :return: list of WebElements
        """
        return self.driver.find_elements(*OPEN_OBS_MENU_LIST_ITEMS)

    def get_observation_in_menu(self, observation_name):
        """
        Select the specified observation from the ad-hoc observation menu

        :param observation_name: Name of the observation to select
        :type observation_name: str
        :return: WebElement for that observation
        """
        observations = self.get_observation_menu_items()
        observation = \
            [el for el in observations if observation_name in el.text]
        if observation:
            return observation[0]
        return None

    def open_observation_form(self, observation_name):
        """
        Open the ad-hoc observation menu, find the specified observation and
        open the observation form

        :param observation_name: Name of the observation to open
        """
        self.open_adhoc_menu()
        observation = self.get_observation_in_menu(observation_name)
        if observation:
            observation_url = observation.get_attribute('href')
            self.click_and_verify_change(
                observation, ADHOC_OBS_MENU_BUTTON, hidden=True)
            return observation_url in self.driver.current_url
        return False

    def close_adhoc_menu(self):
        """
        Close the ad-hoc observation menu
        """
        close_button = self.driver.find_element(*OPEN_OBS_MENU_CLOSE_BUTTON)
        self.click_and_verify_change(close_button, OPEN_OBS_MENU, hidden=True)
