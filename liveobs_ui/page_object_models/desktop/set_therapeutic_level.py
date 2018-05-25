""" Page object for set therapeutic level modal. """
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


from liveobs_ui.page_object_models.desktop.modal_view_common \
    import BaseModalPage
from liveobs_ui.selectors.desktop.set_therapeutic_level_selectors \
    import THERAPEUTIC_LEVEL_FIELD, THERAPEUTIC_LEVEL_FIELD_OPTIONS, \
    THERAPEUTIC_FREQUENCY_FIELD, THERAPEUTIC_FREQUENCY_FIELD_OPTIONS, \
    THERAPEUTIC_STAFF_TO_PATIENT_RATIO_FIELD, \
    THERAPEUTIC_STAFF_TO_PATIENT_RATIO_FIELD_OPTIONS


class SetTherapeuticLevelModal(BaseModalPage):
    """
    Page object for set therapeutic level modal.
    """
    def get_level_field(self):
        """
        Get the frequency field wrapper element.

        :return:
        :rtype: WebElement
        """
        therapeutic_level_input = self.driver.find_elements(
            *THERAPEUTIC_LEVEL_FIELD
        )
        return therapeutic_level_input[0]

    def get_level(self):
        """
        Get the current value of the level field.

        :return:
        :rtype: str
        """
        level_field = self.get_level_field()
        select = Select(level_field)
        currently_selected_option = select.first_selected_option.text.strip()
        return currently_selected_option

    def get_level_field_options(self):
        """
        Get the level field options available in the drop-down.

        :return:
        :rtype: list
        """
        therapeutic_level_options = self.driver.find_elements(
            *THERAPEUTIC_LEVEL_FIELD_OPTIONS
        )
        return [option.text.strip() for option in therapeutic_level_options]

    def set_level(self, level_number):
        """
        Set the level by selecting an option from the level field drop-down.

        :param level_number:
        :type level_number: int
        """
        level_field = self.get_level_field()
        value = 'Level {}'.format(level_number)
        self.fill_select_field(level_field, value)

    def get_frequency_field(self):
        """
        Get the frequency field wrapper element.

        :return:
        :rtype: WebElement
        """
        frequency_fields = self.driver.find_elements(
            *THERAPEUTIC_FREQUENCY_FIELD
        )
        for frequency_field in frequency_fields:
            if frequency_field.is_displayed():
                return frequency_field
        raise NoSuchElementException("No visible frequency field found.")

    def get_frequency(self, readonly=False):
        """
        Get the current value of the frequency field.

        :param readonly: Indicates whether the field is currently expected to
        be read-only as this affects how it is located. The method will fail
        unless this is correctly set.
        :return:
        :rtype: str
        """
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
        """
        Get the frequency field options available in the drop-down.

        :return:
        :rtype: list
        """
        therapeutic_level_options = self.driver.find_elements(
            *THERAPEUTIC_FREQUENCY_FIELD_OPTIONS
        )
        return [option.text.strip() for option in therapeutic_level_options]

    def set_frequency(self, frequency):
        """
        Sets the frequency by selecting an option from the drop-down.

        :param frequency:
        :type frequency: int
        """
        frequency_field = self.get_frequency_field()
        frequency_field_select = frequency_field.find_element_by_tag_name(
            'select')
        self.fill_select_field(frequency_field_select, frequency)

    def get_staff_to_patient_ratio_field(self):
        """
        Get the staff-to-patient ratio field wrapper element.

        :return: Staff-to-patient ratio field
        :rtype: WebElement
        """
        staff_to_patient_ratio = self.driver.find_elements(
            *THERAPEUTIC_STAFF_TO_PATIENT_RATIO_FIELD
        )
        return staff_to_patient_ratio[0]

    def get_staff_to_patient_ratio_field_options(self):
        """
        Get the staff-to-patient ratio field options available in the
        drop-down.

        :return:
        :rtype: list
        """
        staff_to_patient_ratio_options = self.driver.find_elements(
            *THERAPEUTIC_STAFF_TO_PATIENT_RATIO_FIELD_OPTIONS
        )
        return [option.text.strip() for option in
                staff_to_patient_ratio_options]

    def set_staff_to_patient_ratio(self, staff_to_patient_ratio):
        """
        Set the staff-to-patient ratio by selecting an option from the
        drop-down.

        :param staff_to_patient_ratio:
        :type staff_to_patient_ratio: str
        """
        staff_to_patient_ratio_field = self.get_staff_to_patient_ratio_field()
        staff_to_patient_ratio_field_select = staff_to_patient_ratio_field \
            .find_element_by_tag_name('select')
        self.fill_select_field(
            staff_to_patient_ratio_field_select, staff_to_patient_ratio)
