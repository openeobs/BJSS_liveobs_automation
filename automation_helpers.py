""" Automation Helpers """
from yaml import load


class AutomationHelpers(object):
    """
    A class with stuff to help with automation
    """

    def __init__(self, config_file_path):
        """
        Intiialise the automation helpers class
        
        :param config_file_path: Path to context file to load 
        """
        with open(config_file_path, 'r') as config_file:
            self.config = load(config_file.read())

    def get_user_for_role(self, user_role):
        """
        Get login details for user with specified role
        
        :param user_role: Name of user role 
        :return: Tuple of (username, password, database)
        """
        return (
            self.config.get('user_role_map').get(user_role),
            self.config.get('user_role_map').get(user_role),
            self.config.get('database')
        )

    def get_patient_names_for_user(self, user):
        """
        Get list of patients for specified user

        :param user: Name of user
        :return: list of patient names
        """
        return self.config.get('user_patient_map').get(user, [])
