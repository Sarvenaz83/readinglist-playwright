# User Stories – Läslistan

Detta dokument beskriver user stories och hur varje funktion testas genom features och scenarios i Behave.

---

## 📚 Story 1: Visa boklistan
**Som en användare**  
vill jag kunna se en lista med böcker  
så att jag kan välja vad jag vill läsa.

- ✅ Testas i feature: `favoritmarkera.feature`  
- ✅ Scenario: "Räknar alla böcker"  
- ✅ Kontroll att listan innehåller exakt 7 böcker vid start

---

## ❤️ Story 2: Favoritmarkera bok
**Som en användare**  
vill jag kunna klicka på ett hjärta för en bok  
så att boken läggs till i min favoritlista.

- ✅ Testas i feature: `favoritmarkera.feature`  
- ✅ Scenario: "Favoritmarkera en bok från listan"  
- ✅ Kontroll att hjärtat får klassen `selected`  
- ✅ Kontroll att boken visas i vyn "Favoriter"

---

## 🤍 Story 3: Avmarkera favorit
**Som en användare**  
vill jag kunna klicka en gång till på hjärtat  
så att boken tas bort från favoritlistan.

- ✅ Testas i feature: `favoritmarkera.feature`  
- ✅ Scenario Outline med 2 klick  
- ✅ Kontroll att `selected` tas bort från klassnamnet  
- ✅ Kontroll att boken inte längre finns i favoritlistan


---

## 🔁 Story 4: Klicka flera gånger
**Som en användare**  
vill jag kunna klicka flera gånger på hjärtat  
så att jag kan testa att hjärtat växlar mellan markerad och avmarkerad.

- ✅ Testas i feature: `favoritmarkera.feature`  
- ✅ Scenario Outline med 1, 2, 3 klick  
- ✅ Kontroll av status efter varje klick
---

## 🧪 Story 5: Visuell återkoppling (ikonstatus)

**Som en användare**  
vill jag att hjärtats utseende ändras tydligt när jag klickar  
så att jag vet om boken är favorit eller inte.

- ✅ Testas med kontroll av `data-testid` och `selected` i klassnamn  
- ✅ Visuell återkoppling via CSS-stil

---

## 🧭 Story 6: Navigering mellan vyer

**Som en användare**  
vill jag kunna växla mellan "Alla böcker" och "Favoriter"  
så att jag kan se olika delar av boklistan.

- ✅ Testas i feature: `navigation.feature`  
- ✅ Scenarion för att gå till Favoriter och tillbaka  
- ✅ Kontroll att rätt vy visas

---

## ➕ Story 7: Lägga till en ny bok

**Som en användare**  
vill jag kunna fylla i titel och författare  
så att jag kan lägga till en ny bok till listan.

- ✅ Testas i feature: `lagg_till_bok.feature`  
- ✅ Scenario: "Lägga till en ny bok med titel och författare"  
- ✅ Kontroll att boken syns sist i listan

---

## 🚫 Story 8: Förhindra tillägg utan titel/författare

**Som en användare**  
vill jag inte kunna lägga till en bok om fälten är tomma  
så att jag undviker felaktiga eller ofullständiga poster.

- ✅ Testas i feature: `lagg_till_bok.feature`  
- ✅ Scenario Outline med tomma fält  
- ✅ Kontroll att knappen är inaktiv (disabled)  
- ✅ Kontroll att ingen ny bok läggs till

---


