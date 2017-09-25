# Created by Nayira.Sanchez at 15/09/2017
# JIRA: EOBS-1087
# Scenarios covered: Score 3 in 1 field bring Risk to Medium

Feature: NEWS Score/Risk for 3in1 cases.

  Scenario Outline: 3 in 1 observations get correct score/risk
    Given a user with the Nurse role logs into the app
    And they view the My Patients list
    And the My Patients list has loaded
    When Patient Doyle, Worth Scott is selected
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
    And the Full Score submitted is <score>
    And the Full Clinical Risk submitted is <risk>
    And the NEWS observation is confirmed

  Examples:
    | resp_rate | o2_sat | temperature | bp_sys | bp_dias| pulse | AVPU         | sup_o2 | risk    | score |
    | 25        | 96     | 38.0        | 111    | 80     | 51    | Alert        | No     | Medium  | 3     |
    | 8         | 96     | 38.0        | 111    | 80     | 51    | Alert        | No     | Medium  | 3     |
    | 12        | 91     | 36.1        | 219    | 80     | 51    | Alert        | No     | Medium  | 3     |
    | 12        | 96     | 35.0        | 219    | 80     | 51    | Alert        | No     | Medium  | 3     |
    | 12        | 96     | 36.1        | 90     | 80     | 51    | Alert        | No     | Medium  | 3     |
    | 12        | 96     | 36.1        | 220    | 80     | 51    | Alert        | No     | Medium  | 3     |
    | 12        | 96     | 36.1        | 219    | 80     | 40    | Alert        | No     | Medium  | 3     |
    | 20        | 96     | 36.1        | 111    | 80     | 131   | Alert        | No     | Medium  | 3     |
    | 20        | 96     | 36.1        | 111    | 80     | 90    | Voice        | No     | Medium  | 3     |
    | 20        | 96     | 36.1        | 111    | 80     | 90    | Pain         | No     | Medium  | 3     |
    | 20        | 97     | 36.1        | 111    | 80     | 90    | Unresponsive | No     | Medium  | 3     |
