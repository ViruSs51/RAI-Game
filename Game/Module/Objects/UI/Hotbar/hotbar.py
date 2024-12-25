from ...objects import Object
import pygame as pg


class Hotbar(Object):
    def __init__(
        self,
        window: pg.Surface,
        size: list[int] = [300, 20],
        position: list[int] = [0, 0],
        colors: list[list[int] | str] = ["white", "gray", "black"],
        border_radius: int = -1,
    ):
        super().__init__(window, size, position, colors, border_radius)

    async def draw(self, objects: list[Object] = None):
        await super().draw()

        self.bar = pg.draw.rect(
            self.window,
            self.colors[self.fill_index],
            self.pos + self.size,
            border_radius=self.border_radius,
        )
