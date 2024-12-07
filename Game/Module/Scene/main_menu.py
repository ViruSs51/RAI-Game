from pygame import Surface
from .scene import Scene
from ..Objects.UI import button


class MainMenu(Scene):

    def __init__(self, window: Surface):
        super().__init__(window=window)

        
        self.btn1 = button.Button(
            window=self._window,
            size=(200, 50),
            position=(100, 100),
            text_position=(125, 110),
            text='Hello World'
        )

    async def loader(self):
        self._window.fill('blue')

        await self.btn1.draw()