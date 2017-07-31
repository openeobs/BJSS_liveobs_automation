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
    When Patient Doyle, Worth Scott is selected
    And the Take observation button is selected
    Then the NEWS observation is listed
    And the Neurological observation is listed
    And the Blood Glucose observation is listed
    And the Weight observation is listed
    And the Postural Blood Pressure observation is listed
    And the Height observation is listed
    And the Blood Product observation is listed
    And the Food and Fluid observation is not listed
    And the GCS observation is not listed
    And the Bristol Stool observation is not listed
