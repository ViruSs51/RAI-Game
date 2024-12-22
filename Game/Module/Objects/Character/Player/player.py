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
    ):
        super().__init__(window, size, position, images_url)

        self.collider = True
        self.player_border_distance = (self.window_size[0] / 4, self.window_size[1] / 4)

        self.verifyObjectUp = lambda: False if self.player_border_distance[1] + self.speed <= self.pos[1] else True
        self.verifyObjectRight = lambda: False if self.pos[0] <= self.window_size[0] - self.player_border_distance[0] - self.speed else True
        self.verifyObjectDown = lambda: False if self.pos[1] <= self.window_size[1] - self.player_border_distance[1] - self.speed else True
        self.verifyObjectLeft = lambda: False if self.player_border_distance[0] + self.speed <= self.pos[0] else True

        self.verifyUp = lambda: True if self.player_border_distance[1] <= self.pos[1] else False
        self.verifyRight = lambda: True if self.pos[0] <= self.window_size[0] - self.player_border_distance[0] else False
        self.verifyDown = lambda: True if self.pos[1] <= self.window_size[1] - self.player_border_distance[1] else False
        self.verifyLeft = lambda: True if self.player_border_distance[0] <= self.pos[0] else False

        self.toUp = lambda: self.pos[1] - self.speed if self.verifyUp() else self.player_border_distance[1] + self.speed
        self.toRight = lambda: self.pos[0] + self.speed if self.verifyRight() else self.window_size[0] - self.player_border_distance[0] - self.speed
        self.toDown = lambda: self.pos[1] + self.speed if self.verifyDown() else self.window_size[1] - self.player_border_distance[1] - self.speed
        self.toLeft = lambda: self.pos[0] - self.speed if self.verifyLeft() else self.player_border_distance[0] + self.speed

        self.main_speed = 0.35
        self.speed = self.main_speed
        self.running_speed = 0.55

        self.controller = Controller(self.window)

    async def draw(self, objects: list[Object]=None):
        self.character = await self.Animated()
        await self.processing(True)
        await super().draw(objects=objects)
