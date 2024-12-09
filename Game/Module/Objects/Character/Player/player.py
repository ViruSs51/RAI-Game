import pygame as pg

from Game.Module.Scene.scene import Scene
from ..character import Character


class Player(Character):
    def __init__(self, window: pg.Surface, scene: Scene, size: list[int], position: list[int], images_url: list[str]):
        super().__init__(window, scene, size, position, images_url)

    async def draw(self):
        await super().draw()

        self.character = await self.upAnimation()