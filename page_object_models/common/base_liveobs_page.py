""" Common interaction functions """
import time
import logging
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import ElementNotVisibleException
from liveobs_ui.selectors.desktop.form_selectors import \
    FORM_VIEW_AUTOCOMPLETE_CONTAINER


_LOGGER = logging.getLogger(__name__)


class BaseLiveObsPage(object):
    """ Base Page for all LiveObs Interaction """

    def __init__(self, driver):
        self.driver = driver
        self.default_wait = 20

    def wait_for_element(self, element_selector, hidden=False, wait_time=None):
        """
        Wrapper around WebDriverWait to wait for specified element to become
        visible

        :param element_selector: Element Selector tuple
        :type element_selector: tuple
        :param hidden: Check if element is hidden or not
        :type hidden: bool
        :param wait_time: Custom time to wait
        :type wait_time: int
        """
        condition = ec.visibility_of_element_located(element_selector)
        if hidden:
            condition = ec.invisibility_of_element_located(element_selector)
        if not wait_time:
            wait_time = self.default_wait
        ui.WebDriverWait(self.driver, wait_time).until(condition)

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


        :param data: list of dictionaries that contain field names, value to
            enter and field type
        """
        for field in data:
            value = field.get('value')
            name = field.get('name')
            data_type = field.get('type')
            field = self.driver.find_element_by_name(name)
            if data_type == 'select':
                self.fill_select_field(field, value)
            else:
                self.fill_input_field(field, value)

    @staticmethod
    def get_locator(element):
        """
        Get locator for element

        :param element: webelement we want to generate locator for
        :return: Locator for supplied element
        """
        return By.NAME, element.get_attribute('name')

    def fill_select_field(self, element, value):
        """
        Select an option in a select field

        :param element: Select we want to sort out's webelement
        :param value: Value to select in the select field
        """
        select_select = Select(element)
        select_select.select_by_visible_text(value)
        element.send_keys(Keys.TAB)
        ui.WebDriverWait(self.driver, self.default_wait).until(
            ec.text_to_be_present_in_element(self.get_locator(element), value)
        )

    def fill_input_field(self, element, value):
        """
        Enter a value into an input field

        :param element: webelement we want to add value to
        :param value: Value to enter into input
        """
        self.enter_input_value(element, value)
        ui.WebDriverWait(self.driver, self.default_wait).until(
            ec.text_to_be_present_in_element_value(
                self.get_locator(element), value))

    def enter_input_value(
            self, element, value, autocompleted=False, dropdown=False):
        """
        Enter a value into an input field

        :param element: webelement we want to add value to
        :param value: Value we want to add
        :param autocompleted: If should wait for autocomplete box to show
            before continuing
        :param dropdown: If should wait for the different type of dropdown to
            show before continuing
        """
        element.send_keys(value)
        if autocompleted:
            self.wait_for_element(FORM_VIEW_AUTOCOMPLETE_CONTAINER)
        if dropdown:
            # Commented out as it's unreliable to wait for the text drop down
            # to popup
            # self.wait_for_element(FORM_VIEW_AUTOCOMPLETE_TEXTDOWN)
            time.sleep(1)
        element.send_keys(Keys.TAB)

    def enter_many2one_tag_value(self, element, value):
        """
        Add value to many2one tag input then verify that the tag has been added

        :param element: many2one tag input element
        :param value: value to add to the many2one input
        """
        self.enter_input_value(element, value, dropdown=True)
        ui.WebDriverWait(self.driver, self.default_wait).until(
            ec.visibility_of_element_located(
                (
                    By.XPATH,
                    '//div[@class="oe_form_field oe_tags"]/div/div/div/'
                    'div[@class=\'text-tag\']/div/span[contains(text(), '
                    '"{}")]'.format(value)
                )
            )
        )

    @staticmethod
    def element_is_displayed(element_object):
        """
        Verify that an element is visible on the page

        :param element_object: the object or element to verify
        :return: either True/False for the element being displayed
        """
        try:
            return element_object.is_displayed()
        except ElementNotVisibleException as error:
            _LOGGER.info(error)
            return False

    @staticmethod
    def element_is_not_displayed(element_object):
        """
        Verify that an element is not visible on the page

        :param element_object: the object or element to verify
        :return: either True/False for the element not being displayed
        """
        try:
            return element_object.is_not_displayed()
        except Exception as error:  # pylint: disable=broad-except
            _LOGGER.info(error)
