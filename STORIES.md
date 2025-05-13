# User Stories – Läslistan

## 📚 Story 1: Visa boklistan
**Som en användare**  
vill jag kunna se en lista med böcker  
så att jag kan välja vad jag vill läsa.

- ✅ Testad i scenariot "Räknar alla böcker"

---

## ❤️ Story 2: Favoritmarkera bok
**Som en användare**  
vill jag kunna klicka på ett hjärta för en bok  
så att boken läggs till i min favoritlista.

- ✅ Testad i scenariot "Favoritmarkera en bok från listan"
- ✅ Scenario Outline för flera klick

---

## 🤍 Story 3: Avmarkera favorit
**Som en användare**  
vill jag kunna klicka en gång till på hjärtat  
så att boken tas bort från favoritlistan.

- ✅ Testad i Scenario Outline (klick 2 gånger)

---

## 🔁 Story 4: Klicka flera gånger
**Som en användare**  
vill jag kunna klicka flera gånger på hjärtat  
så att jag kan testa att hjärtat växlar mellan markerad och avmarkerad.

- ✅ Scenario Outline (1, 2, 3 klick)

---

## 🧪 Story 5: UI-förändring
**Som en användare**  
vill jag att hjärtats utseende ändras när jag klickar  
så att jag tydligt ser om boken är favorit eller inte.

- ✅ Testad via klass: `star` och `star selected`
