# Created by Nayira.Sanchez at 26/06/2017
  # JIRA: EOBS-1461
  # Scenarios covered: TBD - story being written

Feature: Postural Blood Pressure Observation - Data Entry

  Scenario: Postural Blood Pressure Observation Form is correctly displayed
    Given a user with the Nurse role logs into the app
    And they view the My Patients list
    And the My Patients list has loaded
    When a random patient is selected
    And the Take observation button is selected
    And the Postural Blood Pressure observation is selected from the list
    Then the Postural Blood Pressure observation form is displayed
    And the Sitting Blood Pressure Systolic field is displayed
    And the Sitting Blood Pressure Diastolic field is displayed
    And the Standing Blood Pressure Systolic field is not displayed
    And the Standing Blood Pressure Diastolic field is not displayed
    When the value 120 is inputted in the Sitting Blood Pressure Systolic field
    And the value 80 is inputted in the Sitting Blood Pressure Diastolic field
    Then the Standing Blood Pressure Systolic field is displayed
    And the Standing Blood Pressure Diastolic field is displayed
