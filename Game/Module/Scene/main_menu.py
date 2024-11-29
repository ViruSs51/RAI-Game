from pygame import Surface
from .scene import Scene


class MainMenu(Scene):

    def __init__(self, window: Surface):
        super().__init__(window=window)

    async def loader(self):
        self._window.fill('blue')