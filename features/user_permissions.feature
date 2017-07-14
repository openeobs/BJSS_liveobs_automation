# Created by Nayira.Sanchez at 11/07/2017
  # JIRA: EOBS-
  # Scenarios covered:


Feature: User Permissions for Tasks
  In order to have access to only the functionality I'm allowed to do
  As a user of the system with a specified user role
  I want the system to only show me functionality my role is allowed to access

  Scenario: Mobile Task List Permissions for HCA
    Given a user with the HCA role logs into the app
    When they view the task list
    Then the list of tasks is filtered to show tasks for the HCA role
      | tasks                       |
      | Inform Nurse About Patient  |
      | NEWS Observation            |

  Scenario: Mobile Task List Permissions for Nurse
    Given a user with the Nurse role logs into the app
    When they view the task list
    Then the list of tasks is filtered to show tasks for the Nurse role
      | tasks                                 |
      | Informed About Patient Status (NEWS)? |
      | Select Frequency                      |
      | Assess Patient                        |
      | Inform Shift Coordinator              |
      | Review Frequency                      |
      | Urgently Inform Medical Team          |
      | Immediately Inform Medical Team       |
      | Inform Medical Team?                  |
      | Call an Ambulance (2222/9999)         |
      | Set Clinical Review Frequency         |
      | F&F - 6am Fluid Intake Review         |
      | F&F - 3pm Fluid Intake Review         |
      | NEWS Observation                      |

  Scenario: Mobile Task List Permissions for Doctor
    Given a user with the Doctor role logs into the app
    When they view the task list
    Then the list of tasks is filtered to show tasks for the Doctor role
      | tasks                         |
      | Assessment Required           |
      | Clinical Review               |
      | Set Clinical Review Frequency |
      | F&F - 6am Fluid Intake Review |
      | F&F - 3pm Fluid Intake Review |
