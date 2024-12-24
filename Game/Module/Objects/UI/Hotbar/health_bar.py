import pygame as pg 
from .hotbar import Hotbar
import time, threading


class HealthBar(Hotbar):
    def __init__(self,
        window: pg.Surface,
        size: list[int] = [300, 20],
        position: list[int] = [0, 0],
        colors: list[list[int] | str] = [(255,44,44),(255,44,44), (255,44,44)],
        border_radius: int = -1,
        hp = 10,
        maxhp = 10):
        super().__init__(window, size, position, colors, border_radius)
        self.damage = 60
        self.hp= hp
        self.maxhp = maxhp        

    def damageTaken(self, damage):
        
        time.sleep(20)
        self.hp -= damage

        

    async def draw(self, objects = None):
        ratio = self.hp /self.maxhp
        self.size = [self.size[0] * ratio, 20]
        self.bar = pg.draw.rect(
                self.window,
                self.colors[self.fill_index],
                self.pos + self.size,
                border_radius=self.border_radius,
            )    
    

