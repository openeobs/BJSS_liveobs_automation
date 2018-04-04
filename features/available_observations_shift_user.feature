# Created by Nayira.Sanchez at 04/04/2018
  # JIRA: EOBS-2404
  # Scenarios covered: 6
Feature: Observations available for on Shift Nurse/HCA staff
  # The 'Take Observation' list presents the correct
  # observations for a Shift only user

  Background: Set up Staff users and patient for the test
    Given the user ObsList Nurse exists
    And the user ObsList HCA exists
    And user ObsList Nurse has the role of Nurse
    And the user ObsList Nurse is in Shift for Ward ObsList
    And user ObsList HCA has the role of HCA
    And the user ObsList HCA is in Shift for Ward ObsList
    And the patient ObsList Patient is in ObsList Bed of Ward ObsList
    And the user Responsible ShiftCoordinator exists
    And user Responsible ShiftCoordinator has the role of Shift Coordinator
    And the user Responsible ShiftCoordinator is allocated to Ward ObsList of Greenfield University Hospital
    # The Shift Coordinator scenario is to be moved to available_observations_allocated_user feature once scenario 4 of EOBS-2404 is fully implemented

  Scenario Outline: Observations available for staff on Shift only
    Given the user <user> logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient ObsList Patient is selected
    And the Take observation button is selected
    Then the NEWS observation is not listed
    And the Neurological observation is listed
    And the Blood Glucose observation is listed
    And the Weight observation is listed
    And the Postural Blood Pressure observation is listed
    And the Height observation is listed
    And the Blood Product observation is listed
    And the Food and Fluid observation is not listed
    And the GCS observation is not listed
    And the Bristol Stool observation is not listed

  Examples:
    |user                         |
    |ObsList Nurse                |
    |ObsList HCA                  |
    |Responsible ShiftCoordinator |
