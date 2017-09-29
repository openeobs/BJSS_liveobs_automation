# Created by Nayira.Sanchez at 21/09/2017
# JIRA: Not Available - Need to define
# Scenarios covered:

Feature: Partial NEWS obs - Submit with Reason 'Asleep'

  Background: Set up user and Patient for the test
    Given the user NEWSPartial Nurse exists
    And user NEWSPartial Nurse has the role of Nurse
    And the patient NEWSPartial Patient is in NEWSPartial Bed of Ward Test
    And the user NEWSPartial Nurse is allocated to NEWSPartial Bed of Ward Test

  Scenario Outline: Submission of Partial NEWS Observation
    Given user NEWSPartial Nurse logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When Patient Patient, NEWSPartial is selected
    And the Take observation button is selected
    And the NEWS observation is selected from the list
    Then the NEWS observation form is displayed
    When the value <resp_rate> is inputted in the Respiration Rate field
    And the value <o2_sat> is inputted in the O2 Saturation field
    And the value <temperature> is inputted in the Body Temperature field
    And the value <bp_sys> is inputted in the Blood Pressure Systolic field
    And the value <bp_dias> is inputted in the Blood Pressure Diastolic field
    And the value <pulse> is inputted in the Pulse Rate field
    And the value <AVPU> is selected in the AVPU field
    And the value <sup_o2> is selected in the Patient on supplemental O2 field
    Then the form is submitted
    And the Reason for partial observation popup is displayed
    And the reason <reason> is selected
    And the Partial Score submitted is <score>
    And the Partial Clinical Risk submitted is <risk>
    And the Partial NEWS observation is confirmed

  Examples:
    | resp_rate | o2_sat | temperature | bp_sys | bp_dias| pulse | AVPU          | sup_o2         | risk    | score | reason            |
    | 12        | 96     | 36.1        | 111    | 80     | 51    | Alert         | Please Select  | No      | 0     | Asleep            |
    | 12        | 96     | 35.0        | 111    | 80     | 51    | Alert         | Please Select  | Medium  | 3     | Request By Doctor |
    | 10        | 96     | 36.0        | 92     | 80     | 95    | Alert         | Please Select  | Medium  | 5     | Patient Aggression|
    | 12        | 92     | 36.1        | 111    | 80     | 51    | Alert         | Please Select  | Low     | 2     | Patient Aggression|
    | 10        | 96     | 35.0        | 111    | 80     | 40    | Alert         | Please Select  | High    | 7     | Refused           |
