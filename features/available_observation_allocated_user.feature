# Created by Nayira.Sanchez at 11/07/2017
  # JIRA: EOBS-979, EOBS-898, EOBS-893, EOBS-900, EOBS-1087, EOBS-2404
  # Scenarios covered: EOBS-898.1, EOBS-893.1, EOBS-900.1, EOBS-1087.1
  # EOBS-2404.4, EOBS-2404.5
Feature: Observations available for on Responsible/Allocated Staff
  # The 'Take Observation' list presents the correct
  # observations for a Responsible/Allocated user

  Background: Set up Responsible/Allocated users and patient for the test
    Given the user Allocated Nurse exists
    And the user Allocated HCA exists
    And the user Responsible Doctor exists

    And user Allocated Nurse has the role of Nurse
    And user Allocated HCA has the role of HCA
    And user Responsible Doctor has the role of Doctor

    And the user Allocated Nurse is in Shift for Ward ObsList
    And the user Allocated HCA is in Shift for Ward ObsList

    And the patient ObsList Patient is in ObsList Bed of Ward ObsList

    And the user Allocated Nurse is allocated to ObsList Bed of Ward ObsList
    And the user Allocated HCA is allocated to ObsList Bed of Ward ObsList
    And the user Responsible Doctor is allocated to Ward ObsList of Greenfield University Hospital

  Scenario Outline: Observations available for staff Responsible/Allocated
    Given the user <user> logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient ObsList Patient is selected
    And the Take observation button is selected
    Then the NEWS observation is listed
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
    |Allocated Nurse              |
    |Allocated HCA                |
    |Responsible Doctor           |
#    |Responsible ShiftCoordinator |
