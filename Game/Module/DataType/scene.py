from dataclasses import dataclass
from typing import Any

from ..Scene.main_menu import MainMenu
from ..Scene.Room.Spaceship.control_room import ControlRoom


@dataclass
class Scenes:
    '''
    Tip de date care va contine scenele din joc
    '''
    main_menu: MainMenu
    spaceship_control_room: ControlRoom

    def __getitem__(self, name: str) -> Any:
        return getattr(self, name)
