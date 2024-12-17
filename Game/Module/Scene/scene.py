import pygame as pg

from ..Objects.objects import Object
from ..Objects.Character.Player.player import Player


class Scene:
    objects: list[Object] = []
    swap_scene = None

    def __init__(self, window: pg.Surface, window_size: str|list[int]|tuple[int], config: dict, player: Player=None):
        self.objects = []
        self._window = window
        self._w_size = window_size
        self._player = player
        self.config = config

    def addObject(self, *objects):
        for o in objects:
            self.objects.append(o)

    async def loader(self):
        '''
        Se indica toate obiectele si logica pe scena
        '''
        
        for o in self.objects:
            await o.draw()  

        return self.swap_scene
