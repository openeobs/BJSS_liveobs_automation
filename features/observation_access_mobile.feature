# Created by Nayira.Sanchez at 15/03/2018
Feature: #Enter feature name here
  # Enter feature description here

Feature: NEWS Observation - User has access to observation

  Background: NEWS Form - Set up
    Given the user NEWSForm Nurse exists
    And user NEWSForm Nurse has the role of Nurse
    And the user NEWSForm Nurse is allocated to NEWSForm Bed of Ward Test

    And the user NAYI exists
    And user NAYI has the role of Nurse
    And the user NAYI is in Shift for Ward Test

    And the patient NEWSForm Patient is in NEWSForm Bed of Ward Test


  Scenario: NEWS Observation Form is correctly displayed
    Given the user NEWSForm Nurse logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient Patient, NEWSForm is selected
    And the Take observation button is selected
    And the NEWS observation is displayed

  Scenario: NEWS Observation Form is correctly displayed
    Given the user NAYI logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient Patient, NEWSForm is selected
    And the Take observation button is selected
    And the NEWS observation is not displayed