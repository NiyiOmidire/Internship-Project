Feature: Tests for Main page UI

  Scenario: Verify that footer has correct amount of links
    Given Open Amazon page
    Then Verify footer has 35 links

  Scenario: Verify that footer has many links
    Given Open Amazon page
    Then Verify many links are shown in the footer

#    Note: hover over the a word here then press
#    Press ctrl+b to open the steps that correlates to this feature