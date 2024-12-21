import pygame as pg
from ...Room.room import Room
from ....Objects.Character.Player.player import Player

from ....Objects.UI.button import Button


class ControlRoom(Room):
    def __init__(
        self,
        window: pg.Surface,
        window_size: str | list[int] | tuple[int],
        config: dict,
        player: Player,
    ):
        super().__init__(
            window=window, window_size=window_size, config=config, player=player
        )

        self.addObject(self._player)

    async def loader(self):
        return await super().loader()
