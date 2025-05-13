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
