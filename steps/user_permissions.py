from behave import *
from liveobs_ui.page_object_models.login_page import LoginPage


@given("a user with the {user_role} role logs into the app")
def user_with_role_logins(context, user_role):
    """
    Find a user with the specified role and log them in
    
    :param context: Behave context
    :param user_role: Role the user we're logging in must have
    """
    login_page = LoginPage(context.driver)
    login_url = context.helpers.config.get('server') + \
                context.helpers.config.get('urls').get('login')
    login_page.driver.get(login_url)
    login_details = context.helpers.get_user_for_role(user_role)
    login_page.login(*login_details)
