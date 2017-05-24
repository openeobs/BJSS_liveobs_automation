"""
Selectors for modal component
The modal component is used in the mobile to show information to the user
while they are on another screen. It consists of a cover which greys out the
current screen and the dialog which lays ontop of the cover.
"""

from selenium.webdriver.common.by import By

MODAL_COVER = (By.CSS_SELECTOR, '.cover')
MODAL_DIALOG = (By.CSS_SELECTOR, '.dialog')
MODAL_CONTENT = (By.CSS_SELECTOR, '.dialog .dialogContent')
MODAL_TITLE = (By.CSS_SELECTOR, '.dialog h2')
MODAL_BUTTONS = (By.CSS_SELECTOR, '.dialog .options')

MODAL_CONTENT_DEFINITION_LIST = (By.CSS_SELECTOR, '.dialog dl')
MODAL_CONTENT_DEFINITION_LIST_TERM = (By.CSS_SELECTOR, '.dialog dl dt')
MODAL_CONTENT_DEFINITION_LIST_DEFINITION = (By.CSS_SELECTOR, '.dialog dl dd')
MODAL_CONTENT_LIST = (By.CSS_SELECTOR, '.dialog .menu')
MODAL_CONTENT_IMAGE = (By.CSS_SELECTOR, '.dialog img')
MODAL_CONTENT_IFRAME = (By.CSS_SELECTOR, '.dialog iframe')

MODAL_CONTENT_SELECT = (By.CSS_SELECTOR, '.dialog select')
MODAL_CONTENT_SHARELIST = (By.CSS_SELECTOR, '.dialog .sharelist')
MODAL_CONTENT_SHARELIST_INPUT = (By.CSS_SELECTOR, '.dialog .sharelist input')

LOW_CLINICAL_RISK_MODAL = (By.CSS_SELECTOR, '.dialog.clinicalrisk-low')
MEDIUM_CLINICAL_RISK_MODAL = (By.CSS_SELECTOR, '.dialog.clinicalrisk-medium')
HIGH_CLINICAL_RISK_MODAL = (By.CSS_SELECTOR, '.dialog.clinicalrisk-high')

FULLSCREEN_MODAL = (By.CSS_SELECTOR, '.full-modal')
FULLSCREEN_MODAL_IFRAME = (By.CSS_SELECTOR, '.full-modal iframe')
FULLSCREEN_MODAL_HEADER = (By.CSS_SELECTOR, '.full-modal p')
FULLSCREEN_MODAL_BUTTON = (By.CSS_SELECTOR, '.full-modal p a')
