""" Step Implementations for user_permissions.feature """

# pylint: disable=invalid-name
# pylint: disable=no-name-in-module
# pylint: disable=unused-argument

from behave import given, then
from liveobs_ui.page_object_models.common.login_page import LoginPage
from liveobs_ui.page_object_models.desktop.desktop_common import \
    BaseDesktopPage
from liveobs_ui.page_object_models.mobile.list_page import ListPage
from liveobs_ui.page_object_models.common.background_setup import \
    get_user_credentials


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


# @then("they see a list of the tasks for the patients in the locations "t
#       "they are assigned to")
# def list_of_tasks_for_patient_assigned_to(context):
#     """
#     Verify the patients in the task list are those the user is assigned to
#
#     :param context: Behave context
#     """
#     task_list_page = ListPage(context.driver)
#     patient_names = \
#         context.helpers.get_patient_names_for_user(context.username)
#     tasks = task_list_page.get_list_items()
#     for task in tasks:
#         patient_name = task_list_page.get_patient_from_item(task)
#         assert (patient_name in patient_names), \
#             "{} patient not in {}".format(patient_name, patient_names)


@then("the list of tasks is filtered to show tasks for the {user_role} role")
def list_of_tasks_for_role_task_types(context, user_role):
    """
    Verify that the tasks in the task list are only those that can be carried
    out by the role the user is associated with

    :param context: Behave context
    :param user_role: Role the user is associated with
    """
    tasks_for_role = []
    for row in context.table:
        tasks_for_role.append(row.get('tasks'))
    task_list_page = ListPage(context.driver)
    tasks = task_list_page.get_list_items()
    for task in tasks:
        task_name = task_list_page.get_task_info_from_item(task)
        assert (task_name in tasks_for_role), \
            "{} task not in {}".format(task_name, tasks_for_role)


@given("the user {user_name} logs into the {app_view} app")
def user_logs_into_app(context, user_name, app_view):
    """
    Navigates to web/mobile login page and logs in as user saved in context.
    If no user is found, it raises an exception

    :param context: behave context
    :param user_name: the name of the user. Used to locate the user in context
    :param app_view: either mobile or desktop
    """
    login_page = LoginPage(context.driver)
    login_url = context.helpers.config.get('server') + \
        context.helpers.config.get('urls').get('{}_login'.format(app_view))
    login_page.driver.get(login_url)
    username = get_user_credentials(context.client, user_name)
    if username:
        is_desktop = app_view == 'desktop'
        login_page.login(username, username, desktop=is_desktop)
    else:
        raise ValueError('No user found')
    login_page.verify_page_loaded(app_view)


@then("the available menu items are filtered for the {user_role} role")
def verify_correct_desktop_menu_items_available(context, user_role):
    """
    Verify that the menu items available in the in the desktop menu are only
    those specified for the role the user is associated with

    :param context: Behave context
    :param user_role: Role assigned to the user
    """
    expected_pages = [row.get('page') for row in context.table]
    page_list = BaseDesktopPage(context.driver)
    pages = page_list.get_menu_items_list()
    for page in pages:
        actual_page = page_list.get_menu_item_text(page)
        assert (actual_page in expected_pages), \
            "'{}' page not in {}".format(actual_page, expected_pages)
