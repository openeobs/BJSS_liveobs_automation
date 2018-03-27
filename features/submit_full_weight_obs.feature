# Created by Tom.Leighton at 18/09/2017
# JIRA: EOBS-900
# Scenarios covered: 1, 2
Feature: Verifying submission for full weight observation.

  Background: Weight Obs - Set up
    Given the user WeightObs Nurse exists
    And user WeightObs Nurse has the role of Nurse
    And the user WeightObs Nurse is in the current Shift for Ward Test
    And the patient WeightObs Patient is in WeightObs Bed of Ward Test
    And the user WeightObs Nurse is allocated to WeightObs Bed of Ward Test

  Scenario Outline: Weight observation is correctly submitted
    Given the user WeightObs Nurse logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient Patient, WeightObs is selected
    And the Take observation button is selected
    And the Weight observation is selected from the list
    Then the Weight observation form is displayed
    When the value <weight> is inputted in the Weight (kg) field
    And the value <waist> is inputted in the Waist Measurement (cm) field
    Then the form is submitted
    And the Weight observation is confirmed
    # And the BMI result is confirmed....

  Examples:
    |weight|waist|
    |0     |30   |
    |500   |500  |
    |250   |265  |
