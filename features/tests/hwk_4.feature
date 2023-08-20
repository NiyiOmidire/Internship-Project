# Created by commuter60 at 8/15/2023
Feature: Tests for BestSellers page

  Scenario: Verify that page has correct amount of links
    Given Open Amazon Bestsellers page
    Then Verify page has 5 links


  Scenario: Verify that a user can add a product to cart
    Given Open Amazon Bestsellers page
    When Click search field
    When Look for lamp
    When Click on the first result
    When Click on Add to Cart button
    When Open cart page
    Then Verify result is 1


