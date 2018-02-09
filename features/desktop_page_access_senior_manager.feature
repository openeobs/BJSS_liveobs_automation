# Created by Nayira.Sanchez at 06/02/2018
  # JIRA: EOBS-476
  # Scenarios covered: Senior Manager page visibility

Feature: Page visibility for Senior Manager user - Desktop

  Background: Senior Manager page visibility - Set up user for the test
    Given the user SM_476 exists
    And user SM_476 has the role of Senior Manager
    And the user SM_476 is allocated to Ward Test of Greenfield University Hospital

  Scenario: Senior Manager page visibility
    Given the user SM_476 logs into the desktop app
    Then the available menu items are filtered for the Senior Manager role
      | page                        |
      | Patients by Ward            |
      | Recently Discharged         |
      | Recently Transferred        |
      | Overdue Tasks               |
      | Workload                    |
      | My Dashboard                |
      | NEWS Analysis (last 8 days) |
      | Ward Dashboard              |
