""" Step Implementations for common actions in the mobile application """
from behave import given, when, then
from liveobs_ui.page_object_models.list_page import ListPage
from liveobs_ui.page_object_models.mobile_common import BaseMobilePage
import random


@given("they view the {page_select} list")
@when("they view the {page_select} list")
def user_views_task_list(context, page_select):
    """
    Have the user navigate to the task list

    :param page_select: name of the page to navigate to
    :param context: Behave context
    """
    if page_select == 'My Patients':
        patient_list = ListPage(context.driver)
        patient_list.go_to_patient_list()
    if page_select == 'Tasks':
        task_list_page = ListPage(context.driver)
        task_list_page.go_to_task_list()


@given("the {page_name} list has loaded")
@when("the {page_name} list has loaded")
def test_check(context, page_name):
    """
    Verify the correct mobile list/page has loaded

    :param context: Behave context
    :param page_name: name of the page expected, passed to verify correct URL
    """
    if page_name == 'My Patients':
        patient_list = ListPage(context.driver)
        assert patient_list.is_patient_list(), 'Expected to be in {} but it is not'.format(page_name)
    elif page_name == 'Tasks':
        task_list = ListPage(context.driver)
        assert task_list.is_task_list(), 'Expected to be in {} but it is not'.format(page_name)


@when('the {button_name} button is selected')
def press_button(context, button_name):
    """

    :param context:
    :param button_name:  name of the button to be pressed
    :return:
    """
    button = BaseMobilePage(context.driver)
    button.click_button_with_name(button_name)


@when('a random patient is selected')
def select_a_patient_in_list(context):
    """

    :param context:
    :return:
    """
    press_it = ListPage(context.driver)
    patients = press_it.get_list_items()
    patient = random.choice(patients)
    press_it.open_item(patient)

