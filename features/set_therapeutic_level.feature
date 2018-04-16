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
    When the user Shirley selects the Set Therapeutic Obs Level option

  Scenario: The title 'Set Therapeutic Obs Level' is displayed
    Then The title Set Therapeutic Obs Level is displayed

  Scenario: Default to level 1 for new patients
    Then the therapeutic observation level field defaults to level 1

  Scenario: The user can choose a new observation level for the patient
    Then The user can choose a new observation level for the patient
    | therapeutic level |
    | Level 1           |
    | Level 2           |
    | Level 3           |

  Scenario: Default to previous observation level for existing patients
    Given the patient Patricia is on therapeutic observation level 2
    When the user Shirley selects the Set Therapeutic Obs Level option
    Then the therapeutic observation level field defaults to level 1

  Scenario: Frequency set to 'Every Hour' when setting level 1
    When level 1 is selected for the therapeutic observation level field
    Then the observation frequency field is set to 'Every Hour'
    And it cannot be modified

  Scenario: Select frequency when setting level 2
    When level 2 is selected for the therapeutic observation level field
    Then the user Shirley can choose a frequency for the therapeutic observations

  Scenario: Policy reminder when setting level 3
    When level 3 is selected for the therapeutic observation level field
    Then the text 'One-to-one at all times' is displayed to the user as a policy reminder
    
  Scenario: Policy reminder when setting level 4
    When level 4 is selected for the therapeutic observation level field
    Then the text 'Within arms reach at all times' is displayed to the user as a policy reminder

  Scenario:
    Given level 2 is selected for the therapeutic observation level field
    And the frequency 'Every Fifteen Minutes' is selected
    When the change is saved
    Then the therapeutic observation level for patient Patricia is updated
