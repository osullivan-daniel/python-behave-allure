Feature: Journey Planning

Scenario: Valid Journeys
    Given the user have access to the tfl api
    When they travel search for a journey from {a} to {b}
    Then they should get a valid result
    And it should suggest {starting_A} as a starting point
    And it should suggest {starting_B} as a starting point
    And it should suggest {jounrney_methods}