# Created by Nayira.Sanchez at 13/09/2017
# JIRA: EOBS-1087
# Scenarios covered: 1, 2 and part of 4

Feature: NEWS observation. Calculate Score/Risk.

  Background: NEWS Risk/Score calculation - Set up
    Given the user NEWSFullScore Nurse exists
    And user NEWSFullScore Nurse has the role of Nurse
    And the patient NEWSFullScore Patient is in NEWSFullScore Bed of Ward Test
    And the user NEWSFullScore Nurse is allocated to NEWSFullScore Bed of Ward Test

  Scenario Outline: NEWS Observation is correctly submitted. Risk and Score from 0 to 18
    Given the user NEWSFullScore Nurse logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient Patient, NEWSFullScore is selected
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
    | resp_rate | o2_sat | temperature | bp_sys | bp_dias| pulse | AVPU          | sup_o2 | risk    | score |
    | 12        | 96     | 36.1        | 111    | 80     | 51    | Alert         | No     | No      | 0     |
    | 11        | 96     | 38.0        | 111    | 80     | 51    | Alert         | No     | Low     | 1     |
    | 9         | 95     | 36.1        | 219    | 80     | 90    | Alert         | No     | Low     | 2     |
    | 10        | 94     | 35.1        | 219    | 80     | 90    | Alert         | No     | Low     | 3     |
    | 10        | 94     | 38.1        | 110    | 80     | 51    | Alert         | No     | Low     | 4     |
    | 10        | 94     | 39.0        | 101    | 80     | 50    | Alert         | No     | Medium  | 5     |
    | 10        | 94     | 39.0        | 100    | 80     | 41    | Alert         | No     | Medium  | 6     |
    | 10        | 93     | 39.0        | 91     | 80     | 91    | Alert         | No     | High    | 7     |
    | 10        | 92     | 39.1        | 91     | 80     | 110   | Alert         | No     | High    | 8     |
    | 10        | 92     | 39.1        | 91     | 80     | 111   | Alert         | No     | High    | 9     |
    | 21        | 92     | 39.1        | 91     | 80     | 130   | Alert         | No     | High    | 10    |
    | 24        | 91     | 39.1        | 91     | 80     | 130   | Alert         | No     | High    | 11    |
    | 25        | 91     | 39.1        | 91     | 80     | 130   | Alert         | No     | High    | 12    |
    | 24        | 91     | 35.0        | 90     | 80     | 130   | Alert         | No     | High    | 13    |
    | 8         | 91     | 35.0        | 220    | 80     | 130   | Alert         | No     | High    | 14    |
    | 8         | 91     | 35.0        | 220    | 80     | 131   | Alert         | No     | High    | 15    |
    | 10        | 91     | 35.0        | 220    | 80     | 40    | Voice         | No     | High    | 16    |
    | 23        | 91     | 35.0        | 220    | 80     | 40    | Voice         | No     | High    | 17    |
    | 25        | 91     | 35.0        | 220    | 80     | 40    | Voice         | No     | High    | 18    |

  Scenario Outline: NEWS Observation is correctly submitted. Risk and Score 19 & 20
    Given the user NEWSFullScore Nurse logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient Patient, NEWSFullScore is selected
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
    And the value <device_type> is selected in the O2 Device field
    And the value <flow_rate> is inputted in the Flow Rate (l/min) field
    Then the form is submitted
    And the Full Score submitted is <score>
    And the Full Clinical Risk submitted is <risk>
    And the NEWS observation is confirmed

  Examples:
    | resp_rate | o2_sat | temperature | bp_sys | bp_dias| pulse | AVPU          | sup_o2 | device_type   | flow_rate | risk   | score |
    | 25        | 90     | 40.0        | 220    | 80     | 40    | Pain          | Yes    | Nasal Cannula | 82        |High    | 19    |
    | 8         | 90     | 35.0        | 221    | 80     | 39    | Unresponsive  | Yes    | Nasal Cannula | 82        |High    | 20    |
