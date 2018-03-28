# Created by Nayira.Sanchez at 15/03/2018
@wip
Feature: Observation access on mobile

  As a user,
  I would like to be able to perform observations on the patients under my
  care,
  In order to collect data on their health and take preventative measures.

Feature: NEWS Observation - User has access to observation

  Background: NEWS Form - Set up
    Given the user NEWSForm Nurse exists
    And user NEWSForm Nurse has the role of Nurse
    And the user NEWSForm Nurse is in the current Shift for Ward Test
    And the user NEWSForm Nurse is allocated to NEWSForm Bed of Ward Test

    And the user NAYI Nurse exists
    And user NAYI Nurse has the role of Nurse
    And the user NAYI Nurse is in the current Shift for Ward Test

    And the patient NEWSForm Patient is in NEWSForm Bed of Ward Test


  Scenario: NEWS Observation Form is correctly displayed
    Given the user NEWSForm Nurse logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient NEWSForm Patient is selected
    And the Take observation button is selected
    Then the NEWS observation is listed

  Scenario: NEWS Observation Form is correctly displayed
    Given the user NAYI Nurse logs into the mobile app
    And they view the My Patients list
    And the My Patients list has loaded
    When the Patient NEWSForm Patient is selected
    And the Take observation button is selected
    Then the NEWS observation is not listed
