from selenium.webdriver.support.ui import Select

from liveobs_ui.page_object_models.desktop.modal_view_common \
    import BaseModalPage
from liveobs_ui.selectors.desktop.set_therapeutic_level_selectors \
    import THERAPEUTIC_LEVEL_FIELD, THERAPEUTIC_LEVEL_FIELD_OPTIONS, \
    THERAPEUTIC_FREQUENCY_FIELD


class SetTherapeuticLevelModal(BaseModalPage):

    def get_level_field(self):
        therapeutic_level_input = self.driver.find_elements(
            *THERAPEUTIC_LEVEL_FIELD)
        return therapeutic_level_input[0]

    def get_level(self):
        level_field = self.get_level_field()
        select = Select(level_field)
        currently_selected_option = select.first_selected_option.text.strip()
        return currently_selected_option

    def get_level_field_options(self):
        therapeutic_level_options = self.driver.find_elements(
            *THERAPEUTIC_LEVEL_FIELD_OPTIONS)
        return [option.text.strip() for option in therapeutic_level_options]

    def set_level(self, level_number):
        level_field = self.get_level_field()
        value = 'Level {}'.format(level_number)
        self.fill_select_field(level_field, value)

    def get_frequency_field(self):
        frequency_field = self.driver.find_elements(
            *THERAPEUTIC_FREQUENCY_FIELD)
        return frequency_field[0]

    def get_frequency(self):
        frequency_field = self.get_frequency_field()
        select = Select(frequency_field)
        currently_selected_option = select.first_selected_option.text.strip()
        return currently_selected_option
