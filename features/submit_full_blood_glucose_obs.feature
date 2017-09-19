# Created by Tom.Leighton at 18/09/2017
# JIRA: EOBS-898
# Scenarios covered: 1 and 3

Feature: Submit Full Blood Glucose Observation

  Scenario: Full Blood Glucose Observation is correctly submitted.
    Given a user with the Nurse role logs into the app
    And they view the My Patients list
    And the My Patients list has loaded
    When Patient Doyle, Worth Scott is selected
    And the Take observation button is selected
    And the Blood Glucose observation is selected from the list
    Then the Blood Glucose observation form is displayed
    When the value 10 is inputted in the Blood Glucose (mmol/L) field
    Then the form is submitted
    And the Blood Glucose observation is confirmed
