Feature: Journey Planning

Scenario Outline: Valid Journeys
    Given the user have access to the tfl api
    When they travel search for a journey from <search_from> to <search_to>
    Then they should get a valid result
    # And it should suggest <starting_A> as a starting point
    # And it should suggest <starting_B> as a starting point
    # And it should suggest <journey_methods>

    Examples: both inside london
        | search_from | search_to | starting_A | starting_B | journey_methods |
        | A | B | C | D | E |
    
    Examples: one inside london, one outside london
        | search_from | search_to | starting_A | starting_B | journey_methods |
        | A | B | C | D | E |