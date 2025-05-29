# Läslistan - Automatiserade tester

Detta projekt innehåller automatiserade tester för webbsidan [Läslistan](https://tap-ht24-testverktyg.github.io/exam-template/). Testerna är skrivna i Python med hjälp av Playwright, Behave och Page Object Pattern.

## ✅ Vad som testas

- Visa en lista med böcker (7 st i katalogen)
- Klicka på hjärtat för att favoritmarkera/avmarkera en bok
- Kontrollera att bok visas/döljs i favoritlistan
- Kontrollera att hjärtikonen är markerad (med CSS-klassen `selected`)
- Scenario Outline som testar flera klick på samma hjärta
- Lägga till en ny bok med titel och författare
- Förhindra att tomma böcker läggs till (formuläret är inaktivt om titel/författare saknas)
- Navigering mellan olika vyer (alla böcker ↔ favoriter)

Se `STORIES.md` för user stories och deras koppling till features och scenarion.

## Hur man startar projektet

1. Klona projektet från GitHub:

```bash
git clone https://github.com/Sarvenaz83/readinglist-playwright.git
cd readinglist-playwright

2. Skapa och aktivera ett virtuellt Python-miljö:
python -m venv venv
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

3. Installera beroenden:
pip install -r requirements.txt
pip install playwright behave
playwright install

4. Kör testerna:
behave --no-capture

## Strukture
.
├── features/
│   ├── favoritmarkera.feature          # Favoritmarkera/avmarkera bok
│   ├── lagg_till_bok.feature           # Lägga till ny bok + validering
│   ├── navigation.feature              # Navigering mellan vyer
│   ├── environment.py
│   └── steps/
│       └── steps.py                    # Alla stegsdefinitioner
├── pages/
│   └── page_objects.py                 # Page Object för Läslistan
├── requirements.txt
├── STORIES.md                          # User Stories kopplat till tester
├── README.md
└── exam1_sarvenaz_sinaei.txt



🧪 Verktyg
Python 3.10+

Playwright

Behave

Page Object Pattern
