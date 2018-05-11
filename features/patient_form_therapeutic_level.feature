# Created by Daniel.Metcalfe at 10/05/2018
Feature: Therapeutic level information is displayed on the patient form

  Displaying therapeutic level information on the patient form keeps staff
  informed when they are looking at a patient in more detail.

  Background:
    Given the user Shirley exists
    And user Shirley has the role of Shift Coordinator
    And the user Shirley is allocated to Oak Ward of Greenfield University Hospital

    And the patient Patricia is in Bed One of Oak Ward

    And the user Shirley logs into the desktop app
    And the user Shirley views the patient Patricia

  Scenario: No level set for patient
    Given the patient Patricia has never had a therapeutic observation level set
    When the user Shirley views the patient Patricia
    Then the current level is displayed as Not set
    And the recording frequency is displayed as blank
    And the staff-to-patient ratio is displayed as blank

  Scenario: Patient on level 1
    Given the patient Patricia is on therapeutic observation level 1
    When the user Shirley views the patient Patricia
    Then the current level is displayed as 1
    And the recording frequency is displayed as Every Hour
    And the staff-to-patient ratio is displayed as blank

  Scenario: Patient on level 2
    Given the patient Patricia is on therapeutic observation level 2 with frequency Every 5 Minutes
    When the user Shirley views the patient Patricia
    Then the current level is displayed as 2
    And the recording frequency is displayed as Every 5 Minutes
    And the staff-to-patient ratio is displayed as blank

  Scenario: Patient on level 3
    Given the patient Patricia is on therapeutic observation level 3 with staff-to-patient ratio 2:1
    When the user Shirley views the patient Patricia
    Then the current level is displayed as 3
    And the recording frequency is displayed as Every Hour
    And the staff-to-patient ratio is displayed as 2:1

  Scenario: Therapeutic staff-to-patient ratio is displayed when set
    Given the patient Patricia is on therapeutic observation level 2 with frequency Every 5 Minutes
    When the user Shirley views the patient Patricia
    Then the current level is displayed as 2
    And the recording frequency is displayed as Every 5 Minutes
    And the staff-to-patient ratio is displayed as blank
