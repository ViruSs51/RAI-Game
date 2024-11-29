from dataclasses import dataclass
from typing import Any

from ..Scene.main_menu import MainMenu


@dataclass
class Scenes:
    '''
    Tip de date care va contine scenele din joc
    '''
    main_menu: MainMenu

    def __getitem__(self, name: str):
        return getattr(self, name)
