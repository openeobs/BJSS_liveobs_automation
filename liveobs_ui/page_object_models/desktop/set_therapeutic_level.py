from selenium.webdriver.support.ui import Select

from liveobs_ui.page_object_models.desktop.modal_view_common \
    import BaseModalPage
from liveobs_ui.selectors.desktop.set_therapeutic_level_selectors \
    import THERAPEUTIC_LEVEL_FIELD, THERAPEUTIC_LEVEL_FIELD_OPTIONS, \
    THERAPEUTIC_FREQUENCY_FIELD, THERAPEUTIC_FREQUENCY_FIELD_OPTIONS, \
    THERAPEUTIC_STAFF_TO_PATIENT_RATIO_FIELD, \
    THERAPEUTIC_STAFF_TO_PATIENT_RATIO_FIELD_OPTIONS


class SetTherapeuticLevelModal(BaseModalPage):

    def get_level_field(self):
        therapeutic_level_input = self.driver.find_elements(
            *THERAPEUTIC_LEVEL_FIELD
        )
        return therapeutic_level_input[0]

    def get_level(self):
        level_field = self.get_level_field()
        select = Select(level_field)
        currently_selected_option = select.first_selected_option.text.strip()
        return currently_selected_option

    def get_level_field_options(self):
        therapeutic_level_options = self.driver.find_elements(
            *THERAPEUTIC_LEVEL_FIELD_OPTIONS
        )
        return [option.text.strip() for option in therapeutic_level_options]

    def set_level(self, level_number):
        level_field = self.get_level_field()
        value = 'Level {}'.format(level_number)
        self.fill_select_field(level_field, value)

    def get_frequency_field(self):
        frequency_field = self.driver.find_elements(
            *THERAPEUTIC_FREQUENCY_FIELD
        )
        return frequency_field[0]

    def get_frequency(self, readonly=False):
        frequency_field = self.get_frequency_field()
        if readonly:
            frequency_field_value = frequency_field.text
        else:
            frequency_field_select = frequency_field.find_element_by_tag_name(
                'select')
            select = Select(frequency_field_select)
            frequency_field_value = select.first_selected_option.text.strip()
        return frequency_field_value

    def get_frequency_field_options(self):
        therapeutic_level_options = self.driver.find_elements(
            *THERAPEUTIC_FREQUENCY_FIELD_OPTIONS
        )
        return [option.text.strip() for option in therapeutic_level_options]

    def set_frequency(self, frequency):
        frequency_field = self.get_frequency_field()
        frequency_field_select = frequency_field.find_element_by_tag_name(
            'select')
        self.fill_select_field(frequency_field_select, frequency)

    def get_staff_to_patient_ratio_field(self):
        staff_to_patient_ratio = self.driver.find_elements(
            *THERAPEUTIC_STAFF_TO_PATIENT_RATIO_FIELD
        )
        return staff_to_patient_ratio[0]

    def get_staff_to_patient_ratio_field_options(self):
        staff_to_patient_ratio_options = self.driver.find_elements(
            *THERAPEUTIC_STAFF_TO_PATIENT_RATIO_FIELD_OPTIONS
        )
        return [option.text.strip() for option in
                staff_to_patient_ratio_options]

    def set_staff_to_patient_ratio(self, staff_to_patient_ratio):
        staff_to_patient_ratio_field = self.get_staff_to_patient_ratio_field()
        staff_to_patient_ratio_field_select = staff_to_patient_ratio_field \
            .find_element_by_tag_name('select')
        self.fill_select_field(
            staff_to_patient_ratio_field_select, staff_to_patient_ratio)
