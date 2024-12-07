import pygame as pg
from ...objects import Object
from ...UI import text, button


class GameplayInterface(Object):
    def __init__(self, window: pg.Surface, size: list[int], colors: list[list[int] | str]=None, position: list[int]=[0,0], images_url: list[str] = None):
        super().__init__(window, size, position, colors, images_url)

        self.elements.append(
            button.Button(
                self.window, 
                self.size, 
                position=[
                    position[0]+100,
                    position[1]+100
                ],
                images_url=[
                    '../../../../../Game Assets/objects/ui_1/button2-vibration off.png',
                    '../../../../../Game Assets/objects/ui_1/button2-vibration off.png',
                    '../../../../../Game Assets/objects/ui_1/button2-vibration om.png'
                ]
            )
        )

    async def draw(self):
        await super().draw()