from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.remote_connection import RemoteConnection
from automation_helpers import AutomationHelpers
from os import environ


def before_all(context):
    """
    Before all features and scenarios are run set up environment
    
    :param context: Behave context 
    """
    desired_caps = {
        "platform": "Windows 10",
        "browserName": "chrome",
        "version": "58.0",

    }
    test_name = 'Selenium for Neovahealth/openeobs run {}'.format(
        environ.get('TRAVIS_JOB_NUMBER', None))
    build_tag = environ.get('BUILD_TAG', None)
    tunnel_id = environ.get('TRAVIS_JOB_NUMBER', None)
    username = environ.get('SAUCE_USERNAME', None)
    access_key = environ.get('SAUCE_ACCESS_KEY', None)

    selenium_endpoint = "https://%s:%s@ondemand.saucelabs.com:443/wd/hub" % (
    username, access_key)
    desired_caps['build'] = build_tag
    desired_caps['tunnelIdentifier'] = tunnel_id
    desired_caps['name'] = test_name

    executor = RemoteConnection(selenium_endpoint, resolve_ip=False)
    browser = webdriver.Remote(
        command_executor=executor,
        desired_capabilities=desired_caps
    )

    # This is specifically for SauceLabs plugin.
    # In case test fails after selenium session creation having this
    # here will help track it down.
    # creates one file per test non ideal but xdist is awful
    if browser is not None:
        with open("%s.testlog" % browser.session_id, 'w') as f:
            f.write("SauceOnDemandSessionID=%s job-name=%s\n" % (
            browser.session_id, test_name))
    else:
        raise WebDriverException("Never created!")
    context.driver = webdriver.Chrome()
    context.helpers = AutomationHelpers('config.yml')


def after_all(context):
    """
    After all features and scenarios are run clean up the environment
    
    :param context: Behave context 
    """
    context.driver.quit()
