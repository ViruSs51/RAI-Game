from pygame import Surface
from ..DataType import scene
from ..Scene import main_menu
from ..Scene.loading_scene import Loading
from ..Objects.Character.Player.player import Player

def load_scenes(window: Surface, window_size: str|list[int]|tuple[int], player: Player, config: dict) -> scene.Scenes:
    '''
    Initializeaza exemplarele la scene si le returneaza
    '''

    scenes = scene.Scenes(
        loading_scene= Loading(window=window ,window_size=window_size, config=config),
        main_menu=main_menu.MainMenu(window=window,  window_size=window_size, config=config)
    )

    return scenes

def init_player(window: Surface, config: dict) -> Player:
    player = Player(
        window=window,
        size=config['characters']['player']['size'], 
        position=config['characters']['player']['position'],
        images_url=config['characters']['player']['samples']
    )

    return player