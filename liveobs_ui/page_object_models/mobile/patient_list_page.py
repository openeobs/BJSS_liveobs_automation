from functools import reduce
import random

from .list_page import ListPage

from liveobs_ui.selectors.mobile.list import LIST_ITEM_DATA_NAME


class PatientListPage(ListPage):

    @staticmethod
    def get_patient_from_item(list_item):
        """
        Get the patient's name from list item

        :param list_item: WebElement for List Item
        :return: name of patient the list item is about
        """
        patient_name_el = list_item.find_element(*LIST_ITEM_DATA_NAME)
        return patient_name_el.text

    def select_random_patient(self):
        """
        Finds a random patient in the patient list and selects it

        :return: selects and opens patient
        """
        patients = self.get_list_items()
        patient = random.choice(patients)
        self.open_item(patient)

    def get_list_item(self, patient_name):
        reformatted_patient_name = self.reformat_patient_name_for_patient_card(
            patient_name)
        patient_card = super(PatientListPage, self).get_list_item(
            reformatted_patient_name)
        return patient_card

    @staticmethod
    def reformat_patient_name_for_patient_card(patient_name):
        patient_name_parts = patient_name.split(' ')
        surname = patient_name_parts[-1]
        other_names = patient_name_parts[:-1]
        other_names = reduce(lambda x, y: x + ' ' + y, other_names)
        reformatted_patient_name = '{surname}, {other_names}'.format(
            surname=surname, other_names=other_names)
        return reformatted_patient_name
