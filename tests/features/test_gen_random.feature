Feature: Testing generator gen_random
  Scenario: Testing a range with positive boundaries
    Given amount of numbers 10 and minimum 1 and maximum 10
    When we generate numbers
    Then we have to get the specified number of numbers in a given range

  Scenario: Testing a range with negative boundaries
    Given amount of numbers 10 and minimum -10 and maximum -1
    When we generate numbers
    Then we have to get the specified number of numbers in a given range

  Scenario: Testing a range with positive and negative boundaries
    Given amount of numbers 10 and minimum -10 and maximum 10
    When we generate numbers
    Then we have to get the specified number of numbers in a given range