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
    When the value 10 is inputted in the Respiration Rate field
    And the value 10 is inputted in the O2 Saturation field
    And the value 10 is inputted in the Body Temperature field
    And the value 10 is inputted in the Blood Pressure Systolic field
    And the value 10 is inputted in the Blood Pressure Diastolic field
    And the value 10 is inputted in the Pulse Rate field
    And the value Alert is selected in the AVPU field
    And the value Yes is selected in the Patient on supplemental O2 field
    Then the O2 Device field is displayed
#
#  Scenario: Blood Glucose Observation Form is correctly displayed
#    Given a user with the Nurse role logs into the app
#    And they view the My Patients list
#    And the My Patients list has loaded
#    When a random patient is selected
#    And the Take observation button is selected
#    And the Blood Glucose observation is selected from the list
#    Then the Blood Glucose observation form is displayed
#    And the Blood Glucose (mmol/L) field is displayed
#
#  Scenario: Neurological Observation Form is correctly displayed
#    Given a user with the Nurse role logs into the app
#    And they view the My Patients list
#    And the My Patients list has loaded
#    When a random patient is selected
#    And the Take observation button is selected
#    And the Neurological observation is selected from the list
#    Then the Neurological observation form is displayed
#    And the Eyes Open field is displayed
#    And the Best Verbal Response field is displayed
#    And the Best Motor Response field is displayed
#    And the Pupil Right - Size field is displayed
#    And the Pupil Right - Reaction field is displayed
#    And the Pupil Left - Size field is displayed
#    And the Pupil Left - Reaction field is displayed
#    And the Limb Movement - Left Arm field is displayed
#    And the Limb Movement - Right Arm field is displayed
#    And the Limb Movement - Left Leg field is displayed
#    And the Limb Movement - Right Leg field is displayed
#    And the Eyes Open entry field is set to Mandatory
#    And the Limb Movement - Right Leg entry field is set to Necessary
#
#  Scenario: Weight Observation Form is correctly displayed
#    Given a user with the Nurse role logs into the app
#    And they view the My Patients list
#    And the My Patients list has loaded
#    When a random patient is selected
#    And the Take observation button is selected
#    And the Weight observation is selected from the list
#    Then the Weight observation form is displayed
#    And the Waist Measurement (cm) field is displayed
#    And the Waist Measurement (cm) entry field is not set to Necessary
#
#  Scenario: Postural Blood Pressure Observation Form is correctly displayed
#    Given a user with the Nurse role logs into the app
#    And they view the My Patients list
#    And the My Patients list has loaded
#    When a random patient is selected
#    And the Take observation button is selected
#    And the Postural Blood Pressure observation is selected from the list
#    Then the Postural Blood Pressure observation form is displayed
#    And the Sitting Blood Pressure Systolic field is displayed
#    And the Sitting Blood Pressure Diastolic field is displayed
#    And the Standing Blood Pressure Systolic field is not displayed
#    And the Standing Blood Pressure Diastolic field is not displayed
#    When the value 120 is inputted in the Sitting Blood Pressure Systolic field
#    When the value 80 is inputted in the Sitting Blood Pressure Diastolic field
#    Then the Standing Blood Pressure Systolic field is displayed
#    And the Standing Blood Pressure Diastolic field is displayed
