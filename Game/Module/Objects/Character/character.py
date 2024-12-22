import pygame as pg
from ...Objects.objects import Object
from ..animation import Animation


class Character(Object):

    def __init__(
        self,
        window: pg.Surface,
        size: list[int],
        position: list[int],
        images_url: list[str],
    ):
        self.character: pg.Rect
        self.perspective: int = 0
        self.type_animation: int = 0
        self.main_speed = 0.1
        self.speed = self.main_speed
        self.running_speed = 0.2

        super().__init__(
            window, size, position, colors=None, images_url=images_url, border_radius=-1
        )

        self.press_w = 0
        self.press_s = 0
        self.press_d = 0
        self.press_a = 0
        self.press_shift = 0

        self.toUp = lambda: self.pos[1] - self.speed
        self.toRight = lambda: self.pos[0] + self.speed 
        self.toDown = lambda: self.pos[1] + self.speed
        self.toLeft = lambda: self.pos[0] - self.speed

        self.window_size = window.get_size()

        self.main_pos = self.pos
        self.animation = Animation(
            window=window,
            size=self.size,
            position=self.pos,
            images_url=images_url,
            delay=0.15,
        )

    async def draw(self, objects: list[Object]=None):
        await self.oneStart()
        await super().draw(objects=objects)

    async def Animated(self):
        await self.animation.draw(
            perspective=self.perspective + 4 * self.type_animation
        )

    async def control(self, with_controller: bool=False):
        if with_controller:
            self.press_w = await self.controller.getPressed("w")
            self.press_s = await self.controller.getPressed("s")
            self.press_d = await self.controller.getPressed("d")
            self.press_a = await self.controller.getPressed("a")
            self.press_shift = await self.controller.getPressed("shift")
        self.not_action = set((self.press_w, self.press_s, self.press_d, self.press_a)) == {0}

        if self.press_shift and not self.not_action:
            self.type_animation = 2
            self.speed = self.running_speed

        else:
            self.speed = self.main_speed

        if self.press_w and self.can_move_to_up:
            self.pos[1] = self.toUp()
            self.perspective = 0
            self.type_animation = 1

        elif self.press_s and self.can_move_to_down:
            self.pos[1] = self.toDown()
            self.perspective = 2
            self.type_animation = 1

        if self.press_d and self.can_move_to_right:
            self.pos[0] = self.toRight()
            self.perspective = 1
            self.type_animation = 1

        elif self.press_a and self.can_move_to_left:
            self.pos[0] = self.toLeft()
            self.perspective = 3
            self.type_animation = 1

        if self.not_action:
            self.type_animation = 0

    async def processing(self, *args, **kwargs):
        await self.control(*args, **kwargs)