import pygame as pg

from ..Objects.objects import Object
from ..Objects.Character.Player.player import Player


class Scene:
    objects: list[Object] = []
    swap_scene = None
    returned = []

    def __init__(
        self,
        window: pg.Surface,
        window_size: str | list[int] | tuple[int],
        config: dict,
        player: Player = None,
    ):
        self.objects = []
        self._window = window
        self._w_size = window_size
        self._player = player
        self.config = config

    def addObject(self, *objects):
        for o in objects:
            self.objects.append(o)

    async def loader(self):
        """
        Se indica toate obiectele si logica pe scena
        """

        self.returned = []
        for o in self.objects:
            if -200 < o.pos[0] < self._w_size[0]+200 and -200 < o.pos[1] < self._w_size[1]+200:
                self.returned.append(await o.draw(objects=self.objects))

            else:
                try:
                    await o.processing()
                except: pass

        return self.swap_scene
