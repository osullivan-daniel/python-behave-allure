Feature: Journey Planning

Scenario Outline: Valid Journey
    Given the user have access to the tfl api
    When they travel search for a journey from <search_from> to <search_to> using <mode_of_transport> 
    Then they should get a valid result
    And it should suggest starting points <starting_points>
    And it should suggest mode of transport <expected_mode_of_transport>

    Examples: both inside london
        | search_from                             | search_to         | starting_points                                                                       | mode_of_transport | expected_mode_of_transport |
        | '69 Notting Hill Gate, London, W11 3JS' | 'Canary Wharf'    | ['Kensington (London), Notting Hill Gate', 'Westminster (London), Notting Hill Gate'] | bus              | ["tube"]         | 
    
    Examples: one inside london, one outside london
        | search_from                             | search_to                 | starting_points                                                                       | mode_of_transport | expected_mode_of_transport |
        | '69 Notting Hill Gate, London, W11 3JS' | 'Stansted Airport London' | ['Kensington (London), Notting Hill Gate', 'Westminster (London), Notting Hill Gate'] |                   | ['national-rail']          |
        | '69 Notting Hill Gate, London, W11 3JS' | 'Stansted Airport London' | ['Kensington (London), Notting Hill Gate', 'Westminster (London), Notting Hill Gate'] | bus               | ['bus']                    | 
