import pygame as pg
from ...Objects.objects import Object
from ..animation import Animation


class Character(Object):
    character: pg.Rect
    perspective: int = 0
    type_animation: int = 0
    main_speed = 0.1
    speed = main_speed
    running_speed = 0.2

    def __init__(
        self,
        window: pg.Surface,
        size: list[int],
        position: list[int],
        images_url: list[str],
    ):
        super().__init__(
            window, size, position, colors=None, images_url=images_url, border_radius=-1
        )

        self.window_size = window.get_size()
        self.player_border_distance = (self.window_size[0] / 4, self.window_size[1] / 4)

        self.verifyFloorUp = lambda: False if self.player_border_distance[1] + self.speed <= self.pos[1] else True
        self.verifyFloorRight = lambda: False if self.pos[0] <= self.window_size[0] - self.player_border_distance[0] - self.speed else True
        self.verifyFloorDown = lambda: False if self.pos[1] <= self.window_size[1] - self.player_border_distance[1] - self.speed else True
        self.verifyFloorLeft = lambda: False if self.player_border_distance[0] + self.speed <= self.pos[0] else True

        self.verifyUp = lambda: True if self.player_border_distance[1] <= self.pos[1] else False
        self.verifyRight = lambda: True if self.pos[0] <= self.window_size[0] - self.player_border_distance[0] else False
        self.verifyDown = lambda: True if self.pos[1] <= self.window_size[1] - self.player_border_distance[1] else False
        self.verifyLeft = lambda: True if self.player_border_distance[0] <= self.pos[0] else False

        self.toUp = lambda: self.pos[1] - self.speed if self.verifyUp() else self.player_border_distance[1] + self.speed
        self.toRight = lambda: self.pos[0] + self.speed if self.verifyRight() else self.window_size[0] - self.player_border_distance[0] - self.speed
        self.toDown = lambda: self.pos[1] + self.speed if self.verifyDown() else self.window_size[1] - self.player_border_distance[1] - self.speed
        self.toLeft = lambda: self.pos[0] - self.speed if self.verifyLeft() else self.player_border_distance[0] + self.speed

        self.main_pos = self.pos
        self.animation = Animation(
            window=window,
            size=self.size,
            position=self.pos,
            images_url=images_url,
            delay=0.15,
        )

    async def draw(self):
        await self.oneStart()

    async def Animated(self):
        await self.animation.draw(
            perspective=self.perspective + 4 * self.type_animation
        )
