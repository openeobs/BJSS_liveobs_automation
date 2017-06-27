""" Step Implementations for common actions in the mobile application """
from behave import given, when, then
from liveobs_ui.page_object_models.list_page import ListPage
import random
from time import sleep
from lookups.mobile_lookups import *
from liveobs_ui.page_object_models.mobile_common import BaseMobilePage


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
    elif page_select == 'Tasks':
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

    :param context: Behave context
    :param button_name:  name of the button to be pressed
    :return:
    """
    button_selector = buttons_locators_dict[button_name]
    button_element = context.driver.find_element(*button_selector)
    button_element.click()


@when('a random patient is selected')
def select_a_patient_in_list(context):
    """

    :param context: Behave context
    :return: selects a random patient card from the Patient list in the mobile app
    """
    press_it = ListPage(context.driver)
    patients = press_it.get_list_items()
    patient = random.choice(patients)
    press_it.open_item(patient)


@when('the {observation_type} observation is selected from the list')
def select_take_specific_obs_from_list(context, observation_type):
    """
    Find and selects a specific observation from the Observation list
    :param context: Behave context
    :param observation_type: name of the observation to be selected
    :return: selects the specified observation from the list to open the observation form
    """
    obs_element = context.driver.find_element_by_partial_link_text(observation_type)
    obs_element.click()


@then('the {observation_type} observation form is displayed')
def verify_obs_form_is_displayed(context, observation_type):
    """
    Verify the specified observation form is displayed
    :param context:
    :param observation_type:
    :return:
    """
    obs_form = context.driver.find_element_by_id('obsForm')
    form_check = BaseMobilePage(context.driver)
    form_check.element_is_displayed(obs_form)


@then('the {observation_field} field is displayed')
def verify_obs_field_is_displayed(context, observation_field):
    """
    Verify the specified field is displayed in the form
    :param context:
    :param observation_field:
    :return:
    """
    field_selector = obs_data_field_locators_dict[observation_field]
    obs_field = context.driver.find_element(*field_selector)
    field_check = BaseMobilePage(context.driver)
    field_check.element_is_displayed(obs_field)


@then('the {observation_field} field is not displayed')
def verify_obs_field_is_not_displayed(context, observation_field):
    """
    Verify the specified field is displayed in the form
    :param context:
    :param observation_field:
    :return:
    """
    field_selector = obs_data_field_locators_dict[observation_field]
    obs_field = context.driver.find_element(*field_selector)
    field_check = BaseMobilePage(context.driver)
    field_check.element_is_not_displayed(obs_field)
