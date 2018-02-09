# Created by Nayira.Sanchez at 06/02/2018
  # JIRA: EOBS-476
  # Scenarios covered: Doctor page visibility

Feature: Page visibility for Doctor user - Desktop

  Background: Doctor page visibility - Set up user for the test
    Given the user DO_476 exists
    And user DO_476 has the role of Doctor
    And the user DO_476 is allocated to Ward Test of Greenfield University Hospital

  Scenario: Doctor page visibility
    Given the user DO_476 logs into the desktop app
    Then the available menu items are filtered for the Doctor role
      | page                        |
      | Acuity Board                |
      | Patients by Ward            |
      | Recently Discharged         |
      | Recently Transferred        |
      | Doctor Tasks                |
      | Overdue Tasks               |
      | My Dashboard                |
      | NEWS Analysis (last 8 days) |
      | Ward Dashboard              |
