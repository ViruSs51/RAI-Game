import pygame as pg 
from ..UI.hotbar import Hotbar
import time, threading


class ShieldBar(Hotbar):
    def __init__(self,
        window: pg.Surface,
        size: list[int] = [300, 20],
        position: list[int] = [0, 0],
        colors: list[list[int] | str] = [(173, 216, 230),(173, 216, 230), (173, 216, 230)],
        border_radius: int = -1,
        shield= 100,
        maxshield= 100):
        super().__init__(window, size, position, colors, border_radius)
        self.damage = 60
        self.shield= shield
        self.maxshield= maxshield

    async def takeDamage(self, damage):
        self.shield -= damage
        

    async def draw(self, objects = None):
        ratio = self.shield/self.maxshield
        self.size = [self.size[0] * ratio, 20]
        self.bar = pg.draw.rect(
                self.window,
                self.colors[self.fill_index],
                self.pos + self.size,
                border_radius=self.border_radius
            )    
    

