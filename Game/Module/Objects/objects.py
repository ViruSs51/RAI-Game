from __future__ import annotations
import pygame as pg


class Object:
    def __init__(
        self,
        window: pg.Surface,
        size: list[int],
        position: list[int],
        colors: list[list[int] | str],
        images_url: list[str] = None,
        border_radius: int = -1,
    ):
        self.start = True
        self.fill_index = 0
        self.fill_image = None
        self.window = window
        self.size = size
        self.pos = position
        self.colors = colors
        self.images_url = images_url
        self.border_radius = border_radius

    async def oneStart(self):
        if self.start:
            self.start = False

    async def draw(self): ...

    async def setImages(self, new_images: list = None) -> list:
        if not self.images_url:
            return None

        images = [
            pg.image.load(i)
            for i in (self.images_url if not new_images else new_images)
        ]

        resized_images = []
        for img in images:
            resized_images.append(pg.transform.scale(img, self.size))

        if not new_images:
            self.fill_image = resized_images[0]

        return resized_images
