import pygame as pg

from ..character import Character
from ...Controller.controller import Controller

class Player(Character):
    def __init__(self, window: pg.Surface, size: list[int], position: list[int], images_url: list[str]):
        super().__init__(window, size, position, images_url)

        self.controller = Controller()

    async def draw(self):
        await super().draw()

        self.character = await self.standAnimation()
        await self.control()

    async def control(self):
        if await self.controller.getPressed('w'):
            self.pos[1] -= 0.3
            self.perspective = 0
            self.type_animation = 1
        
        elif await self.controller.getPressed('s'):
            self.pos[1] += 0.3
            self.perspective = 2
            self.type_animation = 1
        
        elif await self.controller.getPressed('a'):
            self.pos[0] -= 0.3
            self.perspective = 3
            self.type_animation = 1
        
        elif await self.controller.getPressed('d'):
            self.pos[0] += 0.3
            self.perspective = 1
            self.type_animation = 1
        
        else:
            self.type_animation = 0
        
