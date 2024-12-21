import pygame as pg
from ...Objects.objects import Object
from ..animation import Animation


class Character(Object):
    character: pg.Rect
    perspective: int = 0
    type_animation: int = 0

    def __init__(self, window: pg.Surface, size: list[int], position: list[int], images_url: list[str]):
        super().__init__(window, size, position, colors=None, images_url=images_url, border_radius=-1)

        self.animation = Animation(
            window=window,
            size=self.size,
            position=self.pos,
            images_url=images_url,
            delay=0.15
        )

    async def draw(self):
        await self.oneStart()

    async def standAnimation(self):
        await self.animation.draw(perspective=self.perspective+4*self.type_animation)
    