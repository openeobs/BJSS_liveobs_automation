# Created by Tom.Leighton at 18/09/2017
# JIRA: EOBS-1564
# Scenarios covered: Needs to be defined

Feature: Verifying submission for full height observation.

  Background: Hight Obs - Set up
    Given the user HightObs Nurse exists
    And user HightObs Nurse has the role of Nurse
    And the patient HightObs Patient is in HightObs Bed of Ward Test
    And the user HightObs Nurse is allocated to HightObs Bed of Ward Test

  Scenario Outline: Height observation is correctly submitted
    Given user HightObs Nurse logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When Patient Patient, HightObs is selected
    And the Take observation button is selected
    And the Height observation is selected from the list
    Then the Height observation form is displayed
    When the value <height> is inputted in the Height (m) field
    Then the form is submitted
    And the Height observation is confirmed

    Examples:
    |height|
    |0.1   |
    |3.0   |
