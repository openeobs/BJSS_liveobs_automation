# Created by Nayira.Sanchez at 11/07/2017
  # JIRA: EOBS-900
  # Scenarios covered: 1 and 2

Feature: Weight Observation - Data Entry

  Scenario: Weight Observation Form is correctly displayed
    Given a user with the Nurse role logs into the app
    And they view the My Patients list
    And the My Patients list has loaded
    When a random patient is selected
    And the Take observation button is selected
    And the Weight observation is selected from the list
    Then the Weight observation form is displayed
    And the Waist Measurement (cm) field is displayed
    And the Waist Measurement (cm) entry field is not set to Necessary
