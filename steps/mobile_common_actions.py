""" Step Implementations for common actions in the mobile application """

# pylint: disable=invalid-name
# pylint: disable=no-name-in-module

# from time import sleep
# from selenium import webdriver
from behave import given, when, then
from liveobs_ui.page_object_models.mobile.list_page import ListPage
from liveobs_ui.page_object_models.mobile.patient_page import PatientPage
from liveobs_ui.page_object_models.mobile.data_entry_page import DataEntryPage
from liveobs_ui.selectors.mobile.get_selector_by_something import \
    get_element_selector
from liveobs_ui.page_object_models.mobile.mobile_common import BaseMobilePage
from liveobs_ui.selectors.mobile.patient_page_selectors import \
    ADHOC_OBS_MENU_BUTTON


@given("they view the {page_select} list")
@when("they view the {page_select} list")
def user_views_task_list(context, page_select):
    """
    Have the user navigate to the task/my patient list page

    :param page_select: name of the page to navigate to
    :param context: Behave context
    """
    patient_list = ListPage(context.driver)
    if page_select == 'My Patients':
        patient_list.go_to_patient_list()
    elif page_select == 'Tasks':
        patient_list.go_to_task_list()


@given("the {page_name} list has loaded")
@when("the {page_name} list has loaded")
def test_check(context, page_name):
    """
    Verify the correct mobile list/page has loaded

    :param context: Behave context
    :param page_name: name of the page expected, passed to verify correct URL
    """
    loaded_page = ListPage(context.driver)
    if page_name == 'My Patients':
        assert loaded_page.is_patient_list(), \
            'Expected to be in {} but it is not'.format(page_name)
    elif page_name == 'Tasks':
        assert loaded_page.is_task_list(), \
            'Expected to be in {} but it is not'.format(page_name)


@when('the {button_name} button is selected')
def press_button_with_name(context, button_name):
    """
    Finds a button from it's name/parameter and clicks it

    :param context: Behave context
    :param button_name:  name of the button to be pressed
    :return: clicks the button
    """
    button_find = BaseMobilePage(context.driver)
    button = button_find.find_button_to_select(button_name)
    button.click()


@when('a random patient is selected')
def select_random_patient_in_list(context):
    """
    Finds and selects a random patient in the 'My Patients' page

    :param context: Behave context
    :return: selects a random patient card from the Patient list in the app
    """
    select_patient = ListPage(context.driver)
    select_patient.select_random_patient()


@when('the {observation_type} observation is selected from the list')
def select_take_specific_obs_from_list(context, observation_type):
    """
    Find and selects a specific observation from the Observation list

    :param context: Behave context
    :param observation_type: name of the observation to be selected
    :return: selects the specified observation from the list to open
        the observation form
    """
    patient_page = PatientPage(context.driver)
    # patient_page.open_observation_form(observation_type)
    obs_element = context.driver.find_element_by_partial_link_text(
        observation_type)
    patient_page.click_and_verify_change(obs_element, ADHOC_OBS_MENU_BUTTON,
                                         hidden=True)


@then('the {observation_type} observation form is displayed')
def verify_obs_form_is_displayed(context, observation_type):
    """
    Verify the specified observation form is displayed

    :param context: Behave context
    :param observation_type: name of the observation form to be checked
    """
    form_check = DataEntryPage(context.driver)
    assert form_check.verify_obs_form_displayed(observation_type), \
        "Expected Form for '{}' to be displayed but it isn't.".format(
            observation_type)


@then('the {observation_field} field is displayed')
def verify_obs_field_is_displayed(context, observation_field):
    """
    Verify the specified field is displayed in the form

    :param context: Behave context
    :param observation_field: name of the observation field to be checked
    """
    field_check = DataEntryPage(context.driver)
    assert field_check.verify_obs_field_displayed(observation_field), \
        "Expected field '{}' to be displayed but it isn't.".format(
            observation_field)


@then('the {observation_field} field is not displayed')
def verify_obs_field_is_not_displayed(context, observation_field):
    """
    Verify the specified field is not displayed in the form

    :param context: Behave context
    :param observation_field: name of the observation field to be checked
    """
    field_check = DataEntryPage(context.driver)
    assert field_check.verify_obs_field_not_displayed(observation_field), \
        "Expected field '{}' to not be displayed but it is.".format(
            observation_field)


@then('the {obs_data_entry_field} entry field is {state_set} to '
      '{expected_state_type}')
def verify_field_is_necessary(context, obs_data_entry_field,
                              state_set, expected_state_type):
    """
    Finds a specific input field and checks the correctness of its expected
    attribute state

    :param context: Behave context
    :param obs_data_entry_field: Name of the field to be checked
    :param state_set: specifies the true/false state to verify
    :param expected_state_type: Either 'Mandatory' or 'Necessary'
    """
    field_selector = get_element_selector(
        obs_data_entry_field)
    field_input = context.driver.find_element(*field_selector)
    stuff = DataEntryPage(context.driver)
    attribute_type_path = stuff.locate_attribute_path(field_input)
    if expected_state_type == 'Mandatory':
        if state_set == 'set':
            assert attribute_type_path.get_attribute(
                "data-required") == 'true'
        elif state_set == 'not set':
            assert attribute_type_path.get_attribute(
                "data-required") == 'false'
    elif expected_state_type == 'Necessary':
        if state_set == 'set':
            assert attribute_type_path.get_attribute(
                "data-necessary") == 'true'
        elif state_set == 'not set':
            assert attribute_type_path.get_attribute(
                "data-necessary") == 'false'


@when('the value {value} is inputted in the {input_field} field')
def input_value_in_field(context, value, input_field):
    """

    :param context:
    :param value:
    :param input_field:
    :return:
    """
    field_selector = get_element_selector(
        input_field)
    stuff = DataEntryPage(context.driver)
    field_input = context.driver.find_element(*field_selector)
    field_locator = stuff.locate_attribute_path(field_input)
    stuff.fill_input_field(field_locator, value)
    # sleep(2)


@when('the value {value} is selected in the {input_field} field')
def select_value_in_field(context, value, input_field):
    """

    :param context:
    :param value:
    :param input_field:
    :return:
    """
    field_selector = get_element_selector(
        input_field)
    stuff = DataEntryPage(context.driver)
    field_input = context.driver.find_element(*field_selector)
    field_locator = stuff.locate_attribute_path(field_input)
    stuff.fill_select_field(field_locator, value)
    # sleep(2)
