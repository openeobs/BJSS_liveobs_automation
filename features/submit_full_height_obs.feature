# Created by Tom.Leighton at 18/09/2017
# JIRA: EOBS-1564
# Scenarios covered: Needs to be defined

Feature: Verifying submission for full height observation.

  Scenario: Height observation is correctly submitted
    Given a user with the Nurse role logs into the app
    And they view the My Patients list
    And the My Patients list has loaded
    When Patient Doyle, Worth Scott is selected
    And the Take observation button is selected
    And the Height observation is selected from the list
    Then the Height observation form is displayed
    When the value 1.5 is inputted in the Height (m) field
    Then the form is submitted
    And the Height observation is confirmed
