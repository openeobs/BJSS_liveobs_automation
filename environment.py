from selenium import webdriver
from automation_helpers import AutomationHelpers


def before_all(context):
    """
    Before all features and scenarios are run set up environment
    
    :param context: Behave context 
    """
    context.driver = webdriver.Chrome()
    context.helpers = AutomationHelpers('config.yml')


def after_all(context):
    """
    After all features and scenarios are run clean up the environment
    
    :param context: Behave context 
    """
    context.driver.quit()
