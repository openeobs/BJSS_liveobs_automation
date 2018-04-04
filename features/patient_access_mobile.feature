# Created by Nayira.Sanchez at 15/03/2018
#   JIRA: EOBS-2404
#   Scenarios covered: 1, 10

Feature: Patient access on mobile

  Background: Setting Tom Data
    Given the user Tom Nurse exists
    And user Tom Nurse has the role of Nurse
    And the user Tom Nurse is in Shift for Ward PatientAccess

    And the user Dan Nurse exists
    And user Dan Nurse has the role of Nurse
    And the patient Ludo Bagman is in Bed 1 of Ward PatientAccess
    And the patient Bathilda Bagshot is in Bed 2 of Ward PatientAccess
    And the user Dan Nurse is allocated to Bed 1 of Ward PatientAccess
    And the user Dan Nurse is in Shift for Ward PatientAccess

    And the user Tom HCA exists
    And user Tom HCA has the role of HCA
    And the user Tom HCA is in Shift for Ward PatientAccess

    And the user Dan HCA exists
    And user Dan HCA has the role of HCA
    And the user Dan HCA is in Shift for Ward PatientAccess
    And the user Dan HCA is allocated to Bed 1 of Ward PatientAccess

    And the user Tom Shift Coordinator exists
    And user Tom Shift Coordinator has the role of Shift Coordinator
    And the user Tom Shift Coordinator is allocated to Ward PatientAccess of Greenfield University Hospital

    And the user Tom Doctor exists
    And user Tom Doctor has the role of Doctor
    And the user Tom Doctor is allocated to Ward PatientAccess of Greenfield University Hospital

    And the user Tom Senior Manager exists
    And user Tom Senior Manager has the role of Senior Manager
    And the user Tom Senior Manager is allocated to Ward PatientAccess of Greenfield University Hospital

  Scenario Outline: All users are able to see all patients in their ward.
    Given the user <user> logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    Then the Patient Ludo Bagman is in the list
    And the Patient Bathilda Bagshot is in the list

    Examples:
    | user                |
    |Tom HCA              |
    |Tom Nurse            |
    |Dan HCA              |
    |Dan Nurse            |
    |Tom Shift Coordinator|
    |Tom Doctor           |
    |Tom Senior Manager   |
