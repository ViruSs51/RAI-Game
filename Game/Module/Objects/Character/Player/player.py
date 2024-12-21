import pygame as pg

from ..character import Character
from ...Controller.controller import Controller


class Player(Character):
    def __init__(
        self,
        window: pg.Surface,
        size: list[int],
        position: list[int],
        images_url: list[str],
    ):
        super().__init__(window, size, position, images_url)

        self.main_speed = 0.35
        self.speed = self.main_speed
        self.running_speed = 0.55

        self.controller = Controller()

    async def draw(self):
        await super().draw()

        self.character = await self.Animated()
        await self.control()

    async def control(self):
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

        if self.press_w:
            self.pos[1] = self.toUp()
            self.perspective = 0
            self.type_animation = 1

        elif self.press_s:
            self.pos[1] = self.toDown()
            self.perspective = 2
            self.type_animation = 1

        if self.press_d:
            self.pos[0] = self.toRight()
            self.perspective = 1
            self.type_animation = 1

        elif self.press_a:
            self.pos[0] = self.toLeft()
            self.perspective = 3
            self.type_animation = 1

        if self.not_action:
            self.type_animation = 0
