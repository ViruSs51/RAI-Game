import pygame as pg
from ...Objects.objects import Object
from ..animation import Animation
from ...Scene.scene import Scene


class Character(Object):
    character: pg.Rect

    def __init__(self, window: pg.Surface, scene: Scene, size: list[int], position: list[int], images_url: list[str]):
        super().__init__(window, size, position, colors=None, images_url=images_url, border_radius=-1)

        self.scene = scene
        self.animation = Animation(
            window=window,
            size=self.size,
            position=self.pos,
            images_url=images_url,
            delay=0.15
        )

    async def draw(self):
        await self.oneStart()

    async def upAnimation(self):
        await self.animation.draw(perspective=0)

    async def rightAnimation(self):
        await self.animation.draw(perspective=1)

    async def downAnimation(self):
        await self.animation.draw(perspective=2)

    async def leftAnimation(self):
        await self.animation.draw(perspective=3)
    