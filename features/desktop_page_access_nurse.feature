# Created by Nayira.Sanchez at 06/02/2018
  # JIRA: EOBS-476
  # Scenarios covered: Nurse page visibility

Feature: Page visibility for Nurse user - Desktop

  Background: Nurse page visibility - Set up user for the test
    Given the user NU_476 exists
    And user NU_476 has the role of Nurse
    And the user NU_476 is allocated to Ward Test of Greenfield University Hospital

  Scenario: Nurse page visibility
    Given the user NU_476 logs into the desktop app
    Then the available menu items are filtered for the Nurse role
      | page                        |
      | Acuity Board                |
      | Patients by Ward            |
