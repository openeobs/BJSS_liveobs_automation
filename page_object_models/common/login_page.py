"""
Page Object Model for Login Page
The login page handles logging into the application
"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

from liveobs_ui.page_object_models.common.base_liveobs_page import \
    BaseLiveObsPage
from liveobs_ui.selectors.mobile.login_page_selectors import USERNAME_FIELD, \
    PASSWORD_FIELD, SUBMIT_BUTTON, DATABASE_DROPDOWN, LOGIN_ERROR_ALERT, \
    LOGIN_FIELD


class LoginPage(BaseLiveObsPage):
    """
    Class that handles interaction with the Login Page
    """

    def login(self, username, password, database='nhclinical', desktop=False):
        """
        Fill out the login form and press the submit button

        :param username: Username to login with
        :param password: Password for the username supplied
        :param database: Name of the database to log into if the
            database selection element is visible
        :param desktop: If the login is via desktop (as different field name)
        """
        if desktop:
            username_el = self.driver.find_element(*LOGIN_FIELD)
        else:
            username_el = self.driver.find_element(*USERNAME_FIELD)
        password_el = self.driver.find_element(*PASSWORD_FIELD)
        login_button = self.driver.find_element(*SUBMIT_BUTTON)
        try:
            database_selector = self.driver.find_element(
                *DATABASE_DROPDOWN
            )
            if database_selector.is_displayed():
                Select(database_selector).select_by_value(database)
        except NoSuchElementException:
            pass

        username_el.send_keys(username)
        password_el.send_keys(password)
        self.click_and_verify_change(login_button, PASSWORD_FIELD, hidden=True)

    def is_login_page(self):
        """
        Verify that we are indeed on the login page

        :return: if current page is the login page
        """
        return '/login' in self.driver.current_url

    def get_login_error_message(self):
        """
        Get error message shown after an unsuccessful login

        :return: Error message if present
        :rtype: str or None
        """
        try:
            error_message = self.driver.find_element(*LOGIN_ERROR_ALERT)
            return error_message.text
        except NoSuchElementException:
            return None
