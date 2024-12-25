import pygame as pg
from ..scene import Scene
from ...Objects.Character.Player.player import Player


class Room(Scene):
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

    async def loader(self):
        return await super().loader()

    async def movementPlayer(self):
        if (
            self._player.verifyObjectUp()
            or self._player.verifyObjectRight()
            or self._player.verifyObjectDown()
            or self._player.verifyObjectLeft()
        ):
            if self._player.press_w and self._player.can_move_to_up:
                self.floor_pos[1] += self._player.speed
                for o in self.objects:
                    if type(o) is not Player:
                        o.pos[1] += self._player.speed

            elif self._player.press_s and self._player.can_move_to_down:
                self.floor_pos[1] -= self._player.speed
                for o in self.objects:
                    if type(o) is not Player:
                        o.pos[1] -= self._player.speed

            if self._player.press_d and self._player.can_move_to_right:
                self.floor_pos[0] -= self._player.speed
                for o in self.objects:
                    if type(o) is not Player:
                        o.pos[0] -= self._player.speed

            elif self._player.press_a and self._player.can_move_to_left:
                self.floor_pos[0] += self._player.speed
                for o in self.objects:
                    if type(o) is not Player:
                        o.pos[0] += self._player.speed

            if (
                self.floor_pos[1] <= self.floor_initial_pos[1] - self.floor_size[1]
                or self.floor_pos[1] >= self.floor_initial_pos[1] + self.floor_size[1]
            ):
                self.floor_pos[1] = self.floor_initial_pos[1]

            if (
                self.floor_pos[0] <= self.floor_initial_pos[0] - self.floor_size[0]
                or self.floor_pos[0] >= self.floor_initial_pos[0] + self.floor_size[0]
            ):
                self.floor_pos[0] = self.floor_initial_pos[0]
