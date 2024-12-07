import pygame as pg
from ...Room.room import Room


class ControlRoom(Room):
    async def loader(self):
        self._window.fill('gray')
        
        await super().loader()