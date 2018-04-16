import unittest

from behave import given, when, then

from liveobs_ui.page_object_models.desktop.acuity_board import AcuityBoardPage
from liveobs_ui.page_object_models.desktop.patient_record \
    import PatientRecordPage
from liveobs_ui.page_object_models.desktop.modal_view_common \
    import BaseModalPage


@given('the user {user_name} views the patient {patient_name}')
def view_patient(context, user_name, patient_name):
    acuity_board = AcuityBoardPage(context.driver)
    acuity_board.go_to_the_acuity_board()
    patient_kanban_card = acuity_board.get_kanban_card_by_name(patient_name)
    acuity_board.open_kanban_card(patient_kanban_card)


@when('the user {user_name} selects the Set Therapeutic Obs Level option')
def select_set_therapeutic_obs_level_option(context, user_name):
    patient_record = PatientRecordPage(context.driver)
    patient_record.open_set_therapeutic_obs_level_wizard()


@then('the title {expected_title} is displayed')
def assert_title_is_displayed(context, expected_title):
    modal_page = BaseModalPage(context.driver)
    modal = modal_page.get_currently_open_modal()
    actual_title = modal_page.get_modal_title(modal)
    assert expected_title == actual_title
