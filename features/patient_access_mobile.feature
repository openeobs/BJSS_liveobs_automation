# Created by Nayira.Sanchez at 15/03/2018
#   JIRA: EOBS-2404
#   Scenarios covered: 1, 10

Feature: Patient access on mobile

  Background: Setting Tom Data
    Given the user Brian Nurse exists
    And user Brian Nurse has the role of Nurse
    And the user Brian Nurse is in Shift for Ward PatientAccess

    And the user Pablo Nurse exists
    And user Pablo Nurse has the role of Nurse
    And the patient Ludo Bagman is in Bed 1 of Ward PatientAccess
    And the patient Bathilda Bagshot is in Bed 2 of Ward PatientAccess
    And the user Pablo Nurse is allocated to Bed 1 of Ward PatientAccess
    And the user Pablo Nurse is in Shift for Ward PatientAccess

    And the user Laura HCA exists
    And user Laura HCA has the role of HCA
    And the user Laura HCA is in Shift for Ward PatientAccess

    And the user Jacqueline HCA exists
    And user Jacqueline HCA has the role of HCA
    And the user Jacqueline HCA is in Shift for Ward PatientAccess
    And the user Jacqueline HCA is allocated to Bed 1 of Ward PatientAccess

    And the user M Shift Coordinator exists
    And user M Shift Coordinator has the role of Shift Coordinator
    And the user M Shift Coordinator is allocated to Ward PatientAccess of Greenfield University Hospital

    And the user House Doctor exists
    And user House Doctor has the role of Doctor
    And the user House Doctor is allocated to Ward PatientAccess of Greenfield University Hospital

    And the user Selena Senior Manager exists
    And user Selena Senior Manager has the role of Senior Manager
    And the user Selena Senior Manager is allocated to Ward PatientAccess of Greenfield University Hospital

  Scenario Outline: All users are able to see all patients in their ward.
    Given the user <user> logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    Then the Patient Bagman, Ludo is in the list
    And the Patient Bagshot, Bathilda is in the list

    Examples:
    | user                  |
    |Laura HCA              |
    |Brian Nurse            |
    |Jacqueline HCA         |
    |Pablo Nurse            |
    |M Shift Coordinator    |
    |House Doctor           |
    |Selena Senior Manager  |
