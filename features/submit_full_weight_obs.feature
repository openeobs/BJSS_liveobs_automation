# Created by Tom.Leighton at 18/09/2017
# JIRA: EOBS-900
# Scenarios covered: 1, 2

Feature: Verifying submission for full weight observation.

  Scenario Outline: Weight observation is correctly submitted
    Given a user with the Nurse role logs into the app
    And they view the My Patients list
    And the My Patients list has loaded
    When Patient Doyle, Worth Scott is selected
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
