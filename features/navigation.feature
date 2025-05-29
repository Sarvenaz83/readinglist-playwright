Feature: Navigering mellan vyer

  Som en användare
  vill jag kunna navigera mellan boklistan och favoritlistan
  så att jag kan se alla böcker eller bara mina favoriter.

  Scenario: Gå till favoritlistan
    Given att jag är på webbsidan
    When jag klickar på länken "Favoriter"
    Then ska jag se vyn med favoriter

  Scenario: Gå tillbaka till boklistan
    Given att jag är på webbsidan
    And jag har klickat på länken "Favoriter"
    When jag klickar på länken "Alla böcker"
    Then ska jag se vyn med alla böcker
