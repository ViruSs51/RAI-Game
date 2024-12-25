# RAI-Game

## Overview
RAI-Game este un joc construit în Python utilizând biblioteca Pygame. Pentru a îmbunătăți performanța și a optimiza gestionarea resurselor, proiectul utilizează programarea asincronă.

## Structura Proiectului
### [main.py](main.py)
Fișierul principal al proiectului. Acesta integrează toate modulele și gestionează logica globală a jocului.

- **Clasa Game**
  - **Inițializare**: Configurează fereastra jocului și încarcă toate scenele definite.
  - **Metode Principale**:
    - `initWindow`: Creează și returnează fereastra principală.
    - `run`: Rulează jocul utilizând metode asincrone.
    - `__loop`: Un loop principal care gestionează logica în timpul rularii.
    - `__functionLoader`: Încarcă și rulează funcțiile globale.
  - **Atribute**:
    - `__run`: Indicativ pentru statusul jocului (rulare/oprire).
    - `__scene`: Scena activă curentă.

### Module
Structurat pe trei categorii principale:
1. **DataType**: Tipuri de date personalizate utilizate pentru optimizarea dezvoltării.
2. **Objects**: Gestionarea obiectelor din joc (buton, text, jucător etc.).
3. **Scene**: Gestionarea scenelor jocului. Modulele conțin elemente precum meniul principal sau alte locații din joc.

- **Scene**:
  - Toate scenele sunt derivate din clasa `Scene`.
  - La încărcarea modulului `Scene`, funcția `load_scenes` returnează o listă cu toate scenele disponibile.
