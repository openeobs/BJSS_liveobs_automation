# Created by Daniel.Metcalfe at 16/04/2017
# JIRA: EOBS-2106
# Scenarios covered: 1-10

Feature: Setting of patient's therapeutic level

  Background: A shift coordinator and patient exist
    Given the user Shirley exists
    And user Shirley has the role of Shift Coordinator
    And the user Shirley is allocated to Oak Ward of Greenfield University Hospital

    And the patient Patricia is in Bed One of Oak Ward

    And the user Shirley logs into the desktop app
    And the user Shirley views the patient Patricia

  Scenario: Error notification when no level selected
    Given the user Shirley selects the Set Therapeutic Obs Level option
    When the therapeutic level changes are saved
    Then a notification with the error message The following fields are invalid: for the field Observation Level is displayed

  Scenario: Error modal when no frequency selected on level 2
    Given the user Shirley selects the Set Therapeutic Obs Level option
    And level 2 is selected for the level field
    When the therapeutic level changes are saved
    Then a modal with the error message Please fill out all fields before saving. is displayed

  Scenario: Error modal when no staff-to-patient ratio selected on level 3
    Given the user Shirley selects the Set Therapeutic Obs Level option
    And level 3 is selected for the level field
    When the therapeutic level changes are saved
    Then a modal with the error message Please fill out all fields before saving. is displayed
