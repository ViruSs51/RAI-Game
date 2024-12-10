import pygame as pg
from ..scene import Scene
from ...Objects.UI.Interface import gameplay_ui
from ...Objects.Character.Player.player import Player

class Room(Scene):
    def __init__(self, window: pg.Surface, window_size: str | list[int] | tuple[int], config: dict, player: Player):
        super().__init__(window=window, window_size=window_size, config=config, player=player)

        self.gameplay_interface = gameplay_ui.GameplayInterface(
            window=window,
            size=window_size,
            colors=None
        )

    async def loader(self):
        await self.gameplay_interface.draw()
        
        await super().loader()