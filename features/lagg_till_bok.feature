Feature: Lägga till nya böcker

  Som en användare
  vill jag kunna lägga till nya böcker i listan
  så att jag kan spara böcker jag är intresserad av att läsa.

  Scenario: Lägga till en ny bok med titel och författare
    Given att jag är på webbsidan
    When jag fyller i titel "Mio min Mio" och författare "Astrid Lindgren"
    And jag klickar på "Lägg till"-knappen
    Then ska boken med titel "Mio min Mio" och författare "Astrid Lindgren" visas i boklistan

  Scenario Outline: Försök att lägga till bok med saknad information
    Given att jag är på webbsidan
    When jag fyller i titel "<titel>" och författare "<författare>"
    And jag klickar på "Lägg till"-knappen
    Then ska ingen ny bok läggas till i listan

    Examples:
      | titel          | författare       |
      |                | Astrid Lindgren  |
      | Mio min Mio    |                  |
      |                |                  |
