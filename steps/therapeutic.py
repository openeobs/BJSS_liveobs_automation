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


@given('the patient {patient_name} has never had a therapeutic observation '
       'level set')
def remove_existing_therapeutic_levels(context, patient_name):
    level_model = context.client.model(
        'nh.clinical.therapeutic.level')
    patient = context.patients[patient_name]
    all_level_records_for_patient_ids = level_model.search([
        ('patient', '=', patient.id)
    ])
    level_model.browse(all_level_records_for_patient_ids).unlink()


@given('the patient {patient_name} is on therapeutic observation level '
       '{level_number}')
def set_patient_therapeutic_level(context, patient_name, level_number):
    level_model = context.client.model(
        'nh.clinical.therapeutic.level')
    patient = context.patients[patient_name]
    all_level_records_for_patient_ids = level_model.search([
        ('patient', '=', patient.id)
    ])
    level_model.browse(all_level_records_for_patient_ids).unlink()
    level_model.create({
        'patient': patient.id,
        'level': int(level_number)
    })


@given('the user {user_name} views the patient {patient_name}')
def view_patient(context, user_name, patient_name):
    acuity_board = AcuityBoardPage(context.driver)
    acuity_board.go_to_the_acuity_board()
    patient_kanban_card = acuity_board.get_kanban_card_by_name(patient_name)
    acuity_board.open_kanban_card(patient_kanban_card)


@given('the user {user_name} selects the Set Therapeutic Obs Level option')
def select_set_therapeutic_obs_level_option(context, user_name):
    patient_record = PatientRecordPage(context.driver)
    patient_record.open_set_therapeutic_obs_level_wizard()


@when('level {level_number} is selected for the therapeutic observation level '
      'field')
def set_level(context, level_number):
    modal_page = SetTherapeuticLevelModal(context.driver)
    modal_page.set_level(level_number)


@when('{frequency} is selected for the therapeutic observation frequency '
      'field')
def set_level(context, frequency):
    modal_page = SetTherapeuticLevelModal(context.driver)
    modal_page.set_frequency(frequency)


@when('the therapeutic level changes are saved')
def assert_changes_are_saved(context):
    modal_page = SetTherapeuticLevelModal(context.driver)
    modal = modal_page.get_currently_open_modal()
    modal_page.click_modal_button_by_name(modal, 'Save')


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
    modal_page = BaseModalPage(context.driver)
    modal = modal_page.get_currently_open_modal()
    actual_title = modal_page.get_modal_title(modal)
    assert expected_title == actual_title


@then('a field labelled {label} is visible')
def assert_field_label(context, label):
    base_desktop_page = BaseDesktopPage(context.driver)
    base_desktop_page.assert_field_label_exists(label)


@then('the observation frequency field is set to {expected_frequency}')
def assert_observation_frequency_field_value(context, expected_frequency):
    modal_page = SetTherapeuticLevelModal(context.driver)
    actual_frequency = modal_page.get_frequency(readonly=True)
    assert expected_frequency == actual_frequency, \
        "Expected '{}' but was actually '{}'"\
        .format(expected_frequency, actual_frequency)


@then('the observation frequency field cannot be modified')
def assert_observation_frequency_field_is_read_only(context):
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
    expected_level = 'Level {}'.format(level_number)
    current_level_record = _get_current_therapeutic_obs_level_record(
        context, patient_name
    )
    actual_level = 'Level {}'.format(current_level_record.level)
    assert expected_level == actual_level, \
        "Expected level to be '{}' but was actually level '{}'" \
        .format(expected_level, actual_level)


@then('the therapeutic observation frequency for patient {patient_name} is '
      'Every {expected_frequency_minutes} Minutes')
def assert_frequency_updated(
        context, patient_name, expected_frequency_minutes):
    expected_frequency_minutes = int(expected_frequency_minutes)
    current_level_record = _get_current_therapeutic_obs_level_record(
        context, patient_name
    )
    actual_frequency_minutes = current_level_record.frequency
    assert expected_frequency_minutes == actual_frequency_minutes, \
        "Expected frequency to be '{}' but was actually '{}'" \
        .format(expected_frequency_minutes, actual_frequency_minutes)


def _get_current_therapeutic_obs_level_record(context, patient_name):
    level_model = context.client.model(
        'nh.clinical.therapeutic.level'
    )
    domain = [('patient', '=', context.patients[patient_name].id)]
    current_level_id = level_model.search(domain, order='id desc', limit=1)
    current_level = level_model.browse(current_level_id[0])
    return current_level
