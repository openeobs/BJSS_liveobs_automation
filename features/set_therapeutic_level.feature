# JIRA: EOBS-2106
# Scenarios covered: 1-10

Feature: Set a patient's therapeutic level

  Background: A shift coordinator and patient exist
    Given the user Shirley exists
    And user Shirley has the role of Shift Coordinator
    And the user Shirley is allocated to Ward A of Greenfield University Hospital

    And the patient Patricia is in Bed 1 of Ward A
    And the patient Patrick is in Bed 2 of Ward A

    And the user Shirley logs into the desktop app
    And they view the patient Patricia

  Scenario: Shift coordinator has an option to set patient's therapeutic level
    Then there is an option to set the therapeutic level

  Scenario: Selecting the option creates a dialog
    Given the Set Therapeutic Obs Level option is selected
    Then a dialog is created
    And

  Scenario: The therapeutic obs level defaults to 1
    Given the set therapeutic obs level
    Then there is an option to set the therapeutic level
