from pygame import Surface
from ..scene import Scene
from ...Objects.UI.Interface import gameplay_ui

class Room(Scene):
    def __init__(self, window: Surface, window_size: str | list[int] | tuple[int]):
        super().__init__(window, window_size)

        self.gameplay_interface = gameplay_ui.GameplayInterface(
            window=window,
            size=window_size,
            colors=None
        )

    async def loader(self):
        self._window.fill('gray')

        self.gameplay_interface.draw()