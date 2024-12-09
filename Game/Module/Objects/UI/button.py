from ..objects import Object
from .text import Text

import pygame as pg
from types import FunctionType


class Button(Object):
    pressed = False
    pressed_time = 0
    text = None

    def __init__(self, window: pg.Surface, size: list[int]=[50, 50], position: list[int]=[0, 0], colors: list[list[int]|str]=['white', 'gray', 'black'], text_position: list[int]=None, text: str=None, font: str=None, font_size: int=36, text_colors: list[list[int]|str]=['black', 'black', 'white'], text_background_colors: list[list[int]|str]=None, images_url: list[str]=None, border_radius: int=-1, function: FunctionType=None):
        super().__init__(window, size, position, colors, images_url, border_radius)

        self.function = function

        if text:
            self.text = Text(self.window, text_position, text, font, font_size, text_colors, text_background_colors)
            self.text.updatePosition(self.getCenterForText())

    def getCenterForText(self):
        return (self.pos[0]+self.size[0]/2-self.text.text_rect.width/2, self.pos[1]+self.size[1]/2-self.text.text_rect.height/2)


    async def draw(self):
        if self.start: self.images = await self.setImages()
        await super().draw()

        if self.images:
            self.button = self.window.blit(self.images[self.fill_index], self.pos)
        else:
            self.button = pg.draw.rect(self.window, self.colors[self.fill_index], self.pos+self.size, border_radius=self.border_radius)

        if self.text: await self.text.draw()


        is_hover = await self.hover()
        is_press = await self.press()

        if not is_hover and not is_press:
            self.fill_index = 0
            
            if self.text: await self.text.updateFill(self.fill_index)

        await self.oneStart()

    async def press(self) -> bool:
        mouse_x, mouse_y = pg.mouse.get_pos()
        left_button_status = pg.mouse.get_pressed()[0]

        if self.function: await self.function()

        if left_button_status and self.button.collidepoint(mouse_x, mouse_y):
            if not self.pressed:
                self.pressed_time = 0

            self.pressed_time += 1
            self.pressed = True

            self.fill_index = 2

            if self.text: await self.text.updateFill(self.fill_index)

            return True

        else:
            self.pressed = False

            return False

    async def hover(self) -> bool:
        mouse_x, mouse_y = pg.mouse.get_pos()

        if self.button.collidepoint(mouse_x, mouse_y):
            self.fill_index = 1

            if self.text: await self.text.updateFill(self.fill_index)

            return True

        else:
            return False
        