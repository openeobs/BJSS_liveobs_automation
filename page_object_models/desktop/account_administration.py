""" Account Administration Page Object Model """
from liveobs_ui.page_object_models.desktop.list_view_common import \
    BaseListViewPage
from liveobs_ui.selectors.desktop.list_selectors import LIST_ITEM_SELECT_BOX, \
    LIST_ITEM_SELECTED_SELECT_BOX


class AccountAdministrationPage(BaseListViewPage):
    """ Interaction with the Account Administration page """

    def go_to_account_administration(self):
        """ Navigate the user to the Account Administration page """
        self.go_to_page('Account Administration')

    def filter_on_hca(self):
        """ Filter the list to show HCA users """
        self.select_filter('HCAs')

    def filter_on_nurse(self):
        """ Filter the list to show Nurse users """
        self.select_filter('Nurses')

    def filter_on_shift_coordinators(self):
        """ Filter the list to show Shift Coordinators """
        self.select_filter('Shift Coordinators')

    def select_user(self, user_name):
        """
        Click the select box for the user in the list

        :param user_name: Name of the user to select
        """
        user_row = self.get_list_item_by_name(user_name)
        select_box = user_row.find_element(*LIST_ITEM_SELECT_BOX)
        self.click_and_verify_change(select_box, LIST_ITEM_SELECTED_SELECT_BOX)

    def select_users(self, user_names):
        """
        Select multiple users in the list

        :param user_names: List of users to select
        """
        if not isinstance(user_names, list):
            raise ValueError('select users expected a list')
        for user_name in user_names:
            self.select_user(user_name)
