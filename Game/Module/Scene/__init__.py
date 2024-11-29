from pygame import Surface

from ..DataType import scene
from ..Scene import main_menu


def load_scenes(window: Surface) -> scene.Scenes:
    '''
    Initializeaza exemplarele la scene si le returneaza
    '''

    scenes = scene.Scenes(
        main_menu=main_menu.MainMenu(window=window)
    )

    return scenes