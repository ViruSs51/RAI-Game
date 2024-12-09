import pygame as pg
from ...Room.room import Room
from ....Objects.Character.Player.player import Player

from ....Objects.UI.button import Button


class ControlRoom(Room):
    def __init__(self, window: pg.Surface, window_size: str | list[int] | tuple[int], config: dict):
        super().__init__(window=window, window_size=window_size, config=config)

        self.player = Player(
            window=window, 
            scene=self, 
            size=self.config['characters']['player']['size'], 
            position=self.config['characters']['player']['position'],
            images_url=self.config['characters']['player']['samples']
        )

    async def loader(self):
        await self.player.draw()
        
        await super().loader()