from pygame import Surface
import numpy as np
from random import randint
from ..DataType import scene
from ..Scene import main_menu
from ..Scene import loading_scene
from ..Objects.Character.Player.player import Player
from ..Scene.Room.Spaceship import control_room


def load_scenes(
    window: Surface,
    window_size: str | list[int] | tuple[int],
    player: Player,
    config: dict,
    AI_training: bool = True,
) -> scene.Scenes:
    """
    Initializeaza exemplarele la scene si le returneaza
    """

    scenes = scene.Scenes(
        loading_scene=loading_scene.Loading(
            window=window, window_size=window_size, config=config
        ),
        main_menu=main_menu.MainMenu(
            window=window, window_size=window_size, config=config
        ),
        spaceship_control_room=control_room.ControlRoom(
            window=window, window_size=window_size, config=config, player=player
        ),
    )

    return scenes


def init_player(window: Surface, config: dict) -> Player:
    player = Player(
        window=window,
        size=config["characters"]["player"]["size"],
        position=config["characters"]["player"]["position"],
        images_url=config["characters"]["player"]["samples"],
        max_life=config["characters"]["player"]["max_life"],
        speed=config["characters"]["player"]["speed"],
        running_speed=config["characters"]["player"]["running_speed"],
        special_sizes=config["characters"]["player"]["special_sizes"],
        attack_range=config["characters"]["player"]["attack_range"],
        damage=config["characters"]["player"]["damage"],
        knockback=config["characters"]["player"]["knockback"],
        stamina=config["characters"]["player"]["stamina"],
    )

    return player
