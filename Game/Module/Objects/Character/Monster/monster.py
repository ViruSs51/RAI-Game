from pygame import Surface
from ..character import Character
from ...objects import Object


class Monster(Character):
    def __init__(self, window: Surface, size: list[int], position: list[int], images_url: list[str], speed: float=0.32, run_speed: float=0.52, max_life: int=10):
        super().__init__(window, size, position, images_url, ctype='monster', max_life=max_life)

        self.collider = True
        self.main_speed = speed
        self.speed = self.main_speed
        self.running_speed = run_speed

    async def draw(self, objects: list[Object]=None):
        self.character = await self.Animated()
        await self.processing()
        await super().draw(objects=objects)