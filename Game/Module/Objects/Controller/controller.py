import pygame as pg

from ..objects import Object
from ...Objects import Controller


class Controller(Object):
    keys = Controller.keys

    def __init__(self, window: pg.Surface):
        super().__init__(window, None, None, None)

    async def getPressed(self, key: str | int):
        return pg.key.get_pressed()[self.keys[key] if type(key) is str else key]

    async def getClick(self, button: int, click_range: list[list] = None):
        """
        button - se indica index-ul la buton, stang, central, drepta
        """
        mouse_x, mouse_y = pg.mouse.get_pos()
        buttons_status = pg.mouse.get_pressed()

        return (buttons_status[button] and not click_range) or (
            buttons_status[button]
            and click_range[0][0] < mouse_x < click_range[0][1]
            and click_range[1][0] < mouse_y < click_range[1][1]
        )
