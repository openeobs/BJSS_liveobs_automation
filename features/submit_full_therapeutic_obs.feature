# Created by Nayira.Sanchez at 23/04/2018
  # JIRA: EOBS-2519
  # Scenarios covered: 1 & 3
Feature: Verifying submission for full therapeutic observation.

  Background: Therapeutic Obs Submission - Set up
    Given the user TheraObs Nurse exists
    And user TheraObs Nurse has the role of Nurse
    And the user TheraObs Nurse is in Shift for Ward Thera
    And the patient TheraObs Patient is in TheraObs Bed of Ward Thera

  Scenario Outline: Therapeutic observation is correctly submitted
    Given the user TheraObs Nurse logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient TheraObs Patient is selected
    And the Take observation button is selected
    And the Therapeutic observation is selected from the list
    Then the Therapeutic observation form is displayed
    When the value <patient_status> is selected in the Patient Status field
    And the value <location> is inputted in the Location field
    And the value <areas_concern> is inputted in the Areas of Concern field
    And the value <intervention_need> is selected in the Intervention Needed? field
    And the value <intervention_staff> is inputted in the Other Staff during Intervention field
    And the value <other_notes> is inputted in the Other Notes field
    Then the form is submitted
    And the Therapeutic observation is confirmed

  Examples:
    | patient_status        | location           | areas_concern                     | intervention_need | intervention_staff                            | other_notes                                                                                         |
    | Awake                 | Living Room        | Nothing in particular             | No                | Nobody                                        | Some stuff written here                                                                             |
    | Consultation          | Consultation Room  | Got scared of lamp                | Yes               | Nasir Straws, Julie Starling                  | Some stuff written here                                                                             |
    | Education             | Classroom 3A       | Nothing of note                   | Please Select     | Doctor Richard Standerson, Nurse Laura Olive  | Some stuff written here                                                                             |
    | Group Therapy         | Swimming Pool      | Didn't interact with the rest     | Yes               | Anna and James                                | Some stuff written here                                                                             |
    | Leave                 | In the Park        | Didn't seem happy to see family   | No                | Nobody                                        | Some stuff written here                                                                             |
    | Out (With Permission) | At family's place  | Uncomfortable with the weather    | Please Select     | Nobody                                        | Some stuff written here                                                                             |
    | Missing (Inform S/N)  | Unknown            | It's missing!                     | No                | Nobody                                        | Patient seems to be gone for about 30 minutes                                                       |
    | Sleeping              | Bed Strawberry 7   | Had nightmares - keeps waking up  | Yes               | Andrea and the rest of nurses                 | Some stuff written here                                                                             |
    | Transfer              | Ambulance          | Nothing in particular             | Please Select     | Nobody                                        | Some stuff written here                                                                             |
    | Discharge             | Probably at home   | Another shiny day, patient is ok  | Please Select     | Nobody                                        | Rainbow Rain, 351 horses, some other stuff and also a little apple with Sánderson in place and some.|
