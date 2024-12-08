from pygame import Surface

from ..DataType import scene
from ..Scene import main_menu
from ..Scene.Room.Spaceship import control_room


def load_scenes(window: Surface, window_size: str|list[int]|tuple[int], config: dict) -> scene.Scenes:
    '''
    Initializeaza exemplarele la scene si le returneaza
    '''

    scenes = scene.Scenes(
        main_menu=main_menu.MainMenu(window=window, window_size=window_size, config=config),
        spaceship_control_room=control_room.ControlRoom(window=window, window_size=window_size, config=config)
    )

    return scenes