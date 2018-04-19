from behave import given, when, then

from liveobs_ui.page_object_models.desktop.set_therapeutic_level \
    import SetTherapeuticLevelModal
from liveobs_ui.page_object_models.desktop.acuity_board import AcuityBoardPage
from liveobs_ui.page_object_models.desktop.patient_record \
    import PatientRecordPage
from liveobs_ui.page_object_models.desktop.modal_view_common \
    import BaseModalPage


@given('the patient {patient_name} is on therapeutic observation level '
       '{level_number}')
def set_patient_therapeutic_level(context, patient_name, level_number):
    level_model = context.client.model(
        'nh.clinical.patient.observation.therapeutic.level')
    level_model.create({
        'patient': context.patients[patient_name].id,
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


@when('{frequency} is selected for the therapeutic observation frequency field'
      'frequency field')
def set_level(context, level_number):
    modal_page = SetTherapeuticLevelModal(context.driver)
    modal_page.set_frequency(15)


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


@then('the user can choose a new observation level for the patient')
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


@then('the observation frequency field is set to {expected_frequency}')
def assert_observation_frequency_field_value(context, expected_frequency):
    modal_page = SetTherapeuticLevelModal(context.driver)
    actual_frequency = modal_page.get_frequency(readonly=True)
    assert expected_frequency == actual_frequency, \
        "Expected '{}' but was actually '{}'"\
        .format(expected_frequency, actual_frequency)


@then('the observation frequency field cannot be modified')
def assert_observation_frequency_field_is_read_only(context):
    pass


@then('a frequency can be chosen for the patient\'s therapeutic observations')
def assert_frequency_field_is_editable(context):
    pass


@then('a staff-to-patient ratio can be chosen')
def assert_staff_to_patient_ratio_field_is_editable(context):
    pass


@then('the therapeutic observation level for patient {patient_name} is level '
      '{level_number}')
def assert_level_updated(context, patient_name, level_number):
    expected_level = 'Level {}'.format(level_number)
    current_level_record = _get_current_therapeutic_obs_level_record(
        context, patient_name
    )
    actual_level = current_level_record.level
    assert expected_level == actual_level, \
        "Expected level to be '{}' but was actually level '{}'" \
        .format(expected_level, actual_level)


@then('the therapeutic observation frequency for patient {patient_name} is '
      '{expected_frequency}')
def assert_frequency_updated(context, patient_name, expected_frequency):
    current_level_record = _get_current_therapeutic_obs_level_record(
        context, patient_name
    )
    actual_frequency = current_level_record.frequency
    assert expected_frequency == actual_frequency, \
        "Expected level to be '{}' but was actually level '{}'" \
        .format(expected_frequency, actual_frequency)


def _get_current_therapeutic_obs_level_record(context, patient_name):
    level_model = context.client.model(
        'nh.clinical.patient.observation.therapeutic.level'
    )
    domain = [('patient', '=', context.patients[patient_name])]
    current_level = level_model.search(domain, order='id desc', limit=1)
    return current_level
