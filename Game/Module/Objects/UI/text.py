import pygame as pg


class Text:
    text_font = None
    text_render = None
    text_rect = None
    fill_color = 0
    fill_background_color = 0

    def __init__(self, window: pg.Surface, position: list[int]=[0, 0], text: str=None, font: str=None, font_size: int=36, text_colors: list[list[int]|str]=['black', 'black', 'white'], background_colors: list[list[int]|str]=None):
        self.window = window
        self.position = position
        self.text = text
        self.font = font
        self.font_size = font_size
        self.text_colors = text_colors
        self.background_color = background_colors

        self.init()

    def init(self):
        self.text_font = pg.font.Font(self.font, self.font_size)
        self.text_render = self.text_font.render(self.text, True, self.text_colors[self.fill_color], self.background_color[self.fill_background_color] if self.background_color else None)
        self.text_rect = self.text_render.get_rect()

    async def show(self):
        self.window.blit(self.text_render, self.position)

        pg.display.update()
    
    async def updateFill(self, fill_index: int):
        self.fill_color = fill_index
        self.fill_background_color = fill_index

        self.init()

    async def updatePosition(self, position: list[int]):
        self.position = position

        self.init()
