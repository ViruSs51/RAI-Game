import pygame as pg
from ..scene import Scene
from ...Objects.UI.Interface import gameplay_ui

class Room(Scene):
    def __init__(self, window: pg.Surface, window_size: str | list[int] | tuple[int]):
        super().__init__(window, window_size)

        self.gameplay_interface = gameplay_ui.GameplayInterface(
            window=window,
            size=window_size,
            colors=None
        )

    async def loader(self):
        await self.gameplay_interface.draw()
        
        await super().loader()