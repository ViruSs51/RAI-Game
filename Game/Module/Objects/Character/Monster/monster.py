from pygame import Surface
from ..character import Character
from ...objects import Object
from time import time


class Monster(Character):
    def __init__(self, window: Surface, size: list[int], position: list[int], images_url: list[str], max_life: int=10, speed: float=0.32, running_speed: float=0.52, special_sizes: list[int]=None, attack_range: list[int]=None, damage: float=1, knockback: dict=None):
        super().__init__(window, size, position, images_url, ctype='monster', max_life=max_life, speed=speed, running_speed=running_speed, special_sizes=special_sizes, attack_range=attack_range, damage=damage, knockback=knockback)
        self.collider = True

    async def draw(self, objects: list[Object]=None):
        if not self.dead:
            self.click_left_button = True
            self.press_d = True
            self.press_shift = True
            self.character = await self.Animated()
            if not self.start: await self.processing()
            await super().draw(objects=objects)