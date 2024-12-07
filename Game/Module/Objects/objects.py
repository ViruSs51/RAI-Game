from __future__ import annotations
import pygame as pg


class Object:
    elements: list[Object] = []

    def __init__(self, window: pg.Surface, size: list[int], position: list[int], colors: list[list[int]|str], images_url: list[str]=None, border_radius: int=-1):
        self.window = window
        self.size = size
        self.pos = position
        self.colors = colors
        self.images_url = images_url
        self.border_radius = border_radius
        
        self.fill_index = 0


    async def draw(self):
        for e in self.elements:
            await e.draw()
        
    async def setImages(self) -> list:
        if not self.images_url:
            return None

        images = [
            pg.image.load(self.images_url[0]),
            pg.image.load(self.images_url[1]),
            pg.image.load(self.images_url[2]),
        ]   

        resized_images = []
        for img in images:
            resized_images.append(
                pg.transform.scale(img, self.size)
            )

        self.fill_image = resized_images[0]

        return resized_images