from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from liveobs_ui.page_object_models.desktop.modal_view_common \
    import BaseModalPage
from liveobs_ui.selectors.desktop.set_therapeutic_level_selectors \
    import THERAPEUTIC_LEVEL_FIELD, THERAPEUTIC_LEVEL_FIELD_OPTIONS, \
    THERAPEUTIC_FREQUENCY_FIELD


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

    def set_frequency(self, frequency_in_minutes):
        frequency_field = self.get_frequency_field()
        if frequency_in_minutes == 15:
            frequency = 'Every Fifteen Minutes'
        else:
            raise NotImplementedError(
                "Frequency {} not supported by this method yet."
                .format(frequency_in_minutes)
            )
        self.fill_select_field(frequency_field, frequency)
