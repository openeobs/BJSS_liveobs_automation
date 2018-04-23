# Created by Nayira.Sanchez at 23/04/2018
  # JIRA: EOBS-2219
  # Scenarios covered: 1 & 2
Feature: Therapeutic Observation - Data Entry

  Background: Therapeutic Obs Form - Set up
    Given the user TheraObs Nurse exists
    And user TheraObs Nurse has the role of Nurse
    And the user TheraObs Nurse is in Shift for Ward Thera
    And the patient TheraObs Patient is in TheraObs Bed of Ward Thera

  Scenario: Therapeutic Observation Form is correctly displayed
    Given the user TheraObs Nurse logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient TheraObs Patient is selected
    And the Take observation button is selected
    And the Therapeutic observation is selected from the list
    Then the Therapeutic observation form is displayed
    And the Patient Status field is displayed
    And the Location field is displayed
    And the Areas of Concern field is displayed
    And the Intervention Needed? field is displayed
    And the Other Staff during intervention field is displayed
    And the Other Notes field is displayed
    And the Patient Status entry field is set to Mandatory
