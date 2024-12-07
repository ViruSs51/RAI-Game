import pygame as pg
from ...Objects.objects import Object
from ...Scene.scene import Scene


class Character(Object):
    def __init__(self, window: pg.Surface, scene: Scene, size: list[int], position: list[int], images_url: list[str]):
        super().__init__(window, size, position, colors=None, images_url=images_url, border_radius=-1)

        self.scene = scene

    async def draw(self):
        if self.start: self.images = await self.setImages()
        self.character = self.window.blit(self.images[self.fill_image], self.size)
    
        await self.oneStart()
        pg.display.update()