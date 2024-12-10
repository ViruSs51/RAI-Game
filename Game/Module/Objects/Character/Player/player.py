import pygame as pg

from ..character import Character


class Player(Character):
    def __init__(self, window: pg.Surface, size: list[int], position: list[int], images_url: list[str]):
        super().__init__(window, size, position, images_url)

    async def draw(self):
        await super().draw()

        self.character = await self.upAnimation()