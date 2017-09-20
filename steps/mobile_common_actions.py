""" Step Implementations for common actions in the mobile application """

# pylint: disable=invalid-name
# pylint: disable=no-name-in-module

from behave import given, when, then
from liveobs_ui.page_object_models.mobile.list_page import ListPage
from liveobs_ui.page_object_models.mobile.patient_page import PatientPage
from liveobs_ui.page_object_models.mobile.data_entry_page import DataEntryPage
from liveobs_ui.page_object_models.mobile.modal_page import ModalPage

from liveobs_ui.selectors.mobile.get_selector_by_lookup import \
    get_element_selector
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
    if button_name == "Take observation":
        patient_page = PatientPage(context.driver)
        patient_page.open_adhoc_menu()


@when('a random patient is selected')
def select_random_patient_in_list(context):
    """
    Finds and selects a random patient in the 'My Patients' page

    :param context: Behave context
    :return: selects a random patient card from the Patient list in the app
    """
    select_patient = ListPage(context.driver)
    select_patient.select_random_patient()


@when('Patient {patient_name} is selected')
def select_defined_patient(context, patient_name):
    """
    Finds a named patient in the list and selects it
    :param context: behave context
    :param patient_name: the name and surenae of the patient to be selected
    """
    select_patient = ListPage(context.driver)
    patient = select_patient.get_list_item(patient_name)
    select_patient.open_item(patient)


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


@then('the {observation_field} field {status} displayed')
def verify_obs_field_is_displayed(context, observation_field, status):
    """
    Verify the specified field is displayed in the form

    :param context: Behave context
    :param observation_field: name of the observation field to be checked
    :param status: either 'is' or 'is not'
    """
    field_check = DataEntryPage(context.driver)
    if status == 'is':
        assert field_check.verify_obs_field_displayed(observation_field), \
            "Expected field '{}' to be displayed but it isn't.".format(
                observation_field)
    else:
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
    obs_form = DataEntryPage(context.driver)
    field_input = obs_form.get_element_by_lookup(obs_data_entry_field)
    attribute_type_path = obs_form.locate_attribute_path(field_input)
    states = {
        'set': 'true',
        'not set': 'false'
    }
    attrib = {
        'Mandatory': obs_form.get_state_of_el(
            attribute_type_path,
            'data-required',
            states.get(state_set)),
        'Necessary': obs_form.get_state_of_el(
            attribute_type_path,
            'data-necessary',
            states.get(state_set))
    }
    assert attrib.get(expected_state_type)


@when('the value {value} is {input_type} in the {input_field} field')
def input_value_in_field(context, value, input_type, input_field):
    """
    Inputs or selects a specified value into a field
    :param context: behave context
    :param value: a value/option to input/select
    :param input_type: either input or select field
    :param input_field: name of field to locate
    """
    field_selector = get_element_selector(
        input_field)
    obs_page = DataEntryPage(context.driver)
    field_input = context.driver.find_element(*field_selector)
    field_locator = obs_page.locate_attribute_path(field_input)
    if input_type == 'inputted':
        obs_page.fill_input_field(field_locator, value)
    elif input_type == 'selected':
        obs_page.fill_select_field(field_locator, value)


@then('the {obs_name} observation {shown} listed')
def verify_obs_in_take_obs_list(context, obs_name, shown):
    """
    Verifies an observation is listed in the Take Observation list
    :param context: behave context
    :param obs_name: text for the observation to find
    :param shown: determines if the element should/should not be on the page
    """
    patient_page = PatientPage(context.driver)
    if shown == 'is':
        assert patient_page.get_observation_in_menu(obs_name), \
            "Expected observation '{}' not displayed on the list.".format(
                obs_name)
    else:
        assert not patient_page.get_observation_in_menu(obs_name), \
            "Unexpected observation '{}' is displayed in the list".format(
                obs_name)


@then('the form is submitted')
def submit_the_form(context):
    """
    Submits an observation form
    :param context: behave context
    """
    form_page = DataEntryPage(context.driver)
    form_page.submit_form()


@then('the {value_to_check} submitted is {expected_value}')
def confirm_calculated_value(context, value_to_check, expected_value):
    """
    Gets and verifies a value (clinical risk or score) displayed in the
    submission confirmation popup
    :param context: behave driver
    :param value_to_check: The value 'name' to look for. Can be Clinical Risk,
     NEWS score or GSC score. Refers to a specific locator in the page, by text
    :param expected_value: the value expected
    :return: boolean
    """
    form_page = DataEntryPage(context.driver)
    displayed_value = form_page.get_clinical_risk_in_popup(value_to_check)
    assert expected_value in displayed_value, \
        "Expected clinical risk '{}' not displayed.".format(expected_value)


@then('the {obs_name} observation is confirmed')
def confirm_observation_submission(context, obs_name):
    """
    Verifies the correct message and observation name is displayed upon
    confirming the submission of an observation form
    :param context: behave context
    :param obs_name: name of the observation expected
    :return: boolean
    """
    form_page = DataEntryPage(context.driver)
    form_page.confirm_submit_scored_ob()
    modal_page = ModalPage(context.driver)
    modals = modal_page.get_open_modals()
    submit_modal = modals[0]
    assert modal_page.get_modal_title(submit_modal) == \
        'Successfully Submitted {} Observation'.format(obs_name)
