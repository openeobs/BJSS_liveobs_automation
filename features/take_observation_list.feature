# Created by Nayira.Sanchez at 11/07/2017
  # JIRA: EOBS-979, EOBS-898, EOBS-893, EOBS-900, EOBS-1087
  # Scenarios covered: EOBS-898.1, EOBS-893.1, EOBS-900.1, EOBS-1087.1

Feature: Mobile UI - 'Take Observation' dropdown list
  # When the user presses the 'Take Observation' button in the mobile app,
  # a drop down list is presented that allows the user to select the type
  # of observation to be conducted.

  Scenario: Mental Hospitals Available Observations
    Given a user with the Nurse role logs into the app
    And they view the My Patients list
    And the My Patients list has loaded
    When a random patient is selected
    And the Take observation button is selected
#    Then the NEWS observation is listed # step not implemented
