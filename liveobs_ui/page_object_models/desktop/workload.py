""" Workload Page Object Model """
from liveobs_ui.page_object_models.desktop.desktop_common import \
    BaseDesktopPage


class WorkloadPage(BaseDesktopPage):
    """ Interaction with the workload page """

    def go_to_workload(self):
        """ Navigate the user to the workload page """
        self.go_to_page('Workload')

    def filter_by_news(self):
        """ Filter the view by NEWS observations """
        self.select_filter('NEWS Observations Only')

    def filter_by_non_news(self):
        """ Filter the view by non-NEWS tasks """
        self.select_filter('Not NEWS')
