""" Page interaction for recently discharged and recently transferred pages """
from liveobs_ui.page_object_models.desktop.wardboard_common import \
    WardBoardPage
from liveobs_ui.page_object_models.desktop.list_view_common import \
    BaseListViewPage


class RecentlyDischargedTransferredPage(BaseListViewPage, WardBoardPage):
    """
    Interactions for the Recently Discharged and Recently Transferred pages.
    These pages share a common view so are bundled together.
    """

    def go_to_recently_discharged(self):
        """ Navigate the user to the Recently Discharged page"""
        self.go_to_page('Recently Discharged')

    def go_to_recently_tranferred(self):
        """ Navigate the user to the Recently Transferred page """
        self.go_to_page('Recently Transferred')
