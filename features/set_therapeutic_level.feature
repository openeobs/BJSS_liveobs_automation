# JIRA: EOBS-2106
# Scenarios covered: 1-10

Feature: Setting of patient's therapeutic level

  Background: A shift coordinator and patient exist
    Given the user Shirley exists
    And user Shirley has the role of Shift Coordinator
    And the user Shirley is allocated to Oak Ward of Greenfield University Hospital

    And the patient Patricia is in Bed One of Oak Ward
    And the patient Patrick is in Bed Two of Oak Ward

    And the user Shirley logs into the desktop app
    And the user Shirley views the patient Patricia

  Scenario: The title 'Set Therapeutic Obs Level' is displayed
    Given the user Shirley selects the Set Therapeutic Obs Level option
    Then The title Set Therapeutic Obs Level is displayed

  Scenario: Default to level 1 for new patients
    Given the user Shirley selects the Set Therapeutic Obs Level option
    Then the therapeutic observation level field is set to level 1

  Scenario: Default to current observation level for existing patients
    Given the patient Patricia is on therapeutic observation level 2
    And the user Shirley selects the Set Therapeutic Obs Level option
    Then the therapeutic observation level field is set to level 2

  Scenario: The user can choose a new observation level for the patient
    Given the user Shirley selects the Set Therapeutic Obs Level option
    Then the user can choose a new observation level for the patient
    | therapeutic level |
    |                   |
    | Level 1           |
    | Level 2           |
    | Level 3           |
    | Level 4           |

  Scenario: Frequency set to 'Every Hour' when setting level 1
    Given the user Shirley selects the Set Therapeutic Obs Level option
    When level 1 is selected for the therapeutic observation level field
    Then the observation frequency field is set to Every Hour
    And it cannot be modified

  Scenario: Select frequency when setting level 2
    Given the user Shirley selects the Set Therapeutic Obs Level option
    When level 2 is selected for the therapeutic observation level field
    Then a frequency can be chosen for the patient's therapeutic observations

  Scenario: Default to current staff to patient ratio when level 3 selected
    Given the user Shirley selects the Set Therapeutic Obs Level option
    When level 3 is selected for the therapeutic observation level field
    Then a staff-to-patient ratio can be chosen

  Scenario: Default to current staff to patient ratio when level 4 selected
    Given the user Shirley selects the Set Therapeutic Obs Level option
    When level 4 is selected for the therapeutic observation level field
    Then a staff-to-patient ratio can be chosen

  Scenario: Changes made are saved
    Given the user Shirley selects the Set Therapeutic Obs Level option
    When level 2 is selected for the therapeutic observation level field
    And 'Every 15 Minutes' is selected for the therapeutic observation frequency field
    Then the therapeutic observation level for patient Patricia is level 2
    And the therapeutic observation frequency for patient Patricia is 'Every 15 Minutes'
