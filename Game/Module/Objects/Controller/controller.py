import pygame as pg

from ..objects import Object
from ...Objects import Controller


class Controller(Object):
    keys = Controller.keys

    def __init__(self, window: pg.Surface):
        super().__init__(window, None, None, None)

    async def getPressed(self, key: str | int, objects: list[Object]=None):
        return pg.key.get_pressed()[self.keys[key] if type(key) is str else key]
