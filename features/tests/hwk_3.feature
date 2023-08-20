# Created by commuter60 at 8/6/2023
#Feature: Tests for orders
#
#  Scenario: Verify that a user can see sign in page by clicking order
#    Given Open Amazon page
#    When Click orders
#    Then Verify sign in header
#
#  Scenario: Verify that a user can see that Amazon cart is empty by clicking the cart icon
#    Given Open Amazon page
#    When Click cart icon
#    Then Verify Amazon cart is empty
#
#  Scenario: Verify that a user can add a product to cart
#    Given Open Amazon page
#    When Click search Amazon field
#    When Search for lamp
#    When Click on the first product
#    When Click on Add to Cart button
#    When Open cart page
#    Then Verify cart has 1 item