""" Step Implementations for user_permissions.feature """
from behave import given, when, then
from liveobs_ui.page_object_models.login_page import LoginPage
from liveobs_ui.page_object_models.list_page import ListPage


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
    context.username = login_details[0]
    login_page.login(*login_details)


@when("they view the task list")
def user_views_task_list(context):
    """
    Have the user navigate to the task list

    :param context: Behave context
    """
    task_list_page = ListPage(context.driver)
    task_list_page.go_to_task_list()


@then("they see a list of the tasks for the patients in the locations "
      "they are assigned to")
def list_of_tasks_for_patient_assigned_to(context):
    """
    Verify the patients in the task list are those the user is assigned to

    :param context: Behave context
    """
    task_list_page = ListPage(context.driver)
    patient_names = \
        context.helpers.get_patient_names_for_user(context.username)
    tasks = task_list_page.get_list_items()
    for task in tasks:
        patient_name = task_list_page.get_patient_from_item(task)
        assert (patient_name in patient_names), \
            "{} patient not in {}".format(patient_name, patient_names)


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
