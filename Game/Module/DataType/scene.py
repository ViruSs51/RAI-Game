from dataclasses import dataclass
from typing import Any

from ..Scene.main_menu import MainMenu
from ..Scene.loading_scene import Loading

@dataclass
class Scenes:
    '''
    Tip de date care va contine scenele din joc
    '''
    loading_scene: Loading
    main_menu: MainMenu
    

    def __getitem__(self, name: str) -> Any:
        return getattr(self, name)
