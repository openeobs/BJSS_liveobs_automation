"""
Implements steps in feature files relating to Therapeutic observations.
"""
import re

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then

from liveobs_ui.page_object_models.desktop.set_therapeutic_level \
    import SetTherapeuticLevelModal
from liveobs_ui.page_object_models.desktop.acuity_board import AcuityBoardPage
from liveobs_ui.page_object_models.desktop.patient_record \
    import PatientRecordPage
from liveobs_ui.page_object_models.desktop.modal_view_common \
    import BaseModalPage
from liveobs_ui.page_object_models.desktop.desktop_common \
    import BaseDesktopPage
from liveobs_ui.page_object_models.desktop.error_modal import ErrorModalPage
from liveobs_ui.page_object_models.desktop.desktop_notification \
    import DesktopNotificationPage

from liveobs_ui.selectors.desktop.error_selectors import \
    MODAL_CONTAINER_ERROR_MESSAGE, NOTIFICATION_ERROR_MESSAGE_FIRST_LINE


@given('no therapeutic observation level has been set for the patient '
       '{patient_name} during the current spell')
def remove_existing_therapeutic_levels(context, patient_name):
    """
    Ensure that the patient has no therapeutic level records so that a test can
    behave as though the patient is new.

    :param context:
    :param patient_name:
    :return:
    """
    level_model = context.client.model(
        'nh.clinical.therapeutic.level')
    patient = context.patients[patient_name]
    all_level_records_for_patient_ids = level_model.search([
        ('patient', '=', patient.id)
    ])
    level_model.browse(all_level_records_for_patient_ids).unlink()


@given('the patient {patient_name} is on therapeutic observation level 1')
def set_patient_therapeutic_level_1(context, patient_name):
    """
    Set a value for the therapeutic observation level field.

    :param context:
    :param patient_name:
    :return:
    """
    level_model = context.client.model(
        'nh.clinical.therapeutic.level')
    patient = context.patients[patient_name]
    all_level_records_for_patient_ids = level_model.search([
        ('patient', '=', patient.id)
    ])
    level_model.browse(all_level_records_for_patient_ids).unlink()
    level_model.create({
        'patient': patient.id,
        'level': 1
    })


@given('the patient {patient_name} is on therapeutic observation level 2 with '
       'frequency {frequency}')
def set_patient_therapeutic_level_2(context, patient_name, frequency):
    """
    Set a value for the therapeutic observation level field.

    :param context:
    :param patient_name:
    :param frequency:
    :return:
    """
    frequency_int = _get_frequency_int_from_string(frequency)

    level_model = context.client.model(
        'nh.clinical.therapeutic.level')
    patient = context.patients[patient_name]
    all_level_records_for_patient_ids = level_model.search([
        ('patient', '=', patient.id)
    ])
    level_model.browse(all_level_records_for_patient_ids).unlink()

    level_model.create({
        'patient': patient.id,
        'level': 2,
        'frequency': frequency_int
    })


@given('the patient {patient_name} is on therapeutic observation level 3 with '
       'staff-to-patient ratio {staff_to_patient_ratio}')
def set_patient_therapeutic_level_3(
        context, patient_name, staff_to_patient_ratio):
    """
    Set a value for the therapeutic observation level field.

    :param context:
    :param patient_name:
    :param staff_to_patient_ratio:
    :return:
    """
    staff_to_patient_ratio_int = \
        _get_staff_to_patient_ratio_int_from_string(staff_to_patient_ratio)

    level_model = context.client.model('nh.clinical.therapeutic.level')
    patient = context.patients[patient_name]
    all_level_records_for_patient_ids = level_model.search([
        ('patient', '=', patient.id)
    ])
    level_model.browse(all_level_records_for_patient_ids).unlink()

    level_model.create({
        'patient': patient.id,
        'level': 3,
        'staff_to_patient_ratio': staff_to_patient_ratio_int
    })


@given('that the patient {patient_name} had a therapeutic observation '
       'level 1 set during a previous spell')
def create_previous_spell(context, patient_name):
    """
    Setup the data so that the patient has a previous spell.

    :param context:
    :param patient_name:
    :return:
    """
    patient = context.patients[patient_name]
    set_patient_therapeutic_level_1(context, patient_name)

    api_model = context.client.model('nh.eobs.api')
    api_model.discharge(patient.other_identifier, {})
    api_model.admit(
        patient.other_identifier, {'location': context.ward.code}
    )


@given('the user {user_name} views the patient {patient_name}')
@when('the user {user_name} views the patient {patient_name}')
def view_patient(context, user_name, patient_name):
    """
    Navigate to the patient form for the passed patient.

    :param context:
    :param user_name:
    :param patient_name:
    :return:
    """
    acuity_board = AcuityBoardPage(context.driver)
    acuity_board.go_to_the_acuity_board()
    patient_kanban_card = acuity_board.get_kanban_card_by_name(patient_name)
    acuity_board.open_kanban_card(patient_kanban_card)


@given('the user {user_name} selects the Set Therapeutic Obs Level option')
def select_set_therapeutic_obs_level_option(context, user_name):
    """
    Select the 'Set Therapeutic Obs Level' option on the patient form.

    :param context:
    :param user_name:
    :return:
    """
    patient_record = PatientRecordPage(context.driver)
    patient_record.open_set_therapeutic_obs_level_wizard()


@given('{level} is selected for the level field')
@when('{level} is selected for the level field')
def select_level(context, level):
    """
    Select a value for the level field.

    :param context:
    :param level:
    :return:
    """
    if level == 'nothing':
        return
    level_number = level[-1]

    modal_page = SetTherapeuticLevelModal(context.driver)
    modal_page.set_level(level_number)


@when('{frequency} is selected for the frequency field')
def select_frequency(context, frequency):
    """
    Select a value for the frequency field.

    :param context:
    :param frequency:
    :return:
    """
    if frequency == 'nothing':
        return
    modal_page = SetTherapeuticLevelModal(context.driver)
    modal_page.set_frequency(frequency)


@when('{staff_to_patient_ratio} is selected for the staff-to-patient ratio '
      'field')
def select_staff_to_patient_ratio(context, staff_to_patient_ratio):
    """
    Select a level for the staff-to-patient ratio field.

    :param context:
    :param staff_to_patient_ratio:
    :return:
    """
    if staff_to_patient_ratio == 'nothing':
        return
    modal_page = SetTherapeuticLevelModal(context.driver)
    modal_page.set_staff_to_patient_ratio(staff_to_patient_ratio)


@when('the therapeutic level changes are saved')
def assert_changes_are_saved(context):
    """
    Save the changes by pressing the 'Save' button in the modal.

    :param context:
    :return:
    """
    modal_page = SetTherapeuticLevelModal(context.driver)
    modal = modal_page.get_currently_open_modal()

    scenario_name = context.scenario.name
    if 'Error notification' in scenario_name:
        modal_page.click_modal_button_by_name(
            modal, 'Save',
            element_to_verify=NOTIFICATION_ERROR_MESSAGE_FIRST_LINE,
            hidden=False
        )
    elif 'Error modal' in scenario_name:
        modal_page.click_modal_button_by_name(
            modal, 'Save',
            element_to_verify=MODAL_CONTAINER_ERROR_MESSAGE,
            hidden=False
        )
    else:
        modal_page.click_modal_button_by_name(modal, 'Save')


@when('the therapeutic level changes are cancelled')
def cancel_therapeutic_level_changes(context):
    """
    Cancel therapeutic level changes by pressing the 'Cancel' button in the
    modal.

    :param context:
    :return:
    """
    modal_page = SetTherapeuticLevelModal(context.driver)
    modal = modal_page.get_currently_open_modal()
    modal_page.click_modal_button_by_name(modal, 'Cancel')


@then('the therapeutic observation level field is set to level {level_number}')
def assert_observation_level_field_value(context, level_number):
    """
    Assert the value of the observation level field.

    :param context:
    :param level_number:
    :return:
    """
    expected_level = 'Level {}'.format(level_number)
    modal_page = SetTherapeuticLevelModal(context.driver)
    actual_level = modal_page.get_level()
    assert expected_level == actual_level, \
        "Expected level input to have a value of '{}' but was actually '{}'." \
        .format(expected_level, actual_level)


@then('a new observation level can be chosen for the patient')
def assert_observation_level_field_options(context):
    """
    Assert the options in the observation level field.

    :param context:
    :return:
    """
    expected_level_options = \
        [row['therapeutic level'] for row in context.table]
    modal_page = SetTherapeuticLevelModal(context.driver)
    actual_level_options = modal_page.get_level_field_options()
    assert expected_level_options == actual_level_options, \
        "Expected options to be '{}' but was actually '{}'" \
        .format(expected_level_options, actual_level_options)


@then('the title {expected_title} is displayed')
def assert_title_is_displayed(context, expected_title):
    """
    Assert that the title in the 'Set Therapeutic Obs Level' popup is as
    expected.

    :param context:
    :param expected_title:
    :return:
    """
    modal_page = BaseModalPage(context.driver)
    modal = modal_page.get_currently_open_modal()
    actual_title = modal_page.get_modal_title(modal)
    assert expected_title == actual_title


@then('a field labelled {label} is visible')
def assert_field_label(context, label):
    """
    Assert that the label for a particular field is as expected.

    :param context:
    :param label:
    :return:
    """
    base_desktop_page = BaseDesktopPage(context.driver)
    base_desktop_page.assert_field_label_exists(label)


@then('the observation frequency field is set to {expected_frequency}')
def assert_observation_frequency_field_value(context, expected_frequency):
    """
    Assert that the value of the frequency field is as expected. Useful for
    checking pre-populated or default values.

    :param context:
    :param expected_frequency:
    :return:
    """
    modal_page = SetTherapeuticLevelModal(context.driver)
    actual_frequency = modal_page.get_frequency(readonly=True)
    assert expected_frequency == actual_frequency, \
        "Expected '{}' but was actually '{}'"\
        .format(expected_frequency, actual_frequency)


@then('the observation frequency field cannot be modified')
def assert_observation_frequency_field_is_read_only(context):
    """
    Assert that a field is read only and therefore cannot be edited.

    :param context:
    :return:
    """
    modal_page = SetTherapeuticLevelModal(context.driver)
    frequency_field = modal_page.get_frequency_field()
    assert frequency_field.tag_name == 'span'  # Not clickable.
    try:
        frequency_field.find_element(By.CSS_SELECTOR, '*')
    except NoSuchElementException:
        # No child elements which means there is nothing to click here.
        # Therefore can deduce that the field is read-only.
        pass


@then('a frequency can be chosen for the patient\'s therapeutic observations')
def assert_frequency_field_is_editable(context):
    """
    Assert that the frequency field is currently editable (rather than
    read-only) so that a frequency can be chosen by the user.

    :param context:
    :return:
    """
    expected_frequency_options = \
        [row['frequency'] for row in context.table]
    modal_page = SetTherapeuticLevelModal(context.driver)
    actual_frequency_options = modal_page.get_frequency_field_options()
    assert expected_frequency_options == actual_frequency_options, \
        "Expected options to be '{}' but was actually '{}'" \
        .format(expected_frequency_options, actual_frequency_options)


@then('a staff-to-patient ratio can be chosen for the patient\'s therapeutic '
      'observations')
def assert_staff_to_patient_ratio_field_is_editable(context):
    """
    Assert that the staff-to-patient ratio field is currently editable (rather
    than read-only) so that a frequency can be chosen by the user.

    :param context:
    :return:
    """
    expected_staff_to_patient_ratio_options = \
        [row['staff-to-patient ratio'] for row in context.table]
    modal_page = SetTherapeuticLevelModal(context.driver)
    actual_frequency_options = \
        modal_page.get_staff_to_patient_ratio_field_options()
    assert expected_staff_to_patient_ratio_options == \
        actual_frequency_options, \
        "Expected options to be '{}' but was actually '{}'" \
        .format(expected_staff_to_patient_ratio_options,
                actual_frequency_options)


@then('the therapeutic observation level for patient {patient_name} is level '
      '{level_number}')
def assert_level_updated(context, patient_name, level_number):
    """
    Assert that the level was persisted.

    :param context:
    :param patient_name:
    :param level_number:
    :return:
    """
    expected_level = 'Level {}'.format(level_number)
    current_level_record = _get_current_therapeutic_obs_level_record(
        context, patient_name
    )
    actual_level = 'Level {}'.format(current_level_record.level)
    assert expected_level == actual_level, \
        "Expected level to be '{}' but was actually level '{}'" \
        .format(expected_level, actual_level)


@then('the therapeutic observation frequency for patient {patient_name} is '
      '{expected_frequency}')
def assert_frequency_updated(
        context, patient_name, expected_frequency):
    """
    Assert that the frequency was persisted.

    :param context:
    :param patient_name:
    :param expected_frequency:
    :return:
    """
    expected_frequency_minutes = \
        _get_frequency_int_from_string(expected_frequency)

    current_level_record = _get_current_therapeutic_obs_level_record(
        context, patient_name
    )

    actual_frequency_minutes = current_level_record.frequency
    assert expected_frequency_minutes == actual_frequency_minutes, \
        "Expected frequency to be '{}' but was actually '{}'" \
        .format(expected_frequency_minutes, actual_frequency_minutes)


@then('The staff-to-patient ratio for patient {patient_name} is '
      '{expected_staff_to_patient_ratio}')
def assert_staff_to_patient_ratio_updated(
        context, patient_name, expected_staff_to_patient_ratio):
    """
    Assert that the staff-to-patient ratio was persisted.

    :param context:
    :param patient_name:
    :param expected_staff_to_patient_ratio:
    :return:
    """
    if expected_staff_to_patient_ratio == 'nothing':
        expected_staff_to_patient_ratio = False
    else:
        expected_staff_to_patient_ratio = \
            int(expected_staff_to_patient_ratio[0])

    current_level_record = _get_current_therapeutic_obs_level_record(
        context, patient_name
    )

    actual_staff_to_patient_ratio = current_level_record.staff_to_patient_ratio
    assert expected_staff_to_patient_ratio == actual_staff_to_patient_ratio, \
        "Expected staff-to-patient ratio to be '{}' but was actually '{}'" \
        .format(expected_staff_to_patient_ratio, actual_staff_to_patient_ratio)


@then('the error message {expected_error_message} is displayed')
def assert_modal_error_message_displayed(context, expected_error_message):
    """
    Asserts the correct error message is displayed in the modal.

    :param context:
    :param expected_error_message:
    :return:
    """
    error_modal = ErrorModalPage(context.driver)
    actual_error_message = error_modal.get_error_message()
    assert expected_error_message == actual_error_message, \
        "Expected error message to be '{}' but was actually '{}'"\
        .format(expected_error_message, actual_error_message)


@then('an invalid field notification is displayed for the field '
      '{invalid_field_name}')
def assert_notification_error_message_displayed(context, invalid_field_name):
    """
    Asserts the correct error message is dispalyed in the notification.

    :param context:
    :param invalid_field_name:
    :return:
    """
    desktop_notification = DesktopNotificationPage(context.driver)

    expected_error_message_first_line = 'The following fields are invalid:'
    actual_error_message_first_line = \
        desktop_notification.get_error_message_first_line()
    assert expected_error_message_first_line == \
        actual_error_message_first_line, \
        "Expected error message to be '{}' but was actually '{}'" \
        .format(
            expected_error_message_first_line, actual_error_message_first_line
        )

    expected_field_names = [invalid_field_name]
    actual_field_names = desktop_notification.get_error_message_list_items()
    assert expected_field_names == actual_field_names


@then('the {field_name} is displayed as {expected_value}')
def get_displayed_value(context, field_name, expected_value):
    """
    Get one of the values displayed for the level on the patient form.

    :param context:
    :param field_name:
    :param expected_value:
    :return:
    """
    patient_form = PatientRecordPage(context.driver)
    if field_name == 'current level':
        actual_value = patient_form.get_therapeutic_level()
    elif field_name == 'recording frequency':
        actual_value = patient_form.get_therapeutic_frequency()
    elif field_name == 'staff-to-patient ratio':
        actual_value = patient_form.get_therapeutic_staff_to_patient_ratio()
    else:
        raise ValueError(
            "Step contains unrecognised field name '{}'.".format(field_name)
        )

    expected_value = '' if expected_value == 'blank' else expected_value

    assert expected_value == actual_value, \
        "Expected '{}' but got '{}'".format(expected_value, actual_value)


def _get_current_therapeutic_obs_level_record(context, patient_name):
    """
    Private method that encapsulates the retrieval of the latest therapeutic
    level record.

    :param context:
    :param patient_name:
    :return:
    """
    patient = context.patients[patient_name]
    level_model = context.client.model('nh.clinical.therapeutic.level')
    current_level = \
        level_model.get_current_level_record_for_patient(patient.id)
    return current_level


def _get_frequency_int_from_string(frequency_string):
    if frequency_string == 'Every Hour':
        frequency_int = 60
    else:
        regex = re.compile(r"Every (\d+) Minutes")
        frequency_number = regex.match(frequency_string).group(1)
        frequency_int = int(frequency_number)
    return frequency_int


def _get_staff_to_patient_ratio_int_from_string(staff_to_patient_ratio_string):
    first_number = staff_to_patient_ratio_string[0]
    staff_to_patient_ratio_int = int(first_number)
    return staff_to_patient_ratio_int
