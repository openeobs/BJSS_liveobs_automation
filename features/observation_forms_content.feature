# Created by Nayira.Sanchez at 26/06/2017

  #This feature includes coverage for the following JIRA tickets:
  #- EOBS-1087

Feature: Mobile - Observation forms
  Ensure the forms for all available observations are correctly displayed in the mobile app, and that all the expected fields are displayed

  Scenario: NEWS Observation Form is correctly displayed
    Given a user with the Nurse role logs into the app
    And they view the My Patients list
    And the My Patients list has loaded
    When a random patient is selected
    And the Take observation button is selected
    And the NEWS observation is selected from the list
    Then the NEWS observation form is displayed
    And the Respiration Rate field is displayed
    And the O2 Saturation field is displayed
    And the Body Temperature field is displayed
    And the Blood Pressure Systolic field is displayed
    And the Blood Pressure Diastolic field is displayed
    And the Pulse Rate field is displayed
    And the AVPU field is displayed
    And the Patient on supplemental O2 field is displayed
    And the O2 Device field is not displayed

  Scenario: Blood Glucose Observation Form is correctly displayed
    Given a user with the Nurse role logs into the app
    And they view the My Patients list
    And the My Patients list has loaded
    When a random patient is selected
    And the Take observation button is selected
    And the Blood Glucose observation is selected from the list
    Then the Blood Glucose observation form is displayed
    And the Blood Glucose (mmol/L) field is displayed

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