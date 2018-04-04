# Created by Nayira.Sanchez at 11/07/2017
  # JIRA: EOBS-898
  # Scenarios covered: 1 and 2

Feature: Blood Glucose Observation - Data Entry

  Background: BG Obs - Set up user and Patient for the test
    Given the user BloodGlu Nurse exists
    And user BloodGlu Nurse has the role of Nurse
    And the user BloodGlu Nurse is in the current Shift for Ward Test
    And the patient BloodGlu Patient is in BloodGlu Bed of Ward Test
    And the user BloodGlu Nurse is allocated to BloodGlu Bed of Ward Test

  Scenario: Blood Glucose Observation Form is correctly displayed
    Given the user BloodGlu Nurse logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient BloodGlu Patient is selected
    And the Take observation button is selected
    And the Blood Glucose observation is selected from the list
    Then the Blood Glucose observation form is displayed
    And the Blood Glucose (mmol/L) field is displayed
