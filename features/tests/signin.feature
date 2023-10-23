Feature: Test for Sign in

  Scenario: Verify user can sign in
    Given Open Signin page
    When Signin
    Then Verify sign in page successful

