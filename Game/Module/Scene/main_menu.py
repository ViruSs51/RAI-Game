from pygame import Surface
from .scene import Scene
from ..Objects.UI import button


class MainMenu(Scene):

    def __init__(self, window: Surface, window_size: str|list[int]|tuple[int], config: dict):
        super().__init__(window=window, window_size=window_size, config=config)

    async def loader(self):
        ...