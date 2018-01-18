# Created by Nayira.Sanchez at 02/10/2017
  # JIRA: EOBS-476
  # Scenarios covered: Shift coordinator page visibility

Feature: Page visibility for user Shift Coordinator

  Background: Shift Coordinator page visibility - Set up user for the test
    Given the user SC_476 exists
    And user SC_476 has the role of Shift Coordinator
    And the user SC_476 is allocated to Ward Test of Greenfield University Hospital

  Scenario: Shift Coordinator page visibility
    Given the user SC_476 logs into the desktop app
    When I wait for a bit
    Then the available menu items are filtered for the Shift Coordinator role
#    Then the list of tasks is filtered to show tasks for the Shift Coordinator role
      | page                        |
      | Acuity Board                |
      | Patients by Ward            |
      | Recently Discharged         |
      | Recently Transferred        |
      | Overdue Tasks               |
      | Workload                    |
      | My Dashboard                |
      | NEWS Analysis (last 8 days) |
      | Account Administration      |
      | Ward Dashboard              |
      | Nursing Shift Change        |
      | Nursing Re-Allocation       |
      | Medical Shift Change        |
