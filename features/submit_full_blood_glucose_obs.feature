# Created by Tom.Leighton at 18/09/2017
# JIRA: EOBS-898
# Scenarios covered: 1 and 3

Feature: Submit Full Blood Glucose Observation

  Background: BG Obs - Set up
    Given the user BloodGluObs Nurse exists
    And user BloodGluObs Nurse has the role of Nurse
    And the patient BloodGluObs Patient is in BloodGluObs Bed of Ward Test
    And the user BloodGluObs Nurse is allocated to BloodGluObs Bed of Ward Test

  Scenario Outline: Blood Glucose observation is correctly submitted
    Given the user BloodGluObs Nurse logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient Patient, BloodGluObs is selected
    And the Take observation button is selected
    And the Blood Glucose observation is selected from the list
    Then the Blood Glucose observation form is displayed
    When the value <vol_blood_glu> is inputted in the Blood Glucose (mmol/L) field
    Then the form is submitted
    And the Blood Glucose observation is confirmed

    Examples:
    |vol_blood_glu|
    |0            |
    |200          |
    |100          |
