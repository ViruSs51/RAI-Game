import pygame as pg


class Scene:

    def __init__(self, window: pg.Surface, window_size: str|list[int]|tuple[int], config: dict):
        self._window = window
        self._w_size = window_size
        self.config = config

    async def loader(self):
        '''
        Se indica toate obiectele si logica pe scena
        '''

        pg.display.update()