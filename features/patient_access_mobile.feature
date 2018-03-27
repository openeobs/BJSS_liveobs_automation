# Created by Nayira.Sanchez at 15/03/2018
Feature: #Enter feature name here
  # Enter feature description here

  Background: Setting Tom Data
    Given the user Tom Nurse exists
    And user Tom Nurse has the role of Nurse
    And the user Tom Nurse is in Shift for Ward Tom

    And the user Dan Nurse exists
    And user Dan Nurse has the role of Nurse
    And the user Dan Nurse is allocated to Bed 1 of Ward Tom

    And the user Tom HCA exists
    And user Tom HCA has the role of HCA
    And the user Tom HCA is in Shift for Ward Tom

    And the user Dan HCA exists
    And user Dan HCA has the role of HCA
    And the user Dan HCA is allocated to Bed 1 of Ward Tom

    And the user Tom Doctor exists
    And user Tom Doctor has the role of Doctor
    And the user Tom Doctor is allocated to Ward Test of Greenfield University Hospital

    And the patient Ludo Bagman is in Bed 1 of Ward Tom
    And the patient Bathilda Bagshot is in Bed 2 of Ward Tom

  Scenario Outline: Users of Ward Shift have full patient visibility from shift change
    Given the user <user> logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    Then the Patient Ludo Bagman is displayed
    And the Patient Bathilda Bagshot is displayed

    Examples:
    | user     |
    |Tom HCA   |
    |Tom Nurse |
    |Dan HCA   |
    |Dan Nurse |
    |Tom Doctor|

#  Scenario Outline: Users of Ward Shift have full patient visibility after re-allocation
#    Given the user <user> logs into the mobile app
#    And they view the My Patients list
#    And the My Patients list has loaded
#    Then the Patient Ludo Bagman is displayed
#    And the Patient Bathilda Bagshot is displayed
#
#    Reallocation steps
#
#    Examples:
#    | | |