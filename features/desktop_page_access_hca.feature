# Created by Nayira.Sanchez at 06/02/2018
  # JIRA: EOBS-476
  # Scenarios covered: HCA page visibility

Feature: Page visibility for HCA user - Desktop

  Background: HCA page visibility - Set up user for the test
    Given the user HCA_476 exists
    And user HCA_476 has the role of HCA
    And the user HCA_476 is allocated to Ward Test of Greenfield University Hospital

  Scenario: HCA page visibility
    Given the user HCA_476 logs into the desktop app
    Then the available menu items are filtered for the HCA role
      | page                        |
      | Acuity Board                |
      | Patients by Ward            |
