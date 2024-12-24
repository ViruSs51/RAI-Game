import pygame as pg
from ..scene import Scene
from ...Objects.Character.Player.player import Player
from ...Objects.UI.health_bar import HealthBar
from ...Objects.UI.shield_bar import ShieldBar
from ...Objects.UI.stamina_bar import StaminaBar

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
        self.loadHotBars()

    
    def loadHotBars(self):
        self.healthBar = HealthBar(window=self._window,position=[self._w_size[0] - 300 - 30,self._w_size[1] - 20 - 30], border_radius=0 )
        self.shieldBar = ShieldBar(window=self._window,position=[self._w_size[0] - 300 - 30,self._w_size[1] - 20 - 30 * 2], border_radius=0 )
        self.staminaBar = StaminaBar(window=self._window,position=[self._w_size[0] - 300 - 30,self._w_size[1] - 20 - 30 * 3], border_radius=0 )

    async def loader(self):
        await self.healthBar.draw()
        await self.shieldBar.draw()
        await self.staminaBar.draw()
        return await super().loader()

    async def movementPlayer(self):
        if self._player.verifyObjectUp() or self._player.verifyObjectRight() or self._player.verifyObjectDown() or self._player.verifyObjectLeft():
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

            if self.floor_pos[1] <= self.floor_initial_pos[1] - self.floor_size[1] or self.floor_pos[1] >= self.floor_initial_pos[1] + self.floor_size[1]:
                self.floor_pos[1] = self.floor_initial_pos[1]

            if self.floor_pos[0] <= self.floor_initial_pos[0] - self.floor_size[0] or self.floor_pos[0] >= self.floor_initial_pos[0] + self.floor_size[0]:
                self.floor_pos[0] = self.floor_initial_pos[0]
