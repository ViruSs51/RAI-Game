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


---

## Installation

Follow these steps to set up and play **RAI**:

### 1. Clone the Repository
```bash
git clone https://github.com/ViruSs51/rai-game.git
cd rai-game
```

### 2. Set Up a Python Virtual Environment (Optional but Recommended)
```bash
python3 -m venv venv
source venv\Scripts\activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Required Dependencies
The game requires specific Python libraries listed in `requirements.txt`. Use the following command to install them:
```bash
pip install -r requirements.txt
```

### 4. Install the image generation model
```bash
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui

cd stable-diffusion-webui
```

If you're on Mac or Linux run webui.sh and wait to finish
```bash
./webui.sh
```

If you're on Windows run webui.bat and wait to finish
```bash
.\webui.bat
```
It will open a browser page, you don't need that 


#### After installation of the Stable Diffusion Model close the terminal and :
#### Go to Game Assets/hypernetworks and move all the hypernetworks to the stable-diffusion-webui/models/hypernetworks folder
#### After that: 
If you're on Mac or Linux run webui.sh with the --api comand line arguments:
```bash
./webui.sh --api
```
If you're on Windows run webui.bat with the --api comand line arguments:
```bash
.\webui.bat --api
```

Close the page that appers


### 5. Go back to RAI-Game folder and run the game:
```bash
python main.py
```

---

## Requirements

- **Python 3.10.7**
- **pip** (Python's package installer)
- **git**
- **Operating System**: Windows, macOS, or Linux

---

## Contributing

We welcome contributions! Feel free to fork the repository and submit pull requests. For major changes, please open an issue to discuss what you'd like to change.

---

## License

This project is licensed under the [MIT License](LICENSE).

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->