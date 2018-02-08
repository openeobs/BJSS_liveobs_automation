# Created by Nayira.Sanchez at 06/02/2018
  # JIRA: EOBS-476
  # Scenarios covered: System Admin page visibility

Feature: Page visibility for System Admin user - Desktop

  Background: System Admin page visibility - Set up user for the test
    Given the user SA_476 exists
    And user SA_476 has the role of System Administrator
    And the user SA_476 is allocated to Ward Test of Greenfield University Hospital

  Scenario: System Admin page visibility
    Given the user SA_476 logs into the desktop app
    Then the available menu items are filtered for the System Admin role

      | page                        |
      | Recently Discharged         |
      | Recently Transferred        |
      | Overdue Tasks               |
      | My Dashboard                |
      | Ward Dashboard              |
      | Open eObs Users             |
      | Locations                   |
      | Patients                    |
      | Patient Visits              |
