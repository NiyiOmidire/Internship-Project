# Created by commuter60 at 10/21/2023
Feature: Test Scenarios for User Guide UI

  Scenario: User can open User guide page
    Given Open Signin page
    When Signin
    And Click on settings option
    And Click on User Guide option
    Then Verify the right page opens
    Then Verify all lesson videos contain titles

