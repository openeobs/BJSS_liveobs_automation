# Created by Tom.Leighton at 18/09/2017
# JIRA: EOBS-1565
# Scenarios covered: Needs to be defined
Feature: Submit Full Blood Product Observation

  Background: BP Obs - Set up
    Given the user BloodProdObs Nurse exists
    And user BloodProdObs Nurse has the role of Nurse
    And the user BloodProdObs Nurse is in the current Shift for Ward Test
    And the patient BloodProdObs Patient is in BloodProdObs Bed of Ward Test
    And the user BloodProdObs Nurse is allocated to BloodProdObs Bed of Ward Test

  Scenario Outline: Blood Product observation is correctly submitted
    Given the user BloodProdObs Nurse logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient Patient, BloodProdObs is selected
    And the Take observation button is selected
    And the Blood Product observation is selected from the list
    Then the Blood Product observation form is displayed
    When the value <vol> is inputted in the Vol (ml) field
    And the value <blood_prod> is selected in the Blood Product (Applied Infusion) field
    Then the form is submitted
    And the Blood Product observation is confirmed

    Examples:
    |vol    |blood_prod       |
    |0.1    |RBC              |
    |10000  |FFP              |
    |0.1    |Platelets        |
    |10000  |Human Albumin Sol|
    |100    |DLI              |
    |5000   |Stem Cells       |
