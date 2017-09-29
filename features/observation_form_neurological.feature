# Created by Nayira.Sanchez at 11/07/2017
  # JIRA: EOBS-893
  # Scenarios covered: 2, 3 and 4

Feature: Neurological Observation - Data Entry

  Background: Neuro Form - Set up
    Given the user Neuro Nurse exists
    And user Neuro Nurse has the role of Nurse
    And the patient Neuro Patient is in Neuro Bed of Ward Test
    And the user Neuro Nurse is allocated to Neuro Bed of Ward Test

  Scenario: Neurological Observation Form is correctly displayed
    Given the user Neuro Nurse logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient Patient, Neuro is selected
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
