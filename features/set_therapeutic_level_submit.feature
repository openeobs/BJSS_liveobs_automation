# Created by Daniel.Metcalfe at 25/04/2017
# JIRA: EOBS-2106
# Scenarios covered: 1-10

Feature: Setting of patient's therapeutic level submission

  Background: Setting of patient's therapeutic level submission - A shift coordinator and patient exist
    Given the user Shirley exists
    And user Shirley has the role of Shift Coordinator
    And the user Shirley is allocated to Oak Ward of Greenfield University Hospital

    And the patient Patricia is in Bed One of Oak Ward

    And the user Shirley logs into the desktop app
    And the user Shirley views the patient Patricia

  Scenario Outline: Changes made are saved on all levels
    Given the user Shirley selects the Set Therapeutic Obs Level option
    When <set level> is selected for the level field
    And <set frequency> is selected for the frequency field
    And <set staff-to-patient ratio> is selected for the staff-to-patient ratio field
    And the therapeutic level changes are saved
    Then the therapeutic observation level for patient Patricia is level <expected level>
    And the therapeutic observation frequency for patient Patricia is <expected frequency>
    And the staff-to-patient ratio for patient Patricia is <expected staff-to-patient ratio>

    Examples:
    | set level | set frequency      | set staff-to-patient ratio | expected level | expected frequency | expected staff-to-patient ratio |
    | 1         | nothing            | nothing                    | 1              | Every Hour         | nothing                         |
    | 2         | Every 5 Minutes    | nothing                    | 2              | Every 5 Minutes    | nothing                         |
    | 2         | Every 20 Minutes   | nothing                    | 2              | Every 20 Minutes   | nothing                         |
    | 2         | Every 30 Minutes   | nothing                    | 2              | Every 30 Minutes   | nothing                         |
    | 3         | nothing            | 1:1                        | 3              | Every Hour         | 1:1                             |
    | 3         | nothing            | 2:1                        | 3              | Every Hour         | 2:1                             |
    | 3         | nothing            | 3:1                        | 3              | Every Hour         | 3:1                             |
