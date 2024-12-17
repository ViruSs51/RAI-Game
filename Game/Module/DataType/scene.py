from dataclasses import dataclass
from typing import Any

from ..Scene.main_menu import MainMenu
from ..Scene.loading_scene import Loading
from ..Scene.Room.Spaceship.control_room import ControlRoom


@dataclass
class Scenes:
    '''
    Tip de date care va contine scenele din joc
    '''
    loading_scene: Loading
    main_menu: MainMenu
    spaceship_control_room: ControlRoom 

    def __getitem__(self, name: str) -> Any:
        return getattr(self, name)
    
    def __contains__(self, item):
        return item in self.__dict__
