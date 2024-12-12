from pygame import Surface
from ..DataType import scene
from ..Scene import main_menu, loading_scene


def load_scenes(window: Surface) -> scene.Scenes:
    '''
    Initializeaza exemplarele la scene si le returneaza
    '''

    scenes = {
        'loading_scene': loading_scene.Loading(window=window),
        'main_menu':main_menu.MainMenu(window=window)
    }

    return scenes