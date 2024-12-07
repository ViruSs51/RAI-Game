import pygame as pg
from ...objects import Object
from ...UI import text, button


class GameplayInterface(Object):
    def __init__(self, window: pg.Surface, size: list[int], colors: list[list[int] | str]=None, position: list[int]=[0,0], images_url: list[str] = None):
        super().__init__(window, size, position, colors, images_url)

        self.elements.append(
            #Pause button
            button.Button(
                self.window, 
                size=[50, 50], 
                position=[
                    position[0]+10,
                    position[1]+10
                ],
                images_url=[
                    'Game Assets/objects/ui_1/button-pause.png',
                    'Game Assets/objects/ui_1/button-pause.png',
                    'Game Assets/objects/ui_1/button-pause.png'
                ]
            )
        )

    async def draw(self):
        await self.drawElemnts()