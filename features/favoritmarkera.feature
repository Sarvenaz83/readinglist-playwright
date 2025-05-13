Feature: Favoritmarkera bok

    Som en användare
    vill jag kunna klicka på ett hjärta på en bok
    så att boken läggs till i min favoritlista

Scenario: Räknar alla böcker
    Given att jag är på webbsidan
    Then ska alla böcker räknas korrekt

Scenario: Favoritmarkera en bok från listan
    Given att jag är på webbsidan
    When jag klickar på hjärtat på den första boken i listan
    Then ska hjärtat ändras till en fylld ikon
    And boken ska finnas i favoritlistan

Scenario Outline: Klicka flera gånger på hjärtat för en bok
  Given att jag är på webbsidan
  When jag klickar på hjärtat för boken med index <index> <antal> gånger
  Then ska hjärtat för boken med index <index> vara <förväntad_status>

Examples:
  | index | antal | förväntad_status |
  | 0     | 1     | markerad         |
  | 0     | 2     | avmarkerad       |
  | 0     | 3     | markerad         |

