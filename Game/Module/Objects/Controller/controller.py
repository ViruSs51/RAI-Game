import pygame as pg

from ..objects import Object
from ...Objects import Controller


class Controller(Object):
    keys = Controller.keys

    def __init__(self):
        super().__init__(None, None, None, None)

    async def getPressed(self, key: str | int):
        return pg.key.get_pressed()[self.keys[key] if type(key) is str else key]
