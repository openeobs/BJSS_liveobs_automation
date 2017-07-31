# Created by Nayira.Sanchez at 11/07/2017
  # JIRA: EOBS-898
  # Scenarios covered: 1 and 2

Feature: Blood Glucose Observation - Data Entry

  Scenario: Blood Glucose Observation Form is correctly displayed
    Given a user with the Nurse role logs into the app
    And they view the My Patients list
    And the My Patients list has loaded
    When Patient Doyle, Worth Scott is selected
    And the Take observation button is selected
    And the Blood Glucose observation is selected from the list
    Then the Blood Glucose observation form is displayed
    And the Blood Glucose (mmol/L) field is displayed
