import pygame as pg
from ..Objects.objects import Object


class Frame(Object):
    def __init__(
        self,
        window: pg.Surface,
        size: list[int],
        position: list[int],
        colors: list[list[int] | str],
        images_url: list[str] = None,
        border_radius: int = -1,
    ):
        super().__init__(window, size, position, colors, images_url, border_radius)

    async def draw(self):
        if self.start:
            await self.setImages()
            
        self.window.blit(self.fill_image, self.pos)

        await self.oneStart()