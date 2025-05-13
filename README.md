# Läslistan - Automatiserade tester

Detta projekt innehåller automatiserade tester för webbsidan [Läslistan](https://tap-ht24-testverktyg.github.io/exam-template/). Testerna är skrivna i Python med hjälp av Playwright, Behave och Page Object Pattern.

## ✅ Vad som testas

- Visa en lista med böcker
- Klicka på hjärtat för att favoritmarkera en bok
- Ta bort en bok från favoritlistan (genom att klicka igen)
- Kontrollera att hjärtikonen ändras (❤️ / 🤍)
- Kontrollera att boken finns i/inte finns i favoritlistan
- Scenario Outline som testar flera klick
- Räkna antalet böcker i katalogen

Se `STORIES.md` för user stories.

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
│   ├── favoritmarkera.feature
│   ├── environment.py
│   └── steps/
│       └── steps.py
├── pages/
│   └── page_objects.py
├── requirements.txt
├── STORIES.md
├── README.md
└── exam1_sarvenaz_sinaei.txt


🧪 Verktyg
Python 3.10+

Playwright

Behave

Page Object Pattern
