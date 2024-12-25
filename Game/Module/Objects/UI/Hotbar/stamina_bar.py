import pygame as pg
from .hotbar import Hotbar
import time, threading


class StaminaBar(Hotbar):
    def __init__(
        self,
        window: pg.Surface,
        size: list[int] = [300, 20],
        position: list[int] = [0, 0],
        colors: list[list[int] | str] = [(255, 234, 0), (255, 234, 0), (255, 234, 0)],
        border_radius: int = -1,
        stamina=100,
        max_stamina=100,
    ):
        super().__init__(window, size, position, colors, border_radius)
        self.stamina = stamina
        self.max_stamina = max_stamina

    async def updateStamina(self, stamina: float):
        self.stamina = stamina

    async def draw(self, objects=None):
        ratio = self.stamina / self.max_stamina
        size = [self.size[0] * ratio, 20]
        self.bar = pg.draw.rect(
            self.window,
            self.colors[self.fill_index],
            self.pos + size,
            border_radius=self.border_radius,
        )
