# Created by Nayira.Sanchez at 11/07/2017
  # JIRA: EOBS-893
  # Scenarios covered: 2, 3 and 4

Feature: Neurological Observation - Data Entry

  Scenario: Neurological Observation Form is correctly displayed
    Given a user with the Nurse role logs into the app
    And they view the My Patients list
    And the My Patients list has loaded
    When a random patient is selected
    And the Take observation button is selected
    And the Neurological observation is selected from the list
    Then the Neurological observation form is displayed
    And the Eyes Open field is displayed
    And the Best Verbal Response field is displayed
    And the Best Motor Response field is displayed
    And the Pupil Right - Size field is displayed
    And the Pupil Right - Reaction field is displayed
    And the Pupil Left - Size field is displayed
    And the Pupil Left - Reaction field is displayed
    And the Limb Movement - Left Arm field is displayed
    And the Limb Movement - Right Arm field is displayed
    And the Limb Movement - Left Leg field is displayed
    And the Limb Movement - Right Leg field is displayed
    And the Eyes Open entry field is set to Mandatory
    And the Limb Movement - Right Leg entry field is set to Necessary