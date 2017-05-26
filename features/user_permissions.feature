Feature: User Permissions
  In order to have access to only the functionality I'm allowed to do
  As a user of the system with a specified user role
  I want the system to only show me functionality my role is allowed to access

  Scenario Outline: Mobile Task List Permissions
    Given I log into the mobile as a user with the <user_role> role
    When I open the task list on the mobile
    Then I see a list of tasks for the patients in the locations I am assigned to
    And the list of tasks is filtered to show tasks for the role(s) I am associated with:
      | role    | tasks                                                                                                                                                                                                                                                                                                                               |
      | HCA     |                                                                                                                                                                                                                                                                                                           |
      | Nurse   | Informed About Patient Status (NEWS)?, Select Frequency, Assess Patient, Inform Shift Coordinator, Review Frequency, Urgently Inform Medical Team, Immediately Inform Medical Team, Inform Medical Team, Call an Ambulance (2222/9999), Set Clinical Review Frequency, F&F - 6am Fluid Intake Review, F&F - 3pm Fluid Intake Review |
      | Doctor  | Assessment Required, Clinical Review, Set Clinical Review Frequency, F&F - 6am Fluid Intake Review, F&F - 3pm Fluid Intake Review                                                                                                                                                                                                   |

    Examples:
      | user_role |
      | HCA       |
      | Nurse     |
      | Doctor    |

  Scenario: Mobile Task List Permissions for HCA
    Given a user with the HCA role logs into the app
    When they view the task list
    Then they see a list of the tasks for the patients in the locations they are assigned to
    And the list of tasks is filtered to show tasks for the HCA role:
      | tasks                       |
      | Inform Nurse About Patient  |
    
  Scenario: Mobile Task List Permissions for Nurse
    Given a user with the Nurse role logs into the app
    When they view the task list
    Then they see a list of the tasks for the patients in the locations they are assigned to
    And the list of tasks is filtered to show tasks for the Nurse role:
      | tasks                                 |
      | Informed About Patient Status (NEWS)? |
      | Select Frequency                      |
      | Assess Patient                        |
      | Inform Shift Coordinator              |
      | Review Frequency                      |
      | Urgently Inform Medical Team          |
      | Immediately Inform Medical Team       |
      | Inform Medical Team                   |
      | Call an Ambulance (2222/9999)         |
      | Set Clinical Review Frequency         |
      | F&F - 6am Fluid Intake Review         |
      | F&F - 3pm Fluid Intake Review         |
    
  Scenario: Mobile Task List Permissions for Doctor
    Given a user with the Doctor role logs into the app
    When they view the task list
    Then they see a list of the tasks for the patients in the locations they are assigned to
    And the list of tasks is filtered to show tasks for the Doctor role:
      | tasks                         |
      | Assessment Required           |
      | Clinical Review               |
      | Set Clinical Review Frequency |
      | F&F - 6am Fluid Intake Review |
      | F&F - 3pm Fluid Intake Review |

  Scenario Outline: Mobile Patient List Permissions
    Given a user with the <user_role> role logs into the app
    When they view the task list
    Then they see a list of the tasks for the patients in the locations they are assigned to

    Examples:
      | user_role |
      | HCA       |
      | Nurse     |
      | Doctor    |