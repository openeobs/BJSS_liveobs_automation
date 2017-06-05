"""
Page Object Model for Login Page
The login page handles logging into the application
"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from liveobs_ui.page_object_models.mobile_common import BaseMobilePage
from liveobs_ui.selectors.login_page_selectors import USERNAME_FIELD, \
    PASSWORD_FIELD, SUBMIT_BUTTON, DATABASE_DROPDOWN, LOGIN_ERROR_ALERT


class LoginPage(BaseMobilePage):
    """
    Class that handles interaction with the Login Page on Mobile
    """

    def login(self, username, password, database='nhclinical'):
        """
        Fill out the login form and press the submit button

        :param username: Username to login with
        :param password: Password for the username supplied
        :param database: Name of the database to log into if the
            database selection element is visible
        """
        username_e = self.driver.find_element(*USERNAME_FIELD)
        password_e = self.driver.find_element(*PASSWORD_FIELD)
        login_button = self.driver.find_element(*SUBMIT_BUTTON)
        try:
            database_selector = self.driver.find_element(
                *DATABASE_DROPDOWN
            )
            if database_selector.is_displayed():
                Select(database_selector).select_by_value(database)
        except NoSuchElementException:
            pass

        username_e.send_keys(username)
        password_e.send_keys(password)
        self.click_and_verify_change(login_button, USERNAME_FIELD, hidden=True)

    def is_login_page(self):
        """
        Verify that we are indeed on the login page

        :return: if current page is the login page
        """
        return '/mobile/login' in self.driver.current_url

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
