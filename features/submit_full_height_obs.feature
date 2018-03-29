# Created by Tom.Leighton at 18/09/2017
# JIRA: EOBS-1564
# Scenarios covered: Needs to be defined
Feature: Verifying submission for full height observation.

  Background: Hight Obs - Set up
    Given the user HeightObs Nurse exists
    And user HeightObs Nurse has the role of Nurse
    And the user HeightObs Nurse is in the current Shift for Ward Test
    And the patient HeightObs Patient is in HeightObs Bed of Ward Test
    And the user HeightObs Nurse is allocated to HeightObs Bed of Ward Test

  Scenario Outline: Height observation is correctly submitted
    Given the user HeightObs Nurse logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient HeightObs Patient is selected
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
