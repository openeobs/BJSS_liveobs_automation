""" Overdue Tasks Page interaction """
from liveobs_ui.page_object_models.desktop.list_view_common import \
    BaseListViewPage


class OverdueTasksPage(BaseListViewPage):
    """
    Interaction with the Overdue Tasks Page
    """

    def go_to_overdue_tasks(self):
        """ Navigate the user to the Overdue Tasks page """
        self.go_to_page('Overdue Tasks')

    def group_by_patient(self):
        """ Group the list items by patient """
        self.select_group_by('Patient')

    def group_by_parent_location(self):
        """ Group the list items by parent location """
        self.select_group_by('Parent Location')

    def group_by_activity(self):
        """ Group the list items by activity """
        self.select_group_by('Activity')

    def group_by_assigned_to(self):
        """ Group the list items by the user they are assigned to """
        self.select_group_by('Assigned to')
