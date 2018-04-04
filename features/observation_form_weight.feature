# Created by Nayira.Sanchez at 11/07/2017
  # JIRA: EOBS-900
  # Scenarios covered: 1 and 2

Feature: Weight Observation - Data Entry

  Background: Weight Form - Set up
    Given the user WeightForm Nurse exists
    And user WeightForm Nurse has the role of Nurse
    And the user WeightForm Nurse is in the current Shift for Ward Test
    And the patient WeightForm Patient is in WeightForm Bed3 of Ward Test
    And the user WeightForm Nurse is allocated to WeightForm Bed3 of Ward Test

  Scenario: Weight Observation Form is correctly displayed
    Given the user WeightForm Nurse logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient WeightForm Patient is selected
    And the Take observation button is selected
    And the Weight observation is selected from the list
    Then the Weight observation form is displayed
    And the Waist Measurement (cm) field is displayed
    And the Waist Measurement (cm) entry field is not set to Necessary
