import pygame as pg 
from .hotbar import Hotbar
import time, threading


class StaminaBar(Hotbar):
    def __init__(self,
        window: pg.Surface,
        size: list[int] = [300, 20],
        position: list[int] = [0, 0],
        colors: list[list[int] | str] = [(136,231,136),(136,231,136), (136,231,136)],
        border_radius: int = -1,
        stamina = 100,
        maxstamina= 100):
        super().__init__(window, size, position, colors, border_radius)
        self.stamina= stamina
        self.maxstamina= maxstamina     

    async def useStamina(self, energyUsed):
        self.useStamina-= energyUsed

        

    async def draw(self, objects = None):
        ratio = self.stamina /self.maxstamina
        self.size = [self.size[0] * ratio, 20]
        self.bar = pg.draw.rect(
                self.window,
                self.colors[self.fill_index],
                self.pos + self.size,
                border_radius=self.border_radius,
            )    
    

