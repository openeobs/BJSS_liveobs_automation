"""
Common Functionality for Mobile
This class contains common functionality for the mobile frontend such as:
- navigating to a particular URL
"""
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from liveobs_ui.selectors.menu_selectors import TASK_ITEM, PATIENT_ITEM, \
    LOGOUT_BUTTON
from liveobs_ui.selectors.list import LIST_CONTAINER


class BaseMobilePage(object):
    """
        Base class to initialise the base page
        that will be called from all pages
    """
    def __init__(self, driver):
        self.driver = driver
        self.default_wait = 20

    def go_to_task_list(self):
        """
            Navigate to the task list
        """
        task_list_item = self.driver.find_element(*TASK_ITEM)
        self.click_and_verify_change(task_list_item, LIST_CONTAINER)

    def go_to_patient_list(self):
        """
            Navigate to the patient list
        """
        patient_list_item = \
            self.driver.find_element(*PATIENT_ITEM)
        self.click_and_verify_change(patient_list_item, LIST_CONTAINER)

    def logout(self):
        """
            Log out of the app
        """
        logout = self.driver.find_element(*LOGOUT_BUTTON)
        logout.click()

    def wait_for_element(self, element_selector, hidden=False):
        """
        Wrapper around WebDriverWait to wait for specified element to become
        visible

        :param element_selector: Element Selector tuple
        :type element_selector: tuple
        :param hidden: Check if element is hidden or not
        :type hidden: bool
        """
        condition = ec.visibility_of_element_located(element_selector)
        if hidden:
            condition = ec.invisibility_of_element_located(element_selector)
        ui.WebDriverWait(self.driver, self.default_wait).until(condition)

    def click_and_verify_change(self, el_to_click, el_to_verify, hidden=False):
        """
        Wrapper around clicking an element and then waiting for a change in the
        page and verifying said change by ensuring an element is visible

        :param el_to_click: Element to click to induce change
        :param el_to_verify: Element to look for to verify change
        :param hidden: Should check for if element is now hidden or not
        """
        el_to_click.click()
        self.wait_for_element(el_to_verify, hidden=hidden)
