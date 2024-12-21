from ..Objects.objects import Object

from time import time
import pygame as pg
import asyncio


class Animation(Object):
    current_delay = 0
    max_delay = 0
    images = []

    def __init__(
        self,
        window: pg.Surface,
        size: list[int],
        position: list[int],
        images_url: list[str],
        colors: list[list[int] | str] = None,
        delay: int = 100,
    ):
        self.all_images = images_url
        super().__init__(window, size, position, colors, images_url[0], -1)

        self.d = delay
        self.max_dalay = time() + self.d

    async def draw(self, perspective: int = 0):
        if self.start:
            for i, pi in enumerate(self.all_images):
                self.images.append(
                    await self.setImages(new_images=pi)
                    if i != 0
                    else await self.setImages()
                )

        await self.delay(perspective=perspective)
        self.window.blit(self.fill_image, self.pos)

        await self.oneStart()

    async def delay(self, perspective: int):
        if time() >= self.max_dalay:
            self.fill_index += 1
            if self.fill_index >= len(self.images[perspective]):
                self.fill_index = 0

            self.fill_image = self.images[perspective][self.fill_index]
            self.max_dalay = time() + self.d
