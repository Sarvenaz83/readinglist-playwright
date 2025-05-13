# Läslistan - Automatiserade tester

Detta projekt innehåller automatiserade tester för webbsidan [Läslistan](https://tap-ht24-testverktyg.github.io/exam-template/). Testerna är skrivna i Python med hjälp av Playwright, Behave och Page Object Pattern.

## Vad som testas

- Visa en lista med böcker
- Klicka på hjärtat för att favoritmarkera en bok
- Kontrollera att hjärtat ändras till en fylld ikon
- Kontrollera att boken visas i favoritlistan
- Räkna antal böcker i katalogen

Se `STORIES.md` för user stories.

## Hur man startar projektet

1. Klona projektet från GitHub:

```bash
git clone https://github.com/DITT-ANVÄNDARNAMN/REPO-NAMN.git
cd REPO-NAMN

2. Skapa och aktivera ett virtuellt Python-miljö:
python -m venv venv
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

3. Installera beroenden:
pip install playwright behave
playwright install

4. Kör testerna:
behave

## Strukture
.
├── features/
│   ├── favoritmarkera.feature
│   ├── environment.py
│   └── steps/
│       └── steps.py
├── pages/
│   └── page_objects.py
├── STORIES.md
├── README.md

## Teknik
Python 
Playwright
Behave
Page Object Pattern
