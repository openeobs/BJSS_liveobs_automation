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