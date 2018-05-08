""" Module that contains the ErrorModalPage class. """
from liveobs_ui.page_object_models.desktop.modal_view_common \
    import BaseModalPage
from liveobs_ui.selectors.desktop.error_selectors \
    import MODAL_CONTAINER_ERROR_MESSAGE


class ErrorModalPage(BaseModalPage):
    """
    Page object for error message modal.
    """
    def get_error_message(self):
        """
        Get the error message in the modal.

        :return:
        """
        return self.driver.find_element(*MODAL_CONTAINER_ERROR_MESSAGE).text
