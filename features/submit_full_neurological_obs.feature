# Created by Tom.Leighton at 18/09/2017
# JIRA: EOBS-893
# Scenarios covered: 2, 3, 4, 5

Feature: Verifying submission for full neurological observation.

Scenario Outline: Neurological observation is correctly submitted
    Given a user with the Nurse role logs into the app
    And they view the My Patients list
    And the My Patients list has loaded
    When Patient Doyle, Worth Scott is selected
    And the Take observation button is selected
    And the Neurological observation is selected from the list
    Then the Neurological observation form is displayed
    When the value <eyes_open> is selected in the Eyes Open field
    And the value <best_verbal_resp> is selected in the Best Verbal Response field
    And the value <best_motor_resp> is selected in the Best Motor Response field
    And the value <pup_r_size> is selected in the Pupil Right - Size field
    And the value <pup_r_reac> is selected in the Pupil Right - Reaction field
    And the value <pup_l_size> is selected in the Pupil Left - Size field
    And the value <pup_l_reac> is selected in the Pupil Left - Reaction field
    And the value <limb_left_arm> is selected in the Limb Movement - Left Arm field
    And the value <limb_right_arm> is selected in the Limb Movement - Right Arm field
    And the value <limb_left_leg> is selected in the Limb Movement - Left Leg field
    And the value <limb_right_leg> is selected in the Limb Movement - Right Leg field
    Then the form is submitted
    And the Score submitted is <score>
    And the Neurological observation is confirmed

  Examples:
  |eyes_open   |best_verbal_resp|best_motor_resp |pup_r_size    |pup_r_reac  |pup_l_size    |pup_l_reac  |limb_left_arm  |limb_right_arm |limb_left_leg  |limb_right_leg |score|
  |Not Testable|Not Testable    |Not Testable    |8mm           |+           |Not Observable|-           |Normal Power   |Not Observable |Extension      |No Response    |0    |
  |None        |Not Testable    |Not Testable    |7mm           |-           |1mm           |Not Testable|Mild Weakness  |No Response    |No Response    |Extension      |1    |
  |None        |None            |Not Testable    |6mm           |Not Testable|2mm           |+           |Severe Weakness|Extension      |Not Observable |Spastic Flexion|2    |
  |None        |None            |None            |5mm           |+           |3mm           |-           |Spastic Flexion|Spastic Flexion|Normal Power   |Severe Weakness|3    |
  |None        |Sounds          |None            |4mm           |-           |4mm           |Not Testable|Extension      |Severe Weakness|Mild Weakness  |Mild Weakness  |4    |
  |None        |Sounds          |Extension       |3mm           |Not Testable|5mm           |+           |No Response    |Mild Weakness  |Severe Weakness|Normal Power   |5    |
  |To Pressure |Sounds          |Extension       |2mm           |+           |6mm           |-           |Not Observable |Normal Power   |Spastic Flexion|Not Observable |6    |
  |To Sound    |Sounds          |Extension       |1mm           |-           |7mm           |Not Testable|Normal Power   |Not Observable |Extension      |No Response    |7    |
  |To Sound    |Words           |Extension       |Not Observable|Not Testable|8mm           |+           |Mild Weakness  |No Response    |No Response    |Extension      |8    |
  |To Sound    |Words           |Abnormal Flexion|8mm           |+           |1mm           |-           |Severe Weakness|Extension      |Not Observable |Spastic Flexion|9    |
  |To Sound    |Confused        |Abnormal Flexion|7mm           |-           |2mm           |Not Testable|Spastic Flexion|Spastic Flexion|Normal Power   |Severe Weakness|10   |
  |Spontaneous |Confused        |Abnormal Flexion|6mm           |Not Testable|3mm           |+           |Extension      |Severe Weakness|Mild Weakness  |Mild Weakness  |11   |
  |Spontaneous |Confused        |Normal Flexion  |5mm           |+           |4mm           |-           |No Response    |Mild Weakness  |Severe Weakness|Normal Power   |12   |
  |Spontaneous |Orientated      |Normal Flexion  |4mm           |-           |5mm           |Not Testable|Not Observable |Normal Power   |Spastic Flexion|Not Observable |13   |
  |Spontaneous |Orientated      |Localising      |3mm           |Not Testable|6mm           |+           |Normal Power   |Not Observable |Extension      |No Response    |14   |
  |Spontaneous |Orientated      |Obey Commands   |2mm           |+           |7mm           |-           |Mild Weakness  |No Response    |No Response    |Extension      |15   |
