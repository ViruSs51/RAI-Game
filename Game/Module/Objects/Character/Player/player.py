import pygame as pg

from ..character import Character
from ...Controller.controller import Controller
from ...objects import Object


class Player(Character):
    def __init__(
        self,
        window: pg.Surface,
        size: list[int],
        position: list[int],
        images_url: list[str],
        max_life: int = 10,
        speed: float = 0.35,
        running_speed: float = 0.8,
        special_sizes: list[int] = None,
        attack_range: list[int] = None,
        damage: float = 1,
        knockback: dict = None,
        stamina: int = 4,
    ):
        super().__init__(
            window,
            size,
            position,
            images_url,
            ctype="player",
            max_life=max_life,
            speed=speed,
            running_speed=running_speed,
            special_sizes=special_sizes,
            attack_range=attack_range,
            damage=damage,
            knockback=knockback,
            stamina=stamina,
        )

        self.collider = True
        self.player_border_distance = (self.window_size[0] / 4, self.window_size[1] / 4)

        self.verifyObjectUp = lambda: (
            False
            if self.player_border_distance[1] + self.speed <= self.pos[1]
            else True
        )
        self.verifyObjectRight = lambda: (
            False
            if self.pos[0]
            <= self.window_size[0] - self.player_border_distance[0] - self.speed
            else True
        )
        self.verifyObjectDown = lambda: (
            False
            if self.pos[1]
            <= self.window_size[1] - self.player_border_distance[1] - self.speed
            else True
        )
        self.verifyObjectLeft = lambda: (
            False
            if self.player_border_distance[0] + self.speed <= self.pos[0]
            else True
        )

        self.verifyUp = lambda: (
            True if self.player_border_distance[1] <= self.pos[1] else False
        )
        self.verifyRight = lambda: (
            True
            if self.pos[0] <= self.window_size[0] - self.player_border_distance[0]
            else False
        )
        self.verifyDown = lambda: (
            True
            if self.pos[1] <= self.window_size[1] - self.player_border_distance[1]
            else False
        )
        self.verifyLeft = lambda: (
            True if self.player_border_distance[0] <= self.pos[0] else False
        )

        self.toUp = lambda: (
            self.pos[1] - self.speed
            if self.verifyUp()
            else self.player_border_distance[1] + 0.1
        )
        self.toRight = lambda: (
            self.pos[0] + self.speed
            if self.verifyRight()
            else self.window_size[0] - self.player_border_distance[0] - 0.1
        )
        self.toDown = lambda: (
            self.pos[1] + self.speed
            if self.verifyDown()
            else self.window_size[1] - self.player_border_distance[1] - 0.1
        )
        self.toLeft = lambda: (
            self.pos[0] - self.speed
            if self.verifyLeft()
            else self.player_border_distance[0] + 0.1
        )

        self.controller = Controller(self.window)
        self.monster_kills = 0

    async def draw(self, objects: list[Object] = None):
        self.character = await self.Animated()
        if not self.start:
            await self.processing(True)
        await super().draw(objects=objects)
