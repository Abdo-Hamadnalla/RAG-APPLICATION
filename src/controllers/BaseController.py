from helper.config import get_settings, Settings
class BaseController:
    """
    Base controller class for handling common functionality across controllers.
    """
    def __init__(self):
        self.app_settings= get_settings()