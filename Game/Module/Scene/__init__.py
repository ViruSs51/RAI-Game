from pygame import Surface

from ..DataType import scene
from ..Objects.Character.Player.player import Player
from ..Scene import main_menu
from ..Scene.Room.Spaceship import control_room
from ..Scene.Interface import gameplay_ui


def load_scenes(window: Surface, window_size: str|list[int]|tuple[int], player: Player, config: dict) -> scene.Scenes:
    '''
    Initializeaza exemplarele la scene si le returneaza
    '''

    scenes = scene.Scenes(
        main_menu=main_menu.MainMenu(window=window, window_size=window_size, config=config),
        spaceship_control_room=control_room.ControlRoom(window=window, window_size=window_size, config=config, player=player)
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