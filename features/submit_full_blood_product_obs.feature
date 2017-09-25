# Created by Tom.Leighton at 18/09/2017
# JIRA: EOBS-1565
# Scenarios covered: Needs to be defined

Feature: Submit Full Blood Product Observation

Scenario Outline: Blood Product observation is correctly submitted
    Given a user with the Nurse role logs into the app
    And they view the My Patients list
    And the My Patients list has loaded
    When Patient Doyle, Worth Scott is selected
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
