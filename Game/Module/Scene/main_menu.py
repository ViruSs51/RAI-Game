from pygame import Surface
from .scene import Scene
from ..Objects.UI import button


class MainMenu(Scene):

    def __init__(self, window: Surface, window_size: str|list[int]|tuple[int]):
        super().__init__(window=window, window_size=window_size)

    async def loader(self):
        ...